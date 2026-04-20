#!/usr/bin/env python3
"""Create the Stage-6D restraint calibration workbench.

Stage 6D is read-only. It decomposes Stage 6B restraint evidence into pressure
buckets, rescue candidates, and soft-penalty hypotheses. It does not alter live
scoring, candidate generation, translator logic, budget logic, or legacy
infrastructure.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Mapping, MutableMapping, Sequence, Tuple


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.tools.analysis_arena_window_utils import safe_rel  # type: ignore
from scripts.tools.create_analysis_arena_stage4_fixture_replay_harness import (  # type: ignore
    RUNS_2_DIR,
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
from scripts.tools.create_analysis_arena_stage6b_shadow_replay_simulator import (  # type: ignore
    _add_to_agg,
    _agg_to_row,
    _is_candidate_row,
    _new_agg,
)


STAGE5_PREFIX = "ANALYSIS_ARENA__CYCLE__STAGE5"
STAGE6B_PREFIX = "ANALYSIS_ARENA__CYCLE__STAGE6B"
READBACK_PREFIX = "ANALYSIS_ARENA__CYCLE__STAGE6B_READBACK"
STAGE6D_PREFIX = "ANALYSIS_ARENA__CYCLE__STAGE6D"


def _parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--runs2-dir", default=str(RUNS_2_DIR), help="RUNS_2 root containing Stage-5/Stage-6B outputs.")
    ap.add_argument("--output-dir", default=str(RUNS_2_DIR), help="Cycle-level output directory.")
    ap.add_argument("--force", action="store_true", help="Overwrite existing Stage-6D outputs.")
    return ap.parse_args()


def _input_paths(runs2_dir: Path) -> Dict[str, Path]:
    return {
        "value_ledger": runs2_dir / f"{STAGE5_PREFIX}_VALUE_LEVEL_REPLAY_LEDGER.csv",
        "scenario_decisions": runs2_dir / f"{READBACK_PREFIX}_SCENARIO_DECISIONS.csv",
        "requirement_results": runs2_dir / f"{READBACK_PREFIX}_REQUIREMENT_RESULTS.csv",
        "next_action_queue": runs2_dir / f"{READBACK_PREFIX}_NEXT_ACTION_QUEUE.csv",
        "restraint_calibration": runs2_dir / f"{STAGE6B_PREFIX}_RESTRAINT_CALIBRATION.csv",
    }


def _output_paths(output_dir: Path) -> Dict[str, Path]:
    return {
        "md": output_dir / f"{STAGE6D_PREFIX}_RESTRAINT_CALIBRATION_WORKBENCH.md",
        "json": output_dir / f"{STAGE6D_PREFIX}_RESTRAINT_CALIBRATION_WORKBENCH.json",
        "bucket_scorecard_csv": output_dir / f"{STAGE6D_PREFIX}_RESTRAINT_BUCKET_SCORECARD.csv",
        "rescue_candidates_csv": output_dir / f"{STAGE6D_PREFIX}_HIGH_PRESSURE_RESCUE_CANDIDATES.csv",
        "policy_matrix_csv": output_dir / f"{STAGE6D_PREFIX}_SOFT_PENALTY_POLICY_MATRIX.csv",
        "next_actions_csv": output_dir / f"{STAGE6D_PREFIX}_RESTRAINT_NEXT_ACTIONS.csv",
    }


def _load_required_csv(path: Path, label: str) -> List[Dict[str, str]]:
    rows = _read_csv_rows(path)
    if not rows:
        raise SystemExit(f"Missing or empty Stage-6D input {label}: {safe_rel(path)}")
    return rows


def _row_by_id(rows: Sequence[Mapping[str, Any]], field: str) -> Dict[str, Mapping[str, Any]]:
    return {str(row.get(field) or ""): row for row in rows}


def _support_label(row: Mapping[str, Any]) -> str:
    return "support_on" if str(row.get("support_context_present") or "").lower() == "true" else "support_off"


def _pressure(row: Mapping[str, Any]) -> str:
    return str(row.get("restraint_pressure") or "unknown").strip().lower() or "unknown"


def _bucket_key_parts(row: Mapping[str, Any]) -> List[Tuple[str, Dict[str, str]]]:
    pressure = _pressure(row)
    mechanism = str(row.get("mechanism_family") or "unknown")
    lane = str(row.get("prototype_lane") or "unknown")
    cluster = str(row.get("cluster_key") or "unknown")
    support = _support_label(row)
    return [
        (
            f"pressure::{pressure}",
            {
                "bucket_type": "pressure",
                "restraint_pressure": pressure,
                "mechanism_family": "",
                "prototype_lane": "",
                "support_context": "",
                "cluster_key": "",
            },
        ),
        (
            f"pressure_lane::{pressure}::{lane}",
            {
                "bucket_type": "pressure_lane",
                "restraint_pressure": pressure,
                "mechanism_family": "",
                "prototype_lane": lane,
                "support_context": "",
                "cluster_key": "",
            },
        ),
        (
            f"pressure_mechanism::{pressure}::{mechanism}",
            {
                "bucket_type": "pressure_mechanism",
                "restraint_pressure": pressure,
                "mechanism_family": mechanism,
                "prototype_lane": "",
                "support_context": "",
                "cluster_key": "",
            },
        ),
        (
            f"pressure_support::{pressure}::{support}",
            {
                "bucket_type": "pressure_support",
                "restraint_pressure": pressure,
                "mechanism_family": "",
                "prototype_lane": "",
                "support_context": support,
                "cluster_key": "",
            },
        ),
        (
            f"pressure_mechanism_lane::{pressure}::{mechanism}::{lane}",
            {
                "bucket_type": "pressure_mechanism_lane",
                "restraint_pressure": pressure,
                "mechanism_family": mechanism,
                "prototype_lane": lane,
                "support_context": "",
                "cluster_key": "",
            },
        ),
        (
            f"high_pressure_cluster::{cluster}" if pressure == "high" else "",
            {
                "bucket_type": "high_pressure_cluster",
                "restraint_pressure": pressure,
                "mechanism_family": mechanism,
                "prototype_lane": lane,
                "support_context": support,
                "cluster_key": cluster,
            },
        ),
    ]


def _bucket_scorecard_rows(
    ledger_rows: Sequence[Mapping[str, Any]],
    *,
    primary: Mapping[str, Any],
    baseline: Mapping[str, Any],
) -> List[Dict[str, Any]]:
    grouped: MutableMapping[str, Dict[str, Any]] = defaultdict(_new_agg)
    labels: Dict[str, Dict[str, str]] = {}
    for row in ledger_rows:
        if not _is_candidate_row(row):
            continue
        for bucket_id, label in _bucket_key_parts(row):
            if not bucket_id:
                continue
            labels[bucket_id] = {"bucket_id": bucket_id, **label}
            _add_to_agg(grouped[bucket_id], row)

    primary_fp = _safe_float(primary.get("false_positive_proxy_rate"))
    primary_yield = _safe_float(primary.get("pool_normalized_positive_yield"))
    baseline_fp = _safe_float(baseline.get("false_positive_proxy_rate"))
    rows: List[Dict[str, Any]] = []
    for bucket_id, agg in grouped.items():
        row = _agg_to_row(labels[bucket_id], agg)
        fp = _safe_float(row.get("false_positive_proxy_rate"))
        yld = _safe_float(row.get("pool_normalized_positive_yield"))
        positive = _safe_int(row.get("positive_conversion_event_count"))
        state_days = _safe_int(row.get("active_state_days"))
        pressure = str(row.get("restraint_pressure") or "")
        row["false_positive_delta_vs_primary"] = fp - primary_fp
        row["yield_delta_vs_primary"] = yld - primary_yield
        row["false_positive_delta_vs_baseline"] = fp - baseline_fp
        row["restraint_readback_posture"] = _restraint_posture(
            pressure=pressure,
            fp=fp,
            yld=yld,
            positive=positive,
            state_days=state_days,
            primary_fp=primary_fp,
            primary_yield=primary_yield,
        )
        rows.append(row)
    return sorted(
        rows,
        key=lambda row: (
            str(row.get("restraint_pressure") or "") != "high",
            -_safe_int(row.get("positive_conversion_event_count")),
            _safe_float(row.get("false_positive_proxy_rate")),
        ),
    )


def _restraint_posture(
    *,
    pressure: str,
    fp: float,
    yld: float,
    positive: int,
    state_days: int,
    primary_fp: float,
    primary_yield: float,
) -> str:
    if state_days < 3 or positive < 10:
        return "low_denominator_retest_only"
    if pressure == "high" and (fp <= primary_fp + 0.08 or yld >= primary_yield * 0.85):
        return "high_pressure_rescue_candidate_soft_penalty_only"
    if pressure == "high":
        return "high_pressure_downweight_candidate"
    if fp <= primary_fp and yld >= primary_yield:
        return "non_high_confirmation_candidate"
    return "reference_bucket_only"


def _rescue_candidate_rows(bucket_rows: Sequence[Mapping[str, Any]]) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for row in bucket_rows:
        posture = str(row.get("restraint_readback_posture") or "")
        if "rescue_candidate" not in posture and "downweight_candidate" not in posture:
            continue
        if str(row.get("restraint_pressure") or "") != "high":
            continue
        rows.append(
            {
                "candidate_id": f"S6D-RESCUE-{len(rows) + 1:03d}",
                "bucket_id": row.get("bucket_id", ""),
                "bucket_type": row.get("bucket_type", ""),
                "mechanism_family": row.get("mechanism_family", ""),
                "prototype_lane": row.get("prototype_lane", ""),
                "support_context": row.get("support_context", ""),
                "cluster_key": row.get("cluster_key", ""),
                "ledger_rows": row.get("ledger_rows", 0),
                "active_state_days": row.get("active_state_days", 0),
                "positive_conversion_event_count": row.get("positive_conversion_event_count", 0),
                "false_positive_proxy_rate": row.get("false_positive_proxy_rate", 0.0),
                "pool_normalized_positive_yield": row.get("pool_normalized_positive_yield", 0.0),
                "false_positive_delta_vs_primary": row.get("false_positive_delta_vs_primary", 0.0),
                "yield_delta_vs_primary": row.get("yield_delta_vs_primary", 0.0),
                "recommended_use": posture,
                "stage_permission": "penalty_research_only",
                "live_permission": "none",
            }
        )
    return sorted(
        rows,
        key=lambda row: (
            str(row.get("recommended_use") or "") != "high_pressure_rescue_candidate_soft_penalty_only",
            -_safe_int(row.get("positive_conversion_event_count")),
            _safe_float(row.get("false_positive_proxy_rate")),
        ),
    )


def _fractional_policy_row(
    *,
    policy_id: str,
    keep_high_fraction: float,
    hard_row: Mapping[str, Any],
    high_row: Mapping[str, Any],
    interpretation: str,
) -> Dict[str, Any]:
    hard_total = _safe_float(hard_row.get("total_overlap_values"))
    hard_fp = _safe_float(hard_row.get("false_positive_proxy_value_count"))
    hard_pos = _safe_float(hard_row.get("positive_conversion_event_count"))
    hard_matched = _safe_float(hard_row.get("matched_value_count"))
    high_total = _safe_float(high_row.get("total_overlap_values")) * keep_high_fraction
    high_fp = _safe_float(high_row.get("false_positive_proxy_value_count")) * keep_high_fraction
    high_pos = _safe_float(high_row.get("positive_conversion_event_count")) * keep_high_fraction
    high_matched = _safe_float(high_row.get("matched_value_count")) * keep_high_fraction
    total = hard_total + high_total
    return {
        "policy_id": policy_id,
        "policy_type": "aggregate_soft_penalty_hypothesis",
        "kept_high_pressure_fraction": keep_high_fraction,
        "estimated_total_overlap_values": total,
        "estimated_matched_value_count": hard_matched + high_matched,
        "estimated_false_positive_proxy_value_count": hard_fp + high_fp,
        "estimated_false_positive_proxy_rate": _rate(hard_fp + high_fp, total),
        "estimated_positive_conversion_event_count": hard_pos + high_pos,
        "estimated_pool_normalized_positive_yield": 100.0 * _rate(hard_pos + high_pos, total),
        "interpretation": interpretation,
        "allowed_permission": "penalty_research_only",
        "live_permission": "none",
    }


def _policy_matrix_rows(restraint_rows: Sequence[Mapping[str, Any]]) -> List[Dict[str, Any]]:
    by_bucket = _row_by_id(restraint_rows, "restraint_calibration_bucket")
    no_penalty = by_bucket.get("no_penalty_all_candidate_rows", {})
    hard = by_bucket.get("hard_exclusion_non_high_pressure", {})
    high = by_bucket.get("removed_high_pressure_candidate_rows", {})
    rows: List[Dict[str, Any]] = []

    def add_reference(policy_id: str, row: Mapping[str, Any], interpretation: str) -> None:
        rows.append(
            {
                "policy_id": policy_id,
                "policy_type": "stage6b_reference_bucket",
                "kept_high_pressure_fraction": "",
                "estimated_total_overlap_values": _safe_float(row.get("total_overlap_values")),
                "estimated_matched_value_count": _safe_float(row.get("matched_value_count")),
                "estimated_false_positive_proxy_value_count": _safe_float(row.get("false_positive_proxy_value_count")),
                "estimated_false_positive_proxy_rate": _safe_float(row.get("false_positive_proxy_rate")),
                "estimated_positive_conversion_event_count": _safe_float(row.get("positive_conversion_event_count")),
                "estimated_pool_normalized_positive_yield": _safe_float(row.get("pool_normalized_positive_yield")),
                "interpretation": interpretation,
                "allowed_permission": "reference_only",
                "live_permission": "none",
            }
        )

    add_reference("no_penalty_all_candidate_rows", no_penalty, "Broad candidate reference; currently higher FP pressure than hard exclusion.")
    add_reference("hard_exclusion_non_high_pressure", hard, "Best aggregate Stage 6B reference but cannot become a live hard veto.")
    add_reference("removed_high_pressure_candidate_rows", high, "High-pressure rows contain conversions but carry weaker FP/yield in aggregate.")
    for fraction in (0.25, 0.50, 0.75):
        rows.append(
            _fractional_policy_row(
                policy_id=f"soft_penalty_keep_high_{int(fraction * 100)}pct",
                keep_high_fraction=fraction,
                hard_row=hard,
                high_row=high,
                interpretation="Aggregate calibration hypothesis only; use bucket rescue candidates before any rewrite design.",
            )
        )
    rows.append(
        {
            "policy_id": "stage6d_recommendation",
            "policy_type": "readback_decision",
            "kept_high_pressure_fraction": "",
            "estimated_total_overlap_values": "",
            "estimated_matched_value_count": "",
            "estimated_false_positive_proxy_value_count": "",
            "estimated_false_positive_proxy_rate": "",
            "estimated_positive_conversion_event_count": "",
            "estimated_pool_normalized_positive_yield": "",
            "interpretation": "Proceed with soft-penalty research only: no hard veto, no live scoring, no candidate-generation permission.",
            "allowed_permission": "penalty_research_only",
            "live_permission": "none",
        }
    )
    return rows


def _next_action_rows(rescue_rows: Sequence[Mapping[str, Any]], policy_rows: Sequence[Mapping[str, Any]]) -> List[Dict[str, Any]]:
    strong_rescues = [row for row in rescue_rows if str(row.get("recommended_use") or "") == "high_pressure_rescue_candidate_soft_penalty_only"]
    return [
        {
            "priority": 1,
            "action_type": "soft_penalty_grid_replay",
            "subject": "restraint_pressure_high",
            "action": "Replay high-pressure rows under soft penalty bands rather than hard exclusion.",
            "evidence": f"{len(policy_rows)} policy rows generated; {len(strong_rescues)} high-pressure rescue buckets found.",
            "allowed_permission": "penalty_research_only",
            "live_permission": "none",
        },
        {
            "priority": 2,
            "action_type": "rescue_bucket_review",
            "subject": "high_pressure_rescue_candidates",
            "action": "Inspect rescue buckets before declaring high pressure globally bad; the aggregate is weaker but contains conversions.",
            "evidence": f"{len(rescue_rows)} high-pressure buckets require review.",
            "allowed_permission": "research_only",
            "live_permission": "none",
        },
        {
            "priority": 3,
            "action_type": "future_window_confirmation",
            "subject": "restraint_soft_penalty",
            "action": "Run this workbench after each future Stage 6B replay to see whether restraint calibration repeats.",
            "evidence": "Stage 6D is a post-readback research layer; it cannot clear live rewrite blockers by itself.",
            "allowed_permission": "readback_only",
            "live_permission": "none",
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
    bucket_rows: Sequence[Mapping[str, Any]],
    rescue_rows: Sequence[Mapping[str, Any]],
    policy_rows: Sequence[Mapping[str, Any]],
    next_actions: Sequence[Mapping[str, Any]],
    output_paths: Mapping[str, Path],
) -> str:
    top_rescues = list(rescue_rows[:10])
    lines: List[str] = [
        "# Analysis Arena Stage 6D Restraint Calibration Workbench",
        "",
        "## Guardrail",
        "",
        "Stage 6D is read-only. It turns restraint evidence into research buckets and soft-penalty hypotheses only; it does not change live scoring, candidate generation, translator logic, budget logic, or legacy infrastructure.",
        "",
        "## Executive Readback",
        "",
        f"- restraint bucket rows generated: `{len(bucket_rows)}`",
        f"- high-pressure rescue/downweight candidates generated: `{len(rescue_rows)}`",
        "- The aggregate hard-exclusion reference is useful evidence, but Stage 6D keeps it blocked from live use and focuses on soft-before-hard calibration.",
        "",
        "## Top High-Pressure Buckets",
        "",
    ]
    lines.extend(
        _table(
            ["candidate_id", "bucket_id", "positive", "fp", "yield", "recommended_use"],
            [
                [
                    row.get("candidate_id", ""),
                    row.get("bucket_id", ""),
                    row.get("positive_conversion_event_count", ""),
                    _pct(row.get("false_positive_proxy_rate")),
                    _fmt(row.get("pool_normalized_positive_yield")),
                    row.get("recommended_use", ""),
                ]
                for row in top_rescues
            ],
        )
    )
    lines.extend(["", "## Soft-Penalty Policy Matrix", ""])
    lines.extend(
        _table(
            ["policy_id", "fp", "yield", "positive", "permission"],
            [
                [
                    row.get("policy_id", ""),
                    _pct(row.get("estimated_false_positive_proxy_rate")),
                    _fmt(row.get("estimated_pool_normalized_positive_yield")),
                    _fmt(row.get("estimated_positive_conversion_event_count")),
                    row.get("allowed_permission", ""),
                ]
                for row in policy_rows
            ],
        )
    )
    lines.extend(["", "## Next Actions", ""])
    lines.extend(
        _table(
            ["priority", "action_type", "subject", "action"],
            [[row.get("priority", ""), row.get("action_type", ""), row.get("subject", ""), row.get("action", "")] for row in next_actions],
        )
    )
    lines.extend(
        [
            "",
            "## Outputs",
            "",
            f"- workbench_json: `{safe_rel(output_paths['json'])}`",
            f"- restraint_bucket_scorecard: `{safe_rel(output_paths['bucket_scorecard_csv'])}`",
            f"- high_pressure_rescue_candidates: `{safe_rel(output_paths['rescue_candidates_csv'])}`",
            f"- soft_penalty_policy_matrix: `{safe_rel(output_paths['policy_matrix_csv'])}`",
            f"- restraint_next_actions: `{safe_rel(output_paths['next_actions_csv'])}`",
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

    ledger_rows = _load_required_csv(inputs["value_ledger"], "Stage 5 value-level replay ledger")
    scenario_decisions = _load_required_csv(inputs["scenario_decisions"], "Stage 6B readback scenario decisions")
    requirement_results = _load_required_csv(inputs["requirement_results"], "Stage 6B readback requirement results")
    _load_required_csv(inputs["next_action_queue"], "Stage 6B readback next action queue")
    restraint_rows = _load_required_csv(inputs["restraint_calibration"], "Stage 6B restraint calibration")

    scenarios = _row_by_id(scenario_decisions, "scenario_id")
    primary = scenarios.get("primary_restrained_candidate_expression", {})
    baseline = scenarios.get("baseline_clean_boxed", {})
    bucket_rows = _bucket_scorecard_rows(ledger_rows, primary=primary, baseline=baseline)
    rescue_rows = _rescue_candidate_rows(bucket_rows)
    policy_rows = _policy_matrix_rows(restraint_rows)
    next_actions = _next_action_rows(rescue_rows, policy_rows)
    restraint_requirement = _row_by_id(requirement_results, "requirement_id").get("S6B-004", {})

    payload = {
        "stage": "6D",
        "guardrail": "read_only_penalty_research_only_no_live_permission",
        "inputs": {key: safe_rel(path) for key, path in inputs.items()},
        "candidate_ledger_rows_loaded": len(ledger_rows),
        "restraint_requirement_result": restraint_requirement,
        "bucket_row_count": len(bucket_rows),
        "high_pressure_rescue_candidate_count": len(rescue_rows),
        "policy_row_count": len(policy_rows),
        "next_stage_dependency": "Use as a soft-penalty research workbench before any Stage 6 rewrite specification.",
    }

    _write_csv(outputs["bucket_scorecard_csv"], bucket_rows, force=bool(args.force))
    _write_csv(outputs["rescue_candidates_csv"], rescue_rows, force=bool(args.force))
    _write_csv(outputs["policy_matrix_csv"], policy_rows, force=bool(args.force))
    _write_csv(outputs["next_actions_csv"], next_actions, force=bool(args.force))
    _write_json(outputs["json"], payload, force=bool(args.force))
    _write_text(
        outputs["md"],
        _render_md(
            bucket_rows=bucket_rows,
            rescue_rows=rescue_rows,
            policy_rows=policy_rows,
            next_actions=next_actions,
            output_paths=outputs,
        ),
        force=bool(args.force),
    )
    print(f"[OK] Wrote Stage 6D restraint calibration workbench: {safe_rel(outputs['md'])}")


if __name__ == "__main__":
    main()
