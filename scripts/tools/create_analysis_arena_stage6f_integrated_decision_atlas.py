#!/usr/bin/env python3
"""Create the Stage-6F integrated decision atlas.

Stage 6F is read-only. It combines Stage 6B readback, Stage 6C confirmation
contracts, Stage 6D restraint calibration, Stage 6E support narrowing, and the
Stage 5 value-level ledger into one decision atlas and priority casebook. It
does not alter live scoring, candidate generation, translator logic, budget
logic, or legacy infrastructure.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Sequence


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.tools.analysis_arena_window_utils import safe_rel  # type: ignore
from scripts.tools.create_analysis_arena_stage4_fixture_replay_harness import (  # type: ignore
    RUNS_2_DIR,
    _fmt,
    _pct,
    _read_csv_rows,
    _resolve_path,
    _safe_float,
    _safe_int,
    _write_csv,
    _write_json,
    _write_text,
)


STAGE5_PREFIX = "ANALYSIS_ARENA__CYCLE__STAGE5"
STAGE6B_READBACK_PREFIX = "ANALYSIS_ARENA__CYCLE__STAGE6B_READBACK"
STAGE6C_PREFIX = "ANALYSIS_ARENA__CYCLE__STAGE6C"
STAGE6D_PREFIX = "ANALYSIS_ARENA__CYCLE__STAGE6D"
STAGE6E_PREFIX = "ANALYSIS_ARENA__CYCLE__STAGE6E"
STAGE6F_PREFIX = "ANALYSIS_ARENA__CYCLE__STAGE6F"


def _parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--runs2-dir", default=str(RUNS_2_DIR), help="RUNS_2 root containing Stage-6B through Stage-6E outputs.")
    ap.add_argument("--output-dir", default=str(RUNS_2_DIR), help="Cycle-level output directory.")
    ap.add_argument("--casebook-limit-per-bucket", type=int, default=8)
    ap.add_argument("--max-ledger-rows", type=int, default=0, help="Optional debugging limit. Default 0 means all ledger rows.")
    ap.add_argument("--force", action="store_true", help="Overwrite existing Stage-6F outputs.")
    return ap.parse_args()


def _input_paths(runs2_dir: Path) -> Dict[str, Path]:
    return {
        "stage5_value_ledger": runs2_dir / f"{STAGE5_PREFIX}_VALUE_LEVEL_REPLAY_LEDGER.csv",
        "scenario_decisions": runs2_dir / f"{STAGE6B_READBACK_PREFIX}_SCENARIO_DECISIONS.csv",
        "requirement_results": runs2_dir / f"{STAGE6B_READBACK_PREFIX}_REQUIREMENT_RESULTS.csv",
        "readback_next_actions": runs2_dir / f"{STAGE6B_READBACK_PREFIX}_NEXT_ACTION_QUEUE.csv",
        "macro_candidates": runs2_dir / f"{STAGE6B_READBACK_PREFIX}_MACRO_FINDINGS_CANDIDATES.csv",
        "confirmation_tests": runs2_dir / f"{STAGE6C_PREFIX}_CONFIRMATION_TEST_MATRIX.csv",
        "rewrite_blockers": runs2_dir / f"{STAGE6C_PREFIX}_REWRITE_BLOCKERS.csv",
        "fresh_window_queue": runs2_dir / f"{STAGE6C_PREFIX}_FRESH_WINDOW_QUEUE.csv",
        "macro_gate": runs2_dir / f"{STAGE6C_PREFIX}_MACRO_REVIEW_GATE.csv",
        "restraint_rescue": runs2_dir / f"{STAGE6D_PREFIX}_HIGH_PRESSURE_RESCUE_CANDIDATES.csv",
        "restraint_policy": runs2_dir / f"{STAGE6D_PREFIX}_SOFT_PENALTY_POLICY_MATRIX.csv",
        "restraint_next_actions": runs2_dir / f"{STAGE6D_PREFIX}_RESTRAINT_NEXT_ACTIONS.csv",
        "support_candidates": runs2_dir / f"{STAGE6E_PREFIX}_SUPPORT_NARROWING_CANDIDATES.csv",
        "support_failures": runs2_dir / f"{STAGE6E_PREFIX}_SUPPORT_FAILURE_MODES.csv",
        "support_next_actions": runs2_dir / f"{STAGE6E_PREFIX}_SUPPORT_NEXT_ACTIONS.csv",
    }


def _output_paths(output_dir: Path) -> Dict[str, Path]:
    return {
        "md": output_dir / f"{STAGE6F_PREFIX}_INTEGRATED_DECISION_ATLAS.md",
        "json": output_dir / f"{STAGE6F_PREFIX}_INTEGRATED_DECISION_ATLAS.json",
        "lane_atlas_csv": output_dir / f"{STAGE6F_PREFIX}_LANE_DECISION_ATLAS.csv",
        "blockers_csv": output_dir / f"{STAGE6F_PREFIX}_ACTIVE_BLOCKERS_AND_CLEARANCE.csv",
        "fresh_queue_csv": output_dir / f"{STAGE6F_PREFIX}_FRESH_WINDOW_CARRY_FORWARD_QUEUE.csv",
        "macro_disposition_csv": output_dir / f"{STAGE6F_PREFIX}_MACRO_FINDINGS_DISPOSITION.csv",
        "casebook_md": output_dir / f"{STAGE6F_PREFIX}_PRIORITY_BUCKET_CASEBOOK.md",
        "casebook_csv": output_dir / f"{STAGE6F_PREFIX}_PRIORITY_BUCKET_CASEBOOK.csv",
        "example_ledger_csv": output_dir / f"{STAGE6F_PREFIX}_BUCKET_EXAMPLE_LEDGER.csv",
    }


def _load_required_csv(path: Path, label: str) -> List[Dict[str, str]]:
    rows = _read_csv_rows(path)
    if not rows:
        raise SystemExit(f"Missing or empty Stage-6F input {label}: {safe_rel(path)}")
    return rows


def _load_optional_csv(path: Path) -> List[Dict[str, str]]:
    return _read_csv_rows(path)


def _row_by_id(rows: Sequence[Mapping[str, Any]], field: str) -> Dict[str, Mapping[str, Any]]:
    return {str(row.get(field) or ""): row for row in rows}


def _first(rows: Sequence[Mapping[str, Any]], field: str, value: str) -> Mapping[str, Any]:
    for row in rows:
        if str(row.get(field) or "") == value:
            return row
    return {}


def _metric_summary(row: Mapping[str, Any]) -> str:
    if not row:
        return "missing"
    parts = []
    if "false_positive_proxy_rate" in row:
        parts.append(f"fp={_pct(row.get('false_positive_proxy_rate'))}")
    if "pool_normalized_positive_yield" in row:
        parts.append(f"yield={_fmt(row.get('pool_normalized_positive_yield'))}")
    if "positive_conversion_event_count" in row:
        parts.append(f"positive={_safe_int(row.get('positive_conversion_event_count'))}")
    if "active_state_days" in row:
        parts.append(f"state_days={_safe_int(row.get('active_state_days'))}")
    if "avg_pool_or_exposure_per_state_day" in row:
        parts.append(f"avg_pool={_fmt(row.get('avg_pool_or_exposure_per_state_day'))}")
    return "; ".join(parts) if parts else "no numeric metrics"


def _test_for_target(tests: Sequence[Mapping[str, Any]], target: str) -> Mapping[str, Any]:
    return _first(tests, "confirmation_target", target)


def _lane_rows(
    *,
    scenarios: Sequence[Mapping[str, Any]],
    requirements: Sequence[Mapping[str, Any]],
    tests: Sequence[Mapping[str, Any]],
    blockers: Sequence[Mapping[str, Any]],
    restraint_rescue: Sequence[Mapping[str, Any]],
    support_candidates: Sequence[Mapping[str, Any]],
    support_failures: Sequence[Mapping[str, Any]],
) -> List[Dict[str, Any]]:
    by_scenario = _row_by_id(scenarios, "scenario_id")
    by_req = _row_by_id(requirements, "requirement_id")

    def blocker_text(linked_test: str) -> str:
        linked = [row for row in blockers if str(row.get("linked_test_id") or "") == linked_test]
        if not linked:
            return ""
        return "|".join(str(row.get("blocker_id") or "") for row in linked)

    def add_from_scenario(
        rows: List[Dict[str, Any]],
        *,
        lane_id: str,
        lane_type: str,
        scenario_id: str,
        linked_test: str,
        decision_posture: str,
        clearance_target: str,
    ) -> None:
        scenario = by_scenario.get(scenario_id, {})
        test = _first(tests, "test_id", linked_test)
        rows.append(
            {
                "lane_id": lane_id,
                "lane_type": lane_type,
                "source_stage": "Stage6B/Stage6C",
                "source_subject": scenario_id,
                "current_decision": scenario.get("readback_decision", ""),
                "current_status": scenario.get("status", ""),
                "decision_posture": decision_posture,
                "evidence_summary": _metric_summary(scenario),
                "primary_blockers": blocker_text(linked_test),
                "fresh_window_requirement": test.get("fresh_window_test", ""),
                "clearance_target": clearance_target,
                "allowed_permission": scenario.get("allowed_permission", "none"),
                "live_permission": "none",
                "next_action": scenario.get("next_action", ""),
            }
        )

    rows: List[Dict[str, Any]] = []
    add_from_scenario(
        rows,
        lane_id="S6F-LANE-001",
        lane_type="primary_candidate_expression",
        scenario_id="primary_restrained_candidate_expression",
        linked_test="S6C-001",
        decision_posture="strongest_current_seed_but_future_confirmation_required",
        clearance_target="repeat Stage 6B/6C on fresh window with FP/yield/pool thresholds met",
    )
    add_from_scenario(
        rows,
        lane_id="S6F-LANE-002",
        lane_type="secondary_lineage_modifier",
        scenario_id="secondary_lineage_supported_restrained",
        linked_test="S6C-007",
        decision_posture="modifier_only_not_independent_expansion",
        clearance_target="prove non-duplicate lift versus primary before any expansion role",
    )
    add_from_scenario(
        rows,
        lane_id="S6F-LANE-003",
        lane_type="broad_lineage_reference",
        scenario_id="broad_lineage_foundation_reference",
        linked_test="S6C-005",
        decision_posture="blocked_until_narrowed",
        clearance_target="narrowed lineage variant must preserve FP/yield and add non-duplicate conversions",
    )

    support_req = by_req.get("S6B-003", {})
    support_test = _test_for_target(tests, "support_context_modifier")
    strict_support = [row for row in support_candidates if str(row.get("recommended_use") or "") == "narrow_support_modifier_candidate"]
    mixed_support = [row for row in support_candidates if str(row.get("recommended_use") or "") != "narrow_support_modifier_candidate"]
    rows.append(
        {
            "lane_id": "S6F-LANE-004",
            "lane_type": "support_modifier_narrowing",
            "source_stage": "Stage6E",
            "source_subject": "support_narrowing_candidates",
            "current_decision": "broad_support_failed_narrow_support_research_allowed",
            "current_status": str(support_req.get("readback_result") or ""),
            "decision_posture": f"{len(strict_support)} strict support candidates; {len(mixed_support)} mixed retest candidates; broad support remains blocked",
            "evidence_summary": f"candidate_rows={len(support_candidates)}; failure_rows={len(support_failures)}",
            "primary_blockers": blocker_text("S6C-003"),
            "fresh_window_requirement": support_test.get("fresh_window_test", ""),
            "clearance_target": "support-on must beat a meaningful support-off peer and repeat on future/fresh windows",
            "allowed_permission": "support_research_only",
            "live_permission": "none",
            "next_action": "Use Stage 6E candidates as casebook/replay targets only.",
        }
    )

    restraint_req = by_req.get("S6B-004", {})
    restraint_test = _test_for_target(tests, "restraint_soft_penalty")
    strict_rescues = [row for row in restraint_rescue if str(row.get("recommended_use") or "") == "high_pressure_rescue_candidate_soft_penalty_only"]
    downweight = [row for row in restraint_rescue if str(row.get("recommended_use") or "") != "high_pressure_rescue_candidate_soft_penalty_only"]
    rows.append(
        {
            "lane_id": "S6F-LANE-005",
            "lane_type": "restraint_soft_penalty",
            "source_stage": "Stage6D",
            "source_subject": "high_pressure_rescue_candidates",
            "current_decision": "hard_exclusion_promising_but_soft_before_hard_required",
            "current_status": str(restraint_req.get("readback_result") or ""),
            "decision_posture": f"{len(strict_rescues)} rescue buckets; {len(downweight)} downweight buckets; hard veto remains blocked",
            "evidence_summary": f"top_rescue={_metric_summary(strict_rescues[0]) if strict_rescues else 'none'}",
            "primary_blockers": blocker_text("S6C-004"),
            "fresh_window_requirement": restraint_test.get("fresh_window_test", ""),
            "clearance_target": "soft penalty must preserve conversions while reducing FP pressure; hard veto forbidden until repeated",
            "allowed_permission": "penalty_research_only",
            "live_permission": "none",
            "next_action": "Use Stage 6D policy matrix and rescue buckets as soft-penalty research inputs.",
        }
    )

    add_from_scenario(
        rows,
        lane_id="S6F-LANE-006",
        lane_type="decay_companion_boundary",
        scenario_id="decay_watch_companion_excluded",
        linked_test="S6C-006",
        decision_posture="companion_only_boundary_confirmed_for_now",
        clearance_target="decay stays separate from candidate-pool scoring on every future replay",
    )
    rows.append(
        {
            "lane_id": "S6F-LANE-007",
            "lane_type": "duplicate_credit_guardrail",
            "source_stage": "Stage6B/Stage6C",
            "source_subject": "stage6a_allowed_candidate_union",
            "current_decision": by_scenario.get("stage6a_allowed_candidate_union", {}).get("readback_decision", ""),
            "current_status": by_req.get("S6B-005", {}).get("readback_result", ""),
            "decision_posture": "mandatory_guardrail",
            "evidence_summary": str(by_req.get("S6B-005", {}).get("evidence") or ""),
            "primary_blockers": blocker_text("S6C-007"),
            "fresh_window_requirement": _test_for_target(tests, "duplicate_credit_guardrail").get("fresh_window_test", ""),
            "clearance_target": "union replay must not double-count shared lineage on every future window",
            "allowed_permission": "readback_reference_only",
            "live_permission": "none",
            "next_action": "Reject any future simulator that blends or double-credits primary/secondary rows.",
        }
    )
    rows.append(
        {
            "lane_id": "S6F-LANE-008",
            "lane_type": "rewrite_gate",
            "source_stage": "Stage6C",
            "source_subject": "translator_scoring_rewrite",
            "current_decision": "blocked_until_future_confirmation",
            "current_status": "active_blocker",
            "decision_posture": "rewrite_not_allowed_yet",
            "evidence_summary": f"active_blockers={len(blockers)}",
            "primary_blockers": "|".join(str(row.get("blocker_id") or "") for row in blockers),
            "fresh_window_requirement": _test_for_target(tests, "translator_scoring_rewrite_gate").get("fresh_window_test", ""),
            "clearance_target": "Stage 6C primary repeat plus support/restraint/decay/duplicate-credit guardrails resolved or quarantined",
            "allowed_permission": "blocked_until_future_confirmation",
            "live_permission": "none",
            "next_action": "Do not start live translator/scoring rewrite from March evidence alone.",
        }
    )
    return rows


def _blocker_rows(blockers: Sequence[Mapping[str, Any]], tests: Sequence[Mapping[str, Any]]) -> List[Dict[str, Any]]:
    tests_by_id = _row_by_id(tests, "test_id")
    rows: List[Dict[str, Any]] = []
    for row in blockers:
        test = tests_by_id.get(str(row.get("linked_test_id") or ""), {})
        rows.append(
            {
                "blocker_id": row.get("blocker_id", ""),
                "linked_test_id": row.get("linked_test_id", ""),
                "status": row.get("status", ""),
                "blocks": test.get("confirmation_target", ""),
                "rationale": row.get("rationale", ""),
                "clearance_condition": row.get("clearance_condition", ""),
                "current_evidence": row.get("current_evidence", ""),
                "fresh_window_test": test.get("fresh_window_test", ""),
                "live_permission": "none",
            }
        )
    return rows


def _fresh_queue_rows(
    *,
    stage6c_queue: Sequence[Mapping[str, Any]],
    restraint_actions: Sequence[Mapping[str, Any]],
    support_actions: Sequence[Mapping[str, Any]],
    lane_rows: Sequence[Mapping[str, Any]],
) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    priority = 1
    lanes_by_type = _row_by_id(lane_rows, "lane_type")

    def add(source_stage: str, subject: str, action: str, acceptance: str, permission: str) -> None:
        nonlocal priority
        rows.append(
            {
                "priority": priority,
                "source_stage": source_stage,
                "subject": subject,
                "carry_forward_action": action,
                "acceptance_or_review_test": acceptance,
                "allowed_permission": permission,
                "live_permission": "none",
            }
        )
        priority += 1

    for row in stage6c_queue:
        add(
            "Stage6C",
            str(row.get("subject") or ""),
            str(row.get("fresh_window_instruction") or ""),
            str(row.get("acceptance_test") or ""),
            str(row.get("allowed_permission") or ""),
        )
    for row in restraint_actions:
        add(
            "Stage6D",
            str(row.get("subject") or ""),
            str(row.get("action") or ""),
            lanes_by_type.get("restraint_soft_penalty", {}).get("clearance_target", ""),
            str(row.get("allowed_permission") or ""),
        )
    for row in support_actions:
        add(
            "Stage6E",
            str(row.get("subject") or ""),
            str(row.get("action") or ""),
            lanes_by_type.get("support_modifier_narrowing", {}).get("clearance_target", ""),
            str(row.get("allowed_permission") or ""),
        )
    return rows


def _macro_disposition_rows(
    *,
    macro_candidates: Sequence[Mapping[str, Any]],
    macro_gate: Sequence[Mapping[str, Any]],
    lane_rows: Sequence[Mapping[str, Any]],
) -> List[Dict[str, Any]]:
    gate_by_id = _row_by_id(macro_gate, "finding_id")
    rows: List[Dict[str, Any]] = []
    for row in macro_candidates:
        gate = gate_by_id.get(str(row.get("finding_id") or ""), {})
        rows.append(
            {
                "finding_id": row.get("finding_id", ""),
                "finding": row.get("finding", ""),
                "current_posture": row.get("posture", ""),
                "stage6f_disposition": gate.get("stage6c_disposition", "hold_for_fresh_confirmation"),
                "promotion_condition": gate.get("promotion_condition", "future/fresh repeat or explicit provisional review"),
                "blocked_from_live_use": "true",
                "recommended_log_action": row.get("recommended_log_action", ""),
                "why_not_confirmed": row.get("why_not_confirmed", ""),
                "related_lane_count": sum(1 for lane in lane_rows if str(row.get("finding", "")).split(" ", 1)[0].lower() in str(lane).lower()),
            }
        )
    return rows


def _target_rows(
    *,
    restraint_rescue: Sequence[Mapping[str, Any]],
    support_candidates: Sequence[Mapping[str, Any]],
) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    priority = 1
    for row in restraint_rescue[:12]:
        rows.append(
            {
                "target_id": f"S6F-TARGET-{priority:03d}",
                "source_stage": "Stage6D",
                "source_candidate_id": row.get("candidate_id", ""),
                "bucket_id": row.get("bucket_id", ""),
                "bucket_type": row.get("bucket_type", ""),
                "mechanism_family": row.get("mechanism_family", ""),
                "prototype_lane": row.get("prototype_lane", ""),
                "restraint_pressure": "high",
                "support_context": row.get("support_context", ""),
                "cluster_key": row.get("cluster_key", ""),
                "recommended_use": row.get("recommended_use", ""),
                "priority_reason": f"positive={_safe_int(row.get('positive_conversion_event_count'))}; fp={_pct(row.get('false_positive_proxy_rate'))}; yield={_fmt(row.get('pool_normalized_positive_yield'))}",
                "live_permission": "none",
            }
        )
        priority += 1
    for row in support_candidates[:12]:
        rows.append(
            {
                "target_id": f"S6F-TARGET-{priority:03d}",
                "source_stage": "Stage6E",
                "source_candidate_id": row.get("candidate_id", ""),
                "bucket_id": row.get("bucket_id", ""),
                "bucket_type": row.get("bucket_type", ""),
                "mechanism_family": row.get("mechanism_family", ""),
                "prototype_lane": row.get("prototype_lane", ""),
                "restraint_pressure": row.get("restraint_pressure", ""),
                "support_context": "support_on",
                "cluster_key": row.get("cluster_key", ""),
                "recommended_use": row.get("recommended_use", ""),
                "priority_reason": f"positive={_safe_int(row.get('positive_conversion_event_count'))}; fp_delta_peer={_fmt(row.get('false_positive_delta_vs_peer'))}; yield_delta_peer={_fmt(row.get('yield_delta_vs_peer'))}",
                "live_permission": "none",
            }
        )
        priority += 1
    return rows


def _matches_target(row: Mapping[str, Any], target: Mapping[str, Any]) -> bool:
    if str(row.get("prototype_lane") or "") not in {"clean_boxed_candidate", "lineage_guarded_boxed_candidate"}:
        return False
    source_stage = str(target.get("source_stage") or "")
    cluster = str(target.get("cluster_key") or "")
    if cluster and str(row.get("cluster_key") or "") != cluster:
        return False
    if source_stage == "Stage6D" and str(row.get("restraint_pressure") or "").lower() != "high":
        return False
    if source_stage == "Stage6E" and str(row.get("support_context_present") or "").lower() != "true":
        return False
    for target_field, row_field in (
        ("mechanism_family", "mechanism_family"),
        ("prototype_lane", "prototype_lane"),
    ):
        value = str(target.get(target_field) or "")
        if value and str(row.get(row_field) or "") != value:
            return False
    pressure = str(target.get("restraint_pressure") or "")
    if source_stage == "Stage6E" and pressure and str(row.get("restraint_pressure") or "").lower() != pressure.lower():
        return False
    return True


def _casebook_rows(
    *,
    ledger_rows: Sequence[Mapping[str, Any]],
    target_rows: Sequence[Mapping[str, Any]],
    limit_per_bucket: int,
) -> tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    casebook: List[Dict[str, Any]] = []
    examples: List[Dict[str, Any]] = []
    for target in target_rows:
        matches = [row for row in ledger_rows if _matches_target(row, target)]
        matches = sorted(
            matches,
            key=lambda row: (
                -_safe_int(row.get("positive_conversion_event_count")),
                -_safe_int(row.get("matched_value_count")),
                _safe_int(row.get("false_positive_proxy_value_count")),
                str(row.get("window") or ""),
                str(row.get("date") or ""),
                str(row.get("state_key") or ""),
            ),
        )
        positive_rows = sum(1 for row in matches if _safe_int(row.get("positive_conversion_event_count")) > 0)
        total_positive = sum(_safe_int(row.get("positive_conversion_event_count")) for row in matches)
        total_overlap = sum(_safe_int(row.get("overlap_value_count")) for row in matches)
        total_fp = sum(_safe_int(row.get("false_positive_proxy_value_count")) for row in matches)
        casebook.append(
            {
                **dict(target),
                "matched_ledger_rows": len(matches),
                "positive_ledger_rows": positive_rows,
                "total_positive_conversion_event_count": total_positive,
                "total_overlap_value_count": total_overlap,
                "false_positive_proxy_value_count": total_fp,
                "casebook_fp_proxy_rate": _safe_float(total_fp) / _safe_float(total_overlap) if total_overlap else 0.0,
                "casebook_positive_yield": 100.0 * _safe_float(total_positive) / _safe_float(total_overlap) if total_overlap else 0.0,
                "casebook_interpretation": _casebook_interpretation(target=target, matches=matches, total_positive=total_positive, total_overlap=total_overlap),
            }
        )
        for idx, row in enumerate(matches[: max(1, int(limit_per_bucket))], start=1):
            examples.append(
                {
                    "target_id": target.get("target_id", ""),
                    "example_rank": idx,
                    "source_stage": target.get("source_stage", ""),
                    "source_candidate_id": target.get("source_candidate_id", ""),
                    "bucket_id": target.get("bucket_id", ""),
                    "window": row.get("window", ""),
                    "date": row.get("date", ""),
                    "state_key": row.get("state_key", ""),
                    "pair_scope": row.get("pair_scope", ""),
                    "source_a": row.get("source_a", ""),
                    "source_b": row.get("source_b", ""),
                    "cluster_key": row.get("cluster_key", ""),
                    "mechanism_family": row.get("mechanism_family", ""),
                    "future_primitive": row.get("future_primitive", ""),
                    "prototype_lane": row.get("prototype_lane", ""),
                    "restraint_pressure": row.get("restraint_pressure", ""),
                    "support_context_present": row.get("support_context_present", ""),
                    "overlap_value_count": _safe_int(row.get("overlap_value_count")),
                    "matched_value_count": _safe_int(row.get("matched_value_count")),
                    "false_positive_proxy_value_count": _safe_int(row.get("false_positive_proxy_value_count")),
                    "positive_conversion_event_count": _safe_int(row.get("positive_conversion_event_count")),
                    "matched_event_ids": row.get("matched_event_ids", ""),
                    "matched_values_sample": row.get("matched_values_sample", ""),
                    "overlap_values_sample": row.get("overlap_values_sample", ""),
                    "included_in_modes": row.get("included_in_modes", ""),
                    "live_permission": "none",
                }
            )
    return casebook, examples


def _casebook_interpretation(*, target: Mapping[str, Any], matches: Sequence[Mapping[str, Any]], total_positive: int, total_overlap: int) -> str:
    if not matches:
        return "no_matching_value_level_rows_found"
    yield_rate = 100.0 * _safe_float(total_positive) / _safe_float(total_overlap) if total_overlap else 0.0
    if str(target.get("recommended_use") or "") == "high_pressure_rescue_candidate_soft_penalty_only":
        return "priority_restraint_rescue_casebook; inspect before globally downweighting high pressure"
    if str(target.get("recommended_use") or "") == "narrow_support_modifier_candidate":
        return "priority_support_narrowing_casebook; requires fresh-window repeat"
    if yield_rate > 15:
        return "strong_research_casebook_high_yield_but_not_live_permission"
    return "research_casebook_review_only"


def _table(headers: Sequence[str], rows: Sequence[Sequence[Any]]) -> List[str]:
    def cell(value: Any) -> str:
        return str(value).replace("|", "\\|")

    lines = [
        "| " + " | ".join(cell(header) for header in headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(cell(value) for value in row) + " |")
    return lines


def _render_md(
    *,
    lane_rows: Sequence[Mapping[str, Any]],
    blocker_rows: Sequence[Mapping[str, Any]],
    queue_rows: Sequence[Mapping[str, Any]],
    macro_rows: Sequence[Mapping[str, Any]],
    casebook_rows: Sequence[Mapping[str, Any]],
    output_paths: Mapping[str, Path],
) -> str:
    by_type = {str(row.get("lane_type") or ""): row for row in lane_rows}
    support_posture = str(by_type.get("support_modifier_narrowing", {}).get("decision_posture") or "support candidate posture unavailable")
    restraint_posture = str(by_type.get("restraint_soft_penalty", {}).get("decision_posture") or "restraint rescue posture unavailable")
    lines: List[str] = [
        "# Analysis Arena Stage 6F Integrated Decision Atlas",
        "",
        "## Guardrail",
        "",
        "Stage 6F is read-only. It integrates Stage 6B through Stage 6E evidence into decision, blocker, queue, macro, and casebook artifacts. It does not change live scoring, candidate generation, translator logic, budget logic, or legacy infrastructure.",
        "",
        "## Executive Readback",
        "",
        "- Primary restrained candidate expression remains the strongest current design seed, but Stage 6C future/fresh confirmation is still required.",
        f"- Restraint evidence posture: {restraint_posture}; restraint remains soft-penalty research, not hard-veto permission.",
        f"- Support evidence posture: {support_posture}; support remains research/modifier-only until repeated.",
        "- Rewrite remains blocked until fresh-window confirmation clears or quarantines the open gates.",
        "",
        "## Lane Decision Atlas",
        "",
    ]
    lines.extend(
        _table(
            ["lane_id", "lane_type", "current_status", "decision_posture", "permission"],
            [
                [
                    row.get("lane_id", ""),
                    row.get("lane_type", ""),
                    row.get("current_status", ""),
                    row.get("decision_posture", ""),
                    row.get("allowed_permission", ""),
                ]
                for row in lane_rows
            ],
        )
    )
    lines.extend(["", "## Active Blockers", ""])
    lines.extend(
        _table(
            ["blocker_id", "blocks", "clearance_condition"],
            [[row.get("blocker_id", ""), row.get("blocks", ""), row.get("clearance_condition", "")] for row in blocker_rows],
        )
    )
    lines.extend(["", "## Priority Casebook Targets", ""])
    lines.extend(
        _table(
            ["target_id", "source_stage", "candidate", "positive", "yield", "interpretation"],
            [
                [
                    row.get("target_id", ""),
                    row.get("source_stage", ""),
                    row.get("source_candidate_id", ""),
                    row.get("total_positive_conversion_event_count", ""),
                    _fmt(row.get("casebook_positive_yield")),
                    row.get("casebook_interpretation", ""),
                ]
                for row in casebook_rows[:15]
            ],
        )
    )
    lines.extend(["", "## Macro Findings Disposition", ""])
    lines.extend(
        _table(
            ["finding_id", "disposition", "promotion_condition"],
            [[row.get("finding_id", ""), row.get("stage6f_disposition", ""), row.get("promotion_condition", "")] for row in macro_rows],
        )
    )
    lines.extend(
        [
            "",
            "## Outputs",
            "",
            f"- atlas_json: `{safe_rel(output_paths['json'])}`",
            f"- lane_decision_atlas: `{safe_rel(output_paths['lane_atlas_csv'])}`",
            f"- active_blockers: `{safe_rel(output_paths['blockers_csv'])}`",
            f"- fresh_window_queue: `{safe_rel(output_paths['fresh_queue_csv'])}`",
            f"- macro_findings_disposition: `{safe_rel(output_paths['macro_disposition_csv'])}`",
            f"- priority_bucket_casebook_md: `{safe_rel(output_paths['casebook_md'])}`",
            f"- priority_bucket_casebook_csv: `{safe_rel(output_paths['casebook_csv'])}`",
            f"- bucket_example_ledger: `{safe_rel(output_paths['example_ledger_csv'])}`",
            "",
        ]
    )
    return "\n".join(lines)


def _render_casebook_md(casebook_rows: Sequence[Mapping[str, Any]], example_rows: Sequence[Mapping[str, Any]], output_paths: Mapping[str, Path]) -> str:
    lines: List[str] = [
        "# Analysis Arena Stage 6F Priority Bucket Casebook",
        "",
        "## Guardrail",
        "",
        "This casebook is evidence review only. It does not create live scoring, candidate-generation, translator, hard-veto, support-promotion, or budget permission.",
        "",
        "## Target Summary",
        "",
    ]
    lines.extend(
        _table(
            ["target_id", "source_stage", "candidate", "rows", "positive", "fp", "yield", "interpretation"],
            [
                [
                    row.get("target_id", ""),
                    row.get("source_stage", ""),
                    row.get("source_candidate_id", ""),
                    row.get("matched_ledger_rows", ""),
                    row.get("total_positive_conversion_event_count", ""),
                    _pct(row.get("casebook_fp_proxy_rate")),
                    _fmt(row.get("casebook_positive_yield")),
                    row.get("casebook_interpretation", ""),
                ]
                for row in casebook_rows
            ],
        )
    )
    lines.extend(["", "## Example Rows", ""])
    lines.extend(
        _table(
            ["target_id", "rank", "window", "date", "state", "positive", "matched_values", "sources"],
            [
                [
                    row.get("target_id", ""),
                    row.get("example_rank", ""),
                    row.get("window", ""),
                    row.get("date", ""),
                    row.get("state_key", ""),
                    row.get("positive_conversion_event_count", ""),
                    row.get("matched_values_sample", ""),
                    f"{row.get('source_a', '')} + {row.get('source_b', '')}",
                ]
                for row in example_rows[:80]
            ],
        )
    )
    lines.extend(
        [
            "",
            "## Files",
            "",
            f"- casebook_csv: `{safe_rel(output_paths['casebook_csv'])}`",
            f"- example_ledger_csv: `{safe_rel(output_paths['example_ledger_csv'])}`",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    args = _parse_args()
    runs2_dir = _resolve_path(args.runs2_dir)
    output_dir = _resolve_path(args.output_dir)
    inputs = _input_paths(runs2_dir)
    outputs = _output_paths(output_dir)

    ledger_rows = _load_required_csv(inputs["stage5_value_ledger"], "Stage 5 value-level ledger")
    if int(args.max_ledger_rows) > 0:
        ledger_rows = ledger_rows[: int(args.max_ledger_rows)]
    scenario_decisions = _load_required_csv(inputs["scenario_decisions"], "Stage 6B scenario decisions")
    requirement_results = _load_required_csv(inputs["requirement_results"], "Stage 6B requirement results")
    readback_next_actions = _load_required_csv(inputs["readback_next_actions"], "Stage 6B next actions")
    macro_candidates = _load_required_csv(inputs["macro_candidates"], "Stage 6B macro candidates")
    confirmation_tests = _load_required_csv(inputs["confirmation_tests"], "Stage 6C confirmation tests")
    rewrite_blockers = _load_required_csv(inputs["rewrite_blockers"], "Stage 6C rewrite blockers")
    fresh_window_queue = _load_required_csv(inputs["fresh_window_queue"], "Stage 6C fresh window queue")
    macro_gate = _load_required_csv(inputs["macro_gate"], "Stage 6C macro gate")
    restraint_rescue = _load_optional_csv(inputs["restraint_rescue"])
    restraint_policy = _load_required_csv(inputs["restraint_policy"], "Stage 6D restraint policy")
    restraint_next_actions = _load_required_csv(inputs["restraint_next_actions"], "Stage 6D next actions")
    support_candidates = _load_optional_csv(inputs["support_candidates"])
    support_failures = _load_required_csv(inputs["support_failures"], "Stage 6E support failures")
    support_next_actions = _load_required_csv(inputs["support_next_actions"], "Stage 6E next actions")

    lane_rows = _lane_rows(
        scenarios=scenario_decisions,
        requirements=requirement_results,
        tests=confirmation_tests,
        blockers=rewrite_blockers,
        restraint_rescue=restraint_rescue,
        support_candidates=support_candidates,
        support_failures=support_failures,
    )
    blocker_rows = _blocker_rows(rewrite_blockers, confirmation_tests)
    queue_rows = _fresh_queue_rows(
        stage6c_queue=fresh_window_queue,
        restraint_actions=restraint_next_actions,
        support_actions=support_next_actions,
        lane_rows=lane_rows,
    )
    macro_rows = _macro_disposition_rows(
        macro_candidates=macro_candidates,
        macro_gate=macro_gate,
        lane_rows=lane_rows,
    )
    targets = _target_rows(restraint_rescue=restraint_rescue, support_candidates=support_candidates)
    casebook_rows, example_rows = _casebook_rows(
        ledger_rows=ledger_rows,
        target_rows=targets,
        limit_per_bucket=int(args.casebook_limit_per_bucket),
    )
    payload = {
        "stage": "6F",
        "guardrail": "read_only_integrated_decision_atlas_no_live_permission",
        "inputs": {key: safe_rel(path) for key, path in inputs.items()},
        "ledger_rows_loaded": len(ledger_rows),
        "lane_count": len(lane_rows),
        "active_blocker_count": len(blocker_rows),
        "fresh_queue_count": len(queue_rows),
        "macro_disposition_count": len(macro_rows),
        "casebook_target_count": len(casebook_rows),
        "casebook_example_count": len(example_rows),
        "restraint_policy_row_count": len(restraint_policy),
        "readback_next_action_count": len(readback_next_actions),
        "next_stage_dependency": "Use Stage 6F as the decision atlas for Stage 7A fresh-window confirmation scaffolding.",
    }

    _write_csv(outputs["lane_atlas_csv"], lane_rows, force=bool(args.force))
    _write_csv(outputs["blockers_csv"], blocker_rows, force=bool(args.force))
    _write_csv(outputs["fresh_queue_csv"], queue_rows, force=bool(args.force))
    _write_csv(outputs["macro_disposition_csv"], macro_rows, force=bool(args.force))
    _write_csv(outputs["casebook_csv"], casebook_rows, force=bool(args.force))
    _write_csv(outputs["example_ledger_csv"], example_rows, force=bool(args.force))
    _write_json(outputs["json"], payload, force=bool(args.force))
    _write_text(
        outputs["md"],
        _render_md(
            lane_rows=lane_rows,
            blocker_rows=blocker_rows,
            queue_rows=queue_rows,
            macro_rows=macro_rows,
            casebook_rows=casebook_rows,
            output_paths=outputs,
        ),
        force=bool(args.force),
    )
    _write_text(outputs["casebook_md"], _render_casebook_md(casebook_rows, example_rows, outputs), force=bool(args.force))
    print(f"[OK] Wrote Stage 6F integrated decision atlas: {safe_rel(outputs['md'])}")


if __name__ == "__main__":
    main()
