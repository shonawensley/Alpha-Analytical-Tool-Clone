#!/usr/bin/env python3
"""Create the Stage-5 Analysis Arena readback decision memo.

This is a read-only interpretation layer over the Stage-5 fixture evaluator.
It converts the scorecards, ablations, support/restraint audits, and
stratification files into explicit next-step gates. It does not alter live
scoring, candidate generation, translator logic, budget logic, or legacy
infrastructure.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, MutableMapping, Sequence, Tuple


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
READBACK_PREFIX = "ANALYSIS_ARENA__CYCLE__STAGE5_READBACK"

MODE_INTENT: Dict[str, str] = {
    "clean_boxed_only": "candidate_expression_baseline",
    "clean_lineage_supported_restrained": "lineage_supported_restrained_candidate_expression",
    "clean_plus_lineage_deduped": "candidate_expression_with_lineage_dedup",
    "clean_with_restraint_filter": "candidate_expression_with_restraint_filter",
    "clean_with_support_context": "candidate_expression_with_support_context",
    "decay_watch_companion": "decay_companion_only",
    "low_denominator_watchlist": "low_denominator_watchlist",
    "restraint_retest": "restraint_calibration_retest",
    "support_gate_context": "support_context_only",
}

CANDIDATE_EXPRESSION_MODES = {
    "clean_boxed_only",
    "clean_lineage_supported_restrained",
    "clean_plus_lineage_deduped",
    "clean_with_restraint_filter",
    "clean_with_support_context",
}


def _parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--runs2-dir", default=str(RUNS_2_DIR), help="RUNS_2 root containing Stage-5 outputs.")
    ap.add_argument("--output-dir", default=str(RUNS_2_DIR), help="Cycle-level output directory.")
    ap.add_argument("--force", action="store_true", help="Overwrite existing Stage-5 readback outputs.")
    return ap.parse_args()


def _stage5_paths(runs2_dir: Path) -> Dict[str, Path]:
    return {
        "evaluator_md": runs2_dir / f"{STAGE5_PREFIX}_SHADOW_TRANSLATOR_FIXTURE_EVALUATOR.md",
        "evaluator_json": runs2_dir / f"{STAGE5_PREFIX}_SHADOW_TRANSLATOR_FIXTURE_EVALUATOR.json",
        "completeness": runs2_dir / f"{STAGE5_PREFIX}_VALUE_COMPLETENESS_AUDIT.csv",
        "mode_scorecard": runs2_dir / f"{STAGE5_PREFIX}_PROTOTYPE_MODE_SCORECARD.csv",
        "ablation": runs2_dir / f"{STAGE5_PREFIX}_ABLATION_MATRIX.csv",
        "support": runs2_dir / f"{STAGE5_PREFIX}_SUPPORT_GATE_ABLATION.csv",
        "restraint": runs2_dir / f"{STAGE5_PREFIX}_RESTRAINT_EFFECT_AUDIT.csv",
        "window": runs2_dir / f"{STAGE5_PREFIX}_WINDOW_STRATIFICATION.csv",
        "state": runs2_dir / f"{STAGE5_PREFIX}_STATE_STRATIFICATION.csv",
        "pro44": runs2_dir / f"{STAGE5_PREFIX}_PRO44_COMPLIANCE_CHECKLIST.csv",
    }


def _output_paths(output_dir: Path) -> Dict[str, Path]:
    return {
        "md": output_dir / f"{READBACK_PREFIX}_DECISION_MEMO.md",
        "json": output_dir / f"{READBACK_PREFIX}_DECISION_MEMO.json",
        "mode_decisions_csv": output_dir / f"{READBACK_PREFIX}_MODE_DECISIONS.csv",
        "next_action_csv": output_dir / f"{READBACK_PREFIX}_NEXT_ACTION_QUEUE.csv",
    }


def _load_required_csv(path: Path, label: str) -> List[Dict[str, str]]:
    rows = _read_csv_rows(path)
    if not rows:
        raise SystemExit(f"Missing or empty required Stage-5 {label}: {safe_rel(path)}")
    return rows


def _load_conditional_csv(path: Path, label: str, *, required: bool) -> List[Dict[str, str]]:
    rows = _read_csv_rows(path)
    if required and not rows:
        raise SystemExit(f"Missing or empty required Stage-5 {label}: {safe_rel(path)}")
    return rows


def _load_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8", errors="replace"))


def _mode_positive_concentration(
    rows: Sequence[Mapping[str, Any]],
    *,
    group_field: str,
) -> Dict[str, Dict[str, Any]]:
    totals: Dict[str, int] = defaultdict(int)
    groups: Dict[str, Counter[str]] = defaultdict(Counter)
    for row in rows:
        mode = str(row.get("prototype_mode") or "")
        group = str(row.get(group_field) or "")
        positive = _safe_int(row.get("positive_conversion_event_count"))
        if not mode or not group:
            continue
        totals[mode] += positive
        groups[mode][group] += positive

    out: Dict[str, Dict[str, Any]] = {}
    for mode, total in totals.items():
        if total <= 0:
            out[mode] = {
                "total_positive_conversion_event_count": 0,
                "top_group": "",
                "top_group_positive_conversion_event_count": 0,
                "top_group_positive_conversion_share": 0.0,
                "concentration_flag": "no_positive_conversion_labels",
            }
            continue
        top_group, top_count = groups[mode].most_common(1)[0]
        share = _rate(top_count, total)
        flag = "high_concentration" if share >= 0.75 else "moderate_concentration" if share >= 0.5 else "distributed"
        out[mode] = {
            "total_positive_conversion_event_count": total,
            "top_group": top_group,
            "top_group_positive_conversion_event_count": top_count,
            "top_group_positive_conversion_share": share,
            "concentration_flag": flag,
        }
    return out


def _aggregate_rows(rows: Iterable[Mapping[str, Any]], label_field: str) -> List[Dict[str, Any]]:
    aggs: Dict[str, MutableMapping[str, Any]] = {}
    for row in rows:
        label = str(row.get(label_field) or "unknown")
        agg = aggs.setdefault(
            label,
            {
                label_field: label,
                "source_rows": 0,
                "ledger_rows": 0,
                "active_state_days": 0,
                "total_overlap_values": 0,
                "matched_value_count": 0,
                "false_positive_proxy_value_count": 0,
                "positive_conversion_event_count": 0,
                "gap_teacher_event_count": 0,
                "wrong_lane_event_count": 0,
            },
        )
        agg["source_rows"] += 1
        for key in (
            "ledger_rows",
            "active_state_days",
            "total_overlap_values",
            "matched_value_count",
            "false_positive_proxy_value_count",
            "positive_conversion_event_count",
            "gap_teacher_event_count",
            "wrong_lane_event_count",
        ):
            agg[key] += _safe_int(row.get(key))

    out: List[Dict[str, Any]] = []
    for agg in aggs.values():
        total = _safe_int(agg.get("total_overlap_values"))
        state_days = _safe_int(agg.get("active_state_days"))
        positive = _safe_int(agg.get("positive_conversion_event_count"))
        agg["matched_value_rate"] = _rate(_safe_int(agg.get("matched_value_count")), total)
        agg["false_positive_proxy_rate"] = _rate(_safe_int(agg.get("false_positive_proxy_value_count")), total)
        agg["positive_conversions_per_100_state_days"] = 100.0 * _rate(positive, state_days)
        agg["pool_normalized_positive_yield"] = 100.0 * _rate(positive, total)
        out.append(dict(agg))
    return sorted(out, key=lambda row: str(row.get(label_field) or ""))


def _ablation_summary(rows: Sequence[Mapping[str, Any]]) -> Dict[str, Any]:
    positive_lift = [
        row
        for row in rows
        if _safe_float(row.get("avg_overlap_support_per100_vs_best_source")) > 0
    ]
    pool_reduction = [
        row
        for row in rows
        if _safe_float(row.get("avg_overlap_pool_reduction_vs_smaller_source")) > 1.0
    ]
    interpretation_counts = Counter(str(row.get("interpretation") or "") for row in rows)
    best_positive = sorted(
        positive_lift,
        key=lambda row: _safe_float(row.get("avg_overlap_support_per100_vs_best_source")),
        reverse=True,
    )[:5]
    strongest_pool_reduction = sorted(
        pool_reduction,
        key=lambda row: _safe_float(row.get("avg_overlap_pool_reduction_vs_smaller_source")),
        reverse=True,
    )[:5]
    return {
        "rows": len(rows),
        "positive_overlap_lift_rows": len(positive_lift),
        "pool_reduction_rows": len(pool_reduction),
        "interpretation_counts": dict(interpretation_counts),
        "best_positive_overlap_rows": [
            {
                "prototype_mode": row.get("prototype_mode", ""),
                "prototype_lane": row.get("prototype_lane", ""),
                "mechanism_family": row.get("mechanism_family", ""),
                "overlap_lift": _safe_float(row.get("avg_overlap_support_per100_vs_best_source")),
                "pool_reduction": _safe_float(row.get("avg_overlap_pool_reduction_vs_smaller_source")),
                "interpretation": row.get("interpretation", ""),
            }
            for row in best_positive
        ],
        "strongest_pool_reduction_rows": [
            {
                "prototype_mode": row.get("prototype_mode", ""),
                "prototype_lane": row.get("prototype_lane", ""),
                "mechanism_family": row.get("mechanism_family", ""),
                "overlap_lift": _safe_float(row.get("avg_overlap_support_per100_vs_best_source")),
                "pool_reduction": _safe_float(row.get("avg_overlap_pool_reduction_vs_smaller_source")),
                "interpretation": row.get("interpretation", ""),
            }
            for row in strongest_pool_reduction
        ],
    }


def _decision_for_mode(
    row: Mapping[str, Any],
    *,
    window_conc: Mapping[str, Any],
    state_conc: Mapping[str, Any],
) -> Tuple[str, str, str, str, str]:
    mode = str(row.get("prototype_mode") or "")
    sample_rate = _safe_float(row.get("sample_completeness_rate"))
    state_days = _safe_int(row.get("active_state_days"))
    false_positive_rate = _safe_float(row.get("false_positive_proxy_rate"))
    pool_yield = _safe_float(row.get("pool_normalized_positive_yield"))
    avg_pool = _safe_float(row.get("avg_pool_or_exposure_per_state_day"))
    window_flag = str(window_conc.get("concentration_flag") or "")
    concentration_note = ""
    if window_flag == "high_concentration":
        concentration_note = f" Positive conversion labels are concentrated in {window_conc.get('top_group')}."

    if sample_rate < 0.95:
        return (
            "blocked_sample_incomplete",
            "blocked",
            "Value-level sample completeness is below the required threshold.",
            "Do not interpret value-level precision until sample completeness is repaired.",
            "no_live_permission",
        )
    if mode == "decay_watch_companion":
        return (
            "companion_only",
            "keep_separate",
            "High coverage but high false-positive proxy and wrong-lane pressure; useful for carryforward context, not boxed permission.",
            "Keep as decay/watch companion and feed only future carryover or territory research.",
            "no_live_permission",
        )
    if mode == "support_gate_context":
        return (
            "support_modifier_only",
            "keep_as_context",
            "Broad support context carries signal but is too wide to stand alone.",
            "Use as a modifier/gate paired with sharper candidate-expression evidence.",
            "no_live_permission",
        )
    if mode == "low_denominator_watchlist" or state_days < 30:
        return (
            "watchlist_retest",
            "retest_before_design",
            "The denominator is too small or fragile for translator design despite attractive rates.",
            "Keep as a retest/watchlist row and require more state-days before specification work.",
            "no_live_permission",
        )
    if mode == "restraint_retest":
        return (
            "restraint_calibration",
            "retest_before_design",
            "The mode is useful for restraint design, but not a candidate-expression lane.",
            "Use to calibrate future penalty/veto surfaces; do not promote as candidate generation.",
            "no_live_permission",
        )
    if mode == "clean_with_restraint_filter":
        return (
            "primary_shadow_spec_seed",
            "design_shadow_spec_next",
            f"Best candidate-expression balance: lower false-positive proxy than broad lineage/support modes and strong pool-normalized yield.{concentration_note}",
            "Draft a shadow-only translator specification around restrained candidate-expression behavior.",
            "shadow_spec_only",
        )
    if mode == "clean_lineage_supported_restrained":
        return (
            "secondary_shadow_spec_seed",
            "design_shadow_spec_next",
            f"Useful restrained lineage/support candidate expression with controlled false-positive proxy, but smaller denominator than broad lineage modes.{concentration_note}",
            "Carry as a secondary shadow-spec lane with lineage de-duplication explicit.",
            "shadow_spec_only",
        )
    if mode == "clean_plus_lineage_deduped":
        return (
            "candidate_foundation_needs_pool_control",
            "narrow_before_design",
            f"Strong event density, but broad pool size and higher false-positive proxy require narrowing before specification.{concentration_note}",
            "Use as a foundation for narrowed variants, not as a direct translator rule.",
            "no_live_permission",
        )
    if mode == "clean_with_support_context":
        return (
            "broad_context_needs_narrowing",
            "narrow_before_design",
            f"Support context increases broad coverage but also expands pool size and false-positive proxy.{concentration_note}",
            "Test support as a paired modifier against clean/restrained candidate rows.",
            "no_live_permission",
        )
    if mode == "clean_boxed_only":
        return (
            "baseline_candidate_expression",
            "baseline_only",
            f"Useful baseline for comparison, but weaker than restrained candidate-expression modes on yield and false-positive proxy.{concentration_note}",
            "Keep as a baseline to measure whether added restraint/support improves the translator.",
            "no_live_permission",
        )

    if avg_pool > 100 or false_positive_rate > 0.55 or pool_yield < 10:
        return (
            "needs_narrowing",
            "narrow_before_design",
            "Current mode is too broad or too weak for direct specification.",
            "Keep as analysis material until a narrower fixture passes.",
            "no_live_permission",
        )
    return (
        "review_candidate",
        "manual_review",
        "Mode passed basic completeness checks but has no explicit readback policy.",
        "Review manually before assigning any future design role.",
        "no_live_permission",
    )


def _mode_decision_rows(
    scorecard_rows: Sequence[Mapping[str, Any]],
    *,
    window_concentration: Mapping[str, Mapping[str, Any]],
    state_concentration: Mapping[str, Mapping[str, Any]],
) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for row in scorecard_rows:
        mode = str(row.get("prototype_mode") or "")
        wconc = window_concentration.get(mode, {})
        sconc = state_concentration.get(mode, {})
        decision, status, reason, next_action, permission = _decision_for_mode(
            row,
            window_conc=wconc,
            state_conc=sconc,
        )
        rows.append(
            {
                "prototype_mode": mode,
                "intended_role": MODE_INTENT.get(mode, "unknown"),
                "readback_decision": decision,
                "status": status,
                "allowed_permission": permission,
                "next_action": next_action,
                "reason": reason,
                "ledger_rows": _safe_int(row.get("ledger_rows")),
                "cluster_count": _safe_int(row.get("cluster_count")),
                "window_count": _safe_int(row.get("window_count")),
                "state_count": _safe_int(row.get("state_count")),
                "active_state_days": _safe_int(row.get("active_state_days")),
                "avg_pool_or_exposure_per_state_day": _safe_float(row.get("avg_pool_or_exposure_per_state_day")),
                "matched_value_rate": _safe_float(row.get("matched_value_rate")),
                "false_positive_proxy_rate": _safe_float(row.get("false_positive_proxy_rate")),
                "positive_conversions_per_100_state_days": _safe_float(row.get("positive_conversions_per_100_state_days")),
                "pool_normalized_positive_yield": _safe_float(row.get("pool_normalized_positive_yield")),
                "deduped_complete_value_match_rate": _safe_float(row.get("deduped_complete_value_match_rate")),
                "sample_completeness_rate": _safe_float(row.get("sample_completeness_rate")),
                "top_window": wconc.get("top_group", ""),
                "top_window_positive_share": wconc.get("top_group_positive_conversion_share", 0.0),
                "window_concentration_flag": wconc.get("concentration_flag", ""),
                "top_state": sconc.get("top_group", ""),
                "top_state_positive_share": sconc.get("top_group_positive_conversion_share", 0.0),
                "state_concentration_flag": sconc.get("concentration_flag", ""),
            }
        )
    return rows


def _next_action_rows(
    mode_rows: Sequence[Mapping[str, Any]],
    *,
    ablation_summary: Mapping[str, Any],
    support_bucket_rows: Sequence[Mapping[str, Any]],
    restraint_bucket_rows: Sequence[Mapping[str, Any]],
) -> List[Dict[str, Any]]:
    actions: List[Dict[str, Any]] = []
    priority = 1
    for row in mode_rows:
        status = str(row.get("status") or "")
        if status in {"design_shadow_spec_next", "narrow_before_design", "retest_before_design"}:
            actions.append(
                {
                    "priority": priority,
                    "action_type": status,
                    "subject": row.get("prototype_mode", ""),
                    "action": row.get("next_action", ""),
                    "rationale": row.get("reason", ""),
                    "allowed_permission": row.get("allowed_permission", ""),
                    "source_artifact": f"{STAGE5_PREFIX}_PROTOTYPE_MODE_SCORECARD.csv",
                }
            )
            priority += 1

    high_concentration_modes = [
        str(row.get("prototype_mode") or "")
        for row in mode_rows
        if str(row.get("window_concentration_flag") or "") == "high_concentration"
    ]
    if high_concentration_modes:
        actions.append(
            {
                "priority": priority,
                "action_type": "window_concentration_guardrail",
                "subject": "positive_conversion_labels",
                "action": "Treat positive-conversion metrics as March-led until future/fresh windows repeat the same readback shape.",
                "rationale": f"{len(high_concentration_modes)} Stage-5 modes have high positive-conversion window concentration.",
                "allowed_permission": "shadow_spec_with_concentration_warning",
                "source_artifact": f"{STAGE5_PREFIX}_WINDOW_STRATIFICATION.csv",
            }
        )
        priority += 1

    actions.append(
        {
            "priority": priority,
            "action_type": "ablation_guardrail",
            "subject": "source_a_source_b_overlap",
            "action": "Treat overlap as narrowing/restraint unless it beats the best individual source on support rate.",
            "rationale": f"{ablation_summary.get('positive_overlap_lift_rows', 0)} of {ablation_summary.get('rows', 0)} ablation rows showed positive overlap lift over the best source.",
            "allowed_permission": "no_duplicate_credit",
            "source_artifact": f"{STAGE5_PREFIX}_ABLATION_MATRIX.csv",
        }
    )
    priority += 1

    if support_bucket_rows:
        actions.append(
            {
                "priority": priority,
                "action_type": "support_gate_policy",
                "subject": "support_context",
                "action": "Keep support context as paired context, not standalone candidate expression.",
                "rationale": "Support rows are broad context; compare candidate rows with support against candidate rows without support before any specification.",
                "allowed_permission": "context_modifier_only",
                "source_artifact": f"{STAGE5_PREFIX}_SUPPORT_GATE_ABLATION.csv",
            }
        )
        priority += 1

    if restraint_bucket_rows:
        actions.append(
            {
                "priority": priority,
                "action_type": "restraint_calibration",
                "subject": "restraint_filter",
                "action": "Calibrate restraint as penalty/veto pressure, not an automatic discard rule.",
                "rationale": "Stage 5 separates kept and removed rows, but removed high-pressure rows may still contain useful signal and must be audited before hard veto design.",
                "allowed_permission": "penalty_research_only",
                "source_artifact": f"{STAGE5_PREFIX}_RESTRAINT_EFFECT_AUDIT.csv",
            }
        )
        priority += 1

    actions.append(
        {
            "priority": priority,
            "action_type": "macro_findings_gate",
            "subject": "macro_findings_log",
            "action": "Do not append a confirmed macro finding until Stage 5 readback conclusions repeat on a future/fresh window or are explicitly reviewed as provisional.",
            "rationale": "The readback is a decision layer; the Macro Findings Log should preserve evidence-led conclusions, not every infrastructure milestone.",
            "allowed_permission": "provisional_only_until_repeat",
            "source_artifact": f"{READBACK_PREFIX}_DECISION_MEMO.md",
        }
    )
    return actions


def _table(headers: Sequence[str], rows: Sequence[Sequence[Any]]) -> List[str]:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(value) for value in row) + " |")
    return lines


def _render_md(
    *,
    runs2_dir: Path,
    mode_rows: Sequence[Mapping[str, Any]],
    next_actions: Sequence[Mapping[str, Any]],
    completeness_rows: Sequence[Mapping[str, Any]],
    support_bucket_rows: Sequence[Mapping[str, Any]],
    restraint_bucket_rows: Sequence[Mapping[str, Any]],
    ablation_summary: Mapping[str, Any],
    out_paths: Mapping[str, Path],
) -> str:
    all_complete = next((row for row in completeness_rows if str(row.get("window") or "") == "ALL_WINDOWS"), {})
    lines: List[str] = [
        "# Analysis Arena Stage 5 Readback Decision Memo",
        "",
        "Purpose: convert Stage 5 fixture evaluator outputs into explicit shadow-spec, support, restraint, watchlist, and documentation gates before any translator/scoring rewrite.",
        "",
        "## Metadata",
        f"- runs2_dir: `{safe_rel(runs2_dir)}`",
        f"- mode_decisions: `{len(mode_rows)}`",
        f"- next_actions: `{len(next_actions)}`",
        f"- matched_stage5_rows: `{all_complete.get('matched_stage5_rows', '')}`",
        f"- matched_sample_completeness_rate: `{_pct(all_complete.get('matched_sample_completeness_rate'))}`",
        "",
        "## Guardrails",
        "- This readback grants no live scoring, candidate-generation, translator, budget, or legacy-infrastructure permission.",
        "- Stage 5 metrics are fixture evidence. They guide shadow specification and restraint design only.",
        "- Support gates remain modifiers, VTRAC/decay remains companion context, and overlap does not receive duplicate-credit scoring unless it beats source A/source B baselines.",
        "- The Macro Findings Log should receive distilled evidence-led conclusions, not raw infrastructure milestones.",
        "",
        "## Executive Readback",
        "- Stage 5 is complete enough to interpret: matched rows are value-level complete for the generated evaluator set.",
        "- The strongest immediate design seed is the restrained candidate-expression lane, not a broad all-lane blend.",
        "- Support context and decay/watch behavior remain valuable, but they are not standalone boxed/straight permission.",
        "- Source overlap mostly acts as a pool-narrowing/restraint surface rather than independent confirmation.",
        "- Positive-conversion labels are currently March-led in the Stage 5 readback, so cross-window structural coverage is not the same as repeated positive-conversion confirmation.",
        "- The next work should be a shadow translator/scoring specification or narrowed fixture prototype, not a live scoring rewrite.",
        "",
        "## Mode Decision Queue",
    ]
    lines.extend(
        _table(
            [
                "mode",
                "decision",
                "status",
                "avg pool",
                "FP proxy",
                "yield",
                "top window share",
                "allowed",
            ],
            [
                [
                    row.get("prototype_mode", ""),
                    row.get("readback_decision", ""),
                    row.get("status", ""),
                    _fmt(row.get("avg_pool_or_exposure_per_state_day")),
                    _pct(row.get("false_positive_proxy_rate")),
                    _fmt(row.get("pool_normalized_positive_yield")),
                    _pct(row.get("top_window_positive_share")),
                    row.get("allowed_permission", ""),
                ]
                for row in mode_rows
            ],
        )
    )
    lines += [
        "",
        "## Support Context Read",
    ]
    if not support_bucket_rows:
        lines.append("- No support-gate ablation rows were produced because no candidate-expression modes reached Stage 5 in this replay.")
    lines.extend(
        _table(
            ["bucket", "rows", "state-days", "FP proxy", "yield", "read"],
            [
                [
                    row.get("support_ablation_bucket", ""),
                    row.get("ledger_rows", ""),
                    row.get("active_state_days", ""),
                    _pct(row.get("false_positive_proxy_rate")),
                    _fmt(row.get("pool_normalized_positive_yield")),
                    "context_modifier_only",
                ]
                for row in support_bucket_rows
            ],
        )
    )
    lines += [
        "",
        "## Restraint Read",
    ]
    if not restraint_bucket_rows:
        lines.append("- No restraint-effect rows were produced because no candidate-expression modes reached Stage 5 in this replay.")
    lines.extend(
        _table(
            ["bucket", "rows", "state-days", "FP proxy", "yield", "read"],
            [
                [
                    row.get("restraint_bucket", ""),
                    row.get("ledger_rows", ""),
                    row.get("active_state_days", ""),
                    _pct(row.get("false_positive_proxy_rate")),
                    _fmt(row.get("pool_normalized_positive_yield")),
                    "penalty_research_only",
                ]
                for row in restraint_bucket_rows
            ],
        )
    )
    lines += [
        "",
        "## Ablation Read",
        f"- ablation_rows: `{ablation_summary.get('rows', 0)}`",
        f"- positive_overlap_lift_rows: `{ablation_summary.get('positive_overlap_lift_rows', 0)}`",
        f"- pool_reduction_rows: `{ablation_summary.get('pool_reduction_rows', 0)}`",
        "- interpretation: overlap should be treated as narrowing/restraint unless it beats the best individual source.",
        "",
        "## Next Action Queue",
    ]
    lines.extend(
        _table(
            ["priority", "type", "subject", "allowed", "action"],
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
        "## Documentation Memory Rule",
        "- `WORKFLOW_CHANGELOG.md` records what was built or changed.",
        "- `AAT9_ANALYSIS_ARENA__SYSTEM_INDEX.md` records what is part of the active package and where it feeds.",
        "- `AAT9_ANALYSIS_ARENA__MACRO_FINDINGS_LOG.md` records evidence-led findings after review, especially repeated or explicitly provisional conclusions.",
        "- RUNS/RUNS_2 reports and receipts record exact run outputs.",
        "- Git commits record exact implementation checkpoints.",
        "",
        "## Output Files",
    ]
    for key, path in out_paths.items():
        lines.append(f"- {key}: `{safe_rel(path)}`")
    lines.append("")
    return "\n".join(lines)


def build_readback_payload(
    *,
    runs2_dir: Path,
    output_dir: Path,
) -> Tuple[Dict[str, Any], List[Dict[str, Any]], List[Dict[str, Any]], str]:
    paths = _stage5_paths(runs2_dir)
    outputs = _output_paths(output_dir)

    mode_scorecard = _load_required_csv(paths["mode_scorecard"], "prototype mode scorecard")
    ablation_rows = _load_required_csv(paths["ablation"], "ablation matrix")
    window_rows = _load_required_csv(paths["window"], "window stratification")
    state_rows = _load_required_csv(paths["state"], "state stratification")
    completeness_rows = _load_required_csv(paths["completeness"], "value completeness audit")
    pro44_rows = _load_required_csv(paths["pro44"], "PRO_44 checklist")
    evaluator_json = _load_json(paths["evaluator_json"])
    candidate_modes_present = bool(
        CANDIDATE_EXPRESSION_MODES & {str(row.get("prototype_mode") or "") for row in mode_scorecard}
    )
    support_rows = _load_conditional_csv(paths["support"], "support-gate ablation", required=candidate_modes_present)
    restraint_rows = _load_conditional_csv(paths["restraint"], "restraint-effect audit", required=candidate_modes_present)

    window_concentration = _mode_positive_concentration(window_rows, group_field="window")
    state_concentration = _mode_positive_concentration(state_rows, group_field="state_key")
    mode_rows = _mode_decision_rows(
        mode_scorecard,
        window_concentration=window_concentration,
        state_concentration=state_concentration,
    )
    ablation = _ablation_summary(ablation_rows)
    support_bucket_rows = _aggregate_rows(support_rows, "support_ablation_bucket")
    restraint_bucket_rows = _aggregate_rows(restraint_rows, "restraint_bucket")
    next_actions = _next_action_rows(
        mode_rows,
        ablation_summary=ablation,
        support_bucket_rows=support_bucket_rows,
        restraint_bucket_rows=restraint_bucket_rows,
    )

    payload: Dict[str, Any] = {
        "runs2_dir": safe_rel(runs2_dir),
        "source_files": {key: safe_rel(path) for key, path in paths.items()},
        "stage5_metadata": evaluator_json.get("metadata", {}),
        "value_completeness": completeness_rows,
        "mode_decisions": mode_rows,
        "support_bucket_readback": support_bucket_rows,
        "restraint_bucket_readback": restraint_bucket_rows,
        "conditional_empty_inputs": {
            "candidate_expression_modes_present": candidate_modes_present,
            "support_gate_ablation_empty_allowed": not candidate_modes_present and not support_rows,
            "restraint_effect_audit_empty_allowed": not candidate_modes_present and not restraint_rows,
            "interpretation": "Empty support/restraint audits are valid only when Stage 5 has no candidate-expression modes.",
        },
        "ablation_summary": ablation,
        "pro44_status_counts": dict(Counter(str(row.get("status") or "") for row in pro44_rows)),
        "next_actions": next_actions,
        "guardrail": "read-only decision memo; no live scoring, candidate generation, translator, budget, or legacy infrastructure changes",
    }
    md = _render_md(
        runs2_dir=runs2_dir,
        mode_rows=mode_rows,
        next_actions=next_actions,
        completeness_rows=completeness_rows,
        support_bucket_rows=support_bucket_rows,
        restraint_bucket_rows=restraint_bucket_rows,
        ablation_summary=ablation,
        out_paths=outputs,
    )
    return payload, mode_rows, next_actions, md


def main() -> None:
    args = _parse_args()
    runs2_dir = _resolve_path(args.runs2_dir)
    output_dir = _resolve_path(args.output_dir)
    out_paths = _output_paths(output_dir)
    payload, mode_rows, next_actions, md = build_readback_payload(runs2_dir=runs2_dir, output_dir=output_dir)

    _write_text(out_paths["md"], md, force=bool(args.force))
    _write_json(out_paths["json"], payload, force=bool(args.force))
    _write_csv(out_paths["mode_decisions_csv"], mode_rows, force=bool(args.force))
    _write_csv(out_paths["next_action_csv"], next_actions, force=bool(args.force))

    print(f"[OK] Wrote Stage-5 readback decision memo: {safe_rel(out_paths['md'])}")
    print(f"[OK] Mode decisions: {len(mode_rows)}")
    print(f"[OK] Next actions: {len(next_actions)}")


if __name__ == "__main__":
    main()
