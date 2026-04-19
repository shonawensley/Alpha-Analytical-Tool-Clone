#!/usr/bin/env python3
"""Create the Stage-4C Analysis Arena shadow translator prototype package.

Stage 4C is a read-only design layer on top of Stage 4B. It does not change
live scoring, candidate generation, translator logic, budget logic, or legacy
infrastructure. It translates the Stage 4B primitive-cluster queue into strict
prototype lanes so future scoring work can be discussed without accidentally
granting live-play permission.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.tools.analysis_arena_window_utils import safe_rel  # type: ignore
from scripts.tools.create_analysis_arena_stage4_fixture_replay_harness import (  # type: ignore
    RUNS_2_DIR,
    _counter_text,
    _fmt,
    _pct,
    _rate,
    _read_csv_rows,
    _resolve_path,
    _safe_float,
    _safe_int,
    _write_csv,
    _write_json,
    _write_text,
)
from scripts.tools.create_analysis_arena_stage4b_replay_readback import _cluster_key  # type: ignore


STAGE4C_PREFIX = "ANALYSIS_ARENA__CYCLE__STAGE4C"


LANE_BY_ACTION = {
    "prototype_as_read_only_boxed_translator_rule": "clean_boxed_candidate",
    "prototype_with_lineage_deduplication": "lineage_guarded_boxed_candidate",
    "prototype_as_gate_not_standalone": "support_gate_only",
    "keep_in_decay_watch_not_boxed_spend": "decay_watch_only",
    "retest_by_state_and_consider_penalty": "concentration_retest_or_restraint",
    "collect_more_windows_before_promotion": "low_denominator_watchlist",
}

PERMISSION_BY_LANE = {
    "clean_boxed_candidate": "shadow_box_candidate_expression",
    "lineage_guarded_boxed_candidate": "shadow_box_candidate_expression_with_dedup",
    "support_gate_only": "shadow_confidence_boost_only",
    "decay_watch_only": "shadow_decay_watch_only",
    "concentration_retest_or_restraint": "shadow_restraint_or_retest",
    "low_denominator_watchlist": "shadow_collect_more_windows",
}

GUARDRAIL_BY_LANE = {
    "clean_boxed_candidate": "read_only_candidate_expression_no_live_scoring",
    "lineage_guarded_boxed_candidate": "read_only_candidate_expression_requires_lineage_dedup",
    "support_gate_only": "support_gate_never_standalone_candidate",
    "decay_watch_only": "decay_or_vtrac_watch_never_boxed_spend_permission",
    "concentration_retest_or_restraint": "concentration_block_requires_broader_state_retest",
    "low_denominator_watchlist": "insufficient_denominator_collect_more_windows",
}

MODE_LANES = {
    "clean_boxed_only": {"clean_boxed_candidate"},
    "clean_plus_lineage_deduped": {"clean_boxed_candidate", "lineage_guarded_boxed_candidate"},
    "support_gate_context": {"support_gate_only"},
    "decay_watch_context": {"decay_watch_only"},
    "restraint_retest": {"concentration_retest_or_restraint"},
    "low_denominator_watchlist": {"low_denominator_watchlist"},
}

CASEBOOK_LANE_ORDER = [
    "clean_boxed_candidate",
    "lineage_guarded_boxed_candidate",
    "support_gate_only",
    "decay_watch_only",
    "concentration_retest_or_restraint",
    "low_denominator_watchlist",
]


def _parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--runs2-dir", default=str(RUNS_2_DIR), help="RUNS_2 root containing Stage-4B outputs.")
    ap.add_argument("--output-dir", default=str(RUNS_2_DIR), help="Cycle-level output directory.")
    ap.add_argument("--casebook-limit", type=int, default=96, help="Maximum casebook rows to emit.")
    ap.add_argument("--force", action="store_true", help="Overwrite existing Stage-4C outputs.")
    return ap.parse_args()


def _stage_paths(runs2_dir: Path) -> Dict[str, Path]:
    return {
        "stage4b_md": runs2_dir / "ANALYSIS_ARENA__CYCLE__STAGE4B_REPLAY_READBACK.md",
        "stage4b_cluster_csv": runs2_dir / "ANALYSIS_ARENA__CYCLE__STAGE4B_PRIMITIVE_CLUSTER_REGISTRY.csv",
        "stage4b_queue_csv": runs2_dir / "ANALYSIS_ARENA__CYCLE__STAGE4B_TRANSLATOR_DESIGN_QUEUE.csv",
        "stage4b_holdout_csv": runs2_dir / "ANALYSIS_ARENA__CYCLE__STAGE4B_LEAVE_ONE_WINDOW_OUT_MATRIX.csv",
        "stage4b_casebook_csv": runs2_dir / "ANALYSIS_ARENA__CYCLE__STAGE4B_SURVIVOR_SUPPORT_RESTRAINT_CASEBOOK.csv",
        "stage4_negative_csv": runs2_dir / "ANALYSIS_ARENA__CYCLE__STAGE4_NEGATIVE_CONTROL_REPLAY_SUMMARY.csv",
        "stage4_ledger_csv": runs2_dir / "ANALYSIS_ARENA__CYCLE__STAGE4_FIXTURE_REPLAY_LEDGER.csv",
    }


def _cycle_paths(output_dir: Path) -> Dict[str, Path]:
    return {
        "md": output_dir / f"{STAGE4C_PREFIX}_SHADOW_TRANSLATOR_PROTOTYPE.md",
        "json": output_dir / f"{STAGE4C_PREFIX}_SHADOW_TRANSLATOR_PROTOTYPE.json",
        "rule_registry_csv": output_dir / f"{STAGE4C_PREFIX}_PROTOTYPE_RULE_REGISTRY.csv",
        "lane_matrix_csv": output_dir / f"{STAGE4C_PREFIX}_LANE_SEPARATION_MATRIX.csv",
        "support_effects_csv": output_dir / f"{STAGE4C_PREFIX}_SUPPORT_GATE_EFFECTS.csv",
        "restraint_audit_csv": output_dir / f"{STAGE4C_PREFIX}_RESTRAINT_APPLICATION_AUDIT.csv",
        "holdout_scorecard_csv": output_dir / f"{STAGE4C_PREFIX}_HOLDOUT_PROTOTYPE_SCORECARD.csv",
        "casebook_csv": output_dir / f"{STAGE4C_PREFIX}_TRANSLATOR_PROTOTYPE_CASEBOOK.csv",
        "casebook_md": output_dir / f"{STAGE4C_PREFIX}_TRANSLATOR_PROTOTYPE_CASEBOOK.md",
    }


def _confidence_tier(row: Dict[str, Any]) -> str:
    holdout_rate = _safe_float(row.get("holdout_confirmation_rate"))
    positive_per100 = _safe_float(row.get("positive_conversions_per_100_state_days"))
    support_per100 = _safe_float(row.get("supported_events_per_100_state_days"))
    if holdout_rate >= 0.80 and positive_per100 > 0.75:
        return "strong_shadow_research_candidate"
    if holdout_rate >= 0.60 and positive_per100 > 0:
        return "moderate_shadow_research_candidate"
    if holdout_rate >= 0.40 or positive_per100 > 0 or support_per100 > 0:
        return "watch_shadow_research_candidate"
    return "weak_or_context_only"


def _restraint_pressure(negative_row: Dict[str, Any] | None) -> str:
    if not negative_row:
        return "low"
    count = _safe_int(negative_row.get("negative_control_count"))
    fp_rate = _safe_float(negative_row.get("avg_false_positive_proxy_rate"))
    if count >= 100 or fp_rate >= 0.99:
        return "high"
    if count > 0:
        return "medium"
    return "low"


def _negative_key(row: Dict[str, Any]) -> str:
    return f"{row.get('mechanism_family') or ''}::{row.get('future_primitive') or ''}"


def _avg(values: Iterable[Any]) -> float:
    nums = [_safe_float(value) for value in values]
    return sum(nums) / len(nums) if nums else 0.0


def _top_rule_sort(row: Dict[str, Any]) -> tuple[Any, ...]:
    return (
        -_safe_float(row.get("holdout_confirmation_rate")),
        -_safe_float(row.get("positive_conversions_per_100_state_days")),
        -_safe_float(row.get("supported_events_per_100_state_days")),
        str(row.get("cluster_key") or ""),
    )


def _build_rule_registry(
    queue_rows: Sequence[Dict[str, str]],
    cluster_rows: Sequence[Dict[str, str]],
    negative_rows: Sequence[Dict[str, str]],
) -> List[Dict[str, Any]]:
    clusters_by_key = {str(row.get("cluster_key") or ""): row for row in cluster_rows}
    negative_by_key = {_negative_key(row): row for row in negative_rows}

    out: List[Dict[str, Any]] = []
    for row in queue_rows:
        cluster_key = str(row.get("cluster_key") or "")
        next_action = str(row.get("next_action") or "")
        lane = LANE_BY_ACTION.get(next_action, "unmapped_research_only")
        cluster = clusters_by_key.get(cluster_key, {})
        negative = negative_by_key.get(_negative_key(row))
        confidence = _confidence_tier(row)
        pressure = _restraint_pressure(negative)
        mode_memberships = [mode for mode, lanes in MODE_LANES.items() if lane in lanes]

        out.append(
            {
                "cluster_key": cluster_key,
                "mechanism_family": row.get("mechanism_family"),
                "future_primitive": row.get("future_primitive"),
                "recommended_cluster_use": row.get("recommended_cluster_use"),
                "stage4b_next_action": next_action,
                "prototype_lane": lane,
                "shadow_permission": PERMISSION_BY_LANE.get(lane, "shadow_research_only"),
                "confidence_tier": confidence,
                "guardrail": GUARDRAIL_BY_LANE.get(lane, "unmapped_no_promotion"),
                "include_in_modes": "|".join(mode_memberships),
                "entity_count": row.get("entity_count"),
                "stage4_decision_mix": row.get("stage4_decision_mix"),
                "shared_lineage_risk_mix": cluster.get("shared_lineage_risk_mix", ""),
                "holdout_confirmed": row.get("holdout_confirmed"),
                "holdout_missed": row.get("holdout_missed"),
                "holdout_confirmation_rate": row.get("holdout_confirmation_rate"),
                "positive_conversions_per_100_state_days": row.get("positive_conversions_per_100_state_days"),
                "supported_events_per_100_state_days": row.get("supported_events_per_100_state_days"),
                "avg_pool_or_exposure_per_state_day": cluster.get("avg_pool_or_exposure_per_state_day", ""),
                "pool_normalized_positive_yield": cluster.get("pool_normalized_positive_yield", ""),
                "representative_entity": row.get("representative_entity"),
                "entity_sample": cluster.get("entity_sample", ""),
                "negative_control_count": negative.get("negative_control_count", "0") if negative else "0",
                "negative_avg_false_positive_proxy_rate": negative.get("avg_false_positive_proxy_rate", "0") if negative else "0",
                "negative_restraint_use": negative.get("restraint_use", "") if negative else "",
                "restraint_pressure": pressure,
                "live_scoring_permission": "none",
                "candidate_generation_permission": "none",
            }
        )

    lane_order = {lane: idx for idx, lane in enumerate(CASEBOOK_LANE_ORDER)}
    return sorted(out, key=lambda row: (lane_order.get(str(row.get("prototype_lane") or ""), 99), *_top_rule_sort(row)))


def _build_lane_matrix(rule_rows: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    grouped: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for row in rule_rows:
        grouped[str(row.get("prototype_lane") or "unknown")].append(row)

    out: List[Dict[str, Any]] = []
    for lane in CASEBOOK_LANE_ORDER + sorted(set(grouped) - set(CASEBOOK_LANE_ORDER)):
        rows = grouped.get(lane, [])
        if not rows:
            continue
        confirmed = sum(_safe_int(row.get("holdout_confirmed")) for row in rows)
        missed = sum(_safe_int(row.get("holdout_missed")) for row in rows)
        tiers = Counter(str(row.get("confidence_tier") or "") for row in rows)
        pressures = Counter(str(row.get("restraint_pressure") or "") for row in rows)
        out.append(
            {
                "prototype_lane": lane,
                "rule_count": len(rows),
                "holdout_confirmed": confirmed,
                "holdout_missed": missed,
                "holdout_confirmation_rate": _rate(confirmed, confirmed + missed),
                "avg_rule_holdout_confirmation_rate": _avg(row.get("holdout_confirmation_rate") for row in rows),
                "avg_positive_conversions_per_100_state_days": _avg(row.get("positive_conversions_per_100_state_days") for row in rows),
                "avg_supported_events_per_100_state_days": _avg(row.get("supported_events_per_100_state_days") for row in rows),
                "strong_count": tiers.get("strong_shadow_research_candidate", 0),
                "moderate_count": tiers.get("moderate_shadow_research_candidate", 0),
                "watch_count": tiers.get("watch_shadow_research_candidate", 0),
                "weak_count": tiers.get("weak_or_context_only", 0),
                "restraint_pressure_mix": _counter_text(pressures),
                "shadow_permission": PERMISSION_BY_LANE.get(lane, "shadow_research_only"),
                "lane_guardrail": GUARDRAIL_BY_LANE.get(lane, "unmapped_no_promotion"),
            }
        )
    return out


def _build_holdout_scorecard(
    rule_rows: Sequence[Dict[str, Any]],
    holdout_rows: Sequence[Dict[str, str]],
) -> List[Dict[str, Any]]:
    lane_by_cluster = {str(row.get("cluster_key") or ""): str(row.get("prototype_lane") or "") for row in rule_rows}
    grouped: Dict[tuple[str, str], List[Dict[str, str]]] = defaultdict(list)
    for row in holdout_rows:
        cluster_key = _cluster_key(row)
        lane = lane_by_cluster.get(cluster_key)
        if not lane:
            continue
        for mode, lanes in MODE_LANES.items():
            if lane in lanes:
                grouped[(mode, str(row.get("holdout_window") or ""))].append(row)

    out: List[Dict[str, Any]] = []
    for (mode, holdout_window), rows in sorted(grouped.items()):
        outcomes = Counter(str(row.get("holdout_outcome") or "") for row in rows)
        confirmed = outcomes.get("holdout_confirmed", 0)
        missed = outcomes.get("holdout_missed", 0)
        train_failed = outcomes.get("train_did_not_survive", 0)
        no_denominator = outcomes.get("no_holdout_denominator", 0)
        clusters = {_cluster_key(row) for row in rows}
        out.append(
            {
                "prototype_mode": mode,
                "holdout_window": holdout_window,
                "rule_rows": len(rows),
                "cluster_count": len(clusters),
                "holdout_confirmed": confirmed,
                "holdout_missed": missed,
                "train_did_not_survive": train_failed,
                "no_holdout_denominator": no_denominator,
                "holdout_confirmation_rate": _rate(confirmed, confirmed + missed),
                "holdout_supported_event_count": sum(_safe_int(row.get("holdout_supported_event_count")) for row in rows),
                "holdout_positive_conversion_event_count": sum(_safe_int(row.get("holdout_positive_conversion_event_count")) for row in rows),
                "holdout_wrong_lane_event_count": sum(_safe_int(row.get("holdout_wrong_lane_event_count")) for row in rows),
                "outcome_mix": _counter_text(outcomes),
                "guardrail": "mode_scorecard_is_read_only_no_live_scoring_permission",
            }
        )
    return out


def _build_support_gate_effects(rule_rows: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    candidate_lanes = {"clean_boxed_candidate", "lineage_guarded_boxed_candidate"}
    candidates = [row for row in rule_rows if str(row.get("prototype_lane") or "") in candidate_lanes]
    supports = [row for row in rule_rows if str(row.get("prototype_lane") or "") == "support_gate_only"]

    out: List[Dict[str, Any]] = []
    for support in supports:
        same_family = [
            row for row in candidates if str(row.get("mechanism_family") or "") == str(support.get("mechanism_family") or "")
        ]
        same_primitive = [
            row for row in candidates if str(row.get("future_primitive") or "") == str(support.get("future_primitive") or "")
        ]
        best_pool = same_primitive or same_family
        best = sorted(best_pool, key=_top_rule_sort)[0] if best_pool else {}
        out.append(
            {
                "support_cluster_key": support.get("cluster_key"),
                "support_mechanism_family": support.get("mechanism_family"),
                "support_future_primitive": support.get("future_primitive"),
                "support_holdout_confirmation_rate": support.get("holdout_confirmation_rate"),
                "support_supported_events_per_100_state_days": support.get("supported_events_per_100_state_days"),
                "same_family_candidate_count": len(same_family),
                "same_primitive_candidate_count": len(same_primitive),
                "best_candidate_cluster_key": best.get("cluster_key", ""),
                "best_candidate_lane": best.get("prototype_lane", ""),
                "best_candidate_holdout_confirmation_rate": best.get("holdout_confirmation_rate", ""),
                "best_candidate_positive_conversions_per_100_state_days": best.get(
                    "positive_conversions_per_100_state_days", ""
                ),
                "support_effect_class": "paired_support_context" if best else "unpaired_support_context",
                "guardrail": "support_gate_can_boost_context_only_never_standalone",
            }
        )
    return sorted(
        out,
        key=lambda row: (
            str(row.get("support_effect_class") or ""),
            -_safe_int(row.get("same_primitive_candidate_count")),
            -_safe_int(row.get("same_family_candidate_count")),
            -_safe_float(row.get("support_holdout_confirmation_rate")),
            str(row.get("support_cluster_key") or ""),
        ),
    )


def _build_restraint_audit(
    rule_rows: Sequence[Dict[str, Any]],
    negative_rows: Sequence[Dict[str, str]],
) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for row in negative_rows:
        out.append(
            {
                "audit_type": "negative_control_family",
                "cluster_key": "",
                "mechanism_family": row.get("mechanism_family"),
                "future_primitive": row.get("future_primitive"),
                "prototype_lane": "negative_control_restraint_library",
                "negative_control_count": row.get("negative_control_count"),
                "avg_false_positive_proxy_rate": row.get("avg_false_positive_proxy_rate"),
                "avg_match_rate": row.get("avg_match_rate"),
                "avg_event_support_rate": row.get("avg_event_support_rate"),
                "restraint_pressure": _restraint_pressure(row),
                "restraint_application": "candidate_penalty_or_veto_surface_only",
                "guardrail": "negative_controls_cannot_promote_directly",
            }
        )

    for row in rule_rows:
        lane = str(row.get("prototype_lane") or "")
        pressure = str(row.get("restraint_pressure") or "")
        if lane == "concentration_retest_or_restraint" or pressure == "high":
            out.append(
                {
                    "audit_type": "prototype_rule_restraint_pressure",
                    "cluster_key": row.get("cluster_key"),
                    "mechanism_family": row.get("mechanism_family"),
                    "future_primitive": row.get("future_primitive"),
                    "prototype_lane": lane,
                    "negative_control_count": row.get("negative_control_count"),
                    "avg_false_positive_proxy_rate": row.get("negative_avg_false_positive_proxy_rate"),
                    "avg_match_rate": "",
                    "avg_event_support_rate": "",
                    "restraint_pressure": pressure,
                    "restraint_application": _restraint_application(row),
                    "guardrail": row.get("guardrail"),
                }
            )
    return sorted(
        out,
        key=lambda row: (
            str(row.get("audit_type") or ""),
            str(row.get("mechanism_family") or ""),
            str(row.get("future_primitive") or ""),
            str(row.get("cluster_key") or ""),
        ),
    )


def _restraint_application(row: Dict[str, Any]) -> str:
    lane = str(row.get("prototype_lane") or "")
    pressure = str(row.get("restraint_pressure") or "")
    if lane == "concentration_retest_or_restraint":
        return "retest_by_state_before_any_candidate_expression"
    if pressure == "high":
        return "apply_future_penalty_or_veto_review_before_candidate_expression"
    return "monitor_only"


def _build_casebook_rows(rule_rows: Sequence[Dict[str, Any]], *, limit: int) -> List[Dict[str, Any]]:
    per_lane_limit = max(4, int(limit) // max(len(CASEBOOK_LANE_ORDER), 1))
    rows_by_lane: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for row in sorted(rule_rows, key=_top_rule_sort):
        lane = str(row.get("prototype_lane") or "")
        if lane not in CASEBOOK_LANE_ORDER:
            continue
        if len(rows_by_lane[lane]) >= per_lane_limit:
            continue
        rows_by_lane[lane].append(row)

    out: List[Dict[str, Any]] = []
    for lane in CASEBOOK_LANE_ORDER:
        for row in rows_by_lane.get(lane, []):
            out.append(
                {
                    "casebook_lane": lane,
                    "cluster_key": row.get("cluster_key"),
                    "mechanism_family": row.get("mechanism_family"),
                    "future_primitive": row.get("future_primitive"),
                    "confidence_tier": row.get("confidence_tier"),
                    "holdout_confirmation_rate": row.get("holdout_confirmation_rate"),
                    "positive_conversions_per_100_state_days": row.get("positive_conversions_per_100_state_days"),
                    "supported_events_per_100_state_days": row.get("supported_events_per_100_state_days"),
                    "restraint_pressure": row.get("restraint_pressure"),
                    "shadow_permission": row.get("shadow_permission"),
                    "guardrail": row.get("guardrail"),
                    "representative_entity": row.get("representative_entity"),
                    "casebook_note": _casebook_note(row),
                }
            )
    return out[: max(int(limit), 0)]


def _casebook_note(row: Dict[str, Any]) -> str:
    lane = str(row.get("prototype_lane") or "")
    if lane == "clean_boxed_candidate":
        return "cleanest shadow translator material; still read-only and aggregate-level"
    if lane == "lineage_guarded_boxed_candidate":
        return "useful candidate material only if duplicate lineage credit is removed"
    if lane == "support_gate_only":
        return "context booster only; pair with sharper bounded candidate evidence"
    if lane == "decay_watch_only":
        return "carryforward/territory evidence only; not boxed spend permission"
    if lane == "concentration_retest_or_restraint":
        return "retest or restraint case; likely fragile until broader support appears"
    if lane == "low_denominator_watchlist":
        return "thin denominator; preserve for future windows before promotion"
    return "research-only example"


def _write_casebook_md(path: Path, rows: Sequence[Dict[str, Any]], *, force: bool) -> None:
    grouped: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[str(row.get("casebook_lane") or "unknown")].append(row)

    lines: List[str] = [
        "# Stage 4C Shadow Translator Prototype Casebook",
        "",
        "Purpose: compact Stage 4C examples by prototype lane. These are design examples only, not live rules.",
        "",
    ]
    for lane in CASEBOOK_LANE_ORDER:
        lane_rows = grouped.get(lane, [])
        if not lane_rows:
            continue
        lines += [
            f"## {lane}",
            "",
            "| cluster | holdout | pos/100 ASD | support/100 ASD | pressure | note |",
            "|---|---:|---:|---:|---:|---|",
        ]
        for row in lane_rows:
            lines.append(
                "| "
                + " | ".join(
                    [
                        f"`{row.get('cluster_key')}`",
                        _pct(row.get("holdout_confirmation_rate")),
                        _fmt(row.get("positive_conversions_per_100_state_days")),
                        _fmt(row.get("supported_events_per_100_state_days")),
                        str(row.get("restraint_pressure")),
                        str(row.get("casebook_note")),
                    ]
                )
                + " |"
            )
        lines.append("")
    _write_text(path, "\n".join(lines), force=force)


def _build_markdown(
    *,
    runs2_dir: Path,
    paths: Dict[str, Path],
    rule_rows: Sequence[Dict[str, Any]],
    lane_rows: Sequence[Dict[str, Any]],
    support_rows: Sequence[Dict[str, Any]],
    restraint_rows: Sequence[Dict[str, Any]],
    holdout_rows: Sequence[Dict[str, Any]],
    casebook_rows: Sequence[Dict[str, Any]],
) -> str:
    lanes = Counter(str(row.get("prototype_lane") or "") for row in rule_rows)
    permissions = Counter(str(row.get("shadow_permission") or "") for row in rule_rows)
    pressure = Counter(str(row.get("restraint_pressure") or "") for row in rule_rows)
    top_clean = [
        row
        for row in rule_rows
        if str(row.get("prototype_lane") or "") in {"clean_boxed_candidate", "lineage_guarded_boxed_candidate"}
    ][:20]
    mode_totals: Dict[str, Counter[str]] = defaultdict(Counter)
    for row in holdout_rows:
        mode_totals[str(row.get("prototype_mode") or "")]["confirmed"] += _safe_int(row.get("holdout_confirmed"))
        mode_totals[str(row.get("prototype_mode") or "")]["missed"] += _safe_int(row.get("holdout_missed"))

    lines: List[str] = [
        "# Analysis Arena Stage 4C Shadow Translator Prototype",
        "",
        "Purpose: convert Stage 4B primitive clusters into a read-only shadow translator design package with strict lane separation.",
        "",
        "## Metadata",
        f"- runs2_dir: `{safe_rel(runs2_dir)}`",
        f"- prototype_rule_rows: `{len(rule_rows)}`",
        f"- lane_matrix_rows: `{len(lane_rows)}`",
        f"- support_gate_effect_rows: `{len(support_rows)}`",
        f"- restraint_audit_rows: `{len(restraint_rows)}`",
        f"- holdout_scorecard_rows: `{len(holdout_rows)}`",
        f"- casebook_rows: `{len(casebook_rows)}`",
        "",
        "## Non-Negotiable Guardrails",
        "- Stage 4C is read-only and cannot change live scoring, candidate generation, translator logic, budget logic, or legacy infrastructure.",
        "- Clean candidate lanes are aggregate shadow expressions only; they are not deployable candidate lists.",
        "- Lineage-guarded lanes require duplicate-credit removal before any future scoring prototype.",
        "- Support gates cannot stand alone. They can only provide context beside sharper bounded evidence.",
        "- VTRAC/decay lanes stay in carryforward/watch territory and cannot become boxed spend permission.",
        "- Concentration and negative-control pressure become restraint/retest surfaces, not promotion surfaces.",
        "- Old-system source names remain locators; `future_primitive` labels are the architecture-facing vocabulary.",
        "",
        "## Prototype Lane Counts",
        "",
    ]
    for key, count in lanes.most_common():
        lines.append(f"- `{key}`: `{count}`")
    lines += ["", "## Shadow Permission Counts", ""]
    for key, count in permissions.most_common():
        lines.append(f"- `{key}`: `{count}`")
    lines += ["", "## Restraint Pressure Counts", ""]
    for key, count in pressure.most_common():
        lines.append(f"- `{key}`: `{count}`")

    lines += [
        "",
        "## Lane Separation Matrix",
        "",
        "| lane | rules | holdout | avg pos/100 ASD | avg support/100 ASD | pressure mix | guardrail |",
        "|---|---:|---:|---:|---:|---|---|",
    ]
    for row in lane_rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{row.get('prototype_lane')}`",
                    str(row.get("rule_count")),
                    _pct(row.get("holdout_confirmation_rate")),
                    _fmt(row.get("avg_positive_conversions_per_100_state_days")),
                    _fmt(row.get("avg_supported_events_per_100_state_days")),
                    f"`{row.get('restraint_pressure_mix')}`",
                    str(row.get("lane_guardrail")),
                ]
            )
            + " |"
        )

    lines += ["", "## Holdout Mode Summary", ""]
    for mode in sorted(mode_totals):
        confirmed = mode_totals[mode]["confirmed"]
        missed = mode_totals[mode]["missed"]
        lines.append(f"- `{mode}`: holdout `{confirmed}/{confirmed + missed}` confirmed (`{_pct(_rate(confirmed, confirmed + missed))}`)")

    lines += [
        "",
        "## Top Candidate-Expression Clusters",
        "",
        "| cluster | lane | holdout | pos/100 ASD | support/100 ASD | pressure | permission |",
        "|---|---:|---:|---:|---:|---:|---|",
    ]
    for row in top_clean:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{row.get('cluster_key')}`",
                    f"`{row.get('prototype_lane')}`",
                    _pct(row.get("holdout_confirmation_rate")),
                    _fmt(row.get("positive_conversions_per_100_state_days")),
                    _fmt(row.get("supported_events_per_100_state_days")),
                    str(row.get("restraint_pressure")),
                    str(row.get("shadow_permission")),
                ]
            )
            + " |"
        )

    paired = sum(1 for row in support_rows if str(row.get("support_effect_class") or "") == "paired_support_context")
    lines += [
        "",
        "## Support / Restraint Read",
        f"- support_gate_rows: `{len(support_rows)}`",
        f"- paired_support_context_rows: `{paired}`",
        f"- restraint_audit_rows: `{len(restraint_rows)}`",
        "- Support context should be treated as a confidence modifier only after a candidate lane already exists.",
        "- High negative-control or concentration pressure should become future penalty/veto/retest material before any promotion discussion.",
        "",
        "## Interpretation",
        "- Stage 4C gives us a clean vocabulary for future translator design, not a scoring rewrite.",
        "- The most useful immediate output is lane separation: candidate expression, lineage deduplication, support context, decay watch, restraint, and low-denominator watchlist are now separated instead of blended.",
        "- The next safe engineering step after reviewing Stage 4C is a fixture-backed prototype evaluation harness, still read-only, that checks candidate-expression modes before any live scoring rewrite.",
        "",
        "## Output Files",
        "",
    ]
    for label, path in paths.items():
        lines.append(f"- {label}: `{safe_rel(path)}`")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    args = _parse_args()
    runs2_dir = _resolve_path(args.runs2_dir)
    output_dir = _resolve_path(args.output_dir)
    stage_paths = _stage_paths(runs2_dir)
    paths = _cycle_paths(output_dir)

    queue_rows = _read_csv_rows(stage_paths["stage4b_queue_csv"])
    cluster_rows = _read_csv_rows(stage_paths["stage4b_cluster_csv"])
    holdout_matrix_rows = _read_csv_rows(stage_paths["stage4b_holdout_csv"])
    negative_rows = _read_csv_rows(stage_paths["stage4_negative_csv"])
    if not queue_rows or not cluster_rows or not holdout_matrix_rows:
        raise SystemExit("Stage 4B outputs are missing or empty. Run stage4b-replay-readback first.")

    rule_rows = _build_rule_registry(queue_rows, cluster_rows, negative_rows)
    lane_rows = _build_lane_matrix(rule_rows)
    holdout_scorecard_rows = _build_holdout_scorecard(rule_rows, holdout_matrix_rows)
    support_rows = _build_support_gate_effects(rule_rows)
    restraint_rows = _build_restraint_audit(rule_rows, negative_rows)
    casebook_rows = _build_casebook_rows(rule_rows, limit=int(args.casebook_limit))

    _write_csv(paths["rule_registry_csv"], rule_rows, force=bool(args.force))
    _write_csv(paths["lane_matrix_csv"], lane_rows, force=bool(args.force))
    _write_csv(paths["holdout_scorecard_csv"], holdout_scorecard_rows, force=bool(args.force))
    _write_csv(paths["support_effects_csv"], support_rows, force=bool(args.force))
    _write_csv(paths["restraint_audit_csv"], restraint_rows, force=bool(args.force))
    _write_csv(paths["casebook_csv"], casebook_rows, force=bool(args.force))
    _write_casebook_md(paths["casebook_md"], casebook_rows, force=bool(args.force))

    payload = {
        "metadata": {
            "runs2_dir": safe_rel(runs2_dir),
            "prototype_rule_rows": len(rule_rows),
            "lane_matrix_rows": len(lane_rows),
            "holdout_scorecard_rows": len(holdout_scorecard_rows),
            "support_gate_effect_rows": len(support_rows),
            "restraint_audit_rows": len(restraint_rows),
            "casebook_rows": len(casebook_rows),
            "guardrail": "read_only_stage4c_shadow_translator_no_live_scoring_or_candidate_generation_changes",
        },
        "prototype_lane_counts": dict(Counter(str(row.get("prototype_lane") or "") for row in rule_rows)),
        "shadow_permission_counts": dict(Counter(str(row.get("shadow_permission") or "") for row in rule_rows)),
        "restraint_pressure_counts": dict(Counter(str(row.get("restraint_pressure") or "") for row in rule_rows)),
        "lane_matrix": lane_rows,
        "top_candidate_expression_clusters": [
            row
            for row in rule_rows
            if str(row.get("prototype_lane") or "") in {"clean_boxed_candidate", "lineage_guarded_boxed_candidate"}
        ][:50],
        "outputs": {label: safe_rel(path) for label, path in paths.items()},
    }
    _write_json(paths["json"], payload, force=bool(args.force))
    _write_text(
        paths["md"],
        _build_markdown(
            runs2_dir=runs2_dir,
            paths=paths,
            rule_rows=rule_rows,
            lane_rows=lane_rows,
            support_rows=support_rows,
            restraint_rows=restraint_rows,
            holdout_rows=holdout_scorecard_rows,
            casebook_rows=casebook_rows,
        ),
        force=bool(args.force),
    )

    print(f"[OK] Wrote Stage-4C shadow translator prototype: {safe_rel(paths['md'])}")
    print(f"[OK] Wrote prototype rules: {len(rule_rows)}")
    print(f"[OK] Wrote lane rows: {len(lane_rows)}")
    print(f"[OK] Wrote holdout scorecard rows: {len(holdout_scorecard_rows)}")


if __name__ == "__main__":
    main()
