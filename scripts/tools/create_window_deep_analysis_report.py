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
    load_brain2_tracker_ledger,
    load_scoreboard,
    load_shadow,
    load_translation_manifest,
    load_state_seed_from_manifest_entry,
    read_json,
    safe_rel,
    validation_dir,
)
from scripts.tools.brain2_rank_contract import input_order_key, rank_evaluation_status


def _parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--window-root", required=True, help="RUNS_2 window root (WINDOW_<...>/)")
    ap.add_argument(
        "--performance-gap-json",
        default="",
        help="Optional performance-gap JSON. Defaults to the canonical output name inside the window root.",
    )
    ap.add_argument(
        "--frontier-json",
        default="",
        help="Optional C1/C2 frontier harness JSON. Defaults to the canonical output name inside the window root.",
    )
    ap.add_argument(
        "--pure-arena-scorecard-json",
        default="",
        help="Optional pure arena finalist scorecard JSON. Defaults to the canonical output name inside the window root.",
    )
    ap.add_argument(
        "--translator-ledger-json",
        default="",
        help="Optional translator-learning ledger JSON. Defaults to the canonical output name inside the window root.",
    )
    ap.add_argument(
        "--decay-json",
        default="",
        help="Optional decay/carryover scorecard JSON. Defaults to the canonical output name inside the window root.",
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
        "frontier_json": window_root / f"{stem}__ANALYSIS_ARENA__C1_C2_FRONTIER_ANALYSIS.json",
        "pure_arena_json": window_root / f"{stem}__ANALYSIS_ARENA__PURE_FINALIST_SCORECARD.json",
        "translator_json": window_root / f"{stem}__ANALYSIS_ARENA__TRANSLATOR_LEARNING_LEDGER.json",
        "decay_json": window_root / f"{stem}__ANALYSIS_ARENA__DECAY_CARRYOVER_SCORECARD.json",
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


def _pct(value: float) -> str:
    return f"{100.0 * value:.1f}%"


def _fmt_top(counter: Counter[str], *, limit: int = 8) -> List[Dict[str, Any]]:
    return [{"value": value, "count": count} for value, count in counter.most_common(limit)]


def _render_top_rows(rows: Iterable[Dict[str, Any]]) -> str:
    return ", ".join(f"`{row['value']}` x{row['count']}" for row in rows) or "_none_"


def _read_csv_rows(path: Path) -> List[Dict[str, str]]:
    import csv

    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", errors="replace", newline="") as fh:
        return [{k: (v or "") for k, v in row.items()} for row in csv.DictReader(fh)]


def _load_doubles_inventory(window_root: Path) -> List[Dict[str, str]]:
    matches = sorted(validation_dir(window_root).glob("*__DOUBLES_MIRROR_DOUBLES__INVENTORY.csv"))
    return _read_csv_rows(matches[0]) if matches else []


def _narrative_payload(
    window_root: Path,
    perf_payload: Dict[str, Any],
    *,
    frontier_payload: Dict[str, Any] | None = None,
    pure_arena_payload: Dict[str, Any] | None = None,
    translator_payload: Dict[str, Any] | None = None,
    decay_payload: Dict[str, Any] | None = None,
) -> Dict[str, Any]:
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
    tracker_ledger_days = 0
    profit_alert_state_counter: Counter[str] = Counter()
    compound_event_counter: Counter[str] = Counter()
    blackapple_alert_counter: Counter[str] = Counter()
    blackapple_watch_counter: Counter[str] = Counter()
    due_threshold_counter: Counter[str] = Counter()
    repeat_watch_hit_counter: Counter[str] = Counter()
    hint_profit_counter: Counter[str] = Counter()
    hint_compound_counter: Counter[str] = Counter()
    hint_blackapple_counter: Counter[str] = Counter()
    hint_due_counter: Counter[str] = Counter()
    hint_consensus_counter: Counter[str] = Counter()
    previous_day_canonicals: set[str] = set()
    rank_contract_rows: List[Dict[str, Any]] = []

    for results_date in dates:
        scoreboard = load_scoreboard(window_root, results_date)
        shadow = load_shadow(window_root, results_date)
        manifest = load_translation_manifest(window_root, results_date)
        board_verdict = scoreboard.get("board_verdict") or {}
        rows = [row for row in (scoreboard.get("scoreboard_rows") or []) if isinstance(row, dict)]
        rank_contract_rows.extend(rows)
        day_rank_evaluation = rank_evaluation_status(rows)
        for row in sorted(rows, key=input_order_key):
            state_key = str(row.get("state_key") or "").strip()
            if state_key and day_rank_evaluation["evaluable"]:
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
        if day_rank_evaluation["evaluable"] and board_verdict.get("top_primary_target"):
            primary_targets[str(board_verdict["top_primary_target"])] += 1
        if day_rank_evaluation["evaluable"] and board_verdict.get("best_clean_host"):
            best_clean_hosts[str(board_verdict["best_clean_host"])] += 1
        day_primary_targets.append(
            {
                "date": results_date,
                "rank_evaluation_status": day_rank_evaluation["status"],
                "top_primary_target": (
                    board_verdict.get("top_primary_target", "")
                    if day_rank_evaluation["evaluable"]
                    else None
                ),
                "best_clean_host": (
                    board_verdict.get("best_clean_host", "")
                    if day_rank_evaluation["evaluable"]
                    else None
                ),
                "secondary_target": (
                    board_verdict.get("secondary_target", "")
                    if day_rank_evaluation["evaluable"]
                    else None
                ),
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

        tracker_ledger = load_brain2_tracker_ledger(window_root, results_date)
        if isinstance(tracker_ledger, dict) and tracker_ledger:
            tracker_ledger_days += 1
            for row in ((tracker_ledger.get("profit_alerts") or {}).get("top_states") or [])[:6]:
                if isinstance(row, dict) and str(row.get("state_key") or "").strip():
                    profit_alert_state_counter[str(row["state_key"]).strip()] += 1
            for row in ((tracker_ledger.get("compound_events") or {}).get("top_rows") or [])[:6]:
                if not isinstance(row, dict):
                    continue
                label = ":".join(
                    part
                    for part in [
                        str(row.get("state_key") or "").strip(),
                        str(row.get("variant") or "").strip(),
                        str(row.get("top_event") or "").strip(),
                    ]
                    if part
                )
                if label:
                    compound_event_counter[label] += 1
            for row in ((tracker_ledger.get("blackapple") or {}).get("alert_states") or [])[:8]:
                if isinstance(row, dict) and str(row.get("state_key") or "").strip():
                    blackapple_alert_counter[str(row["state_key"]).strip()] += 1
            for row in ((tracker_ledger.get("blackapple") or {}).get("watch_states") or [])[:8]:
                if isinstance(row, dict) and str(row.get("state_key") or "").strip():
                    blackapple_watch_counter[str(row["state_key"]).strip()] += 1
            for row in ((tracker_ledger.get("due_doubles") or {}).get("threshold_states") or [])[:8]:
                if isinstance(row, dict) and str(row.get("state_key") or "").strip():
                    due_threshold_counter[str(row["state_key"]).strip()] += 1
            for row in ((tracker_ledger.get("repeat_watch") or {}).get("exact_hits") or [])[:8]:
                if not isinstance(row, dict):
                    continue
                label = ":".join(
                    part
                    for part in [
                        str(row.get("state_key") or "").strip(),
                        str(row.get("variant") or "").strip(),
                        str(row.get("current_index") or "").strip(),
                    ]
                    if part
                )
                if label:
                    repeat_watch_hit_counter[label] += 1
            hint_map = {
                "profit_alerts": hint_profit_counter,
                "compound_events": hint_compound_counter,
                "blackapple": hint_blackapple_counter,
                "due_doubles": hint_due_counter,
                "consensus": hint_consensus_counter,
            }
            for family, counter in hint_map.items():
                carries = ((tracker_ledger.get(family) or {}).get("scoreboard_carries") or [])[:8]
                for row in carries:
                    if isinstance(row, dict) and str(row.get("state_key") or "").strip():
                        counter[str(row["state_key"]).strip()] += 1

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

    frontier_payload = frontier_payload or {}
    frontier_meta = frontier_payload.get("metadata") or {}
    frontier_signatures = (frontier_payload.get("signature_mix") or {}).get("signature_counts") or {}
    frontier_hit_classes = (frontier_payload.get("signature_mix") or {}).get("hit_class_counts") or {}
    frontier_inventory_types = (frontier_payload.get("signature_mix") or {}).get("inventory_type_counts") or {}
    frontier_score_averages = frontier_payload.get("score_averages") or {}
    frontier_promotion_queue = frontier_payload.get("promotion_queue") or []
    frontier_notable_cases = frontier_payload.get("notable_cases") or {}
    pure_arena_payload = pure_arena_payload or {}
    pure_event_layer = pure_arena_payload.get("event_layer") or {}
    pure_hit_layer = pure_arena_payload.get("hit_layer") or {}
    pure_opp_layer = pure_arena_payload.get("opportunity_layer") or {}
    pure_examples = pure_arena_payload.get("examples") or {}
    pure_interpretation = list(pure_arena_payload.get("interpretation") or [])
    translator_payload = translator_payload or {}
    translator_summary = translator_payload.get("summary") or {}
    translator_examples = translator_payload.get("examples") or {}
    translator_interpretation = list(translator_payload.get("interpretation") or [])
    decay_payload = decay_payload or {}
    decay_meta = decay_payload.get("metadata") or {}
    decay_summary = decay_payload.get("summary") or {}
    decay_metric_rows = decay_payload.get("metric_families") or []
    decay_cohort_rows = decay_payload.get("cohort_panels") or []
    decay_examples = decay_payload.get("examples") or {}
    decay_interpretation = list(decay_payload.get("interpretation") or [])

    rank_evaluation = rank_evaluation_status(rank_contract_rows)
    return {
        "metadata": perf_payload.get("metadata") or {},
        "window_overview": {
            "winner_events": len(winner_rows),
            "day_count": len(dates),
            "top_board_states": _fmt_top(top_state_counter, limit=10),
            "board_roles": _fmt_top(role_counter, limit=10),
            "shadow_postures": _fmt_top(posture_counter, limit=10),
            "rank_evaluation": rank_evaluation,
        },
        "board_truth_read": {
            "rank_evaluation": rank_evaluation,
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
            "daily_tracker_ledgers_present": {
                "count": tracker_ledger_days,
                "denominator": len(dates),
            },
            "daily_tracker_rollup": {
                "profit_alert_states": _fmt_top(profit_alert_state_counter, limit=8),
                "compound_event_leads": _fmt_top(compound_event_counter, limit=8),
                "blackapple_alert_states": _fmt_top(blackapple_alert_counter, limit=8),
                "blackapple_watch_states": _fmt_top(blackapple_watch_counter, limit=8),
                "due_threshold_states": _fmt_top(due_threshold_counter, limit=8),
                "repeat_watch_exact_hits": _fmt_top(repeat_watch_hit_counter, limit=8),
                "scoreboard_hint_profit_alert": _fmt_top(hint_profit_counter, limit=8),
                "scoreboard_hint_compound_event": _fmt_top(hint_compound_counter, limit=8),
                "scoreboard_hint_blackapple": _fmt_top(hint_blackapple_counter, limit=8),
                "scoreboard_hint_due_double": _fmt_top(hint_due_counter, limit=8),
                "scoreboard_hint_r_consensus": _fmt_top(hint_consensus_counter, limit=8),
            },
        },
        "translational_pressure": {
            "boxed_seeds": _fmt_top(boxed_counter, limit=10),
            "straight_seeds": _fmt_top(straight_counter, limit=10),
            "vt_box_seeds": _fmt_top(vt_box_counter, limit=10),
            "preserved_not_budgeted": _fmt_top(preserved_counter, limit=10),
        },
        "winner_html_frontier": {
            "case_count": int(frontier_meta.get("case_count") or 0),
            "warnings": list(frontier_meta.get("warnings") or []),
            "signature_counts": dict(sorted(frontier_signatures.items(), key=lambda item: (-int(item[1]), item[0]))),
            "hit_class_counts": dict(sorted(frontier_hit_classes.items(), key=lambda item: (-int(item[1]), item[0]))),
            "inventory_type_counts": dict(sorted(frontier_inventory_types.items(), key=lambda item: (-int(item[1]), item[0]))),
            "score_averages": frontier_score_averages,
            "promotion_queue": frontier_promotion_queue,
            "notable_cases": frontier_notable_cases,
        },
        "pure_arena_finalist_layer": {
            "event_layer": pure_event_layer,
            "hit_layer": pure_hit_layer,
            "opportunity_layer": pure_opp_layer,
            "candidate_examples": pure_examples.get("candidate_supported_hits") or [],
            "gap_examples": pure_examples.get("opportunity_gap_examples") or [],
            "interpretation": pure_interpretation,
        },
        "translator_learning_ledger": {
            "summary": translator_summary,
            "priority_examples": translator_examples.get("priority_rows") or [],
            "gap_examples": translator_examples.get("gap_rows") or [],
            "converted_examples": translator_examples.get("converted_rows") or [],
            "interpretation": translator_interpretation,
        },
        "decay_carryover": {
            "metadata": decay_meta,
            "summary": decay_summary,
            "metric_families": decay_metric_rows,
            "cohort_panels": decay_cohort_rows,
            "future_day_examples": decay_examples.get("future_day_decay") or [],
            "carryforward_examples": decay_examples.get("same_day_carryforward") or [],
            "interpretation": decay_interpretation,
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
    pure_arena = payload["pure_arena_finalist_layer"]
    translator = payload["translator_learning_ledger"]
    decay = payload["decay_carryover"]
    frontier = payload["winner_html_frontier"]
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
    if not (overview.get("rank_evaluation") or {}).get("evaluable"):
        lines.append("- Top board states across the window: `NOT_EVALUABLE` (`INVALID_STATIC_ORDER`).")
    else:
        lines.append(
            "- Top board states across the window: "
            + (", ".join(f"`{row['value']}` x{row['count']}" for row in overview["top_board_states"]) or "_none_")
        )
    lines.append(
        "- Repeated board roles: "
        + (", ".join(f"`{row['value']}` x{row['count']}" for row in overview["board_roles"]) or "_none_")
    )
    if not (board.get("rank_evaluation") or {}).get("evaluable"):
        lines.append("- Repeated top-primary targets: `NOT_EVALUABLE` (`INVALID_STATIC_ORDER`).")
        lines.append("- Repeated best-clean hosts: `NOT_EVALUABLE` (`INVALID_STATIC_ORDER`).")
    else:
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
    lines.append("## 4. Decay / Carryover Companion")
    lines.append("")
    decay_meta = decay.get("metadata") or {}
    decay_summary = decay.get("summary") or {}
    decay_metric_rows = decay.get("metric_families") or []
    decay_cohort_rows = decay.get("cohort_panels") or []
    if decay_meta:
        lines.append(
            f"- Decay horizon: `{decay_meta.get('decay_upload_days_total', 0)}` total upload days / `{decay_meta.get('decay_draws_total_max', 0)}` total draws max"
        )
        lines.append(
            f"- Tail days required beyond the last snapshot day: `{decay_meta.get('decay_tail_days_required', 0)}`"
        )
    else:
        lines.append("- Decay horizon: _not generated_")
    if decay_summary:
        lines.append(
            f"- State-day snapshots: `{decay_summary.get('state_day_snapshots', 0)}` full_horizon=`{decay_summary.get('full_horizon_rows', 0)}` right_censored=`{decay_summary.get('right_censored_rows', 0)}`"
        )
    metric_lookup = {
        str(row.get("metric_family") or ""): row
        for row in decay_metric_rows
        if isinstance(row, dict)
    }
    for metric_name in ("arena_box_total", "arena_vt_total", "sandbox_exact_seed"):
        row = metric_lookup.get(metric_name)
        if not row:
            continue
        lines.append(
            f"- {row.get('label', metric_name)}: same_day=`{row.get('same_day_resolved', 0)}/{row.get('active_state_days', 0)}` "
            f"horizon=`{row.get('horizon_resolved', 0)}/{row.get('active_state_days', 0)}` "
            f"incremental_decay=`{row.get('incremental_decay_lift', 0)}`"
        )
    cohort_lookup = {
        str(row.get("cohort") or ""): row
        for row in decay_cohort_rows
        if isinstance(row, dict)
    }
    top_primary_cohort = cohort_lookup.get("top_primary_target")
    if top_primary_cohort:
        if top_primary_cohort.get("evaluable") is False:
            lines.append("- Top-primary target decay: `NOT_EVALUABLE` (`INVALID_STATIC_ORDER`).")
        else:
            lines.append(
                f"- Top-primary target decay: same_day=`{top_primary_cohort.get('same_day_resolved', 0)}/{top_primary_cohort.get('state_days', 0)}` "
                f"horizon=`{top_primary_cohort.get('horizon_resolved', 0)}/{top_primary_cohort.get('state_days', 0)}`"
            )
    if decay.get("interpretation"):
        lines.append("- Decay interpretation: " + "; ".join(str(item) for item in (decay.get("interpretation") or [])[:3]))
    lines.append("")
    lines.append("## 5. Tracker Families")
    lines.append("")
    for key, value in (trackers.get("tracker_attribution") or {}).items():
        label = key.replace("_support", "").replace("_", " ")
        lines.append(
            f"- {label}: events=`{value.get('events', 0)}` arena_box=`{value.get('arena_box_signal', 0)}` "
            f"play_box=`{value.get('play_card_box', 0)}` gap_box=`{value.get('opportunity_gap_box', 0)}`"
        )
    ledgers = trackers.get("daily_tracker_rollup") or {}
    ledger_meta = trackers.get("daily_tracker_ledgers_present") or {}
    lines.append(
        f"- Daily tracker ledgers present: `{ledger_meta.get('count', 0)}/{ledger_meta.get('denominator', 0)}`"
    )
    lines.append(
        "- Profit-alert lead states: "
        + _render_top_rows(ledgers.get("profit_alert_states") or [])
    )
    lines.append(
        "- Compound-event leaders: "
        + _render_top_rows(ledgers.get("compound_event_leads") or [])
    )
    lines.append(
        "- Blackapple ALERT states: "
        + _render_top_rows(ledgers.get("blackapple_alert_states") or [])
    )
    lines.append(
        "- Blackapple WATCH states: "
        + _render_top_rows(ledgers.get("blackapple_watch_states") or [])
    )
    lines.append(
        "- Due-double threshold states: "
        + _render_top_rows(ledgers.get("due_threshold_states") or [])
    )
    lines.append(
        "- Repeat-watch exact hits: "
        + _render_top_rows(ledgers.get("repeat_watch_exact_hits") or [])
    )
    hint_chunks = [
        f"profit={_render_top_rows(ledgers.get('scoreboard_hint_profit_alert') or [])}",
        f"compound={_render_top_rows(ledgers.get('scoreboard_hint_compound_event') or [])}",
        f"BA={_render_top_rows(ledgers.get('scoreboard_hint_blackapple') or [])}",
        f"due={_render_top_rows(ledgers.get('scoreboard_hint_due_double') or [])}",
        f"r_consensus={_render_top_rows(ledgers.get('scoreboard_hint_r_consensus') or [])}",
    ]
    lines.append(
        "- Scoreboard hint carries: "
        + "; ".join(hint_chunks)
    )
    lines.append(
        "- Doubles result types: "
        + (", ".join(f"`{k}` x{v}" for k, v in (trackers.get("doubles_result_types") or {}).items()) or "_none_")
    )
    lines.append("")
    lines.append("## 6. Translational Pressure")
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
    lines.append("## 7. Pure Arena Finalist / Candidate Layer")
    lines.append("")
    pure_event = pure_arena.get("event_layer") or {}
    pure_hits = pure_arena.get("hit_layer") or {}
    pure_opp = pure_arena.get("opportunity_layer") or {}
    def _count_rate(block: Dict[str, Any]) -> str:
        if not isinstance(block, dict):
            return "`0/0` (`0.0%`)"
        return f"`{int(block.get('count', 0))}/{int(block.get('denominator', 0))}` (`{_pct(float(block.get('rate', 0.0)))}`)"
    lines.append(f"- Any candidate-like event coverage: {_count_rate(pure_event.get('any_candidate_like_events') or {})}")
    lines.append(f"- VT-like finalist coverage: {_count_rate(pure_event.get('vt_like_events') or {})}")
    lines.append(f"- Box-like candidate coverage: {_count_rate(pure_event.get('boxlike_events') or {})}")
    lines.append(f"- Hit finalist support: {_count_rate(pure_hits.get('finalist_supported_hits') or {})}")
    lines.append(f"- Straight hits with finalist support: {_count_rate(pure_hits.get('straight_with_finalist_support') or {})}")
    lines.append(f"- Strict box hits with finalist support: {_count_rate(pure_hits.get('strict_box_with_finalist_support') or {})}")
    lines.append(f"- Opportunity-gap box rows: {_count_rate(pure_opp.get('opportunity_gap_box_rows') or {})}")
    lines.append(f"- Opportunity-gap rows with explicit arena box: {_count_rate(pure_opp.get('gap_rows_with_explicit_arena_box') or {})}")
    for bullet in pure_arena.get("interpretation") or []:
        lines.append(f"  - {bullet}")
    lines.append("")
    lines.append("## 8. Translator Learning Ledger")
    lines.append("")
    translator_summary = translator.get("summary") or {}
    translator_rates = translator_summary.get("rates") or {}
    lines.append(f"- Translator-learning rows: `{translator_summary.get('translator_rows', 0)}/{translator_summary.get('winner_events', 0)}`")
    lines.append(f"- Box-gap cohort rate: `{_pct(float(translator_rates.get('box_gap_rows', 0.0)))}`")
    lines.append(f"- Exact-gap cohort rate: `{_pct(float(translator_rates.get('exact_gap_rows', 0.0)))}`")
    lines.append(f"- Box-converted cohort rate: `{_pct(float(translator_rates.get('box_converted_rows', 0.0)))}`")
    lines.append(f"- VT-converted cohort rate: `{_pct(float(translator_rates.get('vt_converted_rows', 0.0)))}`")
    lines.append(
        "- Translator cohort counts: "
        + (", ".join(f"`{k}` x{v}" for k, v in (translator_summary.get("cohort_counts") or {}).items()) or "_none_")
    )
    lines.append(
        "- Translator frontier mix: "
        + (", ".join(f"`{k}` x{v}" for k, v in (translator_summary.get("frontier_signature_counts") or {}).items()) or "_none_")
    )
    for row in (translator.get("priority_examples") or [])[:5]:
        lines.append(
            f"  - `{row.get('date', '')}` `{row.get('state', '')}` `{row.get('period', '')}` winner=`{row.get('winner', '')}` "
            f"cohort=`{row.get('primary_cohort', '')}` frontier=`{row.get('frontier_signature_type', '')}`"
        )
    for bullet in translator.get("interpretation") or []:
        lines.append(f"  - {bullet}")
    lines.append("")
    lines.append("## 9. Winner HTML Frontier")
    lines.append("")
    lines.append(f"- Frontier cases reviewed: `{frontier.get('case_count', 0)}`")
    lines.append(
        "- Frontier signature mix: "
        + (
            ", ".join(
                f"`{key}` x{value}"
                for key, value in (frontier.get("signature_counts") or {}).items()
            )
            or "_none_"
        )
    )
    lines.append(
        "- Frontier hit-class mix: "
        + (
            ", ".join(
                f"`{key}` x{value}"
                for key, value in (frontier.get("hit_class_counts") or {}).items()
            )
            or "_none_"
        )
    )
    score_averages = frontier.get("score_averages") or {}
    if score_averages:
        lines.append(
            "- Average frontier scores: "
            + ", ".join(
                f"`{key}`={float(value):.3f}"
                for key, value in sorted(score_averages.items())
                if isinstance(value, (int, float))
            )
        )
    promotion_queue = frontier.get("promotion_queue") or []
    lines.append(f"- Frontier promotion ideas sampled: `{len(promotion_queue)}`")
    for item in promotion_queue[:4]:
        if not isinstance(item, dict):
            continue
        lines.append(
            f"  - `{item.get('action', '-')}` `{item.get('theme', '-')}`: {item.get('reason', '').strip() or '-'}"
        )
    notable_cases = frontier.get("notable_cases") or {}
    for label in ("strongest", "most_hidden", "strongest_feeder_progression"):
        case = notable_cases.get(label) or {}
        if not isinstance(case, dict) or not case.get("state"):
            continue
        lines.append(
            f"- Notable `{label}` case: `{case.get('date', '')}` `{case.get('state', '')}` `{case.get('winner', '')}` "
            f"signature=`{case.get('frontier_signature_type', '')}` strength=`{case.get('signature_strength', '')}`"
        )
    if frontier.get("warnings"):
        lines.append(
            "- Frontier warnings: "
            + ", ".join(f"`{value}`" for value in frontier.get("warnings") or [])
        )
    lines.append("")
    lines.append("## 10. Best Findings / Worst Misses")
    lines.append("")
    lines.append(f"- Control-arm realized rows sampled: `{len(findings['control_arm_realized_rows'])}`")
    lines.append(f"- Opportunity-gap rows sampled: `{len(findings['opportunity_gap_rows'])}`")
    lines.append(f"- Direct miss rows sampled: `{len(findings['direct_miss_rows'])}`")
    lines.append("")
    lines.append("## 11. Promotion Ledger")
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
    frontier_json = _window_root_from_arg(args.frontier_json) if args.frontier_json else defaults["frontier_json"]
    pure_arena_json = _window_root_from_arg(args.pure_arena_scorecard_json) if args.pure_arena_scorecard_json else defaults["pure_arena_json"]
    translator_json = _window_root_from_arg(args.translator_ledger_json) if args.translator_ledger_json else defaults["translator_json"]
    decay_json = _window_root_from_arg(args.decay_json) if args.decay_json else defaults["decay_json"]
    out_md = _window_root_from_arg(args.out_md) if args.out_md else defaults["md"]
    out_json = _window_root_from_arg(args.out_json) if args.out_json else defaults["json"]

    perf_payload = read_json(perf_json)
    if not isinstance(perf_payload, dict):
        raise SystemExit(f"Performance gap JSON is not an object: {perf_json}")
    frontier_payload: Dict[str, Any] = {}
    if frontier_json.exists():
        raw_frontier = read_json(frontier_json)
        if isinstance(raw_frontier, dict):
            frontier_payload = raw_frontier
    pure_arena_payload: Dict[str, Any] = {}
    if pure_arena_json.exists():
        raw_pure_arena = read_json(pure_arena_json)
        if isinstance(raw_pure_arena, dict):
            pure_arena_payload = raw_pure_arena
    translator_payload: Dict[str, Any] = {}
    if translator_json.exists():
        raw_translator = read_json(translator_json)
        if isinstance(raw_translator, dict):
            translator_payload = raw_translator
    decay_payload: Dict[str, Any] = {}
    if decay_json.exists():
        raw_decay = read_json(decay_json)
        if isinstance(raw_decay, dict):
            decay_payload = raw_decay
    ledger_path = perf_payload.get("ledger_path")
    ledger_rows: List[Dict[str, Any]] = []
    if ledger_path:
        ledger_file = _window_root_from_arg(str(ledger_path))
        import csv

        if ledger_file.exists():
            with ledger_file.open("r", encoding="utf-8", errors="replace", newline="") as fh:
                ledger_rows = [{k: (v or "") for k, v in row.items()} for row in csv.DictReader(fh)]
    perf_payload["ledger_rows"] = ledger_rows

    narrative = _narrative_payload(
        window_root,
        perf_payload,
        frontier_payload=frontier_payload,
        pure_arena_payload=pure_arena_payload,
        translator_payload=translator_payload,
        decay_payload=decay_payload,
    )
    narrative["schema_version"] = "analysis_arena_window_deep_analysis/v1"
    narrative["performance_gap_json"] = safe_rel(perf_json)
    if frontier_payload:
        narrative["frontier_json"] = safe_rel(frontier_json)
    if pure_arena_payload:
        narrative["pure_arena_scorecard_json"] = safe_rel(pure_arena_json)
    if translator_payload:
        narrative["translator_ledger_json"] = safe_rel(translator_json)
    if decay_payload:
        narrative["decay_scorecard_json"] = safe_rel(decay_json)

    _write_json(out_json, narrative, force=args.force)
    _write_text(out_md, _render_markdown(narrative, perf_json_path=perf_json), force=args.force)
    print(f"Wrote: {safe_rel(out_md)}")
    print(f"Wrote: {safe_rel(out_json)}")


if __name__ == "__main__":
    main()
