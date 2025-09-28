# alpha_analytical/digit_reduction/analyzer_v2/pipeline.py
from pathlib import Path
import yaml
from typing import Dict, Any, List, Optional
from .io import load_training_json, training_dir_for_state, analyzer_out_dir
from .features import compute_item_features
from .pivot import cross_section_pivot, own_vs_combined, set_memory
from .score import score_row
from .writers import write_csv, write_json
from .vtrac_index import vtrac_set, try_load_hot_families_from_predictions, derive_hot_families_from_dr

def run(state: str, analysis_root: Path) -> Dict[str, Any]:
    tdir = training_dir_for_state(analysis_root, state)
    jpath = next(tdir.glob(f"{state}*digit_reduction_logs.json"))
    items = load_training_json(jpath)

    # load config
    cfg = yaml.safe_load((Path(__file__).parent/"config.yml").read_text(encoding="utf-8"))
    W = cfg["weights"]; P = cfg.get("penalties", {}); C = cfg.get("caps", {})
    K = cfg["thresholds"]["early_step_k"]
    vpred_dir = Path(cfg.get("paths", {}).get("vtrac_predictions_dir", "data/outputs/predictions"))

    # per-item features
    per_item_rows: List[Dict[str,Any]] = []
    for it in items:
        feats = compute_item_features(it, early_k=K)
        row = {
          "state": it.key.state, "area": it.key.area, "section": it.key.section,
          "set": it.key.set, "draw": it.key.draw, "col": it.key.col,
          "method": it.key.method, "mode": it.key.mode, **feats
        }
        # add vtrac family from final_3 canon (if available)
        sig = row.get("tail.final_len", 0)
        # we already recorded many details in feats; use first-3 value step core when available
        # compute v-family from the earliest ≤3-value snapshot we found
        # 'compute_item_features' records the canonical first-3 string via helper; reconstruct:
        # NOTE: if you add the exact core string to features later, replace this logic with it directly.
        final_sig = it.steps[-1].value if it.steps else ""
        row["final_3canon"] = "".join(sorted(ch for ch in str(final_sig) if ch.isdigit()))
        row["vtrac.set"] = vtrac_set(row["final_3canon"]) if row["final_3canon"] else ""
        per_item_rows.append(row)

    # pivots
    sec = cross_section_pivot(items)
    mod = own_vs_combined(items)
    mem = set_memory(items)

    # merge pivots
    def k1(r): return (r["state"], r["area"], r["set"], r["draw"], r["col"], r["method"], r["mode"])
    def k2(r): return (r["state"], r["area"], r["section"], r["set"], r["draw"], r["col"], r["method"])
    for r in per_item_rows:
        r.update(sec.get(k1(r), {}))
        r.update(mem.get((r["state"], r["area"], r["section"], r["col"], r["method"], r["mode"]), {}))
        r.update(mod.get(k2(r), {}))

    # ---------------- V‑TRAC synergy (hot families) ----------------
    # 1) prefer predictions JSON if present & mappable
    hot_spec = try_load_hot_families_from_predictions(state, vpred_dir)
    if hot_spec is None:
        # 2) derive from DR rows (graceful fallback)
        hot_spec = derive_hot_families_from_dr(per_item_rows, min_methods=2, prefer_section="Combined", top_k=5)

    # mark v_hot per row (0..1)
    fam_strength = hot_spec.detail or {f:1.0 for f in hot_spec.families}
    def _v_hot(r):
        fam = r.get("vtrac.set","")
        return float(fam_strength.get(fam, 0.0))
    for r in per_item_rows:
        r["vtrac.v_hot"] = _v_hot(r)
        r["vtrac.hot_source"] = hot_spec.source

    # scores
    for r in per_item_rows:
        r["score"] = score_row(r, W, P, C)

    outdir = analyzer_out_dir(analysis_root, state)
    write_csv(outdir / f"{state}_analyzer_v2_per_item.csv", per_item_rows)

    # Compact top candidates (A/B board style)
    board = sorted(
        (r for r in per_item_rows if r.get("final_3canon")),
        key=lambda r: (-float(r["score"]), r.get("traj.first3", 99))
    )[:120]  # keep plenty; the UI will slice further
    write_csv(outdir / f"{state}_analyzer_v2_top_candidates.csv", board)

    # meta (config + provenance + V‑TRAC source)
    write_json(outdir / f"{state}_analyzer_v2_meta.json", {
        "config": cfg, "source": str(jpath),
        "vtrac_hot_source": hot_spec.source, "vtrac_hot_families": sorted(hot_spec.families)
    })
    return {"rows": len(per_item_rows), "outdir": str(outdir)}
