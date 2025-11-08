from __future__ import annotations

import csv
import hashlib
import re
import subprocess
from collections import defaultdict
from pathlib import Path
from typing import Any, DefaultDict, Dict, Iterable, List, Optional, Sequence, Set, Tuple

import yaml

from .features import ItemFeature, build_features
from .io import analyzer_out_dir, load_training_json
from .score import score_row
from .scoring import apply_linear_scoring, apply_post_score, attach_lockscore, top_score_key
from .vtrac_index import VHotSpec, derive_hot_families_from_dr, try_load_hot_families_from_predictions, vtrac_set
from .writers import write_artifacts
from .winners_overlay import build_winner_overlay

SectionKey = Tuple[str, str, str, str, str, int, str, str]

FLAG_KIND_ORDER = ("exact", "vtrac", "drop_exact", "drop_vtrac", "family_exact", "family_vtrac")
FLAG_PATH_PATTERN = r"^(?P<stamp>\d{8})_(?P<variant>Combined|Midday|Evening)_winner_flags$"


def _load_config(path: Optional[Path] = None) -> Dict[str, Any]:
    cfg_path = path or (Path(__file__).parent / "config.yml")
    return yaml.safe_load(cfg_path.read_text(encoding="utf-8"))


def _config_hash(path: Path) -> str:
    digest = hashlib.sha256()
    digest.update(path.read_bytes())
    return digest.hexdigest()


def _git_sha() -> str:
    try:
        output = subprocess.check_output(["git", "rev-parse", "HEAD"], stderr=subprocess.DEVNULL)
        return output.decode("utf-8").strip()
    except Exception:
        return "unknown"


def _as_int(value: Any, default: int = 0) -> int:
    try:
        if isinstance(value, str):
            value = value.strip()
            if not value:
                return default
        return int(value)
    except (TypeError, ValueError):
        try:
            return int(float(value))
        except (TypeError, ValueError):
            return default


def _earliest_any(row: Dict[str, Any]) -> Optional[int]:
    candidates = [
        _as_int(row.get(f"earliest_{kind}_step"), -1) for kind in FLAG_KIND_ORDER
    ]
    positives = [step for step in candidates if step >= 0]
    return min(positives) if positives else None


def _section_key(row: Dict[str, Any]) -> SectionKey:
    return (
        str(row.get("state", "")),
        str(row.get("area", "")),
        str(row.get("section", "")),
        str(row.get("set", "")),
        str(row.get("draw", "")),
        _as_int(row.get("col", 0)),
        str(row.get("method", "")),
        str(row.get("mode", "")),
    )


