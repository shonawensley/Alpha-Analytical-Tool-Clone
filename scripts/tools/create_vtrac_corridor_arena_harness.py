#!/usr/bin/env python3
"""Create a review-only VTRAC corridor/Arena harness.

This harness evaluates whether predictive-safe VTRAC Arena objects expose
winner-side VTRAC structures seen in post-result winner JSONs. It does not
mutate canonical sharepacks, winner artifacts, scoring weights, Play Cards, or
Candidate Universe outputs.
"""

from __future__ import annotations

import argparse
import csv
from datetime import datetime, timedelta
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple


REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
if SRC_ROOT.exists() and str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from alpha_analytical.control_center.batch_runner import parse_winner_sheet  # noqa: E402

from modules.vtrac_reference import get_vtrac_index  # noqa: E402
from modules.vtrac_straight_map import ordered_vcode_for_combo, vstraight_lane_for_combo  # noqa: E402
from scripts.tools.build_aggregated_analysis_arena import build_aggregated_analysis_arena_payload  # noqa: E402
from scripts.tools.create_vtrac_corridor_summary import create_corridor_summary  # noqa: E402


CLASS_ARENA_ORDERED_LANE_CAPTURE = "ARENA_ORDERED_LANE_CAPTURE"
CLASS_ARENA_BOXED_CORRIDOR_CAPTURE = "ARENA_BOXED_CORRIDOR_CAPTURE"
CLASS_ENHANCED_INDEX_CAPTURE = "ENHANCED_INDEX_CAPTURE"
CLASS_WINNER_LENS_ONLY = "WINNER_LENS_ONLY"
CLASS_RENDERER_GAP = "RENDERER_GAP"
CLASS_DRAW_DATA_INFLATED = "DRAW_DATA_INFLATED"
CLASS_SOURCE_INDEX_MISMATCH = "SOURCE_INDEX_MISMATCH"
CLASS_NOT_CAPTURED = "NOT_CAPTURED"
CLASS_UNSUPPORTED_TRIPLE = "UNSUPPORTED_TRIPLE"
CLASS_MISSING_PREDICTIVE_STATE = "MISSING_PREDICTIVE_STATE"


def _safe_rel(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _digits_only(value: Any) -> str:
    return "".join(ch for ch in str(value or "") if ch.isdigit())


def _canon(value: Any) -> str:
    digits = _digits_only(value)
    if len(digits) != 3:
        return ""
    return "".join(sorted(digits))


def _to_int(value: Any, default: int = 0) -> int:
    try:
        if value is None or value == "":
            return default
        return int(value)
    except Exception:
        return default


def _to_float(value: Any, default: float = 0.0) -> float:
    try:
        if value is None or value == "":
            return default
        return float(value)
    except Exception:
        return default


def _iter_dates(start_date: str, end_date: str) -> List[str]:
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    if end < start:
        start, end = end, start
    dates: List[str] = []
    cur = start
    while cur <= end:
        dates.append(cur.strftime("%Y-%m-%d"))
        cur += timedelta(days=1)
    return dates


def _history_date(results_date: str) -> str:
    dt = datetime.strptime(results_date, "%Y-%m-%d") - timedelta(days=1)
    return dt.strftime("%Y-%m-%d")


def _read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8", errors="replace"))


def _write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _write_csv(path: Path, rows: Sequence[Mapping[str, Any]], fieldnames: Sequence[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(fieldnames))
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fieldnames})


def _read_results_map(date: str) -> Dict[str, Dict[str, str]]:
    path = REPO_ROOT / "data" / "results" / f"{date}.txt"
    if not path.exists():
        return {}
    entries = parse_winner_sheet(path.read_text(encoding="utf-8", errors="replace"))
    out: Dict[str, Dict[str, str]] = {}
    for entry in entries:
        state = getattr(entry, "project_state", None)
        if not state:
            continue
        draws: Dict[str, str] = {}
        if getattr(entry, "midday", None):
            draws["Midday"] = str(entry.midday)
        if getattr(entry, "evening", None):
            draws["Evening"] = str(entry.evening)
        if draws:
            out[state] = draws
    return out


