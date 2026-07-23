#!/usr/bin/env python3
"""Interpret a completed Analysis Arena evidence-utilization audit.

This is the human-decision layer after the post-run audit generator. It reads
the utilization ledger, signal attribution ledger, decay/frontier summaries, and
cross-window rollup to produce prioritized translator lessons and next actions.
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
DEFAULT_CROSS_WINDOW_CSV = FINAL_DOCS_DIR / "AAT9_ANALYSIS_ARENA__CROSS_WINDOW_ROLLUP.csv"


def _parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--window-root", required=True, help="RUNS_2 window root.")
    ap.add_argument("--cross-window-csv", default=str(DEFAULT_CROSS_WINDOW_CSV), help="Optional cross-window rollup CSV.")
    ap.add_argument("--pro-feedback", default=str(REPO_ROOT / "tasks" / "PRO_92.txt"), help="Optional PRO feedback file.")
    ap.add_argument("--force", action="store_true", help="Overwrite existing outputs.")
    return ap.parse_args()


def _resolve_path(value: str) -> Path:
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
        for key in row.keys():
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
        "audit_json": window_root / f"{prefix}__EVIDENCE_UTILIZATION_AUDIT.json",
        "util_csv": window_root / f"{prefix}__EVIDENCE_UTILIZATION_LEDGER.csv",
        "signal_csv": window_root / f"{prefix}__WINNER_SIGNAL_ATTRIBUTION_LEDGER.csv",
        "frontier_csv": window_root / f"{prefix}__C1_C2_FRONTIER_CASES.csv",
        "decay_json": window_root / f"{prefix}__DECAY_CARRYOVER_SCORECARD.json",
        "interpretation_md": window_root / f"{prefix}__AUDIT_INTERPRETATION_PASS.md",
        "interpretation_json": window_root / f"{prefix}__AUDIT_INTERPRETATION_PASS.json",
        "priority_cases_csv": window_root / f"{prefix}__AUDIT_INTERPRETATION_PRIORITY_CASES.csv",
        "signal_decisions_csv": window_root / f"{prefix}__AUDIT_INTERPRETATION_SIGNAL_DECISIONS.csv",
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


def _rate(count: int, total: int) -> float:
    return count / total if total else 0.0


def _count(rows: Sequence[Dict[str, Any]], field: str, value: str) -> int:
    return sum(1 for row in rows if str(row.get(field) or "") == value)


def _event_key(row: Dict[str, Any]) -> str:
    return str(row.get("event_id") or f"{row.get('date')}|{row.get('state_key')}|{row.get('period')}|{row.get('winner')}")


def _source_counts_for_events(signal_rows: Sequence[Dict[str, str]], event_ids: set[str]) -> Dict[str, List[Tuple[str, int]]]:
    counters: Dict[str, Counter[str]] = {
        "exact": Counter(),
        "box": Counter(),
        "vtrac": Counter(),
        "tier_a": Counter(),
        "families": Counter(),
    }
    for row in signal_rows:
        if row.get("event_id") not in event_ids:
            continue
        source = f"{row.get('source_family')}:{row.get('source_tool')}"
        counters["families"][str(row.get("source_family") or "")] += 1
        if str(row.get("tier")) == "A":
            counters["tier_a"][source] += 1
        if str(row.get("match_exact")) == "True":
            counters["exact"][source] += 1
        if str(row.get("match_box")) == "True":
            counters["box"][source] += 1
        if str(row.get("match_vtrac_straight")) == "True" or str(row.get("match_vtrac_box")) == "True":
            counters["vtrac"][source] += 1
    return {key: counter.most_common(12) for key, counter in counters.items()}


def _select_examples(rows: Sequence[Dict[str, str]], *, cohort: str, limit: int = 8) -> List[Dict[str, Any]]:
    scoped = [row for row in rows if row.get("outcome_class") == cohort or row.get("evidence_status") == cohort]
    scoped.sort(
        key=lambda row: (
            -_safe_int(row.get("sharp_signal_count")),
            -_safe_int(row.get("box_source_count")),
            -_safe_float(row.get("frontier_strength_score")),
            str(row.get("date") or ""),
            str(row.get("state_key") or ""),
        )
    )
    return [
        {
            "event_id": _event_key(row),
            "date": row.get("date", ""),
            "state_key": row.get("state_key", ""),
            "period": row.get("period", ""),
            "winner": row.get("winner", ""),
            "outcome_class": row.get("outcome_class", ""),
            "evidence_status": row.get("evidence_status", ""),
            "board_rank": row.get("board_rank", ""),
            "legacy_static_rank": row.get("legacy_static_rank", ""),
            "rank_signal_valid": row.get("rank_signal_valid", ""),
            "rank_integrity_status": row.get("rank_integrity_status", ""),
            "sharp_signal_count": row.get("sharp_signal_count", ""),
            "territory_signal_count": row.get("territory_signal_count", ""),
            "frontier_signature_type": row.get("frontier_signature_type", ""),
            "frontier_signature_strength": row.get("frontier_signature_strength", ""),
            "decay_any_profile": row.get("decay_any_profile", ""),
            "interpretation": row.get("interpretation", ""),
        }
        for row in scoped[:limit]
    ]


def _build_signal_decisions(audit_json: Dict[str, Any]) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for row in audit_json.get("boolean_signal_scorecard") or []:
        signal = str(row.get("signal") or "")
        tier = str(row.get("tier") or "")
        target_lane = str(row.get("target_lane") or "")
        present = _safe_int(row.get("present_events"))
        converted = _safe_int(row.get("converted_events"))
        gaps = _safe_int(row.get("gap_events"))
        vt_only = _safe_int(row.get("vt_only_events"))
        decision = "track_context"
        rationale = str(row.get("read") or "")
        if signal in {"arena_exact_signal", "sandbox_exact_seed", "play_card_any_exact"}:
            decision = "straight_lane_fixture"
        elif signal in {"arena_box_signal", "arena_primary_box", "sandbox_box_seed", "play_card_any_box"}:
            decision = "boxed_lane_fixture"
        elif tier == "B" and target_lane == "vtrac":
            decision = "vtrac_decay_lane_only_until_paired"
        elif tier == "B":
            decision = "supporting_gate_not_standalone"
        elif tier == "C":
            decision = "ambient_context_only"
        rows.append(
            {
                "signal": signal,
                "tier": tier,
                "target_lane": target_lane,
                "present_events": present,
                "converted_events": converted,
                "gap_events": gaps,
                "vt_only_events": vt_only,
                "conversion_rate_within_signal": converted / present if present else 0.0,
                "gap_rate_within_signal": gaps / present if present else 0.0,
                "decision": decision,
                "rationale": rationale,
            }
        )
    return rows


def _priority_case_rows(util_rows: Sequence[Dict[str, str]]) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []

    def add(row: Dict[str, str], cohort: str, priority: int, fixture_use: str) -> None:
        rows.append(
            {
                "priority": priority,
                "fixture_cohort": cohort,
                "fixture_use": fixture_use,
                "event_id": _event_key(row),
                "date": row.get("date", ""),
                "state_key": row.get("state_key", ""),
                "period": row.get("period", ""),
                "winner": row.get("winner", ""),
                "outcome_class": row.get("outcome_class", ""),
                "evidence_status": row.get("evidence_status", ""),
                "board_rank": row.get("board_rank", ""),
                "legacy_static_rank": row.get("legacy_static_rank", ""),
                "rank_signal_valid": row.get("rank_signal_valid", ""),
                "rank_integrity_status": row.get("rank_integrity_status", ""),
                "sharp_signal_count": row.get("sharp_signal_count", ""),
                "territory_signal_count": row.get("territory_signal_count", ""),
                "box_source_count": row.get("box_source_count", ""),
                "exact_source_count": row.get("exact_source_count", ""),
                "vtrac_source_count": row.get("vtrac_source_count", ""),
                "frontier_signature_type": row.get("frontier_signature_type", ""),
                "frontier_signature_strength": row.get("frontier_signature_strength", ""),
                "frontier_strength_score": row.get("frontier_strength_score", ""),
                "decay_any_profile": row.get("decay_any_profile", ""),
                "interpretation": row.get("interpretation", ""),
            }
        )

    for row in util_rows:
        if row.get("outcome_class") in {"BOX_GAP", "EXACT_GAP"}:
            add(row, "gap_teacher", 1, "Teach boxed/straight translator what old final layer underused.")

    def top_scoped(selector, cohort: str, priority: int, fixture_use: str, limit: int) -> None:
        scoped = [row for row in util_rows if selector(row)]
        scoped.sort(
            key=lambda row: (
                -_safe_int(row.get("sharp_signal_count")),
                -_safe_int(row.get("box_source_count")),
                -_safe_float(row.get("frontier_strength_score")),
                str(row.get("date") or ""),
            )
        )
        seen = {row["event_id"] for row in rows}
        count = 0
        for row in scoped:
            if _event_key(row) in seen:
                continue
            add(row, cohort, priority, fixture_use)
            seen.add(_event_key(row))
            count += 1
            if count >= limit:
                break

    top_scoped(
        lambda row: row.get("evidence_status") == "CAPTURED_AND_USED",
        "positive_conversion",
        2,
        "Preserve examples of evidence reaching downstream conversion.",
        12,
    )
    top_scoped(
        lambda row: row.get("evidence_status") == "CAPTURED_BUT_WRONG_LANE",
        "wrong_lane_vtrac",
        3,
        "Teach VTRAC/territory restraint versus boxed/straight promotion.",
        12,
    )
    top_scoped(
        lambda row: row.get("evidence_status") == "DECAY_VALIDATED",
        "decay_teacher",
        4,
        "Teach carryforward watch behavior separate from same-day failure.",
        10,
    )
    top_scoped(
        lambda row: row.get("evidence_status") == "CAPTURED_BUT_NOT_PROMOTED",
        "not_promoted_probe",
        5,
        "Investigate whether capture was meaningful or only broad/derived context.",
        10,
    )
    rows.sort(key=lambda row: (int(row["priority"]), str(row["date"]), str(row["state_key"]), str(row["period"])))
    return rows


def _cross_window_context(cross_rows: Sequence[Dict[str, str]], window_root: Path) -> Dict[str, Any]:
    if not cross_rows:
        return {}
    def avg(field: str) -> float:
        vals = [_safe_float(row.get(field), None) for row in cross_rows]  # type: ignore[arg-type]
        clean = [v for v in vals if isinstance(v, float)]
        return sum(clean) / len(clean) if clean else 0.0

    target = None
    for row in cross_rows:
        if str(row.get("window_root") or "").strip() == safe_rel(window_root):
            target = row
            break
    if target is None:
        for row in cross_rows:
            if window_root.name.replace("WINDOW_", "") in str(row.get("window") or ""):
                target = row
                break
    return {
        "windows": len(cross_rows),
        "winner_events": sum(_safe_int(row.get("winner_events")) for row in cross_rows),
        "credited_hits": sum(_safe_int(row.get("credited_hits")) for row in cross_rows),
        "averages": {
            "candidate_like_event_rate": avg("candidate_like_event_rate"),
            "finalist_supported_hit_rate": avg("finalist_supported_hit_rate"),
            "play_card_any_box_rate": avg("play_card_any_box_rate"),
            "opportunity_gap_box_rate": avg("opportunity_gap_box_rate"),
        },
        "current_window": target or {},
    }


def _frontier_context(frontier_rows: Sequence[Dict[str, str]], util_rows: Sequence[Dict[str, str]]) -> Dict[str, Any]:
    event_by_key = {(row.get("date", ""), row.get("state_key", ""), row.get("winner", "")): row for row in util_rows}
    signature = Counter(str(row.get("frontier_signature_type") or "UNSPECIFIED") for row in frontier_rows)
    strength = Counter(str(row.get("signature_strength") or "UNSPECIFIED") for row in frontier_rows)
    sharp_cases: List[Dict[str, Any]] = []
    for row in frontier_rows:
        event = event_by_key.get((row.get("date", ""), row.get("state_key", ""), row.get("winner", ""))) or {}
        sig = str(row.get("frontier_signature_type") or "")
        strong = str(row.get("signature_strength") or "").upper() == "STRONG"
        if sig in {"LITERAL_FRONTIER", "FAMILY_FRONTIER"} or strong:
            sharp_cases.append(
                {
                    "event_id": _event_key(event) if event else f"{row.get('date')}|{row.get('state_key')}|?|{row.get('winner')}",
                    "date": row.get("date", ""),
                    "state_key": row.get("state_key", ""),
                    "winner": row.get("winner", ""),
                    "outcome_class": event.get("outcome_class", ""),
                    "evidence_status": event.get("evidence_status", ""),
                    "signature": sig,
                    "strength": row.get("signature_strength", ""),
                    "frontier_strength_score": row.get("frontier_strength_score", ""),
                    "double_anchor_score": row.get("double_anchor_score", ""),
                    "family_frontier_score": row.get("family_frontier_score", ""),
                    "literal_frontier_score": row.get("literal_frontier_score", ""),
                }
            )
    sharp_cases.sort(key=lambda row: (-_safe_float(row.get("frontier_strength_score")), str(row.get("date"))))
    return {
        "signature_mix": dict(signature.most_common()),
        "strength_mix": dict(strength.most_common()),
        "sharp_case_count": len(sharp_cases),
        "sharp_cases": sharp_cases[:15],
    }


def _decay_context(decay_json: Dict[str, Any]) -> Dict[str, Any]:
    panels = decay_json.get("metric_families") or []
    selected = []
    for panel in panels:
        selected.append(
            {
                "metric_family": panel.get("metric_family"),
                "label": panel.get("label"),
                "active_state_days": panel.get("active_state_days"),
                "same_day_resolved": panel.get("same_day_resolved"),
                "same_day_rate": panel.get("same_day_rate"),
                "horizon_resolved": panel.get("horizon_resolved"),
                "horizon_rate": panel.get("horizon_rate"),
                "incremental_decay_lift": panel.get("incremental_decay_lift"),
            }
        )
    selected.sort(key=lambda row: (-_safe_float(row.get("incremental_decay_lift")), str(row.get("metric_family"))))
    return {
        "metadata": decay_json.get("metadata") or {},
        "summary": decay_json.get("summary") or {},
        "top_metric_lifts": selected[:8],
    }


def _render_examples(title: str, examples: Sequence[Dict[str, Any]]) -> List[str]:
    lines = [f"### {title}", ""]
    if not examples:
        lines.append("- _No examples found._")
        lines.append("")
        return lines
    for row in examples:
        lines.append(
            f"- `{row.get('date')}` `{row.get('state_key')}` `{row.get('period')}` winner=`{row.get('winner')}` "
            f"outcome=`{row.get('outcome_class')}` status=`{row.get('evidence_status')}` "
            + (
                f"analytical_rank=`{row.get('board_rank')}` "
                if _truthy(row.get("rank_signal_valid"))
                else "analytical_rank=`NOT_EVALUABLE` "
            )
            + f"sharp=`{row.get('sharp_signal_count')}` "
            f"frontier=`{row.get('frontier_signature_type') or '-'}` decay=`{row.get('decay_any_profile') or '-'}`"
        )
    lines.append("")
    return lines


def _render_markdown(payload: Dict[str, Any], paths: Dict[str, Path]) -> str:
    summary = payload["summary"]
    counts = summary["audit_counts"]
    cross = payload.get("cross_window_context") or {}
    current = cross.get("current_window") or {}
    averages = cross.get("averages") or {}
    cohort = payload["cohort_interpretation"]
    lines: List[str] = [
        "# Analysis Arena Audit Interpretation Pass",
        "",
        "Purpose: convert the March post-run audit into practical translator, Brain, and cadence decisions.",
        "",
        "## 1. Executive Read",
        "",
        "- PRO_92 reinforces the same conclusion as the audit: this branch is now a serious upstream evidence engine, not yet a finished combo/budget engine.",
        "- The core bottleneck is downstream expression: the system often preserves winner-relevant evidence before the old final candidate layer expresses it correctly.",
        "- This interpretation pass keeps scoring changes blocked until Stage 2 adds false-positive/exposure denominators.",
        "",
        "## 2. Denominators",
        "",
        f"- Winner events audited: `{counts.get('winner_events', 0)}`",
        f"- Signal attribution rows: `{counts.get('signal_attribution_rows', 0)}`",
        f"- Pre-draw winner-aligned rows: `{counts.get('pre_draw_attribution_rows', 0)}`",
        f"- Post-result explanatory rows: `{counts.get('post_result_attribution_rows', 0)}`",
        f"- Priority fixture candidates exported: `{summary.get('priority_case_count', 0)}`",
        "",
        "## 3. Cross-Window Context",
        "",
    ]
    if current:
        lines.extend(
            [
                f"- Cross-window sample: `{cross.get('windows', 0)}` windows, `{cross.get('winner_events', 0)}` winner events, `{cross.get('credited_hits', 0)}` credited hits.",
                f"- March candidate-like rate: `{_pct(_safe_float(current.get('candidate_like_event_rate')))}` vs cross-window average `{_pct(_safe_float(averages.get('candidate_like_event_rate')))}`.",
                f"- March finalist-supported hit rate: `{_pct(_safe_float(current.get('finalist_supported_hit_rate')))}` vs cross-window average `{_pct(_safe_float(averages.get('finalist_supported_hit_rate')))}`.",
                f"- March play-card any-box rate: `{_pct(_safe_float(current.get('play_card_any_box_rate')))}` vs cross-window average `{_pct(_safe_float(averages.get('play_card_any_box_rate')))}`.",
                f"- March opportunity-gap box rate: `{_pct(_safe_float(current.get('opportunity_gap_box_rate')))}` vs cross-window average `{_pct(_safe_float(averages.get('opportunity_gap_box_rate')))}`.",
            ]
        )
    else:
        lines.append("- Cross-window rollup unavailable for this interpretation run.")
    lines.extend(
        [
            "",
            "## 4. Audit Cohort Read",
            "",
            f"- Captured-and-used: `{counts.get('captured_and_used', 0)}`. These are positive fixtures for evidence reaching action.",
            f"- Captured-but-underused: `{counts.get('captured_but_underused', 0)}`. These are highest-priority translator teaching cases.",
            f"- Captured-but-wrong-lane: `{counts.get('captured_but_wrong_lane', 0)}`. These are VTRAC/territory cases that need restraint or sharper boxed/straight gates.",
            f"- Decay-validated: `{counts.get('decay_validated', 0)}`. These should feed carryforward/watch logic, not be flattened into same-day misses.",
            f"- Captured-but-not-promoted: `{counts.get('captured_but_not_promoted', 0)}`. These need Stage-2 exposure testing before promotion.",
            "",
            "Gap cohort source read:",
        ]
    )
    for mode, items in (cohort.get("gap_sources") or {}).items():
        joined = ", ".join(f"`{name}` x{count}" for name, count in items[:8]) or "_none_"
        lines.append(f"- {mode}: {joined}")
    lines.extend(
        [
            "",
            "Wrong-lane source read:",
        ]
    )
    for mode, items in (cohort.get("wrong_lane_sources") or {}).items():
        joined = ", ".join(f"`{name}` x{count}" for name, count in items[:8]) or "_none_"
        lines.append(f"- {mode}: {joined}")

    lines.extend(["", "## 5. Signal Decisions", ""])
    for row in payload["signal_decisions"][:16]:
        lines.append(
            f"- `{row['signal']}` -> `{row['decision']}`; present `{row['present_events']}`, "
            f"converted `{row['converted_events']}`, gaps `{row['gap_events']}`."
        )

    decay = payload.get("decay_context") or {}
    lines.extend(["", "## 6. Decay Interpretation", ""])
    for row in (decay.get("top_metric_lifts") or [])[:6]:
        lines.append(
            f"- `{row.get('metric_family')}`: same-day `{_pct(_safe_float(row.get('same_day_rate')))}`, "
            f"horizon `{_pct(_safe_float(row.get('horizon_rate')))}`, incremental lift `{row.get('incremental_decay_lift')}`."
        )
    lines.extend(
        [
            "",
            "Interpretation: broad VTRAC/territory decay is strong evidence of state-day resolution, but boxed/straight scoring should use narrower exact/box evidence before spending budget.",
        ]
    )

    frontier = payload.get("frontier_context") or {}
    lines.extend(["", "## 7. Frontier Interpretation", ""])
    lines.append(
        "- Signature mix: "
        + (", ".join(f"`{k}` x{v}" for k, v in (frontier.get("signature_mix") or {}).items()) or "_none_")
    )
    lines.append(
        "- Strength mix: "
        + (", ".join(f"`{k}` x{v}" for k, v in (frontier.get("strength_mix") or {}).items()) or "_none_")
    )
    lines.append(f"- Sharp frontier candidates retained: `{frontier.get('sharp_case_count', 0)}`.")
    lines.append("- Read: literal/family/strong/double-anchor frontier should become translator fixtures; generic VTRAC frontier remains territory context.")

    lines.extend(["", "## 8. Priority Cases", ""])
    lines.append(f"- Priority cases CSV: `{safe_rel(paths['priority_cases_csv'])}`")
    lines.append("- Fixture priority 1 contains all gap teachers; priority 2 positive conversions; priority 3 wrong-lane VTRAC; priority 4 decay teachers; priority 5 not-promoted probes.")
    lines.extend([""] + _render_examples("Gap Teachers", payload["examples"].get("gap_teachers") or []))
    lines.extend(_render_examples("Positive Conversions", payload["examples"].get("positive_conversions") or []))
    lines.extend(_render_examples("Wrong-Lane VTRAC", payload["examples"].get("wrong_lane") or []))

    lines.extend(
        [
            "## 9. Next Actions",
            "",
            "1. Build Stage-2 Signal Exposure / False-Positive Ledger before assigning new scoring weights.",
            "2. Use all 23 gap rows as boxed/straight translator training fixtures.",
            "3. Use wrong-lane cases to define when VTRAC territory may promote and when it must remain watch-only.",
            "4. Preserve captured-and-used cases as regression positives for future translator changes.",
            "5. Treat captured-but-not-promoted cases as hypothesis probes, not automatic promotions.",
            "6. Keep Brain2 static-rank diagnostics active before trusting top-primary metrics as dynamic selection.",
            "",
            "## 10. Generated Files",
            "",
            f"- Interpretation JSON: `{safe_rel(paths['interpretation_json'])}`",
            f"- Priority cases CSV: `{safe_rel(paths['priority_cases_csv'])}`",
            f"- Signal decisions CSV: `{safe_rel(paths['signal_decisions_csv'])}`",
        ]
    )
    return "\n".join(lines) + "\n"


def build_payload(window_root: Path, *, cross_window_csv: Path, pro_feedback: Path) -> Tuple[Dict[str, Any], Dict[str, Path]]:
    paths = _default_paths(window_root)
    audit_json = _read_json(paths["audit_json"])
    util_rows = _read_csv_rows(paths["util_csv"])
    signal_rows = _read_csv_rows(paths["signal_csv"])
    frontier_rows = _read_csv_rows(paths["frontier_csv"])
    decay_json = _read_json(paths["decay_json"])
    cross_rows = _read_csv_rows(cross_window_csv)
    priority_cases = _priority_case_rows(util_rows)
    signal_decisions = _build_signal_decisions(audit_json)

    gap_ids = {_event_key(row) for row in util_rows if row.get("outcome_class") in {"BOX_GAP", "EXACT_GAP"}}
    wrong_lane_ids = {_event_key(row) for row in util_rows if row.get("evidence_status") == "CAPTURED_BUT_WRONG_LANE"}
    not_promoted_ids = {_event_key(row) for row in util_rows if row.get("evidence_status") == "CAPTURED_BUT_NOT_PROMOTED"}
    positive_ids = {_event_key(row) for row in util_rows if row.get("evidence_status") == "CAPTURED_AND_USED"}
    summary = {
        "window_root": safe_rel(window_root),
        "audit_counts": audit_json.get("summary", {}).get("counts", {}),
        "evidence_status_counts": audit_json.get("summary", {}).get("evidence_status_counts", {}),
        "outcome_class_counts": audit_json.get("summary", {}).get("outcome_class_counts", {}),
        "priority_case_count": len(priority_cases),
        "pro_92_integrated": pro_feedback.exists(),
    }
    payload: Dict[str, Any] = {
        "schema_version": "analysis_arena_audit_interpretation_pass/v1",
        "summary": summary,
        "cross_window_context": _cross_window_context(cross_rows, window_root),
        "cohort_interpretation": {
            "gap_event_count": len(gap_ids),
            "wrong_lane_event_count": len(wrong_lane_ids),
            "not_promoted_event_count": len(not_promoted_ids),
            "positive_event_count": len(positive_ids),
            "gap_sources": _source_counts_for_events(signal_rows, gap_ids),
            "wrong_lane_sources": _source_counts_for_events(signal_rows, wrong_lane_ids),
            "not_promoted_sources": _source_counts_for_events(signal_rows, not_promoted_ids),
        },
        "signal_decisions": signal_decisions,
        "decay_context": _decay_context(decay_json),
        "frontier_context": _frontier_context(frontier_rows, util_rows),
        "examples": {
            "gap_teachers": _select_examples(util_rows, cohort="BOX_GAP", limit=8)
            + _select_examples(util_rows, cohort="EXACT_GAP", limit=4),
            "positive_conversions": _select_examples(util_rows, cohort="CAPTURED_AND_USED", limit=8),
            "wrong_lane": _select_examples(util_rows, cohort="CAPTURED_BUT_WRONG_LANE", limit=8),
            "decay_teachers": _select_examples(util_rows, cohort="DECAY_VALIDATED", limit=8),
            "not_promoted": _select_examples(util_rows, cohort="CAPTURED_BUT_NOT_PROMOTED", limit=8),
        },
        "pro_92_read": {
            "file": safe_rel(pro_feedback) if pro_feedback.exists() else "",
            "integrated_points": [
                "Analysis Arena is an upstream evidence engine, not yet a finished combo/budget engine.",
                "The main bottleneck is expression of preserved evidence through old downstream candidate/play-card infrastructure.",
                "Opportunity-gap rows are high-value translator teaching examples.",
                "Broad tracker presence should be downgraded unless paired with sharper exact/box/frontier evidence.",
                "C1/C2 frontier remains valuable only when winner sidecar completeness is enforced.",
            ],
        },
    }
    payload["_rows"] = {
        "priority_cases": priority_cases,
        "signal_decisions": signal_decisions,
    }
    return payload, paths


def main() -> None:
    args = _parse_args()
    window_root = _resolve_path(args.window_root)
    cross_window_csv = _resolve_path(args.cross_window_csv)
    pro_feedback = _resolve_path(args.pro_feedback)
    payload, paths = build_payload(window_root, cross_window_csv=cross_window_csv, pro_feedback=pro_feedback)
    rows = payload.pop("_rows")

    _write_csv(paths["priority_cases_csv"], rows["priority_cases"], force=args.force)
    _write_csv(paths["signal_decisions_csv"], rows["signal_decisions"], force=args.force)
    _write_json(paths["interpretation_json"], payload, force=args.force)
    _write_text(paths["interpretation_md"], _render_markdown(payload, paths), force=args.force)

    for key in ("interpretation_md", "interpretation_json", "priority_cases_csv", "signal_decisions_csv"):
        print(f"Wrote: {safe_rel(paths[key])}")


if __name__ == "__main__":
    main()
