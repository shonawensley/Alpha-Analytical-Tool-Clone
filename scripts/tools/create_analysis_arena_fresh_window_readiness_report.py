#!/usr/bin/env python3
"""Create a fresh-window readiness report for the active Analysis Arena package."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any, Dict, List, Sequence


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.tools.analysis_arena_window_utils import read_json, safe_rel


DEFAULT_RUNS2_ROOT = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS_2"
DEFAULT_FINAL_DOCS = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "final docs"
WINDOW_NAME_RE = re.compile(r"^WINDOW_(\d{4}-\d{2}-\d{2})_to_(\d{4}-\d{2}-\d{2})$")


def _parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--runs2-root", default=str(DEFAULT_RUNS2_ROOT), help="RUNS_2 root to scan for completed windows.")
    ap.add_argument("--window-root", action="append", default=[], help="Optional explicit window roots. Can be repeated.")
    ap.add_argument("--out-md", default="", help="Optional markdown output path.")
    ap.add_argument("--out-json", default="", help="Optional JSON output path.")
    ap.add_argument("--force", action="store_true", help="Overwrite existing outputs.")
    return ap.parse_args()


def _resolve_path(value: str) -> Path:
    path = Path(value).expanduser()
    if not path.is_absolute():
        path = (REPO_ROOT / path).resolve()
    return path


def _default_paths() -> Dict[str, Path]:
    stem = "AAT9_ANALYSIS_ARENA__FRESH_WINDOW_READINESS"
    return {
        "md": DEFAULT_FINAL_DOCS / f"{stem}.md",
        "json": DEFAULT_FINAL_DOCS / f"{stem}.json",
    }


def _write_text(path: Path, text: str, *, force: bool) -> None:
    if path.exists() and not force:
        raise SystemExit(f"Refusing to overwrite existing file without --force: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _write_json(path: Path, payload: Any, *, force: bool) -> None:
    _write_text(path, json.dumps(payload, indent=2, sort_keys=True) + "\n", force=force)


def _parse_window_dates(path: Path) -> tuple[date, date] | None:
    match = WINDOW_NAME_RE.match(path.name)
    if not match:
        return None
    try:
        return date.fromisoformat(match.group(1)), date.fromisoformat(match.group(2))
    except ValueError:
        return None


def _discover_windows(runs2_root: Path) -> List[Path]:
    candidates: List[tuple[Path, date, date]] = []
    for path in sorted(runs2_root.glob("WINDOW_*")):
        if not path.is_dir():
            continue
        parsed = _parse_window_dates(path)
        if not parsed:
            continue
        candidates.append((path, parsed[0], parsed[1]))

    canonical_candidates: List[Path] = []
    for path, start, end in candidates:
        contained_by_larger_window = any(
            other_path != path
            and other_start <= start
            and end <= other_end
            and (other_start < start or end < other_end)
            for other_path, other_start, other_end in candidates
        )
        if not contained_by_larger_window:
            canonical_candidates.append(path)

    windows: List[Path] = []
    for path in sorted(canonical_candidates):
        stem = path.name
        required = [
            path / f"{stem}__ANALYSIS_ARENA__PERFORMANCE_GAP.json",
            path / f"{stem}__ANALYSIS_ARENA__DEEP_HIT_ANALYSIS.json",
            path / f"{stem}__ANALYSIS_ARENA__C1_C2_FRONTIER_ANALYSIS.json",
            path / f"{stem}__ANALYSIS_ARENA__PURE_FINALIST_SCORECARD.json",
            path / f"{stem}__ANALYSIS_ARENA__TRANSLATOR_LEARNING_LEDGER.json",
            path / f"{stem}__ANALYSIS_ARENA__DEEP_ANALYSIS__CODEX.json",
        ]
        if all(item.exists() for item in required):
            windows.append(path)
    return windows


def _window_status(window_root: Path) -> Dict[str, Any]:
    stem = window_root.name
    checks = {
        "performance_gap": window_root / f"{stem}__ANALYSIS_ARENA__PERFORMANCE_GAP.json",
        "deep_hit_analysis": window_root / f"{stem}__ANALYSIS_ARENA__DEEP_HIT_ANALYSIS.json",
        "frontier_harness": window_root / f"{stem}__ANALYSIS_ARENA__C1_C2_FRONTIER_ANALYSIS.json",
        "pure_finalist_scorecard": window_root / f"{stem}__ANALYSIS_ARENA__PURE_FINALIST_SCORECARD.json",
        "translator_learning_ledger": window_root / f"{stem}__ANALYSIS_ARENA__TRANSLATOR_LEARNING_LEDGER.json",
        "deep_window_analysis": window_root / f"{stem}__ANALYSIS_ARENA__DEEP_ANALYSIS__CODEX.json",
    }
    status = {key: path.exists() for key, path in checks.items()}
    return {
        "window": stem.replace("WINDOW_", ""),
        "window_root": safe_rel(window_root),
        "complete": all(status.values()),
        "checks": status,
    }


def _exists_status(path: Path) -> Dict[str, Any]:
    return {"path": safe_rel(path), "exists": path.exists()}


def build_payload(runs2_root: Path, window_roots: Sequence[Path]) -> Dict[str, Any]:
    docs = {
        "system_index": _exists_status(DEFAULT_FINAL_DOCS / "AAT9_ANALYSIS_ARENA__SYSTEM_INDEX.md"),
        "quickstart": _exists_status(DEFAULT_FINAL_DOCS / "AAT9_ANALYSIS_ARENA_FRESH_RUNS_CADENCE__QUICKSTART.md"),
        "operating_flow": _exists_status(DEFAULT_FINAL_DOCS / "AAT9_ANALYSIS_ARENA_OPERATING_FLOW__FRESH_RUNS.md"),
        "readme": _exists_status(DEFAULT_FINAL_DOCS / "README.md"),
        "portal": _exists_status(runs2_root / "PORTAL.md"),
        "macro_log": _exists_status(DEFAULT_FINAL_DOCS / "AAT9_ANALYSIS_ARENA__MACRO_FINDINGS_LOG.md"),
    }
    system_artifacts = {
        "cross_window_rollup": _exists_status(DEFAULT_FINAL_DOCS / "AAT9_ANALYSIS_ARENA__CROSS_WINDOW_ROLLUP.json"),
        "tuneup_diagnostics": _exists_status(DEFAULT_FINAL_DOCS / "AAT9_ANALYSIS_ARENA__TUNEUP_DIAGNOSTICS.json"),
        "frontier_negative_control": _exists_status(DEFAULT_FINAL_DOCS / "AAT9_ANALYSIS_ARENA__FRONTIER_NEGATIVE_CONTROL_STUDY.json"),
    }

    rollup_summary: Dict[str, Any] = {}
    tuneup_summary: Dict[str, Any] = {}
    frontier_summary: Dict[str, Any] = {}
    if system_artifacts["cross_window_rollup"]["exists"]:
        rollup_payload = read_json(DEFAULT_FINAL_DOCS / "AAT9_ANALYSIS_ARENA__CROSS_WINDOW_ROLLUP.json")
        if isinstance(rollup_payload, dict):
            rollup_summary = dict(rollup_payload.get("summary") or {})
    if system_artifacts["tuneup_diagnostics"]["exists"]:
        tuneup_payload = read_json(DEFAULT_FINAL_DOCS / "AAT9_ANALYSIS_ARENA__TUNEUP_DIAGNOSTICS.json")
        if isinstance(tuneup_payload, dict):
            tuneup_summary = {
                "ranking_false_positive_count": len(((tuneup_payload.get("brain2_ranking") or {}).get("repeated_false_positive_top_states") or [])),
                "ranking_productive_non_primary_count": len(((tuneup_payload.get("brain2_ranking") or {}).get("productive_non_primary_states") or [])),
                "tracker_lift_rows": len(((tuneup_payload.get("tracker_lift") or {}).get("rows") or [])),
                "doubles_rows": len(((tuneup_payload.get("doubles_subtype") or {}).get("rows") or [])),
            }
    if system_artifacts["frontier_negative_control"]["exists"]:
        frontier_payload = read_json(DEFAULT_FINAL_DOCS / "AAT9_ANALYSIS_ARENA__FRONTIER_NEGATIVE_CONTROL_STUDY.json")
        if isinstance(frontier_payload, dict):
            frontier_summary = {
                "case_count": int((frontier_payload.get("metadata") or {}).get("case_count", 0) or 0),
                "strict_box_cases": int((frontier_payload.get("cohort_counts") or {}).get("strict_box", 0) or 0),
                "box_gap_cases": int((frontier_payload.get("cohort_counts") or {}).get("box_gap", 0) or 0),
                "no_conversion_cases": int((frontier_payload.get("cohort_counts") or {}).get("no_conversion", 0) or 0),
            }

    windows = [_window_status(path) for path in window_roots]
    complete_windows = sum(1 for row in windows if bool(row.get("complete")))
    docs_ready = all(bool(block.get("exists")) for block in docs.values())
    system_ready = all(bool(block.get("exists")) for block in system_artifacts.values())
    readiness_checks = {
        "docs_ready": docs_ready,
        "system_artifacts_ready": system_ready,
        "completed_window_count": complete_windows,
        "minimum_completed_windows_met": complete_windows >= 3,
        "cross_window_rollup_populated": int(rollup_summary.get("window_count", 0) or 0) >= 3,
        "tuneup_diagnostics_populated": int(tuneup_summary.get("tracker_lift_rows", 0) or 0) > 0,
        "frontier_control_populated": int(frontier_summary.get("case_count", 0) or 0) > 0,
    }
    ready = all(bool(value) for value in readiness_checks.values())
    window_lock_inputs = [
        "window start / end dates",
        "decay-upload-days-total horizon (default 5 total upload days including same-day)",
        "tail coverage plan: full results through window_end + 4 days or expected right-censored decay rows",
        "decay execution posture: run during backtest closeout now or defer until future results arrive",
    ]

    return {
        "metadata": {
            "runs2_root": safe_rel(runs2_root),
            "window_count": len(window_roots),
            "ready_for_fresh_windows": ready,
        },
        "docs": docs,
        "system_artifacts": system_artifacts,
        "rollup_summary": rollup_summary,
        "tuneup_summary": tuneup_summary,
        "frontier_summary": frontier_summary,
        "windows": windows,
        "readiness_checks": readiness_checks,
        "window_lock_inputs": window_lock_inputs,
        "next_actions": [
            "Use this report as the fresh-window preflight before starting new gold-day windows.",
            "Keep the current cadence frozen and run cross-window-rollup, tuneup-diagnostics, and frontier-negative-control again after each new fresh window block.",
            "Before each fresh window, explicitly lock the window dates, the decay-upload-days-total setting, and the tail coverage plan.",
            "Do not promote live translator, combo, budget, or frontier scoring changes until the fresh windows repeat or contradict the current comparison-window findings.",
        ],
    }


def _render_markdown(payload: Dict[str, Any]) -> str:
    meta = payload.get("metadata") or {}
    docs = payload.get("docs") or {}
    system_artifacts = payload.get("system_artifacts") or {}
    windows = payload.get("windows") or []
    checks = payload.get("readiness_checks") or {}
    rollup_summary = payload.get("rollup_summary") or {}
    tuneup_summary = payload.get("tuneup_summary") or {}
    frontier_summary = payload.get("frontier_summary") or {}
    lines: List[str] = [
        "# Analysis Arena Fresh-Window Readiness",
        "",
        "## 1. Verdict",
        "",
        f"- Ready for fresh windows: `{bool(meta.get('ready_for_fresh_windows'))}`",
        f"- Completed comparison windows available: `{sum(1 for row in windows if row.get('complete'))}` / `{len(windows)}`",
        "",
        "## 2. Core Docs / Memory Anchors",
        "",
    ]
    for key, block in docs.items():
        lines.append(f"- `{key}`: `{bool(block.get('exists'))}` -> `{block.get('path', '')}`")
    lines += ["", "## 3. System-Level Artifacts", ""]
    for key, block in system_artifacts.items():
        lines.append(f"- `{key}`: `{bool(block.get('exists'))}` -> `{block.get('path', '')}`")
    lines += [
        "",
        "## 4. Comparison Window Inventory",
        "",
        "| Window | Complete | Perf | Hits | Frontier | Pure | Translator | Deep |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for row in windows:
        checks_row = row.get("checks") or {}
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row.get("window", "")),
                    str(bool(row.get("complete"))),
                    str(bool(checks_row.get("performance_gap"))),
                    str(bool(checks_row.get("deep_hit_analysis"))),
                    str(bool(checks_row.get("frontier_harness"))),
                    str(bool(checks_row.get("pure_finalist_scorecard"))),
                    str(bool(checks_row.get("translator_learning_ledger"))),
                    str(bool(checks_row.get("deep_window_analysis"))),
                ]
            )
            + " |"
        )
    lines += [
        "",
        "## 5. Readiness Checks",
        "",
    ]
    for key, value in checks.items():
        lines.append(f"- `{key}`: `{bool(value)}`")
    lines += [
        "",
        "## 6. Per-Window Lock Inputs",
        "",
    ]
    for item in payload.get("window_lock_inputs") or []:
        lines.append(f"- {item}")
    lines += [
        "",
        "## 7. Evidence Snapshot",
        "",
        f"- Cross-window rollup window count: `{rollup_summary.get('window_count', 0)}`",
        f"- Cross-window winner events: `{rollup_summary.get('winner_events', 0)}`",
        f"- Cross-window credited hits: `{rollup_summary.get('credited_hits', 0)}`",
        f"- Tune-up tracker-lift rows: `{tuneup_summary.get('tracker_lift_rows', 0)}`",
        f"- Tune-up ranking false-positive states: `{tuneup_summary.get('ranking_false_positive_count', 0)}`",
        f"- Frontier control cases: `{frontier_summary.get('case_count', 0)}`",
        f"- Frontier control strict-box cases: `{frontier_summary.get('strict_box_cases', 0)}`",
        f"- Frontier control no-conversion cases: `{frontier_summary.get('no_conversion_cases', 0)}`",
        "",
        "## 8. Next Actions",
        "",
    ]
    for item in payload.get("next_actions") or []:
        lines.append(f"- {item}")
    return "\n".join(lines) + "\n"


def main() -> None:
    args = _parse_args()
    runs2_root = _resolve_path(args.runs2_root)
    window_roots = [_resolve_path(value) for value in list(args.window_root or [])] or _discover_windows(runs2_root)
    outputs = _default_paths()
    out_md = _resolve_path(args.out_md) if args.out_md else outputs["md"]
    out_json = _resolve_path(args.out_json) if args.out_json else outputs["json"]
    payload = build_payload(runs2_root, window_roots)
    _write_json(out_json, payload, force=bool(args.force))
    _write_text(out_md, _render_markdown(payload), force=bool(args.force))
    print(safe_rel(out_md))
    print(safe_rel(out_json))


if __name__ == "__main__":
    main()