def _draw_label_for_winner(results_map: Mapping[str, Mapping[str, str]], state: str, winner: str) -> str:
    draws = results_map.get(state) or {}
    matches = [label for label, value in draws.items() if _digits_only(value) == winner]
    if not matches:
        return "Unknown"
    return "+".join(matches)


def _find_latest_enhanced_json(day_dir: Path, state: str) -> Optional[Path]:
    vtrac_dir = day_dir / state / "vtrac" / state
    if not vtrac_dir.exists():
        return None
    hits = sorted(vtrac_dir.glob(f"{state}_vtrac_enhanced_*.json"))
    return hits[-1] if hits else None


def _iter_winner_jsons(
    winners_root: Path,
    date: str,
    states: Sequence[str],
) -> Tuple[List[Path], List[Dict[str, str]]]:
    """Return one deterministic artifact per state/winner plus duplicate receipts."""
    date_dir = winners_root / date
    if not date_dir.exists():
        return [], []
    state_filter = {state for state in states if state}
    candidates: Dict[Tuple[str, str], List[Path]] = {}
    for state_dir in sorted(path for path in date_dir.iterdir() if path.is_dir()):
        if state_filter and state_dir.name not in state_filter:
            continue
        for path in sorted(state_dir.glob("*_winner_*.json")):
            match = re.search(r"_winner_(\d{3})(?:_|$)", path.stem)
            winner = match.group(1) if match else path.name
            key = (state_dir.name, winner)
            candidates.setdefault(key, []).append(path)

    selected: Dict[Tuple[str, str], Path] = {}
    duplicates: List[Dict[str, str]] = []
    for key, paths in sorted(candidates.items()):
        kept = paths[-1]
        selected[key] = kept
        state, winner = key
        duplicates.extend(
            {
                "date": date,
                "state": state,
                "winner": winner,
                "discarded": _safe_rel(discarded),
                "kept": _safe_rel(kept),
                "selection_policy": "lexicographically_latest_filename",
            }
            for discarded in paths[:-1]
        )
    return [selected[key] for key in sorted(selected)], duplicates


def _ranked_match(rows: Sequence[Mapping[str, Any]], key: str, value: Any) -> Tuple[Optional[int], Optional[Mapping[str, Any]]]:
    target = str(value)
    for pos, row in enumerate(rows, start=1):
        if str(row.get(key)) == target:
            return pos, row
    return None, None


def _top_straights(row: Optional[Mapping[str, Any]], limit: int = 12) -> List[str]:
    if not row:
        return []
    witnesses = row.get("top_witness_straights") or []
    out: List[str] = []
    if not isinstance(witnesses, list):
        return out
    for item in witnesses:
        if not isinstance(item, dict):
            continue
        straight = _digits_only(item.get("straight"))
        if len(straight) == 3 and straight not in out:
            out.append(straight)
        if len(out) >= limit:
            break
    return out


def _top_tokens(summary: Mapping[str, Any], limit: int = 12) -> List[str]:
    rows = summary.get("top_tokens_by_cell_hits") or []
    out: List[str] = []
    if not isinstance(rows, list):
        return out
    for item in rows:
        if not isinstance(item, dict):
            continue
        value = _digits_only(item.get("value"))
        if len(value) == 3 and value not in out:
            out.append(value)
        if len(out) >= limit:
            break
    return out


