#!/usr/bin/env python3
"""Create the Stage-6C future/fresh-window confirmation protocol.

Stage 6C is a read-only bridge between Stage 6B readback and future window
work. It turns the Stage 6B decisions into explicit confirmation contracts,
fresh-window queue items, rewrite blockers, and macro-findings gates. It does
not alter live scoring, candidate generation, translator logic, budget logic,
or legacy infrastructure.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Mapping, Sequence


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


STAGE6B_PREFIX = "ANALYSIS_ARENA__CYCLE__STAGE6B"
READBACK_PREFIX = "ANALYSIS_ARENA__CYCLE__STAGE6B_READBACK"
STAGE6C_PREFIX = "ANALYSIS_ARENA__CYCLE__STAGE6C"


def _parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--runs2-dir", default=str(RUNS_2_DIR), help="RUNS_2 root containing Stage-6B readback outputs.")
    ap.add_argument("--output-dir", default=str(RUNS_2_DIR), help="Cycle-level output directory.")
    ap.add_argument("--force", action="store_true", help="Overwrite existing Stage-6C outputs.")
    return ap.parse_args()


def _input_paths(runs2_dir: Path) -> Dict[str, Path]:
    return {
        "readback_json": runs2_dir / f"{READBACK_PREFIX}_DECISION_MEMO.json",
        "scenario_decisions": runs2_dir / f"{READBACK_PREFIX}_SCENARIO_DECISIONS.csv",
        "requirement_results": runs2_dir / f"{READBACK_PREFIX}_REQUIREMENT_RESULTS.csv",
        "guardrail_verdict": runs2_dir / f"{READBACK_PREFIX}_GUARDRAIL_VERDICT.csv",
        "next_action_queue": runs2_dir / f"{READBACK_PREFIX}_NEXT_ACTION_QUEUE.csv",
        "macro_candidates": runs2_dir / f"{READBACK_PREFIX}_MACRO_FINDINGS_CANDIDATES.csv",
        "scenario_scorecard": runs2_dir / f"{STAGE6B_PREFIX}_REPLAY_SCENARIO_SCORECARD.csv",
        "increment_matrix": runs2_dir / f"{STAGE6B_PREFIX}_LANE_INCREMENT_MATRIX.csv",
        "concentration_audit": runs2_dir / f"{STAGE6B_PREFIX}_CONCENTRATION_AUDIT.csv",
    }


def _output_paths(output_dir: Path) -> Dict[str, Path]:
    return {
        "md": output_dir / f"{STAGE6C_PREFIX}_FUTURE_CONFIRMATION_PROTOCOL.md",
        "json": output_dir / f"{STAGE6C_PREFIX}_FUTURE_CONFIRMATION_PROTOCOL.json",
        "test_matrix_csv": output_dir / f"{STAGE6C_PREFIX}_CONFIRMATION_TEST_MATRIX.csv",
        "threshold_contract_csv": output_dir / f"{STAGE6C_PREFIX}_THRESHOLD_CONTRACT.csv",
        "fresh_window_queue_csv": output_dir / f"{STAGE6C_PREFIX}_FRESH_WINDOW_QUEUE.csv",
        "rewrite_blockers_csv": output_dir / f"{STAGE6C_PREFIX}_REWRITE_BLOCKERS.csv",
        "macro_gate_csv": output_dir / f"{STAGE6C_PREFIX}_MACRO_REVIEW_GATE.csv",
    }


def _load_required_csv(path: Path, label: str) -> List[Dict[str, str]]:
    rows = _read_csv_rows(path)
    if not rows:
        raise SystemExit(f"Missing or empty Stage-6C input {label}: {safe_rel(path)}")
    return rows


def _load_optional_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8", errors="replace"))


def _row_by_id(rows: Sequence[Mapping[str, Any]], field: str) -> Dict[str, Mapping[str, Any]]:
    return {str(row.get(field) or ""): row for row in rows}


def _comparison_by_id(rows: Sequence[Mapping[str, Any]]) -> Dict[str, Mapping[str, Any]]:
    return _row_by_id(rows, "comparison_id")


def _current_evidence(row: Mapping[str, Any]) -> str:
    if not row:
        return "missing_current_evidence"
    return (
        f"fp={_pct(row.get('false_positive_proxy_rate'))}; "
        f"yield={_fmt(row.get('pool_normalized_positive_yield'))}; "
        f"positive={_safe_int(row.get('positive_conversion_event_count'))}; "
        f"state_days={_safe_int(row.get('active_state_days'))}; "
        f"avg_pool={_fmt(row.get('avg_pool_or_exposure_per_state_day'))}"
    )


def _test_matrix_rows(
    *,
    scenario_decisions: Sequence[Mapping[str, Any]],
    requirement_results: Sequence[Mapping[str, Any]],
    increment_rows: Sequence[Mapping[str, Any]],
    guardrails: Sequence[Mapping[str, Any]],
) -> List[Dict[str, Any]]:
    scenarios = _row_by_id(scenario_decisions, "scenario_id")
    requirements = _row_by_id(requirement_results, "requirement_id")
    comparisons = _comparison_by_id(increment_rows)
    guardrail_status = {str(row.get("guardrail_area") or ""): str(row.get("status") or "") for row in guardrails}
    primary = scenarios.get("primary_restrained_candidate_expression", {})
    support_req = requirements.get("S6B-003", {})
    restraint_req = requirements.get("S6B-004", {})
    decay_req = requirements.get("S6B-007", {})
    duplicate_req = requirements.get("S6B-005", {})
    concentration_req = requirements.get("S6B-006", {})
    primary_cmp = comparisons.get("primary_vs_baseline", {})
    support_cmp = comparisons.get("support_on_vs_support_off", {})

    return [
        {
            "test_id": "S6C-001",
            "confirmation_target": "primary_restrained_candidate_expression",
            "stage6b_source": "primary_vs_baseline",
            "current_march_evidence": _current_evidence(primary),
            "fresh_window_test": "Repeat Stage 6B replay/readback on a fresh window and compare primary against the baseline clean boxed arm.",
            "pass_threshold": "false_positive_proxy_rate_delta <= -0.050; pool_normalized_positive_yield_delta > 0; avg_pool_ratio_b_vs_a <= 1.500; positive conversions remain non-trivial.",
            "current_threshold_result": (
                f"fp_delta={_fmt(primary_cmp.get('false_positive_proxy_rate_delta'))}; "
                f"yield_delta={_fmt(primary_cmp.get('pool_normalized_positive_yield_delta'))}; "
                f"pool_ratio={_fmt(primary_cmp.get('avg_pool_ratio_b_vs_a'))}"
            ),
            "minimum_repeat_requirement": "Pass on at least one future/fresh window for continued research; prefer two independent fresh confirmations before rewrite spec.",
            "allowed_if_pass": "Keep as provisional primary shadow design seed.",
            "blocked_if_fail": "Return to Stage 6B diagnostics; no rewrite permission.",
            "live_permission": "none",
        },
        {
            "test_id": "S6C-002",
            "confirmation_target": "concentration_warning_break",
            "stage6b_source": "S6B-006",
            "current_march_evidence": str(concentration_req.get("readback_result") or ""),
            "fresh_window_test": "Carry window/state concentration flags into the fresh run and require the finding to survive outside the March window.",
            "pass_threshold": "Primary can pass with warnings only if metrics repeat and concentration warnings are explicit; concentration alone cannot confirm a macro finding.",
            "current_threshold_result": guardrail_status.get("stage6b_compliance", ""),
            "minimum_repeat_requirement": "At least one non-March fresh window, preferably two.",
            "allowed_if_pass": "Mark evidence as repeat-confirmed with concentration caveat.",
            "blocked_if_fail": "Keep finding provisional and do not promote to system rule.",
            "live_permission": "none",
        },
        {
            "test_id": "S6C-003",
            "confirmation_target": "support_context_modifier",
            "stage6b_source": "support_on_vs_support_off",
            "current_march_evidence": str(support_req.get("evidence") or ""),
            "fresh_window_test": "Retest support-on only as a narrower paired modifier, never as broad positive expansion.",
            "pass_threshold": "support-on subset must reduce FP proxy or improve yield versus support-off peer while not materially expanding pool exposure.",
            "current_threshold_result": (
                f"fp_delta={_fmt(support_cmp.get('false_positive_proxy_rate_delta'))}; "
                f"yield_delta={_fmt(support_cmp.get('pool_normalized_positive_yield_delta'))}"
            ),
            "minimum_repeat_requirement": "Must pass narrowed-bucket evidence before entering any scoring rewrite.",
            "allowed_if_pass": "Research-only support modifier candidate.",
            "blocked_if_fail": "Keep support as context-only annotation.",
            "live_permission": "none",
        },
        {
            "test_id": "S6C-004",
            "confirmation_target": "restraint_soft_penalty",
            "stage6b_source": "S6B-004",
            "current_march_evidence": str(restraint_req.get("evidence") or ""),
            "fresh_window_test": "Convert hard-exclusion evidence into soft-penalty simulations and test whether high-pressure rows can be downweighted without losing useful conversions.",
            "pass_threshold": "soft penalty must reduce FP pressure versus no-penalty reference while preserving materially useful positive conversions; hard veto is forbidden at this stage.",
            "current_threshold_result": str(restraint_req.get("readback_result") or ""),
            "minimum_repeat_requirement": "Soft-penalty workbench must show stable calibration before rewrite design.",
            "allowed_if_pass": "Penalty research candidate only.",
            "blocked_if_fail": "Keep restraint as diagnostic warning only.",
            "live_permission": "none",
        },
        {
            "test_id": "S6C-005",
            "confirmation_target": "lineage_narrowing",
            "stage6b_source": "broad_lineage_vs_primary",
            "current_march_evidence": _current_evidence(scenarios.get("broad_lineage_foundation_reference", {})),
            "fresh_window_test": "Retest narrowed lineage variants; do not promote broad lineage foundation directly.",
            "pass_threshold": "narrowed lineage must improve or preserve FP/yield versus primary while adding non-duplicate conversions.",
            "current_threshold_result": "broad lineage is blocked until narrowed",
            "minimum_repeat_requirement": "Narrowing candidate plus fresh replay confirmation.",
            "allowed_if_pass": "Lineage modifier research only.",
            "blocked_if_fail": "Keep broad lineage as foundation reference only.",
            "live_permission": "none",
        },
        {
            "test_id": "S6C-006",
            "confirmation_target": "decay_companion_boundary",
            "stage6b_source": "S6B-007",
            "current_march_evidence": str(decay_req.get("evidence") or ""),
            "fresh_window_test": "Keep decay evidence separate from candidate-pool scoring and repeat the boundary check in future windows.",
            "pass_threshold": "decay remains companion-only; no candidate permission even when carrying useful explanatory hits.",
            "current_threshold_result": str(decay_req.get("readback_result") or ""),
            "minimum_repeat_requirement": "Boundary must remain explicit in every fresh-window readback.",
            "allowed_if_pass": "Companion/carryforward annotation only.",
            "blocked_if_fail": "Audit decay wiring before more replay work.",
            "live_permission": "none",
        },
        {
            "test_id": "S6C-007",
            "confirmation_target": "duplicate_credit_guardrail",
            "stage6b_source": "S6B-005",
            "current_march_evidence": str(duplicate_req.get("evidence") or ""),
            "fresh_window_test": "Verify union replay never double-counts primary and secondary lineage-supported rows.",
            "pass_threshold": "candidate union must not claim duplicate scoring credit.",
            "current_threshold_result": str(duplicate_req.get("readback_result") or ""),
            "minimum_repeat_requirement": "Required every Stage 6B replay/readback.",
            "allowed_if_pass": "Readback reference only.",
            "blocked_if_fail": "Stop rewrite path until duplicate-credit issue is repaired.",
            "live_permission": "none",
        },
        {
            "test_id": "S6C-008",
            "confirmation_target": "macro_findings_gate",
            "stage6b_source": "macro_findings_candidates",
            "current_march_evidence": "Stage 6B macro findings are provisional candidates.",
            "fresh_window_test": "No macro finding becomes confirmed without future/fresh repeat or explicit human review note.",
            "pass_threshold": "repeat evidence exists and caveats are logged.",
            "current_threshold_result": "provisional_only_until_repeat",
            "minimum_repeat_requirement": "One fresh repeat minimum; two preferred for rewrite influence.",
            "allowed_if_pass": "Promote to macro findings log with repeat-confirmed posture.",
            "blocked_if_fail": "Keep in readback package only.",
            "live_permission": "none",
        },
        {
            "test_id": "S6C-009",
            "confirmation_target": "translator_scoring_rewrite_gate",
            "stage6b_source": "rewrite_block",
            "current_march_evidence": "Stage 6B readback explicitly blocks live rewrite from March evidence alone.",
            "fresh_window_test": "Rewrite discussion opens only after S6C primary repeat, duplicate-credit, concentration, support, restraint, and decay gates are cleanly resolved.",
            "pass_threshold": "all prerequisite gates pass or remain explicitly quarantined.",
            "current_threshold_result": "blocked_until_future_confirmation",
            "minimum_repeat_requirement": "Fresh-window confirmation plus workbench readback.",
            "allowed_if_pass": "Draft rewrite specification only, not live deployment.",
            "blocked_if_fail": "No rewrite specification.",
            "live_permission": "none",
        },
    ]


def _threshold_contract_rows(test_rows: Sequence[Mapping[str, Any]]) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for row in test_rows:
        rows.append(
            {
                "contract_id": row.get("test_id", ""),
                "subject": row.get("confirmation_target", ""),
                "metric_contract": row.get("pass_threshold", ""),
                "repeat_contract": row.get("minimum_repeat_requirement", ""),
                "permission_if_met": row.get("allowed_if_pass", ""),
                "permission_if_not_met": row.get("blocked_if_fail", ""),
                "live_permission": "forbidden",
                "candidate_generation_permission": "forbidden",
                "budget_permission": "forbidden",
            }
        )
    return rows


def _fresh_window_queue_rows(next_actions: Sequence[Mapping[str, Any]], test_rows: Sequence[Mapping[str, Any]]) -> List[Dict[str, Any]]:
    tests_by_subject = _row_by_id(test_rows, "confirmation_target")
    rows: List[Dict[str, Any]] = []
    for action in next_actions:
        subject = str(action.get("subject") or "")
        mapped_subject = {
            "primary_restrained_candidate_expression": "primary_restrained_candidate_expression",
            "support_context": "support_context_modifier",
            "restraint_filter": "restraint_soft_penalty",
            "broad_lineage_foundation_reference": "lineage_narrowing",
            "decay_watch_companion": "decay_companion_boundary",
            "macro_findings_log": "macro_findings_gate",
            "translator_scoring_rewrite": "translator_scoring_rewrite_gate",
        }.get(subject, subject)
        test = tests_by_subject.get(mapped_subject, {})
        rows.append(
            {
                "priority": _safe_int(action.get("priority")),
                "queue_item": action.get("action_type", ""),
                "subject": subject,
                "mapped_confirmation_target": mapped_subject,
                "fresh_window_instruction": action.get("action", ""),
                "acceptance_test": test.get("fresh_window_test", ""),
                "pass_threshold": test.get("pass_threshold", ""),
                "required_artifacts": "Stage 6B replay/readback outputs plus Stage 6C/6D/6E workbench readbacks where applicable.",
                "allowed_permission": action.get("allowed_permission", ""),
                "live_permission": "none",
            }
        )
    return rows


def _rewrite_blocker_rows(test_rows: Sequence[Mapping[str, Any]], guardrails: Sequence[Mapping[str, Any]]) -> List[Dict[str, Any]]:
    guardrail_ok = all(str(row.get("status") or "") == "pass" for row in guardrails)
    blockers = [
        ("rewrite_blocker_primary_repeat", "S6C-001", "Primary evidence has not yet repeated on a future/fresh window."),
        ("rewrite_blocker_concentration", "S6C-002", "March concentration warning remains a live-design blocker until fresh repeat exists."),
        ("rewrite_blocker_support_modifier", "S6C-003", "Support-on is not validated as a broad positive modifier."),
        ("rewrite_blocker_restraint_soft_before_hard", "S6C-004", "Hard restraint exclusion cannot be promoted before soft-penalty calibration."),
        ("rewrite_blocker_duplicate_credit", "S6C-007", "Duplicate-credit guardrail must pass on every replay."),
        ("rewrite_blocker_decay_boundary", "S6C-006", "Decay must remain companion-only and separate from spend evidence."),
    ]
    by_id = _row_by_id(test_rows, "test_id")
    rows: List[Dict[str, Any]] = []
    for blocker_id, test_id, rationale in blockers:
        test = by_id.get(test_id, {})
        rows.append(
            {
                "blocker_id": blocker_id,
                "linked_test_id": test_id,
                "status": "active_blocker",
                "rationale": rationale,
                "clearance_condition": test.get("minimum_repeat_requirement", ""),
                "current_evidence": test.get("current_threshold_result", ""),
                "guardrail_context": "stage6b_readback_guardrails_pass" if guardrail_ok else "stage6b_readback_guardrail_issue",
                "live_permission": "forbidden",
            }
        )
    return rows


def _macro_gate_rows(macro_rows: Sequence[Mapping[str, Any]]) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for row in macro_rows:
        posture = str(row.get("posture") or "")
        rows.append(
            {
                "finding_id": row.get("finding_id", ""),
                "finding": row.get("finding", ""),
                "current_posture": posture,
                "stage6c_disposition": "hold_for_fresh_confirmation" if "provisional" in posture else "reference_only",
                "promotion_condition": "repeat on future/fresh window or explicit review note with caveats",
                "blocked_from_live_use": "true",
                "source_evidence": row.get("evidence_artifact", ""),
                "why_not_confirmed": row.get("why_not_confirmed", ""),
            }
        )
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
    test_rows: Sequence[Mapping[str, Any]],
    threshold_rows: Sequence[Mapping[str, Any]],
    queue_rows: Sequence[Mapping[str, Any]],
    blocker_rows: Sequence[Mapping[str, Any]],
    macro_gate_rows: Sequence[Mapping[str, Any]],
    output_paths: Mapping[str, Path],
) -> str:
    lines: List[str] = [
        "# Analysis Arena Stage 6C Future Confirmation Protocol",
        "",
        "## Guardrail",
        "",
        "Stage 6C is read-only. It creates confirmation contracts and queue items for future windows; it does not change live scoring, candidate generation, translator logic, budget logic, or legacy infrastructure.",
        "",
        "## Executive Readback",
        "",
        "- Stage 6B produced a promising primary restrained candidate expression, but Stage 6C treats it as provisional until future/fresh-window confirmation exists.",
        "- Support, restraint, lineage, decay, duplicate-credit, and macro-findings gates remain separate so one favorable aggregate does not silently become a live rule.",
        "- The translator/scoring rewrite remains blocked until the confirmation matrix is rerun against fresh evidence and its blockers are cleared or explicitly quarantined.",
        "",
        "## Confirmation Matrix",
        "",
    ]
    lines.extend(
        _table(
            ["test_id", "target", "fresh_window_test", "pass_threshold", "live_permission"],
            [
                [
                    row.get("test_id", ""),
                    row.get("confirmation_target", ""),
                    row.get("fresh_window_test", ""),
                    row.get("pass_threshold", ""),
                    row.get("live_permission", ""),
                ]
                for row in test_rows
            ],
        )
    )
    lines.extend(["", "## Active Rewrite Blockers", ""])
    lines.extend(
        _table(
            ["blocker_id", "status", "clearance_condition"],
            [[row.get("blocker_id", ""), row.get("status", ""), row.get("clearance_condition", "")] for row in blocker_rows],
        )
    )
    lines.extend(["", "## Fresh Window Queue", ""])
    lines.extend(
        _table(
            ["priority", "queue_item", "subject", "acceptance_test"],
            [
                [
                    row.get("priority", ""),
                    row.get("queue_item", ""),
                    row.get("subject", ""),
                    row.get("acceptance_test", ""),
                ]
                for row in queue_rows
            ],
        )
    )
    lines.extend(["", "## Macro Gate", ""])
    lines.extend(
        _table(
            ["finding_id", "disposition", "promotion_condition"],
            [
                [
                    row.get("finding_id", ""),
                    row.get("stage6c_disposition", ""),
                    row.get("promotion_condition", ""),
                ]
                for row in macro_gate_rows
            ],
        )
    )
    lines.extend(
        [
            "",
            "## Outputs",
            "",
            f"- protocol_json: `{safe_rel(output_paths['json'])}`",
            f"- confirmation_test_matrix: `{safe_rel(output_paths['test_matrix_csv'])}`",
            f"- threshold_contract: `{safe_rel(output_paths['threshold_contract_csv'])}`",
            f"- fresh_window_queue: `{safe_rel(output_paths['fresh_window_queue_csv'])}`",
            f"- rewrite_blockers: `{safe_rel(output_paths['rewrite_blockers_csv'])}`",
            f"- macro_review_gate: `{safe_rel(output_paths['macro_gate_csv'])}`",
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

    readback_json = _load_optional_json(inputs["readback_json"])
    scenario_decisions = _load_required_csv(inputs["scenario_decisions"], "scenario decisions")
    requirement_results = _load_required_csv(inputs["requirement_results"], "requirement results")
    guardrail_verdict = _load_required_csv(inputs["guardrail_verdict"], "guardrail verdict")
    next_actions = _load_required_csv(inputs["next_action_queue"], "next action queue")
    macro_candidates = _load_required_csv(inputs["macro_candidates"], "macro findings candidates")
    _load_required_csv(inputs["scenario_scorecard"], "scenario scorecard")
    increment_rows = _load_required_csv(inputs["increment_matrix"], "increment matrix")
    _load_required_csv(inputs["concentration_audit"], "concentration audit")

    test_rows = _test_matrix_rows(
        scenario_decisions=scenario_decisions,
        requirement_results=requirement_results,
        increment_rows=increment_rows,
        guardrails=guardrail_verdict,
    )
    threshold_rows = _threshold_contract_rows(test_rows)
    queue_rows = _fresh_window_queue_rows(next_actions, test_rows)
    blocker_rows = _rewrite_blocker_rows(test_rows, guardrail_verdict)
    macro_gate = _macro_gate_rows(macro_candidates)
    payload = {
        "stage": "6C",
        "guardrail": "read_only_no_live_scoring_candidate_generation_budget_or_legacy_changes",
        "inputs": {key: safe_rel(path) for key, path in inputs.items()},
        "readback_summary_keys": sorted(readback_json.keys()),
        "confirmation_test_count": len(test_rows),
        "active_rewrite_blocker_count": len(blocker_rows),
        "fresh_window_queue_count": len(queue_rows),
        "macro_gate_count": len(macro_gate),
        "next_stage_dependency": "Run this protocol against future/fresh Stage 6B readback evidence before any rewrite specification.",
    }

    _write_csv(outputs["test_matrix_csv"], test_rows, force=bool(args.force))
    _write_csv(outputs["threshold_contract_csv"], threshold_rows, force=bool(args.force))
    _write_csv(outputs["fresh_window_queue_csv"], queue_rows, force=bool(args.force))
    _write_csv(outputs["rewrite_blockers_csv"], blocker_rows, force=bool(args.force))
    _write_csv(outputs["macro_gate_csv"], macro_gate, force=bool(args.force))
    _write_json(outputs["json"], payload, force=bool(args.force))
    _write_text(
        outputs["md"],
        _render_md(
            test_rows=test_rows,
            threshold_rows=threshold_rows,
            queue_rows=queue_rows,
            blocker_rows=blocker_rows,
            macro_gate_rows=macro_gate,
            output_paths=outputs,
        ),
        force=bool(args.force),
    )
    print(f"[OK] Wrote Stage 6C confirmation protocol: {safe_rel(outputs['md'])}")


if __name__ == "__main__":
    main()
