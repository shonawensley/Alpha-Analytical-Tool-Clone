#!/usr/bin/env python3
"""Create the Stage-6E support modifier narrowing workbench.

Stage 6E is read-only. It decomposes Stage 6B support evidence into paired
support-on/support-off buckets, narrow candidate pockets, and failure modes.
It does not alter live scoring, candidate generation, translator logic, budget
logic, or legacy infrastructure.
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
STAGE6E_PREFIX = "ANALYSIS_ARENA__CYCLE__STAGE6E"


def _parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--runs2-dir", default=str(RUNS_2_DIR), help="RUNS_2 root containing Stage-5/Stage-6B outputs.")
    ap.add_argument("--output-dir", default=str(RUNS_2_DIR), help="Cycle-level output directory.")
    ap.add_argument("--force", action="store_true", help="Overwrite existing Stage-6E outputs.")
    return ap.parse_args()


def _input_paths(runs2_dir: Path) -> Dict[str, Path]:
    return {
        "value_ledger": runs2_dir / f"{STAGE5_PREFIX}_VALUE_LEVEL_REPLAY_LEDGER.csv",
        "scenario_decisions": runs2_dir / f"{READBACK_PREFIX}_SCENARIO_DECISIONS.csv",
        "requirement_results": runs2_dir / f"{READBACK_PREFIX}_REQUIREMENT_RESULTS.csv",
        "next_action_queue": runs2_dir / f"{READBACK_PREFIX}_NEXT_ACTION_QUEUE.csv",
        "support_ablation": runs2_dir / f"{STAGE6B_PREFIX}_SUPPORT_MODIFIER_ABLATION.csv",
    }


def _output_paths(output_dir: Path) -> Dict[str, Path]:
    return {
        "md": output_dir / f"{STAGE6E_PREFIX}_SUPPORT_MODIFIER_NARROWING_WORKBENCH.md",
        "json": output_dir / f"{STAGE6E_PREFIX}_SUPPORT_MODIFIER_NARROWING_WORKBENCH.json",
        "bucket_scorecard_csv": output_dir / f"{STAGE6E_PREFIX}_SUPPORT_BUCKET_SCORECARD.csv",
        "narrowing_candidates_csv": output_dir / f"{STAGE6E_PREFIX}_SUPPORT_NARROWING_CANDIDATES.csv",
        "failure_modes_csv": output_dir / f"{STAGE6E_PREFIX}_SUPPORT_FAILURE_MODES.csv",
        "next_actions_csv": output_dir / f"{STAGE6E_PREFIX}_SUPPORT_NEXT_ACTIONS.csv",
    }


def _load_required_csv(path: Path, label: str) -> List[Dict[str, str]]:
    rows = _read_csv_rows(path)
    if not rows:
        raise SystemExit(f"Missing or empty Stage-6E input {label}: {safe_rel(path)}")
    return rows


def _row_by_id(rows: Sequence[Mapping[str, Any]], field: str) -> Dict[str, Mapping[str, Any]]:
    return {str(row.get(field) or ""): row for row in rows}


def _support_bool(row: Mapping[str, Any]) -> bool:
    return str(row.get("support_context_present") or "").lower() == "true"


def _support_label(row: Mapping[str, Any]) -> str:
    return "support_on" if _support_bool(row) else "support_off"


def _pressure(row: Mapping[str, Any]) -> str:
    return str(row.get("restraint_pressure") or "unknown").strip().lower() or "unknown"


def _bucket_key_parts(row: Mapping[str, Any]) -> List[Tuple[str, str, Dict[str, str]]]:
    support = _support_label(row)
    mechanism = str(row.get("mechanism_family") or "unknown")
    lane = str(row.get("prototype_lane") or "unknown")
    pressure = _pressure(row)
    cluster = str(row.get("cluster_key") or "unknown")
    return [
        (
            f"support::{support}",
            "global",
            {
                "bucket_type": "global",
                "support_context": support,
                "mechanism_family": "",
                "prototype_lane": "",
                "restraint_pressure": "",
                "cluster_key": "",
            },
        ),
        (
            f"support_mechanism::{support}::{mechanism}",
            f"mechanism::{mechanism}",
            {
                "bucket_type": "mechanism",
                "support_context": support,
                "mechanism_family": mechanism,
                "prototype_lane": "",
                "restraint_pressure": "",
                "cluster_key": "",
            },
        ),
        (
            f"support_lane::{support}::{lane}",
            f"lane::{lane}",
            {
                "bucket_type": "lane",
                "support_context": support,
                "mechanism_family": "",
                "prototype_lane": lane,
                "restraint_pressure": "",
                "cluster_key": "",
            },
        ),
        (
            f"support_pressure::{support}::{pressure}",
            f"pressure::{pressure}",
            {
                "bucket_type": "pressure",
                "support_context": support,
                "mechanism_family": "",
                "prototype_lane": "",
                "restraint_pressure": pressure,
                "cluster_key": "",
            },
        ),
        (
            f"support_mechanism_lane::{support}::{mechanism}::{lane}",
            f"mechanism_lane::{mechanism}::{lane}",
            {
                "bucket_type": "mechanism_lane",
                "support_context": support,
                "mechanism_family": mechanism,
                "prototype_lane": lane,
                "restraint_pressure": "",
                "cluster_key": "",
            },
        ),
        (
            f"support_cluster::{support}::{cluster}",
            f"cluster::{cluster}",
            {
                "bucket_type": "cluster",
                "support_context": support,
                "mechanism_family": mechanism,
                "prototype_lane": lane,
                "restraint_pressure": pressure,
                "cluster_key": cluster,
            },
        ),
    ]


def _bucket_scorecard_rows(
    ledger_rows: Sequence[Mapping[str, Any]],
    *,
    primary: Mapping[str, Any],
    support_off_reference: Mapping[str, Any],
) -> List[Dict[str, Any]]:
    grouped: MutableMapping[str, Dict[str, Any]] = defaultdict(_new_agg)
    labels: Dict[str, Dict[str, str]] = {}
    peer_groups: Dict[str, Dict[str, str]] = {}
    for row in ledger_rows:
        if not _is_candidate_row(row):
            continue
        for bucket_id, peer_key, label in _bucket_key_parts(row):
            labels[bucket_id] = {"bucket_id": bucket_id, "peer_key": peer_key, **label}
            peer_groups.setdefault(peer_key, {})[_support_label(row)] = bucket_id
            _add_to_agg(grouped[bucket_id], row)

    raw_rows: Dict[str, Dict[str, Any]] = {}
    primary_fp = _safe_float(primary.get("false_positive_proxy_rate"))
    primary_yield = _safe_float(primary.get("pool_normalized_positive_yield"))
    support_off_fp = _safe_float(support_off_reference.get("false_positive_proxy_rate"))
    support_off_yield = _safe_float(support_off_reference.get("pool_normalized_positive_yield"))
    for bucket_id, agg in grouped.items():
        row = _agg_to_row(labels[bucket_id], agg)
        row["false_positive_delta_vs_primary"] = _safe_float(row.get("false_positive_proxy_rate")) - primary_fp
        row["yield_delta_vs_primary"] = _safe_float(row.get("pool_normalized_positive_yield")) - primary_yield
        row["false_positive_delta_vs_global_support_off"] = _safe_float(row.get("false_positive_proxy_rate")) - support_off_fp
        row["yield_delta_vs_global_support_off"] = _safe_float(row.get("pool_normalized_positive_yield")) - support_off_yield
        raw_rows[bucket_id] = row

    rows: List[Dict[str, Any]] = []
    for bucket_id, row in raw_rows.items():
        peer_key = str(row.get("peer_key") or "")
        peer_support = peer_groups.get(peer_key, {})
        support = str(row.get("support_context") or "")
        peer_bucket_id = peer_support.get("support_off" if support == "support_on" else "support_on", "")
        peer = raw_rows.get(peer_bucket_id, {})
        row["peer_bucket_id"] = peer_bucket_id
        row["peer_active_state_days"] = _safe_int(peer.get("active_state_days"))
        row["peer_total_overlap_values"] = _safe_int(peer.get("total_overlap_values"))
        row["peer_positive_conversion_event_count"] = _safe_int(peer.get("positive_conversion_event_count"))
        row["false_positive_delta_vs_peer"] = _safe_float(row.get("false_positive_proxy_rate")) - _safe_float(peer.get("false_positive_proxy_rate"))
        row["yield_delta_vs_peer"] = _safe_float(row.get("pool_normalized_positive_yield")) - _safe_float(peer.get("pool_normalized_positive_yield"))
        row["support_readback_posture"] = _support_posture(row=row, peer=peer)
        rows.append(row)

    return sorted(
        rows,
        key=lambda row: (
            str(row.get("support_context") or "") != "support_on",
            str(row.get("support_readback_posture") or "") != "narrow_support_modifier_candidate",
            -_safe_int(row.get("positive_conversion_event_count")),
            _safe_float(row.get("false_positive_proxy_rate")),
        ),
    )


def _support_posture(*, row: Mapping[str, Any], peer: Mapping[str, Any]) -> str:
    support = str(row.get("support_context") or "")
    state_days = _safe_int(row.get("active_state_days"))
    positive = _safe_int(row.get("positive_conversion_event_count"))
    peer_state_days = _safe_int(peer.get("active_state_days"))
    peer_total = _safe_int(peer.get("total_overlap_values"))
    fp_delta = _safe_float(row.get("false_positive_delta_vs_peer"))
    yield_delta = _safe_float(row.get("yield_delta_vs_peer"))
    if support != "support_on":
        return "support_off_reference"
    if not peer:
        return "no_peer_retest_only"
    if peer_state_days < 3 or peer_total < 50:
        return "weak_peer_denominator_retest_only"
    if state_days < 3 or positive < 10:
        return "low_denominator_retest_only"
    if fp_delta <= 0 and yield_delta >= 0:
        return "narrow_support_modifier_candidate"
    if fp_delta <= 0 or yield_delta >= 0:
        return "mixed_support_modifier_retest"
    return "support_on_failure_mode"


def _narrowing_candidate_rows(bucket_rows: Sequence[Mapping[str, Any]]) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for row in bucket_rows:
        posture = str(row.get("support_readback_posture") or "")
        if posture not in {"narrow_support_modifier_candidate", "mixed_support_modifier_retest"}:
            continue
        if str(row.get("support_context") or "") != "support_on":
            continue
        rows.append(
            {
                "candidate_id": f"S6E-SUPPORT-{len(rows) + 1:03d}",
                "bucket_id": row.get("bucket_id", ""),
                "bucket_type": row.get("bucket_type", ""),
                "peer_bucket_id": row.get("peer_bucket_id", ""),
                "mechanism_family": row.get("mechanism_family", ""),
                "prototype_lane": row.get("prototype_lane", ""),
                "restraint_pressure": row.get("restraint_pressure", ""),
                "cluster_key": row.get("cluster_key", ""),
                "ledger_rows": row.get("ledger_rows", 0),
                "active_state_days": row.get("active_state_days", 0),
                "peer_active_state_days": row.get("peer_active_state_days", 0),
                "peer_total_overlap_values": row.get("peer_total_overlap_values", 0),
                "peer_positive_conversion_event_count": row.get("peer_positive_conversion_event_count", 0),
                "positive_conversion_event_count": row.get("positive_conversion_event_count", 0),
                "false_positive_proxy_rate": row.get("false_positive_proxy_rate", 0.0),
                "pool_normalized_positive_yield": row.get("pool_normalized_positive_yield", 0.0),
                "false_positive_delta_vs_peer": row.get("false_positive_delta_vs_peer", 0.0),
                "yield_delta_vs_peer": row.get("yield_delta_vs_peer", 0.0),
                "recommended_use": posture,
                "stage_permission": "support_research_only",
                "live_permission": "none",
            }
        )
    return sorted(
        rows,
        key=lambda row: (
            str(row.get("recommended_use") or "") != "narrow_support_modifier_candidate",
            -_safe_int(row.get("positive_conversion_event_count")),
            _safe_float(row.get("false_positive_proxy_rate")),
        ),
    )


def _failure_mode_rows(
    *,
    bucket_rows: Sequence[Mapping[str, Any]],
    support_ablation_rows: Sequence[Mapping[str, Any]],
    requirement_results: Sequence[Mapping[str, Any]],
) -> List[Dict[str, Any]]:
    req = _row_by_id(requirement_results, "requirement_id").get("S6B-003", {})
    ablation = _row_by_id(support_ablation_rows, "support_ablation_bucket")
    rows = [
        {
            "failure_id": "S6E-FAIL-001",
            "failure_mode": "broad_support_on_is_not_a_positive_modifier",
            "evidence": str(req.get("evidence") or ""),
            "recommended_response": "Keep broad support-on out of scoring and search only for narrow paired buckets.",
            "live_permission": "none",
        },
        {
            "failure_id": "S6E-FAIL-002",
            "failure_mode": "support_gate_standalone_stays_context_only",
            "evidence": f"standalone_fp={_pct(ablation.get('support_gate_standalone_excluded', {}).get('false_positive_proxy_rate'))}; standalone_yield={_fmt(ablation.get('support_gate_standalone_excluded', {}).get('pool_normalized_positive_yield'))}",
            "recommended_response": "Do not convert support-gate context into candidate-pool permission.",
            "live_permission": "none",
        },
    ]
    failure_buckets = [
        row
        for row in bucket_rows
        if str(row.get("support_context") or "") == "support_on"
        and str(row.get("support_readback_posture") or "") == "support_on_failure_mode"
    ]
    for row in sorted(failure_buckets, key=lambda r: -_safe_int(r.get("positive_conversion_event_count")))[:20]:
        rows.append(
            {
                "failure_id": f"S6E-FAIL-{len(rows) + 1:03d}",
                "failure_mode": "narrow_bucket_support_on_failed_peer_test",
                "evidence": (
                    f"{row.get('bucket_id', '')}: fp_delta_vs_peer={_fmt(row.get('false_positive_delta_vs_peer'))}; "
                    f"yield_delta_vs_peer={_fmt(row.get('yield_delta_vs_peer'))}; positive={_safe_int(row.get('positive_conversion_event_count'))}"
                ),
                "recommended_response": "Keep as support context only unless a future window reverses the paired peer test.",
                "live_permission": "none",
            }
        )
    return rows


def _next_action_rows(candidate_rows: Sequence[Mapping[str, Any]], failure_rows: Sequence[Mapping[str, Any]]) -> List[Dict[str, Any]]:
    strong = [row for row in candidate_rows if str(row.get("recommended_use") or "") == "narrow_support_modifier_candidate"]
    return [
        {
            "priority": 1,
            "action_type": "support_narrowing_replay",
            "subject": "narrow_support_modifier_candidates",
            "action": "Replay only narrow support candidates that beat their support-off peer; do not use broad support-on.",
            "evidence": f"{len(strong)} strict candidates and {len(candidate_rows)} total retest candidates found.",
            "allowed_permission": "support_research_only",
            "live_permission": "none",
        },
        {
            "priority": 2,
            "action_type": "support_failure_quarantine",
            "subject": "support_on_failure_modes",
            "action": "Keep failed support-on buckets as context-only annotations and exclude from candidate-pool permission.",
            "evidence": f"{len(failure_rows)} support failure rows generated.",
            "allowed_permission": "context_only",
            "live_permission": "none",
        },
        {
            "priority": 3,
            "action_type": "future_window_confirmation",
            "subject": "support_modifier_boundary",
            "action": "Rerun Stage 6E after the next fresh Stage 6B replay to test whether any support pockets repeat.",
            "evidence": "Current support readback is March-window evidence and remains research-only.",
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
    candidate_rows: Sequence[Mapping[str, Any]],
    failure_rows: Sequence[Mapping[str, Any]],
    next_actions: Sequence[Mapping[str, Any]],
    output_paths: Mapping[str, Path],
) -> str:
    top_candidates = list(candidate_rows[:10])
    lines: List[str] = [
        "# Analysis Arena Stage 6E Support Modifier Narrowing Workbench",
        "",
        "## Guardrail",
        "",
        "Stage 6E is read-only. It tests support context as a narrow paired modifier only; it does not change live scoring, candidate generation, translator logic, budget logic, or legacy infrastructure.",
        "",
        "## Executive Readback",
        "",
        f"- support bucket rows generated: `{len(bucket_rows)}`",
        f"- support narrowing/retest candidates generated: `{len(candidate_rows)}`",
        f"- support failure rows generated: `{len(failure_rows)}`",
        "- Broad support-on failed Stage 6B readback, so Stage 6E searches only for narrow support pockets that beat a matched support-off peer.",
        "",
        "## Top Support Narrowing Candidates",
        "",
    ]
    lines.extend(
        _table(
            ["candidate_id", "bucket_id", "peer", "positive", "fp_delta_peer", "yield_delta_peer", "recommended_use"],
            [
                [
                    row.get("candidate_id", ""),
                    row.get("bucket_id", ""),
                    row.get("peer_bucket_id", ""),
                    row.get("positive_conversion_event_count", ""),
                    _fmt(row.get("false_positive_delta_vs_peer")),
                    _fmt(row.get("yield_delta_vs_peer")),
                    row.get("recommended_use", ""),
                ]
                for row in top_candidates
            ],
        )
    )
    lines.extend(["", "## Failure Modes", ""])
    lines.extend(
        _table(
            ["failure_id", "failure_mode", "recommended_response"],
            [[row.get("failure_id", ""), row.get("failure_mode", ""), row.get("recommended_response", "")] for row in failure_rows[:12]],
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
            f"- support_bucket_scorecard: `{safe_rel(output_paths['bucket_scorecard_csv'])}`",
            f"- support_narrowing_candidates: `{safe_rel(output_paths['narrowing_candidates_csv'])}`",
            f"- support_failure_modes: `{safe_rel(output_paths['failure_modes_csv'])}`",
            f"- support_next_actions: `{safe_rel(output_paths['next_actions_csv'])}`",
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
    support_ablation_rows = _load_required_csv(inputs["support_ablation"], "Stage 6B support ablation")

    scenarios = _row_by_id(scenario_decisions, "scenario_id")
    primary = scenarios.get("primary_restrained_candidate_expression", {})
    support_ablation = _row_by_id(support_ablation_rows, "support_ablation_bucket")
    support_off_reference = support_ablation.get("all_candidate_support_off", {})

    bucket_rows = _bucket_scorecard_rows(
        ledger_rows,
        primary=primary,
        support_off_reference=support_off_reference,
    )
    candidate_rows = _narrowing_candidate_rows(bucket_rows)
    failure_rows = _failure_mode_rows(
        bucket_rows=bucket_rows,
        support_ablation_rows=support_ablation_rows,
        requirement_results=requirement_results,
    )
    next_actions = _next_action_rows(candidate_rows, failure_rows)
    support_requirement = _row_by_id(requirement_results, "requirement_id").get("S6B-003", {})

    payload = {
        "stage": "6E",
        "guardrail": "read_only_support_research_only_no_live_permission",
        "inputs": {key: safe_rel(path) for key, path in inputs.items()},
        "candidate_ledger_rows_loaded": len(ledger_rows),
        "support_requirement_result": support_requirement,
        "bucket_row_count": len(bucket_rows),
        "support_narrowing_candidate_count": len(candidate_rows),
        "support_failure_mode_count": len(failure_rows),
        "next_stage_dependency": "Use only as support modifier research before any Stage 6 rewrite specification.",
    }

    _write_csv(outputs["bucket_scorecard_csv"], bucket_rows, force=bool(args.force))
    _write_csv(outputs["narrowing_candidates_csv"], candidate_rows, force=bool(args.force))
    _write_csv(outputs["failure_modes_csv"], failure_rows, force=bool(args.force))
    _write_csv(outputs["next_actions_csv"], next_actions, force=bool(args.force))
    _write_json(outputs["json"], payload, force=bool(args.force))
    _write_text(
        outputs["md"],
        _render_md(
            bucket_rows=bucket_rows,
            candidate_rows=candidate_rows,
            failure_rows=failure_rows,
            next_actions=next_actions,
            output_paths=outputs,
        ),
        force=bool(args.force),
    )
    print(f"[OK] Wrote Stage 6E support modifier narrowing workbench: {safe_rel(outputs['md'])}")


if __name__ == "__main__":
    main()
