#!/usr/bin/env python3
"""Create the Stage-4B Analysis Arena replay readback package.

Stage 4B is a read-only interpretation layer on top of the Stage-4 fixture
replay outputs. It does not change scoring, translator logic, candidate
generation, budgeting, or legacy infrastructure. Its job is to turn the Stage-4
fixture tables into durable decision intelligence:

- primitive cluster registry
- survivor/support/restraint readback
- exemplar casebook rows
- leave-one-window-out holdout matrix
- future translator design queue
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, List, Sequence, Tuple


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


STAGE4B_PREFIX = "ANALYSIS_ARENA__CYCLE__STAGE4B"


def _parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--runs2-dir", default=str(RUNS_2_DIR), help="RUNS_2 root containing Stage-4 outputs.")
    ap.add_argument("--output-dir", default=str(RUNS_2_DIR), help="Cycle-level output directory.")
    ap.add_argument("--casebook-limit", type=int, default=96, help="Maximum casebook rows to emit.")
    ap.add_argument("--force", action="store_true", help="Overwrite existing Stage-4B outputs.")
    return ap.parse_args()


def _stage4_paths(runs2_dir: Path) -> Dict[str, Path]:
    prefix = "ANALYSIS_ARENA__CYCLE__STAGE4"
    return {
        "scorecard_md": runs2_dir / f"{prefix}_FIXTURE_REPLAY_SCORECARD.md",
        "decision_csv": runs2_dir / f"{prefix}_REPLAY_DECISION_REGISTRY.csv",
        "ledger_csv": runs2_dir / f"{prefix}_FIXTURE_REPLAY_LEDGER.csv",
        "mechanism_csv": runs2_dir / f"{prefix}_MECHANISM_FAMILY_SCORECARD.csv",
        "ab_csv": runs2_dir / f"{prefix}_SOURCE_A_B_OVERLAP_COMPARISON.csv",
        "lineage_csv": runs2_dir / f"{prefix}_SHARED_LINEAGE_AUDIT.csv",
        "negative_csv": runs2_dir / f"{prefix}_NEGATIVE_CONTROL_REPLAY_SUMMARY.csv",
    }


def _cycle_paths(output_dir: Path) -> Dict[str, Path]:
    return {
        "md": output_dir / f"{STAGE4B_PREFIX}_REPLAY_READBACK.md",
        "json": output_dir / f"{STAGE4B_PREFIX}_REPLAY_READBACK.json",
        "cluster_csv": output_dir / f"{STAGE4B_PREFIX}_PRIMITIVE_CLUSTER_REGISTRY.csv",
        "casebook_csv": output_dir / f"{STAGE4B_PREFIX}_SURVIVOR_SUPPORT_RESTRAINT_CASEBOOK.csv",
        "casebook_md": output_dir / f"{STAGE4B_PREFIX}_SURVIVOR_SUPPORT_RESTRAINT_CASEBOOK.md",
        "holdout_csv": output_dir / f"{STAGE4B_PREFIX}_LEAVE_ONE_WINDOW_OUT_MATRIX.csv",
        "translator_queue_csv": output_dir / f"{STAGE4B_PREFIX}_TRANSLATOR_DESIGN_QUEUE.csv",
    }


def _source_signature(source: str) -> str:
    text = str(source or "").strip().lower()
    if not text:
        return "none"
    family = text.split(":", 1)[0]
    token_checks = [
        ("mirror_pair_closure", "mirror_pair_closure"),
        ("aux_vtrac_index_overdue", "aux_vtrac_index_overdue"),
        ("aux_positional", "aux_positional"),
        ("vtrac_enhanced_top", "vtrac_enhanced_top"),
        ("secondary_canonicals", "secondary_canonicals"),
        ("secondary_canonical", "secondary_canonicals"),
        ("context_reinforced_canonicals", "context_reinforced_canonicals"),
        ("dominant_canonicals", "dominant_canonicals"),
        ("top_vtrac_indices", "top_vtrac_indices"),
        ("top_canonicals", "top_canonicals"),
        ("budgeted_canonicals_top", "budgeted_canonicals_top"),
        ("ranked_candidate_canonical", "ranked_candidate_canonical"),
        ("ranked_candidate_combo", "ranked_candidate_combo"),
        ("diagnostic_straight_seed", "diagnostic_straight_seed"),
        ("diagnostic_boxed_seed", "diagnostic_boxed_seed"),
        ("diagnostic_vt_box_seed", "diagnostic_vt_box_seed"),
        ("recommended_canonicals", "recommended_canonicals"),
        ("implied_canonicals", "implied_canonicals"),
        ("positional_combo", "positional_combo"),
        ("positional_canonical", "positional_canonical"),
        ("hot_zones_top", "hot_zones_top"),
        ("packb_mirror3rd", "packb_mirror3rd"),
        ("due_doubles_mirror_double", "due_doubles_mirror_double"),
        ("consensus_double", "consensus_double"),
        ("r-perm", "r_perm"),
        ("r_perm", "r_perm"),
    ]
    for needle, label in token_checks:
        if needle in text:
            return f"{family}:{label}"
    if "analysis_prefix:b12" in text or ":b12" in text:
        return f"{family}:b12_budget_surface"
    if "analysis_prefix:b24" in text or ":b24" in text:
        return f"{family}:b24_budget_surface"
    if "analysis_prefix:b36" in text or ":b36" in text:
        return f"{family}:b36_budget_surface"
    normalized = re.sub(r":canonical\b", "", text)
    normalized = normalized.replace("pack_method:", "").replace("pack:", "")
    parts = normalized.split(":")
    return ":".join(parts[:3])


def _cluster_key(row: Dict[str, Any]) -> str:
    primitive = str(row.get("future_primitive") or "unknown_primitive")
    mechanism = str(row.get("mechanism_family") or "unknown_mechanism")
    source_a = _source_signature(str(row.get("source_a") or ""))
    source_b = _source_signature(str(row.get("source_b") or ""))
    if source_a == "none" and source_b == "none":
        source_a = _source_signature(str(row.get("entity_key") or ""))
    pair_sig = "+".join(sorted(sig for sig in [source_a, source_b] if sig != "none")) or "source_only"
    return f"{mechanism}::{primitive}::{pair_sig}"


def _recommended_cluster_use(decisions: Counter[str], lineage: Counter[str], queue: Counter[str]) -> str:
    if decisions.get("survived_as_boxed_translator_candidate"):
        return "translator_candidate_cluster"
    if decisions.get("survived_with_lineage_guardrail"):
        return "translator_candidate_with_duplicate_credit_guardrail"
    if decisions.get("survived_as_support_gate"):
        return "support_gate_cluster"
    if decisions.get("watch_decay_only"):
        return "decay_or_vtrac_watch_cluster"
    if decisions.get("blocked_by_state_concentration"):
        return "state_concentration_retest_or_restraint"
    if decisions.get("low_denominator_watchlist") or decisions.get("fixture_only_low_denominator"):
        return "low_denominator_watchlist"
    if any(key.startswith("demote") for key in decisions):
        return "restraint_or_penalty_cluster"
    if queue.get("P4_diagnostic_replay"):
        return "diagnostic_fixture_cluster"
    if lineage.get("high"):
        return "duplicate_lineage_review"
    return "fixture_only_cluster"


def _build_cluster_registry(decision_rows: Sequence[Dict[str, str]]) -> List[Dict[str, Any]]:
    grouped: Dict[str, List[Dict[str, str]]] = defaultdict(list)
    for row in decision_rows:
        grouped[_cluster_key(row)].append(row)

    out: List[Dict[str, Any]] = []
    for key, rows in grouped.items():
        first = rows[0]
        decisions = Counter(str(row.get("stage4_replay_decision") or "") for row in rows)
        queue = Counter(str(row.get("queue") or "") for row in rows)
        lineage = Counter(str(row.get("shared_lineage_risk") or "") for row in rows)
        entities = [str(row.get("entity_key") or "") for row in rows]
        active = sum(_safe_int(row.get("active_state_days")) for row in rows)
        total = sum(_safe_int(row.get("total_overlap_values")) for row in rows)
        supported = sum(_safe_int(row.get("supported_event_count")) for row in rows)
        positive = sum(_safe_int(row.get("positive_conversion_event_count")) for row in rows)
        gap = sum(_safe_int(row.get("gap_teacher_event_count")) for row in rows)
        wrong = sum(_safe_int(row.get("wrong_lane_event_count")) for row in rows)
        cluster = {
            "cluster_key": key,
            "mechanism_family": first.get("mechanism_family"),
            "future_primitive": first.get("future_primitive"),
            "source_signature_a": _source_signature(str(first.get("source_a") or "")),
            "source_signature_b": _source_signature(str(first.get("source_b") or "")),
            "entity_count": len(rows),
            "stage4_decision_mix": _counter_text(decisions),
            "queue_mix": _counter_text(queue),
            "shared_lineage_risk_mix": _counter_text(lineage),
            "windows_confirmed_max": max(_safe_int(row.get("windows_confirmed")) for row in rows),
            "active_state_days": active,
            "total_overlap_values": total,
            "avg_pool_or_exposure_per_state_day": _rate(total, active),
            "supported_event_count": supported,
            "supported_events_per_100_state_days": 100.0 * _rate(supported, active),
            "positive_conversion_event_count": positive,
            "gap_teacher_event_count": gap,
            "wrong_lane_event_count": wrong,
            "positive_conversions_per_100_state_days": 100.0 * _rate(positive, active),
            "pool_normalized_positive_yield": 100.0 * _rate(positive, total),
            "recommended_cluster_use": _recommended_cluster_use(decisions, lineage, queue),
            "representative_entity": entities[0],
            "entity_sample": "|".join(entities[:6]),
        }
        out.append(cluster)
    return sorted(
        out,
        key=lambda row: (
            str(row.get("recommended_cluster_use") or ""),
            -_safe_int(row.get("entity_count")),
            -_safe_float(row.get("positive_conversions_per_100_state_days")),
            str(row.get("cluster_key") or ""),
        ),
    )


def _aggregate_rows(rows: Sequence[Dict[str, str]]) -> Dict[str, Any]:
    active = sum(_safe_int(row.get("active_state_days")) for row in rows)
    total = sum(_safe_int(row.get("total_overlap_values")) for row in rows)
    supported = sum(_safe_int(row.get("supported_event_count")) for row in rows)
    positive = sum(_safe_int(row.get("positive_conversion_event_count")) for row in rows)
    gap = sum(_safe_int(row.get("gap_teacher_event_count")) for row in rows)
    wrong = sum(_safe_int(row.get("wrong_lane_event_count")) for row in rows)
    matched = sum(_safe_int(row.get("matched_value_count")) for row in rows)
    false_positive = sum(_safe_int(row.get("false_positive_proxy_value_count")) for row in rows)
    return {
        "windows": len({str(row.get("window") or "") for row in rows if row.get("window")}),
        "active_state_days": active,
        "total_overlap_values": total,
        "avg_pool_or_exposure_per_state_day": _rate(total, active),
        "matched_value_count": matched,
        "matched_value_rate": _rate(matched, total),
        "supported_event_count": supported,
        "supported_events_per_100_state_days": 100.0 * _rate(supported, active),
        "positive_conversion_event_count": positive,
        "gap_teacher_event_count": gap,
        "wrong_lane_event_count": wrong,
        "false_positive_proxy_value_count": false_positive,
        "false_positive_proxy_rate": _rate(false_positive, total),
        "positive_conversions_per_100_state_days": 100.0 * _rate(positive, active),
    }


def _train_survives(queue: str, decision: str, agg: Dict[str, Any], lineage_risk: str) -> Tuple[bool, str]:
    windows = _safe_int(agg.get("windows"))
    active = _safe_int(agg.get("active_state_days"))
    avg_pool = _safe_float(agg.get("avg_pool_or_exposure_per_state_day"))
    support_per100 = _safe_float(agg.get("supported_events_per_100_state_days"))
    positive = _safe_int(agg.get("positive_conversion_event_count"))
    gap = _safe_int(agg.get("gap_teacher_event_count"))
    wrong = _safe_int(agg.get("wrong_lane_event_count"))
    if active == 0 or windows < 3:
        return False, "train_insufficient_denominator"
    if queue == "P1_boxed_translator_replay":
        if avg_pool <= 3.5 and support_per100 > 0 and wrong == 0:
            if lineage_risk == "high":
                return True, "train_survives_with_lineage_guardrail"
            return True, "train_survives_clean_boxed_candidate"
        return False, "train_fails_p1_boxed_checks"
    if queue == "P2_support_gate_replay":
        if support_per100 > 0 and wrong <= max(positive + gap, 1):
            return True, "train_survives_support_gate"
        return False, "train_fails_support_gate_checks"
    if queue == "P3_vtrac_decay_watch_replay":
        return True, "train_survives_watch_decay_only"
    if queue == "P4_low_denominator_fixture_replay":
        if positive > 0 and avg_pool <= 2.5:
            return True, "train_survives_low_denominator_watchlist"
        return False, "train_fails_low_denominator_checks"
    if queue == "P4_diagnostic_replay":
        return True, "train_diagnostic_fixture_only"
    return decision.startswith("survived"), "train_uses_stage4_decision"


def _build_holdout_matrix(decision_rows: Sequence[Dict[str, str]], ledger_rows: Sequence[Dict[str, str]]) -> List[Dict[str, Any]]:
    ledger_by_entity: Dict[Tuple[str, str], List[Dict[str, str]]] = defaultdict(list)
    for row in ledger_rows:
        ledger_by_entity[(str(row.get("entity_type") or ""), str(row.get("entity_key") or ""))].append(row)

    out: List[Dict[str, Any]] = []
    for decision in decision_rows:
        entity_key = str(decision.get("entity_key") or "")
        entity_type = str(decision.get("entity_type") or "")
        rows = ledger_by_entity.get((entity_type, entity_key), [])
        if not rows:
            continue
        windows = sorted({str(row.get("window") or "") for row in rows if row.get("window")})
        for holdout in windows:
            train_rows = [row for row in rows if str(row.get("window") or "") != holdout]
            holdout_rows = [row for row in rows if str(row.get("window") or "") == holdout]
            train = _aggregate_rows(train_rows)
            held = _aggregate_rows(holdout_rows)
            survives, train_label = _train_survives(
                str(decision.get("queue") or ""),
                str(decision.get("stage4_replay_decision") or ""),
                train,
                str(decision.get("shared_lineage_risk") or ""),
            )
            holdout_confirmed = (
                _safe_int(held.get("active_state_days")) > 0
                and (
                    _safe_int(held.get("supported_event_count")) > 0
                    or _safe_int(held.get("positive_conversion_event_count")) > 0
                    or (
                        str(decision.get("queue") or "") == "P3_vtrac_decay_watch_replay"
                        and _safe_int(held.get("matched_value_count")) > 0
                    )
                )
            )
            if not survives:
                outcome = "train_did_not_survive"
            elif _safe_int(held.get("active_state_days")) == 0:
                outcome = "no_holdout_denominator"
            elif holdout_confirmed:
                outcome = "holdout_confirmed"
            else:
                outcome = "holdout_missed"
            out.append(
                {
                    "entity_type": entity_type,
                    "entity_key": entity_key,
                    "queue": decision.get("queue"),
                    "mechanism_family": decision.get("mechanism_family"),
                    "future_primitive": decision.get("future_primitive"),
                    "stage4_replay_decision": decision.get("stage4_replay_decision"),
                    "shared_lineage_risk": decision.get("shared_lineage_risk"),
                    "source_a": decision.get("source_a"),
                    "source_b": decision.get("source_b"),
                    "holdout_window": holdout,
                    "train_status": train_label,
                    "holdout_outcome": outcome,
                    "train_windows": train.get("windows"),
                    "train_active_state_days": train.get("active_state_days"),
                    "train_avg_pool_or_exposure_per_state_day": train.get("avg_pool_or_exposure_per_state_day"),
                    "train_supported_events_per_100_state_days": train.get("supported_events_per_100_state_days"),
                    "train_positive_conversions_per_100_state_days": train.get("positive_conversions_per_100_state_days"),
                    "train_wrong_lane_event_count": train.get("wrong_lane_event_count"),
                    "holdout_active_state_days": held.get("active_state_days"),
                    "holdout_supported_event_count": held.get("supported_event_count"),
                    "holdout_positive_conversion_event_count": held.get("positive_conversion_event_count"),
                    "holdout_matched_value_count": held.get("matched_value_count"),
                    "holdout_wrong_lane_event_count": held.get("wrong_lane_event_count"),
                    "holdout_supported_events_per_100_state_days": held.get("supported_events_per_100_state_days"),
                    "holdout_positive_conversions_per_100_state_days": held.get("positive_conversions_per_100_state_days"),
                }
            )
    return out


def _build_casebook(
    decision_rows: Sequence[Dict[str, str]],
    ledger_rows: Sequence[Dict[str, str]],
    *,
    limit: int,
) -> List[Dict[str, Any]]:
    ledger_by_entity: Dict[Tuple[str, str], List[Dict[str, str]]] = defaultdict(list)
    for row in ledger_rows:
        ledger_by_entity[(str(row.get("entity_type") or ""), str(row.get("entity_key") or ""))].append(row)

    priority_order = {
        "survived_as_boxed_translator_candidate": 1,
        "survived_with_lineage_guardrail": 2,
        "survived_as_support_gate": 3,
        "blocked_by_state_concentration": 4,
        "watch_decay_only": 5,
        "low_denominator_watchlist": 6,
    }
    ranked_decisions = sorted(
        decision_rows,
        key=lambda row: (
            priority_order.get(str(row.get("stage4_replay_decision") or ""), 9),
            -_safe_float(row.get("positive_conversions_per_100_state_days")),
            -_safe_float(row.get("supported_events_per_100_state_days")),
            str(row.get("entity_key") or ""),
        ),
    )

    out: List[Dict[str, Any]] = []
    role_counts: Counter[str] = Counter()
    for decision in ranked_decisions:
        role = str(decision.get("stage4_replay_decision") or "")
        if role not in priority_order:
            continue
        if role_counts[role] >= max(8, limit // len(priority_order)):
            continue
        entity = (str(decision.get("entity_type") or ""), str(decision.get("entity_key") or ""))
        rows = ledger_by_entity.get(entity, [])
        if not rows:
            continue
        best = sorted(
            rows,
            key=lambda row: (
                -_safe_int(row.get("positive_conversion_event_count")),
                -_safe_int(row.get("supported_event_count")),
                -_safe_int(row.get("matched_value_count")),
                str(row.get("window") or ""),
            ),
        )[0]
        out.append(
            {
                "case_role": role,
                "entity_type": decision.get("entity_type"),
                "entity_key": decision.get("entity_key"),
                "window": best.get("window"),
                "queue": decision.get("queue"),
                "mechanism_family": decision.get("mechanism_family"),
                "future_primitive": decision.get("future_primitive"),
                "source_a": decision.get("source_a"),
                "source_b": decision.get("source_b"),
                "shared_lineage_risk": decision.get("shared_lineage_risk"),
                "active_state_days": best.get("active_state_days"),
                "avg_pool_or_exposure_per_state_day": best.get("avg_overlap_values_per_state_day"),
                "supported_event_count": best.get("supported_event_count"),
                "positive_conversion_event_count": best.get("positive_conversion_event_count"),
                "wrong_lane_event_count": best.get("wrong_lane_event_count"),
                "matched_value_count": best.get("matched_value_count"),
                "top_state_by_support": best.get("top_state_by_support"),
                "top_state_support_share": best.get("top_state_support_share"),
                "top3_state_support_mix": best.get("top3_state_support_mix"),
                "stage4_rationale": decision.get("stage4_rationale"),
                "readback_note": _casebook_note(role),
            }
        )
        role_counts[role] += 1
        if len(out) >= limit:
            break
    return out


def _casebook_note(role: str) -> str:
    if role == "survived_as_boxed_translator_candidate":
        return "clean future translator exemplar; still read-only until holdout/prototype work"
    if role == "survived_with_lineage_guardrail":
        return "useful mechanism exemplar, but duplicate-credit scoring must be blocked"
    if role == "survived_as_support_gate":
        return "support-only evidence; useful when paired with sharper bounded sources"
    if role == "blocked_by_state_concentration":
        return "fragile concentration example; do not promote without broader confirmation"
    if role == "watch_decay_only":
        return "territory/carryforward example; not boxed spend permission"
    if role == "low_denominator_watchlist":
        return "thin but interesting example; collect more windows before promotion"
    return "fixture example"


def _build_translator_queue(cluster_rows: Sequence[Dict[str, Any]], holdout_rows: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    holdout_by_cluster: Dict[str, Counter[str]] = defaultdict(Counter)
    for row in holdout_rows:
        key = _cluster_key(row)
        holdout_by_cluster[key][str(row.get("holdout_outcome") or "")] += 1

    out: List[Dict[str, Any]] = []
    for cluster in cluster_rows:
        use = str(cluster.get("recommended_cluster_use") or "")
        if use not in {
            "translator_candidate_cluster",
            "translator_candidate_with_duplicate_credit_guardrail",
            "support_gate_cluster",
            "state_concentration_retest_or_restraint",
            "decay_or_vtrac_watch_cluster",
            "low_denominator_watchlist",
        }:
            continue
        counts = holdout_by_cluster.get(str(cluster.get("cluster_key") or ""), Counter())
        confirmed = counts.get("holdout_confirmed", 0)
        missed = counts.get("holdout_missed", 0)
        denominator = confirmed + missed
        if use == "translator_candidate_cluster":
            next_action = "prototype_as_read_only_boxed_translator_rule"
        elif use == "translator_candidate_with_duplicate_credit_guardrail":
            next_action = "prototype_with_lineage_deduplication"
        elif use == "support_gate_cluster":
            next_action = "prototype_as_gate_not_standalone"
        elif use == "state_concentration_retest_or_restraint":
            next_action = "retest_by_state_and_consider_penalty"
        elif use == "decay_or_vtrac_watch_cluster":
            next_action = "keep_in_decay_watch_not_boxed_spend"
        else:
            next_action = "collect_more_windows_before_promotion"
        out.append(
            {
                "cluster_key": cluster.get("cluster_key"),
                "mechanism_family": cluster.get("mechanism_family"),
                "future_primitive": cluster.get("future_primitive"),
                "recommended_cluster_use": use,
                "next_action": next_action,
                "entity_count": cluster.get("entity_count"),
                "stage4_decision_mix": cluster.get("stage4_decision_mix"),
                "holdout_confirmed": confirmed,
                "holdout_missed": missed,
                "holdout_confirmation_rate": _rate(confirmed, denominator),
                "positive_conversions_per_100_state_days": cluster.get("positive_conversions_per_100_state_days"),
                "supported_events_per_100_state_days": cluster.get("supported_events_per_100_state_days"),
                "representative_entity": cluster.get("representative_entity"),
            }
        )
    action_order = {
        "prototype_as_read_only_boxed_translator_rule": 1,
        "prototype_with_lineage_deduplication": 2,
        "prototype_as_gate_not_standalone": 3,
        "keep_in_decay_watch_not_boxed_spend": 4,
        "collect_more_windows_before_promotion": 5,
        "retest_by_state_and_consider_penalty": 6,
    }
    return sorted(
        out,
        key=lambda row: (
            action_order.get(str(row.get("next_action") or ""), 99),
            -_safe_float(row.get("holdout_confirmation_rate")),
            -_safe_float(row.get("positive_conversions_per_100_state_days")),
            str(row.get("cluster_key") or ""),
        ),
    )


def _write_casebook_md(path: Path, rows: Sequence[Dict[str, Any]], *, force: bool) -> None:
    sections: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for row in rows:
        sections[str(row.get("case_role") or "fixture")].append(row)
    lines: List[str] = [
        "# Stage 4B Survivor / Support / Restraint Casebook",
        "",
        "Purpose: compact exemplar rows for manual readback after Stage 4 fixture replay.",
        "",
    ]
    for role in [
        "survived_as_boxed_translator_candidate",
        "survived_with_lineage_guardrail",
        "survived_as_support_gate",
        "blocked_by_state_concentration",
        "watch_decay_only",
        "low_denominator_watchlist",
    ]:
        role_rows = sections.get(role, [])
        if not role_rows:
            continue
        lines += [
            f"## {role}",
            "",
            "| entity | window | primitive | support | positive | top state share | note |",
            "|---|---:|---:|---:|---:|---:|---|",
        ]
        for row in role_rows[:16]:
            lines.append(
                "| "
                + " | ".join(
                    [
                        f"`{row.get('entity_key')}`",
                        str(row.get("window")),
                        f"`{row.get('future_primitive')}`",
                        str(row.get("supported_event_count")),
                        str(row.get("positive_conversion_event_count")),
                        _pct(row.get("top_state_support_share")),
                        str(row.get("readback_note")),
                    ]
                )
                + " |"
            )
        lines.append("")
    _write_text(path, "\n".join(lines), force=force)


def _build_markdown(
    *,
    runs2_dir: Path,
    decision_rows: Sequence[Dict[str, str]],
    cluster_rows: Sequence[Dict[str, Any]],
    holdout_rows: Sequence[Dict[str, Any]],
    translator_rows: Sequence[Dict[str, Any]],
    negative_rows: Sequence[Dict[str, str]],
    paths: Dict[str, Path],
) -> str:
    decision_counts = Counter(str(row.get("stage4_replay_decision") or "") for row in decision_rows)
    cluster_use = Counter(str(row.get("recommended_cluster_use") or "") for row in cluster_rows)
    holdout_counts = Counter(str(row.get("holdout_outcome") or "") for row in holdout_rows)
    next_actions = Counter(str(row.get("next_action") or "") for row in translator_rows)
    top_translator = [
        row
        for row in translator_rows
        if str(row.get("next_action") or "") in {"prototype_as_read_only_boxed_translator_rule", "prototype_with_lineage_deduplication"}
    ][:20]

    lines: List[str] = [
        "# Analysis Arena Stage 4B Replay Readback",
        "",
        "Purpose: turn Stage 4 fixture replay into primitive-level decision intelligence before any scoring or translator rewrite.",
        "",
        "## Metadata",
        f"- runs2_dir: `{safe_rel(runs2_dir)}`",
        f"- stage4_decision_rows: `{len(decision_rows)}`",
        f"- primitive_clusters: `{len(cluster_rows)}`",
        f"- holdout_rows: `{len(holdout_rows)}`",
        f"- translator_queue_rows: `{len(translator_rows)}`",
        f"- negative_control_families: `{len(negative_rows)}`",
        "",
        "## Guardrails",
        "- Stage 4B is read-only and cannot change scoring, candidate generation, translator logic, budget logic, or legacy infrastructure.",
        "- Primitive clusters collapse aliases and old-system locator names; they are not live rules.",
        "- Holdout confirmation is a research filter, not live-play permission.",
        "- Support gates, VTRAC/decay rows, concentration-blocked rows, and negative controls must stay in their lanes.",
        "",
        "## Stage 4 Decision Baseline",
        "",
    ]
    for key, count in decision_counts.most_common():
        lines.append(f"- `{key}`: `{count}`")
    lines += ["", "## Primitive Cluster Uses", ""]
    for key, count in cluster_use.most_common():
        lines.append(f"- `{key}`: `{count}`")
    lines += ["", "## Leave-One-Window-Out Outcomes", ""]
    for key, count in holdout_counts.most_common():
        lines.append(f"- `{key}`: `{count}`")
    lines += ["", "## Translator Queue Next Actions", ""]
    for key, count in next_actions.most_common():
        lines.append(f"- `{key}`: `{count}`")
    lines += [
        "",
        "## Top Translator Candidate Clusters",
        "",
        "| cluster | use | holdout confirm | pos/100 ASD | support/100 ASD | representative |",
        "|---|---:|---:|---:|---:|---|",
    ]
    for row in top_translator:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{row.get('cluster_key')}`",
                    str(row.get("recommended_cluster_use")),
                    _pct(row.get("holdout_confirmation_rate")),
                    _fmt(row.get("positive_conversions_per_100_state_days")),
                    _fmt(row.get("supported_events_per_100_state_days")),
                    f"`{row.get('representative_entity')}`",
                ]
            )
            + " |"
        )
    lines += [
        "",
        "## Interpretation",
        "- The cleanest future translator material is the cluster set marked `translator_candidate_cluster`.",
        "- `translator_candidate_with_duplicate_credit_guardrail` is valuable but must be de-duplicated before any scoring prototype.",
        "- `support_gate_cluster` should help later ranking/translator confidence only when paired with sharper bounded evidence.",
        "- `state_concentration_retest_or_restraint` rows are warning signs until broader state confirmation appears.",
        "- Negative-control families remain restraint/penalty/veto assets.",
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
    stage4 = _stage4_paths(runs2_dir)
    paths = _cycle_paths(output_dir)

    decision_rows = _read_csv_rows(stage4["decision_csv"])
    ledger_rows = _read_csv_rows(stage4["ledger_csv"])
    negative_rows = _read_csv_rows(stage4["negative_csv"])
    if not decision_rows or not ledger_rows:
        raise SystemExit("Stage 4 outputs are missing or empty. Run stage4-fixture-replay first.")

    cluster_rows = _build_cluster_registry(decision_rows)
    holdout_rows = _build_holdout_matrix(decision_rows, ledger_rows)
    casebook_rows = _build_casebook(decision_rows, ledger_rows, limit=int(args.casebook_limit))
    translator_rows = _build_translator_queue(cluster_rows, holdout_rows)

    _write_csv(paths["cluster_csv"], cluster_rows, force=bool(args.force))
    _write_csv(paths["holdout_csv"], holdout_rows, force=bool(args.force))
    _write_csv(paths["casebook_csv"], casebook_rows, force=bool(args.force))
    _write_casebook_md(paths["casebook_md"], casebook_rows, force=bool(args.force))
    _write_csv(paths["translator_queue_csv"], translator_rows, force=bool(args.force))

    payload = {
        "metadata": {
            "runs2_dir": safe_rel(runs2_dir),
            "stage4_decision_rows": len(decision_rows),
            "primitive_clusters": len(cluster_rows),
            "holdout_rows": len(holdout_rows),
            "casebook_rows": len(casebook_rows),
            "translator_queue_rows": len(translator_rows),
            "guardrail": "read_only_stage4b_interpretation_no_live_scoring_changes",
        },
        "stage4_decision_counts": Counter(str(row.get("stage4_replay_decision") or "") for row in decision_rows),
        "cluster_use_counts": Counter(str(row.get("recommended_cluster_use") or "") for row in cluster_rows),
        "holdout_outcome_counts": Counter(str(row.get("holdout_outcome") or "") for row in holdout_rows),
        "translator_next_action_counts": Counter(str(row.get("next_action") or "") for row in translator_rows),
        "top_translator_queue": translator_rows[:50],
        "outputs": {label: safe_rel(path) for label, path in paths.items()},
    }
    _write_json(paths["json"], payload, force=bool(args.force))
    _write_text(
        paths["md"],
        _build_markdown(
            runs2_dir=runs2_dir,
            decision_rows=decision_rows,
            cluster_rows=cluster_rows,
            holdout_rows=holdout_rows,
            translator_rows=translator_rows,
            negative_rows=negative_rows,
            paths=paths,
        ),
        force=bool(args.force),
    )

    print(f"[OK] Wrote Stage-4B readback: {safe_rel(paths['md'])}")
    print(f"[OK] Wrote primitive clusters: {len(cluster_rows)}")
    print(f"[OK] Wrote holdout rows: {len(holdout_rows)}")
    print(f"[OK] Wrote translator queue rows: {len(translator_rows)}")


if __name__ == "__main__":
    main()
