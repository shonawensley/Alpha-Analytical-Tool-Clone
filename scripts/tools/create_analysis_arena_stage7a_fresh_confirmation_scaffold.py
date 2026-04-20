#!/usr/bin/env python3
"""Create the Stage-7A fresh-window confirmation scaffold.

Stage 7A is read-only. It converts Stage 6C and Stage 6F decisions into a
machine-readable scaffold for the next future/fresh window. It does not require
future data yet, and it does not alter live scoring, candidate generation,
translator logic, budget logic, or legacy infrastructure.
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


STAGE6B_READBACK_PREFIX = "ANALYSIS_ARENA__CYCLE__STAGE6B_READBACK"
STAGE6C_PREFIX = "ANALYSIS_ARENA__CYCLE__STAGE6C"
STAGE6D_PREFIX = "ANALYSIS_ARENA__CYCLE__STAGE6D"
STAGE6E_PREFIX = "ANALYSIS_ARENA__CYCLE__STAGE6E"
STAGE6F_PREFIX = "ANALYSIS_ARENA__CYCLE__STAGE6F"
STAGE7A_PREFIX = "ANALYSIS_ARENA__CYCLE__STAGE7A"


def _parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--runs2-dir", default=str(RUNS_2_DIR), help="RUNS_2 root containing Stage-6C and Stage-6F outputs.")
    ap.add_argument("--output-dir", default=str(RUNS_2_DIR), help="Cycle-level output directory.")
    ap.add_argument("--force", action="store_true", help="Overwrite existing Stage-7A outputs.")
    return ap.parse_args()


def _input_paths(runs2_dir: Path) -> Dict[str, Path]:
    return {
        "scenario_decisions": runs2_dir / f"{STAGE6B_READBACK_PREFIX}_SCENARIO_DECISIONS.csv",
        "confirmation_tests": runs2_dir / f"{STAGE6C_PREFIX}_CONFIRMATION_TEST_MATRIX.csv",
        "threshold_contract": runs2_dir / f"{STAGE6C_PREFIX}_THRESHOLD_CONTRACT.csv",
        "rewrite_blockers": runs2_dir / f"{STAGE6C_PREFIX}_REWRITE_BLOCKERS.csv",
        "restraint_rescue": runs2_dir / f"{STAGE6D_PREFIX}_HIGH_PRESSURE_RESCUE_CANDIDATES.csv",
        "support_candidates": runs2_dir / f"{STAGE6E_PREFIX}_SUPPORT_NARROWING_CANDIDATES.csv",
        "lane_atlas": runs2_dir / f"{STAGE6F_PREFIX}_LANE_DECISION_ATLAS.csv",
        "stage6f_blockers": runs2_dir / f"{STAGE6F_PREFIX}_ACTIVE_BLOCKERS_AND_CLEARANCE.csv",
        "stage6f_queue": runs2_dir / f"{STAGE6F_PREFIX}_FRESH_WINDOW_CARRY_FORWARD_QUEUE.csv",
        "stage6f_macro": runs2_dir / f"{STAGE6F_PREFIX}_MACRO_FINDINGS_DISPOSITION.csv",
        "stage6f_casebook": runs2_dir / f"{STAGE6F_PREFIX}_PRIORITY_BUCKET_CASEBOOK.csv",
    }


def _output_paths(output_dir: Path) -> Dict[str, Path]:
    return {
        "md": output_dir / f"{STAGE7A_PREFIX}_FRESH_CONFIRMATION_SCAFFOLD.md",
        "json": output_dir / f"{STAGE7A_PREFIX}_FRESH_CONFIRMATION_SCAFFOLD.json",
        "requirements_csv": output_dir / f"{STAGE7A_PREFIX}_CONFIRMATION_REQUIREMENTS.csv",
        "benchmarks_csv": output_dir / f"{STAGE7A_PREFIX}_MARCH_SEED_BENCHMARKS.csv",
        "template_csv": output_dir / f"{STAGE7A_PREFIX}_FUTURE_WINDOW_EVALUATION_TEMPLATE.csv",
        "checklist_csv": output_dir / f"{STAGE7A_PREFIX}_RUN_CHECKLIST.csv",
    }


def _load_required_csv(path: Path, label: str) -> List[Dict[str, str]]:
    rows = _read_csv_rows(path)
    if not rows:
        raise SystemExit(f"Missing or empty Stage-7A input {label}: {safe_rel(path)}")
    return rows


def _row_by_id(rows: Sequence[Mapping[str, Any]], field: str) -> Dict[str, Mapping[str, Any]]:
    return {str(row.get(field) or ""): row for row in rows}


def _blockers_for_test(blockers: Sequence[Mapping[str, Any]], test_id: str) -> str:
    return "|".join(str(row.get("blocker_id") or "") for row in blockers if str(row.get("linked_test_id") or "") == test_id)


def _requirement_rows(
    *,
    tests: Sequence[Mapping[str, Any]],
    thresholds: Sequence[Mapping[str, Any]],
    blockers: Sequence[Mapping[str, Any]],
    lane_atlas: Sequence[Mapping[str, Any]],
) -> List[Dict[str, Any]]:
    thresholds_by_id = _row_by_id(thresholds, "contract_id")
    lanes_by_subject = _row_by_id(lane_atlas, "source_subject")
    rows: List[Dict[str, Any]] = []
    for idx, test in enumerate(tests, start=1):
        test_id = str(test.get("test_id") or "")
        subject = str(test.get("confirmation_target") or "")
        threshold = thresholds_by_id.get(test_id, {})
        lane = lanes_by_subject.get(subject, {})
        rows.append(
            {
                "requirement_id": f"S7A-REQ-{idx:03d}",
                "stage6c_test_id": test_id,
                "confirmation_target": subject,
                "source_stage6b_evidence": test.get("current_march_evidence", ""),
                "current_threshold_result": test.get("current_threshold_result", ""),
                "fresh_window_test": test.get("fresh_window_test", ""),
                "pass_threshold": threshold.get("metric_contract", test.get("pass_threshold", "")),
                "repeat_contract": threshold.get("repeat_contract", test.get("minimum_repeat_requirement", "")),
                "active_blockers": _blockers_for_test(blockers, test_id),
                "fresh_window_artifacts_required": _required_artifacts_for(subject),
                "evaluation_status": "pending_future_window",
                "permission_if_met": threshold.get("permission_if_met", test.get("allowed_if_pass", "")),
                "permission_if_not_met": threshold.get("permission_if_not_met", test.get("blocked_if_fail", "")),
                "current_lane_posture": lane.get("decision_posture", ""),
                "live_permission": "none",
            }
        )
    return rows


def _required_artifacts_for(subject: str) -> str:
    base = "Stage6B replay/readback; Stage6C confirmation protocol; Stage6F decision atlas"
    if "support" in subject:
        return base + "; Stage6E support narrowing workbench"
    if "restraint" in subject:
        return base + "; Stage6D restraint calibration workbench"
    if "macro" in subject:
        return base + "; Stage6F macro findings disposition"
    return base


def _scenario_metric(row: Mapping[str, Any]) -> str:
    if not row:
        return "missing"
    return (
        f"fp={_pct(row.get('false_positive_proxy_rate'))}; "
        f"yield={_fmt(row.get('pool_normalized_positive_yield'))}; "
        f"positive={_safe_int(row.get('positive_conversion_event_count'))}; "
        f"state_days={_safe_int(row.get('active_state_days'))}"
    )


def _benchmark_rows(
    *,
    scenarios: Sequence[Mapping[str, Any]],
    restraint_rescue: Sequence[Mapping[str, Any]],
    support_candidates: Sequence[Mapping[str, Any]],
    casebook_rows: Sequence[Mapping[str, Any]],
) -> List[Dict[str, Any]]:
    scenarios_by_id = _row_by_id(scenarios, "scenario_id")
    rows: List[Dict[str, Any]] = []
    for scenario_id in (
        "baseline_clean_boxed",
        "primary_restrained_candidate_expression",
        "secondary_lineage_supported_restrained",
        "broad_lineage_foundation_reference",
        "decay_watch_companion_excluded",
    ):
        scenario = scenarios_by_id.get(scenario_id, {})
        rows.append(
            {
                "benchmark_id": f"S7A-BENCH-{len(rows) + 1:03d}",
                "benchmark_type": "stage6b_scenario",
                "source_id": scenario_id,
                "subject": scenario.get("scenario_role", ""),
                "march_metric_summary": _scenario_metric(scenario),
                "recommended_future_comparison": "compare same scenario on future/fresh Stage 6B replay",
                "allowed_permission": scenario.get("allowed_permission", "none"),
                "live_permission": "none",
            }
        )
    for row in restraint_rescue[:5]:
        rows.append(
            {
                "benchmark_id": f"S7A-BENCH-{len(rows) + 1:03d}",
                "benchmark_type": "stage6d_restraint_bucket",
                "source_id": row.get("candidate_id", ""),
                "subject": row.get("bucket_id", ""),
                "march_metric_summary": f"fp={_pct(row.get('false_positive_proxy_rate'))}; yield={_fmt(row.get('pool_normalized_positive_yield'))}; positive={_safe_int(row.get('positive_conversion_event_count'))}",
                "recommended_future_comparison": "repeat bucket under Stage 6D and compare FP/yield/positive conversion stability",
                "allowed_permission": "penalty_research_only",
                "live_permission": "none",
            }
        )
    for row in support_candidates[:5]:
        rows.append(
            {
                "benchmark_id": f"S7A-BENCH-{len(rows) + 1:03d}",
                "benchmark_type": "stage6e_support_bucket",
                "source_id": row.get("candidate_id", ""),
                "subject": row.get("bucket_id", ""),
                "march_metric_summary": f"fp={_pct(row.get('false_positive_proxy_rate'))}; yield={_fmt(row.get('pool_normalized_positive_yield'))}; positive={_safe_int(row.get('positive_conversion_event_count'))}; fp_delta_peer={_fmt(row.get('false_positive_delta_vs_peer'))}",
                "recommended_future_comparison": "repeat paired support-on/support-off peer test under Stage 6E",
                "allowed_permission": "support_research_only",
                "live_permission": "none",
            }
        )
    for row in casebook_rows[:5]:
        rows.append(
            {
                "benchmark_id": f"S7A-BENCH-{len(rows) + 1:03d}",
                "benchmark_type": "stage6f_casebook_target",
                "source_id": row.get("target_id", ""),
                "subject": row.get("bucket_id", ""),
                "march_metric_summary": f"fp={_pct(row.get('casebook_fp_proxy_rate'))}; yield={_fmt(row.get('casebook_positive_yield'))}; positive={_safe_int(row.get('total_positive_conversion_event_count'))}; rows={_safe_int(row.get('matched_ledger_rows'))}",
                "recommended_future_comparison": "rerun casebook target extraction after future/fresh Stage 6F",
                "allowed_permission": "casebook_review_only",
                "live_permission": "none",
            }
        )
    return rows


def _template_rows(requirements: Sequence[Mapping[str, Any]], benchmarks: Sequence[Mapping[str, Any]]) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for req in requirements:
        rows.append(
            {
                "future_window_id": "",
                "future_window_start": "",
                "future_window_end": "",
                "requirement_id": req.get("requirement_id", ""),
                "confirmation_target": req.get("confirmation_target", ""),
                "future_metric_summary": "",
                "future_threshold_result": "",
                "pass_fail": "pending",
                "blocker_cleared": "pending",
                "repeat_confirmed": "pending",
                "notes": "",
            }
        )
    for bench in benchmarks:
        rows.append(
            {
                "future_window_id": "",
                "future_window_start": "",
                "future_window_end": "",
                "requirement_id": bench.get("benchmark_id", ""),
                "confirmation_target": bench.get("source_id", ""),
                "future_metric_summary": "",
                "future_threshold_result": "",
                "pass_fail": "benchmark_pending",
                "blocker_cleared": "n/a",
                "repeat_confirmed": "pending",
                "notes": f"Benchmark source: {bench.get('benchmark_type', '')}",
            }
        )
    return rows


def _checklist_rows(requirements: Sequence[Mapping[str, Any]]) -> List[Dict[str, Any]]:
    return [
        {
            "step": 1,
            "check": "Run normal fresh-window cadence and close the window artifacts.",
            "required_before": "Stage 7A evaluation",
            "status": "pending_future_window",
        },
        {
            "step": 2,
            "check": "Run Stage 3 through Stage 6B readback on the fresh evidence.",
            "required_before": "Stage 7A evaluation",
            "status": "pending_future_window",
        },
        {
            "step": 3,
            "check": "Run Stage 6C, Stage 6D, Stage 6E, and Stage 6F on the fresh evidence.",
            "required_before": "Stage 7A evaluation",
            "status": "pending_future_window",
        },
        {
            "step": 4,
            "check": f"Evaluate {len(requirements)} Stage 7A confirmation requirements against the future window.",
            "required_before": "rewrite discussion",
            "status": "pending_future_window",
        },
        {
            "step": 5,
            "check": "Keep live scoring, candidate-generation, budget, support, restraint, and decay permissions blocked unless explicitly cleared by future readback.",
            "required_before": "any rewrite specification",
            "status": "always_required",
        },
    ]


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
    requirements: Sequence[Mapping[str, Any]],
    benchmarks: Sequence[Mapping[str, Any]],
    template_rows: Sequence[Mapping[str, Any]],
    checklist: Sequence[Mapping[str, Any]],
    output_paths: Mapping[str, Path],
) -> str:
    lines: List[str] = [
        "# Analysis Arena Stage 7A Fresh Confirmation Scaffold",
        "",
        "## Guardrail",
        "",
        "Stage 7A is read-only. It prepares future/fresh-window evaluation rows from Stage 6C and Stage 6F evidence; it does not change live scoring, candidate generation, translator logic, budget logic, or legacy infrastructure.",
        "",
        "## Executive Readback",
        "",
        f"- confirmation requirements: `{len(requirements)}`",
        f"- March seed benchmarks: `{len(benchmarks)}`",
        f"- future-window template rows: `{len(template_rows)}`",
        "- Nothing in this scaffold confirms a fresh-window result yet. It defines what the next fresh window must prove.",
        "",
        "## Confirmation Requirements",
        "",
    ]
    lines.extend(
        _table(
            ["requirement_id", "target", "pass_threshold", "active_blockers"],
            [
                [
                    row.get("requirement_id", ""),
                    row.get("confirmation_target", ""),
                    row.get("pass_threshold", ""),
                    row.get("active_blockers", ""),
                ]
                for row in requirements
            ],
        )
    )
    lines.extend(["", "## March Seed Benchmarks", ""])
    lines.extend(
        _table(
            ["benchmark_id", "type", "source_id", "metrics"],
            [
                [
                    row.get("benchmark_id", ""),
                    row.get("benchmark_type", ""),
                    row.get("source_id", ""),
                    row.get("march_metric_summary", ""),
                ]
                for row in benchmarks[:15]
            ],
        )
    )
    lines.extend(["", "## Run Checklist", ""])
    lines.extend(
        _table(
            ["step", "check", "status"],
            [[row.get("step", ""), row.get("check", ""), row.get("status", "")] for row in checklist],
        )
    )
    lines.extend(
        [
            "",
            "## Outputs",
            "",
            f"- scaffold_json: `{safe_rel(output_paths['json'])}`",
            f"- confirmation_requirements: `{safe_rel(output_paths['requirements_csv'])}`",
            f"- march_seed_benchmarks: `{safe_rel(output_paths['benchmarks_csv'])}`",
            f"- future_window_evaluation_template: `{safe_rel(output_paths['template_csv'])}`",
            f"- run_checklist: `{safe_rel(output_paths['checklist_csv'])}`",
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

    scenarios = _load_required_csv(inputs["scenario_decisions"], "Stage 6B scenario decisions")
    confirmation_tests = _load_required_csv(inputs["confirmation_tests"], "Stage 6C confirmation tests")
    threshold_contract = _load_required_csv(inputs["threshold_contract"], "Stage 6C threshold contract")
    rewrite_blockers = _load_required_csv(inputs["rewrite_blockers"], "Stage 6C rewrite blockers")
    restraint_rescue = _load_required_csv(inputs["restraint_rescue"], "Stage 6D restraint rescue")
    support_candidates = _load_required_csv(inputs["support_candidates"], "Stage 6E support candidates")
    lane_atlas = _load_required_csv(inputs["lane_atlas"], "Stage 6F lane atlas")
    stage6f_blockers = _load_required_csv(inputs["stage6f_blockers"], "Stage 6F blockers")
    _load_required_csv(inputs["stage6f_queue"], "Stage 6F fresh queue")
    _load_required_csv(inputs["stage6f_macro"], "Stage 6F macro disposition")
    stage6f_casebook = _load_required_csv(inputs["stage6f_casebook"], "Stage 6F casebook")

    requirements = _requirement_rows(
        tests=confirmation_tests,
        thresholds=threshold_contract,
        blockers=stage6f_blockers or rewrite_blockers,
        lane_atlas=lane_atlas,
    )
    benchmarks = _benchmark_rows(
        scenarios=scenarios,
        restraint_rescue=restraint_rescue,
        support_candidates=support_candidates,
        casebook_rows=stage6f_casebook,
    )
    template_rows = _template_rows(requirements, benchmarks)
    checklist = _checklist_rows(requirements)
    payload = {
        "stage": "7A",
        "guardrail": "read_only_future_confirmation_scaffold_no_live_permission",
        "inputs": {key: safe_rel(path) for key, path in inputs.items()},
        "confirmation_requirement_count": len(requirements),
        "march_seed_benchmark_count": len(benchmarks),
        "future_template_row_count": len(template_rows),
        "checklist_count": len(checklist),
        "status": "pending_future_window",
        "next_stage_dependency": "Populate the template after a future/fresh window reruns Stage 6B through Stage 6F.",
    }

    _write_csv(outputs["requirements_csv"], requirements, force=bool(args.force))
    _write_csv(outputs["benchmarks_csv"], benchmarks, force=bool(args.force))
    _write_csv(outputs["template_csv"], template_rows, force=bool(args.force))
    _write_csv(outputs["checklist_csv"], checklist, force=bool(args.force))
    _write_json(outputs["json"], payload, force=bool(args.force))
    _write_text(
        outputs["md"],
        _render_md(
            requirements=requirements,
            benchmarks=benchmarks,
            template_rows=template_rows,
            checklist=checklist,
            output_paths=outputs,
        ),
        force=bool(args.force),
    )
    print(f"[OK] Wrote Stage 7A fresh confirmation scaffold: {safe_rel(outputs['md'])}")


if __name__ == "__main__":
    main()
