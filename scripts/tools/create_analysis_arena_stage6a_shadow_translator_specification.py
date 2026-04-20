#!/usr/bin/env python3
"""Create the Stage-6A Analysis Arena shadow translator specification.

Stage 6A is a read-only specification layer. It consumes the Stage-5 readback
decision memo and converts it into a formal shadow translator contract for the
next replay/simulation layer. It does not alter live scoring, candidate
generation, translator logic, budget logic, or legacy infrastructure.
"""

from __future__ import annotations

import argparse
import json
import sys
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
STAGE5_READBACK_PREFIX = "ANALYSIS_ARENA__CYCLE__STAGE5_READBACK"


def _parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--runs2-dir", default=str(RUNS_2_DIR), help="RUNS_2 root containing Stage-5 readback outputs.")
    ap.add_argument("--output-dir", default=str(RUNS_2_DIR), help="Cycle-level output directory.")
    ap.add_argument("--force", action="store_true", help="Overwrite existing Stage-6A outputs.")
    return ap.parse_args()


def _input_paths(runs2_dir: Path) -> Dict[str, Path]:
    return {
        "readback_md": runs2_dir / f"{STAGE5_READBACK_PREFIX}_DECISION_MEMO.md",
        "readback_json": runs2_dir / f"{STAGE5_READBACK_PREFIX}_DECISION_MEMO.json",
        "mode_decisions": runs2_dir / f"{STAGE5_READBACK_PREFIX}_MODE_DECISIONS.csv",
        "next_actions": runs2_dir / f"{STAGE5_READBACK_PREFIX}_NEXT_ACTION_QUEUE.csv",
    }


def _output_paths(output_dir: Path) -> Dict[str, Path]:
    return {
        "md": output_dir / f"{STAGE6A_PREFIX}_SHADOW_TRANSLATOR_SPECIFICATION.md",
        "json": output_dir / f"{STAGE6A_PREFIX}_SHADOW_TRANSLATOR_SPECIFICATION.json",
        "lane_contract_csv": output_dir / f"{STAGE6A_PREFIX}_LANE_CONTRACT.csv",
        "guardrail_csv": output_dir / f"{STAGE6A_PREFIX}_GUARDRAIL_MATRIX.csv",
        "simulation_requirements_csv": output_dir / f"{STAGE6A_PREFIX}_SIMULATION_REQUIREMENTS.csv",
        "acceptance_checklist_csv": output_dir / f"{STAGE6A_PREFIX}_ACCEPTANCE_CHECKLIST.csv",
        "spec_queue_csv": output_dir / f"{STAGE6A_PREFIX}_SHADOW_SPEC_QUEUE.csv",
    }


def _load_required_csv(path: Path, label: str) -> List[Dict[str, str]]:
    rows = _read_csv_rows(path)
    if not rows:
        raise SystemExit(f"Missing or empty required Stage-6A input {label}: {safe_rel(path)}")
    return rows


def _load_required_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise SystemExit(f"Missing required Stage-6A input readback JSON: {safe_rel(path)}")
    return json.loads(path.read_text(encoding="utf-8", errors="replace"))


def _by_mode(rows: Sequence[Mapping[str, Any]]) -> Dict[str, Mapping[str, Any]]:
    return {str(row.get("prototype_mode") or ""): row for row in rows if str(row.get("prototype_mode") or "")}


def _mode_metric(row: Mapping[str, Any], key: str) -> str:
    if key.endswith("_rate") or key.endswith("_share"):
        return _pct(row.get(key))
    return _fmt(row.get(key))