def _load_winner_flags(state: str, analysis_root: Optional[Path]) -> Dict[SectionKey, Dict[str, Any]]:
    base_dir = analyzer_out_dir(state, analysis_root)
    winners_dir = Path(base_dir) / "winners"
    if not winners_dir.exists():
        return {}

    latest: Dict[str, Path] = {}
    pattern = re.compile(FLAG_PATH_PATTERN)  # type: ignore[name-defined]
    for candidate in winners_dir.glob("*_winner_flags.csv"):
        match = pattern.match(candidate.stem)
        if not match:
            continue
        variant = match.group("variant")
        current = latest.get(variant)
        if current is None or candidate.stat().st_mtime > current.stat().st_mtime:
            latest[variant] = candidate

    flags: Dict[SectionKey, Dict[str, Any]] = {}
    for variant, csv_path in latest.items():
        with csv_path.open("r", newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            for row in reader:
                key: SectionKey = (
                    state,
                    str(row.get("area", "")),
                    str(row.get("section", "")),
                    str(row.get("set", "")),
                    str(row.get("draw", "")),
                    _as_int(row.get("col", 0)),
                    str(row.get("method", "")),
                    str(row.get("mode", "")),
                )
                payload = {
                    "dr.win_variant": variant,
                    "dr.win_final_value": str(row.get("dr_win_final_value", "")),
                    "dr.win_drop_digit": str(row.get("dr_win_drop_digit", "")),
                    "dr.win_vtrac_local_index": _as_int(row.get("dr_win_vtrac_local_index", -1)),
                }
                for kind in FLAG_KIND_ORDER:
                    payload[f"dr.win_{kind}"] = _as_int(row.get(f"dr_win_{kind}", 0))
                    payload[f"dr.win_step_{kind}"] = _as_int(row.get(f"dr_win_step_{kind}", -1))
                flags[key] = payload
    return flags


def _aggregate_metrics(entries: List[ItemFeature], config: Dict[str, Any]) -> None:
    ceiling = int(config.get("features", {}).get("variants_step_ceiling", 3))

    cols_map: DefaultDict[Tuple[str, str, str, str, str, str, str, str], Set[int]] = defaultdict(set)
    variant_map: DefaultDict[Tuple[str, str, str, str, int, str, str, str], Set[str]] = defaultdict(set)
    variant_echo_map: DefaultDict[Tuple[str, str, str, str, str, str], Set[str]] = defaultdict(set)
    set_map: DefaultDict[Tuple[str, str, str, str, int, str, str], Set[str]] = defaultdict(set)
    method_map: DefaultDict[Tuple[str, str, str, str, str, int, str], Set[str]] = defaultdict(set)
    cluster_map: DefaultDict[Tuple[str, str, str, str, str], Set[Tuple[str, str, int]]] = defaultdict(set)
    carry_map: DefaultDict[Tuple[str, str, str, str, str], Dict[str, List[int]]] = defaultdict(lambda: defaultdict(list))

    for entry in entries:
        row = entry.row
        earliest = _earliest_any(row)
        row["_earliest_any"] = earliest
        if earliest is None:
            continue
        if earliest <= ceiling:
            cols_key = (row["state"], row["area"], row["section"], row["set"], row["draw"], row["method"], row["mode"], row["family_id"])
            cols_map[cols_key].add(row["col"])

            variant_key = (row["state"], row["area"], row["set"], row["draw"], row["col"], row["method"], row["mode"], row["family_id"])
            variant_map[variant_key].add(row["section"])

            variant_echo_key = (row["state"], row["area"], row["set"], row["draw"], row["family_id"], row["mode"])
            variant_echo_map[variant_echo_key].add(row["section"])

            set_key = (row["state"], row["area"], row["section"], row["draw"], row["col"], row["method"], row["mode"], row["family_id"])
            set_map[set_key].add(row["set"])

            method_key = (row["state"], row["area"], row["section"], row["set"], row["draw"], row["mode"], row["family_id"])
            method_map[method_key].add(row["method"])

            cluster_key = (row["state"], row["area"], row["section"], row["family_id"], row["mode"])
            cluster_map[cluster_key].add((row["set"], row["draw"], row["col"]))

            carry_key = (row["state"], row["area"], row["section"], row["family_id"], row["mode"])
            carry_map[carry_key][row["set"]].append(earliest)

    for entry in entries:
        row = entry.row
        cols_key = (row["state"], row["area"], row["section"], row["set"], row["draw"], row["method"], row["mode"], row["family_id"])
        variant_key = (row["state"], row["area"], row["set"], row["draw"], row["col"], row["method"], row["mode"], row["family_id"])
        variant_echo_key = (row["state"], row["area"], row["set"], row["draw"], row["family_id"], row["mode"])
        set_key = (row["state"], row["area"], row["section"], row["draw"], row["col"], row["method"], row["mode"], row["family_id"])
        method_key = (row["state"], row["area"], row["section"], row["set"], row["draw"], row["mode"], row["family_id"])
        cluster_key = (row["state"], row["area"], row["section"], row["family_id"], row["mode"])
        carry_key = (row["state"], row["area"], row["section"], row["family_id"], row["mode"])

        row["cols_hit"] = len(cols_map.get(cols_key, set()))
        row["variants_hit"] = len(variant_map.get(variant_key, set()))
        row["variant_echo_count"] = len(variant_echo_map.get(variant_echo_key, set()))
        row["set_echo_count"] = len(set_map.get(set_key, set()))
        row["method_consensus"] = len(method_map.get(method_key, set()))
        row["cluster_echo_count"] = len(cluster_map.get(cluster_key, set()))

        carry_sets = carry_map.get(carry_key, {})
        if row["set"] == "Set1" and "Set2" in carry_sets and carry_sets["Set2"]:
            row["recency_carryover"] = int(min(carry_sets["Set2"]) <= ceiling)
        else:
            row["recency_carryover"] = row.get("recency_carryover", 0)

        persistence_exact = _as_int(row.get("persistence_exact"), 0)
        persistence_vtrac = _as_int(row.get("persistence_vtrac"), 0)
        row["box_pair_agree"] = int(max(persistence_exact, persistence_vtrac) >= 2)

        row.pop("_earliest_any", None)


def _top_candidates(rows: List[Dict[str, Any]], cfg: Dict[str, Any]) -> List[Dict[str, Any]]:
    groups: DefaultDict[Tuple[str, str, str, str], List[Dict[str, Any]]] = defaultdict(list)
    for row in rows:
        key = (row["state"], row["section"], row["family_id"], row["mode"])
        groups[key].append(row)

    score_field = top_score_key(cfg, rows)

    board: List[Dict[str, Any]] = []
    for key, members in groups.items():
        best = max(members, key=lambda r: r.get(score_field, r.get("score", 0.0)))
        evidence = [kind for kind in FLAG_KIND_ORDER if _as_int(best.get(f"earliest_{kind}_step"), -1) >= 0]
        steps_summary = ";".join(
            f"{kind}:{_as_int(best.get(f'earliest_{kind}_step'), -1)}" for kind in FLAG_KIND_ORDER
        )
        board_score = float(best.get(score_field, best.get("score", 0.0)) or 0.0)
        board.append(
            {
                "state": key[0],
                "variant": key[1],
                "mode": key[3],
                "family_id": key[2],
                "best_pattern": best.get("pattern", ""),
                "score": board_score,
                "score_baseline": best.get("score", 0.0),
                "score_v2": best.get("score_v2"),
                "final_prob": best.get("final_prob"),
                "lockscore_prob": best.get("lockscore_prob"),
                "boxes_involved": len(members),
                "evidence_tags": ",".join(evidence),
                "steps_summary": steps_summary,
            }
        )
    board.sort(key=lambda row: (-row["score"], -row["boxes_involved"]))
    for idx, row in enumerate(board, start=1):
        row["rank"] = idx
    return board[:200]


def _prepare_vhot(state: str, config: Dict[str, Any], per_item_rows: List[Dict[str, Any]]) -> VHotSpec:
    predictions_dir = Path(config.get("paths", {}).get("vtrac_predictions_dir", "data/outputs/predictions"))
    spec = try_load_hot_families_from_predictions(state, predictions_dir)
    if spec is not None:
        return spec
    return derive_hot_families_from_dr(per_item_rows, min_methods=2, prefer_section="Combined", top_k=5)


def run(state: str, analysis_root: Optional[Path | str] = None, config_path: Optional[Path] = None) -> Dict[str, Any]:
    cfg_path = config_path or (Path(__file__).parent / "config.yml")
    cfg = _load_config(cfg_path)

    root_path = Path(analysis_root) if analysis_root is not None else None
    items, source_path = load_training_json(state, root_path)
    if not items:
        raise ValueError(f"No training items available for state {state}")

    feature_entries = build_features(items, cfg)
    _aggregate_metrics(feature_entries, cfg)

    rows: List[Dict[str, Any]] = []
    for entry in feature_entries:
        rows.append(entry.row)

    flags_map = _load_winner_flags(state, root_path)
    for row in rows:
        key = _section_key(row)
        row.setdefault("dr.win_variant", "")
        row.setdefault("dr.win_final_value", "")
        row.setdefault("dr.win_drop_digit", "")
        row.setdefault("dr.win_vtrac_local_index", -1)
        for kind in FLAG_KIND_ORDER:
            row.setdefault(f"dr.win_{kind}", 0)
            row.setdefault(f"dr.win_step_{kind}", -1)
        if key in flags_map:
            row.update(flags_map[key])

    for row in rows:
        score_data = score_row(row, cfg)
        row["score_raw"] = score_data["score_raw"]
        row["score"] = score_data["score"]
        row["lock_decision"] = score_data["lock_decision"]
        row["lock_reason"] = score_data["lock_reason"]

    hot_spec = _prepare_vhot(state, cfg, rows)
    strength = hot_spec.detail or {}
    for row in rows:
        canon = str(row.get("pattern", ""))
        row["vtrac.set"] = vtrac_set(canon) if canon else ""
        row["vtrac.v_hot"] = float(strength.get(row["vtrac.set"], 0.0))
        row["vtrac.hot_source"] = hot_spec.source

    apply_linear_scoring(rows, cfg)
    apply_post_score(rows, cfg)
    attach_lockscore(rows, cfg)

    overlay_cfg = cfg.get("overlay", {})
    overlay_artifacts = None
    top_rows = _top_candidates(rows, cfg)
    out_dir = analyzer_out_dir(state, root_path)
    meta = {
        "state": state,
        "items": len(rows),
        "source": str(source_path),
        "config_path": str(cfg_path),
        "config_hash": _config_hash(cfg_path),
        "git_sha": _git_sha(),
        "policy": cfg.get("policy", {}),
        "cluster_scan": cfg.get("features", {}).get("cluster_scan", {}),
        "diagnostics": cfg.get("diagnostics", {}),
        "overlay": overlay_cfg,
        "scoring_linear": cfg.get("scoring_linear", {}),
        "scoring_v2": cfg.get("scoring_v2", {}),
        "lockscore": cfg.get("lockscore", {}),
        "vtrac_hot_source": hot_spec.source,
        "vtrac_hot_families": sorted(hot_spec.families),
    }

    diagnostics_cfg = cfg.get("diagnostics", {})
    write_artifacts(
        out_dir=out_dir,
        state=state,
        per_item=rows,
        top_rows=top_rows,
        meta=meta,
        diagnostics_config=diagnostics_cfg,
        feature_entries=feature_entries,
        cfg=cfg,
    )

    artifacts = [
        f"{state}_analyzer_v2_per_item.csv",
        f"{state}_analyzer_v2_top_candidates.csv",
        f"{state}_analyzer_v2_meta.json",
    ]
    if overlay_artifacts:
        artifacts.extend(overlay_artifacts.files)

    return {
        "state": state,
        "rows": len(rows),
        "out_dir": str(out_dir),
        "artifacts": artifacts,
    }
