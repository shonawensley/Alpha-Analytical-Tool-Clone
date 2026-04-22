#!/usr/bin/env python3
"""Create a cross-window rollup for Stage-2/Stage-2B audit outputs.

This is a read-only interpretation layer. It compares completed post-run audit
artifacts across windows and labels stack hypotheses for replay, restraint, or
negative-control use. It does not alter prediction, scoring, or budget logic.
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


RUNS_2_DIR = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS_2"


def _parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--runs2-dir", default=str(RUNS_2_DIR), help="Directory containing RUNS_2 window roots.")
    ap.add_argument(
        "--output-dir",
        default=str(RUNS_2_DIR),
        help="Directory for cycle-level cross-window outputs.",
    )
    ap.add_argument(
        "--window-root",
        action="append",
        default=[],
        help="Explicit completed window root to include. Can be repeated; when provided, RUNS_2 auto-discovery is bypassed.",
    )
    ap.add_argument("--force", action="store_true", help="Overwrite existing outputs.")
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


def _safe_float(value: Any, default: float = 0.0) -> float:
    try:
        text = str(value or "").strip()
        if not text:
            return default
        return float(text)
    except Exception:
        return default


def _safe_int(value: Any, default: int = 0) -> int:
    try:
        text = str(value or "").strip()
        if not text:
            return default
        return int(float(text))
    except Exception:
        return default


def _pct(value: float) -> str:
    return f"{100.0 * value:.1f}%"


def _counter_text(counter: Counter[str]) -> str:
    return "|".join(f"{key}:{count}" for key, count in counter.most_common())


def _prefix_for_window(window: Path) -> str:
    return f"{window.name}__ANALYSIS_ARENA"


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

    windows = []
    for window in sorted(path for path in runs2_dir.glob("WINDOW_*") if path.is_dir()):
        prefix = _prefix_for_window(window)
        stack_json = window / f"{prefix}__STAGE2B_SIGNAL_STACK_SCORECARD.json"
        stage2_json = window / f"{prefix}__STAGE2_SIGNAL_FALSE_POSITIVE_SCORECARD.json"
        if stack_json.exists() and stage2_json.exists():
            windows.append(window)
    return windows


def _window_paths(window: Path) -> Dict[str, Path]:
    prefix = _prefix_for_window(window)
    return {
        "stage2_json": window / f"{prefix}__STAGE2_SIGNAL_FALSE_POSITIVE_SCORECARD.json",
        "stack_json": window / f"{prefix}__STAGE2B_SIGNAL_STACK_SCORECARD.json",
        "hypothesis_csv": window / f"{prefix}__TRANSLATOR_RULE_HYPOTHESIS_QUEUE.csv",
        "work_log_md": window / f"{prefix}__STAGE2B_OVERNIGHT_WORK_LOG.md",
    }


def _rollup_status(row: Dict[str, Any]) -> Tuple[str, str]:
    windows_seen = _safe_int(row.get("windows_seen"))
    pair_scope = str(row.get("pair_scope") or "")
    avg_pool = _safe_float(row.get("avg_overlap_values_per_state_day"))
    match_rate = _safe_float(row.get("weighted_match_rate"))
    support_rate = _safe_float(row.get("weighted_supported_event_rate"))
    false_positive = _safe_float(row.get("false_positive_proxy_rate"))
    positive = _safe_int(row.get("positive_conversion_event_count"))
    gap = _safe_int(row.get("gap_teacher_event_count"))
    wrong = _safe_int(row.get("wrong_lane_event_count"))
    decisions = str(row.get("decision_mix") or "")
    active_days = _safe_int(row.get("active_state_days"))
    total_overlap = _safe_int(row.get("total_overlap_values"))
    supported_events = _safe_int(row.get("supported_event_count"))

    if windows_seen < 2:
        return "single_window_only", "Needs at least one more completed window before interpretation."
    if active_days < 50 or total_overlap < 50 or supported_events < 5:
        return (
            "cross_window_low_denominator_fixture",
            "Recurring but still too thin for promotion; preserve as fixture/watch material.",
        )
    if pair_scope.startswith("vtrac"):
        return (
            "cross_window_vtrac_watch_only",
            "Recurring VTRAC/territory support; keep watch/decay unless paired with bounded box/exact proof.",
        )
    if windows_seen >= 3 and "negative_control_stack" in decisions and false_positive >= 0.94 and match_rate <= 0.01:
        return "recurring_negative_control", "Stable broad/low-conversion exposure; use as restraint and denominator control."
    if (
        windows_seen >= 3
        and pair_scope == "box_overlap"
        and avg_pool <= 2.5
        and match_rate >= 0.02
        and (positive + gap) >= 2
        and (positive + gap) >= wrong
    ):
        return (
            "cross_window_boxed_translator_candidate",
            "Bounded box overlap recurs across windows; eligible for fixture replay, not live scoring.",
        )
    if windows_seen >= 3 and pair_scope == "box_overlap" and avg_pool <= 3.0 and support_rate >= 0.005:
        return "cross_window_boxed_support_gate", "Useful support gate candidate; needs replay before weight promotion."
    return "watch_or_fixture_only", "Keep as fixture/context until a sharper replay rule is proven."


def _stack_rollup(windows: Sequence[Path]) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]], List[Dict[str, Any]]]:
    window_rows: List[Dict[str, Any]] = []
    stacks: Dict[str, Dict[str, Any]] = {}
    sources: Dict[str, Dict[str, Any]] = {}

    for window in windows:
        paths = _window_paths(window)
        stage2 = _read_json(paths["stage2_json"])
        stack = _read_json(paths["stack_json"])
        metadata = stack.get("metadata") or stage2.get("metadata") or {}
        winner_events = _safe_int(metadata.get("winner_events"))
        seed_state_days = _safe_int(metadata.get("seed_state_days"))
        stack_rows = stack.get("scorecard") or []
        source_rows = stage2.get("scorecard") or []
        decision_counts = Counter(str(row.get("stage2b_stack_decision") or "") for row in stack_rows)
        window_rows.append(
            {
                "window": window.name,
                "seed_state_days": seed_state_days,
                "winner_events": winner_events,
                "stage2_exposure_rows": _safe_int(metadata.get("exposure_rows")),
                "stage2b_stack_rows": len(stack_rows),
                "stage2b_decision_mix": _counter_text(decision_counts),
                "work_log": safe_rel(paths["work_log_md"]) if paths["work_log_md"].exists() else "",
            }
        )

        for row in stack_rows:
            pair_key = str(row.get("pair_key") or "")
            if not pair_key:
                continue
            entry = stacks.setdefault(
                pair_key,
                {
                    "pair_key": pair_key,
                    "pair_scope": row.get("pair_scope", ""),
                    "source_a": row.get("source_a", ""),
                    "source_b": row.get("source_b", ""),
                    "windows": set(),
                    "decision_counter": Counter(),
                    "active_state_days": 0,
                    "total_overlap_values": 0,
                    "matched_value_count": 0,
                    "supported_event_count": 0,
                    "event_denominator": 0,
                    "false_positive_proxy_value_count": 0,
                    "positive_conversion_event_count": 0,
                    "gap_teacher_event_count": 0,
                    "wrong_lane_event_count": 0,
                },
            )
            entry["windows"].add(window.name)
            entry["decision_counter"][str(row.get("stage2b_stack_decision") or "")] += 1
            entry["active_state_days"] += _safe_int(row.get("active_state_days"))
            entry["total_overlap_values"] += _safe_int(row.get("total_overlap_values"))
            entry["matched_value_count"] += _safe_int(row.get("matched_value_count"))
            entry["supported_event_count"] += _safe_int(row.get("supported_event_count"))
            entry["event_denominator"] += winner_events
            entry["false_positive_proxy_value_count"] += _safe_int(row.get("false_positive_proxy_value_count"))
            entry["positive_conversion_event_count"] += _safe_int(row.get("positive_conversion_event_count"))
            entry["gap_teacher_event_count"] += _safe_int(row.get("gap_teacher_event_count"))
            entry["wrong_lane_event_count"] += _safe_int(row.get("wrong_lane_event_count"))

        for row in source_rows:
            source_key = str(row.get("source_key") or "")
            if not source_key:
                continue
            entry = sources.setdefault(
                source_key,
                {
                    "source_key": source_key,
                    "source_family": row.get("source_family", ""),
                    "target_lane": row.get("target_lane", ""),
                    "windows": set(),
                    "decision_counter": Counter(),
                    "active_state_days": 0,
                    "total_exposure_values": 0,
                    "lane_hit_value_count": 0,
                    "supported_winner_event_count": 0,
                    "event_denominator": 0,
                    "false_positive_proxy_value_count": 0,
                    "rough_lift_sum": 0.0,
                },
            )
            entry["windows"].add(window.name)
            entry["decision_counter"][str(row.get("stage2_decision") or "")] += 1
            entry["active_state_days"] += _safe_int(row.get("active_state_days"))
            entry["total_exposure_values"] += _safe_int(row.get("total_exposure_values"))
            entry["lane_hit_value_count"] += _safe_int(row.get("lane_hit_value_count"))
            entry["supported_winner_event_count"] += _safe_int(row.get("supported_winner_event_count"))
            entry["event_denominator"] += winner_events
            entry["false_positive_proxy_value_count"] += _safe_int(row.get("false_positive_proxy_value_count"))
            entry["rough_lift_sum"] += _safe_float(row.get("rough_lift_vs_naive"))

    stack_rows_out: List[Dict[str, Any]] = []
    for entry in stacks.values():
        windows_seen = len(entry["windows"])
        total_overlap = _safe_int(entry["total_overlap_values"])
        active_days = _safe_int(entry["active_state_days"])
        event_denominator = _safe_int(entry["event_denominator"])
        row = {
            "pair_key": entry["pair_key"],
            "pair_scope": entry["pair_scope"],
            "source_a": entry["source_a"],
            "source_b": entry["source_b"],
            "windows_seen": windows_seen,
            "windows": "|".join(sorted(entry["windows"])),
            "decision_mix": _counter_text(entry["decision_counter"]),
            "active_state_days": active_days,
            "avg_overlap_values_per_state_day": (total_overlap / active_days) if active_days else 0.0,
            "total_overlap_values": total_overlap,
            "matched_value_count": _safe_int(entry["matched_value_count"]),
            "weighted_match_rate": (_safe_int(entry["matched_value_count"]) / total_overlap) if total_overlap else 0.0,
            "supported_event_count": _safe_int(entry["supported_event_count"]),
            "weighted_supported_event_rate": (_safe_int(entry["supported_event_count"]) / event_denominator)
            if event_denominator
            else 0.0,
            "false_positive_proxy_rate": (_safe_int(entry["false_positive_proxy_value_count"]) / total_overlap)
            if total_overlap
            else 0.0,
            "positive_conversion_event_count": _safe_int(entry["positive_conversion_event_count"]),
            "gap_teacher_event_count": _safe_int(entry["gap_teacher_event_count"]),
            "wrong_lane_event_count": _safe_int(entry["wrong_lane_event_count"]),
        }
        status, rationale = _rollup_status(row)
        row["cross_window_status"] = status
        row["cross_window_rationale"] = rationale
        stack_rows_out.append(row)

    stack_rows_out.sort(
        key=lambda row: (
            -_safe_int(row.get("windows_seen")),
            row.get("cross_window_status") != "cross_window_boxed_translator_candidate",
            -_safe_float(row.get("weighted_match_rate")),
            -_safe_float(row.get("weighted_supported_event_rate")),
            row.get("pair_key", ""),
        )
    )

    source_rows_out: List[Dict[str, Any]] = []
    for entry in sources.values():
        windows_seen = len(entry["windows"])
        total_exposure = _safe_int(entry["total_exposure_values"])
        event_denominator = _safe_int(entry["event_denominator"])
        row = {
            "source_key": entry["source_key"],
            "source_family": entry["source_family"],
            "target_lane": entry["target_lane"],
            "windows_seen": windows_seen,
            "windows": "|".join(sorted(entry["windows"])),
            "decision_mix": _counter_text(entry["decision_counter"]),
            "active_state_days": _safe_int(entry["active_state_days"]),
            "total_exposure_values": total_exposure,
            "lane_hit_value_count": _safe_int(entry["lane_hit_value_count"]),
            "weighted_lane_hit_value_rate": (_safe_int(entry["lane_hit_value_count"]) / total_exposure)
            if total_exposure
            else 0.0,
            "supported_winner_event_count": _safe_int(entry["supported_winner_event_count"]),
            "weighted_winner_event_support_rate": (_safe_int(entry["supported_winner_event_count"]) / event_denominator)
            if event_denominator
            else 0.0,
            "false_positive_proxy_rate": (_safe_int(entry["false_positive_proxy_value_count"]) / total_exposure)
            if total_exposure
            else 0.0,
            "avg_rough_lift_vs_naive": (_safe_float(entry["rough_lift_sum"]) / windows_seen) if windows_seen else 0.0,
        }
        source_rows_out.append(row)

    source_rows_out.sort(
        key=lambda row: (
            -_safe_int(row.get("windows_seen")),
            -_safe_float(row.get("weighted_lane_hit_value_rate")),
            row.get("source_key", ""),
        )
    )
    return window_rows, stack_rows_out, source_rows_out


def _hypothesis_rollup(windows: Sequence[Path], stack_rows: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    stack_by_key = {str(row.get("pair_key") or ""): row for row in stack_rows}
    rows: Dict[str, Dict[str, Any]] = {}
    for window in windows:
        paths = _window_paths(window)
        for row in _read_csv_rows(paths["hypothesis_csv"]):
            trigger = str(row.get("trigger") or "")
            lane = str(row.get("lane") or "")
            key = f"{lane}::{trigger}"
            entry = rows.setdefault(
                key,
                {
                    "hypothesis_key": key,
                    "trigger": trigger,
                    "lane": lane,
                    "windows": set(),
                    "status_counter": Counter(),
                    "active_state_days": 0,
                },
            )
            entry["windows"].add(window.name)
            entry["status_counter"][str(row.get("status") or "")] += 1
            entry["active_state_days"] += _safe_int(row.get("active_state_days"))

    out: List[Dict[str, Any]] = []
    for key, entry in rows.items():
        stack = stack_by_key.get(key, {})
        out.append(
            {
                "hypothesis_key": key,
                "trigger": entry["trigger"],
                "lane": entry["lane"],
                "windows_seen": len(entry["windows"]),
                "windows": "|".join(sorted(entry["windows"])),
                "status_mix": _counter_text(entry["status_counter"]),
                "active_state_days": entry["active_state_days"],
                "cross_window_status": stack.get("cross_window_status", "not_in_stack_rollup"),
                "weighted_match_rate": stack.get("weighted_match_rate", ""),
                "weighted_supported_event_rate": stack.get("weighted_supported_event_rate", ""),
                "avg_overlap_values_per_state_day": stack.get("avg_overlap_values_per_state_day", ""),
                "positive_conversion_event_count": stack.get("positive_conversion_event_count", ""),
                "gap_teacher_event_count": stack.get("gap_teacher_event_count", ""),
                "wrong_lane_event_count": stack.get("wrong_lane_event_count", ""),
            }
        )
    out.sort(
        key=lambda row: (
            -_safe_int(row.get("windows_seen")),
            row.get("cross_window_status") != "cross_window_boxed_translator_candidate",
            -_safe_float(row.get("weighted_match_rate")),
            row.get("hypothesis_key", ""),
        )
    )
    return out


def _render_md(
    *,
    window_rows: Sequence[Dict[str, Any]],
    stack_rows: Sequence[Dict[str, Any]],
    source_rows: Sequence[Dict[str, Any]],
    hypothesis_rows: Sequence[Dict[str, Any]],
    paths: Dict[str, Path],
) -> str:
    status_counts = Counter(str(row.get("cross_window_status") or "") for row in stack_rows)
    hypothesis_status_counts = Counter(str(row.get("cross_window_status") or "") for row in hypothesis_rows)
    lines = [
        "# Stage 2B Cross-Window Stack Rollup",
        "",
        "Purpose: separate repeatable translator/stack candidates from one-window noise before any scoring rewrite.",
        "",
        "## Executive Read",
        "",
        "- The cross-window layer is a confirmation surface, not a live scoring surface.",
        "- Recurring bounded box-overlap stacks are the best replay candidates.",
        "- Recurring VTRAC stacks remain watch/decay unless a bounded box or exact confirmation source proves conversion.",
        "- Recurring negative controls are useful because they define what not to promote.",
        "",
        "## Window Coverage",
        "",
    ]
    for row in window_rows:
        lines.append(
            f"- `{row['window']}`: state_days=`{row['seed_state_days']}`, winners=`{row['winner_events']}`, "
            f"stage2_exposures=`{row['stage2_exposure_rows']}`, stage2b_stacks=`{row['stage2b_stack_rows']}`"
        )

    lines.extend(["", "## Stack Status Mix", ""])
    for key, count in status_counts.most_common():
        lines.append(f"- `{key}`: `{count}`")

    lines.extend(["", "## Hypothesis Confirmation Mix", ""])
    for key, count in hypothesis_status_counts.most_common():
        lines.append(f"- `{key}`: `{count}`")

    sections = [
        ("Cross-Window Boxed Translator Candidates", "cross_window_boxed_translator_candidate"),
        ("Cross-Window Boxed Support Gates", "cross_window_boxed_support_gate"),
        ("Cross-Window VTRAC Watch Only", "cross_window_vtrac_watch_only"),
        ("Recurring Negative Controls", "recurring_negative_control"),
        ("Cross-Window Low-Denominator Fixtures", "cross_window_low_denominator_fixture"),
    ]
    for title, status in sections:
        lines.extend(["", f"## {title}", ""])
        scoped = [row for row in stack_rows if row.get("cross_window_status") == status]
        if not scoped:
            lines.append("- None.")
            continue
        for row in scoped[:20]:
            lines.append(
                "- "
                f"`{row['pair_key']}` windows=`{row['windows_seen']}` "
                f"avg_pool=`{_safe_float(row['avg_overlap_values_per_state_day']):.1f}` "
                f"match_rate=`{_pct(_safe_float(row['weighted_match_rate']))}` "
                f"event_support=`{_pct(_safe_float(row['weighted_supported_event_rate']))}`"
            )

    lines.extend(["", "## Stable Source Surfaces", ""])
    for row in source_rows[:20]:
        lines.append(
            "- "
            f"`{row['source_key']}` windows=`{row['windows_seen']}` lane=`{row['target_lane']}` "
            f"lane_rate=`{_pct(_safe_float(row['weighted_lane_hit_value_rate']))}` "
            f"event_support=`{_pct(_safe_float(row['weighted_winner_event_support_rate']))}` "
            f"decisions=`{row['decision_mix']}`"
        )

    lines.extend(
        [
            "",
            "## Generated Files",
            "",
            f"- Stack confirmation CSV: `{safe_rel(paths['stack_csv'])}`",
            f"- Hypothesis confirmation CSV: `{safe_rel(paths['hypothesis_csv'])}`",
            f"- Source confirmation CSV: `{safe_rel(paths['source_csv'])}`",
            f"- Rollup JSON: `{safe_rel(paths['json'])}`",
            "",
            "## Guardrail",
            "",
            "- A cross-window candidate is only permission to replay against fixtures. It is not a permission to alter live scoring or budgeting.",
            "",
        ]
    )
    return "\n".join(lines)


def _default_paths(output_dir: Path) -> Dict[str, Path]:
    prefix = "ANALYSIS_ARENA__CYCLE__STAGE2B_CROSS_WINDOW"
    return {
        "md": output_dir / f"{prefix}_STACK_ROLLUP.md",
        "json": output_dir / f"{prefix}_STACK_ROLLUP.json",
        "stack_csv": output_dir / f"{prefix}_STACK_CONFIRMATION.csv",
        "hypothesis_csv": output_dir / f"{prefix}_HYPOTHESIS_CONFIRMATION.csv",
        "source_csv": output_dir / f"{prefix}_SOURCE_CONFIRMATION.csv",
    }


def main() -> None:
    args = _parse_args()
    runs2_dir = _resolve_path(args.runs2_dir)
    output_dir = _resolve_path(args.output_dir)
    windows = _discover_windows(runs2_dir, args.window_root)
    if not windows:
        raise SystemExit(f"No Stage 2B-ready windows found under {runs2_dir}")

    window_rows, stack_rows, source_rows = _stack_rollup(windows)
    hypothesis_rows = _hypothesis_rollup(windows, stack_rows)
    paths = _default_paths(output_dir)
    payload = {
        "schema_version": "analysis_arena_stage2b_cross_window_stack_rollup/v1",
        "runs2_dir": safe_rel(runs2_dir),
        "windows": window_rows,
        "stack_status_counts": dict(Counter(str(row.get("cross_window_status") or "") for row in stack_rows).most_common()),
        "hypothesis_status_counts": dict(
            Counter(str(row.get("cross_window_status") or "") for row in hypothesis_rows).most_common()
        ),
        "stack_rows": stack_rows,
        "hypothesis_rows": hypothesis_rows,
        "source_rows": source_rows,
    }
    _write_csv(paths["stack_csv"], stack_rows, force=args.force)
    _write_csv(paths["hypothesis_csv"], hypothesis_rows, force=args.force)
    _write_csv(paths["source_csv"], source_rows, force=args.force)
    _write_json(paths["json"], payload, force=args.force)
    _write_text(
        paths["md"],
        _render_md(
            window_rows=window_rows,
            stack_rows=stack_rows,
            source_rows=source_rows,
            hypothesis_rows=hypothesis_rows,
            paths=paths,
        ),
        force=args.force,
    )

    print(f"wrote {safe_rel(paths['md'])}")
    print(f"wrote {safe_rel(paths['stack_csv'])} stacks={len(stack_rows)}")
    print(f"wrote {safe_rel(paths['hypothesis_csv'])} hypotheses={len(hypothesis_rows)}")
    print(f"wrote {safe_rel(paths['source_csv'])} sources={len(source_rows)}")


if __name__ == "__main__":
    main()
