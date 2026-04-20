#!/usr/bin/env python3
"""Create the Stage-5 Analysis Arena shadow translator fixture evaluator.

Stage 5 is a read-only evaluation harness. It takes Stage 4C prototype lanes
and replays them against completed Stage 2B pairing ledgers at the state-day
fixture level. It does not change live scoring, candidate generation,
translator logic, budget logic, or legacy infrastructure.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, MutableMapping, Sequence, Tuple


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


STAGE5_PREFIX = "ANALYSIS_ARENA__CYCLE__STAGE5"

CANDIDATE_LANES = {"clean_boxed_candidate", "lineage_guarded_boxed_candidate"}
SUPPORT_LANE = "support_gate_only"


def _parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--runs2-dir", default=str(RUNS_2_DIR), help="RUNS_2 root containing Stage-4C outputs.")
    ap.add_argument("--output-dir", default=str(RUNS_2_DIR), help="Cycle-level output directory.")
    ap.add_argument("--casebook-limit", type=int, default=120, help="Maximum Stage-5 casebook rows to emit.")
    ap.add_argument("--max-value-rows", type=int, default=0, help="Optional debugging limit. Default 0 means all rows.")
    ap.add_argument("--force", action="store_true", help="Overwrite existing Stage-5 outputs.")
    return ap.parse_args()


def _stage_paths(runs2_dir: Path) -> Dict[str, Path]:
    return {
        "stage4c_rules": runs2_dir / "ANALYSIS_ARENA__CYCLE__STAGE4C_PROTOTYPE_RULE_REGISTRY.csv",
        "stage4c_support": runs2_dir / "ANALYSIS_ARENA__CYCLE__STAGE4C_SUPPORT_GATE_EFFECTS.csv",
        "stage4c_restraint": runs2_dir / "ANALYSIS_ARENA__CYCLE__STAGE4C_RESTRAINT_APPLICATION_AUDIT.csv",
        "stage4_fixture": runs2_dir / "ANALYSIS_ARENA__CYCLE__STAGE4_FIXTURE_REPLAY_LEDGER.csv",
        "stage4_ablation": runs2_dir / "ANALYSIS_ARENA__CYCLE__STAGE4_SOURCE_A_B_OVERLAP_COMPARISON.csv",
        "stage4b_holdout": runs2_dir / "ANALYSIS_ARENA__CYCLE__STAGE4B_LEAVE_ONE_WINDOW_OUT_MATRIX.csv",
    }


def _cycle_paths(output_dir: Path) -> Dict[str, Path]:
    return {
        "md": output_dir / f"{STAGE5_PREFIX}_SHADOW_TRANSLATOR_FIXTURE_EVALUATOR.md",
        "json": output_dir / f"{STAGE5_PREFIX}_SHADOW_TRANSLATOR_FIXTURE_EVALUATOR.json",
        "value_completeness_csv": output_dir / f"{STAGE5_PREFIX}_VALUE_COMPLETENESS_AUDIT.csv",
        "value_ledger_csv": output_dir / f"{STAGE5_PREFIX}_VALUE_LEVEL_REPLAY_LEDGER.csv",
        "mode_scorecard_csv": output_dir / f"{STAGE5_PREFIX}_PROTOTYPE_MODE_SCORECARD.csv",
        "ablation_csv": output_dir / f"{STAGE5_PREFIX}_ABLATION_MATRIX.csv",
        "window_csv": output_dir / f"{STAGE5_PREFIX}_WINDOW_STRATIFICATION.csv",
        "state_csv": output_dir / f"{STAGE5_PREFIX}_STATE_STRATIFICATION.csv",
        "restraint_csv": output_dir / f"{STAGE5_PREFIX}_RESTRAINT_EFFECT_AUDIT.csv",
        "support_csv": output_dir / f"{STAGE5_PREFIX}_SUPPORT_GATE_ABLATION.csv",
        "pro44_csv": output_dir / f"{STAGE5_PREFIX}_PRO44_COMPLIANCE_CHECKLIST.csv",
        "casebook_csv": output_dir / f"{STAGE5_PREFIX}_VALUE_LEVEL_CASEBOOK.csv",
        "casebook_md": output_dir / f"{STAGE5_PREFIX}_VALUE_LEVEL_CASEBOOK.md",
    }


def _window_name_from_pairing_path(path: Path) -> str:
    return path.parent.name


def _split_pipe(value: Any) -> List[str]:
    return [part.strip() for part in str(value or "").split("|") if part.strip()]


def _sample_status(row: Dict[str, Any]) -> Tuple[str, int, int]:
    expected = _safe_int(row.get("overlap_value_count"))
    sample_count = len(_split_pipe(row.get("overlap_values_sample")))
    if expected == sample_count:
        return "value_level_complete", expected, sample_count
    if sample_count == 0 and expected > 0:
        return "aggregate_only_missing_sample", expected, sample_count
    if sample_count < expected:
        return "sample_truncated", expected, sample_count
    return "sample_count_exceeds_overlap_count", expected, sample_count


def _pair_keys(window: str, pair_scope: str, source_a: str, source_b: str) -> List[Tuple[str, str, str, str]]:
    return [
        (window, pair_scope, source_a, source_b),
        (window, pair_scope, source_b, source_a),
    ]


def _fixture_pair_map(
    fixture_rows: Sequence[Dict[str, str]],
    rules_by_cluster: Dict[str, Dict[str, str]],
) -> Dict[Tuple[str, str, str, str], List[str]]:
    out: Dict[Tuple[str, str, str, str], List[str]] = defaultdict(list)
    for row in fixture_rows:
        cluster_key = _cluster_key(row)
        if cluster_key not in rules_by_cluster:
            continue
        window = str(row.get("window") or "")
        pair_scope = str(row.get("pair_scope") or "")
        source_a = str(row.get("source_a") or "")
        source_b = str(row.get("source_b") or "")
        if not window or not pair_scope or not source_a or not source_b:
            continue
        for key in _pair_keys(window, pair_scope, source_a, source_b):
            if cluster_key not in out[key]:
                out[key].append(cluster_key)
    return out


def _ledger_paths(runs2_dir: Path) -> List[Path]:
    return sorted(runs2_dir.glob("WINDOW_*/*STAGE2B_SIGNAL_PAIRING_LEDGER.csv"))


def _new_agg() -> Dict[str, Any]:
    return {
        "ledger_rows": 0,
        "clusters": set(),
        "windows": set(),
        "states": set(),
        "state_days": set(),
        "total_overlap_values": 0,
        "overlap_sample_values": 0,
        "matched_value_count": 0,
        "false_positive_proxy_value_count": 0,
        "matched_event_count": 0,
        "positive_conversion_event_count": 0,
        "gap_teacher_event_count": 0,
        "wrong_lane_event_count": 0,
        "sample_status": Counter(),
        "deduped_value_keys": set(),
        "deduped_matched_value_keys": set(),
    }


def _add_to_agg(agg: MutableMapping[str, Any], row: Dict[str, Any]) -> None:
    agg["ledger_rows"] += 1
    cluster_key = str(row.get("cluster_key") or "")
    if cluster_key:
        agg["clusters"].add(cluster_key)
    window = str(row.get("window") or "")
    state = str(row.get("state_key") or "")
    state_day = str(row.get("state_day_key") or "")
    if window:
        agg["windows"].add(window)
    if state:
        agg["states"].add(state)
    if state_day:
        agg["state_days"].add(f"{window}|{state_day}")
    agg["total_overlap_values"] += _safe_int(row.get("overlap_value_count"))
    agg["overlap_sample_values"] += _safe_int(row.get("overlap_sample_value_count"))
    agg["matched_value_count"] += _safe_int(row.get("matched_value_count"))
    agg["false_positive_proxy_value_count"] += _safe_int(row.get("false_positive_proxy_value_count"))
    agg["matched_event_count"] += _safe_int(row.get("matched_event_count"))
    agg["positive_conversion_event_count"] += _safe_int(row.get("positive_conversion_event_count"))
    agg["gap_teacher_event_count"] += _safe_int(row.get("gap_teacher_event_count"))
    agg["wrong_lane_event_count"] += _safe_int(row.get("wrong_lane_event_count"))
    agg["sample_status"][str(row.get("sample_status") or "")] += 1
    if str(row.get("sample_status") or "") == "value_level_complete":
        for value in _split_pipe(row.get("overlap_values_sample")):
            agg["deduped_value_keys"].add((window, state_day, value))
        for value in _split_pipe(row.get("matched_values_sample")):
            agg["deduped_matched_value_keys"].add((window, state_day, value))


def _agg_to_row(label_fields: Dict[str, Any], agg: Dict[str, Any]) -> Dict[str, Any]:
    state_days = len(agg["state_days"])
    total = _safe_int(agg["total_overlap_values"])
    matched = _safe_int(agg["matched_value_count"])
    positive = _safe_int(agg["positive_conversion_event_count"])
    wrong = _safe_int(agg["wrong_lane_event_count"])
    deduped_values = len(agg["deduped_value_keys"])
    deduped_matched = len(agg["deduped_matched_value_keys"])
    sample_status = agg["sample_status"]
    complete = sample_status.get("value_level_complete", 0)
    rows = _safe_int(agg["ledger_rows"])
    out = {
        **label_fields,
        "ledger_rows": rows,
        "cluster_count": len(agg["clusters"]),
        "window_count": len(agg["windows"]),
        "state_count": len(agg["states"]),
        "active_state_days": state_days,
        "total_overlap_values": total,
        "avg_pool_or_exposure_per_state_day": _rate(total, state_days),
        "matched_value_count": matched,
        "matched_value_rate": _rate(matched, total),
        "false_positive_proxy_value_count": _safe_int(agg["false_positive_proxy_value_count"]),
        "false_positive_proxy_rate": _rate(_safe_int(agg["false_positive_proxy_value_count"]), total),
        "matched_event_count": _safe_int(agg["matched_event_count"]),
        "positive_conversion_event_count": positive,
        "gap_teacher_event_count": _safe_int(agg["gap_teacher_event_count"]),
        "wrong_lane_event_count": wrong,
        "positive_conversions_per_100_state_days": 100.0 * _rate(positive, state_days),
        "wrong_lane_events_per_100_state_days": 100.0 * _rate(wrong, state_days),
        "wrong_lane_free_conversions_per_100_state_days": 100.0 * _rate(max(0, positive - wrong), state_days),
        "pool_normalized_positive_yield": 100.0 * _rate(positive, total),
        "sample_completeness_rate": _rate(complete, rows),
        "sample_status_mix": _counter_text(sample_status),
        "deduped_complete_value_count": deduped_values,
        "deduped_complete_matched_value_count": deduped_matched,
        "deduped_complete_value_match_rate": _rate(deduped_matched, deduped_values),
    }
    return out


def _mode_list(row: Dict[str, Any]) -> List[str]:
    lane = str(row.get("prototype_lane") or "")
    support = str(row.get("support_context_present") or "") == "true"
    pressure = str(row.get("restraint_pressure") or "")
    modes: List[str] = []
    if lane == "clean_boxed_candidate":
        modes += ["clean_boxed_only", "clean_plus_lineage_deduped"]
    elif lane == "lineage_guarded_boxed_candidate":
        modes.append("clean_plus_lineage_deduped")
    elif lane == "support_gate_only":
        modes.append("support_gate_context")
    elif lane == "decay_watch_only":
        modes.append("decay_watch_companion")
    elif lane == "concentration_retest_or_restraint":
        modes.append("restraint_retest")
    elif lane == "low_denominator_watchlist":
        modes.append("low_denominator_watchlist")
    if lane in CANDIDATE_LANES and support:
        modes.append("clean_with_support_context")
    if lane in CANDIDATE_LANES and pressure != "high":
        modes.append("clean_with_restraint_filter")
    if lane in CANDIDATE_LANES and support and pressure != "high":
        modes.append("clean_lineage_supported_restrained")
    return modes


def _build_value_rows(
    *,
    runs2_dir: Path,
    pair_map: Dict[Tuple[str, str, str, str], List[str]],
    rules_by_cluster: Dict[str, Dict[str, str]],
    max_rows: int,
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]], Dict[str, Counter[str]]]:
    raw_rows: List[Dict[str, Any]] = []
    completeness_by_window: Dict[str, Counter[str]] = defaultdict(Counter)
    scan_counts: Dict[str, Counter[str]] = defaultdict(Counter)

    for path in _ledger_paths(runs2_dir):
        window = _window_name_from_pairing_path(path)
        for row in _read_csv_rows(path):
            scan_counts[window]["pairing_rows_scanned"] += 1
            status, expected, sample_count = _sample_status(row)
            scan_counts[window][status] += 1
            key = (
                window,
                str(row.get("pair_scope") or ""),
                str(row.get("source_a") or ""),
                str(row.get("source_b") or ""),
            )
            cluster_keys = pair_map.get(key, [])
            if not cluster_keys:
                continue
            for cluster_key in cluster_keys:
                rule = rules_by_cluster.get(cluster_key)
                if not rule:
                    continue
                out = {
                    "window": window,
                    "date": row.get("date"),
                    "state_key": row.get("state_key"),
                    "state_day_key": row.get("state_day_key"),
                    "pair_scope": row.get("pair_scope"),
                    "source_a": row.get("source_a"),
                    "source_b": row.get("source_b"),
                    "cluster_key": cluster_key,
                    "mechanism_family": rule.get("mechanism_family"),
                    "future_primitive": rule.get("future_primitive"),
                    "prototype_lane": rule.get("prototype_lane"),
                    "confidence_tier": rule.get("confidence_tier"),
                    "restraint_pressure": rule.get("restraint_pressure"),
                    "shared_lineage_risk_mix": rule.get("shared_lineage_risk_mix"),
                    "sample_status": status,
                    "overlap_value_count": expected,
                    "overlap_sample_value_count": sample_count,
                    "matched_value_count": row.get("matched_value_count"),
                    "false_positive_proxy_value_count": row.get("false_positive_proxy_value_count"),
                    "matched_event_count": row.get("matched_event_count"),
                    "matched_event_ids": row.get("matched_event_ids"),
                    "matched_values_sample": row.get("matched_values_sample"),
                    "overlap_values_sample": row.get("overlap_values_sample"),
                    "gap_teacher_event_count": row.get("gap_teacher_event_count"),
                    "positive_conversion_event_count": row.get("positive_conversion_event_count"),
                    "wrong_lane_event_count": row.get("wrong_lane_event_count"),
                    "outcome_mix": row.get("outcome_mix"),
                    "status_mix": row.get("status_mix"),
                    "live_scoring_permission": "none",
                    "candidate_generation_permission": "none",
                }
                raw_rows.append(out)
                completeness_by_window[window]["matched_stage5_rows"] += 1
                completeness_by_window[window][status] += 1
                completeness_by_window["ALL_WINDOWS"]["matched_stage5_rows"] += 1
                completeness_by_window["ALL_WINDOWS"][status] += 1
                if max_rows > 0 and len(raw_rows) >= max_rows:
                    return raw_rows, _completion_rows(scan_counts, completeness_by_window), scan_counts
    return raw_rows, _completion_rows(scan_counts, completeness_by_window), scan_counts


def _completion_rows(scan_counts: Dict[str, Counter[str]], matched_counts: Dict[str, Counter[str]]) -> List[Dict[str, Any]]:
    windows = sorted(set(scan_counts) | set(matched_counts))
    rows: List[Dict[str, Any]] = []
    total_scan = Counter()
    for counter in scan_counts.values():
        total_scan.update(counter)
    if total_scan:
        scan_counts["ALL_WINDOWS"] = total_scan
    for window in windows:
        scan = scan_counts.get(window, Counter())
        matched = matched_counts.get(window, Counter())
        matched_total = matched.get("matched_stage5_rows", 0)
        complete = matched.get("value_level_complete", 0)
        rows.append(
            {
                "window": window,
                "pairing_rows_scanned": scan.get("pairing_rows_scanned", 0),
                "pairing_value_level_complete": scan.get("value_level_complete", 0),
                "pairing_sample_truncated": scan.get("sample_truncated", 0),
                "pairing_aggregate_only_missing_sample": scan.get("aggregate_only_missing_sample", 0),
                "matched_stage5_rows": matched_total,
                "matched_value_level_complete": complete,
                "matched_sample_truncated": matched.get("sample_truncated", 0),
                "matched_aggregate_only_missing_sample": matched.get("aggregate_only_missing_sample", 0),
                "matched_sample_completeness_rate": _rate(complete, matched_total),
                "interpretation": "value-level replay is exact only for matched rows with value_level_complete status",
            }
        )
    if "ALL_WINDOWS" not in {row["window"] for row in rows}:
        scan = scan_counts.get("ALL_WINDOWS", Counter())
        matched = matched_counts.get("ALL_WINDOWS", Counter())
        matched_total = matched.get("matched_stage5_rows", 0)
        complete = matched.get("value_level_complete", 0)
        rows.append(
            {
                "window": "ALL_WINDOWS",
                "pairing_rows_scanned": scan.get("pairing_rows_scanned", 0),
                "pairing_value_level_complete": scan.get("value_level_complete", 0),
                "pairing_sample_truncated": scan.get("sample_truncated", 0),
                "pairing_aggregate_only_missing_sample": scan.get("aggregate_only_missing_sample", 0),
                "matched_stage5_rows": matched_total,
                "matched_value_level_complete": complete,
                "matched_sample_truncated": matched.get("sample_truncated", 0),
                "matched_aggregate_only_missing_sample": matched.get("aggregate_only_missing_sample", 0),
                "matched_sample_completeness_rate": _rate(complete, matched_total),
                "interpretation": "value-level replay is exact only for matched rows with value_level_complete status",
            }
        )
    return sorted(rows, key=lambda row: (str(row["window"]) != "ALL_WINDOWS", str(row["window"])))


def _annotate_support_context(rows: List[Dict[str, Any]]) -> None:
    support_keys = set()
    for row in rows:
        if str(row.get("prototype_lane") or "") != SUPPORT_LANE:
            continue
        window = str(row.get("window") or "")
        state_day = str(row.get("state_day_key") or "")
        mechanism = str(row.get("mechanism_family") or "")
        primitive = str(row.get("future_primitive") or "")
        support_keys.add((window, state_day, mechanism, primitive))
        support_keys.add((window, state_day, mechanism, "*"))

    for row in rows:
        window = str(row.get("window") or "")
        state_day = str(row.get("state_day_key") or "")
        mechanism = str(row.get("mechanism_family") or "")
        primitive = str(row.get("future_primitive") or "")
        present = (window, state_day, mechanism, primitive) in support_keys or (window, state_day, mechanism, "*") in support_keys
        row["support_context_present"] = "true" if present else "false"
        row["included_in_modes"] = "|".join(_mode_list(row))


def _aggregate_modes(rows: Sequence[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]], List[Dict[str, Any]]]:
    by_mode: Dict[str, Dict[str, Any]] = defaultdict(_new_agg)
    by_mode_window: Dict[Tuple[str, str], Dict[str, Any]] = defaultdict(_new_agg)
    by_mode_state: Dict[Tuple[str, str], Dict[str, Any]] = defaultdict(_new_agg)
    for row in rows:
        for mode in _mode_list(row):
            _add_to_agg(by_mode[mode], row)
            _add_to_agg(by_mode_window[(mode, str(row.get("window") or ""))], row)
            _add_to_agg(by_mode_state[(mode, str(row.get("state_key") or ""))], row)

    mode_rows = [
        _agg_to_row({"prototype_mode": mode}, agg)
        for mode, agg in sorted(by_mode.items())
    ]
    window_rows = [
        _agg_to_row({"prototype_mode": mode, "window": window}, agg)
        for (mode, window), agg in sorted(by_mode_window.items())
    ]
    state_rows = [
        _agg_to_row({"prototype_mode": mode, "state_key": state}, agg)
        for (mode, state), agg in sorted(by_mode_state.items())
    ]
    return mode_rows, window_rows, state_rows


def _build_ablation_rows(
    stage4_ablation_rows: Sequence[Dict[str, str]],
    rules_by_cluster: Dict[str, Dict[str, str]],
) -> List[Dict[str, Any]]:
    grouped: Dict[Tuple[str, str, str], List[Dict[str, Any]]] = defaultdict(list)
    for row in stage4_ablation_rows:
        cluster_key = _cluster_key(row)
        rule = rules_by_cluster.get(cluster_key)
        if not rule:
            continue
        lane = str(rule.get("prototype_lane") or "")
        modes = []
        if lane == "clean_boxed_candidate":
            modes = ["clean_boxed_only", "clean_plus_lineage_deduped"]
        elif lane == "lineage_guarded_boxed_candidate":
            modes = ["clean_plus_lineage_deduped"]
        elif lane == "support_gate_only":
            modes = ["support_gate_context"]
        elif lane == "decay_watch_only":
            modes = ["decay_watch_companion"]
        elif lane == "concentration_retest_or_restraint":
            modes = ["restraint_retest"]
        elif lane == "low_denominator_watchlist":
            modes = ["low_denominator_watchlist"]
        for mode in modes:
            grouped[(mode, lane, str(row.get("mechanism_family") or ""))].append(row)

    out: List[Dict[str, Any]] = []
    for (mode, lane, mechanism), rows in sorted(grouped.items()):
        source_a = sum(_safe_float(row.get("source_a_supported_per_100_state_days")) for row in rows) / len(rows)
        source_b = sum(_safe_float(row.get("source_b_supported_per_100_state_days")) for row in rows) / len(rows)
        overlap = sum(_safe_float(row.get("overlap_supported_per_100_state_days")) for row in rows) / len(rows)
        lift = sum(_safe_float(row.get("overlap_support_per100_vs_best_source")) for row in rows) / len(rows)
        lane_lift = sum(_safe_float(row.get("overlap_lane_rate_vs_best_source")) for row in rows) / len(rows)
        pool_reduction = sum(_safe_float(row.get("overlap_pool_reduction_vs_smaller_source")) for row in rows) / len(rows)
        out.append(
            {
                "prototype_mode": mode,
                "prototype_lane": lane,
                "mechanism_family": mechanism,
                "ablation_rows": len(rows),
                "avg_source_a_supported_per_100_state_days": source_a,
                "avg_source_b_supported_per_100_state_days": source_b,
                "avg_overlap_supported_per_100_state_days": overlap,
                "avg_overlap_support_per100_vs_best_source": lift,
                "avg_overlap_lane_rate_vs_best_source": lane_lift,
                "avg_overlap_pool_reduction_vs_smaller_source": pool_reduction,
                "interpretation": _ablation_interpretation(lift, pool_reduction),
            }
        )
    return out


def _ablation_interpretation(lift: float, pool_reduction: float) -> str:
    if lift > 0 and pool_reduction > 0:
        return "overlap_adds_support_and_reduces_pool"
    if lift <= 0 and pool_reduction > 0:
        return "overlap_reduces_pool_but_does_not_beat_best_source"
    if lift > 0:
        return "overlap_adds_support_without_pool_reduction"
    return "overlap_does_not_beat_best_source"


def _build_support_ablation(rows: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    grouped: Dict[Tuple[str, str, str], Dict[str, Any]] = defaultdict(_new_agg)
    for row in rows:
        if str(row.get("prototype_lane") or "") not in CANDIDATE_LANES:
            continue
        label = "candidate_rows_with_support_context" if row.get("support_context_present") == "true" else "candidate_rows_without_support_context"
        key = (label, str(row.get("prototype_lane") or ""), str(row.get("mechanism_family") or ""))
        _add_to_agg(grouped[key], row)
    return [
        _agg_to_row({"support_ablation_bucket": bucket, "prototype_lane": lane, "mechanism_family": mechanism}, agg)
        for (bucket, lane, mechanism), agg in sorted(grouped.items())
    ]


def _build_restraint_audit(rows: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    grouped: Dict[Tuple[str, str, str], Dict[str, Any]] = defaultdict(_new_agg)
    for row in rows:
        if str(row.get("prototype_lane") or "") not in CANDIDATE_LANES:
            continue
        pressure = str(row.get("restraint_pressure") or "")
        bucket = "kept_by_restraint_filter" if pressure != "high" else "removed_by_high_restraint_pressure"
        key = (bucket, pressure, str(row.get("mechanism_family") or ""))
        _add_to_agg(grouped[key], row)
    return [
        _agg_to_row({"restraint_bucket": bucket, "restraint_pressure": pressure, "mechanism_family": mechanism}, agg)
        for (bucket, pressure, mechanism), agg in sorted(grouped.items())
    ]


def _build_casebook(rows: Sequence[Dict[str, Any]], *, limit: int) -> List[Dict[str, Any]]:
    candidates = [
        row for row in rows
        if str(row.get("prototype_lane") or "") in CANDIDATE_LANES
        and (_safe_int(row.get("positive_conversion_event_count")) > 0 or _safe_int(row.get("matched_event_count")) > 0)
    ]
    ranked = sorted(
        candidates,
        key=lambda row: (
            -_safe_int(row.get("positive_conversion_event_count")),
            -_safe_int(row.get("matched_event_count")),
            -_safe_int(row.get("matched_value_count")),
            str(row.get("sample_status") or ""),
            str(row.get("cluster_key") or ""),
        ),
    )
    out: List[Dict[str, Any]] = []
    for row in ranked[: max(int(limit), 0)]:
        out.append(
            {
                "window": row.get("window"),
                "date": row.get("date"),
                "state_key": row.get("state_key"),
                "cluster_key": row.get("cluster_key"),
                "prototype_lane": row.get("prototype_lane"),
                "mechanism_family": row.get("mechanism_family"),
                "future_primitive": row.get("future_primitive"),
                "support_context_present": row.get("support_context_present"),
                "restraint_pressure": row.get("restraint_pressure"),
                "sample_status": row.get("sample_status"),
                "overlap_value_count": row.get("overlap_value_count"),
                "matched_value_count": row.get("matched_value_count"),
                "matched_event_count": row.get("matched_event_count"),
                "positive_conversion_event_count": row.get("positive_conversion_event_count"),
                "wrong_lane_event_count": row.get("wrong_lane_event_count"),
                "matched_event_ids": row.get("matched_event_ids"),
                "overlap_values_sample": row.get("overlap_values_sample"),
                "matched_values_sample": row.get("matched_values_sample"),
                "included_in_modes": row.get("included_in_modes"),
                "casebook_note": _casebook_note(row),
            }
        )
    return out


def _casebook_note(row: Dict[str, Any]) -> str:
    support = row.get("support_context_present") == "true"
    pressure = str(row.get("restraint_pressure") or "")
    if support and pressure != "high":
        return "candidate row has same-day support context and passes high-pressure restraint filter"
    if support:
        return "candidate row has same-day support context but high restraint pressure remains"
    if pressure == "high":
        return "candidate row converted but would be removed by strict high-pressure restraint filter"
    return "candidate row converted without same-day support context"


def _write_casebook_md(path: Path, rows: Sequence[Dict[str, Any]], *, force: bool) -> None:
    lines = [
        "# Stage 5 Value-Level Casebook",
        "",
        "Purpose: concrete state-day examples from the Stage 5 read-only shadow translator fixture evaluator.",
        "",
        "| window | date | state | lane | support | pressure | positive | matched events | sample | note |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{row.get('window')}`",
                    str(row.get("date")),
                    str(row.get("state_key")),
                    f"`{row.get('prototype_lane')}`",
                    str(row.get("support_context_present")),
                    str(row.get("restraint_pressure")),
                    str(row.get("positive_conversion_event_count")),
                    str(row.get("matched_event_count")),
                    str(row.get("sample_status")),
                    str(row.get("casebook_note")),
                ]
            )
            + " |"
        )
    lines.append("")
    _write_text(path, "\n".join(lines), force=force)


def _build_pro44_rows() -> List[Dict[str, Any]]:
    return [
        {
            "criterion": "split_replay_by_mechanism_family",
            "stage5_status": "covered",
            "evidence": "mode/window/state/ablation rows carry mechanism_family; Stage 4 mechanism scorecard remains upstream baseline",
            "guardrail": "do_not_blend_all_candidates_into_one_pool",
        },
        {
            "criterion": "legacy_names_are_locators_not_rule_names",
            "stage5_status": "covered",
            "evidence": "Stage 5 reads Stage 4C future_primitive and preserves old source names only as source_a/source_b locators",
            "guardrail": "future architecture references mechanism_family and future_primitive",
        },
        {
            "criterion": "shared_lineage_deduplication",
            "stage5_status": "covered_for_replay_modes",
            "evidence": "lineage_guarded rows stay separate from clean rows and clean_plus_lineage_deduped is reported as a distinct prototype mode",
            "guardrail": "lineage rows do not become independent confirmation credit",
        },
        {
            "criterion": "source_a_source_b_overlap_ablation",
            "stage5_status": "covered_aggregate_stage4_backed",
            "evidence": "STAGE5_ABLATION_MATRIX summarizes Stage 4 source A / source B / overlap comparisons by mode/lane/mechanism",
            "guardrail": "overlap cannot be claimed useful without source-side baseline",
        },
        {
            "criterion": "yield_denominator_metrics",
            "stage5_status": "covered",
            "evidence": "mode/window/state/support/restraint outputs include positive/100 ASD, wrong-lane-free/100 ASD, false-positive proxy rate, and pool-normalized yield",
            "guardrail": "do_not_rank_by_raw_hit_counts",
        },
        {
            "criterion": "state_concentration_read",
            "stage5_status": "covered",
            "evidence": "STAGE5_STATE_STRATIFICATION plus Stage 4 concentration upstream checks expose state dependence",
            "guardrail": "do_not_promote_one_state_fragility",
        },
        {
            "criterion": "negative_controls_as_restraint_assets",
            "stage5_status": "covered",
            "evidence": "STAGE5_RESTRAINT_EFFECT_AUDIT measures kept vs removed candidate rows under high-pressure restraint",
            "guardrail": "negative controls are penalty/veto surfaces, not promotion surfaces",
        },
        {
            "criterion": "vtrac_decay_not_boxed_permission",
            "stage5_status": "covered",
            "evidence": "decay_watch_companion is reported as a separate prototype mode and never mixed into boxed candidate-expression modes",
            "guardrail": "territory persistence cannot become boxed spend permission",
        },
        {
            "criterion": "sample_completeness_before_value_level_claims",
            "stage5_status": "new_stage5_control",
            "evidence": "STAGE5_VALUE_COMPLETENESS_AUDIT marks value_level_complete, sample_truncated, and aggregate-only rows before interpreting value-level replay",
            "guardrail": "do_not_overclaim_truncated_samples",
        },
    ]


def _build_markdown(
    *,
    runs2_dir: Path,
    paths: Dict[str, Path],
    value_rows: Sequence[Dict[str, Any]],
    completeness_rows: Sequence[Dict[str, Any]],
    mode_rows: Sequence[Dict[str, Any]],
    ablation_rows: Sequence[Dict[str, Any]],
    support_rows: Sequence[Dict[str, Any]],
    restraint_rows: Sequence[Dict[str, Any]],
    pro44_rows: Sequence[Dict[str, Any]],
    casebook_rows: Sequence[Dict[str, Any]],
) -> str:
    lanes = Counter(str(row.get("prototype_lane") or "") for row in value_rows)
    modes = {str(row.get("prototype_mode") or ""): row for row in mode_rows}
    all_complete = next((row for row in completeness_rows if row.get("window") == "ALL_WINDOWS"), {})
    lines = [
        "# Analysis Arena Stage 5 Shadow Translator Fixture Evaluator",
        "",
        "Purpose: replay Stage 4C shadow translator lanes against completed Stage 2B state-day fixtures without changing live scoring or candidate generation.",
        "",
        "## Metadata",
        f"- runs2_dir: `{safe_rel(runs2_dir)}`",
        f"- value_level_replay_rows: `{len(value_rows)}`",
        f"- prototype_modes: `{len(mode_rows)}`",
        f"- ablation_rows: `{len(ablation_rows)}`",
        f"- support_ablation_rows: `{len(support_rows)}`",
        f"- restraint_audit_rows: `{len(restraint_rows)}`",
        f"- casebook_rows: `{len(casebook_rows)}`",
        "",
        "## Guardrails",
        "- Stage 5 is read-only and cannot change live scoring, candidate generation, translator logic, budget logic, or legacy infrastructure.",
        "- Stage 5 evaluates fixture behavior; it does not create deployable candidate lists.",
        "- VTRAC/decay remains a companion mode and cannot become boxed spend permission.",
        "- Support gates are context filters/modifiers, not standalone candidates.",
        "- Negative-control and concentration pressure are tested as restraint surfaces.",
        "- Value-level claims are valid only for rows marked `value_level_complete`; truncated samples remain aggregate-only evidence.",
        "",
        "## Value Completeness",
        f"- matched_stage5_rows: `{all_complete.get('matched_stage5_rows', 0)}`",
        f"- matched_value_level_complete: `{all_complete.get('matched_value_level_complete', 0)}`",
        f"- matched_sample_truncated: `{all_complete.get('matched_sample_truncated', 0)}`",
        f"- matched_sample_completeness_rate: `{_pct(all_complete.get('matched_sample_completeness_rate', 0))}`",
        "",
        "## Prototype Lane Rows",
        "",
    ]
    for lane, count in lanes.most_common():
        lines.append(f"- `{lane}`: `{count}`")

    lines += [
        "",
        "## Prototype Mode Scorecard",
        "",
        "| mode | rows | ASD | avg pool | pos/100 ASD | wrong-free/100 ASD | FP proxy | complete |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for mode in sorted(modes):
        row = modes[mode]
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{mode}`",
                    str(row.get("ledger_rows")),
                    str(row.get("active_state_days")),
                    _fmt(row.get("avg_pool_or_exposure_per_state_day")),
                    _fmt(row.get("positive_conversions_per_100_state_days")),
                    _fmt(row.get("wrong_lane_free_conversions_per_100_state_days")),
                    _pct(row.get("false_positive_proxy_rate")),
                    _pct(row.get("sample_completeness_rate")),
                ]
            )
            + " |"
        )

    lines += [
        "",
        "## PRO_44 Compliance",
        "",
    ]
    for row in pro44_rows:
        lines.append(f"- `{row.get('criterion')}`: `{row.get('stage5_status')}` - {row.get('guardrail')}")

    top_ablation = sorted(
        ablation_rows,
        key=lambda row: -_safe_float(row.get("avg_overlap_support_per100_vs_best_source")),
    )[:10]
    lines += [
        "",
        "## Top Source A / Source B / Overlap Ablations",
        "",
        "| mode | lane | mechanism | overlap lift | pool reduction | interpretation |",
        "|---|---:|---:|---:|---:|---|",
    ]
    for row in top_ablation:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{row.get('prototype_mode')}`",
                    f"`{row.get('prototype_lane')}`",
                    f"`{row.get('mechanism_family')}`",
                    _fmt(row.get("avg_overlap_support_per100_vs_best_source")),
                    _fmt(row.get("avg_overlap_pool_reduction_vs_smaller_source")),
                    str(row.get("interpretation")),
                ]
            )
            + " |"
        )

    lines += [
        "",
        "## Interpretation",
        "- Stage 5 moves the work from cluster-level governance into fixture-backed shadow expression evaluation.",
        "- The key read is not whether every mode has high raw support; it is which modes preserve positive conversion while controlling pool size, duplicate lineage, support-only evidence, and restraint pressure.",
        "- This is still a pre-rewrite evidence layer. Any actual translator/scoring rewrite should be specified only after Stage 5 results are reviewed.",
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
    stage = _stage_paths(runs2_dir)
    paths = _cycle_paths(output_dir)

    rule_rows = _read_csv_rows(stage["stage4c_rules"])
    fixture_rows = _read_csv_rows(stage["stage4_fixture"])
    ablation_source_rows = _read_csv_rows(stage["stage4_ablation"])
    if not rule_rows or not fixture_rows:
        raise SystemExit("Stage 4C rule registry or Stage 4 fixture ledger is missing. Run Stage 4C first.")

    rules_by_cluster = {str(row.get("cluster_key") or ""): row for row in rule_rows}
    pair_map = _fixture_pair_map(fixture_rows, rules_by_cluster)
    value_rows, completeness_rows, _scan_counts = _build_value_rows(
        runs2_dir=runs2_dir,
        pair_map=pair_map,
        rules_by_cluster=rules_by_cluster,
        max_rows=int(args.max_value_rows or 0),
    )
    _annotate_support_context(value_rows)

    mode_rows, window_rows, state_rows = _aggregate_modes(value_rows)
    ablation_rows = _build_ablation_rows(ablation_source_rows, rules_by_cluster)
    support_rows = _build_support_ablation(value_rows)
    restraint_rows = _build_restraint_audit(value_rows)
    casebook_rows = _build_casebook(value_rows, limit=int(args.casebook_limit))
    pro44_rows = _build_pro44_rows()

    _write_csv(paths["value_completeness_csv"], completeness_rows, force=bool(args.force))
    _write_csv(paths["value_ledger_csv"], value_rows, force=bool(args.force))
    _write_csv(paths["mode_scorecard_csv"], mode_rows, force=bool(args.force))
    _write_csv(paths["ablation_csv"], ablation_rows, force=bool(args.force))
    _write_csv(paths["window_csv"], window_rows, force=bool(args.force))
    _write_csv(paths["state_csv"], state_rows, force=bool(args.force))
    _write_csv(paths["support_csv"], support_rows, force=bool(args.force))
    _write_csv(paths["restraint_csv"], restraint_rows, force=bool(args.force))
    _write_csv(paths["pro44_csv"], pro44_rows, force=bool(args.force))
    _write_csv(paths["casebook_csv"], casebook_rows, force=bool(args.force))
    _write_casebook_md(paths["casebook_md"], casebook_rows, force=bool(args.force))

    payload = {
        "metadata": {
            "runs2_dir": safe_rel(runs2_dir),
            "value_level_replay_rows": len(value_rows),
            "prototype_modes": len(mode_rows),
            "ablation_rows": len(ablation_rows),
            "support_ablation_rows": len(support_rows),
            "restraint_audit_rows": len(restraint_rows),
            "casebook_rows": len(casebook_rows),
            "guardrail": "read_only_stage5_fixture_evaluator_no_live_scoring_or_candidate_generation_changes",
        },
        "lane_counts": dict(Counter(str(row.get("prototype_lane") or "") for row in value_rows)),
        "mode_scorecard": mode_rows,
        "value_completeness": completeness_rows,
        "pro44_compliance": pro44_rows,
        "outputs": {label: safe_rel(path) for label, path in paths.items()},
    }
    _write_json(paths["json"], payload, force=bool(args.force))
    _write_text(
        paths["md"],
        _build_markdown(
            runs2_dir=runs2_dir,
            paths=paths,
            value_rows=value_rows,
            completeness_rows=completeness_rows,
            mode_rows=mode_rows,
            ablation_rows=ablation_rows,
            support_rows=support_rows,
            restraint_rows=restraint_rows,
            pro44_rows=pro44_rows,
            casebook_rows=casebook_rows,
        ),
        force=bool(args.force),
    )

    print(f"[OK] Wrote Stage-5 fixture evaluator: {safe_rel(paths['md'])}")
    print(f"[OK] Wrote value replay rows: {len(value_rows)}")
    print(f"[OK] Wrote prototype mode rows: {len(mode_rows)}")
    print(f"[OK] Wrote casebook rows: {len(casebook_rows)}")


if __name__ == "__main__":
    main()
