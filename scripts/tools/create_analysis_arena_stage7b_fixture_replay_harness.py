#!/usr/bin/env python3
"""Create the Stage-7B fixture replay/readiness harness.

Stage 7B is read-only. It replays the Stage 6F decision atlas against the
Stage 7A fresh-window scaffold and answers whether each carry-forward item is
traceable, testable, and correctly blocked before the next fresh window. It
does not alter live scoring, candidate generation, translator logic, budget
logic, or legacy infrastructure.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Dict, List, Mapping, Sequence


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.tools.analysis_arena_window_utils import safe_rel  # type: ignore
from scripts.tools.create_analysis_arena_stage4_fixture_replay_harness import (  # type: ignore
    RUNS_2_DIR,
    _read_csv_rows,
    _resolve_path,
    _safe_float,
    _safe_int,
    _write_csv,
    _write_json,
    _write_text,
)


STAGE6C_PREFIX = "ANALYSIS_ARENA__CYCLE__STAGE6C"
STAGE6D_PREFIX = "ANALYSIS_ARENA__CYCLE__STAGE6D"
STAGE6E_PREFIX = "ANALYSIS_ARENA__CYCLE__STAGE6E"
STAGE6F_PREFIX = "ANALYSIS_ARENA__CYCLE__STAGE6F"
STAGE7A_PREFIX = "ANALYSIS_ARENA__CYCLE__STAGE7A"
STAGE7B_PREFIX = "ANALYSIS_ARENA__CYCLE__STAGE7B"


def _parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--runs2-dir", default=str(RUNS_2_DIR), help="RUNS_2 root containing Stage-6F and Stage-7A outputs.")
    ap.add_argument("--output-dir", default=str(RUNS_2_DIR), help="Cycle-level output directory.")
    ap.add_argument("--force", action="store_true", help="Overwrite existing Stage-7B outputs.")
    return ap.parse_args()


def _input_paths(runs2_dir: Path) -> Dict[str, Path]:
    return {
        "confirmation_tests": runs2_dir / f"{STAGE6C_PREFIX}_CONFIRMATION_TEST_MATRIX.csv",
        "threshold_contract": runs2_dir / f"{STAGE6C_PREFIX}_THRESHOLD_CONTRACT.csv",
        "stage6c_blockers": runs2_dir / f"{STAGE6C_PREFIX}_REWRITE_BLOCKERS.csv",
        "restraint_candidates": runs2_dir / f"{STAGE6D_PREFIX}_HIGH_PRESSURE_RESCUE_CANDIDATES.csv",
        "support_candidates": runs2_dir / f"{STAGE6E_PREFIX}_SUPPORT_NARROWING_CANDIDATES.csv",
        "lane_atlas": runs2_dir / f"{STAGE6F_PREFIX}_LANE_DECISION_ATLAS.csv",
        "stage6f_blockers": runs2_dir / f"{STAGE6F_PREFIX}_ACTIVE_BLOCKERS_AND_CLEARANCE.csv",
        "stage6f_queue": runs2_dir / f"{STAGE6F_PREFIX}_FRESH_WINDOW_CARRY_FORWARD_QUEUE.csv",
        "stage6f_macro": runs2_dir / f"{STAGE6F_PREFIX}_MACRO_FINDINGS_DISPOSITION.csv",
        "stage6f_casebook": runs2_dir / f"{STAGE6F_PREFIX}_PRIORITY_BUCKET_CASEBOOK.csv",
        "stage6f_examples": runs2_dir / f"{STAGE6F_PREFIX}_BUCKET_EXAMPLE_LEDGER.csv",
        "stage7a_requirements": runs2_dir / f"{STAGE7A_PREFIX}_CONFIRMATION_REQUIREMENTS.csv",
        "stage7a_benchmarks": runs2_dir / f"{STAGE7A_PREFIX}_MARCH_SEED_BENCHMARKS.csv",
        "stage7a_template": runs2_dir / f"{STAGE7A_PREFIX}_FUTURE_WINDOW_EVALUATION_TEMPLATE.csv",
        "stage7a_checklist": runs2_dir / f"{STAGE7A_PREFIX}_RUN_CHECKLIST.csv",
    }


def _output_paths(output_dir: Path) -> Dict[str, Path]:
    return {
        "md": output_dir / f"{STAGE7B_PREFIX}_FIXTURE_REPLAY_HARNESS.md",
        "json": output_dir / f"{STAGE7B_PREFIX}_FIXTURE_REPLAY_HARNESS.json",
        "queue_csv": output_dir / f"{STAGE7B_PREFIX}_QUEUE_REPLAY_STATUS.csv",
        "requirements_csv": output_dir / f"{STAGE7B_PREFIX}_REQUIREMENT_COVERAGE.csv",
        "blockers_csv": output_dir / f"{STAGE7B_PREFIX}_BLOCKER_RECHECK.csv",
        "casebook_csv": output_dir / f"{STAGE7B_PREFIX}_CASEBOOK_TRACEABILITY.csv",
        "ready_md": output_dir / f"{STAGE7B_PREFIX}_READY_FOR_FRESH_WINDOW.md",
    }


def _load_required_csv(path: Path, label: str) -> List[Dict[str, str]]:
    rows = _read_csv_rows(path)
    if not rows:
        raise SystemExit(f"Missing or empty Stage-7B input {label}: {safe_rel(path)}")
    return rows


def _load_optional_csv(path: Path) -> List[Dict[str, str]]:
    return _read_csv_rows(path)


def _row_by_id(rows: Sequence[Mapping[str, Any]], field: str) -> Dict[str, Mapping[str, Any]]:
    return {str(row.get(field) or ""): row for row in rows}


def _split_pipe(value: Any) -> List[str]:
    return [part.strip() for part in str(value or "").split("|") if part.strip()]


def _truth(value: bool) -> str:
    return "true" if value else "false"


def _target_family(subject: str) -> str:
    text = subject.lower()
    if "primary_restrained" in text:
        return "primary"
    if "support" in text:
        return "support"
    if "restraint" in text or "high_pressure" in text or "filter" in text:
        return "restraint"
    if "lineage" in text:
        return "lineage"
    if "decay" in text:
        return "decay"
    if "duplicate" in text or "union" in text:
        return "duplicate_credit"
    if "macro" in text:
        return "macro"
    if "translator" in text or "rewrite" in text or "scoring" in text:
        return "rewrite"
    if "concentration" in text:
        return "concentration"
    return "general"


def _canonical_requirement_target(subject: str) -> str:
    family = _target_family(subject)
    if family == "primary":
        return "primary_restrained_candidate_expression"
    if family == "support":
        return "support_context_modifier"
    if family == "restraint":
        return "restraint_soft_penalty"
    if family == "lineage":
        return "lineage_narrowing"
    if family == "decay":
        return "decay_companion_boundary"
    if family == "duplicate_credit":
        return "duplicate_credit_guardrail"
    if family == "macro":
        return "macro_findings_gate"
    if family == "rewrite":
        return "translator_scoring_rewrite_gate"
    if family == "concentration":
        return "concentration_warning_break"
    return subject


def _related_lane(
    *,
    subject: str,
    lane_by_subject: Mapping[str, Mapping[str, Any]],
    lane_by_type: Mapping[str, Mapping[str, Any]],
) -> Mapping[str, Any]:
    if subject in lane_by_subject:
        return lane_by_subject[subject]
    canonical = _canonical_requirement_target(subject)
    if canonical in lane_by_subject:
        return lane_by_subject[canonical]
    family = _target_family(subject)
    lane_type_by_family = {
        "primary": "primary_candidate_expression",
        "support": "support_modifier_narrowing",
        "restraint": "restraint_soft_penalty",
        "lineage": "broad_lineage_reference",
        "decay": "decay_companion_boundary",
        "duplicate_credit": "duplicate_credit_guardrail",
        "rewrite": "rewrite_gate",
    }
    lane_type = lane_type_by_family.get(family, "")
    return lane_by_type.get(lane_type, {})


def _related_requirement(
    *,
    subject: str,
    requirements_by_target: Mapping[str, Mapping[str, Any]],
) -> Mapping[str, Any]:
    return requirements_by_target.get(_canonical_requirement_target(subject), requirements_by_target.get(subject, {}))


def _readiness_status(
    *,
    subject: str,
    permission: str,
    has_requirement: bool,
    has_acceptance: bool,
    has_live_permission_block: bool,
    has_traceability: bool = True,
) -> str:
    family = _target_family(subject)
    permission_text = permission.lower()
    if family == "rewrite" or "blocked_until" in permission_text:
        return "blocked_by_requirements"
    if not has_requirement or not has_acceptance:
        return "needs_replay_evidence"
    if not has_live_permission_block:
        return "blocked_by_requirements"
    if not has_traceability:
        return "needs_replay_evidence"
    if "context_only" in permission_text or "companion_only" in permission_text:
        return "research_only"
    if family in {"support", "restraint", "lineage", "decay", "duplicate_credit", "macro", "concentration"}:
        return "ready_but_watch"
    return "ready_for_fresh_confirmation"


def _status_rank(status: str) -> int:
    order = {
        "ready_for_fresh_confirmation": 0,
        "ready_but_watch": 1,
        "research_only": 2,
        "needs_replay_evidence": 3,
        "blocked_by_requirements": 4,
    }
    return order.get(status, 9)


def _queue_rows(
    *,
    queue: Sequence[Mapping[str, Any]],
    requirements_by_target: Mapping[str, Mapping[str, Any]],
    lane_by_subject: Mapping[str, Mapping[str, Any]],
    lane_by_type: Mapping[str, Mapping[str, Any]],
    blockers_by_target: Mapping[str, List[Mapping[str, Any]]],
) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for item in queue:
        subject = str(item.get("subject") or "")
        requirement = _related_requirement(subject=subject, requirements_by_target=requirements_by_target)
        lane = _related_lane(subject=subject, lane_by_subject=lane_by_subject, lane_by_type=lane_by_type)
        canonical = _canonical_requirement_target(subject)
        blockers = blockers_by_target.get(canonical, [])
        acceptance = str(item.get("acceptance_or_review_test") or requirement.get("fresh_window_test") or "")
        permission = str(item.get("allowed_permission") or "")
        live_permission = str(item.get("live_permission") or "")
        status = _readiness_status(
            subject=subject,
            permission=permission,
            has_requirement=bool(requirement),
            has_acceptance=bool(acceptance),
            has_live_permission_block=live_permission in {"", "none", "forbidden"},
            has_traceability=bool(lane) or _target_family(subject) in {"macro", "concentration"},
        )
        rows.append(
            {
                "priority": _safe_int(item.get("priority")),
                "source_stage": item.get("source_stage", ""),
                "subject": subject,
                "canonical_confirmation_target": canonical,
                "related_requirement_id": requirement.get("requirement_id", ""),
                "related_stage6c_test_id": requirement.get("stage6c_test_id", ""),
                "related_lane_id": lane.get("lane_id", ""),
                "active_blockers": "|".join(str(row.get("blocker_id") or "") for row in blockers),
                "carry_forward_action": item.get("carry_forward_action", ""),
                "acceptance_or_review_test": acceptance,
                "allowed_permission": permission,
                "live_permission": live_permission,
                "replay_readiness_status": status,
                "readiness_reason": _queue_reason(status=status, requirement=requirement, lane=lane, blockers=blockers),
            }
        )
    return sorted(rows, key=lambda row: (_safe_int(row.get("priority")), str(row.get("subject") or "")))


def _queue_reason(
    *,
    status: str,
    requirement: Mapping[str, Any],
    lane: Mapping[str, Any],
    blockers: Sequence[Mapping[str, Any]],
) -> str:
    if status == "blocked_by_requirements":
        return "kept blocked until prerequisite fresh-window gates are cleared"
    if status == "needs_replay_evidence":
        return "missing requirement, acceptance test, or traceable Stage 6F lane"
    if status == "research_only":
        return "usable as context/companion research only; no candidate-pool or live permission"
    if status == "ready_but_watch":
        return f"testable with caveats; active_blockers={len(blockers)}; lane={lane.get('lane_id', '')}"
    return f"testable primary confirmation path; requirement={requirement.get('requirement_id', '')}; active_blockers={len(blockers)}"


def _requirement_rows(
    *,
    requirements: Sequence[Mapping[str, Any]],
    tests_by_id: Mapping[str, Mapping[str, Any]],
    thresholds_by_id: Mapping[str, Mapping[str, Any]],
    queue_rows: Sequence[Mapping[str, Any]],
    lane_by_subject: Mapping[str, Mapping[str, Any]],
    lane_by_type: Mapping[str, Mapping[str, Any]],
    template_rows: Sequence[Mapping[str, Any]],
    macro_rows: Sequence[Mapping[str, Any]],
) -> List[Dict[str, Any]]:
    template_targets = {
        str(row.get("requirement_id") or "") for row in template_rows if str(row.get("requirement_id") or "").startswith("S7A-REQ-")
    }
    queue_by_target: Dict[str, List[Mapping[str, Any]]] = {}
    for row in queue_rows:
        queue_by_target.setdefault(str(row.get("canonical_confirmation_target") or ""), []).append(row)

    rows: List[Dict[str, Any]] = []
    for req in requirements:
        target = str(req.get("confirmation_target") or "")
        test_id = str(req.get("stage6c_test_id") or "")
        lane = _related_lane(subject=target, lane_by_subject=lane_by_subject, lane_by_type=lane_by_type)
        related_queue = queue_by_target.get(target, [])
        active_blockers = _split_pipe(req.get("active_blockers"))
        has_test = test_id in tests_by_id
        has_threshold = test_id in thresholds_by_id
        has_template = str(req.get("requirement_id") or "") in template_targets
        has_macro = _target_family(target) != "macro" or bool(macro_rows)
        has_live_block = str(req.get("live_permission") or "") in {"", "none", "forbidden"}
        if not (has_test and has_threshold and has_template and has_live_block and has_macro):
            status = "blocked_by_requirements"
        elif _target_family(target) == "rewrite":
            status = "blocked_by_requirements"
        elif _target_family(target) == "primary":
            status = "ready_for_fresh_confirmation"
        elif not related_queue and _target_family(target) not in {"concentration", "duplicate_credit"}:
            status = "needs_replay_evidence"
        elif _target_family(target) in {"decay"}:
            status = "research_only"
        else:
            status = "ready_but_watch"
        rows.append(
            {
                "requirement_id": req.get("requirement_id", ""),
                "stage6c_test_id": test_id,
                "confirmation_target": target,
                "has_stage6c_test": _truth(has_test),
                "has_threshold_contract": _truth(has_threshold),
                "has_stage7a_template_row": _truth(has_template),
                "related_queue_count": len(related_queue),
                "related_lane_id": lane.get("lane_id", ""),
                "active_blocker_count": len(active_blockers),
                "fresh_window_test_present": _truth(bool(req.get("fresh_window_test"))),
                "pass_threshold_present": _truth(bool(req.get("pass_threshold"))),
                "repeat_contract_present": _truth(bool(req.get("repeat_contract"))),
                "live_permission": req.get("live_permission", ""),
                "coverage_status": status,
                "coverage_note": _requirement_note(status=status, target=target, related_queue=related_queue, active_blockers=active_blockers),
            }
        )
    return rows


def _requirement_note(
    *,
    status: str,
    target: str,
    related_queue: Sequence[Mapping[str, Any]],
    active_blockers: Sequence[str],
) -> str:
    if status == "blocked_by_requirements":
        return "rewrite/live permission remains blocked or required scaffold pieces are incomplete"
    if status == "needs_replay_evidence":
        return "requirement exists but lacks a carry-forward queue path"
    if status == "research_only":
        return "boundary/context evidence must remain separate from candidate-pool scoring"
    if status == "ready_but_watch":
        return f"testable with caveats; queue_paths={len(related_queue)}; active_blockers={len(active_blockers)}"
    return f"primary confirmation target is testable; active_blockers={len(active_blockers)}"


def _blocker_rows(
    *,
    blockers: Sequence[Mapping[str, Any]],
    requirements_by_test: Mapping[str, Mapping[str, Any]],
) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for blocker in blockers:
        linked_test_id = str(blocker.get("linked_test_id") or "")
        req = requirements_by_test.get(linked_test_id, {})
        current_evidence = str(blocker.get("current_evidence") or "").lower()
        if not req:
            status = "blocked_by_requirements"
        elif not blocker.get("clearance_condition") or not blocker.get("fresh_window_test"):
            status = "needs_replay_evidence"
        elif "pass" in current_evidence:
            status = "ready_but_watch"
        else:
            status = "ready_for_fresh_confirmation"
        rows.append(
            {
                "blocker_id": blocker.get("blocker_id", ""),
                "linked_test_id": linked_test_id,
                "blocks": blocker.get("blocks", ""),
                "stage7a_requirement_id": req.get("requirement_id", ""),
                "blocker_status": blocker.get("status", ""),
                "current_evidence": blocker.get("current_evidence", ""),
                "clearance_condition": blocker.get("clearance_condition", ""),
                "fresh_window_test": blocker.get("fresh_window_test", ""),
                "recheck_status": status,
                "recheck_note": _blocker_note(status=status),
                "live_permission": blocker.get("live_permission", ""),
            }
        )
    return rows


def _blocker_note(*, status: str) -> str:
    if status == "blocked_by_requirements":
        return "no matching Stage 7A requirement found; keep blocker active"
    if status == "needs_replay_evidence":
        return "missing fresh-window test or clearance condition"
    if status == "ready_but_watch":
        return "current evidence is favorable but must be rechecked on every future replay"
    return "active blocker has a clear fresh-window recheck path"


def _casebook_rows(
    *,
    casebook: Sequence[Mapping[str, Any]],
    examples: Sequence[Mapping[str, Any]],
    restraint_by_id: Mapping[str, Mapping[str, Any]],
    support_by_id: Mapping[str, Mapping[str, Any]],
    benchmarks_by_source: Mapping[str, Mapping[str, Any]],
    requirements_by_target: Mapping[str, Mapping[str, Any]],
) -> List[Dict[str, Any]]:
    example_counts = Counter(str(row.get("target_id") or "") for row in examples)
    rows: List[Dict[str, Any]] = []
    for item in casebook:
        target_id = str(item.get("target_id") or "")
        source_stage = str(item.get("source_stage") or "")
        source_candidate_id = str(item.get("source_candidate_id") or "")
        source_row = restraint_by_id.get(source_candidate_id, {}) if source_stage == "Stage6D" else support_by_id.get(source_candidate_id, {})
        requirement_target = "restraint_soft_penalty" if source_stage == "Stage6D" else "support_context_modifier"
        req = requirements_by_target.get(requirement_target, {})
        matched_rows = _safe_int(item.get("matched_ledger_rows"))
        positives = _safe_int(item.get("total_positive_conversion_event_count"))
        examples_count = example_counts[target_id]
        recommended_use = str(item.get("recommended_use") or "")
        strict_candidate = recommended_use in {
            "high_pressure_rescue_candidate_soft_penalty_only",
            "narrow_support_modifier_candidate",
        }
        if not source_row or matched_rows <= 0 or examples_count <= 0:
            status = "needs_replay_evidence"
        elif strict_candidate and positives > 0 and req:
            status = "ready_but_watch"
        else:
            status = "research_only"
        rows.append(
            {
                "target_id": target_id,
                "source_stage": source_stage,
                "source_candidate_id": source_candidate_id,
                "source_candidate_found": _truth(bool(source_row)),
                "bucket_id": item.get("bucket_id", ""),
                "recommended_use": recommended_use,
                "related_requirement_id": req.get("requirement_id", ""),
                "benchmark_id": benchmarks_by_source.get(source_candidate_id, {}).get("benchmark_id", ""),
                "matched_ledger_rows": matched_rows,
                "example_rows": examples_count,
                "positive_conversion_event_count": positives,
                "casebook_fp_proxy_rate": _safe_float(item.get("casebook_fp_proxy_rate")),
                "casebook_positive_yield": _safe_float(item.get("casebook_positive_yield")),
                "traceability_status": status,
                "traceability_note": _casebook_note(status=status, strict_candidate=strict_candidate, positives=positives),
                "live_permission": item.get("live_permission", ""),
            }
        )
    return rows


def _casebook_note(*, status: str, strict_candidate: bool, positives: int) -> str:
    if status == "needs_replay_evidence":
        return "missing source candidate, matched ledger rows, or example rows"
    if status == "ready_but_watch":
        return "strict research candidate with positive March evidence; retest on fresh window before any influence"
    if strict_candidate and positives <= 0:
        return "strict candidate lacks positive conversion count in casebook rollup"
    return "casebook evidence is useful for review but not a promotion candidate"


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


def _status_counts(rows: Sequence[Mapping[str, Any]], field: str) -> Dict[str, int]:
    return dict(Counter(str(row.get(field) or "") for row in rows))


def _worst_status(rows: Sequence[Mapping[str, Any]], field: str) -> str:
    statuses = [str(row.get(field) or "") for row in rows]
    return max(statuses, key=_status_rank) if statuses else "missing"


def _render_md(
    *,
    queue_rows: Sequence[Mapping[str, Any]],
    requirement_rows: Sequence[Mapping[str, Any]],
    blocker_rows: Sequence[Mapping[str, Any]],
    casebook_rows: Sequence[Mapping[str, Any]],
    output_paths: Mapping[str, Path],
) -> str:
    queue_counts = _status_counts(queue_rows, "replay_readiness_status")
    req_counts = _status_counts(requirement_rows, "coverage_status")
    blocker_counts = _status_counts(blocker_rows, "recheck_status")
    casebook_counts = _status_counts(casebook_rows, "traceability_status")
    ready_queue = [row for row in queue_rows if row.get("replay_readiness_status") in {"ready_for_fresh_confirmation", "ready_but_watch"}]
    blocked_queue = [row for row in queue_rows if row.get("replay_readiness_status") == "blocked_by_requirements"]

    lines: List[str] = [
        "# Analysis Arena Stage 7B Fixture Replay Harness",
        "",
        "## Guardrail",
        "",
        "Stage 7B is read-only. It replays the Stage 6F decision atlas against the Stage 7A fresh-window scaffold. It does not change live scoring, candidate generation, translator logic, budget logic, or legacy infrastructure.",
        "",
        "## Executive Readback",
        "",
        f"- queue rows replayed: `{len(queue_rows)}`",
        f"- requirement coverage rows: `{len(requirement_rows)}`",
        f"- blocker recheck rows: `{len(blocker_rows)}`",
        f"- casebook traceability rows: `{len(casebook_rows)}`",
        f"- queue readiness counts: `{json.dumps(queue_counts, sort_keys=True)}`",
        f"- requirement coverage counts: `{json.dumps(req_counts, sort_keys=True)}`",
        f"- blocker recheck counts: `{json.dumps(blocker_counts, sort_keys=True)}`",
        f"- casebook traceability counts: `{json.dumps(casebook_counts, sort_keys=True)}`",
        "- Fresh-window replay can proceed; scoring rewrite remains blocked until future evidence clears or quarantines the open gates.",
        "",
        "## Queue Replay Status",
        "",
    ]
    lines.extend(
        _table(
            ["priority", "subject", "requirement", "lane", "status"],
            [
                [
                    row.get("priority", ""),
                    row.get("subject", ""),
                    row.get("related_requirement_id", ""),
                    row.get("related_lane_id", ""),
                    row.get("replay_readiness_status", ""),
                ]
                for row in queue_rows
            ],
        )
    )
    lines.extend(["", "## Requirement Coverage", ""])
    lines.extend(
        _table(
            ["requirement", "target", "queue_count", "lane", "status"],
            [
                [
                    row.get("requirement_id", ""),
                    row.get("confirmation_target", ""),
                    row.get("related_queue_count", ""),
                    row.get("related_lane_id", ""),
                    row.get("coverage_status", ""),
                ]
                for row in requirement_rows
            ],
        )
    )
    lines.extend(["", "## Blocker Recheck", ""])
    lines.extend(
        _table(
            ["blocker", "requirement", "blocks", "status"],
            [
                [
                    row.get("blocker_id", ""),
                    row.get("stage7a_requirement_id", ""),
                    row.get("blocks", ""),
                    row.get("recheck_status", ""),
                ]
                for row in blocker_rows
            ],
        )
    )
    lines.extend(["", "## Highest-Priority Casebook Traceability", ""])
    lines.extend(
        _table(
            ["target", "candidate", "requirement", "examples", "status"],
            [
                [
                    row.get("target_id", ""),
                    row.get("source_candidate_id", ""),
                    row.get("related_requirement_id", ""),
                    row.get("example_rows", ""),
                    row.get("traceability_status", ""),
                ]
                for row in casebook_rows[:12]
            ],
        )
    )
    lines.extend(
        [
            "",
            "## Fresh-Window Operating Readback",
            "",
            f"- Ready or watch-list queue items: `{len(ready_queue)}`",
            f"- Blocked queue items: `{len(blocked_queue)}`",
            f"- Worst requirement status: `{_worst_status(requirement_rows, 'coverage_status')}`",
            f"- Worst casebook status: `{_worst_status(casebook_rows, 'traceability_status')}`",
            "- Operational meaning: use Stage 7B as the pre-flight map for the next fresh window. Do not use it as permission to rewrite scoring.",
            "",
            "## Outputs",
            "",
            f"- harness_json: `{safe_rel(output_paths['json'])}`",
            f"- queue_replay_status: `{safe_rel(output_paths['queue_csv'])}`",
            f"- requirement_coverage: `{safe_rel(output_paths['requirements_csv'])}`",
            f"- blocker_recheck: `{safe_rel(output_paths['blockers_csv'])}`",
            f"- casebook_traceability: `{safe_rel(output_paths['casebook_csv'])}`",
            f"- ready_for_fresh_window: `{safe_rel(output_paths['ready_md'])}`",
            "",
        ]
    )
    return "\n".join(lines)


def _render_ready_md(
    *,
    queue_rows: Sequence[Mapping[str, Any]],
    requirement_rows: Sequence[Mapping[str, Any]],
    blocker_rows: Sequence[Mapping[str, Any]],
    casebook_rows: Sequence[Mapping[str, Any]],
) -> str:
    ready = [row for row in queue_rows if row.get("replay_readiness_status") == "ready_for_fresh_confirmation"]
    watch = [row for row in queue_rows if row.get("replay_readiness_status") == "ready_but_watch"]
    blocked = [row for row in queue_rows if row.get("replay_readiness_status") == "blocked_by_requirements"]
    research = [row for row in queue_rows if row.get("replay_readiness_status") == "research_only"]
    missing = [row for row in queue_rows if row.get("replay_readiness_status") == "needs_replay_evidence"]
    casebook_watch = [row for row in casebook_rows if row.get("traceability_status") == "ready_but_watch"]

    lines: List[str] = [
        "# Stage 7B Ready-For-Fresh-Window Readback",
        "",
        "## Bottom Line",
        "",
        "The next fresh window is ready for read-only confirmation replay, not for live scoring or candidate-generation changes.",
        "",
        "## Replay Permissions",
        "",
        f"- `ready_for_fresh_confirmation`: {len(ready)} queue item(s)",
        f"- `ready_but_watch`: {len(watch)} queue item(s)",
        f"- `research_only`: {len(research)} queue item(s)",
        f"- `needs_replay_evidence`: {len(missing)} queue item(s)",
        f"- `blocked_by_requirements`: {len(blocked)} queue item(s)",
        f"- casebook watch targets: {len(casebook_watch)}",
        "",
        "## Allowed Next Action",
        "",
        "Run the next fresh-window cadence, then rerun Stage 6B through Stage 7B and compare these March seed statuses against the future evidence.",
        "",
        "## Explicitly Not Allowed",
        "",
        "- No live scoring rewrite.",
        "- No candidate-generation rewrite.",
        "- No budget rewrite.",
        "- No hard restraint veto.",
        "- No broad support promotion.",
        "- No decay conversion into candidate-pool spend evidence.",
        "",
        "## First Items To Inspect After Fresh Window",
        "",
    ]
    lines.extend(
        _table(
            ["priority", "subject", "requirement", "status"],
            [
                [
                    row.get("priority", ""),
                    row.get("subject", ""),
                    row.get("related_requirement_id", ""),
                    row.get("replay_readiness_status", ""),
                ]
                for row in list(ready) + list(watch)
            ],
        )
    )
    lines.extend(["", "## Blockers That Must Stay Visible", ""])
    lines.extend(
        _table(
            ["blocker", "requirement", "fresh test"],
            [
                [
                    row.get("blocker_id", ""),
                    row.get("stage7a_requirement_id", ""),
                    row.get("fresh_window_test", ""),
                ]
                for row in blocker_rows
            ],
        )
    )
    lines.extend(["", "## Requirement Coverage Snapshot", ""])
    lines.extend(
        _table(
            ["requirement", "target", "status", "note"],
            [
                [
                    row.get("requirement_id", ""),
                    row.get("confirmation_target", ""),
                    row.get("coverage_status", ""),
                    row.get("coverage_note", ""),
                ]
                for row in requirement_rows
            ],
        )
    )
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    args = _parse_args()
    runs2_dir = _resolve_path(args.runs2_dir)
    output_dir = _resolve_path(args.output_dir)
    inputs = _input_paths(runs2_dir)
    outputs = _output_paths(output_dir)

    confirmation_tests = _load_required_csv(inputs["confirmation_tests"], "Stage 6C confirmation tests")
    threshold_contract = _load_required_csv(inputs["threshold_contract"], "Stage 6C threshold contract")
    _load_required_csv(inputs["stage6c_blockers"], "Stage 6C rewrite blockers")
    restraint_candidates = _load_optional_csv(inputs["restraint_candidates"])
    support_candidates = _load_optional_csv(inputs["support_candidates"])
    lane_atlas = _load_required_csv(inputs["lane_atlas"], "Stage 6F lane atlas")
    stage6f_blockers = _load_required_csv(inputs["stage6f_blockers"], "Stage 6F blockers")
    stage6f_queue = _load_required_csv(inputs["stage6f_queue"], "Stage 6F carry-forward queue")
    stage6f_macro = _load_required_csv(inputs["stage6f_macro"], "Stage 6F macro disposition")
    stage6f_casebook = _load_optional_csv(inputs["stage6f_casebook"])
    stage6f_examples = _load_optional_csv(inputs["stage6f_examples"])
    stage7a_requirements = _load_required_csv(inputs["stage7a_requirements"], "Stage 7A requirements")
    stage7a_benchmarks = _load_required_csv(inputs["stage7a_benchmarks"], "Stage 7A benchmarks")
    stage7a_template = _load_required_csv(inputs["stage7a_template"], "Stage 7A future template")
    _load_required_csv(inputs["stage7a_checklist"], "Stage 7A checklist")

    tests_by_id = _row_by_id(confirmation_tests, "test_id")
    thresholds_by_id = _row_by_id(threshold_contract, "contract_id")
    requirements_by_target = _row_by_id(stage7a_requirements, "confirmation_target")
    requirements_by_test = _row_by_id(stage7a_requirements, "stage6c_test_id")
    lane_by_subject = _row_by_id(lane_atlas, "source_subject")
    lane_by_type = _row_by_id(lane_atlas, "lane_type")
    restraint_by_id = _row_by_id(restraint_candidates, "candidate_id")
    support_by_id = _row_by_id(support_candidates, "candidate_id")
    benchmarks_by_source = _row_by_id(stage7a_benchmarks, "source_id")

    blockers_by_target: Dict[str, List[Mapping[str, Any]]] = {}
    for blocker in stage6f_blockers:
        req = requirements_by_test.get(str(blocker.get("linked_test_id") or ""), {})
        target = str(req.get("confirmation_target") or blocker.get("blocks") or "")
        blockers_by_target.setdefault(target, []).append(blocker)

    queue_status = _queue_rows(
        queue=stage6f_queue,
        requirements_by_target=requirements_by_target,
        lane_by_subject=lane_by_subject,
        lane_by_type=lane_by_type,
        blockers_by_target=blockers_by_target,
    )
    requirement_coverage = _requirement_rows(
        requirements=stage7a_requirements,
        tests_by_id=tests_by_id,
        thresholds_by_id=thresholds_by_id,
        queue_rows=queue_status,
        lane_by_subject=lane_by_subject,
        lane_by_type=lane_by_type,
        template_rows=stage7a_template,
        macro_rows=stage6f_macro,
    )
    blocker_recheck = _blocker_rows(blockers=stage6f_blockers, requirements_by_test=requirements_by_test)
    casebook_traceability = _casebook_rows(
        casebook=stage6f_casebook,
        examples=stage6f_examples,
        restraint_by_id=restraint_by_id,
        support_by_id=support_by_id,
        benchmarks_by_source=benchmarks_by_source,
        requirements_by_target=requirements_by_target,
    )

    payload = {
        "stage": "7B",
        "guardrail": "read_only_fixture_replay_readiness_no_live_permission",
        "inputs": {key: safe_rel(path) for key, path in inputs.items()},
        "queue_row_count": len(queue_status),
        "requirement_row_count": len(requirement_coverage),
        "blocker_row_count": len(blocker_recheck),
        "casebook_row_count": len(casebook_traceability),
        "optional_empty_inputs": {
            "restraint_candidate_rows": len(restraint_candidates),
            "support_candidate_rows": len(support_candidates),
            "stage6f_casebook_rows": len(stage6f_casebook),
            "stage6f_example_rows": len(stage6f_examples),
            "interpretation": "Zero rows are valid when Run 2 exposes no optional rescue/support/casebook targets.",
        },
        "queue_status_counts": _status_counts(queue_status, "replay_readiness_status"),
        "requirement_status_counts": _status_counts(requirement_coverage, "coverage_status"),
        "blocker_status_counts": _status_counts(blocker_recheck, "recheck_status"),
        "casebook_status_counts": _status_counts(casebook_traceability, "traceability_status"),
        "fresh_window_replay_status": "ready_for_read_only_confirmation_replay",
        "scoring_rewrite_status": "blocked_until_future_confirmation",
    }

    _write_csv(outputs["queue_csv"], queue_status, force=bool(args.force))
    _write_csv(outputs["requirements_csv"], requirement_coverage, force=bool(args.force))
    _write_csv(outputs["blockers_csv"], blocker_recheck, force=bool(args.force))
    _write_csv(outputs["casebook_csv"], casebook_traceability, force=bool(args.force))
    _write_json(outputs["json"], payload, force=bool(args.force))
    _write_text(
        outputs["ready_md"],
        _render_ready_md(
            queue_rows=queue_status,
            requirement_rows=requirement_coverage,
            blocker_rows=blocker_recheck,
            casebook_rows=casebook_traceability,
        ),
        force=bool(args.force),
    )
    _write_text(
        outputs["md"],
        _render_md(
            queue_rows=queue_status,
            requirement_rows=requirement_coverage,
            blocker_rows=blocker_recheck,
            casebook_rows=casebook_traceability,
            output_paths=outputs,
        ),
        force=bool(args.force),
    )
    print(f"[OK] Wrote Stage 7B fixture replay harness: {safe_rel(outputs['md'])}")


if __name__ == "__main__":
    main()
