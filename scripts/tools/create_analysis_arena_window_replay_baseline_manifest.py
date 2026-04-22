#!/usr/bin/env python3
"""Freeze a baseline manifest before an Analysis Arena replay.

This is a read-only fingerprint of the preserved baseline window plus the
cycle-level Analysis Arena artifacts that the replay comparison will later use.
It exists to catch silent baseline drift before a same-window replay is
interpreted.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.tools.analysis_arena_window_utils import safe_rel


DEFAULT_RUNS2_ROOT = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS_2"
DEFAULT_FINAL_DOCS = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "final docs"
DEFAULT_BASELINE_WINDOW = DEFAULT_RUNS2_ROOT / "WINDOW_2026-03-09_to_2026-03-23"
DEFAULT_STEM = "AAT9_ANALYSIS_ARENA__MARCH_RUN2_BASELINE_MANIFEST"


def _parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--baseline-window-root", default=str(DEFAULT_BASELINE_WINDOW))
    ap.add_argument("--baseline-cycle-root", default=str(DEFAULT_RUNS2_ROOT))
    ap.add_argument("--run-label", default="march_2026_15day_replay_v2")
    ap.add_argument("--evidence-tier", default="same_window_replay")
    ap.add_argument("--out-md", default="")
    ap.add_argument("--out-json", default="")
    ap.add_argument("--out-csv", default="")
    ap.add_argument("--force", action="store_true", help="Overwrite existing outputs.")
    return ap.parse_args()


def _resolve_path(value: str | Path) -> Path:
    path = Path(value).expanduser()
    if not path.is_absolute():
        path = (REPO_ROOT / path).resolve()
    return path


def _default_paths() -> Dict[str, Path]:
    return {
        "md": DEFAULT_FINAL_DOCS / f"{DEFAULT_STEM}.md",
        "json": DEFAULT_FINAL_DOCS / f"{DEFAULT_STEM}.json",
        "csv": DEFAULT_FINAL_DOCS / f"{DEFAULT_STEM}.csv",
    }


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
    fields = ["scope", "path", "size_bytes", "mtime_ns", "sha256"]
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _iter_files(root: Path) -> Iterable[Path]:
    if not root.exists():
        return []
    return sorted(path for path in root.rglob("*") if path.is_file())


def _iter_cycle_files(root: Path) -> Iterable[Path]:
    if not root.exists():
        return []
    return sorted(
        path
        for path in root.glob("ANALYSIS_ARENA__CYCLE__*")
        if path.is_file() and not path.name.startswith("ANALYSIS_ARENA__CYCLE__WINDOW_REPLAY_")
    )


def _record(scope: str, path: Path) -> Dict[str, Any]:
    stat = path.stat()
    return {
        "scope": scope,
        "path": safe_rel(path),
        "size_bytes": stat.st_size,
        "mtime_ns": stat.st_mtime_ns,
        "sha256": _sha256(path),
    }


def _manifest_digest(rows: Sequence[Dict[str, Any]]) -> str:
    digest = hashlib.sha256()
    for row in rows:
        digest.update(json.dumps(row, sort_keys=True, separators=(",", ":")).encode("utf-8"))
        digest.update(b"\n")
    return digest.hexdigest()


def build_payload(
    *,
    baseline_window_root: Path,
    baseline_cycle_root: Path,
    run_label: str,
    evidence_tier: str,
) -> Dict[str, Any]:
    rows: List[Dict[str, Any]] = []
    seen: set[Path] = set()

    for path in _iter_files(baseline_window_root):
        resolved = path.resolve()
        seen.add(resolved)
        rows.append(_record("baseline_window", path))

    for path in _iter_cycle_files(baseline_cycle_root):
        resolved = path.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        rows.append(_record("baseline_cycle", path))

    rows = sorted(rows, key=lambda row: (str(row.get("scope", "")), str(row.get("path", ""))))
    window_count = sum(1 for row in rows if row.get("scope") == "baseline_window")
    cycle_count = sum(1 for row in rows if row.get("scope") == "baseline_cycle")
    total_bytes = sum(int(row.get("size_bytes") or 0) for row in rows)

    blockers: List[str] = []
    if not baseline_window_root.exists():
        blockers.append("baseline window root is missing")
    if not baseline_cycle_root.exists():
        blockers.append("baseline cycle root is missing")
    if not rows:
        blockers.append("baseline manifest contains no files")

    return {
        "schema_version": "analysis_arena_window_replay_baseline_manifest/v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "run_label": run_label,
        "evidence_tier": evidence_tier,
        "baseline_window_root": safe_rel(baseline_window_root),
        "baseline_cycle_root": safe_rel(baseline_cycle_root),
        "status": "baseline_manifest_frozen" if not blockers else "blocked_baseline_manifest_incomplete",
        "stage8_permission": "blocked",
        "summary": {
            "total_files": len(rows),
            "baseline_window_files": window_count,
            "baseline_cycle_files": cycle_count,
            "total_bytes": total_bytes,
            "manifest_sha256": _manifest_digest(rows),
        },
        "blockers": blockers,
        "files": rows,
    }


def _render_markdown(payload: Dict[str, Any]) -> str:
    summary = payload.get("summary") or {}
    blockers = payload.get("blockers") or []
    lines = [
        "# AAT9 Analysis Arena - March Run 2 Baseline Manifest",
        "",
        "## 1. Verdict",
        "",
        f"- run_label: `{payload.get('run_label', '')}`",
        f"- evidence_tier: `{payload.get('evidence_tier', '')}`",
        f"- status: `{payload.get('status', '')}`",
        f"- stage8_permission: `{payload.get('stage8_permission', 'blocked')}`",
        f"- manifest_sha256: `{summary.get('manifest_sha256', '')}`",
        "",
        "## 2. Frozen Roots",
        "",
        f"- baseline_window_root: `{payload.get('baseline_window_root', '')}`",
        f"- baseline_cycle_root: `{payload.get('baseline_cycle_root', '')}`",
        "",
        "## 3. Counts",
        "",
        f"- total_files: `{summary.get('total_files', 0)}`",
        f"- baseline_window_files: `{summary.get('baseline_window_files', 0)}`",
        f"- baseline_cycle_files: `{summary.get('baseline_cycle_files', 0)}`",
        f"- total_bytes: `{summary.get('total_bytes', 0)}`",
        "",
        "## 4. Blockers",
        "",
    ]
    if blockers:
        lines.extend(f"- {item}" for item in blockers)
    else:
        lines.append("- none")
    lines += [
        "",
        "## 5. Guardrail",
        "",
        "- This manifest is a baseline fingerprint only.",
        "- It does not execute Run 2, unlock Stage 8, or modify scoring/candidate/budget logic.",
        "- If the manifest hash changes unexpectedly before interpretation, rerun safety review before trusting comparison results.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    args = _parse_args()
    baseline_window_root = _resolve_path(args.baseline_window_root)
    baseline_cycle_root = _resolve_path(args.baseline_cycle_root)
    defaults = _default_paths()
    out_md = _resolve_path(args.out_md) if str(args.out_md or "").strip() else defaults["md"]
    out_json = _resolve_path(args.out_json) if str(args.out_json or "").strip() else defaults["json"]
    out_csv = _resolve_path(args.out_csv) if str(args.out_csv or "").strip() else defaults["csv"]

    payload = build_payload(
        baseline_window_root=baseline_window_root,
        baseline_cycle_root=baseline_cycle_root,
        run_label=str(args.run_label or "").strip() or "window_replay",
        evidence_tier=str(args.evidence_tier or "").strip() or "same_window_replay",
    )
    rows = list(payload.get("files") or [])
    _write_json(out_json, payload, force=bool(args.force))
    _write_csv(out_csv, rows, force=bool(args.force))
    _write_text(out_md, _render_markdown(payload), force=bool(args.force))

    print(f"[OK] Wrote baseline manifest markdown: {safe_rel(out_md)}")
    print(f"[OK] Wrote baseline manifest JSON: {safe_rel(out_json)}")
    print(f"[OK] Wrote baseline manifest CSV: {safe_rel(out_csv)}")
    if payload.get("blockers"):
        raise SystemExit("Baseline manifest blockers: " + "; ".join(str(item) for item in payload["blockers"]))


if __name__ == "__main__":
    main()
