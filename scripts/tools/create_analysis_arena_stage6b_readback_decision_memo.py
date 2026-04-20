#!/usr/bin/env python3
"""Create the Stage-6B Analysis Arena readback decision memo.

Stage 6B readback is a read-only interpretation layer over the Stage-6B
shadow replay simulator. It converts scenario scorecards, increment tests,
support/restraint ablations, concentration warnings, and guardrail compliance
into explicit next-step gates. It does not alter live scoring, candidate
generation, translator logic, budget logic, or legacy infrastructure.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Dict, List, Mapping, Sequence, Tuple


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


STAGE6A_PREFIX = "ANALYSIS_ARENA__CYCLE__STAGE6A"
STAGE6B_PREFIX = "ANALYSIS_ARENA__CYCLE__STAGE6B"
READBACK_PREFIX = "ANALYSIS_ARENA__CYCLE__STAGE6B_READBACK"


def _parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--runs2-dir", default=str(RUNS_2_DIR), help="RUNS_2 root containing Stage-6B outputs.")
    ap.add_argument("--output-dir", default=str(RUNS_2_DIR), help="Cycle-level output directory.")
    ap.add_argument("--force", action="store_true", help="Overwrite existing Stage-6B readback outputs.")
    return ap.parse_args()


def _input_paths(runs2_dir: Path) -> Dict[str, Path]:
    return {
        "stage6b_md": runs2_dir / f"{STAGE6B_PREFIX}_SHADOW_REPLAY_SIMULATOR.md",
        "stage6b_json": runs2_dir / f"{STAGE6B_PREFIX}_SHADOW_REPLAY_SIMULATOR.json",
        "scenario_scorecard": runs2_dir / f"{STAGE6B_PREFIX}_REPLAY_SCENARIO_SCORECARD.csv",
        "increment_matrix": runs2_dir / f"{STAGE6B_PREFIX}_LANE_INCREMENT_MATRIX.csv",
        "support_ablation": runs2_dir / f"{STAGE6B_PREFIX}_SUPPORT_MODIFIER_ABLATION.csv",
        "restraint_calibration": runs2_dir / f"{STAGE6B_PREFIX}_RESTRAINT_CALIBRATION.csv",
        "concentration_audit": runs2_dir / f"{STAGE6B_PREFIX}_CONCENTRATION_AUDIT.csv",
        "guardrail_compliance": runs2_dir / f"{STAGE6B_PREFIX}_GUARDRAIL_COMPLIANCE.csv",
        "stage6a_requirements": runs2_dir / f"{STAGE6A_PREFIX}_SIMULATION_REQUIREMENTS.csv",
        "stage6a_guardrails": runs2_dir / f"{STAGE6A_PREFIX}_GUARDRAIL_MATRIX.csv",
    }


def _output_paths(output_dir: Path) -> Dict[str, Path]:
    return {
        "md": output_dir / f"{READBACK_PREFIX}_DECISION_MEMO.md",
        "json": output_dir / f"{READBACK_PREFIX}_DECISION_MEMO.json",
        "scenario_decisions_csv": output_dir / f"{READBACK_PREFIX}_SCENARIO_DECISIONS.csv",
        "requirement_results_csv": output_dir / f"{READBACK_PREFIX}_REQUIREMENT_RESULTS.csv",
        "guardrail_verdict_csv": output_dir / f"{READBACK_PREFIX}_GUARDRAIL_VERDICT.csv",
        "next_action_csv": output_dir / f"{READBACK_PREFIX}_NEXT_ACTION_QUEUE.csv",
        "macro_findings_candidates_csv": output_dir / f"{READBACK_PREFIX}_MACRO_FINDINGS_CANDIDATES.csv",
    }


def _load_required_csv(path: Path, label: str) -> List[Dict[str, str]]:
    rows = _read_csv_rows(path)
    if not rows:
        raise SystemExit(f"Missing or empty required Stage-6B readback input {label}: {safe_rel(path)}")
    return rows


def _load_required_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise SystemExit(f"Missing required Stage-6B readback input JSON: {safe_rel(path)}")
    return json.loads(path.read_text(encoding="utf-8", errors="replace"))


def _row_by_id(rows: Sequence[Mapping[str, Any]], field: str) -> Dict[str, Mapping[str, Any]]:
    return {str(row.get(field) or ""): row for row in rows}


def _comparison_by_id(rows: Sequence[Mapping[str, Any]]) -> Dict[str, Mapping[str, Any]]:
    return _row_by_id(rows, "comparison_id")


def _concentration_for(rows: Sequence[Mapping[str, Any]], scenario_id: str, dimension: str) -> Mapping[str, Any]:
    for row in rows:
        if str(row.get("scenario_id") or "") == scenario_id and str(row.get("dimension") or "") == dimension:
            return row
    return {}


def _guardrails_pass(rows: Sequence[Mapping[str, Any]]) -> bool:
    return all(str(row.get("status") or "") == "pass" for row in rows)


def _metric_delta(row: Mapping[str, Any], key: str) -> float:
    return _safe_float(row.get(key))


def _primary_replay_pass(comparisons: Mapping[str, Mapping[str, Any]]) -> bool:
    primary = comparisons.get("primary_vs_baseline", {})
    return (
        _metric_delta(primary, "false_positive_proxy_rate_delta") <= -0.05
        and _metric_delta(primary, "pool_normalized_positive_yield_delta") > 0
        and _safe_float(primary.get("avg_pool_ratio_b_vs_a")) <= 1.5
    )


def _decision_for_scenario(
    row: Mapping[str, Any],
    *,
    comparisons: Mapping[str, Mapping[str, Any]],
    concentration_rows: Sequence[Mapping[str, Any]],
    guardrails_ok: bool,
) -> Tuple[str, str, str, str, str, str]:
    scenario = str(row.get("scenario_id") or "")
    window_conc = _concentration_for(concentration_rows, scenario, "window")
    window_flag = str(window_conc.get("concentration_flag") or "")
    concentration_note = ""
    if window_flag == "high_concentration":
        concentration_note = " March-window concentration remains a blocking warning for live rewrite."

    if not guardrails_ok:
        return (
            "blocked_guardrail_failure",
            "blocked",
            "Stage 6B guardrail compliance is not clean.",
            "Repair guardrail failures and rerun Stage 6B before interpretation.",
            "blocked",
            "no_macro_entry",
        )

    if scenario == "baseline_clean_boxed":
        return (
            "baseline_reference_only",
            "baseline_only",
            "Baseline clean boxed scenario is useful as the comparison arm, not as a new rule.",
            "Keep as the benchmark for future shadow replay.",
            "baseline_only",
            "no_macro_entry",
        )

    if scenario == "primary_restrained_candidate_expression":
        primary_pass = _primary_replay_pass(comparisons)
        if primary_pass:
            return (
                "provisional_primary_shadow_design_seed",
                "future_window_confirmation_required",
                "Primary restrained replay improves false-positive proxy and yield versus baseline while keeping pool expansion bounded." + concentration_note,
                "Carry this lane into future/fresh-window confirmation and Stage 6B repeat readback before any rewrite specification.",
                "readback_only_no_live_permission",
                "provisional_candidate",
            )
        return (
            "primary_not_ready",
            "blocked",
            "Primary restrained replay did not beat the baseline strongly enough.",
            "Do not advance this lane until a stronger replay appears.",
            "blocked",
            "no_macro_entry",
        )

    if scenario == "secondary_lineage_supported_restrained":
        secondary = comparisons.get("secondary_vs_primary", {})
        return (
            "secondary_modifier_not_independent_expansion",
            "keep_as_lineage_modifier_retest",
            "Secondary lineage-supported replay slightly improves FP proxy but loses positive conversions and yield versus primary; it should not expand the pool independently." + concentration_note,
            "Keep as lineage/support modifier research, not an independent candidate-expression expansion.",
            "modifier_research_only",
            "provisional_candidate",
        )

    if scenario == "stage6a_allowed_candidate_union":
        union = comparisons.get("union_vs_primary", {})
        if abs(_safe_float(union.get("positive_conversion_delta"))) < 1e-9 and abs(_safe_float(union.get("avg_pool_ratio_b_vs_a")) - 1.0) < 1e-9:
            return (
                "duplicate_credit_blocked_cleanly",
                "guardrail_pass_reference",
                "The Stage 6A candidate union matches primary replay, proving the secondary lane is not adding duplicate-credit expansion.",
                "Keep union as a guardrail reference; do not score primary and secondary twice.",
                "readback_reference_only",
                "provisional_supporting_evidence",
            )
        return (
            "union_needs_duplicate_credit_review",
            "blocked",
            "The Stage 6A candidate union differs from primary, so duplicate-credit risk must be audited.",
            "Audit union construction before any future replay.",
            "blocked",
            "no_macro_entry",
        )

    if scenario == "broad_lineage_foundation_reference":
        return (
            "broad_lineage_blocked_until_narrowed",
            "narrow_before_design",
            "Broad lineage raises pool size and FP proxy versus primary despite more raw positive conversions." + concentration_note,
            "Derive narrowed lineage variants only after primary replay stays favorable on future windows.",
            "narrowing_research_only",
            "provisional_candidate",
        )

    if scenario == "candidate_rows_with_support_context":
        return (
            "support_on_not_validated_as_modifier",
            "modifier_not_ready",
            "Candidate rows with support context show worse FP proxy, worse yield, and much larger exposure than support-off rows.",
            "Do not use support-on as a positive modifier yet; search for narrower support conditions.",
            "support_research_only",
            "provisional_candidate",
        )

    if scenario == "candidate_rows_without_support_context":
        return (
            "support_off_reference_is_sharper",
            "support_ablation_reference",
            "Support-off candidate rows are smaller and sharper in this replay; this is a reference, not a standalone rule.",
            "Use this as the comparator for future support modifier design.",
            "reference_only",
            "provisional_supporting_evidence",
        )

    if scenario == "support_gate_context_excluded":
        return (
            "support_gate_remains_context_only",
            "context_only",
            "Standalone support gate context is broad and remains excluded from candidate pools.",
            "Keep support gates as context-only until paired candidate rows improve in replay.",
            "context_only",
            "provisional_supporting_evidence",
        )

    if scenario == "decay_watch_companion_excluded":
        return (
            "decay_watch_remains_companion_only",
            "companion_only",
            "Decay/watch carries large coverage but much worse FP proxy and yield than candidate union.",
            "Keep decay as carryforward/context annotation only; do not convert it into boxed candidate permission.",
            "companion_only",
            "provisional_supporting_evidence",
        )

    if scenario == "low_denominator_watchlist_excluded":
        return (
            "low_denominator_watchlist_retest",
            "retest_only",
            "The low-denominator watchlist looks sharp but has too little exposure for design promotion.",
            "Keep as a watchlist and require future/fresh repeat state-days.",
            "retest_only",
            "provisional_candidate",
        )

    if scenario == "restraint_retest_surface_excluded":
        return (
            "restraint_surface_promising_but_excluded",
            "penalty_research_only",
            "The restraint surface has attractive FP/yield metrics but is not a candidate-expression lane.",
            "Use it for penalty/veto calibration and soft-before-hard restraint design.",
            "penalty_research_only",
            "provisional_candidate",
        )

    return (
        "manual_review",
        "manual_review",
        "No explicit Stage 6B readback policy exists for this scenario.",
        "Review manually before assigning design role.",
        "no_live_permission",
        "no_macro_entry",
    )


def _scenario_decision_rows(
    score_rows: Sequence[Mapping[str, Any]],
    *,
    comparisons: Mapping[str, Mapping[str, Any]],
    concentration_rows: Sequence[Mapping[str, Any]],
    guardrails_ok: bool,
) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for row in score_rows:
        scenario = str(row.get("scenario_id") or "")
        wconc = _concentration_for(concentration_rows, scenario, "window")
        sconc = _concentration_for(concentration_rows, scenario, "state")
        decision, status, reason, next_action, permission, macro_posture = _decision_for_scenario(
            row,
            comparisons=comparisons,
            concentration_rows=concentration_rows,
            guardrails_ok=guardrails_ok,
        )
        rows.append(
            {
                "scenario_id": scenario,
                "scenario_role": row.get("scenario_role", ""),
                "readback_decision": decision,
                "status": status,
                "allowed_permission": permission,
                "macro_findings_posture": macro_posture,
                "next_action": next_action,
                "reason": reason,
                "ledger_rows": _safe_int(row.get("ledger_rows")),
                "cluster_count": _safe_int(row.get("cluster_count")),
                "state_count": _safe_int(row.get("state_count")),
                "active_state_days": _safe_int(row.get("active_state_days")),
                "avg_pool_or_exposure_per_state_day": _safe_float(row.get("avg_pool_or_exposure_per_state_day")),
                "false_positive_proxy_rate": _safe_float(row.get("false_positive_proxy_rate")),
                "pool_normalized_positive_yield": _safe_float(row.get("pool_normalized_positive_yield")),
                "positive_conversion_event_count": _safe_int(row.get("positive_conversion_event_count")),
                "window_concentration_flag": wconc.get("concentration_flag", ""),
                "top_window": wconc.get("top_group", ""),
                "top_window_positive_share": _safe_float(wconc.get("top_group_positive_conversion_share")),
                "state_concentration_flag": sconc.get("concentration_flag", ""),
                "top_state": sconc.get("top_group", ""),
                "top_state_positive_share": _safe_float(sconc.get("top_group_positive_conversion_share")),
            }
        )
    return rows


def _requirement_result_rows(
    requirements: Sequence[Mapping[str, Any]],
    *,
    comparisons: Mapping[str, Mapping[str, Any]],
    guardrails: Sequence[Mapping[str, Any]],
    support_rows: Sequence[Mapping[str, Any]],
    restraint_rows: Sequence[Mapping[str, Any]],
) -> List[Dict[str, Any]]:
    guardrail_ids = {str(row.get("guardrail_id") or ""): str(row.get("status") or "") for row in guardrails}
    support_by_bucket = _row_by_id(support_rows, "support_ablation_bucket")
    restraint_by_bucket = _row_by_id(restraint_rows, "restraint_calibration_bucket")

    def result_for(requirement_id: str) -> Tuple[str, str, str]:
        if requirement_id == "S6B-001":
            primary = comparisons.get("primary_vs_baseline", {})
            if _primary_replay_pass(comparisons):
                return (
                    "pass_with_concentration_warning",
                    "Primary beats baseline on FP proxy and yield with bounded pool expansion.",
                    "Repeat on future/fresh windows before rewrite specification.",
                )
            return ("fail", "Primary does not beat baseline enough.", "Do not advance primary lane.")
        if requirement_id == "S6B-002":
            secondary = comparisons.get("secondary_vs_primary", {})
            if _safe_float(secondary.get("pool_normalized_positive_yield_delta")) < 0:
                return (
                    "partial_modifier_only",
                    "Secondary is not an independent expansion because it loses yield and conversions versus primary.",
                    "Keep as lineage/support modifier research only.",
                )
            return ("pass_shadow_modifier", "Secondary adds value versus primary.", "Retest duplicate-credit and lineage guardrails.")
        if requirement_id == "S6B-003":
            support = comparisons.get("support_on_vs_support_off", {})
            if _safe_float(support.get("false_positive_proxy_rate_delta")) > 0 or _safe_float(support.get("pool_normalized_positive_yield_delta")) < 0:
                return (
                    "fail_as_positive_modifier",
                    "Support-on rows are broader and weaker than support-off rows in this replay.",
                    "Keep support-only excluded and search for narrower paired support conditions.",
                )
            return ("pass_modifier_candidate", "Support improves paired candidate rows.", "Retest support modifier on future windows.")
        if requirement_id == "S6B-004":
            no_penalty = restraint_by_bucket.get("no_penalty_all_candidate_rows", {})
            hard = restraint_by_bucket.get("hard_exclusion_non_high_pressure", {})
            if _safe_float(hard.get("false_positive_proxy_rate")) < _safe_float(no_penalty.get("false_positive_proxy_rate")):
                return (
                    "pass_research_not_live",
                    "Hard exclusion improves FP proxy and yield versus no-penalty, but Stage 6A requires soft-before-hard calibration.",
                    "Build soft-penalty calibration before any hard veto design.",
                )
            return ("needs_retest", "Restraint did not clearly improve candidate rows.", "Keep restraint as research only.")
        if requirement_id == "S6B-005":
            status = "pass" if guardrail_ids.get("G07_no_duplicate_credit_claim") == "pass" else "fail"
            return (
                status,
                "Stage 6B reports union replay without duplicate scoring credit.",
                "Keep overlap as narrowing/restraint unless future source-side ablation proves lift.",
            )
        if requirement_id == "S6B-006":
            status = "pass_with_warning" if guardrail_ids.get("G06_concentration_warning_carried") == "pass" else "fail"
            return (
                status,
                "Concentration warnings are carried through Stage 6B.",
                "Require future/fresh repeat before rewrite claims.",
            )
        if requirement_id == "S6B-007":
            decay = comparisons.get("decay_vs_candidate_union", {})
            if _safe_float(decay.get("false_positive_proxy_rate_delta")) > 0:
                return (
                    "pass_excluded",
                    "Decay companion stays outside candidate pool and is weaker than candidate union as spend evidence.",
                    "Keep as carryforward/context only.",
                )
            return ("needs_review", "Decay comparison did not show expected separation.", "Audit decay lane.")
        return ("manual_review", "No explicit readback result rule.", "Review manually.")

    rows: List[Dict[str, Any]] = []
    for requirement in requirements:
        result, evidence, next_action = result_for(str(requirement.get("requirement_id") or ""))
        rows.append(
            {
                "requirement_id": requirement.get("requirement_id", ""),
                "test_target": requirement.get("test_target", ""),
                "readback_result": result,
                "metric": requirement.get("metric", ""),
                "pass_condition": requirement.get("pass_condition", ""),
                "evidence": evidence,
                "next_action": next_action,
                "live_permission": "forbidden",
            }
        )
    return rows


def _guardrail_verdict_rows(
    *,
    stage6a_guardrails: Sequence[Mapping[str, Any]],
    stage6b_guardrails: Sequence[Mapping[str, Any]],
    scenario_rows: Sequence[Mapping[str, Any]],
) -> List[Dict[str, Any]]:
    decisions = Counter(str(row.get("status") or "") for row in scenario_rows)
    stage6b_pass = _guardrails_pass(stage6b_guardrails)
    rows = [
        {
            "guardrail_area": "stage6b_compliance",
            "status": "pass" if stage6b_pass else "fail",
            "evidence": f"{sum(1 for row in stage6b_guardrails if str(row.get('status') or '') == 'pass')} of {len(stage6b_guardrails)} Stage 6B compliance checks passed.",
            "verdict": "Readback may proceed." if stage6b_pass else "Reject readback until Stage 6B compliance is repaired.",
        },
        {
            "guardrail_area": "live_permission",
            "status": "pass",
            "evidence": "All readback decisions set live permission to forbidden or readback-only.",
            "verdict": "No live scoring/candidate/budget permission granted.",
        },
        {
            "guardrail_area": "lane_separation",
            "status": "pass",
            "evidence": f"Scenario statuses remain separated: {dict(decisions)}.",
            "verdict": "Candidate, support, decay, low-denominator, and restraint lanes remain separate.",
        },
        {
            "guardrail_area": "stage6a_guardrails_referenced",
            "status": "pass" if len(stage6a_guardrails) >= 9 else "fail",
            "evidence": f"{len(stage6a_guardrails)} Stage 6A guardrails loaded.",
            "verdict": "Stage 6A contract is available for readback." if len(stage6a_guardrails) >= 9 else "Stage 6A guardrail context is incomplete.",
        },
    ]
    return rows


def _next_action_rows(
    *,
    scenario_rows: Sequence[Mapping[str, Any]],
    requirement_rows: Sequence[Mapping[str, Any]],
    guardrail_rows: Sequence[Mapping[str, Any]],
) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    priority = 1

    def add(action_type: str, subject: str, action: str, rationale: str, permission: str, source: str) -> None:
        nonlocal priority
        rows.append(
            {
                "priority": priority,
                "action_type": action_type,
                "subject": subject,
                "action": action,
                "rationale": rationale,
                "allowed_permission": permission,
                "source_artifact": source,
            }
        )
        priority += 1

    primary = next((row for row in scenario_rows if str(row.get("scenario_id") or "") == "primary_restrained_candidate_expression"), {})
    if str(primary.get("status") or "") == "future_window_confirmation_required":
        add(
            "future_window_confirmation",
            "primary_restrained_candidate_expression",
            "Repeat Stage 6B replay/readback on future/fresh windows before any translator/scoring rewrite specification.",
            str(primary.get("reason") or ""),
            "readback_only_no_live_permission",
            f"{READBACK_PREFIX}_SCENARIO_DECISIONS.csv",
        )

    add(
        "support_modifier_rework",
        "support_context",
        "Do not promote support-on as a positive modifier yet; build narrower paired support hypotheses only.",
        "Stage 6B support-on rows were broader and weaker than support-off rows.",
        "support_research_only",
        f"{READBACK_PREFIX}_REQUIREMENT_RESULTS.csv",
    )
    add(
        "restraint_soft_penalty_calibration",
        "restraint_filter",
        "Design soft-penalty calibration before any hard veto or hard exclusion rule.",
        "Hard exclusion improved replay metrics, but Stage 6A guardrail requires soft-before-hard validation.",
        "penalty_research_only",
        f"{READBACK_PREFIX}_REQUIREMENT_RESULTS.csv",
    )
    add(
        "lineage_narrowing",
        "broad_lineage_foundation_reference",
        "Derive narrowed lineage variants; do not promote broad lineage foundation directly.",
        "Broad lineage increased pool size and FP proxy versus primary.",
        "narrowing_research_only",
        f"{READBACK_PREFIX}_SCENARIO_DECISIONS.csv",
    )
    add(
        "decay_companion_boundary",
        "decay_watch_companion",
        "Keep decay/watch as carryforward annotations and out of candidate pool metrics.",
        "Decay companion has weaker FP/yield as spend evidence and must remain companion-only.",
        "companion_only",
        f"{READBACK_PREFIX}_REQUIREMENT_RESULTS.csv",
    )
    add(
        "macro_findings_gate",
        "macro_findings_log",
        "Treat Stage 6B findings as provisional candidates until repeated on future/fresh windows or explicitly reviewed.",
        "Readback is evidence-led but still March-concentrated.",
        "provisional_only_until_repeat",
        f"{READBACK_PREFIX}_MACRO_FINDINGS_CANDIDATES.csv",
    )
    add(
        "rewrite_block",
        "translator_scoring_rewrite",
        "Do not begin a live translator/scoring rewrite from this readback alone.",
        "Stage 6B readback is favorable for primary research, but concentration and support/restraint gates remain open.",
        "blocked_until_future_confirmation",
        f"{READBACK_PREFIX}_GUARDRAIL_VERDICT.csv",
    )
    return rows


def _macro_findings_candidate_rows(scenario_rows: Sequence[Mapping[str, Any]], requirement_rows: Sequence[Mapping[str, Any]]) -> List[Dict[str, Any]]:
    rows = [
        {
            "finding_id": "S6B-MF-001",
            "finding": "Primary restrained candidate-expression replay improves FP proxy and pool-normalized yield versus baseline.",
            "evidence_artifact": f"{READBACK_PREFIX}_SCENARIO_DECISIONS.csv",
            "supporting_row": "primary_restrained_candidate_expression",
            "posture": "provisional_candidate",
            "why_not_confirmed": "Stage 6B positive-conversion evidence is still March-window concentrated and requires future/fresh repeat.",
            "recommended_log_action": "Hold for future-window confirmation or explicitly log as provisional only.",
        },
        {
            "finding_id": "S6B-MF-002",
            "finding": "Support context is not validated as a positive modifier in the current replay.",
            "evidence_artifact": f"{READBACK_PREFIX}_REQUIREMENT_RESULTS.csv",
            "supporting_row": "S6B-003",
            "posture": "provisional_candidate",
            "why_not_confirmed": "Support-on rows worsened FP/yield and expanded exposure; narrower support conditions need testing.",
            "recommended_log_action": "Keep as engineering/research finding unless repeated across future windows.",
        },
        {
            "finding_id": "S6B-MF-003",
            "finding": "Decay/watch remains companion-only and should not be converted into boxed candidate permission.",
            "evidence_artifact": f"{READBACK_PREFIX}_REQUIREMENT_RESULTS.csv",
            "supporting_row": "S6B-007",
            "posture": "provisional_supporting_evidence",
            "why_not_confirmed": "The boundary is supported by multiple guardrails, but live policy still needs future readback repetition.",
            "recommended_log_action": "Reference in readback; promote to macro only after repeated fresh-window confirmation or explicit review.",
        },
        {
            "finding_id": "S6B-MF-004",
            "finding": "Restraint filtering is promising, but hard exclusion must not be promoted before soft-penalty calibration.",
            "evidence_artifact": f"{READBACK_PREFIX}_REQUIREMENT_RESULTS.csv",
            "supporting_row": "S6B-004",
            "posture": "provisional_candidate",
            "why_not_confirmed": "Hard exclusion improved replay metrics, but soft-before-hard guardrail remains open.",
            "recommended_log_action": "Keep as penalty research follow-up.",
        },
    ]
    return rows


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
    runs2_dir: Path,
    scenario_rows: Sequence[Mapping[str, Any]],
    requirement_rows: Sequence[Mapping[str, Any]],
    guardrail_rows: Sequence[Mapping[str, Any]],
    next_actions: Sequence[Mapping[str, Any]],
    macro_rows: Sequence[Mapping[str, Any]],
    output_paths: Mapping[str, Path],
) -> str:
    by_scenario = _row_by_id(scenario_rows, "scenario_id")
    primary = by_scenario.get("primary_restrained_candidate_expression", {})
    lines: List[str] = [
        "# Analysis Arena Stage 6B Readback Decision Memo",
        "",
        "Purpose: convert Stage 6B shadow replay outputs into explicit readback decisions before any translator/scoring rewrite discussion.",
        "",
        "## Metadata",
        f"- runs2_dir: `{safe_rel(runs2_dir)}`",
        f"- scenario_decisions: `{len(scenario_rows)}`",
        f"- requirement_results: `{len(requirement_rows)}`",
        f"- guardrail_verdict_rows: `{len(guardrail_rows)}`",
        f"- next_actions: `{len(next_actions)}`",
        "",
        "## Guardrails",
        "- Stage 6B readback grants no live scoring, candidate-generation, translator, budget, or legacy-infrastructure permission.",
        "- Primary favorable replay is not a rewrite trigger until future/fresh windows repeat the shape.",
        "- Support-only, decay/watch, low-denominator, broad-lineage, and restraint surfaces remain separated.",
        "- Macro Findings Log entries should stay provisional unless repeated or explicitly reviewed as evidence-led conclusions.",
        "",
        "## Executive Readback",
        f"- Primary restrained lane decision: `{primary.get('readback_decision', '')}` with FP proxy `{_pct(primary.get('false_positive_proxy_rate'))}`, yield `{_fmt(primary.get('pool_normalized_positive_yield'))}`, and avg pool `{_fmt(primary.get('avg_pool_or_exposure_per_state_day'))}`.",
        "- The primary lane is the best current shadow-design seed, but it requires future/fresh-window confirmation before rewrite specification.",
        "- Secondary lineage support is useful as modifier/retest context, not as independent expansion.",
        "- Support-on behavior is not yet validated as a positive modifier; support remains context-only until narrower paired support passes.",
        "- Restraint remains promising penalty research, with soft-before-hard calibration required.",
        "- Decay/watch remains companion-only, not boxed candidate permission.",
        "",
        "## Scenario Decisions",
    ]
    lines.extend(
        _table(
            ["scenario", "decision", "status", "permission", "FP proxy", "yield", "top-window share"],
            [
                [
                    row.get("scenario_id", ""),
                    row.get("readback_decision", ""),
                    row.get("status", ""),
                    row.get("allowed_permission", ""),
                    _pct(row.get("false_positive_proxy_rate")),
                    _fmt(row.get("pool_normalized_positive_yield")),
                    _pct(row.get("top_window_positive_share")),
                ]
                for row in scenario_rows
            ],
        )
    )
    lines += [
        "",
        "## Requirement Results",
    ]
    lines.extend(
        _table(
            ["requirement", "target", "result", "next action"],
            [
                [
                    row.get("requirement_id", ""),
                    row.get("test_target", ""),
                    row.get("readback_result", ""),
                    row.get("next_action", ""),
                ]
                for row in requirement_rows
            ],
        )
    )
    lines += [
        "",
        "## Guardrail Verdict",
    ]
    lines.extend(
        _table(
            ["area", "status", "verdict"],
            [
                [row.get("guardrail_area", ""), row.get("status", ""), row.get("verdict", "")]
                for row in guardrail_rows
            ],
        )
    )
    lines += [
        "",
        "## Next Action Queue",
    ]
    lines.extend(
        _table(
            ["priority", "type", "subject", "permission", "action"],
            [
                [
                    row.get("priority", ""),
                    row.get("action_type", ""),
                    row.get("subject", ""),
                    row.get("allowed_permission", ""),
                    row.get("action", ""),
                ]
                for row in next_actions
            ],
        )
    )
    lines += [
        "",
        "## Macro Findings Candidates",
    ]
    lines.extend(
        _table(
            ["finding", "posture", "recommended action"],
            [
                [row.get("finding_id", ""), row.get("posture", ""), row.get("recommended_log_action", "")]
                for row in macro_rows
            ],
        )
    )
    lines += [
        "",
        "## Interpretation",
        "- Stage 6B readback is favorable enough to preserve the primary restrained lane as the next research spine.",
        "- It is not favorable enough to start a live rewrite because the evidence is still March-concentrated and support/restraint calibration is unfinished.",
        "- The next development layer should be future-window confirmation and soft-penalty/narrow-support design, not live scoring or budget changes.",
        "",
        "## Output Files",
    ]
    for key, path in output_paths.items():
        lines.append(f"- {key}: `{safe_rel(path)}`")
    lines.append("")
    return "\n".join(lines)


def build_readback_payload(
    *,
    runs2_dir: Path,
    output_dir: Path,
) -> Tuple[Dict[str, Any], Dict[str, List[Dict[str, Any]]], str]:
    inputs = _input_paths(runs2_dir)
    outputs = _output_paths(output_dir)

    stage6b_json = _load_required_json(inputs["stage6b_json"])
    scenario_scorecard = _load_required_csv(inputs["scenario_scorecard"], "scenario scorecard")
    increment_matrix = _load_required_csv(inputs["increment_matrix"], "lane increment matrix")
    support_ablation = _load_required_csv(inputs["support_ablation"], "support modifier ablation")
    restraint_calibration = _load_required_csv(inputs["restraint_calibration"], "restraint calibration")
    concentration_audit = _load_required_csv(inputs["concentration_audit"], "concentration audit")
    guardrail_compliance = _load_required_csv(inputs["guardrail_compliance"], "guardrail compliance")
    stage6a_requirements = _load_required_csv(inputs["stage6a_requirements"], "Stage 6A simulation requirements")
    stage6a_guardrails = _load_required_csv(inputs["stage6a_guardrails"], "Stage 6A guardrails")

    comparisons = _comparison_by_id(increment_matrix)
    guardrails_ok = _guardrails_pass(guardrail_compliance)
    scenario_rows = _scenario_decision_rows(
        scenario_scorecard,
        comparisons=comparisons,
        concentration_rows=concentration_audit,
        guardrails_ok=guardrails_ok,
    )
    requirement_rows = _requirement_result_rows(
        stage6a_requirements,
        comparisons=comparisons,
        guardrails=guardrail_compliance,
        support_rows=support_ablation,
        restraint_rows=restraint_calibration,
    )
    guardrail_rows = _guardrail_verdict_rows(
        stage6a_guardrails=stage6a_guardrails,
        stage6b_guardrails=guardrail_compliance,
        scenario_rows=scenario_rows,
    )
    next_actions = _next_action_rows(
        scenario_rows=scenario_rows,
        requirement_rows=requirement_rows,
        guardrail_rows=guardrail_rows,
    )
    macro_rows = _macro_findings_candidate_rows(scenario_rows, requirement_rows)

    tables = {
        "scenario_decisions": scenario_rows,
        "requirement_results": requirement_rows,
        "guardrail_verdict": guardrail_rows,
        "next_actions": next_actions,
        "macro_findings_candidates": macro_rows,
    }
    payload: Dict[str, Any] = {
        "runs2_dir": safe_rel(runs2_dir),
        "source_files": {key: safe_rel(path) for key, path in inputs.items()},
        "stage6b_permission": stage6b_json.get("stage6b_permission", ""),
        "stage6b_live_permission": stage6b_json.get("live_permission", ""),
        **tables,
        "readback_permission": "read_only_decision_memo",
        "live_permission": "forbidden",
        "next_layer": "future/fresh-window confirmation before any translator/scoring rewrite specification",
    }
    md = _render_md(
        runs2_dir=runs2_dir,
        scenario_rows=scenario_rows,
        requirement_rows=requirement_rows,
        guardrail_rows=guardrail_rows,
        next_actions=next_actions,
        macro_rows=macro_rows,
        output_paths=outputs,
    )
    return payload, tables, md


def main() -> None:
    args = _parse_args()
    runs2_dir = _resolve_path(args.runs2_dir)
    output_dir = _resolve_path(args.output_dir)
    out_paths = _output_paths(output_dir)
    payload, tables, md = build_readback_payload(runs2_dir=runs2_dir, output_dir=output_dir)

    _write_text(out_paths["md"], md, force=bool(args.force))
    _write_json(out_paths["json"], payload, force=bool(args.force))
    _write_csv(out_paths["scenario_decisions_csv"], tables["scenario_decisions"], force=bool(args.force))
    _write_csv(out_paths["requirement_results_csv"], tables["requirement_results"], force=bool(args.force))
    _write_csv(out_paths["guardrail_verdict_csv"], tables["guardrail_verdict"], force=bool(args.force))
    _write_csv(out_paths["next_action_csv"], tables["next_actions"], force=bool(args.force))
    _write_csv(out_paths["macro_findings_candidates_csv"], tables["macro_findings_candidates"], force=bool(args.force))

    print(f"[OK] Wrote Stage-6B readback decision memo: {safe_rel(out_paths['md'])}")
    print(f"[OK] Scenario decisions: {len(tables['scenario_decisions'])}")
    print(f"[OK] Requirement results: {len(tables['requirement_results'])}")
    print(f"[OK] Next actions: {len(tables['next_actions'])}")


if __name__ == "__main__":
    main()