def classify_case(
    *,
    ordered_lane_match: bool,
    boxed_corridor_match: bool,
    enhanced_index_rank: Optional[int],
    winner_pattern_hits: int,
    renderer_gap: bool,
    draw_data_inflation_warning: bool,
    source_index_mismatch_count: int,
    unsupported_triple: bool = False,
    missing_predictive_state: bool = False,
) -> List[str]:
    classes: List[str] = []
    if unsupported_triple:
        classes.append(CLASS_UNSUPPORTED_TRIPLE)
    if missing_predictive_state:
        classes.append(CLASS_MISSING_PREDICTIVE_STATE)
    if ordered_lane_match:
        classes.append(CLASS_ARENA_ORDERED_LANE_CAPTURE)
    if boxed_corridor_match:
        classes.append(CLASS_ARENA_BOXED_CORRIDOR_CAPTURE)
    if enhanced_index_rank is not None:
        classes.append(CLASS_ENHANCED_INDEX_CAPTURE)
    if winner_pattern_hits > 0 and not ordered_lane_match and not boxed_corridor_match:
        classes.append(CLASS_WINNER_LENS_ONLY)
    if renderer_gap:
        classes.append(CLASS_RENDERER_GAP)
    if draw_data_inflation_warning:
        classes.append(CLASS_DRAW_DATA_INFLATED)
    if source_index_mismatch_count > 0:
        classes.append(CLASS_SOURCE_INDEX_MISMATCH)
    if not classes:
        classes.append(CLASS_NOT_CAPTURED)
    return classes


def _arena_payload_for_state(
    *,
    day_dir: Path,
    sharepacks_root: Path,
    date: str,
    state: str,
    profile: str,
    experiment_tag: str,
    top_items: int,
) -> Optional[Dict[str, Any]]:
    if not (day_dir / state).exists():
        return None
    return build_aggregated_analysis_arena_payload(
        day_dir=day_dir,
        state_key=state,
        results_date=date,
        history_date=_history_date(date),
        profile=profile,
        experiment_tag=experiment_tag,
        sharepacks_root=sharepacks_root,
        repo_root=REPO_ROOT,
        top_items=top_items,
    )


def _case_summary_markdown(case: Mapping[str, Any]) -> str:
    classifications = ", ".join(case.get("classification") or []) or "-"
    lines = [
        f"# VTRAC Corridor Arena Harness Case - {case.get('date')} {case.get('state')} {case.get('draw_label')} {case.get('winner_literal')}",
        "",
        "## Summary",
        "",
        f"- Winner: `{case.get('winner_literal')}` canonical `{case.get('winner_canonical')}`",
        f"- Ordered vcode: `{case.get('winner_ordered_vcode') or '-'}`",
        f"- Boxed VTRAC index: `{case.get('winner_boxed_vtrac_index') or '-'}`",
        f"- Classification: `{classifications}`",
        "",
        "## Capture",
        "",
        f"- Arena ordered lane rank: `{case.get('arena_ordered_vcode_rank') or '-'}`",
        f"- Arena boxed corridor rank: `{case.get('arena_boxed_index_rank') or '-'}`",
        f"- Enhanced index rank: `{case.get('enhanced_index_rank') or '-'}`",
        f"- Source-index mismatch count: `{case.get('source_index_mismatch_count')}`",
        "",
        "## Winner-Side Pattern Rows",
        "",
        f"- Literal permutation hits: `{case.get('literal_pattern_hits')}`",
        f"- Ordered lane hits: `{case.get('ordered_lane_pattern_hits')}`",
        f"- Boxed corridor hits: `{case.get('boxed_corridor_pattern_hits')}`",
        f"- Renderer gap: `{case.get('renderer_gap')}`",
        f"- Draw-data inflation warning: `{case.get('draw_data_inflation_warning')}`",
        "",
        "## Witness Overlap",
        "",
        f"- Arena ordered witnesses: `{case.get('arena_ordered_top_witnesses') or '-'}`",
        f"- Winner ordered top tokens: `{case.get('winner_ordered_top_tokens') or '-'}`",
        f"- Ordered witness overlap: `{case.get('ordered_witness_overlap') or '-'}`",
        f"- Arena boxed witnesses: `{case.get('arena_boxed_top_witnesses') or '-'}`",
        f"- Winner boxed top tokens: `{case.get('winner_boxed_top_tokens') or '-'}`",
        f"- Boxed witness overlap: `{case.get('boxed_witness_overlap') or '-'}`",
        "",
        "## Inputs",
        "",
        f"- Winner JSON: `{case.get('winner_json_path')}`",
        f"- VTRAC Enhanced JSON: `{case.get('enhanced_json_path') or '-'}`",
    ]
    return "\n".join(lines) + "\n"


