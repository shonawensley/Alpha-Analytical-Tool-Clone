#!/usr/bin/env python3
"""Create Stage-2B stack, fixture, and translator-hypothesis reports.

Stage 2 produced exposure denominators for individual signals. Stage 2B asks
which signals become more useful when they agree, and which examples should
become translator fixtures without rewriting live scoring yet.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence, Tuple


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.tools.analysis_arena_window_utils import safe_rel  # type: ignore


FINAL_DOCS_DIR = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "final docs"
RUNS_2_DIR = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS_2"


def _parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--window-root", required=True, help="RUNS_2 window root.")
    ap.add_argument("--runs2-dir", default=str(RUNS_2_DIR), help="Directory containing RUNS_2 windows.")
    ap.add_argument("--final-docs-dir", default=str(FINAL_DOCS_DIR), help="Final docs directory.")
    ap.add_argument("--force", action="store_true", help="Overwrite existing outputs.")
    return ap.parse_args()


def _resolve_path(value: str | Path) -> Path:
    path = Path(value).expanduser()
    if not path.is_absolute():
        path = (REPO_ROOT / path).resolve()
    return path


def _read_csv_rows(path: Path) -> List[Dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", errors="replace", newline="") as fh:
        return [{k: (v or "") for k, v in row.items()} for row in csv.DictReader(fh)]


def _read_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8", errors="replace"))


def _write_text(path: Path, text: str, *, force: bool) -> None:
    if path.exists() and not force:
        raise SystemExit(f"Refusing to overwrite existing file without --force: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _write_json(path: Path, payload: Any, *, force: bool) -> None:
    _write_text(path, json.dumps(payload, indent=2, sort_keys=True) + "\n", force=force)


def _write_csv(path: Path, rows: Sequence[Dict[str, Any]], *, force: bool) -> None:
    if path.exists() and not force:
        raise SystemExit(f"Refusing to overwrite existing file without --force: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames: List[str] = []
    for row in rows:
        for key in row:
            if key not in fieldnames:
                fieldnames.append(key)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def _default_paths(window_root: Path) -> Dict[str, Path]:
    stem = window_root.name
    prefix = f"{stem}__ANALYSIS_ARENA"
    return {
        "util": window_root / f"{prefix}__EVIDENCE_UTILIZATION_LEDGER.csv",
        "attribution": window_root / f"{prefix}__WINNER_SIGNAL_ATTRIBUTION_LEDGER.csv",
        "priority_cases": window_root / f"{prefix}__AUDIT_INTERPRETATION_PRIORITY_CASES.csv",
        "stage2_exposure": window_root / f"{prefix}__STAGE2_SIGNAL_EXPOSURE_LEDGER.csv",
        "stage2_scorecard": window_root / f"{prefix}__STAGE2_SIGNAL_FALSE_POSITIVE_SCORECARD.json",
        "stage2_decisions": window_root / f"{prefix}__STAGE2_SIGNAL_PROMOTION_DECISION_MATRIX.csv",
        "stage2_fixtures": window_root / f"{prefix}__STAGE2_TRANSLATOR_FIXTURE_CANDIDATES.csv",
        "executive_md": window_root / f"{prefix}__STAGE2_EXECUTIVE_READOUT.md",
        "source_family_csv": window_root / f"{prefix}__STAGE2_SOURCE_FAMILY_RANKING.csv",
        "risk_csv": window_root / f"{prefix}__STAGE2_DENOMINATOR_RISK_MAP.csv",
        "pair_ledger_csv": window_root / f"{prefix}__STAGE2B_SIGNAL_PAIRING_LEDGER.csv",
        "stack_md": window_root / f"{prefix}__STAGE2B_SIGNAL_STACK_SCORECARD.md",
        "stack_json": window_root / f"{prefix}__STAGE2B_SIGNAL_STACK_SCORECARD.json",
        "promotion_csv": window_root / f"{prefix}__STAGE2B_PROMOTION_CANDIDATES.csv",
        "negative_csv": window_root / f"{prefix}__STAGE2B_NEGATIVE_CONTROL_STACKS.csv",
        "fixture_md": window_root / f"{prefix}__TRANSLATOR_FIXTURE_DEEP_REVIEW.md",
        "gap_stacks_csv": window_root / f"{prefix}__GAP_TEACHER_STACKS.csv",
        "wrong_lane_md": window_root / f"{prefix}__WRONG_LANE_RESTRAINT_RULES.md",
        "positive_csv": window_root / f"{prefix}__POSITIVE_CONVERSION_REGRESSION_SET.csv",
        "decay_csv": window_root / f"{prefix}__DECAY_CARRYFORWARD_TEACHING_SET.csv",
        "hypothesis_md": window_root / f"{prefix}__TRANSLATOR_RULE_HYPOTHESIS_QUEUE.md",
        "hypothesis_csv": window_root / f"{prefix}__TRANSLATOR_RULE_HYPOTHESIS_QUEUE.csv",
        "readiness_md": window_root / f"{prefix}__STAGE2_CROSS_WINDOW_READINESS.md",
        "work_log_md": window_root / f"{prefix}__STAGE2B_OVERNIGHT_WORK_LOG.md",
    }


def _truthy(value: Any) -> bool:
    return str(value or "").strip().lower() in {"1", "true", "yes", "y"}


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


def _pct(value: float) -> str:
    return f"{100.0 * value:.1f}%"


def _rate(count: int | float, total: int | float) -> float:
    return float(count) / float(total) if total else 0.0


def _split_ids(value: Any) -> List[str]:
    raw = str(value or "").strip()
    if not raw:
        return []
    if ";" in raw:
        return [part for part in raw.split(";") if part]
    return [raw]


def _join_ids(values: Iterable[Any]) -> str:
    out: List[str] = []
    seen: set[str] = set()
    for value in values:
        text = str(value or "").strip()
        if text and text not in seen:
            seen.add(text)
            out.append(text)
    return ";".join(out)


def _digits_only(value: Any) -> str:
    return "".join(ch for ch in str(value or "") if ch.isdigit())


def _canon(value: Any) -> str:
    digits = _digits_only(value)
    if not digits:
        return ""
    digits = digits.zfill(3) if len(digits) <= 3 else digits
    return "".join(sorted(digits)) if len(digits) == 3 else ""


def _vtrac_index(value: Any) -> str:
    text = str(value or "").strip()
    if text.isdigit() and 1 <= int(text) <= 35 and len(text) <= 2:
        return str(int(text))
    digits = _digits_only(text)
    if len(digits) != 3:
        return ""
    try:
        import modules.vtrac_reference as vr  # type: ignore

        idx = vr.get_vtrac_index(digits)
        return str(idx) if isinstance(idx, int) else ""
    except Exception:
        return ""


def _event_id(row: Dict[str, Any]) -> str:
    return str(row.get("event_id") or f"{row.get('date')}|{row.get('state_key')}|{row.get('period')}|{row.get('winner')}")


def _source_family(source_key: str) -> str:
    return source_key.split(":", 1)[0] if ":" in source_key else source_key


def _source_tool(source_key: str) -> str:
    return source_key.split(":", 1)[1] if ":" in source_key else ""


def _source_score_lookup(score_rows: Sequence[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    return {str(row.get("source_key") or ""): row for row in score_rows}


def _risk_label(row: Dict[str, Any]) -> Tuple[str, str]:
    decision = str(row.get("stage2_decision") or "")
    lane = str(row.get("target_lane") or "")
    false_rate = _safe_float(row.get("false_positive_proxy_rate"))
    avg_pool = _safe_float(row.get("avg_pool_size"))
    lift = _safe_float(row.get("rough_lift_vs_naive"))
    active = _safe_int(row.get("active_state_days"))
    if decision == "sample_too_small" or active < 10:
        return "SAMPLE_TOO_SMALL", "Needs more windows before use."
    if decision.startswith("denominator") or avg_pool >= 50:
        return "BROAD_DENOMINATOR_CONTROL", "Too broad for direct promotion; useful as a control surface."
    if false_rate >= 0.98 and lift < 1.0:
        return "HIGH_FALSE_PROXY", "Fires often without same-day winner support in this window."
    if lane == "vtrac":
        return "VTRAC_WATCH", "Territory signal; needs boxed/exact pairing."
    if "supporting_gate" in decision:
        return "SUPPORT_GATE_CANDIDATE", "Potential gate, not standalone scorer."
    if "context" in decision:
        return "CONTEXT_OR_NEGATIVE_CONTROL", "Keep context-only unless paired."
    return "REVIEW", "Needs manual interpretation."


def _source_family_ranking(score_rows: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    buckets: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for row in score_rows:
        buckets[str(row.get("source_family") or _source_family(str(row.get("source_key") or "")))].append(row)
    out: List[Dict[str, Any]] = []
    for family, rows in buckets.items():
        exposures = sum(_safe_int(row.get("total_exposure_values")) for row in rows)
        lane_hits = sum(_safe_int(row.get("lane_hit_value_count")) for row in rows)
        supported = sum(_safe_int(row.get("supported_winner_event_count")) for row in rows)
        active_days = [max(0, _safe_int(row.get("active_state_days"))) for row in rows]
        avg_pool = sum(_safe_float(row.get("avg_pool_size")) for row in rows) / len(rows)
        decisions = Counter(str(row.get("stage2_decision") or "") for row in rows)
        out.append(
            {
                "source_family": family,
                "source_count": len(rows),
                "total_exposure_values": exposures,
                "lane_hit_value_count": lane_hits,
                "lane_hit_value_rate": _rate(lane_hits, exposures),
                "supported_winner_event_count_sum": supported,
                "avg_active_state_days": sum(active_days) / len(active_days) if active_days else 0.0,
                "avg_pool_size": avg_pool,
                "top_decisions": "|".join(f"{k}:{v}" for k, v in decisions.most_common()),
                "read": _family_read(family, decisions),
            }
        )
    out.sort(key=lambda row: (-_safe_float(row["lane_hit_value_rate"]), -_safe_int(row["total_exposure_values"]), row["source_family"]))
    return out


def _family_read(family: str, decisions: Counter[str]) -> str:
    if family == "translation_sandbox":
        return "Core translator teaching surface; strongest as paired boxed/VTRAC evidence."
    if family == "brain1":
        return "Arena evidence surface; useful but should be paired before spend decisions."
    if family == "board_scoreboard":
        return "Brain2 board surface; useful diagnostic, but rank-static behavior remains a guardrail."
    if family == "old_candidate_universe":
        return "Control-arm denominator and pack-family teaching surface; avoid direct trust in broad union exposure."
    if family == "old_play_card":
        return "Current downstream expression baseline; useful for old-vs-new translator lessons."
    if family in {"positional", "blackapple", "profit_alerts", "due_doubles"}:
        return "Support/context surface; test as a paired gate, not standalone promotion."
    return "Context surface; review through denominator and fixture behavior."


def _denominator_risk_map(score_rows: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for row in score_rows:
        risk, rationale = _risk_label(row)
        out.append(
            {
                "source_key": row.get("source_key", ""),
                "source_family": row.get("source_family", _source_family(str(row.get("source_key") or ""))),
                "target_lane": row.get("target_lane", ""),
                "active_state_days": row.get("active_state_days", ""),
                "avg_pool_size": row.get("avg_pool_size", ""),
                "total_exposure_values": row.get("total_exposure_values", ""),
                "lane_hit_value_rate": row.get("lane_hit_value_rate", ""),
                "winner_event_support_rate": row.get("winner_event_support_rate", ""),
                "false_positive_proxy_rate": row.get("false_positive_proxy_rate", ""),
                "rough_lift_vs_naive": row.get("rough_lift_vs_naive", ""),
                "stage2_decision": row.get("stage2_decision", ""),
                "risk_label": risk,
                "risk_rationale": rationale,
            }
        )
    out.sort(key=lambda row: (row["risk_label"], -_safe_float(row["false_positive_proxy_rate"]), -_safe_float(row["avg_pool_size"])))
    return out


def _scope_entries(row: Dict[str, str]) -> List[Tuple[str, str, List[str]]]:
    value = str(row.get("signal_value") or "").strip()
    kind = str(row.get("signal_value_kind") or "").strip()
    target_lane = str(row.get("target_lane") or "").strip()
    event_ids = _split_ids(row.get("matched_event_ids"))
    entries: List[Tuple[str, str, List[str]]] = []

    if kind == "literal":
        digits = _digits_only(value)
        if len(digits) == 3:
            if _safe_int(row.get("exact_event_count")) > 0:
                entries.append(("exact", digits, event_ids))
            else:
                entries.append(("exact", digits, []))
            canon = _canon(digits)
            if canon:
                entries.append(("box", canon, event_ids if _safe_int(row.get("box_event_count")) > 0 or _safe_int(row.get("exact_event_count")) > 0 else []))
            idx = _vtrac_index(digits)
            if idx:
                entries.append(("vtrac", idx, event_ids if _safe_int(row.get("vtrac_event_count")) > 0 else []))
    elif kind == "canonical":
        canon = _canon(value) if len(_digits_only(value)) == 3 else _digits_only(value)
        if canon:
            entries.append(("box", canon, event_ids if _safe_int(row.get("box_event_count")) > 0 or _safe_int(row.get("exact_event_count")) > 0 else []))
            idx = _vtrac_index(canon)
            if idx:
                entries.append(("vtrac", idx, event_ids if _safe_int(row.get("vtrac_event_count")) > 0 else []))
    elif kind == "vtrac_index" or target_lane == "vtrac":
        idx = _vtrac_index(value)
        if idx:
            entries.append(("vtrac", idx, event_ids if _safe_int(row.get("vtrac_event_count")) > 0 else []))
    return entries


def _build_pairing_ledger(
    exposure_rows: Sequence[Dict[str, str]],
    score_rows: Sequence[Dict[str, Any]],
    event_lookup: Dict[str, Dict[str, str]],
) -> List[Dict[str, Any]]:
    score_by_source = _source_score_lookup(score_rows)
    eligible = {
        source
        for source, score in score_by_source.items()
        if str(score.get("stage2_decision") or "") != "sample_too_small"
    }
    state_day_sources: Dict[str, Dict[str, Dict[str, Dict[str, set[str]]]]] = defaultdict(lambda: defaultdict(lambda: defaultdict(dict)))
    state_day_meta: Dict[str, Tuple[str, str]] = {}
    source_lanes: Dict[str, str] = {}
    source_decisions: Dict[str, str] = {}

    for row in exposure_rows:
        source = str(row.get("source_key") or "")
        if source not in eligible:
            continue
        if str(row.get("stage2_decision") or "") == "sample_too_small":
            continue
        state_day = str(row.get("state_day_key") or "")
        if not state_day:
            continue
        state_day_meta[state_day] = (str(row.get("date") or ""), str(row.get("state_key") or ""))
        source_lanes[source] = str(row.get("target_lane") or "")
        source_decisions[source] = str(score_by_source.get(source, {}).get("stage2_decision") or "")
        for scope, key, event_ids in _scope_entries(row):
            if scope == "vtrac" and source_lanes[source] != "vtrac":
                # VTRAC stacks are only useful here when at least one side is an actual VTRAC source.
                pass
            bucket = state_day_sources[state_day][source][scope]
            bucket.setdefault(key, set()).update(event_ids)

    ledger: List[Dict[str, Any]] = []
    for state_day, by_source in state_day_sources.items():
        sources = sorted(by_source)
        date, state_key = state_day_meta.get(state_day, ("", ""))
        for i, source_a in enumerate(sources):
            for source_b in sources[i + 1 :]:
                scopes = sorted(set(by_source[source_a]) & set(by_source[source_b]))
                for scope in scopes:
                    if scope == "vtrac" and source_lanes.get(source_a) != "vtrac" and source_lanes.get(source_b) != "vtrac":
                        continue
                    values_a = by_source[source_a][scope]
                    values_b = by_source[source_b][scope]
                    overlap = sorted(set(values_a) & set(values_b))
                    if not overlap:
                        continue
                    matched_values: List[str] = []
                    matched_events: set[str] = set()
                    for value in overlap:
                        event_ids = set(values_a.get(value, set())) | set(values_b.get(value, set()))
                        if event_ids:
                            matched_values.append(value)
                            matched_events.update(event_ids)
                    lanes = {source_lanes.get(source_a, ""), source_lanes.get(source_b, "")}
                    if scope == "vtrac" and "vtrac" in lanes and len(lanes) > 1:
                        pair_scope = "vtrac_box_confirmation"
                    else:
                        pair_scope = f"{scope}_overlap"
                    outcome_counts = Counter(str(event_lookup.get(event_id, {}).get("outcome_class") or "") for event_id in matched_events)
                    status_counts = Counter(str(event_lookup.get(event_id, {}).get("evidence_status") or "") for event_id in matched_events)
                    ledger.append(
                        {
                            "date": date,
                            "state_key": state_key,
                            "state_day_key": state_day,
                            "pair_scope": pair_scope,
                            "source_a": source_a,
                            "source_b": source_b,
                            "source_a_lane": source_lanes.get(source_a, ""),
                            "source_b_lane": source_lanes.get(source_b, ""),
                            "source_a_decision": source_decisions.get(source_a, ""),
                            "source_b_decision": source_decisions.get(source_b, ""),
                            "overlap_value_count": len(overlap),
                            "matched_value_count": len(matched_values),
                            "false_positive_proxy_value_count": len(overlap) - len(matched_values),
                            "matched_event_count": len(matched_events),
                            "matched_event_ids": _join_ids(sorted(matched_events)),
                            "matched_values_sample": "|".join(matched_values[:20]),
                            "overlap_values_sample": "|".join(overlap[:20]),
                            "gap_teacher_event_count": outcome_counts.get("BOX_GAP", 0) + outcome_counts.get("EXACT_GAP", 0),
                            "positive_conversion_event_count": outcome_counts.get("STRAIGHT", 0) + outcome_counts.get("STRICT_BOX", 0) + outcome_counts.get("BOX_ANY", 0),
                            "wrong_lane_event_count": status_counts.get("CAPTURED_BUT_WRONG_LANE", 0),
                            "outcome_mix": "|".join(f"{k}:{v}" for k, v in outcome_counts.most_common() if k),
                            "status_mix": "|".join(f"{k}:{v}" for k, v in status_counts.most_common() if k),
                        }
                    )
    ledger.sort(
        key=lambda row: (
            -_safe_int(row.get("matched_event_count")),
            -_safe_int(row.get("matched_value_count")),
            _safe_int(row.get("overlap_value_count")),
            row.get("pair_scope", ""),
            row.get("source_a", ""),
            row.get("source_b", ""),
        )
    )
    return ledger


def _stack_decision(row: Dict[str, Any]) -> Tuple[str, str]:
    active = _safe_int(row.get("active_state_days"))
    avg_pool = _safe_float(row.get("avg_overlap_values_per_state_day"))
    hit_rate = _safe_float(row.get("matched_value_rate"))
    event_support = _safe_float(row.get("supported_event_rate"))
    pair_scope = str(row.get("pair_scope") or "")
    false_rate = _safe_float(row.get("false_positive_proxy_rate"))
    if active < 10:
        return "sample_too_small_stack", "Needs more window coverage before promotion."
    if avg_pool >= 50 or false_rate >= 0.995:
        return "negative_control_stack", "Overlap remains too broad or too rarely resolves."
    if pair_scope == "vtrac_box_confirmation":
        if event_support >= 0.18 or hit_rate >= 0.06:
            return "vtrac_box_confirmation_watch", "Promising territory-plus-box pairing, but still watch/decay until stricter box rule is proven."
        return "vtrac_context_stack", "VTRAC pairing did not clear watch threshold."
    if pair_scope == "box_overlap":
        if hit_rate >= 0.012 and avg_pool <= 12 and active >= 30:
            return "boxed_translator_stack_candidate", "Box overlap is bounded enough to become a translator experiment candidate."
        if hit_rate >= 0.006:
            return "boxed_support_stack", "Useful as a supporting gate, not a standalone promotion."
    if pair_scope == "exact_overlap":
        if hit_rate >= 0.003 and avg_pool <= 20 and active >= 30:
            return "straight_stack_probe", "Straight overlap is rare; treat as strict-lane probe only."
        return "straight_context_stack", "Straight overlap does not yet justify promotion."
    return "context_stack", "Keep as context until more evidence accumulates."


def _pair_scorecard(pair_ledger: Sequence[Dict[str, Any]], event_lookup: Dict[str, Dict[str, str]]) -> List[Dict[str, Any]]:
    grouped: Dict[Tuple[str, str, str], List[Dict[str, Any]]] = defaultdict(list)
    for row in pair_ledger:
        a, b = sorted([str(row.get("source_a") or ""), str(row.get("source_b") or "")])
        grouped[(str(row.get("pair_scope") or ""), a, b)].append(row)
    out: List[Dict[str, Any]] = []
    total_event_count = len(event_lookup)
    for (scope, source_a, source_b), rows in grouped.items():
        active_days = {str(row.get("state_day_key") or "") for row in rows}
        overlap_values = sum(_safe_int(row.get("overlap_value_count")) for row in rows)
        matched_values = sum(_safe_int(row.get("matched_value_count")) for row in rows)
        matched_events = {
            event_id
            for row in rows
            for event_id in _split_ids(row.get("matched_event_ids"))
        }
        outcome_counts = Counter(str(event_lookup.get(event_id, {}).get("outcome_class") or "") for event_id in matched_events)
        status_counts = Counter(str(event_lookup.get(event_id, {}).get("evidence_status") or "") for event_id in matched_events)
        payload = {
            "pair_key": f"{scope}::{source_a} + {source_b}",
            "pair_scope": scope,
            "source_a": source_a,
            "source_b": source_b,
            "active_state_days": len(active_days),
            "total_overlap_values": overlap_values,
            "matched_value_count": matched_values,
            "matched_value_rate": _rate(matched_values, overlap_values),
            "false_positive_proxy_value_count": overlap_values - matched_values,
            "false_positive_proxy_rate": _rate(overlap_values - matched_values, overlap_values),
            "supported_event_count": len(matched_events),
            "supported_event_rate": _rate(len(matched_events), total_event_count),
            "avg_overlap_values_per_state_day": _rate(overlap_values, len(active_days)),
            "gap_teacher_event_count": outcome_counts.get("BOX_GAP", 0) + outcome_counts.get("EXACT_GAP", 0),
            "positive_conversion_event_count": outcome_counts.get("STRAIGHT", 0) + outcome_counts.get("STRICT_BOX", 0) + outcome_counts.get("BOX_ANY", 0),
            "wrong_lane_event_count": status_counts.get("CAPTURED_BUT_WRONG_LANE", 0),
            "outcome_mix": "|".join(f"{k}:{v}" for k, v in outcome_counts.most_common() if k),
            "status_mix": "|".join(f"{k}:{v}" for k, v in status_counts.most_common() if k),
        }
        decision, rationale = _stack_decision(payload)
        payload["stage2b_stack_decision"] = decision
        payload["decision_rationale"] = rationale
        out.append(payload)
    out.sort(
        key=lambda row: (
            row["stage2b_stack_decision"].startswith("negative"),
            -_safe_float(row.get("supported_event_rate")),
            -_safe_float(row.get("matched_value_rate")),
            _safe_float(row.get("avg_overlap_values_per_state_day")),
            row.get("pair_key", ""),
        )
    )
    return out


def _pair_ledger_drilldown(pair_ledger: Sequence[Dict[str, Any]], *, negative_limit: int = 5000) -> List[Dict[str, Any]]:
    matched: List[Dict[str, Any]] = []
    negative: List[Dict[str, Any]] = []
    for row in pair_ledger:
        if _safe_int(row.get("matched_event_count")) > 0:
            out = dict(row)
            out["ledger_role"] = "matched_drilldown"
            matched.append(out)
        else:
            out = dict(row)
            out["ledger_role"] = "negative_control_sample"
            negative.append(out)
    negative.sort(
        key=lambda row: (
            -_safe_int(row.get("overlap_value_count")),
            row.get("pair_scope", ""),
            row.get("source_a", ""),
            row.get("source_b", ""),
        )
    )
    return matched + negative[:negative_limit]


def _gap_teacher_stacks(priority_rows: Sequence[Dict[str, str]], pair_ledger: Sequence[Dict[str, Any]], stack_rows: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    stack_by_key = {str(row.get("pair_key") or ""): row for row in stack_rows}
    event_pairs: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for row in pair_ledger:
        for event_id in _split_ids(row.get("matched_event_ids")):
            event_pairs[event_id].append(row)
    out: List[Dict[str, Any]] = []
    for case in priority_rows:
        if str(case.get("outcome_class") or "") not in {"BOX_GAP", "EXACT_GAP"}:
            continue
        event_id = _event_id(case)
        rows = event_pairs.get(event_id, [])
        rows.sort(key=lambda row: (-_safe_int(row.get("matched_value_count")), _safe_int(row.get("overlap_value_count"))))
        for row in rows[:12]:
            source_a, source_b = sorted([str(row.get("source_a") or ""), str(row.get("source_b") or "")])
            pair_key = f"{row.get('pair_scope')}::{source_a} + {source_b}"
            stack = stack_by_key.get(pair_key, {})
            out.append(
                {
                    "event_id": event_id,
                    "date": case.get("date", ""),
                    "state_key": case.get("state_key", ""),
                    "period": case.get("period", ""),
                    "winner": case.get("winner", ""),
                    "outcome_class": case.get("outcome_class", ""),
                    "pair_scope": row.get("pair_scope", ""),
                    "source_a": row.get("source_a", ""),
                    "source_b": row.get("source_b", ""),
                    "overlap_value_count": row.get("overlap_value_count", ""),
                    "matched_value_count": row.get("matched_value_count", ""),
                    "matched_values_sample": row.get("matched_values_sample", ""),
                    "stack_decision": stack.get("stage2b_stack_decision", ""),
                    "stack_supported_event_rate": stack.get("supported_event_rate", ""),
                    "stack_matched_value_rate": stack.get("matched_value_rate", ""),
                    "lesson": "Gap teacher: Arena/source evidence overlapped but old final expression did not fully convert.",
                }
            )
    return out


def _positive_regression_rows(util_rows: Sequence[Dict[str, str]], pair_ledger: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    event_pair_counts: Dict[str, Counter[str]] = defaultdict(Counter)
    for row in pair_ledger:
        pair = f"{row.get('pair_scope')}::{row.get('source_a')}+{row.get('source_b')}"
        for event_id in _split_ids(row.get("matched_event_ids")):
            event_pair_counts[event_id][pair] += 1
    out: List[Dict[str, Any]] = []
    for row in util_rows:
        if str(row.get("evidence_status") or "") != "CAPTURED_AND_USED":
            continue
        event_id = _event_id(row)
        out.append(
            {
                "event_id": event_id,
                "date": row.get("date", ""),
                "state_key": row.get("state_key", ""),
                "period": row.get("period", ""),
                "winner": row.get("winner", ""),
                "outcome_class": row.get("outcome_class", ""),
                "board_rank": row.get("board_rank", ""),
                "sharp_signal_count": row.get("sharp_signal_count", ""),
                "territory_signal_count": row.get("territory_signal_count", ""),
                "top_stack_pairs": "|".join(pair for pair, _ in event_pair_counts.get(event_id, Counter()).most_common(8)),
                "regression_use": "Positive conversion anchor for future translator changes.",
            }
        )
    return out


def _decay_rows(util_rows: Sequence[Dict[str, str]]) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for row in util_rows:
        if str(row.get("evidence_status") or "") != "DECAY_VALIDATED":
            continue
        out.append(
            {
                "event_id": _event_id(row),
                "date": row.get("date", ""),
                "state_key": row.get("state_key", ""),
                "period": row.get("period", ""),
                "winner": row.get("winner", ""),
                "outcome_class": row.get("outcome_class", ""),
                "decay_any_profile": row.get("decay_any_profile", ""),
                "active_decay_metric_count": row.get("active_decay_metric_count", ""),
                "active_decay_metrics": row.get("active_decay_metrics", ""),
                "carryforward_use": "Keep as watch/carryforward teaching fixture; do not flatten into same-day miss.",
            }
        )
    return out


def _hypothesis_rows(stack_rows: Sequence[Dict[str, Any]], source_rows: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    source_candidates = [
        row
        for row in source_rows
        if str(row.get("stage2_decision") or "") in {"boxed_supporting_gate", "vtrac_watch_decay_only_until_box_pairing"}
    ]
    rows: List[Dict[str, Any]] = []
    idx = 1
    decision_order = [
        "boxed_translator_stack_candidate",
        "boxed_support_stack",
        "straight_stack_probe",
        "vtrac_box_confirmation_watch",
        "negative_control_stack",
    ]
    selected_stacks: List[Dict[str, Any]] = []
    for decision_name in decision_order:
        scoped = [row for row in stack_rows if str(row.get("stage2b_stack_decision") or "") == decision_name]
        scoped.sort(
            key=lambda row: (
                -_safe_float(row.get("matched_value_rate")),
                -_safe_float(row.get("supported_event_rate")),
                _safe_float(row.get("avg_overlap_values_per_state_day")),
                row.get("pair_key", ""),
            )
        )
        limit = 35 if decision_name in {"boxed_translator_stack_candidate", "boxed_support_stack"} else 25
        selected_stacks.extend(scoped[:limit])

    for row in selected_stacks:
        decision = str(row.get("stage2b_stack_decision") or "")
        if decision == "boxed_translator_stack_candidate":
            status = "test_now"
        elif decision in {"boxed_support_stack", "straight_stack_probe"}:
            status = "test_as_gate"
        elif decision == "vtrac_box_confirmation_watch":
            status = "watch_only_until_box_confirmed"
        else:
            status = "negative_control"
        rows.append(
            {
                "rule_id": f"HYP-{idx:03d}",
                "hypothesis_type": "signal_stack",
                "status": status,
                "lane": row.get("pair_scope", ""),
                "trigger": f"{row.get('source_a')} + {row.get('source_b')}",
                "active_state_days": row.get("active_state_days", ""),
                "avg_exposure_pool": row.get("avg_overlap_values_per_state_day", ""),
                "matched_value_rate": row.get("matched_value_rate", ""),
                "supported_event_rate": row.get("supported_event_rate", ""),
                "gap_teacher_event_count": row.get("gap_teacher_event_count", ""),
                "positive_conversion_event_count": row.get("positive_conversion_event_count", ""),
                "wrong_lane_event_count": row.get("wrong_lane_event_count", ""),
                "risk_control": row.get("decision_rationale", ""),
                "next_test": _next_test_for_status(status),
            }
        )
        idx += 1
    for source in source_candidates[:40]:
        rows.append(
            {
                "rule_id": f"HYP-{idx:03d}",
                "hypothesis_type": "single_source_gate",
                "status": "pair_before_promotion",
                "lane": source.get("target_lane", ""),
                "trigger": source.get("source_key", ""),
                "active_state_days": source.get("active_state_days", ""),
                "avg_exposure_pool": source.get("avg_pool_size", ""),
                "matched_value_rate": source.get("lane_hit_value_rate", ""),
                "supported_event_rate": source.get("winner_event_support_rate", ""),
                "gap_teacher_event_count": "",
                "positive_conversion_event_count": "",
                "wrong_lane_event_count": "",
                "risk_control": source.get("decision_rationale", ""),
                "next_test": "Only test as a partner in Stage 2B stack replay, not as standalone weight.",
            }
        )
        idx += 1
    return rows


def _next_test_for_status(status: str) -> str:
    if status == "test_now":
        return "Replay as boxed translator gate against March fixtures and at least one older window."
    if status == "test_as_gate":
        return "Use as a support condition paired with Arena box or sandbox box evidence."
    if status == "watch_only_until_box_confirmed":
        return "Keep in VTRAC/decay watch until a boxed source confirms the specific canonical family."
    if status == "negative_control":
        return "Use to guard against broad over-promotion and false confidence."
    return "Review manually."


def _cross_window_readiness(runs2_dir: Path, current_window: Path) -> Tuple[str, List[Dict[str, Any]]]:
    rows: List[Dict[str, Any]] = []
    for window in sorted(runs2_dir.glob("WINDOW_*")):
        if not window.is_dir() or "__PREALIGN" in window.name:
            continue
        prefix = f"{window.name}__ANALYSIS_ARENA"
        analysis_dir = window / "ANALYSIS_ARENA"
        files = {
            "performance_gap": window / f"{prefix}__PERFORMANCE_GAP__ledger.csv",
            "evidence_utilization": window / f"{prefix}__EVIDENCE_UTILIZATION_LEDGER.csv",
            "stage2_exposure": window / f"{prefix}__STAGE2_SIGNAL_EXPOSURE_LEDGER.csv",
            "stage2b_stack": window / f"{prefix}__STAGE2B_SIGNAL_STACK_SCORECARD.json",
            "priority_cases": window / f"{prefix}__AUDIT_INTERPRETATION_PRIORITY_CASES.csv",
        }
        scoreboard_count = len(list(analysis_dir.glob("*__BOARD_SCOREBOARD__analysis_arena_day_review.json"))) if analysis_dir.exists() else 0
        manifest_count = len(list(analysis_dir.glob("*__TRANSLATION_SANDBOX_SEED__analysis_arena_day_review.json"))) if analysis_dir.exists() else 0
        stage2_ready = files["performance_gap"].exists() and scoreboard_count > 0 and manifest_count > 0
        stage2b_ready = files["stage2_exposure"].exists() and files["stage2b_stack"].exists()
        if window.resolve() == current_window.resolve():
            recommended_action = "Already current Stage 2B baseline"
        elif stage2b_ready:
            recommended_action = "Ready for cross-window rollup"
        elif stage2_ready:
            recommended_action = "Run Stage 2 then Stage 2B"
        else:
            recommended_action = "Backfill missing window artifacts"
        rows.append(
            {
                "window": window.name,
                "is_current_window": str(window.resolve() == current_window.resolve()),
                "scoreboard_count": scoreboard_count,
                "translation_manifest_count": manifest_count,
                "has_performance_gap": str(files["performance_gap"].exists()),
                "has_evidence_utilization": str(files["evidence_utilization"].exists()),
                "has_stage2_exposure": str(files["stage2_exposure"].exists()),
                "has_stage2b_stack": str(files["stage2b_stack"].exists()),
                "stage2_ready": str(stage2_ready),
                "stage2b_ready": str(stage2b_ready),
                "recommended_action": recommended_action,
            }
        )
    lines = [
        "# Stage 2 Cross-Window Readiness",
        "",
        "Purpose: prevent overfitting March by identifying which older windows can receive the same Stage 2 / Stage 2B treatment.",
        "",
    ]
    for row in rows:
        lines.append(
            f"- `{row['window']}`: scoreboards=`{row['scoreboard_count']}`, manifests=`{row['translation_manifest_count']}`, "
            f"stage2_ready=`{row['stage2_ready']}`, stage2b_ready=`{row['stage2b_ready']}`, action={row['recommended_action']}"
        )
    lines.append("")
    return "\n".join(lines), rows


def _render_executive_readout(
    *,
    score_rows: Sequence[Dict[str, Any]],
    source_family_rows: Sequence[Dict[str, Any]],
    risk_rows: Sequence[Dict[str, Any]],
    stack_rows: Sequence[Dict[str, Any]],
    fixture_rows: Sequence[Dict[str, str]],
    metadata: Dict[str, Any],
) -> str:
    decision_counts = Counter(str(row.get("stage2_decision") or "") for row in score_rows)
    stack_counts = Counter(str(row.get("stage2b_stack_decision") or "") for row in stack_rows)
    risk_counts = Counter(str(row.get("risk_label") or "") for row in risk_rows)
    lines = [
        "# Stage 2 Executive Readout",
        "",
        "Purpose: interpret the Stage 2 denominator layer before any scoring or translator rewrite.",
        "",
        "## Executive Read",
        "",
        "- Stage 2 did not invalidate the Arena. It narrowed the work: useful evidence exists, but promotion must be gated by exposure burden.",
        "- Single broad signals are mostly not enough. The next value is in pair/stack behavior and fixture-driven translator tests.",
        "- VTRAC remains a strong territory/watch layer, but not a direct boxed/straight spending rule without narrower confirmation.",
        "- Boxed support gates are the most practical near-term translator surface.",
        "",
        "## Denominators",
        "",
        f"- Seed state-days: `{metadata.get('seed_state_days', 0)}`",
        f"- Winner events: `{metadata.get('winner_events', 0)}`",
        f"- Stage 2 exposure rows: `{metadata.get('exposure_rows', 0)}`",
        f"- Stage 2 source/lane rows: `{len(score_rows)}`",
        f"- Stage 2B stack rows: `{len(stack_rows)}`",
        f"- Fixture candidates: `{len(fixture_rows)}`",
        "",
        "## Stage 2 Decision Mix",
        "",
    ]
    for key, count in decision_counts.most_common():
        lines.append(f"- `{key}`: `{count}`")
    lines.extend(["", "## Stage 2B Stack Decision Mix", ""])
    for key, count in stack_counts.most_common():
        lines.append(f"- `{key}`: `{count}`")
    lines.extend(["", "## Denominator Risk Mix", ""])
    for key, count in risk_counts.most_common():
        lines.append(f"- `{key}`: `{count}`")
    lines.extend(["", "## Source-Family Read", ""])
    for row in source_family_rows:
        lines.append(
            f"- `{row['source_family']}`: sources=`{row['source_count']}`, "
            f"exposures=`{row['total_exposure_values']}`, lane_rate=`{_pct(_safe_float(row['lane_hit_value_rate']))}`. {row['read']}"
        )
    lines.extend(["", "## Immediate Guardrail", ""])
    lines.append("- Do not convert this directly into weights. Use the hypothesis queue to run bounded translator experiments first.")
    lines.append("")
    return "\n".join(lines)


def _render_stack_md(stack_rows: Sequence[Dict[str, Any]], *, full_pair_count: int, exported_pair_count: int) -> str:
    decision_counts = Counter(str(row.get("stage2b_stack_decision") or "") for row in stack_rows)
    lines = [
        "# Stage 2B Signal Stack Scorecard",
        "",
        "Purpose: identify which signal combinations are sharper than individual sources.",
        "",
        "## Denominators",
        "",
        f"- Full pair/state-day denominator rows: `{full_pair_count}`",
        f"- Exported drill-down ledger rows: `{exported_pair_count}`",
        f"- Stack scorecard rows: `{len(stack_rows)}`",
        "",
        "## Decision Mix",
        "",
    ]
    for key, count in decision_counts.most_common():
        lines.append(f"- `{key}`: `{count}`")
    sections = [
        ("Boxed Translator Candidates", {"boxed_translator_stack_candidate"}),
        ("Boxed Support Stacks", {"boxed_support_stack"}),
        ("VTRAC Confirmation Watch", {"vtrac_box_confirmation_watch"}),
        ("Straight Stack Probes", {"straight_stack_probe"}),
        ("Negative Controls", {"negative_control_stack"}),
    ]
    for title, decisions in sections:
        lines.extend(["", f"## {title}", ""])
        scoped = [row for row in stack_rows if str(row.get("stage2b_stack_decision") or "") in decisions]
        scoped.sort(
            key=lambda row: (
                -_safe_float(row.get("matched_value_rate")),
                -_safe_float(row.get("supported_event_rate")),
                _safe_float(row.get("avg_overlap_values_per_state_day")),
                row.get("pair_key", ""),
            )
        )
        if not scoped:
            lines.append("- None in this window.")
            continue
        for row in scoped[:20]:
            lines.append(
                "- "
                f"`{row['pair_key']}` active=`{row['active_state_days']}` "
                f"avg_pool=`{_safe_float(row['avg_overlap_values_per_state_day']):.1f}` "
                f"match_rate=`{_pct(_safe_float(row['matched_value_rate']))}` "
                f"event_support=`{_pct(_safe_float(row['supported_event_rate']))}` "
                f"decision=`{row['stage2b_stack_decision']}`"
            )
    lines.extend(["", "## Read", ""])
    lines.append("- Stack candidates are experiment inputs, not live-scoring weights.")
    lines.append("- VTRAC confirmation stacks remain watch/decay unless paired with bounded boxed overlap.")
    lines.append("- Negative-control stacks are valuable because they prevent broad over-promotion.")
    lines.append("")
    return "\n".join(lines)


def _render_fixture_md(
    *,
    priority_rows: Sequence[Dict[str, str]],
    gap_rows: Sequence[Dict[str, Any]],
    positive_rows: Sequence[Dict[str, Any]],
    decay_rows: Sequence[Dict[str, Any]],
    util_rows: Sequence[Dict[str, str]],
) -> str:
    status_counts = Counter(str(row.get("evidence_status") or "") for row in util_rows)
    outcome_counts = Counter(str(row.get("outcome_class") or "") for row in util_rows)
    lines = [
        "# Translator Fixture Deep Review",
        "",
        "Purpose: convert Stage 1 and Stage 2 evidence into stable translator teaching sets.",
        "",
        "## Fixture Counts",
        "",
        f"- Priority fixture rows: `{len(priority_rows)}`",
        f"- Gap teacher stack rows: `{len(gap_rows)}`",
        f"- Positive regression fixtures: `{len(positive_rows)}`",
        f"- Decay carryforward fixtures: `{len(decay_rows)}`",
        "",
        "Evidence status mix:",
    ]
    for key, count in status_counts.most_common():
        lines.append(f"- `{key}`: `{count}`")
    lines.append("")
    lines.append("Outcome mix:")
    for key, count in outcome_counts.most_common():
        lines.append(f"- `{key}`: `{count}`")
    lines.extend(
        [
            "",
            "## Fixture Use",
            "",
            "- Gap teachers show where evidence existed but the old downstream layer under-expressed it.",
            "- Wrong-lane cases define restraint rules, especially for VTRAC territory.",
            "- Positive conversions become regression anchors for future translator edits.",
            "- Decay cases preserve the carryforward/watch concept without contaminating same-day scoring.",
            "",
        ]
    )
    return "\n".join(lines)


def _render_wrong_lane_md(util_rows: Sequence[Dict[str, str]], stack_rows: Sequence[Dict[str, Any]]) -> str:
    wrong = [row for row in util_rows if row.get("evidence_status") == "CAPTURED_BUT_WRONG_LANE"]
    vt_stacks = [row for row in stack_rows if str(row.get("pair_scope") or "").startswith("vtrac")]
    lines = [
        "# Wrong-Lane Restraint Rules",
        "",
        "Purpose: prevent VTRAC/territory evidence from being over-promoted into boxed/straight action.",
        "",
        f"- Wrong-lane cases: `{len(wrong)}`",
        f"- VTRAC-related stack rows: `{len(vt_stacks)}`",
        "",
        "## Rules",
        "",
        "- VTRAC-only evidence may mark territory/watch/carryforward, but should not create a boxed/straight spend by itself.",
        "- A VTRAC source needs a bounded boxed or exact confirmation source before translator promotion.",
        "- Broad VTRAC stacks with high false-positive proxy stay negative-control/context surfaces.",
        "- Wrong-lane cases must be included as regression tests before any translator promotion.",
        "",
        "## Highest-Support VTRAC Stacks",
        "",
    ]
    vt_stacks.sort(key=lambda row: (-_safe_float(row.get("supported_event_rate")), -_safe_float(row.get("matched_value_rate"))))
    for row in vt_stacks[:20]:
        lines.append(
            "- "
            f"`{row['pair_key']}` decision=`{row['stage2b_stack_decision']}` "
            f"event_support=`{_pct(_safe_float(row['supported_event_rate']))}` "
            f"wrong_lane_events=`{row['wrong_lane_event_count']}`"
        )
    lines.append("")
    return "\n".join(lines)


def _render_hypothesis_md(rows: Sequence[Dict[str, Any]]) -> str:
    status_counts = Counter(str(row.get("status") or "") for row in rows)
    lines = [
        "# Translator Rule Hypothesis Queue",
        "",
        "Purpose: queue bounded translator experiments from Stage 2/2B evidence without changing live scoring prematurely.",
        "",
        "## Status Mix",
        "",
    ]
    for key, count in status_counts.most_common():
        lines.append(f"- `{key}`: `{count}`")
    lines.extend(["", "## Top Hypotheses", ""])
    for row in rows[:40]:
        lines.append(
            "- "
            f"`{row['rule_id']}` [{row['status']}]: `{row['trigger']}` "
            f"lane=`{row['lane']}` avg_pool=`{row['avg_exposure_pool']}` "
            f"match_rate=`{_pct(_safe_float(row['matched_value_rate']))}`"
        )
    lines.extend(["", "## Guardrail", ""])
    lines.append("- These are experiment hypotheses. They are not final scoring weights or budget rules.")
    lines.append("")
    return "\n".join(lines)


def _render_work_log(paths: Dict[str, Path], counts: Dict[str, Any]) -> str:
    lines = [
        "# Stage 2B Overnight Work Log",
        "",
        "Scope: approved read-only post-run interpretation package after Stage 2 exposure denominators.",
        "",
        "## Completed Work",
        "",
        "- Built source-family ranking and denominator risk map.",
        "- Built signal-pair/stack ledger and stack scorecard.",
        "- Built fixture deep-review outputs for gap, positive, wrong-lane, and decay teaching sets.",
        "- Built translator rule hypothesis queue.",
        "- Built cross-window readiness check.",
        "",
        "## Counts",
        "",
    ]
    for key, value in counts.items():
        lines.append(f"- `{key}`: `{value}`")
    lines.extend(["", "## Generated Files", ""])
    for key in [
        "executive_md",
        "source_family_csv",
        "risk_csv",
        "pair_ledger_csv",
        "stack_md",
        "stack_json",
        "promotion_csv",
        "negative_csv",
        "fixture_md",
        "gap_stacks_csv",
        "wrong_lane_md",
        "positive_csv",
        "decay_csv",
        "hypothesis_md",
        "hypothesis_csv",
        "readiness_md",
    ]:
        lines.append(f"- `{key}`: `{safe_rel(paths[key])}`")
    lines.extend(["", "## Next Review", ""])
    lines.append("- Start with the executive readout, then the hypothesis queue, then the stack scorecard.")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    args = _parse_args()
    window_root = _resolve_path(args.window_root)
    runs2_dir = _resolve_path(args.runs2_dir)
    if not window_root.exists():
        raise SystemExit(f"Window root not found: {window_root}")
    paths = _default_paths(window_root)

    util_rows = _read_csv_rows(paths["util"])
    attribution_rows = _read_csv_rows(paths["attribution"])
    priority_rows = _read_csv_rows(paths["priority_cases"])
    exposure_rows = _read_csv_rows(paths["stage2_exposure"])
    score_payload = _read_json(paths["stage2_scorecard"])
    score_rows = score_payload.get("scorecard") or []
    stage2_fixture_rows = _read_csv_rows(paths["stage2_fixtures"])
    if not exposure_rows or not score_rows:
        raise SystemExit("Stage 2 outputs are required before Stage 2B can run.")

    event_lookup = {_event_id(row): row for row in util_rows}
    source_family_rows = _source_family_ranking(score_rows)
    risk_rows = _denominator_risk_map(score_rows)
    pair_ledger = _build_pairing_ledger(exposure_rows, score_rows, event_lookup)
    stack_rows = _pair_scorecard(pair_ledger, event_lookup)
    pair_ledger_export = _pair_ledger_drilldown(pair_ledger)
    promotion_rows = [
        row
        for row in stack_rows
        if str(row.get("stage2b_stack_decision") or "")
        in {"boxed_translator_stack_candidate", "boxed_support_stack", "vtrac_box_confirmation_watch", "straight_stack_probe"}
    ]
    negative_rows = [row for row in stack_rows if str(row.get("stage2b_stack_decision") or "") == "negative_control_stack"]
    gap_rows = _gap_teacher_stacks(priority_rows, pair_ledger, stack_rows)
    positive_rows = _positive_regression_rows(util_rows, pair_ledger)
    carryforward_rows = _decay_rows(util_rows)
    hypothesis_rows = _hypothesis_rows(stack_rows, score_rows)
    readiness_md, readiness_rows = _cross_window_readiness(runs2_dir, window_root)

    metadata = score_payload.get("metadata") or {}
    metadata["stage2b_stack_rows"] = len(stack_rows)
    metadata["pairing_ledger_rows"] = len(pair_ledger)
    metadata["exported_pairing_drilldown_rows"] = len(pair_ledger_export)
    _write_csv(paths["source_family_csv"], source_family_rows, force=args.force)
    _write_csv(paths["risk_csv"], risk_rows, force=args.force)
    _write_text(
        paths["executive_md"],
        _render_executive_readout(
            score_rows=score_rows,
            source_family_rows=source_family_rows,
            risk_rows=risk_rows,
            stack_rows=stack_rows,
            fixture_rows=stage2_fixture_rows,
            metadata=metadata,
        ),
        force=args.force,
    )
    _write_csv(paths["pair_ledger_csv"], pair_ledger_export, force=args.force)
    stack_payload = {
        "schema_version": "analysis_arena_stage2b_signal_stack_scorecard/v1",
        "window_root": safe_rel(window_root),
        "metadata": metadata,
        "decision_counts": dict(Counter(str(row.get("stage2b_stack_decision") or "") for row in stack_rows).most_common()),
        "scorecard": stack_rows,
    }
    _write_json(paths["stack_json"], stack_payload, force=args.force)
    _write_text(
        paths["stack_md"],
        _render_stack_md(
            stack_rows,
            full_pair_count=len(pair_ledger),
            exported_pair_count=len(pair_ledger_export),
        ),
        force=args.force,
    )
    _write_csv(paths["promotion_csv"], promotion_rows, force=args.force)
    _write_csv(paths["negative_csv"], negative_rows, force=args.force)
    _write_csv(paths["gap_stacks_csv"], gap_rows, force=args.force)
    _write_csv(paths["positive_csv"], positive_rows, force=args.force)
    _write_csv(paths["decay_csv"], carryforward_rows, force=args.force)
    _write_text(
        paths["fixture_md"],
        _render_fixture_md(
            priority_rows=priority_rows,
            gap_rows=gap_rows,
            positive_rows=positive_rows,
            decay_rows=carryforward_rows,
            util_rows=util_rows,
        ),
        force=args.force,
    )
    _write_text(paths["wrong_lane_md"], _render_wrong_lane_md(util_rows, stack_rows), force=args.force)
    _write_csv(paths["hypothesis_csv"], hypothesis_rows, force=args.force)
    _write_text(paths["hypothesis_md"], _render_hypothesis_md(hypothesis_rows), force=args.force)
    _write_text(paths["readiness_md"], readiness_md, force=args.force)

    counts = {
        "source_family_rows": len(source_family_rows),
        "risk_rows": len(risk_rows),
        "full_pairing_denominator_rows": len(pair_ledger),
        "exported_pairing_drilldown_rows": len(pair_ledger_export),
        "stack_scorecard_rows": len(stack_rows),
        "promotion_candidate_rows": len(promotion_rows),
        "negative_control_rows": len(negative_rows),
        "gap_teacher_stack_rows": len(gap_rows),
        "positive_regression_rows": len(positive_rows),
        "decay_carryforward_rows": len(carryforward_rows),
        "hypothesis_rows": len(hypothesis_rows),
        "cross_window_rows": len(readiness_rows),
        "attribution_rows_read": len(attribution_rows),
    }
    _write_text(paths["work_log_md"], _render_work_log(paths, counts), force=args.force)

    print(f"wrote {safe_rel(paths['executive_md'])}")
    print(f"wrote {safe_rel(paths['pair_ledger_csv'])} rows={len(pair_ledger_export)} full_pair_rows={len(pair_ledger)}")
    print(f"wrote {safe_rel(paths['stack_md'])} stacks={len(stack_rows)}")
    print(f"wrote {safe_rel(paths['hypothesis_md'])} hypotheses={len(hypothesis_rows)}")
    print(f"wrote {safe_rel(paths['work_log_md'])}")


if __name__ == "__main__":
    main()