def _lane_contract_rows(mode_rows: Sequence[Mapping[str, Any]]) -> List[Dict[str, Any]]:
    modes = _by_mode(mode_rows)

    def mode(name: str) -> Mapping[str, Any]:
        return modes.get(name, {})

    lane_defs = [
        {
            "lane_id": "primary_restrained_candidate_expression",
            "source_modes": "clean_with_restraint_filter",
            "stage5_decision": mode("clean_with_restraint_filter").get("readback_decision", ""),
            "allowed_permission": "shadow_spec_only",
            "role": "primary shadow candidate-expression seed",
            "activation_scope": "candidate-expression evidence that survives Stage-5 restraint filtering",
            "support_policy": "support context may modify rank/priority only when paired with this lane; support cannot create candidates",
            "restraint_policy": "medium restraint may remain; high restraint becomes penalty/retest input, not automatic live veto",
            "lineage_policy": "dedupe shared lineage and do not double-count source aliases",
            "overlap_policy": "overlap can narrow or restrain only; no duplicate confirmation credit",
            "decay_policy": "decay/VTRAC may annotate carryforward context only; no boxed spend permission",
            "concentration_policy": "carry March-led positive-conversion warning until future/fresh windows repeat",
            "stage6b_requirement": "simulate against clean_boxed_only baseline, secondary lane, support-on/off, and restraint-on/off splits",
        },
        {
            "lane_id": "secondary_lineage_supported_restrained",
            "source_modes": "clean_lineage_supported_restrained",
            "stage5_decision": mode("clean_lineage_supported_restrained").get("readback_decision", ""),
            "allowed_permission": "shadow_spec_only",
            "role": "secondary shadow candidate-expression seed",
            "activation_scope": "lineage-supported candidate-expression evidence with explicit de-duplication and restraint awareness",
            "support_policy": "support is paired context only and must not expand the pool by itself",
            "restraint_policy": "carry restraint pressure as penalty/retest context",
            "lineage_policy": "mandatory lineage guardrail; source A/source B aliases are locators, not independent votes",
            "overlap_policy": "overlap requires source-side baseline comparison before any credit",
            "decay_policy": "decay/VTRAC stays companion context",
            "concentration_policy": "shadow-spec allowed with concentration warning",
            "stage6b_requirement": "simulate as secondary lane and compare incremental lift versus primary-only expression",
        },
        {
            "lane_id": "narrowed_lineage_foundation",
            "source_modes": "clean_plus_lineage_deduped",
            "stage5_decision": mode("clean_plus_lineage_deduped").get("readback_decision", ""),
            "allowed_permission": "narrow_before_design",
            "role": "broad candidate foundation requiring narrowing",
            "activation_scope": "not directly active; may provide narrowed fixture variants only",
            "support_policy": "support must be tested as a modifier, not an expansion",
            "restraint_policy": "must test pool-control and false-positive reduction before design promotion",
            "lineage_policy": "lineage de-duplication mandatory",
            "overlap_policy": "overlap narrowing only",
            "decay_policy": "no decay-to-box conversion",
            "concentration_policy": "March-led warning blocks direct promotion",
            "stage6b_requirement": "create narrowed variants and require better false-positive proxy than broad lineage baseline",
        },
        {
            "lane_id": "support_context_modifier",
            "source_modes": "support_gate_context|clean_with_support_context",
            "stage5_decision": "support_modifier_only|broad_context_needs_narrowing",
            "allowed_permission": "context_modifier_only",
            "role": "paired support/ranking context",
            "activation_scope": "only activates when paired with primary or secondary candidate-expression rows",
            "support_policy": "standalone support is forbidden",
            "restraint_policy": "support cannot override restraint pressure",
            "lineage_policy": "support aliases remain locators only",
            "overlap_policy": "support overlap cannot receive duplicate credit",
            "decay_policy": "support cannot convert decay/watch rows into candidate rows",
            "concentration_policy": "requires on/off ablation in Stage 6B",
            "stage6b_requirement": "run support-on versus support-off replay for primary and secondary lanes",
        },
        {
            "lane_id": "decay_watch_companion",
            "source_modes": "decay_watch_companion",
            "stage5_decision": mode("decay_watch_companion").get("readback_decision", ""),
            "allowed_permission": "companion_only",
            "role": "carryforward/territory annotation",
            "activation_scope": "may annotate horizons and carryforward context only",
            "support_policy": "not applicable",
            "restraint_policy": "wrong-lane pressure must remain visible",
            "lineage_policy": "not candidate lineage",
            "overlap_policy": "no overlap credit",
            "decay_policy": "explicitly barred from boxed/straight spend permission",
            "concentration_policy": "future decay rollup required before any stronger claim",
            "stage6b_requirement": "keep separate companion columns; do not include in candidate pool metrics",
        },
        {
            "lane_id": "low_denominator_watchlist",
            "source_modes": "low_denominator_watchlist",
            "stage5_decision": mode("low_denominator_watchlist").get("readback_decision", ""),
            "allowed_permission": "retest_before_design",
            "role": "retest/watchlist only",
            "activation_scope": "not active in shadow spec except as tagged watch material",
            "support_policy": "not standalone",
            "restraint_policy": "do not hard-code from small denominator",
            "lineage_policy": "dedupe before future retest",
            "overlap_policy": "overlap cannot rescue denominator fragility",
            "decay_policy": "not spend permission",
            "concentration_policy": "requires more state-days",
            "stage6b_requirement": "exclude from candidate expression; report separately",
        },
        {
            "lane_id": "restraint_calibration_surface",
            "source_modes": "restraint_retest",
            "stage5_decision": mode("restraint_retest").get("readback_decision", ""),
            "allowed_permission": "penalty_research_only",
            "role": "penalty/veto calibration surface",
            "activation_scope": "calibrates penalties; does not create candidates",
            "support_policy": "support cannot override restraint",
            "restraint_policy": "test soft penalty before any hard veto",
            "lineage_policy": "not independent evidence",
            "overlap_policy": "may act as restraint only",
            "decay_policy": "not spend permission",
            "concentration_policy": "requires future/fresh retest",
            "stage6b_requirement": "simulate no-penalty, soft-penalty, and hard-exclusion views as separate readback modes",
        },
    ]

    for row in lane_defs:
        source_mode = str(row.get("source_modes") or "").split("|")[0]
        metrics = mode(source_mode)
        row.update(
            {
                "stage5_status": metrics.get("status", ""),
                "stage5_avg_pool": _safe_float(metrics.get("avg_pool_or_exposure_per_state_day")),
                "stage5_false_positive_proxy_rate": _safe_float(metrics.get("false_positive_proxy_rate")),
                "stage5_pool_normalized_positive_yield": _safe_float(metrics.get("pool_normalized_positive_yield")),
                "stage5_top_window": metrics.get("top_window", ""),
                "stage5_window_concentration_flag": metrics.get("window_concentration_flag", ""),
                "live_permission": "forbidden",
            }
        )
    return lane_defs


