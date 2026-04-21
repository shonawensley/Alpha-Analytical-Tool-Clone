#!/usr/bin/env python3
"""Create a read-only window replay/replication readiness report.

The report scans existing Analysis Arena windows and source-data coverage so
known windows can be reused safely without confusing replay evidence with true
fresh-window confirmation.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from datetime import date, timedelta
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.tools.analysis_arena_window_utils import safe_rel


DEFAULT_RUNS2_ROOT = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS_2"
DEFAULT_FINAL_DOCS = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "final docs"
DEFAULT_HISTORY_ROOT = REPO_ROOT / "data" / "history"
DEFAULT_RESULTS_ROOT = REPO_ROOT / "data" / "results"
DEFAULT_BONUS_RESULTS_ROOT = REPO_ROOT / "data" / "results_bonus"
DEFAULT_PREDICTIVE_SHAREPACKS_ROOT = REPO_ROOT / "sharepacks" / "_predictive"
DEFAULT_TRUTH_SHAREPACKS_ROOT = REPO_ROOT / "sharepacks"

DATE_RE = re.compile(r"(20\d{2})[-_](\d{2})[-_](\d{2})")
WINDOW_RE = re.compile(r"^WINDOW_(?P<start>\d{4}-\d{2}-\d{2})_to_(?P<end>\d{4}-\d{2}-\d{2})(?P<suffix>.*)$")
MARCH_BASELINE_WINDOW = "WINDOW_2026-03-09_to_2026-03-23"


def _parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--runs2-root", default=str(DEFAULT_RUNS2_ROOT), help="RUNS_2 root to scan.")
    ap.add_argument("--window-root", action="append", default=[], help="Optional explicit RUNS_2 window roots. Can be repeated.")
    ap.add_argument("--history-root", default=str(DEFAULT_HISTORY_ROOT), help="History workbook root.")
    ap.add_argument("--results-root", default=str(DEFAULT_RESULTS_ROOT), help="Core results root.")
    ap.add_argument("--bonus-results-root", default=str(DEFAULT_BONUS_RESULTS_ROOT), help="Bonus-ball sidecar results root.")
    ap.add_argument("--predictive-sharepacks-root", default=str(DEFAULT_PREDICTIVE_SHAREPACKS_ROOT), help="Predictive sharepacks root.")
    ap.add_argument("--truth-sharepacks-root", default=str(DEFAULT_TRUTH_SHAREPACKS_ROOT), help="Post-results truth sharepacks root.")
    ap.add_argument("--out-md", default="", help="Optional Markdown output path.")
    ap.add_argument("--out-json", default="", help="Optional JSON output path.")
    ap.add_argument("--out-csv", default="", help="Optional CSV output path.")
    ap.add_argument("--force", action="store_true", help="Overwrite existing outputs.")
    return ap.parse_args()


def _resolve_path(value: str) -> Path:
    path = Path(value).expanduser()
    if not path.is_absolute():
        path = (REPO_ROOT / path).resolve()
    return path


def _default_paths() -> Dict[str, Path]:
    stem = "AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_READINESS"
    return {
        "md": DEFAULT_FINAL_DOCS / f"{stem}.md",
        "json": DEFAULT_FINAL_DOCS / f"{stem}.json",
        "csv": DEFAULT_FINAL_DOCS / f"{stem}.csv",
    }


def _write_text(path: Path, text: str, *, force: bool) -> None:
    if path.exists() and not force:
        raise SystemExit(f"Refusing to overwrite existing file without --force: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _write_json(path: Path, payload: Any, *, force: bool) -> None:
    _write_text(path, json.dumps(payload, indent=2, sort_keys=True) + "\n", force=force)


def _write_csv(path: Path, rows: List[Dict[str, Any]], *, force: bool) -> None:
    if path.exists() and not force:
        raise SystemExit(f"Refusing to overwrite existing file without --force: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "window_name",
        "window_start",
        "window_end",
        "evidence_tier",
        "readiness_status",
        "recommended_next_use",
        "file_count",
        "history_missing_count",
        "predictive_missing_count",
        "truth_missing_count",
        "results_missing_count",
        "tail_missing_count",
        "bonus_missing_count",
        "has_full_decay_tail",
        "has_bonus_tail",
        "baseline_manifest_status",
        "allowed_conclusions",
        "blocked_conclusions",
        "window_root",
    ]
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row.get(key, "") for key in fieldnames})


def _parse_date(value: str) -> date | None:
    try:
        y, m, d = (int(part) for part in value.split("-"))
        return date(y, m, d)
    except Exception:
        return None


def _date_range(start: date, end: date) -> List[date]:
    out: List[date] = []
    current = start
    while current <= end:
        out.append(current)
        current += timedelta(days=1)
    return out


def _date_set_from_paths(paths: Iterable[Path]) -> set[date]:
    out: set[date] = set()
    for path in paths:
        match = DATE_RE.search(str(path))
        if not match:
            continue
        try:
            out.add(date(int(match.group(1)), int(match.group(2)), int(match.group(3))))
        except ValueError:
            continue
    return out


def _date_set_from_named_dirs(path: Path) -> set[date]:
    if not path.exists():
        return set()
    out: set[date] = set()
    for child in path.iterdir():
        if not child.is_dir():
            continue
        parsed = _parse_date(child.name)
        if parsed:
            out.add(parsed)
    return out


def _date_set_from_result_files(path: Path) -> set[date]:
    if not path.exists():
        return set()
    out: set[date] = set()
    for child in path.glob("*.txt"):
        parsed = _parse_date(child.stem)
        if parsed:
            out.add(parsed)
    return out


def _missing(dates: Sequence[date], available: set[date]) -> List[str]:
    return [item.isoformat() for item in dates if item not in available]


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _window_parts(window_root: Path) -> Dict[str, Any] | None:
    match = WINDOW_RE.match(window_root.name)
    if not match:
        return None
    start = _parse_date(match.group("start"))
    end = _parse_date(match.group("end"))
    if not start or not end:
        return None
    return {
        "start": start,
        "end": end,
        "suffix": match.group("suffix") or "",
    }


def _discover_windows(runs2_root: Path) -> List[Path]:
    if not runs2_root.exists():
        return []
    return sorted(path for path in runs2_root.glob("WINDOW_*") if path.is_dir() and _window_parts(path))


def _key_artifact_paths(window_root: Path) -> Dict[str, Path]:
    stem = window_root.name
    return {
        "performance_gap_json": window_root / f"{stem}__ANALYSIS_ARENA__PERFORMANCE_GAP.json",
        "deep_hit_analysis_json": window_root / f"{stem}__ANALYSIS_ARENA__DEEP_HIT_ANALYSIS.json",
        "frontier_harness_json": window_root / f"{stem}__ANALYSIS_ARENA__C1_C2_FRONTIER_ANALYSIS.json",
        "pure_finalist_scorecard_json": window_root / f"{stem}__ANALYSIS_ARENA__PURE_FINALIST_SCORECARD.json",
        "translator_learning_ledger_json": window_root / f"{stem}__ANALYSIS_ARENA__TRANSLATOR_LEARNING_LEDGER.json",
        "deep_analysis_json": window_root / f"{stem}__ANALYSIS_ARENA__DEEP_ANALYSIS__CODEX.json",
        "decay_carryover_json": window_root / f"{stem}__ANALYSIS_ARENA__DECAY_CARRYOVER_SCORECARD.json",
        "window_close_receipt": window_root / "ANALYSIS_ARENA__CYCLE__WINDOW_CLOSE__tool_only__arena_v0.md",
        "window_decay_receipt": window_root / "ANALYSIS_ARENA__CYCLE__WINDOW_DECAY_CLOSE.md",
    }


def _artifact_family_counts(window_root: Path) -> Dict[str, int]:
    analysis = window_root / "ANALYSIS_ARENA"
    validation = window_root / "VALIDATION"
    return {
        "total_files": sum(1 for path in window_root.rglob("*") if path.is_file()),
        "analysis_arena_files": sum(1 for path in analysis.rglob("*") if path.is_file()) if analysis.exists() else 0,
        "validation_files": sum(1 for path in validation.rglob("*") if path.is_file()) if validation.exists() else 0,
        "root_files": sum(1 for path in window_root.iterdir() if path.is_file()) if window_root.exists() else 0,
        "cycle_receipts": sum(1 for path in window_root.rglob("ANALYSIS_ARENA__CYCLE__*.md") if path.is_file()),
        "board_scoreboards": sum(1 for path in analysis.glob("*__BOARD_SCOREBOARD__*.json") if path.is_file()) if analysis.exists() else 0,
        "translation_sandbox_manifests": sum(1 for path in analysis.glob("*__TRANSLATION_SANDBOX_SEED__*.json") if path.is_file()) if analysis.exists() else 0,
        "brain2_tracker_ledgers": sum(1 for path in validation.glob("*__BRAIN2_TRACKER_LEDGER.json") if path.is_file()) if validation.exists() else 0,
    }


def _baseline_hashes(window_root: Path) -> Dict[str, Dict[str, Any]]:
    out: Dict[str, Dict[str, Any]] = {}
    for key, path in _key_artifact_paths(window_root).items():
        exists = path.exists()
        out[key] = {
            "path": safe_rel(path),
            "exists": exists,
            "sha256": _sha256(path) if exists else "",
        }
    return out


def _baseline_status(key_artifacts: Dict[str, bool], file_count: int) -> str:
    critical = [
        "performance_gap_json",
        "deep_hit_analysis_json",
        "frontier_harness_json",
        "pure_finalist_scorecard_json",
        "translator_learning_ledger_json",
        "deep_analysis_json",
    ]
    if all(key_artifacts.get(key) for key in critical):
        return "baseline_complete"
    if file_count > 0:
        return "partial_baseline"
    return "missing_baseline"


def _recommended_use(window_name: str, evidence_tier: str, readiness_status: str) -> str:
    if window_name == MARCH_BASELINE_WINDOW:
        return "strongest_same_window_replay_candidate"
    if readiness_status == "needs_prep":
        return "repair_missing_coverage_before_replay"
    if "__PREALIGN_SNAPSHOT" in window_name:
        return "baseline_snapshot_reference_only"
    if readiness_status == "ready_with_caveats":
        return "archived_replication_with_explicit_caveats"
    if evidence_tier == "archived_window_replication":
        return "archived_replication_candidate"
    return "same_window_replay_candidate"


def _allowed_conclusions(evidence_tier: str, readiness_status: str) -> str:
    if readiness_status == "needs_prep":
        return "coverage gaps can be repaired; do not interpret as replay evidence yet"
    if evidence_tier == "same_window_replay":
        return "regression; traceability; before-after comparison; deterministic rerun checks"
    if evidence_tier == "archived_window_replication":
        return "historical replication; window-character stress test; blocker recheck target"
    return "fresh confirmation only if explicitly prepared after gates"


def _blocked_conclusions(evidence_tier: str) -> str:
    if evidence_tier in {"same_window_replay", "archived_window_replication"}:
        return "no fresh-confirmation claim; no Stage 8A unlock; no live scoring/budget replacement"
    return "no live scoring/budget replacement without Stage 8 shadow evidence"


def _window_evidence_tier(window_name: str) -> str:
    if window_name == MARCH_BASELINE_WINDOW or "__PREALIGN_SNAPSHOT" in window_name:
        return "same_window_replay"
    return "archived_window_replication"


def _window_row(
    *,
    window_root: Path,
    history_dates: set[date],
    results_dates: set[date],
    bonus_dates: set[date],
    predictive_dates: set[date],
    truth_dates: set[date],
) -> Dict[str, Any]:
    parts = _window_parts(window_root)
    if not parts:
        raise SystemExit(f"Invalid window root name: {window_root}")

    start: date = parts["start"]
    end: date = parts["end"]
    window_dates = _date_range(start, end)
    history_needed = [item - timedelta(days=1) for item in window_dates]
    tail_needed = _date_range(start, end + timedelta(days=4))

    history_missing = _missing(history_needed, history_dates)
    predictive_missing = _missing(window_dates, predictive_dates)
    truth_missing = _missing(window_dates, truth_dates)
    results_missing = _missing(window_dates, results_dates)
    tail_missing = _missing(tail_needed, results_dates)
    bonus_missing = _missing(tail_needed, bonus_dates)

    counts = _artifact_family_counts(window_root)
    key_artifact_paths = _key_artifact_paths(window_root)
    key_artifacts = {key: path.exists() for key, path in key_artifact_paths.items()}
    baseline_manifest_status = _baseline_status(key_artifacts, counts["total_files"])

    critical_missing = bool(history_missing or predictive_missing or results_missing)
    caveat_missing = bool(truth_missing or tail_missing)
    if critical_missing:
        readiness_status = "needs_prep"
    elif caveat_missing:
        readiness_status = "ready_with_caveats"
    else:
        readiness_status = "ready"

    evidence_tier = _window_evidence_tier(window_root.name)
    recommended_next_use = _recommended_use(window_root.name, evidence_tier, readiness_status)

    return {
        "window_name": window_root.name,
        "window_root": safe_rel(window_root),
        "window_start": start.isoformat(),
        "window_end": end.isoformat(),
        "window_day_count": len(window_dates),
        "history_needed": [item.isoformat() for item in history_needed],
        "results_needed": [item.isoformat() for item in window_dates],
        "tail_results_needed": [item.isoformat() for item in tail_needed],
        "evidence_tier": evidence_tier,
        "readiness_status": readiness_status,
        "recommended_next_use": recommended_next_use,
        "history_missing": history_missing,
        "predictive_missing": predictive_missing,
        "truth_missing": truth_missing,
        "results_missing": results_missing,
        "tail_missing": tail_missing,
        "bonus_missing": bonus_missing,
        "history_missing_count": len(history_missing),
        "predictive_missing_count": len(predictive_missing),
        "truth_missing_count": len(truth_missing),
        "results_missing_count": len(results_missing),
        "tail_missing_count": len(tail_missing),
        "bonus_missing_count": len(bonus_missing),
        "has_full_decay_tail": not bool(tail_missing),
        "has_bonus_tail": not bool(bonus_missing),
        "file_count": counts["total_files"],
        "artifact_family_counts": counts,
        "key_artifacts": key_artifacts,
        "baseline_manifest_status": baseline_manifest_status,
        "baseline_hashes": _baseline_hashes(window_root),
        "allowed_conclusions": _allowed_conclusions(evidence_tier, readiness_status),
        "blocked_conclusions": _blocked_conclusions(evidence_tier),
    }


def _stage_artifact_status(runs2_root: Path) -> Dict[str, bool]:
    names = {
        "stage6b_shadow_replay": "ANALYSIS_ARENA__CYCLE__STAGE6B_SHADOW_REPLAY_SIMULATOR.json",
        "stage6b_readback": "ANALYSIS_ARENA__CYCLE__STAGE6B_READBACK_DECISION_MEMO.json",
        "stage6c_confirmation": "ANALYSIS_ARENA__CYCLE__STAGE6C_FUTURE_CONFIRMATION_PROTOCOL.json",
        "stage6d_restraint": "ANALYSIS_ARENA__CYCLE__STAGE6D_RESTRAINT_CALIBRATION_WORKBENCH.json",
        "stage6e_support": "ANALYSIS_ARENA__CYCLE__STAGE6E_SUPPORT_MODIFIER_NARROWING_WORKBENCH.json",
        "stage6f_atlas": "ANALYSIS_ARENA__CYCLE__STAGE6F_INTEGRATED_DECISION_ATLAS.json",
        "stage7a_scaffold": "ANALYSIS_ARENA__CYCLE__STAGE7A_FRESH_CONFIRMATION_SCAFFOLD.json",
        "stage7b_harness": "ANALYSIS_ARENA__CYCLE__STAGE7B_FIXTURE_REPLAY_HARNESS.json",
    }
    return {key: (runs2_root / filename).exists() for key, filename in names.items()}


def build_payload(
    *,
    runs2_root: Path,
    window_roots: Sequence[Path],
    history_root: Path,
    results_root: Path,
    bonus_results_root: Path,
    predictive_sharepacks_root: Path,
    truth_sharepacks_root: Path,
) -> Dict[str, Any]:
    history_dates = _date_set_from_paths(history_root.rglob("*")) if history_root.exists() else set()
    results_dates = _date_set_from_result_files(results_root)
    bonus_dates = _date_set_from_result_files(bonus_results_root)
    predictive_dates = _date_set_from_named_dirs(predictive_sharepacks_root)
    truth_dates = _date_set_from_named_dirs(truth_sharepacks_root)

    rows = [
        _window_row(
            window_root=window_root,
            history_dates=history_dates,
            results_dates=results_dates,
            bonus_dates=bonus_dates,
            predictive_dates=predictive_dates,
            truth_dates=truth_dates,
        )
        for window_root in window_roots
    ]
    rows_sorted = sorted(rows, key=lambda row: (row["readiness_status"] == "needs_prep", row["evidence_tier"], row["window_start"]))

    same_window = [row for row in rows_sorted if row["evidence_tier"] == "same_window_replay" and row["readiness_status"] != "needs_prep"]
    archived = [row for row in rows_sorted if row["evidence_tier"] == "archived_window_replication" and row["readiness_status"] == "ready"]
    archived_caveats = [row for row in rows_sorted if row["evidence_tier"] == "archived_window_replication" and row["readiness_status"] == "ready_with_caveats"]
    needs_prep = [row for row in rows_sorted if row["readiness_status"] == "needs_prep"]

    strongest_same = next((row for row in same_window if row["window_name"] == MARCH_BASELINE_WINDOW), same_window[0] if same_window else {})
    strongest_archived = archived[0] if archived else (archived_caveats[0] if archived_caveats else {})
    stage_status = _stage_artifact_status(runs2_root)

    return {
        "metadata": {
            "runs2_root": safe_rel(runs2_root),
            "history_root": safe_rel(history_root),
            "results_root": safe_rel(results_root),
            "bonus_results_root": safe_rel(bonus_results_root),
            "predictive_sharepacks_root": safe_rel(predictive_sharepacks_root),
            "truth_sharepacks_root": safe_rel(truth_sharepacks_root),
            "window_count": len(rows_sorted),
        },
        "source_coverage": {
            "history_date_count": len(history_dates),
            "results_date_count": len(results_dates),
            "bonus_results_date_count": len(bonus_dates),
            "predictive_sharepack_date_count": len(predictive_dates),
            "truth_sharepack_date_count": len(truth_dates),
            "history_date_min": min(history_dates).isoformat() if history_dates else "",
            "history_date_max": max(history_dates).isoformat() if history_dates else "",
            "results_date_min": min(results_dates).isoformat() if results_dates else "",
            "results_date_max": max(results_dates).isoformat() if results_dates else "",
            "bonus_results_date_min": min(bonus_dates).isoformat() if bonus_dates else "",
            "bonus_results_date_max": max(bonus_dates).isoformat() if bonus_dates else "",
            "predictive_date_min": min(predictive_dates).isoformat() if predictive_dates else "",
            "predictive_date_max": max(predictive_dates).isoformat() if predictive_dates else "",
            "truth_date_min": min(truth_dates).isoformat() if truth_dates else "",
            "truth_date_max": max(truth_dates).isoformat() if truth_dates else "",
        },
        "stage_artifact_status": stage_status,
        "summary": {
            "same_window_replay_candidates": len(same_window),
            "archived_replication_ready": len(archived),
            "archived_replication_with_caveats": len(archived_caveats),
            "needs_prep": len(needs_prep),
            "strongest_same_window_replay_candidate": strongest_same.get("window_name", ""),
            "strongest_archived_replication_candidate": strongest_archived.get("window_name", ""),
            "stage6b_to_stage7b_artifacts_present": all(stage_status.values()),
        },
        "rows": rows_sorted,
        "comparison_design_stub": {
            "baseline_vs_rerun_categories": [
                "unchanged",
                "improved_traceability",
                "newly_exposed",
                "degraded",
                "contradicted",
                "renamed_or_reclassified_only",
                "blocked_by_missing_data",
            ],
            "compare_before_running": [
                "evidence_tier",
                "run_label",
                "baseline_manifest_status",
                "key_artifact_hashes",
                "allowed_conclusions",
                "blocked_conclusions",
            ],
            "stage6b_to_stage7b_compare_after_rerun": [
                "scenario decisions",
                "requirement results",
                "rewrite blockers",
                "restraint bucket posture",
                "support narrowing posture",
                "lane decision atlas",
                "fresh-window carry-forward queue",
                "Stage 7B queue replay status",
            ],
        },
    }


def _bool(value: Any) -> str:
    return "true" if bool(value) else "false"


def _short_missing(items: Sequence[str], *, limit: int = 5) -> str:
    if not items:
        return "none"
    head = ", ".join(items[:limit])
    if len(items) > limit:
        return f"{head}, ..."
    return head


def _render_markdown(payload: Dict[str, Any]) -> str:
    meta = payload.get("metadata") or {}
    summary = payload.get("summary") or {}
    source = payload.get("source_coverage") or {}
    rows = payload.get("rows") or []
    stage_status = payload.get("stage_artifact_status") or {}
    comparison = payload.get("comparison_design_stub") or {}

    lines: List[str] = [
        "# Analysis Arena Window Replay Readiness",
        "",
        "## 1. Verdict",
        "",
        f"- Scanned windows: `{meta.get('window_count', 0)}`",
        f"- Same-window replay candidates: `{summary.get('same_window_replay_candidates', 0)}`",
        f"- Archived replication ready: `{summary.get('archived_replication_ready', 0)}`",
        f"- Archived replication with caveats: `{summary.get('archived_replication_with_caveats', 0)}`",
        f"- Needs prep: `{summary.get('needs_prep', 0)}`",
        f"- Strongest same-window replay candidate: `{summary.get('strongest_same_window_replay_candidate', '')}`",
        f"- Strongest archived replication candidate: `{summary.get('strongest_archived_replication_candidate', '')}`",
        f"- Stage 6B-through-Stage 7B artifacts present: `{_bool(summary.get('stage6b_to_stage7b_artifacts_present'))}`",
        "",
        "Operational meaning:",
        "",
        "- use same-window replay for regression and before/after comparison",
        "- use archived replication for historical stress testing",
        "- use only true fresh confirmation to unlock Stage 8A consideration",
        "",
        "## 2. Source Coverage",
        "",
        "| Source | Count | Min | Max |",
        "|---|---:|---|---|",
        f"| History workbooks | {source.get('history_date_count', 0)} | `{source.get('history_date_min', '')}` | `{source.get('history_date_max', '')}` |",
        f"| Core results | {source.get('results_date_count', 0)} | `{source.get('results_date_min', '')}` | `{source.get('results_date_max', '')}` |",
        f"| Bonus results | {source.get('bonus_results_date_count', 0)} | `{source.get('bonus_results_date_min', '')}` | `{source.get('bonus_results_date_max', '')}` |",
        f"| Predictive sharepacks | {source.get('predictive_sharepack_date_count', 0)} | `{source.get('predictive_date_min', '')}` | `{source.get('predictive_date_max', '')}` |",
        f"| Truth sharepacks | {source.get('truth_sharepack_date_count', 0)} | `{source.get('truth_date_min', '')}` | `{source.get('truth_date_max', '')}` |",
        "",
        "## 3. Stage 6B Through Stage 7B Artifact Status",
        "",
    ]
    for key, value in stage_status.items():
        lines.append(f"- `{key}`: `{_bool(value)}`")

    lines += [
        "",
        "## 4. Window Readiness Matrix",
        "",
        "| Window | Tier | Status | Files | Tail | Bonus | Recommendation |",
        "|---|---|---|---:|---|---|---|",
    ]
    for row in rows:
        lines.append(
            "| "
            f"`{row.get('window_name', '')}` | "
            f"`{row.get('evidence_tier', '')}` | "
            f"`{row.get('readiness_status', '')}` | "
            f"{row.get('file_count', 0)} | "
            f"`{_bool(row.get('has_full_decay_tail'))}` | "
            f"`{_bool(row.get('has_bonus_tail'))}` | "
            f"`{row.get('recommended_next_use', '')}` |"
        )

    lines += [
        "",
        "## 5. Coverage Caveats",
        "",
    ]
    for row in rows:
        caveats: List[str] = []
        for key in ("history_missing", "predictive_missing", "truth_missing", "results_missing", "tail_missing", "bonus_missing"):
            values = row.get(key) or []
            if values:
                caveats.append(f"{key}={_short_missing(values)}")
        if caveats:
            lines.append(f"- `{row.get('window_name', '')}`: {'; '.join(caveats)}")
    if not any(any(row.get(key) for key in ("history_missing", "predictive_missing", "truth_missing", "results_missing", "tail_missing", "bonus_missing")) for row in rows):
        lines.append("- no coverage caveats detected")

    lines += [
        "",
        "## 6. Baseline Manifest Use",
        "",
        "Before any same-window replay:",
        "",
        "- preserve the existing window root as the baseline",
        "- choose a new run label or output namespace",
        "- compare key artifact hashes and row-level outputs after the rerun",
        "- classify differences as behavior changes, traceability improvements, or naming/reclassification only",
        "",
        "## 7. Replay Comparison Design Stub",
        "",
        "Durable design reference:",
        "",
        "- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_COMPARISON_DESIGN.md`",
        "",
        "Baseline-vs-rerun categories:",
        "",
    ]
    for item in comparison.get("baseline_vs_rerun_categories") or []:
        lines.append(f"- `{item}`")
    lines += [
        "",
        "Stage 6B-through-Stage 7B comparison targets:",
        "",
    ]
    for item in comparison.get("stage6b_to_stage7b_compare_after_rerun") or []:
        lines.append(f"- {item}")
    lines += [
        "",
        "## 8. Hard Boundary",
        "",
        "This report does not run a window and does not grant Stage 8 permission.",
        "Same-window replay and archived-window replication can support development and historical stress testing, but they cannot replace true fresh-window confirmation.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    args = _parse_args()
    runs2_root = _resolve_path(str(args.runs2_root))
    window_roots = [_resolve_path(value) for value in list(args.window_root or [])] or _discover_windows(runs2_root)
    history_root = _resolve_path(str(args.history_root))
    results_root = _resolve_path(str(args.results_root))
    bonus_results_root = _resolve_path(str(args.bonus_results_root))
    predictive_sharepacks_root = _resolve_path(str(args.predictive_sharepacks_root))
    truth_sharepacks_root = _resolve_path(str(args.truth_sharepacks_root))

    defaults = _default_paths()
    out_md = _resolve_path(str(args.out_md)) if args.out_md else defaults["md"]
    out_json = _resolve_path(str(args.out_json)) if args.out_json else defaults["json"]
    out_csv = _resolve_path(str(args.out_csv)) if args.out_csv else defaults["csv"]

    payload = build_payload(
        runs2_root=runs2_root,
        window_roots=window_roots,
        history_root=history_root,
        results_root=results_root,
        bonus_results_root=bonus_results_root,
        predictive_sharepacks_root=predictive_sharepacks_root,
        truth_sharepacks_root=truth_sharepacks_root,
    )
    rows = list(payload.get("rows") or [])

    _write_json(out_json, payload, force=bool(args.force))
    _write_csv(out_csv, rows, force=bool(args.force))
    _write_text(out_md, _render_markdown(payload), force=bool(args.force))

    print(f"[OK] Wrote replay readiness markdown: {safe_rel(out_md)}")
    print(f"[OK] Wrote replay readiness JSON: {safe_rel(out_json)}")
    print(f"[OK] Wrote replay readiness CSV: {safe_rel(out_csv)}")


if __name__ == "__main__":
    main()
