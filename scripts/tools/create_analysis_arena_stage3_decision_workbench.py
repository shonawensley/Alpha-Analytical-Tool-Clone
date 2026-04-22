#!/usr/bin/env python3
"""Create the Stage-3 Analysis Arena decision workbench.

Stage 3 is a read-only decision layer. It turns Stage-2/Stage-2B audit
artifacts into promotion, replay, restraint, decay, and readiness outputs
without changing live scoring, candidate generation, budgeting, or legacy
pipeline behavior.
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
FINAL_DOCS_DIR = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "final docs"
WINDOW_RE = re.compile(r"^WINDOW_\d{4}-\d{2}-\d{2}_to_\d{4}-\d{2}-\d{2}$")
TRUTHY = {"1", "true", "yes", "y", "True"}
BOXED_STATUSES = {"cross_window_boxed_translator_candidate", "cross_window_boxed_support_gate"}
WATCH_STATUSES = {"cross_window_vtrac_watch_only", "watch_or_fixture_only"}


def _parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--runs2-dir", default=str(RUNS_2_DIR), help="RUNS_2 root containing completed window folders.")
    ap.add_argument("--output-dir", default=str(RUNS_2_DIR), help="Cycle-level output directory.")
    ap.add_argument(
        "--window-root",
        action="append",
        default=[],
        help="Explicit completed window root to include. Can be repeated; when provided, RUNS_2 auto-discovery is bypassed.",
    )
    ap.add_argument(
        "--focus-window",
        default="",
        help="Window folder to use for the casebook. Defaults to the newest window with priority cases.",
    )
    ap.add_argument("--force", action="store_true", help="Overwrite existing Stage-3 outputs.")
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


def _split_pipe(value: Any) -> List[str]:
    return [part.strip() for part in str(value or "").split("|") if part.strip()]


def _source_family(source_key: str) -> str:
    return source_key.split(":", 1)[0] if ":" in source_key else source_key


def _truthy(value: Any) -> bool:
    return str(value or "").strip() in TRUTHY or str(value or "").strip().lower() in TRUTHY


def _counter_text(counter: Counter[str]) -> str:
    return "|".join(f"{key}:{count}" for key, count in counter.most_common() if key)


def _discover_windows(runs2_dir: Path, explicit_window_roots: Sequence[str] | None = None) -> List[Path]:
    if explicit_window_roots:
        windows: List[Path] = []
        seen: set[Path] = set()
        for value in explicit_window_roots:
            window = _resolve_path(value)
            if not window.is_dir():
                raise SystemExit(f"Explicit window root not found: {window}")
            resolved = window.resolve()
            if resolved in seen:
                continue
            seen.add(resolved)
            windows.append(window)
        return sorted(windows, key=lambda path: path.name)

    return sorted(path for path in runs2_dir.iterdir() if path.is_dir() and WINDOW_RE.match(path.name))


def _prefix(window: Path) -> str:
    return f"{window.name}__ANALYSIS_ARENA"


def _window_paths(window: Path) -> Dict[str, Path]:
    stem = _prefix(window)
    return {
        "priority_cases": window / f"{stem}__AUDIT_INTERPRETATION_PRIORITY_CASES.csv",
        "utilization_csv": window / f"{stem}__EVIDENCE_UTILIZATION_LEDGER.csv",
        "attribution_csv": window / f"{stem}__WINNER_SIGNAL_ATTRIBUTION_LEDGER.csv",
        "audit_json": window / f"{stem}__EVIDENCE_UTILIZATION_AUDIT.json",
        "decay_json": window / f"{stem}__DECAY_CARRYOVER_SCORECARD.json",
        "decay_rows": window / f"{stem}__DECAY_CARRYOVER_ROWS.csv",
        "casebook_md": window / f"{stem}__STAGE3_CASEBOOK.md",
        "casebook_csv": window / f"{stem}__STAGE3_CASEBOOK.csv",
    }


def _cycle_paths(output_dir: Path) -> Dict[str, Path]:
    prefix = "ANALYSIS_ARENA__CYCLE__STAGE3"
    return {
        "md": output_dir / f"{prefix}_DECISION_WORKBENCH.md",
        "json": output_dir / f"{prefix}_DECISION_WORKBENCH.json",
        "registry_csv": output_dir / f"{prefix}_PROMOTION_REGISTRY.csv",
        "replay_csv": output_dir / f"{prefix}_REPLAY_QUEUE.csv",
        "negative_csv": output_dir / f"{prefix}_NEGATIVE_CONTROL_MAP.csv",
        "evidence_csv": output_dir / f"{prefix}_EVIDENCE_UTILIZATION_MATRIX.csv",
        "decay_csv": output_dir / f"{prefix}_DECAY_STRATIFICATION.csv",
        "readiness_md": output_dir / f"{prefix}_FRESH_WINDOW_DECISION_READINESS.md",
    }


def _load_cross_window(runs2_dir: Path) -> Dict[str, Any]:
    json_path = runs2_dir / "ANALYSIS_ARENA__CYCLE__STAGE2B_CROSS_WINDOW_STACK_ROLLUP.json"
    if json_path.exists():
        return _read_json(json_path)
    return {
        "stack_rows": _read_csv_rows(runs2_dir / "ANALYSIS_ARENA__CYCLE__STAGE2B_CROSS_WINDOW_STACK_CONFIRMATION.csv"),
        "source_rows": _read_csv_rows(runs2_dir / "ANALYSIS_ARENA__CYCLE__STAGE2B_CROSS_WINDOW_SOURCE_CONFIRMATION.csv"),
        "hypothesis_rows": _read_csv_rows(runs2_dir / "ANALYSIS_ARENA__CYCLE__STAGE2B_CROSS_WINDOW_HYPOTHESIS_CONFIRMATION.csv"),
        "windows": [],
    }


def _choose_focus_window(windows: Sequence[Path], explicit: str) -> Path | None:
    if explicit:
        path = _resolve_path(explicit)
        if path.is_dir():
            return path
        candidate = RUNS_2_DIR / explicit
        if candidate.is_dir():
            return candidate
        raise SystemExit(f"Focus window not found: {explicit}")
    eligible = [window for window in windows if _window_paths(window)["priority_cases"].exists()]
    return eligible[-1] if eligible else (windows[-1] if windows else None)


def _stack_decision(row: Dict[str, Any]) -> Tuple[str, str, str, int]:
    status = str(row.get("cross_window_status") or "")
    pair_scope = str(row.get("pair_scope") or "")
    windows_seen = _safe_int(row.get("windows_seen"))
    avg_pool = _safe_float(row.get("avg_overlap_values_per_state_day"))
    match_rate = _safe_float(row.get("weighted_match_rate"))
    event_support = _safe_float(row.get("weighted_supported_event_rate"))
    fp_rate = _safe_float(row.get("false_positive_proxy_rate"))
    positive = _safe_int(row.get("positive_conversion_event_count"))
    gap = _safe_int(row.get("gap_teacher_event_count"))
    wrong = _safe_int(row.get("wrong_lane_event_count"))

    if status == "cross_window_boxed_translator_candidate":
        if wrong > positive + gap:
            return "blocked_wrong_lane", "boxed", "Repeated boxed stack, but wrong-lane count exceeds positive/gap evidence.", 4
        return "promote_candidate", "boxed", "Eligible for fixture replay as a boxed translator candidate; live scoring remains blocked.", 1
    if status == "cross_window_boxed_support_gate":
        return "supporting_gate", "boxed", "Useful as a paired support gate; replay before any weight promotion.", 2
    if status == "cross_window_vtrac_watch_only" or pair_scope.startswith("vtrac"):
        return "watch_decay_only", "vtrac", "Repeated VTRAC/territory behavior; keep in decay/watch lane until boxed/exact proof appears.", 3
    if status == "recurring_negative_control" or (fp_rate >= 0.94 and match_rate <= 0.011 and windows_seen >= 3):
        return "negative_control", pair_scope.replace("_overlap", "") or "context", "Repeated broad/low-conversion exposure; use as restraint.", 5
    if status == "cross_window_low_denominator_fixture":
        return "blocked_low_denominator", pair_scope.replace("_overlap", "") or "fixture", "Recurring but denominator is too thin for promotion; preserve as fixture only.", 4
    if windows_seen < 2:
        return "needs_more_windows", pair_scope.replace("_overlap", "") or "context", "Single-window only; not enough repeatability.", 6
    if event_support > 0 and avg_pool <= 3.0:
        return "needs_replay", pair_scope.replace("_overlap", "") or "context", "Potentially useful but not sharp enough for promotion.", 4
    return "fixture_only", pair_scope.replace("_overlap", "") or "context", "Keep for manual review and future denominator checks.", 5


def _source_decision(row: Dict[str, Any]) -> Tuple[str, str, str, int]:
    lane = str(row.get("target_lane") or "context")
    windows_seen = _safe_int(row.get("windows_seen"))
    exposure = _safe_int(row.get("total_exposure_values"))
    support = _safe_float(row.get("weighted_winner_event_support_rate"))
    lane_rate = _safe_float(row.get("weighted_lane_hit_value_rate"))
    fp_rate = _safe_float(row.get("false_positive_proxy_rate"))
    decisions = str(row.get("decision_mix") or "")
    if "denominator_only_broad_control" in decisions or (exposure >= 10000 and fp_rate >= 0.94 and lane_rate <= 0.005):
        return "negative_control", lane, "Stable broad denominator/control source; useful for restraint, not promotion.", 5
    if lane == "vtrac":
        return "watch_decay_only", lane, "Stable VTRAC source; use as territory/decay context unless a bounded boxed partner confirms it.", 3
    if "negative" in decisions and fp_rate >= 0.94:
        return "negative_control", lane, "Stable source has negative-control behavior; use as restraint.", 5
    if windows_seen >= 3 and lane in {"boxed", "box"} and support >= 0.005 and lane_rate >= 0.01:
        return "supporting_gate", "boxed", "Cross-window boxed source support is useful as a gate, not a standalone scorer.", 2
    if windows_seen >= 3 and lane in {"straight", "exact"} and support >= 0.003:
        return "supporting_gate", "straight", "Cross-window exact/straight source support is fixture material; replay before promotion.", 2
    if windows_seen >= 2 and fp_rate >= 0.98 and lane_rate <= 0.01:
        return "negative_control", lane, "Repeated exposure has weak conversion and high false proxy.", 5
    return "needs_replay", lane, "Insufficient direct permission for promotion; keep in replay/diagnostic queue.", 4


def _evidence_strength(windows_seen: int, role: str, event_support: float, match_rate: float, avg_pool: float) -> str:
    if role in {"promote_candidate", "supporting_gate"} and windows_seen >= 5 and event_support >= 0.005 and avg_pool <= 3.0:
        return "high_replay_value"
    if role in {"promote_candidate", "supporting_gate", "watch_decay_only"} and windows_seen >= 3:
        return "medium_replay_value"
    if role in {"negative_control", "blocked_low_denominator", "blocked_wrong_lane"}:
        return "restraint_value"
    if match_rate > 0 or event_support > 0:
        return "low_replay_value"
    return "context_only"


def _build_promotion_registry(cross: Dict[str, Any]) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for row in cross.get("stack_rows") or []:
        role, lane, rationale, priority = _stack_decision(row)
        windows_seen = _safe_int(row.get("windows_seen"))
        avg_pool = _safe_float(row.get("avg_overlap_values_per_state_day"))
        match_rate = _safe_float(row.get("weighted_match_rate"))
        event_support = _safe_float(row.get("weighted_supported_event_rate"))
        rows.append(
            {
                "entity_type": "stack",
                "entity_key": row.get("pair_key", ""),
                "decision_role": role,
                "lane": lane,
                "replay_priority": priority,
                "evidence_strength": _evidence_strength(windows_seen, role, event_support, match_rate, avg_pool),
                "direct_scoring_permission": "blocked",
                "allowed_use": _allowed_use(role),
                "windows_seen": windows_seen,
                "windows": row.get("windows", ""),
                "pool_or_exposure_size": row.get("avg_overlap_values_per_state_day", ""),
                "match_rate": match_rate,
                "event_support_rate": event_support,
                "false_positive_proxy_rate": row.get("false_positive_proxy_rate", ""),
                "positive_conversion_event_count": row.get("positive_conversion_event_count", ""),
                "gap_teacher_event_count": row.get("gap_teacher_event_count", ""),
                "wrong_lane_event_count": row.get("wrong_lane_event_count", ""),
                "source_family": f"{_source_family(str(row.get('source_a') or ''))}|{_source_family(str(row.get('source_b') or ''))}",
                "source_a": row.get("source_a", ""),
                "source_b": row.get("source_b", ""),
                "stage2_status": row.get("cross_window_status", ""),
                "rationale": rationale,
            }
        )
    for row in cross.get("source_rows") or []:
        role, lane, rationale, priority = _source_decision(row)
        windows_seen = _safe_int(row.get("windows_seen"))
        lane_rate = _safe_float(row.get("weighted_lane_hit_value_rate"))
        support = _safe_float(row.get("weighted_winner_event_support_rate"))
        rows.append(
            {
                "entity_type": "source",
                "entity_key": row.get("source_key", ""),
                "decision_role": role,
                "lane": lane,
                "replay_priority": priority,
                "evidence_strength": _evidence_strength(
                    windows_seen,
                    role,
                    support,
                    lane_rate,
                    _safe_float(row.get("total_exposure_values")),
                ),
                "direct_scoring_permission": "blocked",
                "allowed_use": _allowed_use(role),
                "windows_seen": windows_seen,
                "windows": row.get("windows", ""),
                "pool_or_exposure_size": row.get("total_exposure_values", ""),
                "match_rate": lane_rate,
                "event_support_rate": support,
                "false_positive_proxy_rate": row.get("false_positive_proxy_rate", ""),
                "positive_conversion_event_count": "",
                "gap_teacher_event_count": "",
                "wrong_lane_event_count": "",
                "source_family": row.get("source_family", ""),
                "source_a": row.get("source_key", ""),
                "source_b": "",
                "stage2_status": row.get("decision_mix", ""),
                "rationale": rationale,
            }
        )
    rows.sort(
        key=lambda row: (
            _safe_int(row.get("replay_priority")),
            -_safe_int(row.get("windows_seen")),
            -_safe_float(row.get("event_support_rate")),
            -_safe_float(row.get("match_rate")),
            str(row.get("entity_key") or ""),
        )
    )
    return rows


def _allowed_use(role: str) -> str:
    return {
        "promote_candidate": "fixture_replay_and_manual_translator_design",
        "supporting_gate": "paired_gate_replay_only",
        "watch_decay_only": "decay_watch_and_context_only",
        "negative_control": "restraint_and_penalty_design",
        "blocked_low_denominator": "fixture_only_until_more_denominator",
        "blocked_wrong_lane": "restraint_teacher",
        "needs_more_windows": "collect_more_windows",
        "needs_replay": "diagnostic_replay",
        "fixture_only": "manual_fixture_review",
    }.get(role, "diagnostic_review")


def _build_replay_queue(registry: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for row in registry:
        role = str(row.get("decision_role") or "")
        if role not in {"promote_candidate", "supporting_gate", "watch_decay_only", "blocked_low_denominator", "needs_replay"}:
            continue
        if role == "watch_decay_only" and len([r for r in rows if r.get("replay_lane") == "vtrac_decay_watch"]) >= 40:
            continue
        queue = {
            "promote_candidate": "P1_boxed_translator_replay",
            "supporting_gate": "P2_support_gate_replay",
            "watch_decay_only": "P3_vtrac_decay_watch_replay",
            "blocked_low_denominator": "P4_low_denominator_fixture_replay",
            "needs_replay": "P4_diagnostic_replay",
        }.get(role, "P5_review")
        rows.append(
            {
                "queue_id": f"STAGE3-RQ-{len(rows) + 1:04d}",
                "queue": queue,
                "entity_type": row.get("entity_type", ""),
                "entity_key": row.get("entity_key", ""),
                "replay_lane": "vtrac_decay_watch" if role == "watch_decay_only" else row.get("lane", ""),
                "windows_seen": row.get("windows_seen", ""),
                "evidence_strength": row.get("evidence_strength", ""),
                "pool_or_exposure_size": row.get("pool_or_exposure_size", ""),
                "match_rate": row.get("match_rate", ""),
                "event_support_rate": row.get("event_support_rate", ""),
                "false_positive_proxy_rate": row.get("false_positive_proxy_rate", ""),
                "must_not_change_live_scoring": "yes",
                "test_goal": _replay_goal(role),
                "success_condition": _success_condition(role),
                "guardrail": row.get("rationale", ""),
            }
        )
    rows.sort(
        key=lambda row: (
            str(row.get("queue") or ""),
            -_safe_int(row.get("windows_seen")),
            -_safe_float(row.get("event_support_rate")),
            -_safe_float(row.get("match_rate")),
            str(row.get("entity_key") or ""),
        )
    )
    return rows


def _replay_goal(role: str) -> str:
    if role == "promote_candidate":
        return "Replay as bounded boxed translator rule against completed windows."
    if role == "supporting_gate":
        return "Replay as paired gate and measure whether it improves precision without broadening pool size."
    if role == "watch_decay_only":
        return "Replay as carryforward/context signal, not spendable boxed/straight expression."
    if role == "blocked_low_denominator":
        return "Keep as fixture until more events prove denominator stability."
    return "Replay diagnostically before any scoring consideration."


def _success_condition(role: str) -> str:
    if role == "promote_candidate":
        return "Maintains cross-window box support with bounded pool and no wrong-lane inflation."
    if role == "supporting_gate":
        return "Improves candidate filtering when paired with sharp boxed/exact evidence."
    if role == "watch_decay_only":
        return "Explains delayed territory resolution without causing boxed/straight over-promotion."
    if role == "blocked_low_denominator":
        return "Gains enough denominator to leave fixture-only status."
    return "Produces repeatable lift without becoming a recurring negative control."


def _build_negative_control_map(registry: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for row in registry:
        role = str(row.get("decision_role") or "")
        fp_rate = _safe_float(row.get("false_positive_proxy_rate"))
        if role not in {"negative_control", "blocked_wrong_lane"} and fp_rate < 0.98:
            continue
        rows.append(
            {
                "control_id": f"STAGE3-NC-{len(rows) + 1:04d}",
                "entity_type": row.get("entity_type", ""),
                "entity_key": row.get("entity_key", ""),
                "decision_role": role,
                "lane": row.get("lane", ""),
                "windows_seen": row.get("windows_seen", ""),
                "false_positive_proxy_rate": row.get("false_positive_proxy_rate", ""),
                "match_rate": row.get("match_rate", ""),
                "event_support_rate": row.get("event_support_rate", ""),
                "wrong_lane_event_count": row.get("wrong_lane_event_count", ""),
                "restraint_use": "Do not promote directly; use to design penalties, gates, and wrong-lane blocks.",
                "rationale": row.get("rationale", ""),
            }
        )
    rows.sort(
        key=lambda row: (
            row.get("decision_role") != "negative_control",
            -_safe_int(row.get("windows_seen")),
            -_safe_float(row.get("false_positive_proxy_rate")),
            str(row.get("entity_key") or ""),
        )
    )
    for idx, row in enumerate(rows, start=1):
        row["control_id"] = f"STAGE3-NC-{idx:04d}"
    return rows


def _event_id(row: Dict[str, Any]) -> str:
    return str(row.get("event_id") or f"{row.get('date', '')}|{row.get('state_key', '')}|{row.get('period', '')}|{row.get('winner', '')}")


def _build_evidence_utilization_matrix(focus_window: Path | None, cross: Dict[str, Any]) -> List[Dict[str, Any]]:
    family_rows: Dict[str, Dict[str, Any]] = {}
    if focus_window:
        paths = _window_paths(focus_window)
        util_rows = _read_csv_rows(paths["utilization_csv"])
        attr_rows = _read_csv_rows(paths["attribution_csv"])
        util_by_event = {_event_id(row): row for row in util_rows}
        for row in attr_rows:
            family = str(row.get("source_family") or "")
            if not family:
                continue
            event = util_by_event.get(str(row.get("event_id") or ""), {})
            entry = family_rows.setdefault(
                family,
                {
                    "source_family": family,
                    "focus_window": focus_window.name,
                    "attribution_rows": 0,
                    "unique_events": set(),
                    "pre_draw_rows": 0,
                    "post_result_rows": 0,
                    "exact_match_rows": 0,
                    "box_match_rows": 0,
                    "vtrac_match_rows": 0,
                    "captured_and_used_events": set(),
                    "captured_but_underused_events": set(),
                    "captured_but_wrong_lane_events": set(),
                    "captured_but_not_promoted_events": set(),
                    "decay_validated_events": set(),
                    "outcome_counter": Counter(),
                    "promoted_stage_counter": Counter(),
                },
            )
            event_id = str(row.get("event_id") or "")
            entry["attribution_rows"] += 1
            entry["unique_events"].add(event_id)
            if _truthy(row.get("pre_draw_available")):
                entry["pre_draw_rows"] += 1
            else:
                entry["post_result_rows"] += 1
            if _truthy(row.get("match_exact")):
                entry["exact_match_rows"] += 1
            if _truthy(row.get("match_box")):
                entry["box_match_rows"] += 1
            if _truthy(row.get("match_vtrac_straight")) or _truthy(row.get("match_vtrac_box")):
                entry["vtrac_match_rows"] += 1
            status = str(event.get("evidence_status") or "")
            outcome = str(event.get("outcome_class") or "")
            entry["outcome_counter"][outcome] += 1
            entry["promoted_stage_counter"][str(row.get("promoted_stage") or "")] += 1
            if status == "CAPTURED_AND_USED":
                entry["captured_and_used_events"].add(event_id)
            elif status == "CAPTURED_BUT_UNDERUSED":
                entry["captured_but_underused_events"].add(event_id)
            elif status == "CAPTURED_BUT_WRONG_LANE":
                entry["captured_but_wrong_lane_events"].add(event_id)
            elif status == "CAPTURED_BUT_NOT_PROMOTED":
                entry["captured_but_not_promoted_events"].add(event_id)
            elif status == "DECAY_VALIDATED":
                entry["decay_validated_events"].add(event_id)

    cross_family: Dict[str, Dict[str, Any]] = defaultdict(lambda: {"sources": 0, "windows_seen_max": 0, "support": 0.0, "lane_rate": 0.0})
    for row in cross.get("source_rows") or []:
        family = str(row.get("source_family") or _source_family(str(row.get("source_key") or "")))
        bucket = cross_family[family]
        bucket["sources"] += 1
        bucket["windows_seen_max"] = max(_safe_int(bucket["windows_seen_max"]), _safe_int(row.get("windows_seen")))
        bucket["support"] += _safe_float(row.get("weighted_winner_event_support_rate"))
        bucket["lane_rate"] += _safe_float(row.get("weighted_lane_hit_value_rate"))

    for family in cross_family:
        family_rows.setdefault(
            family,
            {
                "source_family": family,
                "focus_window": focus_window.name if focus_window else "",
                "attribution_rows": 0,
                "unique_events": set(),
                "pre_draw_rows": 0,
                "post_result_rows": 0,
                "exact_match_rows": 0,
                "box_match_rows": 0,
                "vtrac_match_rows": 0,
                "captured_and_used_events": set(),
                "captured_but_underused_events": set(),
                "captured_but_wrong_lane_events": set(),
                "captured_but_not_promoted_events": set(),
                "decay_validated_events": set(),
                "outcome_counter": Counter(),
                "promoted_stage_counter": Counter(),
            },
        )

    out: List[Dict[str, Any]] = []
    for family, entry in family_rows.items():
        cross_info = cross_family.get(family, {})
        unique_events = len(entry["unique_events"])
        underused = len(entry["captured_but_underused_events"])
        wrong = len(entry["captured_but_wrong_lane_events"])
        used = len(entry["captured_and_used_events"])
        not_promoted = len(entry["captured_but_not_promoted_events"])
        decay = len(entry["decay_validated_events"])
        role = _family_decision_role(family, used, underused, wrong, not_promoted, decay, cross_info)
        out.append(
            {
                "source_family": family,
                "focus_window": entry["focus_window"],
                "attribution_rows": entry["attribution_rows"],
                "unique_winner_events": unique_events,
                "pre_draw_rows": entry["pre_draw_rows"],
                "post_result_rows": entry["post_result_rows"],
                "exact_match_rows": entry["exact_match_rows"],
                "box_match_rows": entry["box_match_rows"],
                "vtrac_match_rows": entry["vtrac_match_rows"],
                "captured_and_used_events": used,
                "captured_but_underused_events": underused,
                "captured_but_wrong_lane_events": wrong,
                "captured_but_not_promoted_events": not_promoted,
                "decay_validated_events": decay,
                "cross_window_source_count": cross_info.get("sources", 0),
                "cross_window_max_windows_seen": cross_info.get("windows_seen_max", 0),
                "cross_window_avg_support_rate": _rate(_safe_float(cross_info.get("support")), _safe_int(cross_info.get("sources"))),
                "cross_window_avg_lane_rate": _rate(_safe_float(cross_info.get("lane_rate")), _safe_int(cross_info.get("sources"))),
                "outcome_mix": _counter_text(entry["outcome_counter"]),
                "promoted_stage_mix": _counter_text(entry["promoted_stage_counter"]),
                "stage3_decision_role": role,
                "read": _family_read(family, role),
            }
        )
    out.sort(
        key=lambda row: (
            row.get("stage3_decision_role") not in {"translator_teaching_surface", "support_gate_surface"},
            -_safe_int(row.get("captured_but_underused_events")),
            -_safe_int(row.get("captured_and_used_events")),
            -_safe_int(row.get("unique_winner_events")),
            str(row.get("source_family") or ""),
        )
    )
    return out


def _family_decision_role(
    family: str,
    used: int,
    underused: int,
    wrong: int,
    not_promoted: int,
    decay: int,
    cross_info: Dict[str, Any],
) -> str:
    if family in {"translation_sandbox", "arena", "brain1"} and underused > 0:
        return "translator_teaching_surface"
    if family in {"board_scoreboard", "old_candidate_universe"} and wrong >= used:
        return "restraint_or_denominator_surface"
    if family in {"tracker", "frontier"} and wrong > used + underused:
        return "context_requires_gate"
    if decay > used and family in {"brain1", "arena", "translation_sandbox", "board_scoreboard"}:
        return "decay_watch_surface"
    if _safe_int(cross_info.get("windows_seen_max")) >= 3:
        return "support_gate_surface"
    if not_promoted > used:
        return "hypothesis_probe_surface"
    return "diagnostic_surface"


def _family_read(family: str, role: str) -> str:
    if role == "translator_teaching_surface":
        return "High-value teaching surface for boxed/straight expression; keep scoring blocked until replay."
    if role == "restraint_or_denominator_surface":
        return "Useful denominator/control surface; do not trust as direct candidate expression."
    if role == "context_requires_gate":
        return "Context is useful but must be gated by sharper exact/boxed/frontier evidence."
    if role == "decay_watch_surface":
        return "Useful for carryforward/watch behavior; separate from same-day spendable candidate logic."
    if role == "support_gate_surface":
        return "Cross-window evidence supports gate/replay use, not standalone promotion."
    if family == "old_play_card":
        return "Downstream baseline; use for old-vs-Arena expression comparisons."
    return "Diagnostic source; retain in matrix until replay proves a sharper role."


def _metric_lane(metric: str) -> str:
    tokens = {part for part in metric.split("_") if part}
    if "exact" in tokens or "straight" in tokens:
        return "straight"
    if "vt" in tokens or "vtrac" in tokens:
        return "vtrac"
    if "box" in tokens or "boxed" in tokens:
        return "boxed"
    return "context"


def _metric_family(metric: str) -> str:
    if metric.startswith("board_"):
        return "board_scoreboard"
    if metric.startswith("brain1_"):
        return "brain1"
    if metric.startswith("sandbox_"):
        return "translation_sandbox"
    if metric.startswith("arena_"):
        return "arena"
    if metric.startswith("preserved_"):
        return "control_arm"
    return "arena"


def _build_decay_stratification(windows: Sequence[Path]) -> List[Dict[str, Any]]:
    grouped: Dict[str, Dict[str, Any]] = {}
    for window in windows:
        decay_json = _read_json(_window_paths(window)["decay_json"])
        for row in decay_json.get("metric_families") or []:
            metric = str(row.get("metric_family") or "")
            if not metric:
                continue
            entry = grouped.setdefault(
                metric,
                {
                    "metric_family": metric,
                    "source_family": _metric_family(metric),
                    "lane": _metric_lane(metric),
                    "windows": set(),
                    "active_state_days": 0,
                    "same_day_resolved": 0,
                    "horizon_resolved": 0,
                    "incremental_decay_lift": 0,
                    "profile_counter": Counter(),
                    "right_censored": 0,
                },
            )
            entry["windows"].add(window.name)
            entry["active_state_days"] += _safe_int(row.get("active_state_days") or row.get("state_days"))
            entry["same_day_resolved"] += _safe_int(row.get("same_day_resolved"))
            entry["horizon_resolved"] += _safe_int(row.get("horizon_resolved"))
            entry["incremental_decay_lift"] += _safe_int(row.get("incremental_decay_lift"))
            for key, value in (row.get("profile_counts") or {}).items():
                entry["profile_counter"][str(key)] += _safe_int(value)
            entry["right_censored"] += _safe_int((row.get("profile_counts") or {}).get("right_censored"))

    out: List[Dict[str, Any]] = []
    for entry in grouped.values():
        active = _safe_int(entry["active_state_days"])
        horizon = _safe_int(entry["horizon_resolved"])
        same = _safe_int(entry["same_day_resolved"])
        lane = str(entry["lane"])
        out.append(
            {
                "metric_family": entry["metric_family"],
                "source_family": entry["source_family"],
                "lane": lane,
                "windows_seen": len(entry["windows"]),
                "windows": "|".join(sorted(entry["windows"])),
                "active_state_days": active,
                "same_day_resolved": same,
                "same_day_rate": _rate(same, active),
                "horizon_resolved": horizon,
                "horizon_rate": _rate(horizon, active),
                "incremental_decay_lift": entry["incremental_decay_lift"],
                "incremental_decay_rate": _rate(max(0, horizon - same), active),
                "profile_mix": _counter_text(entry["profile_counter"]),
                "right_censored_rows": entry["right_censored"],
                "stage3_decay_role": _decay_role(lane, _rate(same, active), _rate(horizon, active)),
                "read": _decay_read(lane),
            }
        )
    out.sort(
        key=lambda row: (
            row.get("lane") != "boxed",
            -_safe_float(row.get("incremental_decay_rate")),
            -_safe_float(row.get("horizon_rate")),
            str(row.get("metric_family") or ""),
        )
    )
    return out


def _decay_role(lane: str, same_rate: float, horizon_rate: float) -> str:
    lift = max(0.0, horizon_rate - same_rate)
    if lane == "vtrac" and horizon_rate >= 0.5:
        return "territory_decay_watch"
    if lane == "boxed" and lift >= 0.05:
        return "boxed_carryforward_teacher"
    if lane == "straight" and horizon_rate > 0:
        return "straight_precision_probe"
    if lift > 0:
        return "carryforward_context"
    return "same_day_or_miss_context"


def _decay_read(lane: str) -> str:
    if lane == "vtrac":
        return "VTRAC decay may be strong, but remains watch/context until paired with bounded box or exact proof."
    if lane == "boxed":
        return "Boxed decay can teach carryforward behavior, but replay must control pool size."
    if lane == "straight":
        return "Straight decay is precision-sensitive; treat as fixture/probe only."
    return "Context decay; use for interpretation, not direct spend."


def _top_sources_for_event(attr_rows: Sequence[Dict[str, str]], event_id: str, match_field: str, limit: int = 8) -> str:
    counter: Counter[str] = Counter()
    for row in attr_rows:
        if str(row.get("event_id") or "") != event_id:
            continue
        if _truthy(row.get(match_field)):
            counter[f"{row.get('source_family')}:{row.get('source_tool')}"] += 1
    return "|".join(f"{key} x{count}" for key, count in counter.most_common(limit))


def _case_lesson(row: Dict[str, str]) -> Tuple[str, str]:
    cohort = str(row.get("fixture_cohort") or "")
    if cohort == "gap_teacher":
        return "translator_gap_teacher", "Evidence existed but downstream expression underused it; replay boxed/straight translator rules."
    if cohort == "positive_conversion":
        return "positive_regression_anchor", "Preserve as a regression positive for future translator changes."
    if cohort == "wrong_lane_vtrac":
        return "wrong_lane_restraint_teacher", "Do not spend broad VTRAC/territory evidence without sharper boxed/exact confirmation."
    if cohort == "decay_teacher":
        return "carryforward_teacher", "Treat as delayed-resolution evidence instead of a same-day miss."
    if cohort == "not_promoted_probe":
        return "hypothesis_probe", "Captured evidence needs replay before promotion."
    return "manual_review", "Review manually before use."


def _build_casebook(focus_window: Path | None) -> Tuple[List[Dict[str, Any]], str]:
    if focus_window is None:
        return [], ""
    paths = _window_paths(focus_window)
    priority_rows = _read_csv_rows(paths["priority_cases"])
    attr_rows = _read_csv_rows(paths["attribution_csv"])
    if not priority_rows:
        return [], ""
    rows: List[Dict[str, Any]] = []
    for row in priority_rows:
        event_id = _event_id(row)
        lesson, lesson_read = _case_lesson(row)
        rows.append(
            {
                "event_id": event_id,
                "fixture_cohort": row.get("fixture_cohort", ""),
                "stage3_lesson": lesson,
                "priority": row.get("priority", ""),
                "date": row.get("date", ""),
                "state_key": row.get("state_key", ""),
                "period": row.get("period", ""),
                "winner": row.get("winner", ""),
                "outcome_class": row.get("outcome_class", ""),
                "evidence_status": row.get("evidence_status", ""),
                "board_rank": row.get("board_rank", ""),
                "sharp_signal_count": row.get("sharp_signal_count", ""),
                "territory_signal_count": row.get("territory_signal_count", ""),
                "box_source_count": row.get("box_source_count", ""),
                "exact_source_count": row.get("exact_source_count", ""),
                "vtrac_source_count": row.get("vtrac_source_count", ""),
                "frontier_signature_type": row.get("frontier_signature_type", ""),
                "frontier_signature_strength": row.get("frontier_signature_strength", ""),
                "decay_any_profile": row.get("decay_any_profile", ""),
                "top_exact_sources": _top_sources_for_event(attr_rows, event_id, "match_exact"),
                "top_box_sources": _top_sources_for_event(attr_rows, event_id, "match_box"),
                "top_vtrac_sources": _top_sources_for_event(attr_rows, event_id, "match_vtrac_box"),
                "recommended_use": lesson_read,
                "guardrail": "Fixture/replay use only; no direct live scoring change.",
            }
        )
    rows.sort(key=lambda row: (_safe_int(row.get("priority")), str(row.get("date")), str(row.get("state_key")), str(row.get("period"))))
    return rows, _render_casebook_md(focus_window, rows, paths)


def _render_casebook_md(focus_window: Path, rows: Sequence[Dict[str, Any]], paths: Dict[str, Path]) -> str:
    cohort_counts = Counter(str(row.get("fixture_cohort") or "") for row in rows)
    lines = [
        "# Stage 3 March Casebook",
        "",
        "Purpose: convert priority March examples into reusable translator, replay, restraint, and decay lessons.",
        "",
        "## Guardrail",
        "",
        "- These cases are teaching fixtures, not live scoring changes.",
        "- Positive cases protect future translator changes from regression.",
        "- Gap and wrong-lane cases define what the future expression layer should promote or restrain.",
        "",
        "## Cohort Mix",
        "",
    ]
    for key, count in cohort_counts.most_common():
        lines.append(f"- `{key}`: `{count}`")
    lines.extend(["", "## Highest-Value Cases", ""])
    for row in rows[:40]:
        lines.append(
            "- "
            f"`{row.get('date')}` `{row.get('state_key')}` `{row.get('period')}` winner=`{row.get('winner')}` "
            f"cohort=`{row.get('fixture_cohort')}` outcome=`{row.get('outcome_class')}` "
            f"rank=`{row.get('board_rank')}` sharp=`{row.get('sharp_signal_count')}` "
            f"lesson=`{row.get('stage3_lesson')}`"
        )
    lines.extend(
        [
            "",
            "## Generated Files",
            "",
            f"- Casebook CSV: `{safe_rel(paths['casebook_csv'])}`",
            "",
        ]
    )
    return "\n".join(lines)


def _render_readiness_md(
    *,
    registry: Sequence[Dict[str, Any]],
    replay_rows: Sequence[Dict[str, Any]],
    negative_rows: Sequence[Dict[str, Any]],
    evidence_rows: Sequence[Dict[str, Any]],
    decay_rows: Sequence[Dict[str, Any]],
    paths: Dict[str, Path],
) -> str:
    decision_counts = Counter(str(row.get("decision_role") or "") for row in registry)
    lines = [
        "# Stage 3 Fresh-Window Decision Readiness",
        "",
        "Purpose: lock how Stage-3 evidence should be used before the next fresh window.",
        "",
        "## Permission Model",
        "",
        "- Approved now: observation, replay, casebook review, decay/watch interpretation, negative-control restraint.",
        "- Blocked now: live scoring changes, live budget changes, automatic candidate promotion.",
        "- Required before scoring rewrite: replay candidates must survive cross-window fixture replay with denominator controls.",
        "",
        "## Decision Mix",
        "",
    ]
    for key, count in decision_counts.most_common():
        lines.append(f"- `{key}`: `{count}`")
    lines.extend(["", "## Highest Priority Replay", ""])
    for row in replay_rows[:20]:
        lines.append(
            "- "
            f"`{row.get('queue')}` `{row.get('entity_key')}` windows=`{row.get('windows_seen')}` "
            f"support=`{_pct(row.get('event_support_rate'))}` match=`{_pct(row.get('match_rate'))}`"
        )
    lines.extend(["", "## Highest Priority Restraints", ""])
    for row in negative_rows[:15]:
        lines.append(
            "- "
            f"`{row.get('entity_key')}` role=`{row.get('decision_role')}` windows=`{row.get('windows_seen')}` "
            f"false_proxy=`{_pct(row.get('false_positive_proxy_rate'))}`"
        )
    lines.extend(["", "## Evidence Families To Watch", ""])
    for row in evidence_rows[:12]:
        lines.append(
            "- "
            f"`{row.get('source_family')}` role=`{row.get('stage3_decision_role')}` "
            f"used=`{row.get('captured_and_used_events')}` underused=`{row.get('captured_but_underused_events')}` "
            f"wrong_lane=`{row.get('captured_but_wrong_lane_events')}`"
        )
    lines.extend(["", "## Decay Guardrail", ""])
    for row in decay_rows[:10]:
        lines.append(
            "- "
            f"`{row.get('metric_family')}` lane=`{row.get('lane')}` horizon=`{_pct(row.get('horizon_rate'))}` "
            f"incremental=`{_pct(row.get('incremental_decay_rate'))}` role=`{row.get('stage3_decay_role')}`"
        )
    lines.extend(
        [
            "",
            "## Files",
            "",
            f"- Decision workbench: `{safe_rel(paths['md'])}`",
            f"- Promotion registry: `{safe_rel(paths['registry_csv'])}`",
            f"- Replay queue: `{safe_rel(paths['replay_csv'])}`",
            f"- Negative-control map: `{safe_rel(paths['negative_csv'])}`",
            f"- Evidence-utilization matrix: `{safe_rel(paths['evidence_csv'])}`",
            f"- Decay stratification: `{safe_rel(paths['decay_csv'])}`",
            "",
        ]
    )
    return "\n".join(lines)


def _render_workbench_md(
    *,
    windows: Sequence[Path],
    focus_window: Path | None,
    registry: Sequence[Dict[str, Any]],
    replay_rows: Sequence[Dict[str, Any]],
    negative_rows: Sequence[Dict[str, Any]],
    evidence_rows: Sequence[Dict[str, Any]],
    decay_rows: Sequence[Dict[str, Any]],
    casebook_rows: Sequence[Dict[str, Any]],
    paths: Dict[str, Path],
    casebook_path: Path | None,
) -> str:
    role_counts = Counter(str(row.get("decision_role") or "") for row in registry)
    replay_counts = Counter(str(row.get("queue") or "") for row in replay_rows)
    lines = [
        "# Analysis Arena Stage 3 Decision Workbench",
        "",
        "Purpose: convert Stage-2/Stage-2B evidence into disciplined promotion, replay, restraint, and readiness decisions.",
        "",
        "## Executive Read",
        "",
        "- Stage 3 is a decision surface, not a live scoring surface.",
        "- Cross-window repeatability is now the main filter separating replay candidates from one-window noise.",
        "- VTRAC/territory strength remains valuable, but it is explicitly watch/decay unless paired with bounded boxed/exact proof.",
        "- Negative controls are promoted as restraint assets so future ranking/budget work learns what not to spend on.",
        "",
        "## Corpus",
        "",
        f"- Cross-window windows: `{len(windows)}`",
        f"- Focus casebook window: `{focus_window.name if focus_window else 'none'}`",
        f"- Registry rows: `{len(registry)}`",
        f"- Replay rows: `{len(replay_rows)}`",
        f"- Negative-control rows: `{len(negative_rows)}`",
        f"- Evidence-family rows: `{len(evidence_rows)}`",
        f"- Decay rows: `{len(decay_rows)}`",
        f"- Casebook rows: `{len(casebook_rows)}`",
        "",
        "## Decision Role Mix",
        "",
    ]
    for key, count in role_counts.most_common():
        lines.append(f"- `{key}`: `{count}`")
    lines.extend(["", "## Replay Queue Mix", ""])
    for key, count in replay_counts.most_common():
        lines.append(f"- `{key}`: `{count}`")
    lines.extend(["", "## Top Boxed Translator Candidates", ""])
    boxed = [row for row in registry if row.get("decision_role") == "promote_candidate"][:20]
    for row in boxed:
        lines.append(
            "- "
            f"`{row.get('entity_key')}` windows=`{row.get('windows_seen')}` "
            f"pool=`{_safe_float(row.get('pool_or_exposure_size')):.1f}` "
            f"match=`{_pct(row.get('match_rate'))}` support=`{_pct(row.get('event_support_rate'))}`"
        )
    if not boxed:
        lines.append("- None.")
    lines.extend(["", "## Top Support Gates", ""])
    support = [row for row in registry if row.get("decision_role") == "supporting_gate"][:20]
    for row in support:
        lines.append(
            "- "
            f"`{row.get('entity_key')}` windows=`{row.get('windows_seen')}` "
            f"match=`{_pct(row.get('match_rate'))}` support=`{_pct(row.get('event_support_rate'))}`"
        )
    if not support:
        lines.append("- None.")
    lines.extend(["", "## Top Watch/Decay Surfaces", ""])
    for row in [r for r in registry if r.get("decision_role") == "watch_decay_only"][:15]:
        lines.append(
            "- "
            f"`{row.get('entity_key')}` lane=`{row.get('lane')}` windows=`{row.get('windows_seen')}` "
            f"support=`{_pct(row.get('event_support_rate'))}`"
        )
    lines.extend(["", "## Top Negative Controls", ""])
    for row in negative_rows[:15]:
        lines.append(
            "- "
            f"`{row.get('entity_key')}` false_proxy=`{_pct(row.get('false_positive_proxy_rate'))}` "
            f"role=`{row.get('decision_role')}`"
        )
    lines.extend(["", "## Evidence Utilization Read", ""])
    for row in evidence_rows[:12]:
        lines.append(
            "- "
            f"`{row.get('source_family')}` -> `{row.get('stage3_decision_role')}`; "
            f"used `{row.get('captured_and_used_events')}`, underused `{row.get('captured_but_underused_events')}`, "
            f"wrong-lane `{row.get('captured_but_wrong_lane_events')}`, decay `{row.get('decay_validated_events')}`."
        )
    lines.extend(["", "## Generated Files", ""])
    for key in ("json", "registry_csv", "replay_csv", "negative_csv", "evidence_csv", "decay_csv", "readiness_md"):
        lines.append(f"- `{safe_rel(paths[key])}`")
    if casebook_path:
        lines.append(f"- `{safe_rel(casebook_path)}`")
    lines.extend(
        [
            "",
            "## Guardrail",
            "",
            "- This workbench grants replay and interpretation permission only. It does not grant live scoring, candidate-formation, or budget permission.",
            "",
        ]
    )
    return "\n".join(lines)


def build_workbench(
    runs2_dir: Path,
    output_dir: Path,
    focus_window_arg: str,
    explicit_window_roots: Sequence[str] | None = None,
) -> Tuple[Dict[str, Any], Dict[str, Path], Path | None]:
    windows = _discover_windows(runs2_dir, explicit_window_roots)
    cross = _load_cross_window(runs2_dir)
    focus_window = _choose_focus_window(windows, focus_window_arg)
    paths = _cycle_paths(output_dir)
    registry = _build_promotion_registry(cross)
    replay_rows = _build_replay_queue(registry)
    negative_rows = _build_negative_control_map(registry)
    evidence_rows = _build_evidence_utilization_matrix(focus_window, cross)
    decay_rows = _build_decay_stratification(windows)
    casebook_rows, casebook_md = _build_casebook(focus_window)
    casebook_path = None
    if focus_window and casebook_rows:
        casebook_path = _window_paths(focus_window)["casebook_md"]
    payload = {
        "schema_version": "analysis_arena_stage3_decision_workbench/v1",
        "runs2_dir": safe_rel(runs2_dir),
        "output_dir": safe_rel(output_dir),
        "windows": [window.name for window in windows],
        "focus_window": focus_window.name if focus_window else "",
        "decision_role_counts": dict(Counter(str(row.get("decision_role") or "") for row in registry).most_common()),
        "replay_queue_counts": dict(Counter(str(row.get("queue") or "") for row in replay_rows).most_common()),
        "registry_rows": registry,
        "replay_rows": replay_rows,
        "negative_control_rows": negative_rows,
        "evidence_utilization_rows": evidence_rows,
        "decay_stratification_rows": decay_rows,
        "casebook_rows": casebook_rows,
        "_casebook_md": casebook_md,
    }
    return payload, paths, casebook_path


def main() -> None:
    args = _parse_args()
    runs2_dir = _resolve_path(args.runs2_dir)
    output_dir = _resolve_path(args.output_dir)
    payload, paths, casebook_path = build_workbench(runs2_dir, output_dir, args.focus_window, args.window_root)

    registry = payload["registry_rows"]
    replay_rows = payload["replay_rows"]
    negative_rows = payload["negative_control_rows"]
    evidence_rows = payload["evidence_utilization_rows"]
    decay_rows = payload["decay_stratification_rows"]
    casebook_rows = payload["casebook_rows"]
    casebook_md = payload.pop("_casebook_md")
    windows = [_resolve_path(runs2_dir / name) for name in payload["windows"]]
    focus_window = _resolve_path(runs2_dir / payload["focus_window"]) if payload["focus_window"] else None

    _write_csv(paths["registry_csv"], registry, force=args.force)
    _write_csv(paths["replay_csv"], replay_rows, force=args.force)
    _write_csv(paths["negative_csv"], negative_rows, force=args.force)
    _write_csv(paths["evidence_csv"], evidence_rows, force=args.force)
    _write_csv(paths["decay_csv"], decay_rows, force=args.force)
    if focus_window and casebook_rows:
        wpaths = _window_paths(focus_window)
        _write_csv(wpaths["casebook_csv"], casebook_rows, force=args.force)
        _write_text(wpaths["casebook_md"], casebook_md, force=args.force)
    _write_text(
        paths["readiness_md"],
        _render_readiness_md(
            registry=registry,
            replay_rows=replay_rows,
            negative_rows=negative_rows,
            evidence_rows=evidence_rows,
            decay_rows=decay_rows,
            paths=paths,
        ),
        force=args.force,
    )
    _write_json(paths["json"], payload, force=args.force)
    _write_text(
        paths["md"],
        _render_workbench_md(
            windows=windows,
            focus_window=focus_window,
            registry=registry,
            replay_rows=replay_rows,
            negative_rows=negative_rows,
            evidence_rows=evidence_rows,
            decay_rows=decay_rows,
            casebook_rows=casebook_rows,
            paths=paths,
            casebook_path=casebook_path,
        ),
        force=args.force,
    )

    print(f"wrote {safe_rel(paths['md'])}")
    print(f"wrote {safe_rel(paths['registry_csv'])} registry_rows={len(registry)}")
    print(f"wrote {safe_rel(paths['replay_csv'])} replay_rows={len(replay_rows)}")
    print(f"wrote {safe_rel(paths['negative_csv'])} negative_controls={len(negative_rows)}")
    print(f"wrote {safe_rel(paths['evidence_csv'])} evidence_families={len(evidence_rows)}")
    print(f"wrote {safe_rel(paths['decay_csv'])} decay_rows={len(decay_rows)}")
    if casebook_path:
        print(f"wrote {safe_rel(casebook_path)} casebook_rows={len(casebook_rows)}")


if __name__ == "__main__":
    main()