def _guardrail_rows(action_rows: Sequence[Mapping[str, Any]]) -> List[Dict[str, Any]]:
    action_by_type = {str(row.get("action_type") or ""): row for row in action_rows}
    return [
        {
            "guardrail_id": "G01_no_live_permission",
            "severity": "hard_block",
            "source": "Stage 5 readback",
            "rule": "Stage 6A is a shadow specification only.",
            "enforcement": "No writes to live scoring, candidate generation, translator code, budget logic, or legacy infrastructure.",
            "failure_response": "Stop and redesign as read-only artifact.",
        },
        {
            "guardrail_id": "G02_primary_lane_only_seed",
            "severity": "hard_block",
            "source": "clean_with_restraint_filter",
            "rule": "Primary spec seed is restrained candidate-expression behavior.",
            "enforcement": "Do not blend support, decay, low-denominator, and restraint rows into one pool.",
            "failure_response": "Reject Stage 6B simulator output as blended and rerun with separated lanes.",
        },
        {
            "guardrail_id": "G03_secondary_lineage_dedup",
            "severity": "hard_block",
            "source": "clean_lineage_supported_restrained",
            "rule": "Secondary lane must carry lineage de-duplication.",
            "enforcement": "Source A/source B aliases are locators, not independent votes.",
            "failure_response": "Remove duplicate-credit rows before replay.",
        },
        {
            "guardrail_id": "G04_overlap_no_duplicate_credit",
            "severity": "hard_block",
            "source": "source A/source B ablation",
            "rule": "Overlap does not receive extra scoring credit unless it beats the best source-side baseline.",
            "enforcement": action_by_type.get("ablation_guardrail", {}).get("action", "Treat overlap as narrowing/restraint only."),
            "failure_response": "Keep overlap as pool narrowing or restraint.",
        },
        {
            "guardrail_id": "G05_support_modifier_only",
            "severity": "hard_block",
            "source": "support gate policy",
            "rule": "Support context cannot create candidates.",
            "enforcement": action_by_type.get("support_gate_policy", {}).get("action", "Support remains paired context only."),
            "failure_response": "Move support-only rows out of candidate-expression scoring.",
        },
        {
            "guardrail_id": "G06_decay_companion_only",
            "severity": "hard_block",
            "source": "decay_watch_companion",
            "rule": "Decay/VTRAC territory cannot become boxed or straight spend permission.",
            "enforcement": "Carry decay columns as companion annotations only.",
            "failure_response": "Remove decay-driven candidate rows from simulation.",
        },
        {
            "guardrail_id": "G07_restraint_soft_before_hard",
            "severity": "design_constraint",
            "source": "restraint calibration",
            "rule": "Calibrate restraint as penalty/veto pressure before any hard exclusion.",
            "enforcement": action_by_type.get("restraint_calibration", {}).get("action", "Compare no-penalty, soft-penalty, hard-exclusion views."),
            "failure_response": "Keep restraint in research-only mode.",
        },
        {
            "guardrail_id": "G08_march_concentration_warning",
            "severity": "design_constraint",
            "source": "window concentration",
            "rule": "Positive-conversion metrics are March-led until future/fresh windows repeat the shape.",
            "enforcement": action_by_type.get("window_concentration_guardrail", {}).get("action", "Carry concentration warning in all Stage 6B outputs."),
            "failure_response": "Do not promote from shadow spec to live rewrite.",
        },
        {
            "guardrail_id": "G09_macro_findings_gate",
            "severity": "documentation_gate",
            "source": "macro findings gate",
            "rule": "Macro Findings Log receives evidence-led findings, not infrastructure milestones.",
            "enforcement": action_by_type.get("macro_findings_gate", {}).get("action", "Tag as provisional unless repeated or confirmed."),
            "failure_response": "Keep finding in readback/spec memo only.",
        },
    ]