def _summary_markdown(payload: Mapping[str, Any]) -> str:
    rows = payload.get("cases") or []
    class_counts = payload.get("class_counts") or {}
    lines = [
        f"# VTRAC Corridor Arena Harness - {payload.get('run_label')}",
        "",
        "Purpose: review-only validation of VTRAC ordered-lane and boxed-corridor Arena preservation against winner-side corridor evidence.",
        "",
        "## Scope",
        "",
        f"- Dates: `{payload.get('date_start')}` to `{payload.get('date_end')}`",
        f"- Case count: `{len(rows)}`",
        f"- Sharepacks root: `{payload.get('sharepacks_root')}`",
        f"- Winners root: `{payload.get('winners_root')}`",
        f"- Top items: `{payload.get('top_items')}`",
        "",
        "## Classification Counts",
        "",
        "| Classification | Count |",
        "|---|---:|",
    ]
    for key, value in sorted(class_counts.items(), key=lambda kv: (-int(kv[1]), kv[0])):
        lines.append(f"| {key} | {value} |")
    lines.extend(
        [
            "",
            "## Case Ledger",
            "",
            "| Date | State | Draw | Winner | VCode | Index | Ordered Rank | Boxed Rank | Enhanced Rank | Classes |",
            "|---|---|---|---|---|---:|---:|---:|---:|---|",
        ]
    )
    for row in rows:
        classes = ", ".join(row.get("classification") or [])
        lines.append(
            f"| {row.get('date')} | {row.get('state')} | {row.get('draw_label')} | {row.get('winner_literal')} | {row.get('winner_ordered_vcode') or '-'} | {row.get('winner_boxed_vtrac_index') or '-'} | {row.get('arena_ordered_vcode_rank') or '-'} | {row.get('arena_boxed_index_rank') or '-'} | {row.get('enhanced_index_rank') or '-'} | {classes} |"
        )
    lines.extend(
        [
            "",
            "## Interpretation Guardrail",
            "",
            "This harness evaluates evidence preservation only. It does not prove live prediction quality, change scoring, change budgets, or promote candidates into final plays.",
        ]
    )
    return "\n".join(lines) + "\n"


