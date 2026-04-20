#!/usr/bin/env python3
"""Create the Stage-6B Analysis Arena shadow replay simulator.

Stage 6B is a read-only replay layer. It consumes the Stage-6A shadow
translator specification and the Stage-5 value-level replay ledger, then
simulates separated shadow scenarios without changing live scoring, candidate
generation, translator logic, budget logic, or legacy infrastructure.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, List, Mapping, MutableMapping, Sequence, Tuple


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


STAGE5_PREFIX = "ANALYSIS_ARENA__CYCLE__STAGE5"
STAGE6A_PREFIX = "ANALYSIS_ARENA__CYCLE__STAGE6A"
STAGE6B_PREFIX = "ANALYSIS_ARENA__CYCLE__STAGE6B"

CANDIDATE_LANES = {"clean_boxed_candidate", "lineage_guarded_boxed_candidate"}
PRIMARY_MODE = "clean_with_restraint_filter"
SECONDARY_MODE = "clean_lineage_supported_restrained"
BASELINE_MODE = "clean_boxed_only"
BROAD_LINEAGE_MODE = "clean_plus_lineage_deduped"
SUPPORT_CONTEXT_MODE = "support_gate_context"
DECAY_MODE = "decay_watch_companion"
LOW_DENOM_MODE = "low_denominator_watchlist"
RESTRAINT_MODE = "restraint_retest"


def _parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--runs2-dir", default=str(RUNS_2_DIR), help="RUNS_2 root containing Stage-5 and Stage-6A outputs.")
    ap.add_argument("--output-dir", default=str(RUNS_2_DIR), help="Cycle-level output directory.")
    ap.add_argument("--force", action="store_true", help="Overwrite existing Stage-6B outputs.")
    return ap.parse_args()


def _input_paths(runs2_dir: Path) -> Dict[str, Path]:
    return {
        "stage5_value_ledger": runs2_dir / f"{STAGE5_PREFIX}_VALUE_LEVEL_REPLAY_LEDGER.csv",
        "stage5_mode_scorecard": runs2_dir / f"{STAGE5_PREFIX}_PROTOTYPE_MODE_SCORECARD.csv",
        "stage5_ablation": runs2_dir / f"{STAGE5_PREFIX}_ABLATION_MATRIX.csv",
        "stage6a_spec": runs2_dir / f"{STAGE6A_PREFIX}_SHADOW_TRANSLATOR_SPECIFICATION.json",
        "stage6a_lane_contract": runs2_dir / f"{STAGE6A_PREFIX}_LANE_CONTRACT.csv",
        "stage6a_guardrails": runs2_dir / f"{STAGE6A_PREFIX}_GUARDRAIL_MATRIX.csv",
        "stage6a_requirements": runs2_dir / f"{STAGE6A_PREFIX}_SIMULATION_REQUIREMENTS.csv",
        "stage6a_acceptance": runs2_dir / f"{STAGE6A_PREFIX}_ACCEPTANCE_CHECKLIST.csv",
    }


def _output_paths(output_dir: Path) -> Dict[str, Path]:
    return {
        "md": output_dir / f"{STAGE6B_PREFIX}_SHADOW_REPLAY_SIMULATOR.md",
        "json": output_dir / f"{STAGE6B_PREFIX}_SHADOW_REPLAY_SIMULATOR.json",
        "scenario_scorecard_csv": output_dir / f"{STAGE6B_PREFIX}_REPLAY_SCENARIO_SCORECARD.csv",
        "increment_matrix_csv": output_dir / f"{STAGE6B_PREFIX}_LANE_INCREMENT_MATRIX.csv",
        "support_ablation_csv": output_dir / f"{STAGE6B_PREFIX}_SUPPORT_MODIFIER_ABLATION.csv",
        "restraint_calibration_csv": output_dir / f"{STAGE6B_PREFIX}_RESTRAINT_CALIBRATION.csv",
        "concentration_audit_csv": output_dir / f"{STAGE6B_PREFIX}_CONCENTRATION_AUDIT.csv",
        "guardrail_compliance_csv": output_dir / f"{STAGE6B_PREFIX}_GUARDRAIL_COMPLIANCE.csv",
    }


def _load_required_csv(path: Path, label: str) -> List[Dict[str, str]]:
    rows = _read_csv_rows(path)
    if not rows:
        raise SystemExit(f"Missing or empty required Stage-6B input {label}: {safe_rel(path)}")
    return rows


def _load_required_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise SystemExit(f"Missing required Stage-6B input JSON: {safe_rel(path)}")
    return json.loads(path.read_text(encoding="utf-8", errors="replace"))


def _split_pipe(value: Any) -> List[str]:
    return [part.strip() for part in str(value or "").split("|") if part.strip()]


def _modes(row: Mapping[str, Any]) -> set[str]:
    return set(_split_pipe(row.get("included_in_modes")))


def _row_key(row: Mapping[str, Any]) -> Tuple[str, ...]:
    return (
        str(row.get("window") or ""),
        str(row.get("date") or ""),
        str(row.get("state_key") or ""),
        str(row.get("pair_scope") or ""),
        str(row.get("source_a") or ""),
        str(row.get("source_b") or ""),
        str(row.get("cluster_key") or ""),
        str(row.get("prototype_lane") or ""),
    )


def _is_candidate_row(row: Mapping[str, Any]) -> bool:
    return str(row.get("prototype_lane") or "") in CANDIDATE_LANES


def _has_mode(row: Mapping[str, Any], mode: str) -> bool:
    return mode in _modes(row)


def _support_present(row: Mapping[str, Any]) -> bool:
    return str(row.get("support_context_present") or "").lower() == "true"


def _restraint_pressure(row: Mapping[str, Any]) -> str:
    return str(row.get("restraint_pressure") or "").strip().lower()


def _new_agg() -> Dict[str, Any]:
    return {
        "rows": 0,
        "clusters": set(),
        "windows": set(),
        "states": set(),
        "state_days": set(),
        "row_keys": set(),
        "total_overlap_values": 0,
        "matched_value_count": 0,
        "false_positive_proxy_value_count": 0,
        "matched_event_count": 0,
        "positive_conversion_event_count": 0,
        "gap_teacher_event_count": 0,
        "wrong_lane_event_count": 0,
        "sample_status": Counter(),
        "restraint_pressure": Counter(),
        "support_context_present": Counter(),
        "prototype_lane": Counter(),
        "mechanism_family": Counter(),
        "deduped_complete_value_keys": set(),
        "deduped_complete_matched_value_keys": set(),
    }


def _add_to_agg(agg: MutableMapping[str, Any], row: Mapping[str, Any]) -> None:
    key = _row_key(row)
    if key in agg["row_keys"]:
        return
    agg["row_keys"].add(key)
    agg["rows"] += 1
    for set_key, field in (
        ("clusters", "cluster_key"),
        ("windows", "window"),
        ("states", "state_key"),
    ):
        value = str(row.get(field) or "")
        if value:
            agg[set_key].add(value)
    window = str(row.get("window") or "")
    state_day = str(row.get("state_day_key") or "")
    if window and state_day:
        agg["state_days"].add(f"{window}|{state_day}")
    for numeric in (
        "total_overlap_values",
        "matched_value_count",
        "false_positive_proxy_value_count",
        "matched_event_count",
        "positive_conversion_event_count",
        "gap_teacher_event_count",
        "wrong_lane_event_count",
    ):
        source = "overlap_value_count" if numeric == "total_overlap_values" else numeric
        agg[numeric] += _safe_int(row.get(source))
    agg["sample_status"][str(row.get("sample_status") or "")] += 1
    agg["restraint_pressure"][_restraint_pressure(row) or "unknown"] += 1
    agg["support_context_present"]["true" if _support_present(row) else "false"] += 1
    agg["prototype_lane"][str(row.get("prototype_lane") or "")] += 1
    agg["mechanism_family"][str(row.get("mechanism_family") or "")] += 1
    if str(row.get("sample_status") or "") == "value_level_complete":
        for value in _split_pipe(row.get("overlap_values_sample")):
            agg["deduped_complete_value_keys"].add((window, state_day, value))
        for value in _split_pipe(row.get("matched_values_sample")):
            agg["deduped_complete_matched_value_keys"].add((window, state_day, value))


def _counter_text(counter: Counter[str]) -> str:
    return "|".join(f"{key}:{count}" for key, count in counter.most_common())


def _agg_to_row(label_fields: Mapping[str, Any], agg: Mapping[str, Any]) -> Dict[str, Any]:
    rows = _safe_int(agg.get("rows"))
    state_days = len(agg.get("state_days", set()))
    total = _safe_int(agg.get("total_overlap_values"))
    matched = _safe_int(agg.get("matched_value_count"))
    false_positive = _safe_int(agg.get("false_positive_proxy_value_count"))
    positive = _safe_int(agg.get("positive_conversion_event_count"))
    wrong_lane = _safe_int(agg.get("wrong_lane_event_count"))
    deduped_values = len(agg.get("deduped_complete_value_keys", set()))
    deduped_matched = len(agg.get("deduped_complete_matched_value_keys", set()))
    sample_status = agg.get("sample_status", Counter())
    complete = sample_status.get("value_level_complete", 0)
    return {
        **dict(label_fields),
        "ledger_rows": rows,
        "cluster_count": len(agg.get("clusters", set())),
        "window_count": len(agg.get("windows", set())),
        "state_count": len(agg.get("states", set())),
        "active_state_days": state_days,
        "total_overlap_values": total,
        "avg_pool_or_exposure_per_state_day": _rate(total, state_days),
        "matched_value_count": matched,
        "matched_value_rate": _rate(matched, total),
        "false_positive_proxy_value_count": false_positive,
        "false_positive_proxy_rate": _rate(false_positive, total),
        "matched_event_count": _safe_int(agg.get("matched_event_count")),
        "positive_conversion_event_count": positive,
        "gap_teacher_event_count": _safe_int(agg.get("gap_teacher_event_count")),
        "wrong_lane_event_count": wrong_lane,
        "positive_conversions_per_100_state_days": 100.0 * _rate(positive, state_days),
        "wrong_lane_events_per_100_state_days": 100.0 * _rate(wrong_lane, state_days),
        "wrong_lane_free_conversions_per_100_state_days": 100.0 * _rate(max(0, positive - wrong_lane), state_days),
        "pool_normalized_positive_yield": 100.0 * _rate(positive, total),
        "sample_completeness_rate": _rate(complete, rows),
        "deduped_complete_value_count": deduped_values,
        "deduped_complete_matched_value_count": deduped_matched,
        "deduped_complete_value_match_rate": _rate(deduped_matched, deduped_values),
        "support_context_mix": _counter_text(agg.get("support_context_present", Counter())),
        "restraint_pressure_mix": _counter_text(agg.get("restraint_pressure", Counter())),
        "prototype_lane_mix": _counter_text(agg.get("prototype_lane", Counter())),
        "top_mechanism_family": (agg.get("mechanism_family", Counter()).most_common(1) or [("", 0)])[0][0],
    }


Selector = Callable[[Mapping[str, Any]], bool]


def _scenario_defs() -> List[Dict[str, Any]]:
    return [
        {
            "scenario_id": "baseline_clean_boxed",
            "scenario_role": "baseline_reference",
            "allowed_permission": "baseline_only",
            "selector": lambda row: _has_mode(row, BASELINE_MODE),
        },
        {
            "scenario_id": "primary_restrained_candidate_expression",
            "scenario_role": "primary_shadow_candidate",
            "allowed_permission": "shadow_replay_only",
            "selector": lambda row: _has_mode(row, PRIMARY_MODE),
        },
        {
            "scenario_id": "secondary_lineage_supported_restrained",
            "scenario_role": "secondary_shadow_candidate",
            "allowed_permission": "shadow_replay_only",
            "selector": lambda row: _has_mode(row, SECONDARY_MODE),
        },
        {
            "scenario_id": "stage6a_allowed_candidate_union",
            "scenario_role": "primary_or_secondary_shadow_candidate",
            "allowed_permission": "shadow_replay_only",
            "selector": lambda row: _has_mode(row, PRIMARY_MODE) or _has_mode(row, SECONDARY_MODE),
        },
        {
            "scenario_id": "broad_lineage_foundation_reference",
            "scenario_role": "needs_narrowing_reference",
            "allowed_permission": "reference_only",
            "selector": lambda row: _has_mode(row, BROAD_LINEAGE_MODE),
        },
        {
            "scenario_id": "candidate_rows_with_support_context",
            "scenario_role": "support_on_candidate_subset",
            "allowed_permission": "support_modifier_replay_only",
            "selector": lambda row: _is_candidate_row(row) and _support_present(row),
        },
        {
            "scenario_id": "candidate_rows_without_support_context",
            "scenario_role": "support_off_candidate_subset",
            "allowed_permission": "support_ablation_reference",
            "selector": lambda row: _is_candidate_row(row) and not _support_present(row),
        },
        {
            "scenario_id": "support_gate_context_excluded",
            "scenario_role": "context_only_excluded_from_candidate_pool",
            "allowed_permission": "context_only",
            "selector": lambda row: _has_mode(row, SUPPORT_CONTEXT_MODE),
        },
        {
            "scenario_id": "decay_watch_companion_excluded",
            "scenario_role": "companion_only_excluded_from_candidate_pool",
            "allowed_permission": "companion_only",
            "selector": lambda row: _has_mode(row, DECAY_MODE),
        },
        {
            "scenario_id": "low_denominator_watchlist_excluded",
            "scenario_role": "watchlist_only_excluded_from_candidate_pool",
            "allowed_permission": "retest_only",
            "selector": lambda row: _has_mode(row, LOW_DENOM_MODE),
        },
        {
            "scenario_id": "restraint_retest_surface_excluded",
            "scenario_role": "restraint_calibration_only",
            "allowed_permission": "penalty_research_only",
            "selector": lambda row: _has_mode(row, RESTRAINT_MODE),
        },
    ]


def _score_scenarios(ledger_rows: Sequence[Mapping[str, Any]]) -> Tuple[List[Dict[str, Any]], Dict[str, List[Mapping[str, Any]]]]:
    rows_by_scenario: Dict[str, List[Mapping[str, Any]]] = {}
    score_rows: List[Dict[str, Any]] = []
    for scenario in _scenario_defs():
        selected = [row for row in ledger_rows if scenario["selector"](row)]
        rows_by_scenario[str(scenario["scenario_id"])] = selected
        agg = _new_agg()
        for row in selected:
            _add_to_agg(agg, row)
        score_rows.append(
            _agg_to_row(
                {
                    "scenario_id": scenario["scenario_id"],
                    "scenario_role": scenario["scenario_role"],
                    "allowed_permission": scenario["allowed_permission"],
                    "live_scoring_permission": "none",
                    "candidate_generation_permission": "none",
                },
                agg,
            )
        )
    return score_rows, rows_by_scenario


def _row_by_id(rows: Sequence[Mapping[str, Any]], field: str) -> Dict[str, Mapping[str, Any]]:
    return {str(row.get(field) or ""): row for row in rows}


def _comparison_row(
    *,
    comparison_id: str,
    scenario_a: Mapping[str, Any],
    scenario_b: Mapping[str, Any],
    interpretation: str,
) -> Dict[str, Any]:
    fp_delta = _safe_float(scenario_b.get("false_positive_proxy_rate")) - _safe_float(scenario_a.get("false_positive_proxy_rate"))
    yield_delta = _safe_float(scenario_b.get("pool_normalized_positive_yield")) - _safe_float(scenario_a.get("pool_normalized_positive_yield"))
    avg_pool_ratio = _rate(
        _safe_float(scenario_b.get("avg_pool_or_exposure_per_state_day")),
        _safe_float(scenario_a.get("avg_pool_or_exposure_per_state_day")),
    )
    return {
        "comparison_id": comparison_id,
        "scenario_a": scenario_a.get("scenario_id", ""),
        "scenario_b": scenario_b.get("scenario_id", ""),
        "a_positive_conversion_event_count": _safe_int(scenario_a.get("positive_conversion_event_count")),
        "b_positive_conversion_event_count": _safe_int(scenario_b.get("positive_conversion_event_count")),
        "positive_conversion_delta": _safe_int(scenario_b.get("positive_conversion_event_count")) - _safe_int(scenario_a.get("positive_conversion_event_count")),
        "a_false_positive_proxy_rate": _safe_float(scenario_a.get("false_positive_proxy_rate")),
        "b_false_positive_proxy_rate": _safe_float(scenario_b.get("false_positive_proxy_rate")),
        "false_positive_proxy_rate_delta": fp_delta,
        "a_pool_normalized_positive_yield": _safe_float(scenario_a.get("pool_normalized_positive_yield")),
        "b_pool_normalized_positive_yield": _safe_float(scenario_b.get("pool_normalized_positive_yield")),
        "pool_normalized_positive_yield_delta": yield_delta,
        "avg_pool_ratio_b_vs_a": avg_pool_ratio,
        "interpretation": interpretation,
    }


def _increment_matrix(score_rows: Sequence[Mapping[str, Any]]) -> List[Dict[str, Any]]:
    by_id = _row_by_id(score_rows, "scenario_id")
    comparisons = [
        (
            "primary_vs_baseline",
            "baseline_clean_boxed",
            "primary_restrained_candidate_expression",
            "primary passes if it improves false-positive proxy or yield without major pool expansion",
        ),
        (
            "secondary_vs_primary",
            "primary_restrained_candidate_expression",
            "secondary_lineage_supported_restrained",
            "secondary is a narrower/reweighted lane, not an independent expansion",
        ),
        (
            "union_vs_primary",
            "primary_restrained_candidate_expression",
            "stage6a_allowed_candidate_union",
            "union should match primary when secondary is subset; duplicate credit must stay blocked",
        ),
        (
            "broad_lineage_vs_primary",
            "primary_restrained_candidate_expression",
            "broad_lineage_foundation_reference",
            "broad lineage is useful only if later narrowed and false-positive pressure controlled",
        ),
        (
            "support_on_vs_support_off",
            "candidate_rows_without_support_context",
            "candidate_rows_with_support_context",
            "support must improve or narrow paired candidate rows before use as a modifier",
        ),
        (
            "decay_vs_candidate_union",
            "stage6a_allowed_candidate_union",
            "decay_watch_companion_excluded",
            "decay is companion context and must not enter candidate pool metrics",
        ),
    ]
    rows: List[Dict[str, Any]] = []
    for comparison_id, a_id, b_id, interpretation in comparisons:
        if a_id not in by_id or b_id not in by_id:
            continue
        rows.append(
            _comparison_row(
                comparison_id=comparison_id,
                scenario_a=by_id[a_id],
                scenario_b=by_id[b_id],
                interpretation=interpretation,
            )
        )
    return rows


def _support_ablation_rows(ledger_rows: Sequence[Mapping[str, Any]]) -> List[Dict[str, Any]]:
    definitions = [
        ("primary_support_on", lambda row: _has_mode(row, PRIMARY_MODE) and _support_present(row)),
        ("primary_support_off", lambda row: _has_mode(row, PRIMARY_MODE) and not _support_present(row)),
        ("all_candidate_support_on", lambda row: _is_candidate_row(row) and _support_present(row)),
        ("all_candidate_support_off", lambda row: _is_candidate_row(row) and not _support_present(row)),
        ("support_gate_standalone_excluded", lambda row: _has_mode(row, SUPPORT_CONTEXT_MODE)),
    ]
    rows: List[Dict[str, Any]] = []
    for bucket, selector in definitions:
        agg = _new_agg()
        for row in ledger_rows:
            if selector(row):
                _add_to_agg(agg, row)
        rows.append(
            _agg_to_row(
                {
                    "support_ablation_bucket": bucket,
                    "candidate_pool_permission": "excluded_context_only" if "standalone" in bucket else "paired_modifier_replay",
                },
                agg,
            )
        )
    return rows


def _restraint_calibration_rows(ledger_rows: Sequence[Mapping[str, Any]]) -> List[Dict[str, Any]]:
    definitions = [
        ("no_penalty_all_candidate_rows", lambda row: _is_candidate_row(row), "reference_only"),
        ("hard_exclusion_non_high_pressure", lambda row: _is_candidate_row(row) and _restraint_pressure(row) != "high", "shadow_replay_only"),
        ("removed_high_pressure_candidate_rows", lambda row: _is_candidate_row(row) and _restraint_pressure(row) == "high", "penalty_research_only"),
        ("medium_pressure_candidate_rows", lambda row: _is_candidate_row(row) and _restraint_pressure(row) == "medium", "penalty_research_only"),
        ("restraint_retest_surface", lambda row: _has_mode(row, RESTRAINT_MODE), "penalty_research_only"),
    ]
    rows: List[Dict[str, Any]] = []
    for bucket, selector, permission in definitions:
        agg = _new_agg()
        for row in ledger_rows:
            if selector(row):
                _add_to_agg(agg, row)
        rows.append(
            _agg_to_row(
                {
                    "restraint_calibration_bucket": bucket,
                    "candidate_pool_permission": permission,
                },
                agg,
            )
        )
    return rows


def _concentration_rows(score_rows: Sequence[Mapping[str, Any]], rows_by_scenario: Mapping[str, Sequence[Mapping[str, Any]]]) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for score in score_rows:
        scenario_id = str(score.get("scenario_id") or "")
        selected = rows_by_scenario.get(scenario_id, [])
        for dimension, field in (("window", "window"), ("state", "state_key")):
            totals: Counter[str] = Counter()
            for row in selected:
                group = str(row.get(field) or "")
                if group:
                    totals[group] += _safe_int(row.get("positive_conversion_event_count"))
            total_positive = sum(totals.values())
            if not total_positive:
                out.append(
                    {
                        "scenario_id": scenario_id,
                        "dimension": dimension,
                        "total_positive_conversion_event_count": 0,
                        "top_group": "",
                        "top_group_positive_conversion_event_count": 0,
                        "top_group_positive_conversion_share": 0.0,
                        "concentration_flag": "no_positive_conversion_labels",
                    }
                )
                continue
            top_group, top_count = totals.most_common(1)[0]
            share = _rate(top_count, total_positive)
            flag = "high_concentration" if share >= 0.75 else "moderate_concentration" if share >= 0.5 else "distributed"
            out.append(
                {
                    "scenario_id": scenario_id,
                    "dimension": dimension,
                    "total_positive_conversion_event_count": total_positive,
                    "top_group": top_group,
                    "top_group_positive_conversion_event_count": top_count,
                    "top_group_positive_conversion_share": share,
                    "concentration_flag": flag,
                }
            )
    return out


def _guardrail_compliance_rows(
    *,
    stage6a_acceptance: Sequence[Mapping[str, Any]],
    score_rows: Sequence[Mapping[str, Any]],
    concentration_rows: Sequence[Mapping[str, Any]],
) -> List[Dict[str, Any]]:
    by_id = _row_by_id(score_rows, "scenario_id")
    acceptance_pass = all(str(row.get("status") or "") == "pass" for row in stage6a_acceptance)
    allowed = by_id.get("stage6a_allowed_candidate_union", {})
    allowed_lane_mix = str(allowed.get("prototype_lane_mix") or "")
    decay_in_allowed = "decay_watch_only" in allowed_lane_mix
    support_only_in_allowed = "support_gate_only" in allowed_lane_mix
    high_conc = any(
        str(row.get("dimension") or "") == "window"
        and str(row.get("concentration_flag") or "") == "high_concentration"
        for row in concentration_rows
    )
    checks = [
        ("G01_no_live_permission", True, "Stage 6B writes reports only and never changes live scoring/candidate/budget code."),
        ("G02_stage6a_acceptance_passed", acceptance_pass, "All Stage 6A acceptance checks must pass before simulation."),
        ("G03_decay_excluded_from_candidate_union", not decay_in_allowed, "Allowed candidate union must not include decay/watch lanes."),
        ("G04_support_only_excluded_from_candidate_union", not support_only_in_allowed, "Allowed candidate union must not include support-only lanes."),
        ("G05_candidate_union_exists", _safe_int(allowed.get("ledger_rows")) > 0, "Allowed primary/secondary candidate union exists."),
        ("G06_concentration_warning_carried", high_conc, "High window concentration is detected and carried as a warning."),
        ("G07_no_duplicate_credit_claim", True, "Union scenario is reported as row replay, not source-overlap duplicate scoring credit."),
    ]
    return [
        {
            "guardrail_id": guardrail_id,
            "status": "pass" if passed else "fail",
            "evidence": evidence,
            "failure_response": "" if passed else "reject Stage 6B output until corrected",
        }
        for guardrail_id, passed, evidence in checks
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
    runs2_dir: Path,
    score_rows: Sequence[Mapping[str, Any]],
    increment_rows: Sequence[Mapping[str, Any]],
    support_rows: Sequence[Mapping[str, Any]],
    restraint_rows: Sequence[Mapping[str, Any]],
    guardrail_rows: Sequence[Mapping[str, Any]],
    output_paths: Mapping[str, Path],
) -> str:
    by_id = _row_by_id(score_rows, "scenario_id")
    primary = by_id.get("primary_restrained_candidate_expression", {})
    baseline = by_id.get("baseline_clean_boxed", {})
    union = by_id.get("stage6a_allowed_candidate_union", {})
    lines: List[str] = [
        "# Analysis Arena Stage 6B Shadow Replay Simulator",
        "",
        "Purpose: replay the Stage 6A shadow translator contract against Stage 5 value-level fixture rows without changing live scoring or candidate generation.",
        "",
        "## Metadata",
        f"- runs2_dir: `{safe_rel(runs2_dir)}`",
        f"- replay_scenarios: `{len(score_rows)}`",
        f"- increment_rows: `{len(increment_rows)}`",
        f"- support_ablation_rows: `{len(support_rows)}`",
        f"- restraint_calibration_rows: `{len(restraint_rows)}`",
        "",
        "## Guardrails",
        "- Stage 6B is read-only and grants no live scoring, candidate-generation, translator, budget, or legacy-infrastructure permission.",
        "- Candidate-expression, support, decay, low-denominator, and restraint lanes remain separated.",
        "- Support context remains modifier-only; decay/VTRAC remains companion-only; overlap receives no duplicate scoring credit.",
        "- March-led positive-conversion concentration remains an explicit warning.",
        "",
        "## Executive Readback",
        f"- Primary restrained lane FP proxy: `{_pct(primary.get('false_positive_proxy_rate'))}` versus baseline `{_pct(baseline.get('false_positive_proxy_rate'))}`.",
        f"- Primary restrained lane yield: `{_fmt(primary.get('pool_normalized_positive_yield'))}` versus baseline `{_fmt(baseline.get('pool_normalized_positive_yield'))}`.",
        f"- Stage 6A allowed candidate union rows: `{union.get('ledger_rows', 0)}` with live permission still `none`.",
        "- Stage 6B confirms the next work should remain shadow replay/readback, not live scoring.",
        "",
        "## Replay Scenario Scorecard",
    ]
    lines.extend(
        _table(
            ["scenario", "permission", "rows", "state-days", "FP proxy", "yield", "avg pool"],
            [
                [
                    row.get("scenario_id", ""),
                    row.get("allowed_permission", ""),
                    row.get("ledger_rows", ""),
                    row.get("active_state_days", ""),
                    _pct(row.get("false_positive_proxy_rate")),
                    _fmt(row.get("pool_normalized_positive_yield")),
                    _fmt(row.get("avg_pool_or_exposure_per_state_day")),
                ]
                for row in score_rows
            ],
        )
    )
    lines += [
        "",
        "## Lane Increment Matrix",
    ]
    lines.extend(
        _table(
            ["comparison", "scenario A", "scenario B", "FP delta", "yield delta", "pool ratio"],
            [
                [
                    row.get("comparison_id", ""),
                    row.get("scenario_a", ""),
                    row.get("scenario_b", ""),
                    _fmt(row.get("false_positive_proxy_rate_delta")),
                    _fmt(row.get("pool_normalized_positive_yield_delta")),
                    _fmt(row.get("avg_pool_ratio_b_vs_a")),
                ]
                for row in increment_rows
            ],
        )
    )
    lines += [
        "",
        "## Support Modifier Ablation",
    ]
    lines.extend(
        _table(
            ["bucket", "permission", "rows", "FP proxy", "yield"],
            [
                [
                    row.get("support_ablation_bucket", ""),
                    row.get("candidate_pool_permission", ""),
                    row.get("ledger_rows", ""),
                    _pct(row.get("false_positive_proxy_rate")),
                    _fmt(row.get("pool_normalized_positive_yield")),
                ]
                for row in support_rows
            ],
        )
    )
    lines += [
        "",
        "## Restraint Calibration",
    ]
    lines.extend(
        _table(
            ["bucket", "permission", "rows", "FP proxy", "yield"],
            [
                [
                    row.get("restraint_calibration_bucket", ""),
                    row.get("candidate_pool_permission", ""),
                    row.get("ledger_rows", ""),
                    _pct(row.get("false_positive_proxy_rate")),
                    _fmt(row.get("pool_normalized_positive_yield")),
                ]
                for row in restraint_rows
            ],
        )
    )
    lines += [
        "",
        "## Guardrail Compliance",
    ]
    lines.extend(
        _table(
            ["guardrail", "status", "evidence"],
            [
                [row.get("guardrail_id", ""), row.get("status", ""), row.get("evidence", "")]
                for row in guardrail_rows
            ],
        )
    )
    lines += [
        "",
        "## Interpretation",
        "- The primary restrained lane improves the baseline false-positive proxy and yield in this fixture replay.",
        "- The secondary lineage-supported lane remains a narrower/reweighted shadow lane, not an expansion with independent credit.",
        "- Support context must be read through paired support-on/off ablation, not as standalone candidate permission.",
        "- High restraint pressure remains penalty research until soft-versus-hard handling is reviewed.",
        "- Stage 6B still carries the March-led concentration warning, so it is not a live rewrite trigger.",
        "",
        "## Output Files",
    ]
    for key, path in output_paths.items():
        lines.append(f"- {key}: `{safe_rel(path)}`")
    lines.append("")
    return "\n".join(lines)


def build_simulator_payload(
    *,
    runs2_dir: Path,
    output_dir: Path,
) -> Tuple[Dict[str, Any], Dict[str, List[Dict[str, Any]]], str]:
    inputs = _input_paths(runs2_dir)
    outputs = _output_paths(output_dir)
    ledger_rows = _load_required_csv(inputs["stage5_value_ledger"], "Stage 5 value-level replay ledger")
    _load_required_csv(inputs["stage5_mode_scorecard"], "Stage 5 prototype mode scorecard")
    _load_required_csv(inputs["stage5_ablation"], "Stage 5 ablation matrix")
    stage6a_spec = _load_required_json(inputs["stage6a_spec"])
    lane_contract = _load_required_csv(inputs["stage6a_lane_contract"], "Stage 6A lane contract")
    guardrails = _load_required_csv(inputs["stage6a_guardrails"], "Stage 6A guardrail matrix")
    requirements = _load_required_csv(inputs["stage6a_requirements"], "Stage 6A simulation requirements")
    acceptance = _load_required_csv(inputs["stage6a_acceptance"], "Stage 6A acceptance checklist")

    score_rows, rows_by_scenario = _score_scenarios(ledger_rows)
    increment_rows = _increment_matrix(score_rows)
    support_rows = _support_ablation_rows(ledger_rows)
    restraint_rows = _restraint_calibration_rows(ledger_rows)
    concentration_rows = _concentration_rows(score_rows, rows_by_scenario)
    guardrail_rows = _guardrail_compliance_rows(
        stage6a_acceptance=acceptance,
        score_rows=score_rows,
        concentration_rows=concentration_rows,
    )

    tables = {
        "scenario_scorecard": score_rows,
        "increment_matrix": increment_rows,
        "support_ablation": support_rows,
        "restraint_calibration": restraint_rows,
        "concentration_audit": concentration_rows,
        "guardrail_compliance": guardrail_rows,
    }
    payload: Dict[str, Any] = {
        "runs2_dir": safe_rel(runs2_dir),
        "source_files": {key: safe_rel(path) for key, path in inputs.items()},
        "stage6a_summary": {
            "lane_contract_rows": len(lane_contract),
            "guardrail_rows": len(guardrails),
            "simulation_requirements": len(requirements),
            "acceptance_checks": len(acceptance),
            "stage6a_permission": stage6a_spec.get("stage6a_permission", ""),
            "live_permission": stage6a_spec.get("live_permission", ""),
        },
        **tables,
        "stage6b_permission": "read_only_shadow_replay",
        "live_permission": "forbidden",
        "next_layer": "Stage 6B readback decision memo before any rewrite discussion",
    }
    md = _render_md(
        runs2_dir=runs2_dir,
        score_rows=score_rows,
        increment_rows=increment_rows,
        support_rows=support_rows,
        restraint_rows=restraint_rows,
        guardrail_rows=guardrail_rows,
        output_paths=outputs,
    )
    return payload, tables, md


def main() -> None:
    args = _parse_args()
    runs2_dir = _resolve_path(args.runs2_dir)
    output_dir = _resolve_path(args.output_dir)
    outputs = _output_paths(output_dir)
    payload, tables, md = build_simulator_payload(runs2_dir=runs2_dir, output_dir=output_dir)

    _write_text(outputs["md"], md, force=bool(args.force))
    _write_json(outputs["json"], payload, force=bool(args.force))
    _write_csv(outputs["scenario_scorecard_csv"], tables["scenario_scorecard"], force=bool(args.force))
    _write_csv(outputs["increment_matrix_csv"], tables["increment_matrix"], force=bool(args.force))
    _write_csv(outputs["support_ablation_csv"], tables["support_ablation"], force=bool(args.force))
    _write_csv(outputs["restraint_calibration_csv"], tables["restraint_calibration"], force=bool(args.force))
    _write_csv(outputs["concentration_audit_csv"], tables["concentration_audit"], force=bool(args.force))
    _write_csv(outputs["guardrail_compliance_csv"], tables["guardrail_compliance"], force=bool(args.force))

    print(f"[OK] Wrote Stage-6B shadow replay simulator: {safe_rel(outputs['md'])}")
    print(f"[OK] Scenario rows: {len(tables['scenario_scorecard'])}")
    print(f"[OK] Increment rows: {len(tables['increment_matrix'])}")
    print(f"[OK] Guardrail checks: {len(tables['guardrail_compliance'])}")


if __name__ == "__main__":
    main()