def _simulation_requirement_rows() -> List[Dict[str, Any]]:
    return [
        {
            "requirement_id": "S6B-001",
            "test_target": "primary_restrained_candidate_expression",
            "mandatory_input": "Stage5 value-level replay ledger and mode decisions",
            "metric": "false_positive_proxy_rate, pool_normalized_positive_yield, active_state_days",
            "pass_condition": "beats clean_boxed_only on false-positive proxy or yield without larger pool explosion",
            "reason": "Primary lane is the best Stage-5 shadow-spec seed but must be replayed before any design confidence.",
        },
        {
            "requirement_id": "S6B-002",
            "test_target": "secondary_lineage_supported_restrained",
            "mandatory_input": "Stage5 readback mode decisions",
            "metric": "incremental positive conversion versus primary-only; lineage duplicate count",
            "pass_condition": "adds value without duplicate-credit inflation",
            "reason": "Secondary lane is useful only if lineage guardrails hold.",
        },
        {
            "requirement_id": "S6B-003",
            "test_target": "support_context_modifier",
            "mandatory_input": "Stage5 support-gate ablation",
            "metric": "support-on versus support-off false-positive proxy and yield",
            "pass_condition": "support improves or narrows paired candidate rows; standalone support remains excluded",
            "reason": "Support context is broad and must be measured as a modifier.",
        },
        {
            "requirement_id": "S6B-004",
            "test_target": "restraint_calibration_surface",
            "mandatory_input": "Stage5 restraint-effect audit",
            "metric": "no-penalty versus soft-penalty versus hard-exclusion readback",
            "pass_condition": "soft penalty reduces junk without killing useful signal; hard exclusion requires explicit proof",
            "reason": "Stage 5 says restraint is useful but not safe as automatic discard logic.",
        },
        {
            "requirement_id": "S6B-005",
            "test_target": "source_a_source_b_overlap",
            "mandatory_input": "Stage5 ablation matrix",
            "metric": "overlap lift versus best source and pool reduction",
            "pass_condition": "overlap is treated as narrowing/restraint unless positive lift appears",
            "reason": "Stage 5 found zero positive overlap lift rows over best source.",
        },
        {
            "requirement_id": "S6B-006",
            "test_target": "window_and_state_concentration",
            "mandatory_input": "Stage5 window/state stratification",
            "metric": "positive conversion share by window and state",
            "pass_condition": "all shadow outputs carry concentration warnings until repeated on future/fresh windows",
            "reason": "Stage 5 positive-conversion labels are March-led.",
        },
        {
            "requirement_id": "S6B-007",
            "test_target": "decay_watch_companion",
            "mandatory_input": "Stage5 decay/watch mode rows",
            "metric": "annotation coverage and wrong-lane pressure",
            "pass_condition": "decay remains excluded from candidate pool metrics",
            "reason": "Decay/VTRAC can explain territory but cannot become spend permission.",
        },
    ]