def _case_from_winner(
    *,
    date: str,
    winner_json: Path,
    day_dir: Path,
    sharepacks_root: Path,
    results_map: Mapping[str, Mapping[str, str]],
    arena_payload_cache: Dict[Tuple[str, str], Optional[Dict[str, Any]]],
    profile: str,
    experiment_tag: str,
    top_items: int,
    per_case_dir: Path,
) -> Dict[str, Any]:
    state = winner_json.parent.name
    winner_payload = _read_json(winner_json)
    winner_literal = _digits_only(winner_payload.get("winner_combo") if isinstance(winner_payload, dict) else "")
    winner_index = get_vtrac_index(winner_literal) if len(winner_literal) == 3 else None
    draw_label = _draw_label_for_winner(results_map, state, winner_literal)
    enhanced_json = _find_latest_enhanced_json(day_dir, state)
    case_stem = f"{date}__{state}__{draw_label}__{winner_literal}__VTRAC_CORRIDOR_ARENA_HARNESS".replace("+", "_")

    base: Dict[str, Any] = {
        "date": date,
        "state": state,
        "draw_label": draw_label,
        "winner_literal": winner_literal,
        "winner_canonical": _canon(winner_literal),
        "winner_boxed_vtrac_index": winner_index,
        "winner_ordered_vcode": ordered_vcode_for_combo(winner_literal) if winner_index is not None else None,
        "winner_ordered_lane_8": vstraight_lane_for_combo(winner_literal) if winner_index is not None else [],
        "winner_json_path": _safe_rel(winner_json),
        "enhanced_json_path": _safe_rel(enhanced_json) if enhanced_json else None,
    }

    if winner_index is None:
        base.update(
            {
                "classification": classify_case(
                    ordered_lane_match=False,
                    boxed_corridor_match=False,
                    enhanced_index_rank=None,
                    winner_pattern_hits=0,
                    renderer_gap=False,
                    draw_data_inflation_warning=False,
                    source_index_mismatch_count=0,
                    unsupported_triple=True,
                ),
                "skip_reason": "winner has no boxed VTRAC index in current VTRAC reference semantics",
                "source_index_mismatch_count": 0,
            }
        )
        return base

    corridor_summary = create_corridor_summary(
        winner_json_path=winner_json,
        enhanced_json_path=enhanced_json,
        date=date,
        state=state,
        winner=winner_literal,
    )

    cache_key = (date, state)
    if cache_key not in arena_payload_cache:
        arena_payload_cache[cache_key] = _arena_payload_for_state(
            day_dir=day_dir,
            sharepacks_root=sharepacks_root,
            date=date,
            state=state,
            profile=profile,
            experiment_tag=experiment_tag,
            top_items=top_items,
        )
    arena_payload = arena_payload_cache[cache_key]

    arena_objects: Dict[str, Any] = {}
    if isinstance(arena_payload, dict):
        vtrac_tool = ((arena_payload.get("string_tools") or {}).get("vtrac_analyzer") or {})
        if isinstance(vtrac_tool, dict) and isinstance(vtrac_tool.get("arena_objects"), dict):
            arena_objects = vtrac_tool["arena_objects"]

    ordered_rows = arena_objects.get("ordered_lane_corridors") if isinstance(arena_objects.get("ordered_lane_corridors"), list) else []
    boxed_rows = arena_objects.get("boxed_index_corridors") if isinstance(arena_objects.get("boxed_index_corridors"), list) else []
    ordered_rank, ordered_row = _ranked_match(ordered_rows, "ordered_vcode", base["winner_ordered_vcode"])
    boxed_rank, boxed_row = _ranked_match(boxed_rows, "boxed_vtrac_index", winner_index)
    mismatch_count = sum(1 for row in [*ordered_rows, *boxed_rows] if isinstance(row, dict) and row.get("source_index_mismatch"))

    evidence = corridor_summary.get("winner_json_evidence") or {}
    row_scopes = evidence.get("row_scope_breakout") or {}
    literal_pattern = ((row_scopes.get("literal_permutation_exposure") or {}).get("pattern_rows_only") or {})
    ordered_pattern = ((row_scopes.get("ordered_lane_exposure") or {}).get("pattern_rows_only") or {})
    boxed_pattern = ((row_scopes.get("boxed_index_corridor_exposure") or {}).get("pattern_rows_only") or {})
    flags = corridor_summary.get("interpretation_flags") or {}
    enhanced = corridor_summary.get("enhanced_vtrac_comparison") or {}

    arena_ordered_witnesses = _top_straights(ordered_row)
    arena_boxed_witnesses = _top_straights(boxed_row)
    winner_ordered_tokens = _top_tokens(ordered_pattern)
    winner_boxed_tokens = _top_tokens(boxed_pattern)
    ordered_overlap = sorted(set(arena_ordered_witnesses) & set(winner_ordered_tokens))
    boxed_overlap = sorted(set(arena_boxed_witnesses) & set(winner_boxed_tokens))

    classification = classify_case(
        ordered_lane_match=ordered_rank is not None,
        boxed_corridor_match=boxed_rank is not None,
        enhanced_index_rank=enhanced.get("target_index_rank"),
        winner_pattern_hits=_to_int(boxed_pattern.get("strict_cell_hits")),
        renderer_gap=bool(flags.get("renderer_gap")),
        draw_data_inflation_warning=bool(flags.get("draw_data_inflation_warning")),
        source_index_mismatch_count=mismatch_count,
        missing_predictive_state=arena_payload is None,
    )

    base.update(
        {
            "arena_ordered_vcode_rank": ordered_rank,
            "arena_ordered_vcode_score": ordered_row.get("score_total") if isinstance(ordered_row, dict) else None,
            "arena_ordered_vcode_in_default_top12": bool(ordered_rank is not None and ordered_rank <= 12),
            "arena_boxed_index_rank": boxed_rank,
            "arena_boxed_index_score": boxed_row.get("score_total") if isinstance(boxed_row, dict) else None,
            "arena_boxed_index_in_default_top12": bool(boxed_rank is not None and boxed_rank <= 12),
            "enhanced_index_rank": enhanced.get("target_index_rank"),
            "enhanced_index_score": enhanced.get("target_index_score"),
            "literal_pattern_hits": _to_int(literal_pattern.get("strict_cell_hits")),
            "ordered_lane_pattern_hits": _to_int(ordered_pattern.get("strict_cell_hits")),
            "boxed_corridor_pattern_hits": _to_int(boxed_pattern.get("strict_cell_hits")),
            "renderer_gap": bool(flags.get("renderer_gap")),
            "analyzer_gap": bool(flags.get("analyzer_gap")),
            "draw_data_inflation_warning": bool(flags.get("draw_data_inflation_warning")),
            "source_index_mismatch_count": mismatch_count,
            "semantic_guardrails": arena_objects.get("semantic_guardrails") if isinstance(arena_objects.get("semantic_guardrails"), dict) else {},
            "arena_ordered_top_witnesses": ", ".join(arena_ordered_witnesses),
            "winner_ordered_top_tokens": ", ".join(winner_ordered_tokens),
            "ordered_witness_overlap": ", ".join(ordered_overlap),
            "arena_boxed_top_witnesses": ", ".join(arena_boxed_witnesses),
            "winner_boxed_top_tokens": ", ".join(winner_boxed_tokens),
            "boxed_witness_overlap": ", ".join(boxed_overlap),
            "classification": classification,
            "corridor_summary": corridor_summary,
            "arena_match_rows": {
                "ordered_lane": ordered_row,
                "boxed_index": boxed_row,
            },
        }
    )

    _write_json(per_case_dir / f"{case_stem}.json", base)
    _write_text(per_case_dir / f"{case_stem}.md", _case_summary_markdown(base))
    return base


