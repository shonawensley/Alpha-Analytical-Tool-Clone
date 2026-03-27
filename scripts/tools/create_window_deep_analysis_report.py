#!/usr/bin/env python3
"""Create a Codex-style deep analysis report for an Analysis Arena window."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.tools.analysis_arena_window_utils import (
    analysis_dir,
    iter_window_dates,
    load_scoreboard,
    load_shadow,
    load_translation_manifest,
    load_state_seed_from_manifest_entry,
    read_json,
    safe_rel,
    validation_dir,
)


def _parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--window-root", required=True, help="RUNS_2 window root (WINDOW_<...>/)")
    ap.add_argument(
        "--performance-gap-json",
        default="",
        help="Optional performance-gap JSON. Defaults to the canonical output name inside the window root.",
    )
    ap.add_argument("--out-md", default="", help="Optional markdown output path.")
    ap.add_argument("--out-json", default="", help="Optional JSON output path.")
    ap.add_argument("--force", action="store_true", help="Overwrite existing outputs.")
    return ap.parse_args()


def _window_root_from_arg(value: str) -> Path:
    path = Path(value).expanduser()
    if not path.is_absolute():
        path = (REPO_ROOT / path).resolve()
    return path


def _default_paths(window_root: Path) -> Dict[str, Path]:
    stem = window_root.name
    return {
        "perf_json": window_root / f"{stem}__ANALYSIS_ARENA__PERFORMANCE_GAP.json",
        "md": window_root / f"{stem}__ANALYSIS_ARENA__DEEP_ANALYSIS__CODEX.md",
        "json": window_root / f"{stem}__ANALYSIS_ARENA__DEEP_ANALYSIS__CODEX.json",
    }


def _write_text(path: Path, text: str, *, force: bool) -> None:
    if path.exists() and not force:
        raise SystemExit(f"Refusing to overwrite existing file without --force: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _write_json(path: Path, payload: Any, *, force: bool) -> None:
    _write_text(path, json.dumps(payload, indent=2, sort_keys=True) + "\n", force=force)


def _fmt_top(counter: Counter[str], *, limit: int = 8) -> List[Dict[str, Any]]:
    return [{"value": value, "count": count} for value, count in counter.most_common(limit)]


def _read_csv_rows(path: Path) -> List[Dict[str, str]]:
    import csv

    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", errors="replace", newline="") as fh:
        return [{k: (v or "") for k, v in row.items()} for row in csv.DictReader(fh)]


def _load_doubles_inventory(window_root: Path) -> List[Dict[str, str]]:
    matches = sorted(validation_dir(window_root).glob("*__DOUBLES_MIRROR_DOUBLES__INVENTORY.csv"))
    return _read_csv_rows(matches[0]) if matches else []


def _narrative_payload(window_root: Path, perf_payload: Dict[str, Any]) -> Dict[str, Any]:
    dates = iter_window_dates(window_root)
    winner_rows = perf_payload.get("ledger_rows") or []
    top_state_counter: Counter[str] = Counter()
    role_counter: Counter[str] = Counter()
    posture_counter: Counter[str] = Counter()
    primary_targets: Counter[str] = Counter()
    best_clean_hosts: Counter[str] = Counter()
    shared_canonicals: Counter[str] = Counter()
    shared_vt: Counter[str] = Counter()
    day_primary_targets: List[Dict[str, Any]] = []
    carryover_pairs: Counter[str] = Counter()
    boxed_counter: Counter[str] = Counter()
    straight_counter: Counter[str] = Counter()
    vt_box_counter: Counter[str] = Counter()
    preserved_counter: Counter[str] = Counter()
    previous_day_canonicals: set[str] = set()

    for results_date in dates:
        scoreboard = load_scoreboard(window_root, results_date)
        shadow = load_shadow(window_root, results_date)
        manifest = load_translation_manifest(window_root, results_date)
        board_verdict = scoreboard.get("board_verdict") or {}
        rows = scoreboard.get("scoreboard_rows") or []
        for row in sorted(rows, key=lambda item: int(item.get("score_rank") or 9999))[:5]:
            state_key = str(row.get("state_key") or "").strip()
            if state_key:
                top_state_counter[state_key] += 1
            role = str(row.get("role") or "").strip()
            if role:
                role_counter[role] += 1
            for canonical in (row.get("top_canonicals") or [])[:3]:
                if str(canonical).strip():
                    shared_canonicals[str(canonical).strip()] += 1
            for vt in (row.get("top_vtrac_indices") or [])[:3]:
                if str(vt).strip():
                    shared_vt[str(vt).strip()] += 1
        state_decisions = shadow.get("state_decisions") or []
        for decision in state_decisions:
            posture = str(decision.get("posture") or "").strip()
            if posture:
                posture_counter[posture] += 1
        if board_verdict.get("top_primary_target"):
            primary_targets[str(board_verdict["top_primary_target"])] += 1
        if board_verdict.get("best_clean_host"):
            best_clean_hosts[str(board_verdict["best_clean_host"])] += 1
        day_primary_targets.append(
            {
                "date": results_date,
                "top_primary_target": board_verdict.get("top_primary_target", ""),
                "best_clean_host": board_verdict.get("best_clean_host", ""),
                "secondary_target": board_verdict.get("secondary_target", ""),
            }
        )
        current_day_canonicals: set[str] = set()
        for entry in manifest.get("state_receipts") or []:
            seed = load_state_seed_from_manifest_entry(entry)
            brain1 = seed.get("brain1_core") or {}
            sandbox = seed.get("sandbox_hypotheses") or {}
            control_arm = seed.get("control_arm") or {}
            for canonical in (brain1.get("dominant_canonicals") or [])[:4]:
                value = str(canonical).strip()
                if value:
                    current_day_canonicals.add(value)
            for item in sandbox.get("diagnostic_boxed_seed") or []:
                if isinstance(item, dict) and str(item.get("value")).strip():
                    boxed_counter[str(item["value"]).strip()] += 1
            for item in sandbox.get("diagnostic_straight_seed") or []:
                if isinstance(item, dict) and str(item.get("value")).strip():
                    straight_counter[str(item["value"]).strip()] += 1
            for item in sandbox.get("diagnostic_vt_box_seed") or []:
                if isinstance(item, dict) and str(item.get("value")).strip():
                    vt_box_counter[str(item["value"]).strip()] += 1
            for value in control_arm.get("preserved_not_budgeted_canonicals_top") or []:
                value = str(value).strip()
                if value:
                    preserved_counter[value] += 1
        for canonical in sorted(current_day_canonicals & previous_day_canonicals):
            carryover_pairs[canonical] += 1
        previous_day_canonicals = current_day_canonicals

    doubles_rows = _load_doubles_inventory(window_root)
    doubles_counter = Counter(str(row.get("type") or "").strip() or "_none_" for row in doubles_rows)

    opportunity_gap_rows = [
        row for row in winner_rows if row.get("opportunity_gap_box") or row.get("opportunity_gap_exact")
    ]
    best_realized_rows = [
        row
        for row in winner_rows
        if row.get("play_card_any_box") or row.get("play_card_any_exact") or row.get("cu_box") or row.get("cu_exact")
    ]
    direct_miss_rows = [
        row for row in winner_rows if not row.get("winner_on_board") and not row.get("arena_box_signal")
    ]

    return {
        "metadata": perf_payload.get("metadata") or {},
        "window_overview": {
            "winner_events": len(winner_rows),
            "day_count": len(dates),
            "top_board_states": _fmt_top(top_state_counter, limit=10),
            "board_roles": _fmt_top(role_counter, limit=10),
            "shadow_postures": _fmt_top(posture_counter, limit=10),
        },
        "board_truth_read": {
            "primary_targets": _fmt_top(primary_targets, limit=8),
            "best_clean_hosts": _fmt_top(best_clean_hosts, limit=8),
            "daily_targets": day_primary_targets,
        },
        "shared_complexes": {
            "repeated_canonicals": _fmt_top(shared_canonicals, limit=12),
            "repeated_vtrac_indices": _fmt_top(shared_vt, limit=10),
            "carryover_canonicals": _fmt_top(carryover_pairs, limit=10),
        },
        "tracker_families": {
            "tracker_attribution": perf_payload.get("tracker_attribution") or {},
            "doubles_result_types": dict(doubles_counter.most_common()),
        },
        "translational_pressure": {
            "boxed_seeds": _fmt_top(boxed_counter, limit=10),
            "straight_seeds": _fmt_top(straight_counter, limit=10),
            "vt_box_seeds": _fmt_top(vt_box_counter, limit=10),
            "preserved_not_budgeted": _fmt_top(preserved_counter, limit=10),
        },
        "best_findings": {
            "control_arm_realized_rows": best_realized_rows[:12],
            "opportunity_gap_rows": opportunity_gap_rows[:12],
            "direct_miss_rows": direct_miss_rows[:12],
        },
        "promotion_ledger": {
            "preserve": [
                "Keep arena truth quality, control-arm realization, and opportunity gap as separate evaluation layers.",
                "Keep translation sandbox seeds and preserved-not-budgeted canonicals as explicit translator-learning inputs.",
            ],
            "observe": [
                "Repeated carryover canonicals across consecutive days.",
                "Tracker families that consistently show arena-box support but weak downstream realization.",
            ],
            "demote": [
                "Using B12/B24/B36 alone as the main measure of analysis quality.",
            ],
        },
    }


def _render_markdown(payload: Dict[str, Any], *, perf_json_path: Path) -> str:
    meta = payload["metadata"]
    overview = payload["window_overview"]
    board = payload["board_truth_read"]
    shared = payload["shared_complexes"]
    trackers = payload["tracker_families"]
    pressure = payload["translational_pressure"]
    findings = payload["best_findings"]
    promotion = payload["promotion_ledger"]
    lines: List[str] = []
    lines.append("# Analysis Arena Window Deep Analysis Report")
    lines.append("")
    lines.append("## 1. Window Overview")
    lines.append("")
    lines.append(f"- Window root: `{meta.get('window_root', '')}`")
    lines.append(f"- Dates: `{meta.get('window_dates', [''])[0]}` to `{meta.get('window_dates', [''])[-1]}`" if meta.get("window_dates") else "- Dates: _none_")
    lines.append(f"- Winner events reviewed: `{overview['winner_events']}`")
    lines.append(f"- Day count: `{overview['day_count']}`")
    lines.append(f"- Performance gap metrics source: `{safe_rel(perf_json_path)}`")
    lines.append("")
    lines.append("## 2. Board-Level Truth Read")
    lines.append("")
    lines.append(
        "- Top board states across the window: "
        + (", ".join(f"`{row['value']}` x{row['count']}" for row in overview["top_board_states"]) or "_none_")
    )
    lines.append(
        "- Repeated board roles: "
        + (", ".join(f"`{row['value']}` x{row['count']}" for row in overview["board_roles"]) or "_none_")
    )
    lines.append(
        "- Repeated top primary targets: "
        + (", ".join(f"`{row['value']}` x{row['count']}" for row in board["primary_targets"]) or "_none_")
    )
    lines.append(
        "- Repeated best clean hosts: "
        + (", ".join(f"`{row['value']}` x{row['count']}" for row in board["best_clean_hosts"]) or "_none_")
    )
    lines.append("")
    lines.append("## 3. Shared Complexes / Carryover / Decay")
    lines.append("")
    lines.append(
        "- Repeated canonicals: "
        + (", ".join(f"`{row['value']}` x{row['count']}" for row in shared["repeated_canonicals"]) or "_none_")
    )
    lines.append(
        "- Repeated VTRAC indices: "
        + (", ".join(f"`{row['value']}` x{row['count']}" for row in shared["repeated_vtrac_indices"]) or "_none_")
    )
    lines.append(
        "- Carryover canonicals across consecutive days: "
        + (", ".join(f"`{row['value']}` x{row['count']}" for row in shared["carryover_canonicals"]) or "_none_")
    )
    lines.append("")
    lines.append("## 4. Tracker Families")
    lines.append("")
    for key, value in (trackers.get("tracker_attribution") or {}).items():
        label = key.replace("_support", "").replace("_", " ")
        lines.append(
            f"- {label}: events=`{value.get('events', 0)}` arena_box=`{value.get('arena_box_signal', 0)}` "
            f"play_box=`{value.get('play_card_box', 0)}` gap_box=`{value.get('opportunity_gap_box', 0)}`"
        )
    lines.append(
        "- Doubles result types: "
        + (", ".join(f"`{k}` x{v}" for k, v in (trackers.get("doubles_result_types") or {}).items()) or "_none_")
    )
    lines.append("")
    lines.append("## 5. Translational Pressure")
    lines.append("")
    lines.append(
        "- Boxed seeds: "
        + (", ".join(f"`{row['value']}` x{row['count']}" for row in pressure["boxed_seeds"]) or "_none_")
    )
    lines.append(
        "- Straight seeds: "
        + (", ".join(f"`{row['value']}` x{row['count']}" for row in pressure["straight_seeds"]) or "_none_")
    )
    lines.append(
        "- VT-box seeds: "
        + (", ".join(f"`{row['value']}` x{row['count']}" for row in pressure["vt_box_seeds"]) or "_none_")
    )
    lines.append(
        "- Preserved-not-budgeted canonicals: "
        + (", ".join(f"`{row['value']}` x{row['count']}" for row in pressure["preserved_not_budgeted"]) or "_none_")
    )
    lines.append("")
    lines.append("## 6. Best Findings / Worst Misses")
    lines.append("")
    lines.append(f"- Control-arm realized rows sampled: `{len(findings['control_arm_realized_rows'])}`")
    lines.append(f"- Opportunity-gap rows sampled: `{len(findings['opportunity_gap_rows'])}`")
    lines.append(f"- Direct miss rows sampled: `{len(findings['direct_miss_rows'])}`")
    lines.append("")
    lines.append("## 7. Promotion Ledger")
    lines.append("")
    for item in promotion["preserve"]:
        lines.append(f"- Preserve: {item}")
    for item in promotion["observe"]:
        lines.append(f"- Observe: {item}")
    for item in promotion["demote"]:
        lines.append(f"- Demote: {item}")
    return "\n".join(lines) + "\n"


def main() -> None:
    args = _parse_args()
    window_root = _window_root_from_arg(args.window_root)
    defaults = _default_paths(window_root)
    perf_json = _window_root_from_arg(args.performance_gap_json) if args.performance_gap_json else defaults["perf_json"]
    out_md = _window_root_from_arg(args.out_md) if args.out_md else defaults["md"]
    out_json = _window_root_from_arg(args.out_json) if args.out_json else defaults["json"]

    perf_payload = read_json(perf_json)
    if not isinstance(perf_payload, dict):
        raise SystemExit(f"Performance gap JSON is not an object: {perf_json}")
    ledger_path = perf_payload.get("ledger_path")
    ledger_rows: List[Dict[str, Any]] = []
    if ledger_path:
        ledger_file = _window_root_from_arg(str(ledger_path))
        import csv

        if ledger_file.exists():
            with ledger_file.open("r", encoding="utf-8", errors="replace", newline="") as fh:
                ledger_rows = [{k: (v or "") for k, v in row.items()} for row in csv.DictReader(fh)]
    perf_payload["ledger_rows"] = ledger_rows

    narrative = _narrative_payload(window_root, perf_payload)
    narrative["schema_version"] = "analysis_arena_window_deep_analysis/v1"
    narrative["performance_gap_json"] = safe_rel(perf_json)

    _write_json(out_json, narrative, force=args.force)
    _write_text(out_md, _render_markdown(narrative, perf_json_path=perf_json), force=args.force)
    print(f"Wrote: {safe_rel(out_md)}")
    print(f"Wrote: {safe_rel(out_json)}")


if __name__ == "__main__":
    main()