def _acceptance_checklist_rows(
    *,
    lane_rows: Sequence[Mapping[str, Any]],
    guardrail_rows: Sequence[Mapping[str, Any]],
    simulation_rows: Sequence[Mapping[str, Any]],
) -> List[Dict[str, Any]]:
    lane_ids = {str(row.get("lane_id") or "") for row in lane_rows}
    guardrail_ids = {str(row.get("guardrail_id") or "") for row in guardrail_rows}
    sim_ids = {str(row.get("requirement_id") or "") for row in simulation_rows}
    checks = [
        ("A01_primary_lane_present", "primary_restrained_candidate_expression" in lane_ids, "primary restrained candidate-expression lane exists"),
        ("A02_secondary_lane_present", "secondary_lineage_supported_restrained" in lane_ids, "secondary lineage-supported restrained lane exists"),
        ("A03_support_standalone_forbidden", "G05_support_modifier_only" in guardrail_ids, "support-only context is forbidden as candidate source"),
        ("A04_decay_spend_forbidden", "G06_decay_companion_only" in guardrail_ids, "decay/VTRAC spend permission is blocked"),
        ("A05_overlap_duplicate_credit_blocked", "G04_overlap_no_duplicate_credit" in guardrail_ids, "source overlap duplicate-credit is blocked"),
        ("A06_concentration_warning_carried", "G08_march_concentration_warning" in guardrail_ids, "March-led concentration warning is explicit"),
        ("A07_simulation_requirements_exist", len(sim_ids) >= 7, "Stage 6B simulation requirements are defined"),
        ("A08_no_live_permission", "G01_no_live_permission" in guardrail_ids, "live scoring/candidate/budget changes are blocked"),
    ]
    return [
        {
            "check_id": check_id,
            "status": "pass" if passed else "fail",
            "requirement": requirement,
            "failure_response": "do not proceed to Stage 6B until fixed" if not passed else "",
        }
        for check_id, passed, requirement in checks
    ]