def run_harness(
    *,
    date_start: str,
    date_end: str,
    states: Sequence[str],
    sharepacks_root: Path,
    winners_root: Path,
    output_root: Path,
    profile: str,
    experiment_tag: str,
    top_items: int,
) -> Dict[str, Any]:
    dates = _iter_dates(date_start, date_end)
    run_label = dates[0] if len(dates) == 1 else f"{dates[0]}_to_{dates[-1]}"
    output_dir = output_root / run_label
    per_case_dir = output_dir / "per_case"
    arena_payload_cache: Dict[Tuple[str, str], Optional[Dict[str, Any]]] = {}

    cases: List[Dict[str, Any]] = []
    missing_winner_dates: List[str] = []
    duplicate_winner_artifacts: List[Dict[str, str]] = []
    for date in dates:
        day_dir = sharepacks_root / date
        results_map = _read_results_map(date)
        winner_jsons, duplicate_receipts = _iter_winner_jsons(
            winners_root,
            date,
            states,
        )
        duplicate_winner_artifacts.extend(duplicate_receipts)
        if not winner_jsons:
            missing_winner_dates.append(date)
            continue
        for winner_json in winner_jsons:
            cases.append(
                _case_from_winner(
                    date=date,
                    winner_json=winner_json,
                    day_dir=day_dir,
                    sharepacks_root=sharepacks_root,
                    results_map=results_map,
                    arena_payload_cache=arena_payload_cache,
                    profile=profile,
                    experiment_tag=experiment_tag,
                    top_items=top_items,
                    per_case_dir=per_case_dir,
                )
            )

    class_counts: Dict[str, int] = {}
    for case in cases:
        for label in case.get("classification") or []:
            class_counts[str(label)] = class_counts.get(str(label), 0) + 1

    payload = {
        "schema": "aat9.vtrac_corridor_arena_harness.v1",
        "review_only": True,
        "run_label": run_label,
        "date_start": dates[0],
        "date_end": dates[-1],
        "states": list(states),
        "sharepacks_root": _safe_rel(sharepacks_root),
        "winners_root": _safe_rel(winners_root),
        "top_items": top_items,
        "profile": profile,
        "experiment_tag": experiment_tag,
        "missing_winner_dates": missing_winner_dates,
        "duplicate_winner_artifacts": duplicate_winner_artifacts,
        "class_counts": class_counts,
        "cases": cases,
    }

    csv_fields = [
        "date",
        "state",
        "draw_label",
        "winner_literal",
        "winner_canonical",
        "winner_ordered_vcode",
        "winner_boxed_vtrac_index",
        "arena_ordered_vcode_rank",
        "arena_ordered_vcode_score",
        "arena_ordered_vcode_in_default_top12",
        "arena_boxed_index_rank",
        "arena_boxed_index_score",
        "arena_boxed_index_in_default_top12",
        "enhanced_index_rank",
        "enhanced_index_score",
        "literal_pattern_hits",
        "ordered_lane_pattern_hits",
        "boxed_corridor_pattern_hits",
        "renderer_gap",
        "analyzer_gap",
        "draw_data_inflation_warning",
        "source_index_mismatch_count",
        "ordered_witness_overlap",
        "boxed_witness_overlap",
        "classification",
        "winner_json_path",
        "enhanced_json_path",
    ]
    csv_rows = []
    for case in cases:
        row = dict(case)
        row["classification"] = "|".join(case.get("classification") or [])
        csv_rows.append(row)

    stem = f"VTRAC_CORRIDOR_ARENA_HARNESS__{run_label}"
    _write_json(output_dir / f"{stem}.json", payload)
    _write_text(output_dir / f"{stem}.md", _summary_markdown(payload))
    _write_csv(output_dir / f"{stem}.csv", csv_rows, csv_fields)
    return payload


