#!/usr/bin/env python3
"""
Aux sharepack summary (Master Validation Part 3).

This script produces a **sharepack-stable** evidence dump of Aux signals:
- Draw CSV snapshot (Combined/Midday/Evening) copied into the sharepack
- Repeat-watch + VTRAC overlay/heatboard
- Positional pressure + shortlist
- Doubles + pairs overdue pressure
- Sums/root-sums pressure
- Blackapple triggers/candidates

Outputs:
- `sharepacks/<DATE>/<STATE>/aux/<STATE>/summary.md`
- `sharepacks/<DATE>/<STATE>/aux/<STATE>/summary.json`

Run:
  python3 scripts/tools/aux_sharepack_summary.py --date 2025-06-21 --state OntarioCanada4
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from datetime import date as _date
from pathlib import Path
from typing import Any, Dict, List, Tuple

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
SRC = ROOT / "src"
if SRC.exists() and str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from alpha_analytical.control_center import aux_validation  # noqa: E402
from core import aux_config  # noqa: E402
from modules import blackapple  # noqa: E402
from modules.aux_loaders import load_state_draws  # noqa: E402

VARIANTS: Tuple[str, ...] = ("combined", "midday", "evening")


def parse_iso_date(value: str) -> _date:
    try:
        return _date.fromisoformat(value)
    except ValueError as exc:
        raise SystemExit(f"Invalid --date (expected YYYY-MM-DD): {value}") from exc


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def fmt_head(draws: List[str], limit: int = 5) -> str:
    sample = draws[:limit]
    suffix = " …" if len(draws) > limit else ""
    return ", ".join(sample) + suffix


def safe_rel(path_str: str | None) -> str:
    if not path_str:
        return "-"
    path = Path(path_str)
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def resolve_live_draw_paths(state: str, *, max_n: int) -> Dict[str, Dict[str, Any]]:
    resolved: Dict[str, Dict[str, Any]] = {}
    for variant in VARIANTS:
        draws, path_str = load_state_draws(state, variant=variant, base=None, max_n=max_n)
        resolved[variant] = {
            "original_path": path_str,
            "draw_count": len(draws),
            "draws_head": draws[:5],
        }
    return resolved


def snapshot_draws(state: str, snapshot_dir: Path, *, max_n: int) -> Dict[str, Dict[str, Any]]:
    ensure_dir(snapshot_dir)
    info = resolve_live_draw_paths(state, max_n=max_n)
    for variant, payload in info.items():
        src_str = payload.get("original_path")
        if not src_str:
            payload["snapshot_path"] = None
            payload["snapshot_error"] = "original_path_missing"
            continue
        src = Path(src_str)
        if not src.exists():
            payload["snapshot_path"] = str(snapshot_dir / src.name)
            payload["snapshot_error"] = "original_path_not_found"
            continue
        dst = snapshot_dir / src.name
        shutil.copy2(src, dst)
        payload["snapshot_path"] = str(dst)
    return info


def resolve_aux_state_label(state_key: str) -> str | None:
    """
    Map a sharepack state key (e.g., OntarioCanada4) to an Aux extractor label
    (e.g., Ontario) for draw generation from a workbook.
    """
    try:
        from modules.module_d_auxiliary_tools.refactored import draws_extractor_p3_columns as column_map  # type: ignore
    except Exception:
        return None

    canonical = column_map.canonical_state(state_key)
    if canonical:
        return canonical

    norm_key = re.sub(r"[^a-z0-9]+", "", (state_key or "").lower())
    best: str | None = None
    best_score = 0
    for tracked in column_map.get_tracked_states():
        norm_tracked = re.sub(r"[^a-z0-9]+", "", tracked.lower())
        if not norm_tracked:
            continue
        if norm_tracked in norm_key or norm_key in norm_tracked:
            score = len(norm_tracked)
            if score > best_score:
                best_score = score
                best = tracked
    return best


def generate_draws_to_snapshot(
    *,
    excel_path: str,
    state_key: str,
    snapshot_dir: Path,
    max_draws: int,
) -> Dict[str, Any]:
    """
    Generate Combined/Midday/Evening draw CSVs for a state from a specific workbook
    snapshot into the sharepack snapshot directory.
    """
    ensure_dir(snapshot_dir)
    aux_state_label = resolve_aux_state_label(state_key)
    if not aux_state_label:
        return {
            "ok": False,
            "excel_path": excel_path,
            "state_key": state_key,
            "error": "aux_state_label_unresolved",
        }
    from modules.module_d_auxiliary_tools.refactored import extractor as aux_extractor  # type: ignore

    aux_extractor.save_category_csvs(
        excel_path=excel_path,
        states=[aux_state_label],
        outdir=snapshot_dir,
        include_combined=True,
        include_specials=False,
        max_draws=max_draws,
    )
    return {
        "ok": True,
        "excel_path": excel_path,
        "state_key": state_key,
        "aux_state_label": aux_state_label,
    }


def load_snapshot_draws(state: str, snapshot_dir: Path, *, max_n: int) -> Dict[str, Dict[str, Any]]:
    by_variant: Dict[str, Dict[str, Any]] = {}
    for variant in VARIANTS:
        draws, resolved_path = load_state_draws(state, variant=variant, base=snapshot_dir, max_n=max_n)
        by_variant[variant] = {
            "resolved_path": resolved_path,
            "draw_count": len(draws),
            "draws_head": draws[:5],
        }
    return by_variant


def top_doubles(stats: Dict[str, Dict[str, int]], limit: int) -> List[Dict[str, Any]]:
    rows = [{"combo": combo, **payload} for combo, payload in (stats or {}).items()]
    rows.sort(key=lambda row: int(row.get("draws_since", 0)), reverse=True)
    return rows[:limit]


def top_overlay(overlay: Dict[int, int], limit: int) -> List[Dict[str, Any]]:
    rows = [{"index": idx, "draws_since": ds} for idx, ds in (overlay or {}).items()]
    rows.sort(key=lambda row: row["draws_since"], reverse=True)
    return rows[:limit]


def top_heatboard(heatboard: Dict[int, Dict[str, Any]], limit: int) -> List[Dict[str, Any]]:
    rows = [{"index": idx, **payload} for idx, payload in (heatboard or {}).items()]
    rows.sort(key=lambda row: int(row.get("ds", 0)), reverse=True)
    return rows[:limit]


def top_sums(payload: Dict[str, Any], limit: int) -> List[Dict[str, Any]]:
    by_sum = (payload or {}).get("by_sum", {}) or {}
    rows = [{"sum": label, **stats} for label, stats in by_sum.items()]
    rows.sort(key=lambda row: int(row.get("draws_since", 0)), reverse=True)
    return rows[:limit]


def top_pairs(payload: Dict[str, Any], limit: int) -> Dict[str, List[Dict[str, Any]]]:
    status = (payload or {}).get("status", {}) or {}
    repeating = [{"pair": pair, "draws_since": ds, "severity": status.get(pair)} for pair, ds in (payload or {}).get("repeating", {}).items()]
    non_repeating = [
        {"pair": pair, "draws_since": ds, "severity": status.get(pair)}
        for pair, ds in (payload or {}).get("non_repeating", {}).items()
    ]
    repeating.sort(key=lambda row: int(row.get("draws_since", 0)), reverse=True)
    non_repeating.sort(key=lambda row: int(row.get("draws_since", 0)), reverse=True)
    return {"repeating": repeating[:limit], "non_repeating": non_repeating[:limit]}


def top_blackapple(payload: Dict[str, Any], limit: int) -> List[Dict[str, Any]]:
    candidates = (payload or {}).get("candidates", []) or []
    rows: List[Dict[str, Any]] = []
    for cand in candidates[:limit]:
        rows.append(
            {
                "combo": cand.get("combo"),
                "score": cand.get("score"),
                "tags": sorted(list(cand.get("tags") or [])),
            }
        )
    return rows


def build_summary(
    state: str,
    sharepack_date: str,
    *,
    snapshot_dir: Path,
    max_n: int,
    limit: int,
    sums_window: int,
    pairs_window: int,
    positional_window: int,
    excel_path: str | None = None,
) -> Dict[str, Any]:
    live_info = resolve_live_draw_paths(state, max_n=max_n)
    snapshot_meta: Dict[str, Any] = {"mode": "copied_from_live"}
    if excel_path:
        snapshot_meta = {"mode": "generated_from_excel"}
        snapshot_meta.update(
            generate_draws_to_snapshot(
                excel_path=excel_path,
                state_key=state,
                snapshot_dir=snapshot_dir,
                max_draws=max_n,
            )
        )
    else:
        snapshot_meta["copy_report"] = snapshot_draws(state, snapshot_dir, max_n=max_n)
    snapshot_draws_info = load_snapshot_draws(state, snapshot_dir, max_n=max_n)

    repeat_watch = aux_validation.repeat_summary_by_variant(state, base=snapshot_dir, max_n=max_n)
    positional_shortlist = aux_validation.positional_shortlist_report(
        state,
        base=snapshot_dir,
        max_n=max_n,
        window=positional_window,
    )
    positional_hard_due = aux_validation.positional_hard_due_by_variant(
        state,
        base=snapshot_dir,
        max_n=max_n,
        window=positional_window,
    )

    doubles_by_variant = aux_validation.collect_variant_stats(state, base=snapshot_dir, max_n=max_n)
    doubles_alerts = aux_validation.multi_variant_alerts(state, base=snapshot_dir, max_n=max_n)

    pairs_by_variant = aux_validation.collect_pair_stats_for_state(
        state,
        base=snapshot_dir,
        max_n=max_n,
        window=pairs_window,
    )
    pairs_alerts = aux_validation.pair_multi_variant_alerts(
        state,
        base=snapshot_dir,
        max_n=max_n,
        window=pairs_window,
    )

    vtrac_overlay = aux_validation.vtrac_overlay_by_variant(state, base=snapshot_dir, max_n=max_n)
    vtrac_heatboard = aux_validation.vtrac_heatboard_by_variant(
        state,
        base=snapshot_dir,
        max_n=max_n,
        window=max_n,
    )

    sums_by_variant = aux_validation.sums_stats_by_variant(
        state,
        base=snapshot_dir,
        max_n=max_n,
        window=sums_window,
    )

    ba_by_variant: Dict[str, Any] = {}
    for variant in VARIANTS:
        draws, _ = load_state_draws(state, variant=variant, base=snapshot_dir, max_n=max_n)
        raw = blackapple.analyze_blackapple(draws)
        sanitized_candidates: List[Dict[str, Any]] = []
        for cand in raw.get("candidates", []) or []:
            tags = cand.get("tags") or []
            if isinstance(tags, set):
                tags_list = sorted(list(tags))
            else:
                tags_list = list(tags) if isinstance(tags, (list, tuple)) else [str(tags)]
            sanitized_candidates.append(
                {
                    "combo": cand.get("combo"),
                    "score": cand.get("score"),
                    "tags": tags_list,
                }
            )
        ba_by_variant[variant] = {
            "score": raw.get("score"),
            "triggers": raw.get("triggers"),
            "candidates": sanitized_candidates,
        }

    return {
        "state": state,
        "date": sharepack_date,
        "draw_sources": {
            "snapshot_dir": str(snapshot_dir),
            "snapshot_meta": snapshot_meta,
            "live": live_info,
            "snapshot": snapshot_draws_info,
        },
        "config": {
            "PAIRS_WINDOW": getattr(aux_config, "PAIRS_WINDOW", None),
            "POSITIONAL_WINDOW": getattr(aux_config, "POSITIONAL_WINDOW", None),
            "VTRAC_INDEX_WINDOW": getattr(aux_config, "VTRAC_INDEX_WINDOW", None),
            "COMBO_DOUBLE_LATE": getattr(aux_config, "COMBO_DOUBLE_LATE", None),
            "COMBO_DOUBLE_VERY_LATE": getattr(aux_config, "COMBO_DOUBLE_VERY_LATE", None),
            "REPEATING_LATE": getattr(aux_config, "REPEATING_LATE", None),
            "REPEATING_VERY_LATE": getattr(aux_config, "REPEATING_VERY_LATE", None),
            "NONREPEATING_LATE": getattr(aux_config, "NONREPEATING_LATE", None),
            "NONREPEATING_VERY_LATE": getattr(aux_config, "NONREPEATING_VERY_LATE", None),
            "PAIR_PENDING": getattr(aux_config, "PAIR_PENDING", None),
            "max_n_used": max_n,
            "pairs_window_used": pairs_window,
            "positional_window_used": positional_window,
            "sums_window_used": sums_window,
        },
        "repeat_watch": repeat_watch,
        "positional": {
            "shortlist_report": positional_shortlist,
            "hard_due_by_variant": positional_hard_due,
        },
        "doubles": {
            "by_variant": doubles_by_variant,
            "multi_variant_alerts": doubles_alerts,
            "top_by_variant": {v: top_doubles(payload, limit) for v, payload in doubles_by_variant.items()},
        },
        "pairs": {
            "by_variant": pairs_by_variant,
            "multi_variant_alerts": pairs_alerts,
            "top_by_variant": {v: top_pairs(payload, limit) for v, payload in pairs_by_variant.items()},
        },
        "vtrac": {
            "overlay_by_variant": vtrac_overlay,
            "heatboard_by_variant": vtrac_heatboard,
            "overlay_top": {v: top_overlay(payload, limit) for v, payload in vtrac_overlay.items()},
            "heatboard_top": {v: top_heatboard(payload, limit) for v, payload in vtrac_heatboard.items()},
        },
        "sums": {
            "by_variant": sums_by_variant,
            "top_by_variant": {v: top_sums(payload, limit) for v, payload in sums_by_variant.items()},
        },
        "blackapple": {
            "by_variant": ba_by_variant,
            "top_by_variant": {v: top_blackapple(payload, limit) for v, payload in ba_by_variant.items()},
        },
    }


def render_markdown(summary: Dict[str, Any]) -> str:
    state = summary["state"]
    date = summary["date"]
    cfg = summary.get("config", {})
    draws = summary.get("draw_sources", {})

    lines: List[str] = []
    lines.append(f"# Aux Summary — {state} — {date}")
    lines.append("")
    lines.append("Evidence dump for Master Validation **Part 3** (Aux).")
    lines.append("All facts are labeled by source for provenance.")
    lines.append("")

    lines.append("## Config (source: core/aux_config.py)")
    lines.append(
        f"- windows: pairs={cfg.get('PAIRS_WINDOW')} positional={cfg.get('POSITIONAL_WINDOW')} vtrac_index={cfg.get('VTRAC_INDEX_WINDOW')} sums_used={cfg.get('sums_window_used')}"
    )
    lines.append(
        f"- thresholds: doubles_late={cfg.get('COMBO_DOUBLE_LATE')} doubles_very_late={cfg.get('COMBO_DOUBLE_VERY_LATE')} pair_pending={cfg.get('PAIR_PENDING')}"
    )
    lines.append("")

    lines.append("## Draw sources (source: modules.aux_loaders.load_state_draws)")
    lines.append(f"- snapshot_dir: `{safe_rel(draws.get('snapshot_dir'))}`")
    meta = draws.get("snapshot_meta", {}) or {}
    lines.append(f"- snapshot_mode: {meta.get('mode') or '-'}")
    if meta.get("mode") == "generated_from_excel":
        lines.append(f"- excel: `{safe_rel(meta.get('excel_path'))}` | aux_state_label: {meta.get('aux_state_label') or '-'}")
        if meta.get("ok") is False:
            lines.append(f"- snapshot_error: {meta.get('error')}")
    for variant in VARIANTS:
        live = (draws.get("live", {}) or {}).get(variant, {})
        snap = (draws.get("snapshot", {}) or {}).get(variant, {})
        lines.append(
            f"- {variant}: live=`{safe_rel(live.get('original_path'))}` snap=`{safe_rel(snap.get('resolved_path'))}` n={snap.get('draw_count')} head={fmt_head(snap.get('draws_head') or [])}"
        )
    lines.append("")

    repeat_watch = summary.get("repeat_watch", {}) or {}
    positional = summary.get("positional", {}) or {}
    shortlist = positional.get("shortlist_report", {}) or {}
    hard_due = positional.get("hard_due_by_variant", {}) or {}
    doubles_top = (summary.get("doubles", {}) or {}).get("top_by_variant", {}) or {}
    pairs_top = (summary.get("pairs", {}) or {}).get("top_by_variant", {}) or {}
    vtrac_overlay_top = (summary.get("vtrac", {}) or {}).get("overlay_top", {}) or {}
    vtrac_heat_top = (summary.get("vtrac", {}) or {}).get("heatboard_top", {}) or {}
    sums_top = (summary.get("sums", {}) or {}).get("top_by_variant", {}) or {}
    ba_top = (summary.get("blackapple", {}) or {}).get("top_by_variant", {}) or {}
    ba_by_variant = (summary.get("blackapple", {}) or {}).get("by_variant", {}) or {}

    for variant in VARIANTS:
        lines.append(f"## {variant.title()} (variant)")
        lines.append("")

        lines.append("### Repeat watch (source: aux_validation.repeat_summary_by_variant)")
        rw = repeat_watch.get(variant, {}) or {}
        if rw:
            lines.append(
                f"- current_index={rw.get('current_index')} streak={rw.get('current_streak')} max={rw.get('max_streak')} last_repeat_gap={rw.get('last_repeat_gap')} last_repeat_index={rw.get('last_repeat_index')}"
            )
        else:
            lines.append("- _no data_")
        lines.append("")

        lines.append("### Positional (source: aux_validation.positional_shortlist_report)")
        top_digits = (shortlist.get("variant_top_digits", {}) or {}).get(variant, []) or []
        if top_digits:
            parts = [f"P{row['position']+1}:{row['digit']} (gap={row['gap']})" for row in top_digits]
            lines.append(f"- top digits: {', '.join(parts)}")
        else:
            lines.append("- top digits: _no data_")
        lines.append(f"- consensus_notes: {', '.join(shortlist.get('consensus_notes', []) or []) or '-'}")
        lines.append(f"- double_pressure_notes: {', '.join(shortlist.get('double_pressure_notes', []) or []) or '-'}")
        lines.append("")

        lines.append("### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)")
        hd = hard_due.get(variant, []) or []
        if hd:
            parts = [f"P{row['position']+1}:{row['digit']} (ds={row['draws_since']})" for row in hd]
            lines.append(f"- hard_due: {', '.join(parts)}")
        else:
            lines.append("- hard_due: none")
        lines.append("")

        lines.append("### Positional shortlist (source: aux_validation.positional_shortlist_report)")
        candidates = shortlist.get("candidates", []) or []
        if candidates:
            for cand in candidates[:10]:
                tags = cand.get("tags") or []
                tag_display = ",".join(tags[:5]) if tags else "-"
                lines.append(f"- {cand.get('combo')}: score={cand.get('score')} tags={tag_display} src={cand.get('source') or '-'}")
        else:
            lines.append("- _no candidates_")
        lines.append("")

        lines.append("### Doubles (source: aux_validation.collect_variant_stats)")
        doubles_rows = doubles_top.get(variant, []) or []
        if doubles_rows:
            for row in doubles_rows:
                lines.append(f"- {row.get('combo')}: ds={row.get('draws_since')} sev={row.get('severity')}")
        else:
            lines.append("- _no late doubles_")
        lines.append("")

        lines.append("### Pairs (source: aux_validation.collect_pair_stats_for_state)")
        pairs_rows = pairs_top.get(variant, {}) or {}
        rep = pairs_rows.get("repeating", []) or []
        nr = pairs_rows.get("non_repeating", []) or []
        if rep:
            lines.append("- repeating:")
            for row in rep:
                sev = row.get("severity") or "-"
                lines.append(f"  - {row.get('pair')}: ds={row.get('draws_since')} sev={sev}")
        if nr:
            lines.append("- non_repeating:")
            for row in nr:
                sev = row.get("severity") or "-"
                lines.append(f"  - {row.get('pair')}: ds={row.get('draws_since')} sev={sev}")
        if not rep and not nr:
            lines.append("- _no pair rows_")
        lines.append("")

        lines.append("### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)")
        overlay = vtrac_overlay_top.get(variant, []) or []
        if overlay:
            lines.append("- top overdue indices (ds): " + ", ".join(f"{row['index']}:{row['draws_since']}" for row in overlay))
        else:
            lines.append("- _no data_")
        lines.append("")

        lines.append("### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)")
        heat = vtrac_heat_top.get(variant, []) or []
        if heat:
            heat_str = ", ".join(
                f"{row['index']}:ds={row.get('ds')} fs={row.get('freq_short')} fl={row.get('freq_long')} hz={row.get('hazard')}"
                for row in heat
            )
            lines.append(f"- top heat (by ds): {heat_str}")
        else:
            lines.append("- _no data_")
        lines.append("")

        lines.append("### Sums (source: aux_validation.sums_stats_by_variant)")
        sums_rows = sums_top.get(variant, []) or []
        if sums_rows:
            for row in sums_rows:
                flags = row.get("flags") or {}
                active = "+".join([k for k, v in flags.items() if v]) if flags else "-"
                lines.append(f"- S{row.get('sum')}: ds={row.get('draws_since')} flags={active}")
        else:
            lines.append("- _no data_")
        lines.append("")

        lines.append("### Blackapple (source: modules.blackapple.analyze_blackapple)")
        ba = ba_by_variant.get(variant, {}) or {}
        lines.append(f"- score={ba.get('score')} triggers={ba.get('triggers')}")
        top = ba_top.get(variant, []) or []
        if top:
            lines.append("- top candidates:")
            for row in top:
                lines.append(f"  - {row.get('combo')}: score={row.get('score')} tags={','.join(row.get('tags') or []) or '-'}")
        else:
            lines.append("- _no candidates_")
        lines.append("")

    lines.append("## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)")
    lines.append("")
    doubles_alerts = (summary.get("doubles", {}) or {}).get("multi_variant_alerts", {}) or {}
    pairs_alerts = (summary.get("pairs", {}) or {}).get("multi_variant_alerts", {}) or {}

    lines.append("### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)")
    if doubles_alerts:
        for combo, by_variant in sorted(doubles_alerts.items()):
            parts = [f"{v}:{p.get('draws_since')}({p.get('severity')})" for v, p in sorted(by_variant.items())]
            lines.append(f"- {combo} -> {'; '.join(parts)}")
    else:
        lines.append("- none")
    lines.append("")

    lines.append("### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)")
    if pairs_alerts:
        for pair, by_variant in sorted(pairs_alerts.items()):
            parts = [f"{v}:{p.get('draws_since')}({p.get('severity')})" for v, p in sorted(by_variant.items())]
            lines.append(f"- {pair} -> {'; '.join(parts)}")
    else:
        lines.append("- none")
    lines.append("")

    lines.append("### Aggregated positional digits (source: aux_validation.positional_shortlist_report)")
    agg = shortlist.get("aggregated_digits", {}) or {}
    if agg:
        for pos, digits in agg.items():
            digit_str = ", ".join(
                f"{d.get('digit')}({d.get('score')})[{','.join((d.get('tags') or [])[:2])}]"
                for d in digits
            )
            lines.append(f"- P{int(pos)+1}: {digit_str}")
    else:
        lines.append("- _no data_")
    lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    ap = argparse.ArgumentParser(description="Build Aux summary.md/.json inside a sharepack for Part 3.")
    ap.add_argument("--date", required=True, help="Sharepack date folder (results/winners date, YYYY-MM-DD)")
    ap.add_argument("--state", required=True, help="State key (e.g., OntarioCanada4)")
    ap.add_argument("--max-n", type=int, default=1000, help="Max newest draws to load (default 1000)")
    ap.add_argument("--limit", type=int, default=10, help="Top-N rows to render per section (default 10)")
    ap.add_argument("--sums-window", type=int, default=100, help="Sums analysis window (default 100)")
    ap.add_argument(
        "--excel",
        default=None,
        help="Optional Pick3StatsC4 workbook path to generate draw CSVs into the sharepack snapshot dir (recommended for backtests).",
    )
    ap.add_argument(
        "--pairs-window",
        type=int,
        default=int(getattr(aux_config, "PAIRS_WINDOW", 360)),
        help="Pairs window override (default: aux_config PAIRS_WINDOW)",
    )
    ap.add_argument(
        "--positional-window",
        type=int,
        default=int(getattr(aux_config, "POSITIONAL_WINDOW", 150)),
        help="Positional window override (default: aux_config POSITIONAL_WINDOW)",
    )
    ap.add_argument("--md-out", default="summary.md", help="Markdown output filename (default summary.md)")
    ap.add_argument("--json-out", default="summary.json", help="JSON output filename (default summary.json)")
    args = ap.parse_args()

    parse_iso_date(args.date)

    sharepack_root = ROOT / "sharepacks" / args.date / args.state
    if not sharepack_root.exists():
        raise SystemExit(f"Sharepack not found: {sharepack_root}")

    aux_root = sharepack_root / "aux" / args.state
    snapshot_dir = sharepack_root / "aux" / "draws"
    ensure_dir(aux_root)
    ensure_dir(snapshot_dir)

    summary = build_summary(
        args.state,
        args.date,
        snapshot_dir=snapshot_dir,
        max_n=args.max_n,
        limit=args.limit,
        sums_window=args.sums_window,
        pairs_window=args.pairs_window,
        positional_window=args.positional_window,
        excel_path=args.excel,
    )
    md_text = render_markdown(summary)

    md_path = aux_root / args.md_out
    json_path = aux_root / args.json_out
    md_path.write_text(md_text, encoding="utf-8")
    json_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    print(f"Wrote: {md_path}")
    print(f"Wrote: {json_path}")


if __name__ == "__main__":
    main()