def _spec_queue_rows(next_action_rows: Sequence[Mapping[str, Any]]) -> List[Dict[str, Any]]:
    queue = [
        {
            "priority": 1,
            "work_item": "stage6b_shadow_replay_simulator",
            "source_decision": "design_shadow_spec_next",
            "scope": "simulate primary and secondary shadow lanes against completed fixtures",
            "blocked_until": "Stage 6A acceptance checklist passes",
            "permission": "read_only_replay",
        },
        {
            "priority": 2,
            "work_item": "support_modifier_ablation",
            "source_decision": "support_gate_policy",
            "scope": "test support-on/support-off paired with primary and secondary candidate lanes",
            "blocked_until": "Stage 6B simulator exists",
            "permission": "read_only_replay",
        },
        {
            "priority": 3,
            "work_item": "restraint_penalty_calibration",
            "source_decision": "restraint_calibration",
            "scope": "compare no-penalty, soft-penalty, and hard-exclusion variants",
            "blocked_until": "Stage 6B simulator exists",
            "permission": "read_only_replay",
        },
        {
            "priority": 4,
            "work_item": "narrowed_lineage_variant_design",
            "source_decision": "narrow_before_design",
            "scope": "derive smaller lineage variants without promoting broad lineage pools",
            "blocked_until": "primary/secondary simulator baselines exist",
            "permission": "shadow_design_only",
        },
        {
            "priority": 5,
            "work_item": "macro_findings_review_gate",
            "source_decision": "macro_findings_gate",
            "scope": "decide whether Stage 6A/6B findings are provisional, repeated, confirmed, deferred, or contradicted",
            "blocked_until": "Stage 6B readback or future/fresh repeat",
            "permission": "documentation_only",
        },
    ]
    seen_decisions = {str(row.get("action_type") or "") for row in next_action_rows}
    for row in queue:
        row["source_present_in_stage5_readback"] = "yes" if row["source_decision"] in seen_decisions else "no"
    return queue


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
    lane_rows: Sequence[Mapping[str, Any]],
    guardrail_rows: Sequence[Mapping[str, Any]],
    simulation_rows: Sequence[Mapping[str, Any]],
    checklist_rows: Sequence[Mapping[str, Any]],
    spec_queue_rows: Sequence[Mapping[str, Any]],
    output_paths: Mapping[str, Path],
) -> str:
    lines: List[str] = [
        "# Analysis Arena Stage 6A Shadow Translator Specification",
        "",
        "Purpose: turn Stage 5 readback decisions into a formal shadow translator contract before any replay simulator or scoring rewrite work.",
        "",
        "## Metadata",
        f"- runs2_dir: `{safe_rel(runs2_dir)}`",
        f"- lane_contract_rows: `{len(lane_rows)}`",
        f"- guardrail_rows: `{len(guardrail_rows)}`",
        f"- simulation_requirements: `{len(simulation_rows)}`",
        f"- acceptance_checks: `{len(checklist_rows)}`",
        "",
        "## Guardrails",
        "- Stage 6A is read-only and grants no live scoring, candidate-generation, translator, budget, or legacy-infrastructure permission.",
        "- The primary spec seed is restrained candidate-expression behavior, not a blend of every Stage 5 lane.",
        "- Support context is modifier-only; decay/VTRAC is companion-only; low-denominator and restraint rows are retest/calibration lanes.",
        "- Source overlap cannot receive duplicate confirmation credit because Stage 5 overlap ablation did not beat best-source baselines.",
        "- Positive-conversion evidence remains March-led until future/fresh windows repeat the same readback shape.",
        "",
        "## Lane Contract",
    ]
    lines.extend(
        _table(
            ["lane", "source modes", "permission", "role", "FP proxy", "yield"],
            [
                [
                    row.get("lane_id", ""),
                    row.get("source_modes", ""),
                    row.get("allowed_permission", ""),
                    row.get("role", ""),
                    _pct(row.get("stage5_false_positive_proxy_rate")),
                    _fmt(row.get("stage5_pool_normalized_positive_yield")),
                ]
                for row in lane_rows
            ],
        )
    )
    lines += [
        "",
        "## Guardrail Matrix",
    ]
    lines.extend(
        _table(
            ["guardrail", "severity", "rule", "failure response"],
            [
                [
                    row.get("guardrail_id", ""),
                    row.get("severity", ""),
                    row.get("rule", ""),
                    row.get("failure_response", ""),
                ]
                for row in guardrail_rows
            ],
        )
    )
    lines += [
        "",
        "## Stage 6B Simulation Requirements",
    ]
    lines.extend(
        _table(
            ["requirement", "target", "metric", "pass condition"],
            [
                [
                    row.get("requirement_id", ""),
                    row.get("test_target", ""),
                    row.get("metric", ""),
                    row.get("pass_condition", ""),
                ]
                for row in simulation_rows
            ],
        )
    )
    lines += [
        "",
        "## Acceptance Checklist",
    ]
    lines.extend(
        _table(
            ["check", "status", "requirement"],
            [
                [row.get("check_id", ""), row.get("status", ""), row.get("requirement", "")]
                for row in checklist_rows
            ],
        )
    )
    lines += [
        "",
        "## Shadow Spec Queue",
    ]
    lines.extend(
        _table(
            ["priority", "work item", "permission", "blocked until"],
            [
                [
                    row.get("priority", ""),
                    row.get("work_item", ""),
                    row.get("permission", ""),
                    row.get("blocked_until", ""),
                ]
                for row in spec_queue_rows
            ],
        )
    )
    lines += [
        "",
        "## Interpretation",
        "- Stage 6A authorizes a future read-only Stage 6B replay simulator, not live scoring.",
        "- The simulator should test the primary restrained lane first, then secondary lineage-supported restrained behavior, then support/restraint ablations.",
        "- Any Stage 6B output must preserve concentration warnings and lane separation.",
        "- Macro findings should wait for Stage 6B readback or future/fresh repeat evidence.",
        "",
        "## Output Files",
    ]
    for key, path in output_paths.items():
        lines.append(f"- {key}: `{safe_rel(path)}`")
    lines.append("")
    return "\n".join(lines)