def _parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--date", help="Single YYYY-MM-DD date. Overrides --start-date/--end-date if provided.")
    ap.add_argument("--start-date", default="2026-03-09")
    ap.add_argument("--end-date")
    ap.add_argument("--states", nargs="*", default=[])
    ap.add_argument("--sharepacks-root", default="sharepacks/_predictive")
    ap.add_argument("--winners-root", default="reports/stable/winners_by_date_fixed")
    ap.add_argument("--output-root", default="tasks/analysis_arena_d/harness_outputs/VTRAC_CORRIDOR_HARNESS")
    ap.add_argument("--profile", default="tool_only")
    ap.add_argument("--experiment-tag", default="arena_v0")
    ap.add_argument("--top-items", type=int, default=48)
    return ap.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = _parse_args(argv)
    start = args.date or args.start_date
    end = args.date or args.end_date or start
    payload = run_harness(
        date_start=start,
        date_end=end,
        states=args.states,
        sharepacks_root=(REPO_ROOT / args.sharepacks_root).resolve(),
        winners_root=(REPO_ROOT / args.winners_root).resolve(),
        output_root=(REPO_ROOT / args.output_root).resolve(),
        profile=args.profile,
        experiment_tag=args.experiment_tag,
        top_items=args.top_items,
    )
    out_dir = REPO_ROOT / args.output_root / str(payload.get("run_label"))
    print(f"Wrote VTRAC corridor Arena harness: {_safe_rel(out_dir)}")
    print(f"Cases: {len(payload.get('cases') or [])}")
    print(f"Class counts: {payload.get('class_counts')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
