#!/usr/bin/env python3
"""Create the Stage-4 Analysis Arena fixture replay harness.

Stage 4 is a read-only replay/audit layer. It tests the Stage-3 replay queue
against completed Stage-2B fixture windows and adds the controls needed before
any scoring, translator, candidate-generation, or budgeting rewrite:

- mechanism-family separation
- future primitive aliases for old-system locator names
- source-A / source-B / overlap comparison
- shared-lineage duplicate-credit audit
- yield and state concentration diagnostics
- negative-control/restraint summaries
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence, Tuple


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.tools.analysis_arena_window_utils import safe_rel  # type: ignore


RUNS_2_DIR = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS_2"
WINDOW_RE = re.compile(r"^WINDOW_\d{4}-\d{2}-\d{2}_to_\d{4}-\d{2}-\d{2}$")
STAGE4_PREFIX = "ANALYSIS_ARENA__CYCLE__STAGE4"


def _parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--runs2-dir", default=str(RUNS_2_DIR), help="RUNS_2 root containing Stage-2B/Stage-3 artifacts.")
    ap.add_argument("--output-dir", default=str(RUNS_2_DIR), help="Cycle-level output directory.")
    ap.add_argument(
        "--max-replay-rows",
        type=int,
        default=0,
        help="Optional debugging limit for Stage-3 replay queue rows. Default 0 means all rows.",
    )
    ap.add_argument("--force", action="store_true", help="Overwrite existing Stage-4 outputs.")
    return ap.parse_args()


def _resolve_path(value: str | Path) -> Path:
    path = Path(value).expanduser()
    if not path.is_absolute():
        path = (REPO_ROOT / path).resolve()
    return path


def _read_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8", errors="replace"))


def _read_csv_rows(path: Path) -> List[Dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", errors="replace", newline="") as fh:
        return [{k: (v or "") for k, v in row.items()} for row in csv.DictReader(fh)]


def _write_text(path: Path, text: str, *, force: bool) -> None:
    if path.exists() and not force:
        raise SystemExit(f"Refusing to overwrite existing file without --force: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _write_json(path: Path, payload: Any, *, force: bool) -> None:
    _write_text(path, json.dumps(payload, indent=2, sort_keys=True) + "\n", force=force)


def _write_csv(path: Path, rows: Sequence[Dict[str, Any]], *, force: bool, fieldnames: Sequence[str] | None = None) -> None:
    if path.exists() and not force:
        raise SystemExit(f"Refusing to overwrite existing file without --force: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    final_fields: List[str] = list(fieldnames or [])
    for row in rows:
        for key in row:
            if key not in final_fields:
                final_fields.append(key)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=final_fields)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def _safe_int(value: Any, default: int = 0) -> int:
    try:
        text = str(value or "").strip()
        if not text:
            return default
        return int(float(text))
    except Exception:
        return default


def _safe_float(value: Any, default: float = 0.0) -> float:
    try:
        text = str(value or "").strip()
        if not text:
            return default
        return float(text)
    except Exception:
        return default


def _rate(count: int | float, total: int | float) -> float:
    return float(count) / float(total) if total else 0.0


def _pct(value: Any) -> str:
    return f"{100.0 * _safe_float(value):.1f}%"


def _fmt(value: Any, digits: int = 3) -> str:
    return f"{_safe_float(value):.{digits}f}"


def _split_pipe(value: Any) -> List[str]:
    return [part.strip() for part in str(value or "").split("|") if part.strip()]


def _source_family(source_key: str) -> str:
    return source_key.split(":", 1)[0] if ":" in source_key else source_key


def _counter_text(counter: Counter[str]) -> str:
    return "|".join(f"{key}:{count}" for key, count in counter.most_common() if key)


def _discover_windows(runs2_dir: Path) -> List[Path]:
    return sorted(path for path in runs2_dir.iterdir() if path.is_dir() and WINDOW_RE.match(path.name))


def _prefix(window: Path) -> str:
    return f"{window.name}__ANALYSIS_ARENA"


def _window_paths(window: Path) -> Dict[str, Path]:
    stem = _prefix(window)
    return {
        "source_scorecard_json": window / f"{stem}__STAGE2_SIGNAL_FALSE_POSITIVE_SCORECARD.json",
        "stack_scorecard_json": window / f"{stem}__STAGE2B_SIGNAL_STACK_SCORECARD.json",
        "pairing_ledger_csv": window / f"{stem}__STAGE2B_SIGNAL_PAIRING_LEDGER.csv",
    }


def _cycle_paths(output_dir: Path) -> Dict[str, Path]:
    return {
        "md": output_dir / f"{STAGE4_PREFIX}_FIXTURE_REPLAY_SCORECARD.md",
        "json": output_dir / f"{STAGE4_PREFIX}_FIXTURE_REPLAY_SCORECARD.json",
        "ledger_csv": output_dir / f"{STAGE4_PREFIX}_FIXTURE_REPLAY_LEDGER.csv",
        "mechanism_csv": output_dir / f"{STAGE4_PREFIX}_MECHANISM_FAMILY_SCORECARD.csv",
        "ab_csv": output_dir / f"{STAGE4_PREFIX}_SOURCE_A_B_OVERLAP_COMPARISON.csv",
        "yield_csv": output_dir / f"{STAGE4_PREFIX}_YIELD_AND_CONCENTRATION_MATRIX.csv",
        "lineage_csv": output_dir / f"{STAGE4_PREFIX}_SHARED_LINEAGE_AUDIT.csv",
        "decision_csv": output_dir / f"{STAGE4_PREFIX}_REPLAY_DECISION_REGISTRY.csv",
        "negative_csv": output_dir / f"{STAGE4_PREFIX}_NEGATIVE_CONTROL_REPLAY_SUMMARY.csv",
    }


def _stage3_paths(runs2_dir: Path) -> Dict[str, Path]:
    return {
        "replay_csv": runs2_dir / "ANALYSIS_ARENA__CYCLE__STAGE3_REPLAY_QUEUE.csv",
        "registry_csv": runs2_dir / "ANALYSIS_ARENA__CYCLE__STAGE3_PROMOTION_REGISTRY.csv",
        "negative_csv": runs2_dir / "ANALYSIS_ARENA__CYCLE__STAGE3_NEGATIVE_CONTROL_MAP.csv",
        "stage2b_stack_csv": runs2_dir / "ANALYSIS_ARENA__CYCLE__STAGE2B_CROSS_WINDOW_STACK_CONFIRMATION.csv",
        "stage2b_source_csv": runs2_dir / "ANALYSIS_ARENA__CYCLE__STAGE2B_CROSS_WINDOW_SOURCE_CONFIRMATION.csv",
    }


def _parse_pair_key(entity_key: str) -> Tuple[str, str, str]:
    if "::" not in entity_key or " + " not in entity_key:
        return "", "", ""
    pair_scope, rest = entity_key.split("::", 1)
    source_a, source_b = rest.split(" + ", 1)
    return pair_scope.strip(), source_a.strip(), source_b.strip()


def _make_pair_key(pair_scope: str, source_a: str, source_b: str) -> str:
    return f"{pair_scope}::{source_a} + {source_b}"


def _lineage_for_source(source_key: str) -> str:
    family = _source_family(source_key)
    if family in {"arena", "brain1", "translation_sandbox"}:
        return "arena_translation_lineage"
    if family in {"old_candidate_universe", "old_play_card"}:
        return "legacy_control_expression_lineage"
    if family in {"board_scoreboard", "shadow_policy"}:
        return "board_policy_lineage"
    if family in {"blackapple", "control_center", "due_doubles", "aux"}:
        return "control_center_aux_lineage"
    if family in {"profit_alerts", "tracker"}:
        return "tracker_alert_lineage"
    if family in {"stable", "vtrac", "hot_zones", "digit_reduction"}:
        return "native_tool_feed_lineage"
    return f"{family}_lineage" if family else "unknown_lineage"


def _mechanism_family(entity_key: str, source_a: str, source_b: str, lane: str, queue: str) -> Tuple[str, str]:
    text = " ".join([entity_key, source_a, source_b, lane, queue]).lower()
    spendable_box_lane = lane in {"box", "boxed", "straight", "exact"}

    if "blackapple" in text:
        return "blackapple_related_boxed_overlap", "blackapple_support_gate_or_restraint"
    if "profit_alert" in text or "profit-alert" in text:
        return "profit_alert_related_boxed_overlap", "tracker_boxed_support_gate"
    if "mirror_pair_closure" in text:
        return "mirror_pair_closure_spine", "bounded_mirror_pair_box_overlap"
    if "vtrac_enhanced" in text or "secondary_canonical" in text or "secondary_canon" in text or "dominant_vtrac" in text or "top_vtrac" in text:
        primitive = "bounded_vtrac_enhanced_box_overlap" if spendable_box_lane else "territory_vtrac_watch_overlap"
        return "vtrac_enhanced_secondary_spine", primitive
    if "positional" in text:
        return "positional_spine", "bounded_positional_box_overlap"
    if "r-perm" in text or "r_perm" in text or "rperm" in text:
        return "r_perm_spine", "bounded_r_perm_box_overlap"
    if "due_double" in text or "due-doubles" in text:
        return "due_doubles_support_spine", "due_doubles_support_gate"
    if "budgeted_canonical" in text or "analysis_prefix:b12" in text or "analysis_prefix:b24" in text or "analysis_prefix:b36" in text or "old_play_card" in text:
        return "old_play_card_expression_spine", "legacy_budget_expression_locator"
    if "watch" in queue.lower() or lane == "vtrac":
        return "vtrac_decay_watch_spine", "territory_decay_watch_overlap"
    return "misc_stage3_replay", "misc_bounded_replay_fixture"


def _lineage_risk(source_a: str, source_b: str) -> Tuple[str, str, str]:
    sources = [s for s in [source_a, source_b] if s]
    if not sources:
        return "none", "", "source replay row; no A/B duplicate-credit risk"
    lineages = [_lineage_for_source(source) for source in sources]
    lineage_text = "|".join(lineages)
    if len(set(lineages)) == 1 and len(lineages) > 1:
        return "high", lineage_text, "source A and source B share the same evidence lineage; treat overlap as confirmation, not independent votes"
    if "legacy_control_expression_lineage" in lineages and len(lineages) > 1:
        return "medium", lineage_text, "legacy expression surface participates; keep as locator/future primitive evidence, not old-system endorsement"
    return "low", lineage_text, "lineages are different enough for replay comparison, but still require A/B/overlap proof"


def _load_source_scorecards(windows: Sequence[Path]) -> Dict[str, Dict[str, Dict[str, Any]]]:
    out: Dict[str, Dict[str, Dict[str, Any]]] = {}
    for window in windows:
        data = _read_json(_window_paths(window)["source_scorecard_json"])
        rows = data.get("scorecard") or []
        out[window.name] = {str(row.get("source_key") or ""): row for row in rows if row.get("source_key")}
    return out


def _load_stack_scorecards(windows: Sequence[Path]) -> Dict[str, Dict[str, Dict[str, Any]]]:
    out: Dict[str, Dict[str, Dict[str, Any]]] = {}
    for window in windows:
        data = _read_json(_window_paths(window)["stack_scorecard_json"])
        rows = data.get("scorecard") or []
        out[window.name] = {str(row.get("pair_key") or ""): row for row in rows if row.get("pair_key")}
    return out


def _empty_pair_agg() -> Dict[str, Any]:
    return {
        "ledger_state_days": set(),
        "ledger_states": set(),
        "ledger_total_overlap_values": 0,
        "ledger_matched_value_count": 0,
        "ledger_false_positive_proxy_value_count": 0,
        "ledger_matched_event_count": 0,
        "ledger_positive_conversion_event_count": 0,
        "ledger_gap_teacher_event_count": 0,
        "ledger_wrong_lane_event_count": 0,
        "state_support_units": Counter(),
        "state_positive_units": Counter(),
        "state_matched_events": Counter(),
    }


def _load_pairing_ledger_aggs(windows: Sequence[Path]) -> Dict[str, Dict[str, Dict[str, Any]]]:
    out: Dict[str, Dict[str, Dict[str, Any]]] = {}
    for window in windows:
        per_window: Dict[str, Dict[str, Any]] = {}
        path = _window_paths(window)["pairing_ledger_csv"]
        if not path.exists():
            out[window.name] = per_window
            continue
        with path.open("r", encoding="utf-8", errors="replace", newline="") as fh:
            for row in csv.DictReader(fh):
                scope = str(row.get("pair_scope") or "")
                source_a = str(row.get("source_a") or "")
                source_b = str(row.get("source_b") or "")
                if not scope or not source_a or not source_b:
                    continue
                keys = {
                    _make_pair_key(scope, source_a, source_b),
                    _make_pair_key(scope, source_b, source_a),
                }
                matched_events = _safe_int(row.get("matched_event_count"))
                positive = _safe_int(row.get("positive_conversion_event_count"))
                gap = _safe_int(row.get("gap_teacher_event_count"))
                wrong = _safe_int(row.get("wrong_lane_event_count"))
                support_units = matched_events + positive + gap
                state = str(row.get("state_key") or "")
                for key in keys:
                    agg = per_window.setdefault(key, _empty_pair_agg())
                    agg["ledger_state_days"].add(str(row.get("state_day_key") or ""))
                    if state:
                        agg["ledger_states"].add(state)
                    agg["ledger_total_overlap_values"] += _safe_int(row.get("overlap_value_count"))
                    agg["ledger_matched_value_count"] += _safe_int(row.get("matched_value_count"))
                    agg["ledger_false_positive_proxy_value_count"] += _safe_int(row.get("false_positive_proxy_value_count"))
                    agg["ledger_matched_event_count"] += matched_events
                    agg["ledger_positive_conversion_event_count"] += positive
                    agg["ledger_gap_teacher_event_count"] += gap
                    agg["ledger_wrong_lane_event_count"] += wrong
                    if state:
                        agg["state_support_units"][state] += support_units
                        agg["state_positive_units"][state] += positive
                        agg["state_matched_events"][state] += matched_events
        out[window.name] = per_window
    return out


def _top_share(counter: Counter[str]) -> Tuple[str, int, float, str]:
    total = sum(counter.values())
    if not total:
        return "", 0, 0.0, ""
    top_state, top_count = counter.most_common(1)[0]
    top3 = "|".join(f"{state}:{count}" for state, count in counter.most_common(3))
    return top_state, top_count, _rate(top_count, total), top3


def _source_metrics(row: Dict[str, Any] | None, prefix: str) -> Dict[str, Any]:
    row = row or {}
    active = _safe_int(row.get("active_state_days"))
    exposure = _safe_int(row.get("total_exposure_values"))
    lane_hits = _safe_int(row.get("lane_hit_value_count"))
    supported = _safe_int(row.get("supported_winner_event_count"))
    false_positive = _safe_int(row.get("false_positive_proxy_value_count"))
    if not false_positive and exposure and lane_hits:
        false_positive = max(0, exposure - lane_hits)
    return {
        f"{prefix}_source_active_state_days": active,
        f"{prefix}_source_total_exposure_values": exposure,
        f"{prefix}_source_avg_pool_size": _safe_float(row.get("avg_pool_size")),
        f"{prefix}_source_lane_hit_value_count": lane_hits,
        f"{prefix}_source_lane_hit_value_rate": _safe_float(row.get("lane_hit_value_rate"), _rate(lane_hits, exposure)),
        f"{prefix}_source_supported_winner_event_count": supported,
        f"{prefix}_source_supported_per_100_state_days": 100.0 * _rate(supported, active),
        f"{prefix}_source_false_positive_proxy_rate": _safe_float(row.get("false_positive_proxy_rate"), _rate(false_positive, exposure)),
        f"{prefix}_source_stage2_decision": str(row.get("stage2_decision") or ""),
        f"{prefix}_source_target_lane": str(row.get("target_lane") or ""),
    }


def _stack_metrics(row: Dict[str, Any] | None) -> Dict[str, Any]:
    row = row or {}
    active = _safe_int(row.get("active_state_days"))
    total = _safe_int(row.get("total_overlap_values"))
    matched = _safe_int(row.get("matched_value_count"))
    supported = _safe_int(row.get("supported_event_count"))
    false_positive = _safe_int(row.get("false_positive_proxy_value_count"))
    if not false_positive and total:
        false_positive = max(0, total - matched)
    return {
        "active_state_days": active,
        "total_overlap_values": total,
        "avg_overlap_values_per_state_day": _safe_float(row.get("avg_overlap_values_per_state_day"), _rate(total, active)),
        "matched_value_count": matched,
        "matched_value_rate": _safe_float(row.get("matched_value_rate"), _rate(matched, total)),
        "supported_event_count": supported,
        "supported_event_rate": _safe_float(row.get("supported_event_rate")),
        "supported_events_per_100_state_days": 100.0 * _rate(supported, active),
        "false_positive_proxy_value_count": false_positive,
        "false_positive_proxy_rate": _safe_float(row.get("false_positive_proxy_rate"), _rate(false_positive, total)),
        "positive_conversion_event_count": _safe_int(row.get("positive_conversion_event_count")),
        "gap_teacher_event_count": _safe_int(row.get("gap_teacher_event_count")),
        "wrong_lane_event_count": _safe_int(row.get("wrong_lane_event_count")),
        "stage2b_stack_decision": str(row.get("stage2b_stack_decision") or ""),
    }


def _comparison_metrics(stack: Dict[str, Any], source_a: Dict[str, Any], source_b: Dict[str, Any]) -> Dict[str, Any]:
    a_per100 = _safe_float(source_a.get("source_a_source_supported_per_100_state_days"))
    b_per100 = _safe_float(source_b.get("source_b_source_supported_per_100_state_days"))
    overlap_per100 = _safe_float(stack.get("supported_events_per_100_state_days"))
    a_rate = _safe_float(source_a.get("source_a_source_lane_hit_value_rate"))
    b_rate = _safe_float(source_b.get("source_b_source_lane_hit_value_rate"))
    overlap_rate = _safe_float(stack.get("matched_value_rate"))
    a_pool = _safe_float(source_a.get("source_a_source_avg_pool_size"))
    b_pool = _safe_float(source_b.get("source_b_source_avg_pool_size"))
    overlap_pool = _safe_float(stack.get("avg_overlap_values_per_state_day"))
    best_pool = min([p for p in [a_pool, b_pool] if p > 0], default=0.0)
    return {
        "overlap_support_per100_vs_best_source": overlap_per100 - max(a_per100, b_per100),
        "overlap_lane_rate_vs_best_source": overlap_rate - max(a_rate, b_rate),
        "overlap_pool_reduction_vs_smaller_source": best_pool - overlap_pool if best_pool else 0.0,
    }


def _replay_decision(row: Dict[str, Any]) -> Tuple[str, str]:
    queue = str(row.get("queue") or "")
    lane = str(row.get("replay_lane") or row.get("lane") or "")
    windows = _safe_int(row.get("windows_confirmed"))
    active = _safe_int(row.get("active_state_days"))
    avg_pool = _safe_float(row.get("avg_overlap_values_per_state_day"))
    support_per100 = _safe_float(row.get("supported_events_per_100_state_days"))
    positive_per100 = _safe_float(row.get("positive_conversions_per_100_state_days"))
    wrong = _safe_int(row.get("wrong_lane_event_count"))
    positive = _safe_int(row.get("positive_conversion_event_count"))
    gap = _safe_int(row.get("gap_teacher_event_count"))
    fp_rate = _safe_float(row.get("false_positive_proxy_rate"))
    concentration = _safe_float(row.get("top_state_support_share"))
    lineage_risk = str(row.get("shared_lineage_risk") or "")
    mechanism = str(row.get("mechanism_family") or "")
    overlap_support_lift = _safe_float(row.get("overlap_support_per100_vs_best_source"))

    if queue == "P3_vtrac_decay_watch_replay" or lane == "vtrac":
        return "watch_decay_only", "VTRAC/territory evidence remains useful as carryforward context, not boxed spend permission."
    if "blackapple" in mechanism and fp_rate >= 0.995 and positive + gap == 0:
        return "demote_to_restraint", "Blackapple-related replay is broad/no-conversion in fixtures; preserve as restraint material."
    if windows < 2 or active == 0:
        return "needs_more_fixture_coverage", "Too few fixture windows or no active replay denominator."
    if concentration > 0.70 and positive + gap + _safe_int(row.get("supported_event_count")) > 0:
        return "blocked_by_state_concentration", "Replay support is too concentrated in one state to promote."
    if queue == "P1_boxed_translator_replay":
        if avg_pool <= 3.5 and support_per100 > 0 and wrong == 0 and windows >= 3:
            if lineage_risk == "high" and overlap_support_lift <= 0:
                return "survived_with_lineage_guardrail", "Bounded replay survives, but shared lineage means it cannot be counted as independent multi-source proof."
            return "survived_as_boxed_translator_candidate", "Bounded boxed replay survives fixture testing as a candidate for future translator design."
        if wrong > positive + gap:
            return "demote_to_wrong_lane_restraint", "Wrong-lane count exceeds positive/gap support."
        return "needs_replay_refinement", "P1 replay did not clear the bounded pool/support/wrong-lane checks cleanly."
    if queue == "P2_support_gate_replay":
        if support_per100 > 0 and wrong <= max(positive + gap, 1):
            return "survived_as_support_gate", "Replay supports support-gate use only; not standalone scoring."
        return "fixture_only_support_probe", "Keep as a support fixture until stronger conversion appears."
    if queue == "P4_low_denominator_fixture_replay":
        if positive > 0 and windows >= 3 and avg_pool <= 2.5:
            return "low_denominator_watchlist", "Low-denominator fixture has signal, but remains watchlist material."
        return "fixture_only_low_denominator", "Interesting but too thin for promotion."
    if queue == "P4_diagnostic_replay":
        return "diagnostic_fixture_only", "Diagnostic replay material; useful for explanation and regression tests."
    return "fixture_only", "No direct promotion permission from replay; preserve as fixture material."


def _aggregate_entity_rows(ledger_rows: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    grouped: Dict[Tuple[str, str], List[Dict[str, Any]]] = defaultdict(list)
    for row in ledger_rows:
        grouped[(str(row.get("entity_type") or ""), str(row.get("entity_key") or ""))].append(row)

    out: List[Dict[str, Any]] = []
    for (_entity_type, _entity_key), rows in grouped.items():
        first = rows[0]
        active = sum(_safe_int(row.get("active_state_days")) for row in rows)
        total = sum(_safe_int(row.get("total_overlap_values")) for row in rows)
        matched = sum(_safe_int(row.get("matched_value_count")) for row in rows)
        supported = sum(_safe_int(row.get("supported_event_count")) for row in rows)
        false_positive = sum(_safe_int(row.get("false_positive_proxy_value_count")) for row in rows)
        positive = sum(_safe_int(row.get("positive_conversion_event_count")) for row in rows)
        gap = sum(_safe_int(row.get("gap_teacher_event_count")) for row in rows)
        wrong = sum(_safe_int(row.get("wrong_lane_event_count")) for row in rows)
        source_a_supported = sum(_safe_int(row.get("source_a_source_supported_winner_event_count")) for row in rows)
        source_b_supported = sum(_safe_int(row.get("source_b_source_supported_winner_event_count")) for row in rows)
        source_a_active = sum(_safe_int(row.get("source_a_source_active_state_days")) for row in rows)
        source_b_active = sum(_safe_int(row.get("source_b_source_active_state_days")) for row in rows)
        top_state_counts = Counter()
        positive_state_counts = Counter()
        for row in rows:
            top_state = str(row.get("top_state_by_support") or "")
            if top_state:
                top_state_counts[top_state] += _safe_int(row.get("top_state_support_count"))
            top_positive = str(row.get("top_state_by_positive") or "")
            if top_positive:
                positive_state_counts[top_positive] += _safe_int(row.get("top_state_positive_count"))
        top_state, top_count, top_share, top3 = _top_share(top_state_counts)
        top_positive, top_positive_count, top_positive_share, top3_positive = _top_share(positive_state_counts)
        windows_confirmed = sum(1 for row in rows if _safe_int(row.get("active_state_days")) > 0 or _safe_int(row.get("source_active_state_days")) > 0)
        overlap_support_lift = sum(_safe_float(row.get("overlap_support_per100_vs_best_source")) for row in rows) / len(rows)
        overlap_lane_lift = sum(_safe_float(row.get("overlap_lane_rate_vs_best_source")) for row in rows) / len(rows)
        pool_reduction = sum(_safe_float(row.get("overlap_pool_reduction_vs_smaller_source")) for row in rows) / len(rows)
        aggregate = {
            "queue": first.get("queue"),
            "entity_type": first.get("entity_type"),
            "entity_key": first.get("entity_key"),
            "replay_lane": first.get("replay_lane"),
            "stage3_decision_role": first.get("stage3_decision_role"),
            "source_a": first.get("source_a"),
            "source_b": first.get("source_b"),
            "mechanism_family": first.get("mechanism_family"),
            "future_primitive": first.get("future_primitive"),
            "shared_lineage_risk": first.get("shared_lineage_risk"),
            "lineage_group": first.get("lineage_group"),
            "windows_confirmed": windows_confirmed,
            "windows_tested": len(rows),
            "active_state_days": active,
            "total_overlap_values": total,
            "avg_overlap_values_per_state_day": _rate(total, active),
            "matched_value_count": matched,
            "matched_value_rate": _rate(matched, total),
            "supported_event_count": supported,
            "supported_events_per_100_state_days": 100.0 * _rate(supported, active),
            "false_positive_proxy_value_count": false_positive,
            "false_positive_proxy_rate": _rate(false_positive, total),
            "positive_conversion_event_count": positive,
            "gap_teacher_event_count": gap,
            "wrong_lane_event_count": wrong,
            "positive_conversions_per_100_state_days": 100.0 * _rate(positive, active),
            "wrong_lane_free_conversions_per_100_state_days": 100.0 * _rate(max(0, positive - wrong), active),
            "pool_normalized_positive_yield": 100.0 * _rate(positive, total),
            "source_a_supported_per_100_state_days": 100.0 * _rate(source_a_supported, source_a_active),
            "source_b_supported_per_100_state_days": 100.0 * _rate(source_b_supported, source_b_active),
            "overlap_support_per100_vs_best_source": overlap_support_lift,
            "overlap_lane_rate_vs_best_source": overlap_lane_lift,
            "overlap_pool_reduction_vs_smaller_source": pool_reduction,
            "states_with_support_proxy": len(top_state_counts),
            "top_state_by_support": top_state,
            "top_state_support_count": top_count,
            "top_state_support_share": top_share,
            "top3_state_support_mix": top3,
            "top_state_by_positive": top_positive,
            "top_state_positive_count": top_positive_count,
            "top_state_positive_share": top_positive_share,
            "top3_state_positive_mix": top3_positive,
        }
        decision, rationale = _replay_decision(aggregate)
        aggregate["stage4_replay_decision"] = decision
        aggregate["stage4_rationale"] = rationale
        out.append(aggregate)
    return sorted(
        out,
        key=lambda row: (
            str(row.get("stage4_replay_decision") or ""),
            -_safe_int(row.get("windows_confirmed")),
            -_safe_float(row.get("positive_conversions_per_100_state_days")),
            str(row.get("entity_key") or ""),
        ),
    )


def _build_fixture_ledger(
    *,
    replay_rows: Sequence[Dict[str, str]],
    registry_by_key: Dict[Tuple[str, str], Dict[str, str]],
    windows: Sequence[Path],
    stack_by_window: Dict[str, Dict[str, Dict[str, Any]]],
    source_by_window: Dict[str, Dict[str, Dict[str, Any]]],
    ledger_aggs_by_window: Dict[str, Dict[str, Dict[str, Any]]],
) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for replay in replay_rows:
        entity_type = str(replay.get("entity_type") or "")
        entity_key = str(replay.get("entity_key") or "")
        registry = registry_by_key.get((entity_type, entity_key), {})
        queue = str(replay.get("queue") or "")
        lane = str(replay.get("replay_lane") or registry.get("lane") or "")
        pair_scope, parsed_a, parsed_b = _parse_pair_key(entity_key)
        source_a = str(registry.get("source_a") or parsed_a or (entity_key if entity_type == "source" else ""))
        source_b = str(registry.get("source_b") or parsed_b or "")
        if entity_type == "source" and not source_a:
            source_a = entity_key
        mechanism, primitive = _mechanism_family(entity_key, source_a, source_b, lane, queue)
        lineage_risk, lineage_group, lineage_note = _lineage_risk(source_a, source_b)
        for window in windows:
            window_name = window.name
            stack_row: Dict[str, Any] | None = None
            ledger_agg: Dict[str, Any] | None = None
            if entity_type == "stack":
                stack_row = stack_by_window.get(window_name, {}).get(entity_key)
                if not stack_row and pair_scope and source_a and source_b:
                    stack_row = stack_by_window.get(window_name, {}).get(_make_pair_key(pair_scope, source_a, source_b))
                    if not stack_row:
                        stack_row = stack_by_window.get(window_name, {}).get(_make_pair_key(pair_scope, source_b, source_a))
                ledger_agg = ledger_aggs_by_window.get(window_name, {}).get(entity_key)
                if not ledger_agg and pair_scope and source_a and source_b:
                    ledger_agg = ledger_aggs_by_window.get(window_name, {}).get(_make_pair_key(pair_scope, source_a, source_b))
                    if not ledger_agg:
                        ledger_agg = ledger_aggs_by_window.get(window_name, {}).get(_make_pair_key(pair_scope, source_b, source_a))
            source_a_row = source_by_window.get(window_name, {}).get(source_a) if source_a else None
            source_b_row = source_by_window.get(window_name, {}).get(source_b) if source_b else None

            stack = _stack_metrics(stack_row)
            source_a_metrics = _source_metrics(source_a_row, "source_a")
            source_b_metrics = _source_metrics(source_b_row, "source_b")
            comparison = _comparison_metrics(stack, source_a_metrics, source_b_metrics)

            support_counter: Counter[str] = Counter()
            positive_counter: Counter[str] = Counter()
            states_active = 0
            if ledger_agg:
                support_counter = ledger_agg["state_support_units"]
                positive_counter = ledger_agg["state_positive_units"]
                states_active = len(ledger_agg["ledger_states"])
            top_state, top_count, top_share, top3 = _top_share(support_counter)
            top_positive, top_positive_count, top_positive_share, top3_positive = _top_share(positive_counter)

            source_active = _safe_int(source_a_metrics.get("source_a_source_active_state_days"))
            if entity_type == "source":
                stack["active_state_days"] = source_active
                stack["total_overlap_values"] = _safe_int(source_a_metrics.get("source_a_source_total_exposure_values"))
                stack["avg_overlap_values_per_state_day"] = _safe_float(source_a_metrics.get("source_a_source_avg_pool_size"))
                stack["matched_value_count"] = _safe_int(source_a_metrics.get("source_a_source_lane_hit_value_count"))
                stack["matched_value_rate"] = _safe_float(source_a_metrics.get("source_a_source_lane_hit_value_rate"))
                stack["supported_event_count"] = _safe_int(source_a_metrics.get("source_a_source_supported_winner_event_count"))
                stack["supported_events_per_100_state_days"] = _safe_float(source_a_metrics.get("source_a_source_supported_per_100_state_days"))
                stack["false_positive_proxy_rate"] = _safe_float(source_a_metrics.get("source_a_source_false_positive_proxy_rate"))
                total_values = _safe_int(stack.get("total_overlap_values"))
                matched_values = _safe_int(stack.get("matched_value_count"))
                stack["false_positive_proxy_value_count"] = max(0, total_values - matched_values)

            row: Dict[str, Any] = {
                "queue_id": replay.get("queue_id"),
                "queue": queue,
                "window": window_name,
                "entity_type": entity_type,
                "entity_key": entity_key,
                "replay_lane": lane,
                "stage3_decision_role": registry.get("decision_role") or "",
                "stage3_evidence_strength": replay.get("evidence_strength") or registry.get("evidence_strength") or "",
                "stage3_allowed_use": registry.get("allowed_use") or "",
                "source_a": source_a,
                "source_b": source_b,
                "pair_scope": pair_scope,
                "mechanism_family": mechanism,
                "future_primitive": primitive,
                "shared_lineage_risk": lineage_risk,
                "lineage_group": lineage_group,
                "lineage_note": lineage_note,
                "states_active_in_pairing_ledger": states_active,
                "top_state_by_support": top_state,
                "top_state_support_count": top_count,
                "top_state_support_share": top_share,
                "top3_state_support_mix": top3,
                "top_state_by_positive": top_positive,
                "top_state_positive_count": top_positive_count,
                "top_state_positive_share": top_positive_share,
                "top3_state_positive_mix": top3_positive,
            }
            row.update(stack)
            row.update(source_a_metrics)
            row.update(source_b_metrics)
            row.update(comparison)
            out.append(row)
    return out


def _build_mechanism_scorecard(decision_rows: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    grouped: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for row in decision_rows:
        grouped[str(row.get("mechanism_family") or "unknown")].append(row)
    out: List[Dict[str, Any]] = []
    for family, rows in grouped.items():
        active = sum(_safe_int(row.get("active_state_days")) for row in rows)
        total = sum(_safe_int(row.get("total_overlap_values")) for row in rows)
        supported = sum(_safe_int(row.get("supported_event_count")) for row in rows)
        positive = sum(_safe_int(row.get("positive_conversion_event_count")) for row in rows)
        wrong = sum(_safe_int(row.get("wrong_lane_event_count")) for row in rows)
        decisions = Counter(str(row.get("stage4_replay_decision") or "") for row in rows)
        primitives = Counter(str(row.get("future_primitive") or "") for row in rows)
        out.append(
            {
                "mechanism_family": family,
                "entity_count": len(rows),
                "top_future_primitives": _counter_text(primitives),
                "stage4_decision_mix": _counter_text(decisions),
                "active_state_days": active,
                "total_overlap_values": total,
                "avg_pool_or_exposure_per_state_day": _rate(total, active),
                "supported_event_count": supported,
                "supported_events_per_100_state_days": 100.0 * _rate(supported, active),
                "positive_conversion_event_count": positive,
                "positive_conversions_per_100_state_days": 100.0 * _rate(positive, active),
                "wrong_lane_event_count": wrong,
                "recommended_next_use": _recommended_family_use(decisions, family),
            }
        )
    return sorted(out, key=lambda row: (-_safe_int(row.get("entity_count")), str(row.get("mechanism_family") or "")))


def _recommended_family_use(decisions: Counter[str], family: str) -> str:
    if decisions.get("survived_as_boxed_translator_candidate") or decisions.get("survived_with_lineage_guardrail"):
        return "candidate_family_for_future_translator_replay_review"
    if decisions.get("survived_as_support_gate"):
        return "support_gate_family_only"
    if "vtrac" in family or decisions.get("watch_decay_only"):
        return "decay_or_territory_watch_only"
    if decisions.get("demote_to_restraint") or decisions.get("demote_to_wrong_lane_restraint"):
        return "restraint_or_penalty_library"
    return "fixture_or_more_windows"


def _build_ab_comparison(decision_rows: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    rows = []
    for row in decision_rows:
        if str(row.get("entity_type") or "") != "stack":
            continue
        rows.append(
            {
                "entity_key": row.get("entity_key"),
                "queue": row.get("queue"),
                "mechanism_family": row.get("mechanism_family"),
                "future_primitive": row.get("future_primitive"),
                "source_a": row.get("source_a"),
                "source_b": row.get("source_b"),
                "shared_lineage_risk": row.get("shared_lineage_risk"),
                "lineage_group": row.get("lineage_group"),
                "windows_confirmed": row.get("windows_confirmed"),
                "overlap_supported_per_100_state_days": row.get("supported_events_per_100_state_days"),
                "source_a_supported_per_100_state_days": row.get("source_a_supported_per_100_state_days"),
                "source_b_supported_per_100_state_days": row.get("source_b_supported_per_100_state_days"),
                "overlap_support_per100_vs_best_source": row.get("overlap_support_per100_vs_best_source"),
                "overlap_lane_rate_vs_best_source": row.get("overlap_lane_rate_vs_best_source"),
                "overlap_pool_reduction_vs_smaller_source": row.get("overlap_pool_reduction_vs_smaller_source"),
                "stage4_replay_decision": row.get("stage4_replay_decision"),
                "stage4_rationale": row.get("stage4_rationale"),
            }
        )
    return sorted(rows, key=lambda row: (-_safe_float(row.get("overlap_support_per100_vs_best_source")), str(row.get("entity_key") or "")))


def _build_lineage_audit(decision_rows: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    out = []
    for row in decision_rows:
        out.append(
            {
                "entity_key": row.get("entity_key"),
                "queue": row.get("queue"),
                "mechanism_family": row.get("mechanism_family"),
                "source_a": row.get("source_a"),
                "source_b": row.get("source_b"),
                "shared_lineage_risk": row.get("shared_lineage_risk"),
                "lineage_group": row.get("lineage_group"),
                "overlap_support_per100_vs_best_source": row.get("overlap_support_per100_vs_best_source"),
                "stage4_replay_decision": row.get("stage4_replay_decision"),
                "lineage_interpretation": (
                    "Do not count as independent confirmation."
                    if row.get("shared_lineage_risk") == "high"
                    else "Use normally after A/B/overlap comparison."
                ),
            }
        )
    return sorted(out, key=lambda row: (str(row.get("shared_lineage_risk") or ""), str(row.get("entity_key") or "")))


def _build_negative_control_summary(negative_rows: Sequence[Dict[str, str]]) -> List[Dict[str, Any]]:
    grouped: Dict[Tuple[str, str], List[Dict[str, str]]] = defaultdict(list)
    for row in negative_rows:
        entity_key = str(row.get("entity_key") or "")
        lane = str(row.get("lane") or "")
        scope, source_a, source_b = _parse_pair_key(entity_key)
        mechanism, primitive = _mechanism_family(entity_key, source_a, source_b, lane, "negative_control")
        grouped[(mechanism, primitive)].append(row)
    out = []
    for (mechanism, primitive), rows in grouped.items():
        windows_seen = sum(_safe_int(row.get("windows_seen")) for row in rows)
        fp_rates = [_safe_float(row.get("false_positive_proxy_rate")) for row in rows]
        match_rates = [_safe_float(row.get("match_rate")) for row in rows]
        support_rates = [_safe_float(row.get("event_support_rate")) for row in rows]
        lanes = Counter(str(row.get("lane") or "") for row in rows)
        out.append(
            {
                "mechanism_family": mechanism,
                "future_primitive": primitive,
                "negative_control_count": len(rows),
                "lane_mix": _counter_text(lanes),
                "avg_windows_seen": _rate(windows_seen, len(rows)),
                "avg_false_positive_proxy_rate": sum(fp_rates) / len(fp_rates) if fp_rates else 0.0,
                "avg_match_rate": sum(match_rates) / len(match_rates) if match_rates else 0.0,
                "avg_event_support_rate": sum(support_rates) / len(support_rates) if support_rates else 0.0,
                "restraint_use": "candidate penalty/veto library; do not promote directly",
            }
        )
    return sorted(out, key=lambda row: (-_safe_int(row.get("negative_control_count")), str(row.get("mechanism_family") or "")))


def _build_markdown(
    *,
    runs2_dir: Path,
    windows: Sequence[Path],
    replay_rows: Sequence[Dict[str, str]],
    ledger_rows: Sequence[Dict[str, Any]],
    decision_rows: Sequence[Dict[str, Any]],
    mechanism_rows: Sequence[Dict[str, Any]],
    negative_rows: Sequence[Dict[str, Any]],
    paths: Dict[str, Path],
) -> str:
    decisions = Counter(str(row.get("stage4_replay_decision") or "") for row in decision_rows)
    queues = Counter(str(row.get("queue") or "") for row in decision_rows)
    families = Counter(str(row.get("mechanism_family") or "") for row in decision_rows)
    lineage = Counter(str(row.get("shared_lineage_risk") or "") for row in decision_rows)
    survived = [
        row
        for row in decision_rows
        if str(row.get("stage4_replay_decision") or "") in {"survived_as_boxed_translator_candidate", "survived_with_lineage_guardrail"}
    ]
    support = [row for row in decision_rows if str(row.get("stage4_replay_decision") or "") == "survived_as_support_gate"]
    restraint = [
        row
        for row in decision_rows
        if str(row.get("stage4_replay_decision") or "").startswith("demote")
        or str(row.get("stage4_replay_decision") or "") == "blocked_by_state_concentration"
    ]

    lines: List[str] = [
        "# Analysis Arena Stage 4 Fixture Replay Scorecard",
        "",
        "Purpose: replay the Stage-3 queue against completed fixture windows before any scoring, translator, candidate, or budget rewrite.",
        "",
        "## Metadata",
        f"- runs2_dir: `{safe_rel(runs2_dir)}`",
        f"- fixture_windows: `{len(windows)}`",
        f"- stage3_replay_rows: `{len(replay_rows)}`",
        f"- fixture_ledger_rows: `{len(ledger_rows)}`",
        f"- replay_decision_rows: `{len(decision_rows)}`",
        "",
        "## Guardrails",
        "- Stage 4 is read-only. It does not alter live scoring, candidate generation, budgeting, or legacy pipelines.",
        "- `survived_as_boxed_translator_candidate` means future translator-design evidence, not live-play permission.",
        "- VTRAC/territory rows remain watch/decay only unless bounded boxed or exact replay evidence survives.",
        "- Shared-lineage rows cannot be counted as independent multi-source proof.",
        "- Legacy method names are locators; `future_primitive` is the architecture-facing label.",
        "",
        "## Decision Counts",
        "",
    ]
    for key, count in decisions.most_common():
        lines.append(f"- `{key}`: `{count}`")
    lines += ["", "## Queue Counts", ""]
    for key, count in queues.most_common():
        lines.append(f"- `{key}`: `{count}`")
    lines += ["", "## Mechanism Families", ""]
    for key, count in families.most_common(12):
        lines.append(f"- `{key}`: `{count}`")
    lines += ["", "## Shared Lineage Risk", ""]
    for key, count in lineage.most_common():
        lines.append(f"- `{key}`: `{count}`")
    lines += [
        "",
        "## Top Boxed Translator Survivors",
        "",
        "| entity | primitive | windows | pool | positive/100 ASD | support/100 ASD | lineage | decision |",
        "|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in sorted(survived, key=lambda r: (-_safe_float(r.get("positive_conversions_per_100_state_days")), -_safe_int(r.get("windows_confirmed"))))[:15]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{row.get('entity_key')}`",
                    f"`{row.get('future_primitive')}`",
                    str(row.get("windows_confirmed")),
                    _fmt(row.get("avg_overlap_values_per_state_day")),
                    _fmt(row.get("positive_conversions_per_100_state_days")),
                    _fmt(row.get("supported_events_per_100_state_days")),
                    str(row.get("shared_lineage_risk")),
                    str(row.get("stage4_replay_decision")),
                ]
            )
            + " |"
        )
    lines += [
        "",
        "## Top Support Gates",
        "",
        "| entity | primitive | windows | support/100 ASD | wrong-lane | decision |",
        "|---|---:|---:|---:|---:|---|",
    ]
    for row in sorted(support, key=lambda r: (-_safe_float(r.get("supported_events_per_100_state_days")), str(r.get("entity_key") or "")))[:15]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{row.get('entity_key')}`",
                    f"`{row.get('future_primitive')}`",
                    str(row.get("windows_confirmed")),
                    _fmt(row.get("supported_events_per_100_state_days")),
                    str(row.get("wrong_lane_event_count")),
                    str(row.get("stage4_replay_decision")),
                ]
            )
            + " |"
        )
    lines += [
        "",
        "## Restraint / Blocked Examples",
        "",
        "| entity | primitive | reason | top-state share | fp rate |",
        "|---|---:|---|---:|---:|",
    ]
    for row in sorted(restraint, key=lambda r: (-_safe_float(r.get("false_positive_proxy_rate")), str(r.get("entity_key") or "")))[:12]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{row.get('entity_key')}`",
                    f"`{row.get('future_primitive')}`",
                    str(row.get("stage4_rationale")),
                    _pct(row.get("top_state_support_share")),
                    _pct(row.get("false_positive_proxy_rate")),
                ]
            )
            + " |"
        )
    lines += [
        "",
        "## Negative-Control Mechanism Summary",
        "",
        "| mechanism | primitive | controls | avg fp rate | use |",
        "|---|---:|---:|---:|---|",
    ]
    for row in negative_rows[:12]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{row.get('mechanism_family')}`",
                    f"`{row.get('future_primitive')}`",
                    str(row.get("negative_control_count")),
                    _pct(row.get("avg_false_positive_proxy_rate")),
                    str(row.get("restraint_use")),
                ]
            )
            + " |"
        )
    lines += [
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
    paths = _cycle_paths(output_dir)
    s3 = _stage3_paths(runs2_dir)

    replay_rows = _read_csv_rows(s3["replay_csv"])
    if int(args.max_replay_rows or 0) > 0:
        replay_rows = replay_rows[: int(args.max_replay_rows)]
    registry_rows = _read_csv_rows(s3["registry_csv"])
    negative_map_rows = _read_csv_rows(s3["negative_csv"])
    registry_by_key = {
        (str(row.get("entity_type") or ""), str(row.get("entity_key") or "")): row
        for row in registry_rows
    }
    windows = _discover_windows(runs2_dir)
    if not replay_rows:
        raise SystemExit(f"Missing or empty Stage-3 replay queue: {s3['replay_csv']}")
    if not windows:
        raise SystemExit(f"No fixture windows found under {runs2_dir}")

    stack_by_window = _load_stack_scorecards(windows)
    source_by_window = _load_source_scorecards(windows)
    ledger_aggs_by_window = _load_pairing_ledger_aggs(windows)
    fixture_ledger = _build_fixture_ledger(
        replay_rows=replay_rows,
        registry_by_key=registry_by_key,
        windows=windows,
        stack_by_window=stack_by_window,
        source_by_window=source_by_window,
        ledger_aggs_by_window=ledger_aggs_by_window,
    )
    decision_rows = _aggregate_entity_rows(fixture_ledger)
    mechanism_rows = _build_mechanism_scorecard(decision_rows)
    ab_rows = _build_ab_comparison(decision_rows)
    yield_rows = sorted(
        decision_rows,
        key=lambda row: (
            -_safe_float(row.get("positive_conversions_per_100_state_days")),
            -_safe_float(row.get("supported_events_per_100_state_days")),
            str(row.get("entity_key") or ""),
        ),
    )
    lineage_rows = _build_lineage_audit(decision_rows)
    negative_summary = _build_negative_control_summary(negative_map_rows)

    _write_csv(paths["ledger_csv"], fixture_ledger, force=bool(args.force))
    _write_csv(paths["decision_csv"], decision_rows, force=bool(args.force))
    _write_csv(paths["mechanism_csv"], mechanism_rows, force=bool(args.force))
    _write_csv(paths["ab_csv"], ab_rows, force=bool(args.force))
    _write_csv(paths["yield_csv"], yield_rows, force=bool(args.force))
    _write_csv(paths["lineage_csv"], lineage_rows, force=bool(args.force))
    _write_csv(paths["negative_csv"], negative_summary, force=bool(args.force))

    payload = {
        "metadata": {
            "runs2_dir": safe_rel(runs2_dir),
            "output_dir": safe_rel(output_dir),
            "fixture_windows": [window.name for window in windows],
            "stage3_replay_rows": len(replay_rows),
            "fixture_ledger_rows": len(fixture_ledger),
            "replay_decision_rows": len(decision_rows),
            "guardrail": "read_only_fixture_replay_no_live_scoring_changes",
        },
        "decision_counts": Counter(str(row.get("stage4_replay_decision") or "") for row in decision_rows),
        "queue_counts": Counter(str(row.get("queue") or "") for row in decision_rows),
        "mechanism_family_counts": Counter(str(row.get("mechanism_family") or "") for row in decision_rows),
        "shared_lineage_risk_counts": Counter(str(row.get("shared_lineage_risk") or "") for row in decision_rows),
        "top_mechanism_rows": mechanism_rows[:30],
        "outputs": {label: safe_rel(path) for label, path in paths.items()},
    }
    _write_json(paths["json"], payload, force=bool(args.force))
    _write_text(
        paths["md"],
        _build_markdown(
            runs2_dir=runs2_dir,
            windows=windows,
            replay_rows=replay_rows,
            ledger_rows=fixture_ledger,
            decision_rows=decision_rows,
            mechanism_rows=mechanism_rows,
            negative_rows=negative_summary,
            paths=paths,
        ),
        force=bool(args.force),
    )

    print(f"[OK] Wrote Stage-4 fixture replay scorecard: {safe_rel(paths['md'])}")
    print(f"[OK] Wrote replay ledger rows: {len(fixture_ledger)}")
    print(f"[OK] Wrote replay decision rows: {len(decision_rows)}")


if __name__ == "__main__":
    main()