def build_spec_payload(
    *,
    runs2_dir: Path,
    output_dir: Path,
) -> Tuple[Dict[str, Any], Dict[str, List[Dict[str, Any]]], str]:
    inputs = _input_paths(runs2_dir)
    outputs = _output_paths(output_dir)
    mode_rows = _load_required_csv(inputs["mode_decisions"], "mode decisions")
    next_action_rows = _load_required_csv(inputs["next_actions"], "next action queue")
    readback_json = _load_required_json(inputs["readback_json"])

    lane_rows = _lane_contract_rows(mode_rows)
    guardrails = _guardrail_rows(next_action_rows)
    simulation = _simulation_requirement_rows()
    checklist = _acceptance_checklist_rows(
        lane_rows=lane_rows,
        guardrail_rows=guardrails,
        simulation_rows=simulation,
    )
    spec_queue = _spec_queue_rows(next_action_rows)

    tables = {
        "lane_contract": lane_rows,
        "guardrails": guardrails,
        "simulation_requirements": simulation,
        "acceptance_checklist": checklist,
        "spec_queue": spec_queue,
    }
    payload: Dict[str, Any] = {
        "runs2_dir": safe_rel(runs2_dir),
        "source_files": {key: safe_rel(path) for key, path in inputs.items()},
        "stage5_readback_summary": {
            "mode_decisions": len(mode_rows),
            "next_actions": len(next_action_rows),
            "stage5_metadata": readback_json.get("stage5_metadata", {}),
            "guardrail": readback_json.get("guardrail", ""),
        },
        **tables,
        "stage6a_permission": "shadow_specification_only",
        "live_permission": "forbidden",
        "next_layer": "Stage 6B read-only shadow replay simulator",
    }
    md = _render_md(
        runs2_dir=runs2_dir,
        lane_rows=lane_rows,
        guardrail_rows=guardrails,
        simulation_rows=simulation,
        checklist_rows=checklist,
        spec_queue_rows=spec_queue,
        output_paths=outputs,
    )
    return payload, tables, md


def main() -> None:
    args = _parse_args()
    runs2_dir = _resolve_path(args.runs2_dir)
    output_dir = _resolve_path(args.output_dir)
    outputs = _output_paths(output_dir)
    payload, tables, md = build_spec_payload(runs2_dir=runs2_dir, output_dir=output_dir)

    _write_text(outputs["md"], md, force=bool(args.force))
    _write_json(outputs["json"], payload, force=bool(args.force))
    _write_csv(outputs["lane_contract_csv"], tables["lane_contract"], force=bool(args.force))
    _write_csv(outputs["guardrail_csv"], tables["guardrails"], force=bool(args.force))
    _write_csv(outputs["simulation_requirements_csv"], tables["simulation_requirements"], force=bool(args.force))
    _write_csv(outputs["acceptance_checklist_csv"], tables["acceptance_checklist"], force=bool(args.force))
    _write_csv(outputs["spec_queue_csv"], tables["spec_queue"], force=bool(args.force))

    print(f"[OK] Wrote Stage-6A shadow translator specification: {safe_rel(outputs['md'])}")
    print(f"[OK] Lane contract rows: {len(tables['lane_contract'])}")
    print(f"[OK] Simulation requirements: {len(tables['simulation_requirements'])}")
    print(f"[OK] Acceptance checks: {len(tables['acceptance_checklist'])}")


if __name__ == "__main__":
    main()
