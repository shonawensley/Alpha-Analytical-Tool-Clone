#!/usr/bin/env python3
"""Run a frozen, winner-joined Positional Tracker harness for AUX CORE.

Generation is performed from pre-result Aux draw snapshots. Winner ledgers are
loaded separately and joined only after each Positional report exists. The tool
is diagnostic: it writes review artifacts and never changes runtime scoring.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
from collections import defaultdict
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Any, Dict, Iterable, Mapping, Optional, Sequence


ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from modules.module_d_auxiliary_tools.refactored.positional_tool import WeightsConfig  # type: ignore
from scripts.tools.positional_aux_core import (  # type: ignore
    WIDTHS,
    build_lossless_report,
    grade_winner,
    load_frozen_draws,
    render_report_markdown,
    safe_rel,
    sha256_file,
    write_json,
)


DEFAULT_OUTPUT = (
    ROOT
    / "docs"
    / "AAT9_KIT"
    / "FINAL VALIDATION"
    / "RUNS_2"
    / "POSITIONAL_AUX_CORE_HARNESS_V1"
)
GENERATED_FILENAMES: frozenset[str] = frozenset(
    {
        "EXAMPLE__2026-03-09__Connecticut4__Evening__091.json",
        "EXAMPLE__2026-03-09__Connecticut4__Evening__091.md",
        "MANIFEST.json",
        "POSITIONAL_ABLATION_LEDGER.csv",
        "POSITIONAL_DECAY_LEDGER.csv",
        "POSITIONAL_DECAY_ROLLUP.csv",
        "POSITIONAL_FEATURE_LEDGER.csv",
        "POSITIONAL_ROLLUP.csv",
        "SKIPPED_OR_ERROR_ROWS.csv",
        "START_HERE.md",
    }
)


@dataclass(frozen=True)
class CohortSpec:
    name: str
    role: str
    day_root: Path
    winner_ledger: Path


@dataclass(frozen=True)
class ProfileSpec:
    name: str
    scope: str
    weights: Optional[WeightsConfig] = None
    shortlist_cfg: Optional[Mapping[str, Any]] = None


DEFAULT_COHORTS: tuple[CohortSpec, ...] = (
    CohortSpec(
        name="june_2025",
        role="discovery",
        day_root=ROOT / "sharepacks" / "_predictive_replay" / "archived_window_replay_v3_june2025",
        winner_ledger=(
            ROOT
            / "docs"
            / "AAT9_KIT"
            / "FINAL VALIDATION"
            / "RUNS_2"
            / "REPLAY"
            / "archived_window_replay_v3_june2025"
            / "WINDOW_2025-06-21_to_2025-06-27"
            / "WINDOW_2025-06-21_to_2025-06-27__ANALYSIS_ARENA__WINNER_SIGNAL_ATTRIBUTION_LEDGER.csv"
        ),
    ),
    CohortSpec(
        name="early_january_2026",
        role="calibration",
        day_root=ROOT / "sharepacks" / "_predictive_replay" / "archived_window_replay_v2",
        winner_ledger=(
            ROOT
            / "docs"
            / "AAT9_KIT"
            / "FINAL VALIDATION"
            / "RUNS_2"
            / "REPLAY"
            / "archived_window_replay_v2"
            / "WINDOW_2025-12-30_to_2026-01-09"
            / "WINDOW_2025-12-30_to_2026-01-09__ANALYSIS_ARENA__WINNER_SIGNAL_ATTRIBUTION_LEDGER.csv"
        ),
    ),
    CohortSpec(
        name="late_january_2026",
        role="calibration",
        day_root=(
            ROOT
            / "sharepacks"
            / "_predictive_replay"
            / "archived_window_replay_v2_jan19_recovered"
        ),
        winner_ledger=(
            ROOT
            / "docs"
            / "AAT9_KIT"
            / "FINAL VALIDATION"
            / "RUNS_2"
            / "REPLAY"
            / "archived_window_replay_v2_jan19_recovered"
            / "WINDOW_2026-01-15_to_2026-01-22"
            / "WINDOW_2026-01-15_to_2026-01-22__ANALYSIS_ARENA__WINNER_SIGNAL_ATTRIBUTION_LEDGER.csv"
        ),
    ),
    CohortSpec(
        name="march_2026",
        role="holdout",
        day_root=ROOT / "sharepacks" / "_predictive_replay" / "march_2026_15day_replay_v2",
        winner_ledger=(
            ROOT
            / "docs"
            / "AAT9_KIT"
            / "FINAL VALIDATION"
            / "RUNS_2"
            / "REPLAY"
            / "march_2026_15day_replay_v2"
            / "WINDOW_2026-03-09_to_2026-03-23"
            / "WINDOW_2026-03-09_to_2026-03-23__ANALYSIS_ARENA__WINNER_SIGNAL_ATTRIBUTION_LEDGER.csv"
        ),
    ),
)


def _profiles() -> tuple[ProfileSpec, ...]:
    base = WeightsConfig()
    return (
        ProfileSpec("native_all_variant", "static"),
        ProfileSpec(
            "no_mirror",
            "static",
            weights=replace(
                base,
                mirror_same_variant=0.0,
                consensus_mirror=0.0,
            ),
            shortlist_cfg={"weights": {"mirror_echo": 0.0}},
        ),
        ProfileSpec(
            "no_cross_variant",
            "static",
            weights=replace(
                base,
                consensus_exact=0.0,
                consensus_mirror=0.0,
            ),
            shortlist_cfg={"weights": {"xvar": 0.0}},
        ),
        ProfileSpec(
            "no_double_pressure",
            "static",
            weights=replace(
                base,
                double_pressure=0.0,
                double_due_bonus=0.0,
            ),
            shortlist_cfg={"weights": {"double_pressure": 0.0}},
        ),
        ProfileSpec(
            "no_swap",
            "static",
            weights=replace(
                base,
                swap_echo=0.0,
                swap_echo_mirror=0.0,
            ),
        ),
        ProfileSpec(
            "no_repeat_endcap",
            "static",
            shortlist_cfg={"features": {"enable_repeat_endcap": False}},
        ),
        ProfileSpec(
            "no_lane_concordance",
            "static",
            shortlist_cfg={"features": {"enable_lane_concordance": False}},
        ),
        ProfileSpec("target_variant_only", "target_variant"),
        ProfileSpec("target_vtrac_context", "target_vtrac"),
        ProfileSpec("target_due_double_context", "target_due_double"),
        ProfileSpec(
            "forced_due_double_sensitivity",
            "forced_due_double",
        ),
    )


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        default=str(DEFAULT_OUTPUT),
        help="Destination for generated harness artifacts.",
    )
    parser.add_argument(
        "--cohort",
        action="append",
        default=[],
        metavar="NAME:ROLE:DAY_ROOT:WINNER_LEDGER",
        help="Override default cohorts; repeat for multiple windows.",
    )
    parser.add_argument(
        "--profile",
        action="append",
        default=[],
        help="Run only named profiles; repeat as needed.",
    )
    parser.add_argument(
        "--event-limit",
        type=int,
        default=0,
        help="Optional deterministic event limit for smoke tests.",
    )
    parser.add_argument("--force", action="store_true", help="Replace output directory contents.")
    return parser.parse_args()


def _resolve(value: str) -> Path:
    path = Path(value).expanduser()
    return path.resolve() if path.is_absolute() else (ROOT / path).resolve()


def _parse_cohort(value: str) -> CohortSpec:
    parts = value.split(":", 3)
    if len(parts) != 4:
        raise ValueError(
            "Cohort must be NAME:ROLE:DAY_ROOT:WINNER_LEDGER, "
            f"received {value!r}"
        )
    name, role, day_root, winner_ledger = parts
    return CohortSpec(
        name=name.strip(),
        role=role.strip(),
        day_root=_resolve(day_root),
        winner_ledger=_resolve(winner_ledger),
    )


def _read_csv(path: Path) -> list[Dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", errors="replace", newline="") as fh:
        return [
            {str(key): str(value or "") for key, value in row.items()}
            for row in csv.DictReader(fh)
        ]


def _truthy(value: Any) -> bool:
    return str(value or "").strip().lower() in {"1", "true", "yes", "y"}


def _load_events(spec: CohortSpec) -> list[Dict[str, str]]:
    if not spec.winner_ledger.exists():
        raise FileNotFoundError(spec.winner_ledger)
    events: Dict[str, Dict[str, str]] = {}
    for row in _read_csv(spec.winner_ledger):
        event_id = row.get("event_id", "").strip()
        if not event_id:
            continue
        event = {
            "event_id": event_id,
            "date": row.get("date", "").strip(),
            "state_key": row.get("state_key", "").strip(),
            "period": row.get("period", "").strip().title(),
            "winner": row.get("winner", "").strip().zfill(3),
        }
        existing = events.get(event_id)
        if existing:
            identity = {
                key: existing[key]
                for key in ("event_id", "date", "state_key", "period", "winner")
            }
            if identity != event:
                raise ValueError(f"Conflicting winner identity for {event_id}")
        else:
            existing = {
                **event,
                "winner_ledger_row_count": "0",
                "winner_ledger_pre_draw_row_count": "0",
                "winner_ledger_post_result_row_count": "0",
            }
            events[event_id] = existing
        existing["winner_ledger_row_count"] = str(
            int(existing["winner_ledger_row_count"]) + 1
        )
        availability_key = (
            "winner_ledger_pre_draw_row_count"
            if _truthy(row.get("pre_draw_available"))
            else "winner_ledger_post_result_row_count"
        )
        existing[availability_key] = str(int(existing[availability_key]) + 1)
    return sorted(
        events.values(),
        key=lambda row: (
            row["date"],
            row["state_key"],
            0 if row["period"] == "Midday" else 1,
            row["winner"],
        ),
    )


def _load_meta(day_dir: Path) -> Dict[str, Any]:
    path = day_dir / "control_center" / "meta.json"
    if not path.exists():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def _state_draws_dir(day_dir: Path, state_key: str) -> Path:
    return day_dir / state_key / "aux" / "draws"


def _state_summary_path(day_dir: Path, state_key: str) -> Path:
    return day_dir / state_key / "aux" / state_key / "summary.json"


def _target_vtrac_indices(summary_path: Path, period: str) -> list[int]:
    if not summary_path.exists():
        return []
    payload = json.loads(summary_path.read_text(encoding="utf-8"))
    overlay_top = (
        ((payload.get("vtrac") or {}).get("overlay_top") or {})
        .get(period.lower(), [])
    )
    values = []
    for row in overlay_top if isinstance(overlay_top, list) else []:
        if not isinstance(row, dict):
            continue
        try:
            values.append(int(row.get("index")))
        except (TypeError, ValueError):
            continue
    return values


def _draws_since_last_double(draws: Sequence[str]) -> int:
    for index, draw in enumerate(draws):
        counts = defaultdict(int)
        for char in str(draw):
            counts[char] += 1
        if any(count >= 2 for count in counts.values()):
            return index
    return len(draws)


def _build_profile_report(
    *,
    spec: ProfileSpec,
    state_key: str,
    results_date: str,
    period: str,
    draws_dir: Path,
    summary_path: Path,
) -> Dict[str, Any]:
    kwargs: Dict[str, Any] = {
        "state_key": state_key,
        "results_date": results_date,
        "draws_dir": draws_dir,
        "profile": spec.name,
        "weights": spec.weights,
        "shortlist_cfg": spec.shortlist_cfg,
    }
    if spec.scope == "target_variant":
        kwargs["target_variant"] = period.lower()
    elif spec.scope == "target_vtrac":
        kwargs["vtrac_hot_indices"] = _target_vtrac_indices(
            summary_path,
            period,
        )
    elif spec.scope == "target_due_double":
        draws_by_variant, _ = load_frozen_draws(state_key, draws_dir)
        target_draws = draws_by_variant.get(period.lower(), [])
        draws_since = _draws_since_last_double(target_draws)
        kwargs["due_doubles_active"] = draws_since >= 71
    elif spec.scope == "forced_due_double":
        kwargs["due_doubles_active"] = True
    return build_lossless_report(**kwargs)


def _flatten_grade(
    *,
    cohort: CohortSpec,
    event: Mapping[str, str],
    profile: str,
    payload: Mapping[str, Any],
    grade: Mapping[str, Any],
    include_receipts: bool,
) -> Dict[str, Any]:
    row: Dict[str, Any] = {
        "cohort": cohort.name,
        "cohort_role": cohort.role,
        "profile": profile,
        "event_id": event["event_id"],
        "date": event["date"],
        "state_key": event["state_key"],
        "period": event["period"],
        "winner": grade["winner"],
        "winner_canonical": grade["winner_canonical"],
        "winner_vtrac_index": grade["winner_vtrac_index"],
        "winner_kind": grade["winner_kind"],
        "winner_ledger_row_count": event.get("winner_ledger_row_count", ""),
        "winner_ledger_pre_draw_row_count": event.get(
            "winner_ledger_pre_draw_row_count",
            "",
        ),
        "winner_ledger_post_result_row_count": event.get(
            "winner_ledger_post_result_row_count",
            "",
        ),
        "analysis_scope": ((payload.get("metadata") or {}).get("analysis_scope")),
        "target_variant": ((payload.get("metadata") or {}).get("target_variant")),
        "context_due_doubles_active": (
            (payload.get("context_receipt") or {}).get("due_doubles_active")
        ),
        "context_vtrac_hot_index_count": len(
            (payload.get("context_receipt") or {}).get("vtrac_hot_indices") or []
        ),
        "source_is_frozen_pre_result": (
            payload.get("metadata") or {}
        ).get("source_is_frozen_pre_result"),
        "winner_join_phase": grade["winner_join_phase"],
        "target_variant_exact_position_count": grade[
            "target_variant_exact_position_count"
        ],
        "all_variant_same_position_exact_count": grade[
            "all_variant_same_position_exact_count"
        ],
        "all_variant_same_position_mirror_count": grade[
            "all_variant_same_position_mirror_count"
        ],
        "loose_cross_position_exact_count": grade[
            "loose_cross_position_exact_count"
        ],
        "loose_cross_position_mirror_count": grade[
            "loose_cross_position_mirror_count"
        ],
        "front_pair_same_variant": bool(
            grade["pair_receipts"]["front"]["same_variant_exact_support"]
        ),
        "back_pair_same_variant": bool(
            grade["pair_receipts"]["back"]["same_variant_exact_support"]
        ),
        "endcap_pair_same_variant": bool(
            grade["pair_receipts"]["endcap"]["same_variant_exact_support"]
        ),
        "front_pair_cross_variant": grade["pair_receipts"]["front"][
            "cross_variant_position_support"
        ],
        "back_pair_cross_variant": grade["pair_receipts"]["back"][
            "cross_variant_position_support"
        ],
        "endcap_pair_cross_variant": grade["pair_receipts"]["endcap"][
            "cross_variant_position_support"
        ],
        "double_anchor_top2": grade["double_anchor_top2"],
        "candidate_count": grade["candidate_count"],
        "shortlist_exact_rank": grade["shortlist_exact_rank"] or "",
        "shortlist_canonical_rank": grade["shortlist_canonical_rank"] or "",
        "shortlist_vtrac_rank": grade["shortlist_vtrac_rank"] or "",
        "role_labels": "|".join(grade["role_labels"]),
    }
    for width in WIDTHS:
        receipt = grade["width_receipts"][str(width)]
        row[f"exact_at_{width}"] = receipt["exact"]
        row[f"canonical_at_{width}"] = receipt["canonical_box"]
        row[f"vtrac_at_{width}"] = receipt["vtrac_box"]
    if include_receipts:
        row["position_receipts_json"] = json.dumps(
            grade["position_receipts"],
            sort_keys=True,
            separators=(",", ":"),
        )
        row["pair_receipts_json"] = json.dumps(
            grade["pair_receipts"],
            sort_keys=True,
            separators=(",", ":"),
        )
        row["double_anchor_occurrences_json"] = json.dumps(
            grade["double_anchor_occurrences"],
            sort_keys=True,
            separators=(",", ":"),
        )
    return row


def _write_csv(path: Path, rows: Sequence[Mapping[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields: list[str] = []
    for row in rows:
        for key in row:
            if key not in fields:
                fields.append(key)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def _as_bool(value: Any) -> bool:
    return value is True or str(value).strip().lower() == "true"


def _average(rows: Sequence[Mapping[str, Any]], field: str) -> float:
    values = []
    for row in rows:
        try:
            values.append(float(row.get(field) or 0.0))
        except (TypeError, ValueError):
            continue
    return sum(values) / len(values) if values else 0.0


def _rate(rows: Sequence[Mapping[str, Any]], field: str) -> float:
    return (
        sum(1 for row in rows if _as_bool(row.get(field))) / len(rows)
        if rows
        else 0.0
    )


def _rollup_rows(rows: Sequence[Mapping[str, Any]]) -> list[Dict[str, Any]]:
    groups: Dict[tuple[str, str, str, str, str], list[Mapping[str, Any]]] = defaultdict(list)
    for row in rows:
        base = (
            str(row["cohort"]),
            str(row["cohort_role"]),
            str(row["profile"]),
        )
        groups[(*base, "all", "all")].append(row)
        groups[(*base, "period", str(row["period"]))].append(row)
        groups[(*base, "winner_kind", str(row["winner_kind"]))].append(row)

    output = []
    for key, group in sorted(groups.items()):
        cohort, role, profile, segment_type, segment = key
        row: Dict[str, Any] = {
            "cohort": cohort,
            "cohort_role": role,
            "profile": profile,
            "segment_type": segment_type,
            "segment": segment,
            "events": len(group),
            "avg_target_exact_positions": round(
                _average(group, "target_variant_exact_position_count"),
                6,
            ),
            "avg_all_variant_exact_positions": round(
                _average(group, "all_variant_same_position_exact_count"),
                6,
            ),
            "avg_all_variant_mirror_positions": round(
                _average(group, "all_variant_same_position_mirror_count"),
                6,
            ),
            "target_exact_2plus_rate": round(
                sum(
                    1
                    for item in group
                    if int(item.get("target_variant_exact_position_count") or 0) >= 2
                )
                / len(group),
                6,
            ),
            "all_variant_exact_3of3_rate": round(
                sum(
                    1
                    for item in group
                    if int(item.get("all_variant_same_position_exact_count") or 0) == 3
                )
                / len(group),
                6,
            ),
            "front_pair_same_variant_rate": round(
                _rate(group, "front_pair_same_variant"),
                6,
            ),
            "back_pair_same_variant_rate": round(
                _rate(group, "back_pair_same_variant"),
                6,
            ),
            "double_anchor_top2_rate": round(
                _rate(
                    [
                        item
                        for item in group
                        if item.get("winner_kind") in {"double", "triple"}
                    ],
                    "double_anchor_top2",
                ),
                6,
            ),
        }
        for width in WIDTHS:
            row[f"exact_at_{width}_rate"] = round(
                _rate(group, f"exact_at_{width}"),
                6,
            )
            row[f"canonical_at_{width}_rate"] = round(
                _rate(group, f"canonical_at_{width}"),
                6,
            )
            row[f"vtrac_at_{width}_rate"] = round(
                _rate(group, f"vtrac_at_{width}"),
                6,
            )
        output.append(row)
    return output


def _decay_rows(
    baseline_reports: Mapping[tuple[str, str, str], Mapping[str, Any]],
    events_by_cohort: Mapping[str, Sequence[Mapping[str, str]]],
    cohort_by_name: Mapping[str, CohortSpec],
) -> list[Dict[str, Any]]:
    output = []
    for cohort_name, events in events_by_cohort.items():
        spec = cohort_by_name[cohort_name]
        by_state: Dict[str, list[Mapping[str, str]]] = defaultdict(list)
        for event in events:
            by_state[event["state_key"]].append(event)
        for state_key, state_events in by_state.items():
            state_events = sorted(
                state_events,
                key=lambda row: (
                    row["date"],
                    0 if row["period"] == "Midday" else 1,
                ),
            )
            for report_date in sorted(
                date
                for cohort, date, state in baseline_reports
                if cohort == cohort_name and state == state_key
            ):
                payload = baseline_reports[(cohort_name, report_date, state_key)]
                future = [
                    event for event in state_events if event["date"] >= report_date
                ][:4]
                for horizon, event in enumerate(future):
                    grade = grade_winner(
                        payload,
                        period=event["period"],
                        winner=event["winner"],
                    )
                    output.append(
                        {
                            "cohort": cohort_name,
                            "cohort_role": spec.role,
                            "report_date": report_date,
                            "state_key": state_key,
                            "draw_horizon": horizon,
                            "result_date": event["date"],
                            "period": event["period"],
                            "winner": grade["winner"],
                            "exact_at_16": grade["width_receipts"]["16"]["exact"],
                            "canonical_at_16": grade["width_receipts"]["16"][
                                "canonical_box"
                            ],
                            "vtrac_at_16": grade["width_receipts"]["16"][
                                "vtrac_box"
                            ],
                            "target_variant_exact_position_count": grade[
                                "target_variant_exact_position_count"
                            ],
                            "all_variant_same_position_exact_count": grade[
                                "all_variant_same_position_exact_count"
                            ],
                        }
                    )
    return output


def _decay_rollup_rows(
    rows: Sequence[Mapping[str, Any]],
) -> list[Dict[str, Any]]:
    output = []
    cohorts = sorted(
        {
            (str(row["cohort"]), str(row["cohort_role"]))
            for row in rows
        }
    )
    for cohort, role in cohorts:
        cohort_rows = [
            row for row in rows if str(row["cohort"]) == cohort
        ]
        for horizon in range(4):
            point_rows = [
                row
                for row in cohort_rows
                if int(row["draw_horizon"]) == horizon
            ]
            output.append(
                {
                    "cohort": cohort,
                    "cohort_role": role,
                    "mode": "at_draw_horizon",
                    "draw_horizon": horizon,
                    "denominator_kind": "result_rows",
                    "denominator": len(point_rows),
                    "exact_rate": round(_rate(point_rows, "exact_at_16"), 6),
                    "canonical_rate": round(
                        _rate(point_rows, "canonical_at_16"),
                        6,
                    ),
                    "vtrac_rate": round(_rate(point_rows, "vtrac_at_16"), 6),
                }
            )

            reports: Dict[tuple[str, str], list[Mapping[str, Any]]] = defaultdict(list)
            for row in cohort_rows:
                if int(row["draw_horizon"]) <= horizon:
                    reports[
                        (str(row["report_date"]), str(row["state_key"]))
                    ].append(row)
            cumulative_rows = [
                {
                    "exact_at_16": any(
                        _as_bool(item.get("exact_at_16")) for item in group
                    ),
                    "canonical_at_16": any(
                        _as_bool(item.get("canonical_at_16")) for item in group
                    ),
                    "vtrac_at_16": any(
                        _as_bool(item.get("vtrac_at_16")) for item in group
                    ),
                }
                for group in reports.values()
            ]
            output.append(
                {
                    "cohort": cohort,
                    "cohort_role": role,
                    "mode": "cumulative_through_horizon",
                    "draw_horizon": horizon,
                    "denominator_kind": "state_day_reports",
                    "denominator": len(cumulative_rows),
                    "exact_rate": round(
                        _rate(cumulative_rows, "exact_at_16"),
                        6,
                    ),
                    "canonical_rate": round(
                        _rate(cumulative_rows, "canonical_at_16"),
                        6,
                    ),
                    "vtrac_rate": round(
                        _rate(cumulative_rows, "vtrac_at_16"),
                        6,
                    ),
                }
            )
    return output


def _render_summary(
    *,
    cohorts: Sequence[CohortSpec],
    profiles: Sequence[ProfileSpec],
    all_rows: Sequence[Mapping[str, Any]],
    decay_rows: Sequence[Mapping[str, Any]],
    decay_rollups: Sequence[Mapping[str, Any]],
    skipped: Sequence[Mapping[str, Any]],
) -> str:
    baseline = [row for row in all_rows if row["profile"] == "native_all_variant"]
    lines = [
        "# Positional AUX CORE Harness v1",
        "",
        "This is a read-only replay harness. Positional reports are generated from",
        "frozen pre-result Aux draw snapshots; winners are joined afterward.",
        "",
        "## Coverage",
        "",
        f"- Cohorts: `{len(cohorts)}`",
        f"- Profiles: `{len(profiles)}`",
        f"- Baseline events: `{len(baseline)}`",
        f"- Profile-event rows: `{len(all_rows)}`",
        f"- Decay rows: `{len(decay_rows)}`",
        f"- Skipped/error rows: `{len(skipped)}`",
        "",
        "## Baseline By Cohort",
        "",
        "| Cohort | Role | Events | Exact@16 | Canonical@16 | VTRAC@16 | Avg target EPS | Avg all-variant EPS |",
        "|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    for spec in cohorts:
        rows = [row for row in baseline if row["cohort"] == spec.name]
        lines.append(
            "| "
            + " | ".join(
                [
                    spec.name,
                    spec.role,
                    str(len(rows)),
                    f"{100 * _rate(rows, 'exact_at_16'):.1f}%",
                    f"{100 * _rate(rows, 'canonical_at_16'):.1f}%",
                    f"{100 * _rate(rows, 'vtrac_at_16'):.1f}%",
                    f"{_average(rows, 'target_variant_exact_position_count'):.3f}",
                    f"{_average(rows, 'all_variant_same_position_exact_count'):.3f}",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Cumulative Same-State Decay",
            "",
            "| Cohort | Through draw | State-day reports | Exact@16 | Canonical@16 | VTRAC@16 |",
            "|---|---:|---:|---:|---:|---:|",
        ]
    )
    for spec in cohorts:
        for horizon in range(4):
            row = next(
                item
                for item in decay_rollups
                if item["cohort"] == spec.name
                and item["mode"] == "cumulative_through_horizon"
                and int(item["draw_horizon"]) == horizon
            )
            lines.append(
                "| "
                + " | ".join(
                    [
                        spec.name,
                        str(horizon),
                        str(row["denominator"]),
                        f"{100 * float(row['exact_rate']):.1f}%",
                        f"{100 * float(row['canonical_rate']):.1f}%",
                        f"{100 * float(row['vtrac_rate']):.1f}%",
                    ]
                )
                + " |"
            )
    lines.extend(
        [
            "",
            "## Interpretation Boundary",
            "",
            "- Exact, canonical, and VTRAC coverage are reported separately.",
            "- Position and pair support remain evidence receipts, not final predictions.",
            "- Ablations diagnose sensitivity; they do not select new production weights.",
            "- The target-VTRAC profile is an experimental use of the target variant's",
            "  frozen top-overdue indices, not a claim about current sharepack behavior.",
            "- The forced-due-double profile is an always-on sensitivity test because",
            "  the native `>=71` trigger did not activate in these cohorts.",
            "- Decay horizon 0 is the first observed result on the report date; later",
            "  horizons are the next observed draws for the same state, not calendar days.",
            "- No raw score is compared across different Aux tools.",
            "",
        ]
    )
    return "\n".join(lines)


def _manifest(
    *,
    cohorts: Sequence[CohortSpec],
    profiles: Sequence[ProfileSpec],
    output_dir: Path,
    counts: Mapping[str, int],
) -> Dict[str, Any]:
    artifacts = []
    for path in sorted(output_dir.iterdir()):
        if not path.is_file() or path.name == "MANIFEST.json":
            continue
        artifacts.append(
            {
                "path": safe_rel(path),
                "sha256": sha256_file(path),
                "bytes": path.stat().st_size,
            }
        )
    return {
        "schema_version": "positional_aux_core_harness_manifest_v1",
        "runtime_mutation": False,
        "winner_join_phase": "post_result_grading",
        "cohorts": [
            {
                "name": spec.name,
                "role": spec.role,
                "day_root": safe_rel(spec.day_root),
                "winner_ledger": safe_rel(spec.winner_ledger),
                "winner_ledger_sha256": sha256_file(spec.winner_ledger),
            }
            for spec in cohorts
        ],
        "profiles": [spec.name for spec in profiles],
        "counts": dict(counts),
        "artifacts": artifacts,
    }


def run(
    *,
    cohorts: Sequence[CohortSpec],
    profiles: Sequence[ProfileSpec],
    output_dir: Path,
    event_limit: int = 0,
    force: bool = False,
) -> Dict[str, Any]:
    if output_dir.exists() and any(output_dir.iterdir()) and not force:
        raise FileExistsError(
            f"Output directory is not empty; pass --force: {output_dir}"
        )
    output_dir.mkdir(parents=True, exist_ok=True)
    if force:
        for child in output_dir.iterdir():
            if child.is_file() and child.name in GENERATED_FILENAMES:
                child.unlink()
            elif child.is_dir():
                raise IsADirectoryError(
                    f"Refusing to recursively delete existing directory: {child}"
                )

    profile_map = {spec.name: spec for spec in profiles}
    if "native_all_variant" not in profile_map:
        raise ValueError("The baseline native_all_variant profile is mandatory")

    all_rows: list[Dict[str, Any]] = []
    feature_rows: list[Dict[str, Any]] = []
    skipped: list[Dict[str, Any]] = []
    baseline_reports: Dict[tuple[str, str, str], Dict[str, Any]] = {}
    events_by_cohort: Dict[str, list[Dict[str, str]]] = {}
    example_written = False

    for cohort in cohorts:
        events = _load_events(cohort)
        if event_limit:
            events = events[:event_limit]
        events_by_cohort[cohort.name] = events
        grouped: Dict[tuple[str, str], list[Dict[str, str]]] = defaultdict(list)
        for event in events:
            grouped[(event["date"], event["state_key"])].append(event)

        for (results_date, state_key), state_events in sorted(grouped.items()):
            day_dir = cohort.day_root / results_date
            draws_dir = _state_draws_dir(day_dir, state_key)
            summary_path = _state_summary_path(day_dir, state_key)
            try:
                meta = _load_meta(day_dir)
                history_date = str(meta.get("history_date") or "")
                if history_date and history_date >= results_date:
                    raise ValueError(
                        f"Non-predictive history boundary {history_date} >= {results_date}"
                    )
            except Exception as exc:
                skipped.append(
                    {
                        "cohort": cohort.name,
                        "date": results_date,
                        "state_key": state_key,
                        "profile": "*",
                        "error": f"meta:{type(exc).__name__}:{exc}",
                    }
                )
                continue

            static_cache: Dict[str, Dict[str, Any]] = {}
            for profile in profiles:
                if profile.scope != "static":
                    continue
                try:
                    static_cache[profile.name] = _build_profile_report(
                        spec=profile,
                        state_key=state_key,
                        results_date=results_date,
                        period=state_events[0]["period"],
                        draws_dir=draws_dir,
                        summary_path=summary_path,
                    )
                except Exception as exc:
                    skipped.append(
                        {
                            "cohort": cohort.name,
                            "date": results_date,
                            "state_key": state_key,
                            "profile": profile.name,
                            "error": f"{type(exc).__name__}:{exc}",
                        }
                    )
            baseline = static_cache.get("native_all_variant")
            if baseline is not None:
                baseline_reports[(cohort.name, results_date, state_key)] = baseline

            target_cache: Dict[tuple[str, str], Dict[str, Any]] = {}
            for event in state_events:
                for profile in profiles:
                    payload = static_cache.get(profile.name)
                    if payload is None and profile.scope != "static":
                        cache_key = (profile.name, event["period"])
                        payload = target_cache.get(cache_key)
                        if payload is None:
                            try:
                                payload = _build_profile_report(
                                    spec=profile,
                                    state_key=state_key,
                                    results_date=results_date,
                                    period=event["period"],
                                    draws_dir=draws_dir,
                                    summary_path=summary_path,
                                )
                                target_cache[cache_key] = payload
                            except Exception as exc:
                                skipped.append(
                                    {
                                        "cohort": cohort.name,
                                        "date": results_date,
                                        "state_key": state_key,
                                        "profile": profile.name,
                                        "period": event["period"],
                                        "error": f"{type(exc).__name__}:{exc}",
                                    }
                                )
                                continue
                    if payload is None:
                        continue
                    grade = grade_winner(
                        payload,
                        period=event["period"],
                        winner=event["winner"],
                    )
                    row = _flatten_grade(
                        cohort=cohort,
                        event=event,
                        profile=profile.name,
                        payload=payload,
                        grade=grade,
                        include_receipts=False,
                    )
                    all_rows.append(row)
                    if profile.name == "native_all_variant":
                        feature_rows.append(
                            _flatten_grade(
                                cohort=cohort,
                                event=event,
                                profile=profile.name,
                                payload=payload,
                                grade=grade,
                                include_receipts=True,
                            )
                        )
                    if (
                        not example_written
                        and results_date == "2026-03-09"
                        and state_key == "Connecticut4"
                        and event["period"] == "Evening"
                        and event["winner"] == "091"
                        and profile.name == "native_all_variant"
                    ):
                        example = {
                            "frozen_positional_report": payload,
                            "post_result_grading": grade,
                        }
                        write_json(
                            output_dir
                            / "EXAMPLE__2026-03-09__Connecticut4__Evening__091.json",
                            example,
                        )
                        (
                            output_dir
                            / "EXAMPLE__2026-03-09__Connecticut4__Evening__091.md"
                        ).write_text(
                            render_report_markdown(payload, grading=grade),
                            encoding="utf-8",
                        )
                        example_written = True

    rollups = _rollup_rows(all_rows)
    cohort_by_name = {spec.name: spec for spec in cohorts}
    decay_rows = _decay_rows(
        baseline_reports,
        events_by_cohort,
        cohort_by_name,
    )
    decay_rollups = _decay_rollup_rows(decay_rows)

    _write_csv(output_dir / "POSITIONAL_FEATURE_LEDGER.csv", feature_rows)
    _write_csv(output_dir / "POSITIONAL_ABLATION_LEDGER.csv", all_rows)
    _write_csv(output_dir / "POSITIONAL_ROLLUP.csv", rollups)
    _write_csv(output_dir / "POSITIONAL_DECAY_LEDGER.csv", decay_rows)
    _write_csv(output_dir / "POSITIONAL_DECAY_ROLLUP.csv", decay_rollups)
    _write_csv(output_dir / "SKIPPED_OR_ERROR_ROWS.csv", skipped)
    (output_dir / "START_HERE.md").write_text(
        _render_summary(
            cohorts=cohorts,
            profiles=profiles,
            all_rows=all_rows,
            decay_rows=decay_rows,
            decay_rollups=decay_rollups,
            skipped=skipped,
        ),
        encoding="utf-8",
    )

    counts = {
        "baseline_events": len(feature_rows),
        "profile_event_rows": len(all_rows),
        "rollup_rows": len(rollups),
        "decay_rows": len(decay_rows),
        "decay_rollup_rows": len(decay_rollups),
        "winner_ledger_source_rows": sum(
            int(row.get("winner_ledger_row_count") or 0)
            for row in feature_rows
        ),
        "winner_ledger_pre_draw_rows": sum(
            int(row.get("winner_ledger_pre_draw_row_count") or 0)
            for row in feature_rows
        ),
        "winner_ledger_post_result_rows": sum(
            int(row.get("winner_ledger_post_result_row_count") or 0)
            for row in feature_rows
        ),
        "skipped_or_error_rows": len(skipped),
    }
    write_json(
        output_dir / "MANIFEST.json",
        _manifest(
            cohorts=cohorts,
            profiles=profiles,
            output_dir=output_dir,
            counts=counts,
        ),
    )
    return counts


def main() -> None:
    args = _parse_args()
    cohorts = (
        tuple(_parse_cohort(value) for value in args.cohort)
        if args.cohort
        else DEFAULT_COHORTS
    )
    available = {spec.name: spec for spec in _profiles()}
    if args.profile:
        unknown = [name for name in args.profile if name not in available]
        if unknown:
            raise SystemExit(f"Unknown profiles: {', '.join(unknown)}")
        profiles = tuple(available[name] for name in args.profile)
        if "native_all_variant" not in {spec.name for spec in profiles}:
            profiles = (available["native_all_variant"], *profiles)
    else:
        profiles = _profiles()
    counts = run(
        cohorts=cohorts,
        profiles=profiles,
        output_dir=_resolve(args.output_dir),
        event_limit=max(0, int(args.event_limit)),
        force=bool(args.force),
    )
    print(json.dumps(counts, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
