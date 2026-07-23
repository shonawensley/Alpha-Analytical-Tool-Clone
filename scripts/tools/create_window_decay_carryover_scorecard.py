#!/usr/bin/env python3
"""Create a decay/carryover scorecard for a completed Analysis Arena window.

This keeps same-day window metrics clean while separately measuring whether the
same state-day snapshot resolved within a bounded future horizon.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.tools.analysis_arena_window_utils import (
    WinnerEvent,
    analysis_dir,
    iter_window_dates,
    load_scoreboard,
    load_state_seed_from_manifest_entry,
    load_translation_manifest,
    safe_rel,
    validation_dir,
    winner_events_for_state,
    winners_for_date,
)
from scripts.tools.brain2_rank_contract import (
    RANK_INTEGRITY_INVALID_STATIC_ORDER,
    analytical_rank,
    analytical_score,
    display_order_contract_from_row,
    rank_contract_from_row,
    rank_evaluation_status,
)


DEFAULT_RESULTS_ROOT = REPO_ROOT / "data" / "results"
PROFILE_ORDER = [
    "direct_same_outcome",
    "same_day_precursor_plus_same_day",
    "same_day_carryforward",
    "future_day_decay",
    "miss",
    "right_censored",
]


@dataclass(frozen=True)
class OutcomeEvent:
    date: str
    period: str
    literal: str
    canonical: str
    vtrac_index: Optional[int]
    day_offset: int
    draw_offset: int


@dataclass(frozen=True)
class MetricSpec:
    name: str
    label: str
    target_kind: str
    active_field: str
    values_field: str


METRIC_SPECS: List[MetricSpec] = [
    MetricSpec("board_top_box_core", "Board top box core", "canonical", "board_top_box_active", "board_top_box_values"),
    MetricSpec("board_top_vt_core", "Board top VTRAC core", "index", "board_top_vt_active", "board_top_vt_values"),
    MetricSpec("brain1_box_core", "Brain 1 box core", "canonical", "brain1_box_active", "brain1_box_values"),
    MetricSpec("brain1_vt_core", "Brain 1 VTRAC core", "index", "brain1_vt_active", "brain1_vt_values"),
    MetricSpec("sandbox_box_seed", "Sandbox box seed", "canonical", "sandbox_box_active", "sandbox_box_values"),
    MetricSpec("sandbox_exact_seed", "Sandbox exact seed", "literal", "sandbox_exact_active", "sandbox_exact_values"),
    MetricSpec("sandbox_vt_seed", "Sandbox VTRAC seed", "index", "sandbox_vt_active", "sandbox_vt_values"),
    MetricSpec("preserved_not_budgeted", "Preserved not budgeted", "canonical", "preserved_active", "preserved_values"),
    MetricSpec("arena_box_total", "Arena box total", "canonical", "arena_box_total_active", "arena_box_total_values"),
    MetricSpec("arena_vt_total", "Arena VTRAC total", "index", "arena_vt_total_active", "arena_vt_total_values"),
]


def _parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--window-root", required=True, help="RUNS_2 window root (WINDOW_<...>/)")
    ap.add_argument(
        "--results-root",
        default=str(DEFAULT_RESULTS_ROOT),
        help="Results truth root used for future tail evaluation (default: data/results).",
    )
    ap.add_argument(
        "--decay-upload-days-total",
        type=int,
        default=5,
        help="Total upload-day horizon including same-day. Default: 5.",
    )
    ap.add_argument("--out-md", default="", help="Optional markdown output path.")
    ap.add_argument("--out-json", default="", help="Optional JSON output path.")
    ap.add_argument("--out-csv", default="", help="Optional CSV output path.")
    ap.add_argument("--force", action="store_true", help="Overwrite existing outputs.")
    return ap.parse_args()


def _resolve_path(value: str) -> Path:
    path = Path(value).expanduser()
    if not path.is_absolute():
        path = (REPO_ROOT / path).resolve()
    return path


def _default_paths(window_root: Path) -> Dict[str, Path]:
    stem = window_root.name
    return {
        "md": window_root / f"{stem}__ANALYSIS_ARENA__DECAY_CARRYOVER_SCORECARD.md",
        "json": window_root / f"{stem}__ANALYSIS_ARENA__DECAY_CARRYOVER_SCORECARD.json",
        "csv": window_root / f"{stem}__ANALYSIS_ARENA__DECAY_CARRYOVER_ROWS.csv",
    }


def _write_text(path: Path, text: str, *, force: bool) -> None:
    if path.exists() and not force:
        raise SystemExit(f"Refusing to overwrite existing file without --force: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _write_json(path: Path, payload: Any, *, force: bool) -> None:
    _write_text(path, json.dumps(payload, indent=2, sort_keys=True) + "\n", force=force)


def _write_csv(path: Path, rows: List[Dict[str, Any]], *, force: bool) -> None:
    if path.exists() and not force:
        raise SystemExit(f"Refusing to overwrite existing file without --force: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames: List[str] = []
    for row in rows:
        for key in row.keys():
            if key not in fieldnames:
                fieldnames.append(key)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def _join(values: Iterable[str]) -> str:
    return "|".join(str(value).strip() for value in values if str(value).strip())


def _future_dates_total(snapshot_date: str, total_upload_days: int) -> List[str]:
    base = datetime.strptime(snapshot_date, "%Y-%m-%d").date()
    return [(base + timedelta(days=offset)).isoformat() for offset in range(max(0, int(total_upload_days)))]


def _hint_present(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, (list, tuple, set, dict)):
        return bool(value)
    text = str(value or "").strip()
    if not text:
        return False
    return text.lower() not in {"-", "_none_", "none", "n/a", "na"}


def _seed_signal_lists(seed: Dict[str, Any]) -> Dict[str, List[str]]:
    brain1 = seed.get("brain1_core") or {}
    sandbox = seed.get("sandbox_hypotheses") or {}
    control_arm = seed.get("control_arm") or {}
    brain1_box = []
    for group in ("dominant_canonicals", "context_reinforced_canonicals"):
        brain1_box.extend(str(value).strip() for value in (brain1.get(group) or []) if str(value).strip())
    return {
        "brain1_box": _ordered_unique(brain1_box),
        "brain1_vt": _ordered_unique(str(value).strip() for value in (brain1.get("dominant_vtrac_indices") or []) if str(value).strip()),
        "sandbox_box": _ordered_unique(
            str(item.get("value")).strip()
            for item in (sandbox.get("diagnostic_boxed_seed") or [])
            if isinstance(item, dict) and str(item.get("value")).strip()
        ),
        "sandbox_exact": _ordered_unique(
            str(item.get("value")).strip()
            for item in (sandbox.get("diagnostic_straight_seed") or [])
            if isinstance(item, dict) and str(item.get("value")).strip()
        ),
        "sandbox_vt": _ordered_unique(
            str(item.get("value")).strip()
            for item in (sandbox.get("diagnostic_vt_box_seed") or [])
            if isinstance(item, dict) and str(item.get("value")).strip()
        ),
        "preserved": _ordered_unique(str(value).strip() for value in (control_arm.get("preserved_not_budgeted_canonicals_top") or []) if str(value).strip()),
    }


def _ordered_unique(values: Iterable[str]) -> List[str]:
    out: List[str] = []
    seen = set()
    for value in values:
        text = str(value or "").strip()
        if not text or text in seen:
            continue
        seen.add(text)
        out.append(text)
    return out


def _outcome_events_for_state(
    *,
    results_root: Path,
    snapshot_date: str,
    state_key: str,
    total_upload_days: int,
) -> Dict[str, Any]:
    required_dates = _future_dates_total(snapshot_date, total_upload_days)
    observed_dates: List[str] = []
    events: List[OutcomeEvent] = []
    draw_offset = 0
    for day_offset, results_date in enumerate(required_dates):
        results_path = results_root / f"{results_date}.txt"
        if not results_path.exists():
            break
        observed_dates.append(results_date)
        winners = winners_for_date(results_root=results_root, results_date=results_date)
        for event in winner_events_for_state(date=results_date, state_key=state_key, winners_by_state=winners):
            events.append(
                OutcomeEvent(
                    date=event.date,
                    period=event.period,
                    literal=event.literal,
                    canonical=event.canonical,
                    vtrac_index=event.vtrac_index,
                    day_offset=day_offset,
                    draw_offset=draw_offset,
                )
            )
            draw_offset += 1
    return {
        "events": events,
        "observed_dates": observed_dates,
        "required_dates": required_dates,
        "full_horizon_covered": len(observed_dates) == len(required_dates),
        "observed_upload_days": len(observed_dates),
        "observed_draws": len(events),
        "required_last_date": required_dates[-1] if required_dates else snapshot_date,
    }


def _match_first(events: Sequence[OutcomeEvent], *, values: Sequence[str], target_kind: str) -> Optional[OutcomeEvent]:
    wanted = {str(value).strip() for value in values if str(value).strip()}
    if not wanted:
        return None
    for event in events:
        if target_kind == "canonical" and event.canonical in wanted:
            return event
        if target_kind == "literal" and event.literal in wanted:
            return event
        if target_kind == "index" and event.vtrac_index is not None and str(event.vtrac_index) in wanted:
            return event
    return None


def _resolution_profile(event: Optional[OutcomeEvent], *, full_horizon_covered: bool) -> str:
    if event is None:
        return "miss" if full_horizon_covered else "right_censored"
    if event.day_offset == 0 and event.period == "Midday":
        return "direct_same_outcome"
    if event.day_offset == 0 and event.period == "Evening":
        return "same_day_carryforward"
    return "future_day_decay"


def _same_day(profile: str) -> bool:
    return profile in {"direct_same_outcome", "same_day_precursor_plus_same_day", "same_day_carryforward"}


def _hit(profile: str) -> bool:
    return profile in {"direct_same_outcome", "same_day_precursor_plus_same_day", "same_day_carryforward", "future_day_decay"}


def _event_text(event: Optional[OutcomeEvent]) -> str:
    if event is None:
        return ""
    return f"{event.date} {event.period} {event.literal}"


def _safe_int(value: Any, default: int = 999) -> int:
    try:
        return int(str(value).strip())
    except Exception:
        return int(default)


def _snapshot_row(
    *,
    snapshot_date: str,
    state_key: str,
    scoreboard_row: Dict[str, Any],
    board_verdict: Dict[str, Any],
    seed: Dict[str, Any],
    outcomes: Dict[str, Any],
) -> Dict[str, Any]:
    rank_contract = rank_contract_from_row(scoreboard_row)
    display_contract = display_order_contract_from_row(scoreboard_row)
    rank_valid = bool(rank_contract.get("rank_signal_valid"))
    seed_lists = _seed_signal_lists(seed)
    board_box_values = _ordered_unique(str(value).strip() for value in (scoreboard_row.get("top_canonicals") or []) if str(value).strip())
    board_vt_values = _ordered_unique(str(value).strip() for value in (scoreboard_row.get("top_vtrac_indices") or []) if str(value).strip())
    arena_box_total_values = _ordered_unique(board_box_values + seed_lists["brain1_box"] + seed_lists["sandbox_box"] + seed_lists["preserved"])
    arena_vt_total_values = _ordered_unique(board_vt_values + seed_lists["brain1_vt"] + seed_lists["sandbox_vt"])
    events: List[OutcomeEvent] = list(outcomes["events"] or [])

    row: Dict[str, Any] = {
        "snapshot_date": snapshot_date,
        "state_key": state_key,
        **display_contract,
        "input_order": scoreboard_row.get("input_order") or scoreboard_row.get("input_rank") or "",
        "legacy_static_rank": scoreboard_row.get("legacy_static_rank") or scoreboard_row.get("score_rank") or "",
        "legacy_priority_score": scoreboard_row.get("legacy_priority_score") or scoreboard_row.get("priority_score") or "",
        "score_rank": analytical_rank(scoreboard_row) or "",
        "priority_score": analytical_score(scoreboard_row) if rank_valid else "",
        "analytical_rank": rank_contract.get("analytical_rank") or "",
        "analytical_score": rank_contract.get("analytical_score") if rank_valid else "",
        "analytical_rank_source": rank_contract.get("analytical_rank_source") or "",
        "rank_signal_valid": rank_valid,
        "rank_integrity_status": rank_contract.get("rank_integrity_status"),
        "rank_exclusion_reason": rank_contract.get("rank_exclusion_reason"),
        "role": scoreboard_row.get("role", ""),
        "targeting_bucket": scoreboard_row.get("targeting_bucket", ""),
        "tracker_posture": scoreboard_row.get("tracker_posture", ""),
        "top_primary_target": (
            board_verdict.get("top_primary_target") == state_key if rank_valid else ""
        ),
        "secondary_target": (
            board_verdict.get("secondary_target") == state_key if rank_valid else ""
        ),
        "best_clean_host": (
            board_verdict.get("best_clean_host") == state_key if rank_valid else ""
        ),
        "highest_context_support_state": board_verdict.get("highest_context_support_state") == state_key,
        "profit_alert_hint_present": _hint_present(scoreboard_row.get("profit_alert_hint")),
        "compound_event_hint_present": _hint_present(scoreboard_row.get("compound_event_hint")),
        "due_double_hint_present": _hint_present(scoreboard_row.get("due_double_hint")),
        "blackapple_hint_present": _hint_present(scoreboard_row.get("blackapple_reco_hint")),
        "r_consensus_hint_present": _hint_present(scoreboard_row.get("r_consensus_hint")),
        "survivor_hint_present": _hint_present(scoreboard_row.get("survivor_hint")),
        "required_last_results_date": outcomes["required_last_date"],
        "observed_upload_days": outcomes["observed_upload_days"],
        "observed_draws": outcomes["observed_draws"],
        "full_horizon_covered": bool(outcomes["full_horizon_covered"]),
        "right_censored": not bool(outcomes["full_horizon_covered"]),
        "board_top_box_values": _join(board_box_values),
        "board_top_vt_values": _join(board_vt_values),
        "brain1_box_values": _join(seed_lists["brain1_box"]),
        "brain1_vt_values": _join(seed_lists["brain1_vt"]),
        "sandbox_box_values": _join(seed_lists["sandbox_box"]),
        "sandbox_exact_values": _join(seed_lists["sandbox_exact"]),
        "sandbox_vt_values": _join(seed_lists["sandbox_vt"]),
        "preserved_values": _join(seed_lists["preserved"]),
        "arena_box_total_values": _join(arena_box_total_values),
        "arena_vt_total_values": _join(arena_vt_total_values),
    }

    values_by_family = {
        "board_top_box_values": board_box_values,
        "board_top_vt_values": board_vt_values,
        "brain1_box_values": seed_lists["brain1_box"],
        "brain1_vt_values": seed_lists["brain1_vt"],
        "sandbox_box_values": seed_lists["sandbox_box"],
        "sandbox_exact_values": seed_lists["sandbox_exact"],
        "sandbox_vt_values": seed_lists["sandbox_vt"],
        "preserved_values": seed_lists["preserved"],
        "arena_box_total_values": arena_box_total_values,
        "arena_vt_total_values": arena_vt_total_values,
    }

    matches: Dict[str, Optional[OutcomeEvent]] = {}
    for spec in METRIC_SPECS:
        values = values_by_family[spec.values_field]
        row[spec.active_field] = bool(values)
        match = _match_first(events, values=values, target_kind=spec.target_kind)
        matches[spec.name] = match
        profile = _resolution_profile(match, full_horizon_covered=bool(outcomes["full_horizon_covered"])) if values else ""
        row[f"{spec.name}_profile"] = profile
        row[f"{spec.name}_same_day"] = _same_day(profile) if profile else False
        row[f"{spec.name}_hit"] = _hit(profile) if profile else False
        row[f"{spec.name}_day_offset"] = match.day_offset if match is not None else ""
        row[f"{spec.name}_draw_offset"] = match.draw_offset if match is not None else ""
        row[f"{spec.name}_event"] = _event_text(match)

    overall_event = None
    overall_profile = ""
    active_profiles = [row[f"{spec.name}_profile"] for spec in METRIC_SPECS if row.get(spec.active_field)]
    ranked_events = [event for event in matches.values() if event is not None]
    if ranked_events:
        overall_event = sorted(ranked_events, key=lambda item: (item.day_offset, item.draw_offset, item.date, item.period))[0]
        overall_profile = _resolution_profile(overall_event, full_horizon_covered=bool(outcomes["full_horizon_covered"]))
    elif any(row.get(spec.active_field) for spec in METRIC_SPECS):
        overall_profile = "miss" if bool(outcomes["full_horizon_covered"]) else "right_censored"

    row["arena_any_signal_active"] = any(row.get(spec.active_field) for spec in METRIC_SPECS)
    row["arena_any_signal_profile"] = overall_profile
    row["arena_any_signal_same_day"] = _same_day(overall_profile) if overall_profile else False
    row["arena_any_signal_hit"] = _hit(overall_profile) if overall_profile else False
    row["arena_any_signal_day_offset"] = overall_event.day_offset if overall_event is not None else ""
    row["arena_any_signal_draw_offset"] = overall_event.draw_offset if overall_event is not None else ""
    row["arena_any_signal_event"] = _event_text(overall_event)
    row["active_metric_count"] = sum(1 for spec in METRIC_SPECS if row.get(spec.active_field))
    row["active_metric_names"] = _join(spec.name for spec in METRIC_SPECS if row.get(spec.active_field))
    row["active_profiles"] = _join(profile for profile in active_profiles if profile)
    row["tracker_hint_any"] = any(
        bool(row.get(field))
        for field in (
            "profit_alert_hint_present",
            "compound_event_hint_present",
            "due_double_hint_present",
            "blackapple_hint_present",
            "r_consensus_hint_present",
            "survivor_hint_present",
        )
    )
    return row


def _top_examples(rows: Iterable[Dict[str, Any]], *, profile: str, limit: int = 8) -> List[Dict[str, Any]]:
    matched = [row for row in rows if row.get("arena_any_signal_profile") == profile]
    matched.sort(
        key=lambda row: (
            str(row.get("snapshot_date") or ""),
            str(row.get("state_key") or ""),
        )
    )
    out: List[Dict[str, Any]] = []
    for row in matched[:limit]:
        out.append(
            {
                "snapshot_date": row.get("snapshot_date", ""),
                "state": row.get("state_key", ""),
                "display_order": row.get("display_order", ""),
                "display_order_source": row.get("display_order_source", ""),
                "analytical_rank": row.get("analytical_rank", ""),
                "legacy_static_rank": row.get("legacy_static_rank", ""),
                "targeting_bucket": row.get("targeting_bucket", ""),
                "tracker_posture": row.get("tracker_posture", ""),
                "arena_any_signal_event": row.get("arena_any_signal_event", ""),
                "active_metric_names": row.get("active_metric_names", "").split("|") if row.get("active_metric_names") else [],
            }
        )
    return out


def _panel_for_metric(rows: Sequence[Dict[str, Any]], *, spec: MetricSpec) -> Dict[str, Any]:
    scoped = [row for row in rows if bool(row.get(spec.active_field))]
    profiles = Counter(str(row.get(f"{spec.name}_profile") or "") for row in scoped if str(row.get(f"{spec.name}_profile") or "").strip())
    same_day = sum(1 for row in scoped if bool(row.get(f"{spec.name}_same_day")))
    horizon = sum(1 for row in scoped if bool(row.get(f"{spec.name}_hit")))
    return {
        "metric_family": spec.name,
        "label": spec.label,
        "active_state_days": len(scoped),
        "same_day_resolved": same_day,
        "same_day_rate": (same_day / len(scoped)) if scoped else 0.0,
        "horizon_resolved": horizon,
        "horizon_rate": (horizon / len(scoped)) if scoped else 0.0,
        "incremental_decay_lift": horizon - same_day,
        "profile_counts": {name: profiles.get(name, 0) for name in PROFILE_ORDER},
    }


def _panel_for_cohort(rows: Sequence[Dict[str, Any]], *, name: str, label: str, selector) -> Dict[str, Any]:
    scoped = [row for row in rows if selector(row)]
    profiles = Counter(str(row.get("arena_any_signal_profile") or "") for row in scoped if str(row.get("arena_any_signal_profile") or "").strip())
    same_day = sum(1 for row in scoped if bool(row.get("arena_any_signal_same_day")))
    horizon = sum(1 for row in scoped if bool(row.get("arena_any_signal_hit")))
    return {
        "cohort": name,
        "label": label,
        "state_days": len(scoped),
        "same_day_resolved": same_day,
        "same_day_rate": (same_day / len(scoped)) if scoped else 0.0,
        "horizon_resolved": horizon,
        "horizon_rate": (horizon / len(scoped)) if scoped else 0.0,
        "incremental_decay_lift": horizon - same_day,
        "profile_counts": {name_: profiles.get(name_, 0) for name_ in PROFILE_ORDER},
    }


def _not_evaluable_cohort(*, name: str, label: str) -> Dict[str, Any]:
    return {
        "cohort": name,
        "label": label,
        "status": "NOT_EVALUABLE",
        "evaluable": False,
        "reason": RANK_INTEGRITY_INVALID_STATIC_ORDER,
        "state_days": None,
        "same_day_resolved": None,
        "same_day_rate": None,
        "horizon_resolved": None,
        "horizon_rate": None,
        "incremental_decay_lift": None,
        "profile_counts": {name_: None for name_ in PROFILE_ORDER},
    }


def build_payload(window_root: Path, *, results_root: Path, decay_upload_days_total: int) -> Dict[str, Any]:
    if decay_upload_days_total < 1:
        raise SystemExit("--decay-upload-days-total must be >= 1")
    dates = iter_window_dates(window_root)
    rows: List[Dict[str, Any]] = []
    for results_date in dates:
        scoreboard = load_scoreboard(window_root, results_date)
        manifest = load_translation_manifest(window_root, results_date)
        board_verdict = scoreboard.get("board_verdict") or {}
        scoreboard_rows = scoreboard.get("scoreboard_rows") or []
        scoreboard_by_state = {
            str(row.get("state_key") or "").strip(): row
            for row in scoreboard_rows
            if isinstance(row, dict) and str(row.get("state_key") or "").strip()
        }
        state_receipts = manifest.get("state_receipts") or []
        manifest_by_state = {
            str(entry.get("state_key") or "").strip(): entry
            for entry in state_receipts
            if isinstance(entry, dict) and str(entry.get("state_key") or "").strip()
        }
        active_state_keys = sorted(set(scoreboard_by_state) | set(manifest_by_state))
        for state_key in active_state_keys:
            seed = load_state_seed_from_manifest_entry(manifest_by_state.get(state_key, {})) if manifest_by_state.get(state_key) else {}
            scoreboard_row = scoreboard_by_state.get(state_key, {})
            if not seed and not scoreboard_row:
                continue
            outcomes = _outcome_events_for_state(
                results_root=results_root,
                snapshot_date=results_date,
                state_key=state_key,
                total_upload_days=decay_upload_days_total,
            )
            rows.append(
                _snapshot_row(
                    snapshot_date=results_date,
                    state_key=state_key,
                    scoreboard_row=scoreboard_row,
                    board_verdict=board_verdict if isinstance(board_verdict, dict) else {},
                    seed=seed if isinstance(seed, dict) else {},
                    outcomes=outcomes,
                )
            )

    metric_families = [_panel_for_metric(rows, spec=spec) for spec in METRIC_SPECS]
    overall_panel = _panel_for_cohort(rows, name="arena_any_signal", label="Arena any signal", selector=lambda row: bool(row.get("arena_any_signal_active")))
    rank_evaluation = rank_evaluation_status(
        [
            {
                "analytical_rank": row.get("analytical_rank"),
                "analytical_score": row.get("analytical_score"),
                "analytical_rank_source": row.get("analytical_rank_source") or None,
                "rank_signal_available": row.get("rank_signal_valid") is True,
                "rank_signal_valid": row.get("rank_signal_valid") is True,
                "rank_integrity_status": row.get("rank_integrity_status"),
            }
            for row in rows
        ]
    )
    if rank_evaluation["evaluable"]:
        top_primary_panel = _panel_for_cohort(
            rows,
            name="top_primary_target",
            label="Top primary target",
            selector=lambda row: bool(row.get("top_primary_target")),
        )
        top3_panel = _panel_for_cohort(
            rows,
            name="top3_ranked",
            label="Top-3 ranked states",
            selector=lambda row: _safe_int(row.get("analytical_rank"), default=999) <= 3,
        )
    else:
        top_primary_panel = _not_evaluable_cohort(
            name="top_primary_target",
            label="Top primary target",
        )
        top3_panel = _not_evaluable_cohort(
            name="top3_ranked",
            label="Top-3 ranked states",
        )
    cohort_panels = [
        overall_panel,
        top_primary_panel,
        top3_panel,
        _panel_for_cohort(rows, name="tracker_hint_present", label="Any tracker hint present", selector=lambda row: bool(row.get("tracker_hint_any"))),
        _panel_for_cohort(rows, name="profit_alert_hint_present", label="Profit-alert hint present", selector=lambda row: bool(row.get("profit_alert_hint_present"))),
        _panel_for_cohort(rows, name="due_double_hint_present", label="Due-double hint present", selector=lambda row: bool(row.get("due_double_hint_present"))),
    ]
    interpretation: List[str] = [
        "Same-day window grading stays clean; this scorecard separately measures delayed resolution within the configured horizon.",
        "A miss is only a true miss when the full tail is present. Incomplete tail coverage is reported as right_censored.",
        "Upload-day horizon is the primary setting. Draw-based accounting is preserved as a companion lens because same-day Midday/Evening crossover matters.",
    ]
    if overall_panel["incremental_decay_lift"] > 0:
        interpretation.append(
            f"Arena-any-signal state-days gained `{overall_panel['incremental_decay_lift']}` extra resolutions beyond same-day inside the current decay horizon."
        )
    if any(int(panel["profile_counts"].get("same_day_carryforward") or 0) > 0 for panel in cohort_panels):
        interpretation.append("Same-day carryforward remains distinct from future-day decay and should not be flattened into one generic later-hit bucket.")

    return {
        "schema_version": "analysis_arena_decay_carryover_v1",
        "metadata": {
            "window_root": safe_rel(window_root),
            "analysis_dir": safe_rel(analysis_dir(window_root)),
            "validation_dir": safe_rel(validation_dir(window_root)),
            "window_dates": [dates[0], dates[-1]] if dates else [],
            "snapshot_days": len(dates),
            "results_root": safe_rel(results_root),
            "decay_upload_days_total": int(decay_upload_days_total),
            "decay_tail_days_required": max(0, int(decay_upload_days_total) - 1),
            "decay_draws_total_max": int(decay_upload_days_total) * 2,
            "same_day_included": True,
            "resolution_policy": "Upload-day horizon is primary; draw-based offsets are companion accounting only.",
            "results_tail_rule": "A 5 total upload-day horizon requires results through snapshot day + 4 days.",
            "rank_evaluation": rank_evaluation,
        },
        "summary": {
            "state_day_snapshots": len(rows),
            "full_horizon_rows": sum(1 for row in rows if bool(row.get("full_horizon_covered"))),
            "right_censored_rows": sum(1 for row in rows if bool(row.get("right_censored"))),
            "max_observed_draws": max((int(row.get("observed_draws") or 0) for row in rows), default=0),
            "max_observed_upload_days": max((int(row.get("observed_upload_days") or 0) for row in rows), default=0),
        },
        "metric_families": metric_families,
        "cohort_panels": cohort_panels,
        "examples": {
            "future_day_decay": _top_examples(rows, profile="future_day_decay"),
            "same_day_carryforward": _top_examples(rows, profile="same_day_carryforward"),
            "right_censored": _top_examples(rows, profile="right_censored"),
        },
        "interpretation": interpretation,
        "rows": rows,
    }


def _pct(value: float) -> str:
    return f"{100.0 * value:.1f}%"


def _render_markdown(payload: Dict[str, Any], *, csv_path: Path) -> str:
    meta = payload.get("metadata") or {}
    summary = payload.get("summary") or {}
    metric_families = payload.get("metric_families") or []
    cohort_panels = payload.get("cohort_panels") or []
    examples = payload.get("examples") or {}
    lines: List[str] = [
        "# Analysis Arena Decay / Carryover Scorecard",
        "",
        "Purpose:",
        "",
        "- keep same-day window metrics clean",
        "- separately measure whether Arena-era state-day snapshots resolve inside a bounded future horizon",
        "- preserve same-day carryforward and future-day decay as different resolution types",
        "",
        "## 1. Configured Horizon",
        "",
        f"- Window root: `{meta.get('window_root', '')}`",
        f"- Results root: `{meta.get('results_root', '')}`",
        f"- Snapshot dates: `{meta.get('window_dates', [''])[0]}` to `{meta.get('window_dates', [''])[-1]}`" if meta.get("window_dates") else "- Snapshot dates: _none_",
        f"- Snapshot upload days: `{meta.get('snapshot_days', 0)}`",
        f"- Decay horizon: `{meta.get('decay_upload_days_total', 0)}` total upload days (same-day included)",
        f"- Max draw horizon: `{meta.get('decay_draws_total_max', 0)}` total draws",
        f"- Tail days required beyond the last snapshot day: `{meta.get('decay_tail_days_required', 0)}`",
        f"- Results-tail rule: `{meta.get('results_tail_rule', '')}`",
        f"- CSV roster: `{safe_rel(csv_path)}`",
        "",
        "## 2. Coverage",
        "",
        f"- State-day snapshots: `{summary.get('state_day_snapshots', 0)}`",
        f"- Full-horizon rows: `{summary.get('full_horizon_rows', 0)}`",
        f"- Right-censored rows: `{summary.get('right_censored_rows', 0)}`",
        f"- Max observed upload days: `{summary.get('max_observed_upload_days', 0)}`",
        f"- Max observed draws: `{summary.get('max_observed_draws', 0)}`",
        "",
        "## 3. Metric Family Scoreboard",
        "",
        "| Metric | Active | Same-day | Horizon | Incremental decay lift | Direct same | Same-day precursor | Same-day carryforward | Future-day decay | Miss | Right-censored |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for panel in metric_families:
        profiles = panel.get("profile_counts") or {}
        lines.append(
            "| "
            + " | ".join(
                [
                    str(panel.get("label", "")),
                    str(panel.get("active_state_days", 0)),
                    f"{panel.get('same_day_resolved', 0)} ({_pct(panel.get('same_day_rate', 0.0))})",
                    f"{panel.get('horizon_resolved', 0)} ({_pct(panel.get('horizon_rate', 0.0))})",
                    str(panel.get("incremental_decay_lift", 0)),
                    str(profiles.get("direct_same_outcome", 0)),
                    str(profiles.get("same_day_precursor_plus_same_day", 0)),
                    str(profiles.get("same_day_carryforward", 0)),
                    str(profiles.get("future_day_decay", 0)),
                    str(profiles.get("miss", 0)),
                    str(profiles.get("right_censored", 0)),
                ]
            )
            + " |"
        )
    lines += [
        "",
        "## 4. Cohort Panels",
        "",
        "| Cohort | State-days | Same-day | Horizon | Incremental decay lift | Direct same | Same-day carryforward | Future-day decay | Miss | Right-censored |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for panel in cohort_panels:
        if panel.get("evaluable") is False:
            lines.append(
                f"| {panel.get('label', '')} | NOT_EVALUABLE | NOT_EVALUABLE | "
                f"NOT_EVALUABLE | NOT_EVALUABLE | - | - | - | - | - |"
            )
            continue
        profiles = panel.get("profile_counts") or {}
        lines.append(
            "| "
            + " | ".join(
                [
                    str(panel.get("label", "")),
                    str(panel.get("state_days", 0)),
                    f"{panel.get('same_day_resolved', 0)} ({_pct(panel.get('same_day_rate', 0.0))})",
                    f"{panel.get('horizon_resolved', 0)} ({_pct(panel.get('horizon_rate', 0.0))})",
                    str(panel.get("incremental_decay_lift", 0)),
                    str(profiles.get("direct_same_outcome", 0)),
                    str(profiles.get("same_day_carryforward", 0)),
                    str(profiles.get("future_day_decay", 0)),
                    str(profiles.get("miss", 0)),
                    str(profiles.get("right_censored", 0)),
                ]
            )
            + " |"
        )
    lines += ["", "## 5. Notable Examples", ""]
    for label, rows in (
        ("Future-day decay", examples.get("future_day_decay") or []),
        ("Same-day carryforward", examples.get("same_day_carryforward") or []),
        ("Right-censored", examples.get("right_censored") or []),
    ):
        lines.append(f"### {label}")
        lines.append("")
        if not rows:
            lines.append("- _none_")
            lines.append("")
            continue
        for row in rows:
            lines.append(
                f"- `{row.get('snapshot_date', '')}` `{row.get('state', '')}` "
                f"display=`{row.get('display_order', '')}` analytical_rank=`{row.get('analytical_rank', '') or 'unavailable'}` "
                f"legacy_rank=`{row.get('legacy_static_rank', '') or '-'}` "
                f"event=`{row.get('arena_any_signal_event', '') or '-'}` metrics=`{', '.join(row.get('active_metric_names') or []) or '-'}`"
            )
        lines.append("")
    lines += ["## 6. Interpretation", ""]
    for item in payload.get("interpretation") or []:
        lines.append(f"- {item}")
    return "\n".join(lines) + "\n"


def main() -> None:
    args = _parse_args()
    window_root = _resolve_path(args.window_root)
    results_root = _resolve_path(args.results_root)
    out_paths = _default_paths(window_root)
    md_path = _resolve_path(args.out_md) if args.out_md else out_paths["md"]
    json_path = _resolve_path(args.out_json) if args.out_json else out_paths["json"]
    csv_path = _resolve_path(args.out_csv) if args.out_csv else out_paths["csv"]

    payload = build_payload(
        window_root=window_root,
        results_root=results_root,
        decay_upload_days_total=int(args.decay_upload_days_total),
    )
    _write_csv(csv_path, list(payload.get("rows") or []), force=bool(args.force))
    _write_json(json_path, payload, force=bool(args.force))
    _write_text(md_path, _render_markdown(payload, csv_path=csv_path), force=bool(args.force))


if __name__ == "__main__":
    main()
