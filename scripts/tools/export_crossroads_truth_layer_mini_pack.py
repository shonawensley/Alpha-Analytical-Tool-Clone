#!/usr/bin/env python3
"""
Export a tiny Crossroads "truth layer" bundle for ChatGPT Pro Deep Research.

Why this exists:
- Some Deep Research sessions cannot access non-default git branches.
- Some environments do not reliably open zip archives.

This exporter stages the minimum 7 markdown files that resolve the Crossroads question:
- 5 glass-box traces (the 5 deterministic cases)
- 2 B36 conversion scoreboards (in-sample + OOS guardrail)

It also writes:
- README.md (operator instructions)
- MANIFEST.csv (mechanical access check)
- BUNDLE.md (single-file concatenation of all 7, for one-upload workflows)
- PROMPT.md (copy/paste prompt that references the staged short filenames)
"""

from __future__ import annotations

import argparse
import csv
import shutil
from pathlib import Path
from typing import Dict, List, Tuple

REPO_ROOT = Path(__file__).resolve().parents[2]


def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Export Crossroads truth-layer mini pack (7 files).")
    p.add_argument(
        "--out",
        default=str(REPO_ROOT / "sharepacks" / "_scratch" / "crossroads_truth_layer_mini__2026-01-15"),
        help="Output directory (default: sharepacks/_scratch/crossroads_truth_layer_mini__2026-01-15)",
    )
    p.add_argument("--zip", action="store_true", help="Also create a .zip archive next to the folder.")
    p.add_argument("--force", action="store_true", help="Overwrite output directory if it exists.")
    return p.parse_args()


def _copy_file(
    src: Path, dest: Path, *, manifest_rows: List[Dict[str, object]], missing_ok: bool = False
) -> None:
    if not src.exists() or not src.is_file():
        status = "missing_ok" if missing_ok else "missing"
        manifest_rows.append({"status": status, "src": str(src), "dest": str(dest), "bytes": 0})
        if not missing_ok:
            raise SystemExit(f"Missing required file: {src}")
        return
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)
    manifest_rows.append({"status": "copied", "src": str(src), "dest": str(dest), "bytes": src.stat().st_size})


def _write_manifest(out_dir: Path, manifest_rows: List[Dict[str, object]]) -> None:
    path = out_dir / "MANIFEST.csv"
    cols = ["status", "src", "dest", "bytes"]
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for row in manifest_rows:
            w.writerow({k: row.get(k, "") for k in cols})


def _write_readme(out_dir: Path, staged: List[Tuple[str, str]]) -> None:
    lines: List[str] = []
    lines.append("# Crossroads Truth Layer — Mini Pack (7 files)")
    lines.append("")
    lines.append("Purpose: unblock ChatGPT Pro Deep Research when branch access / zip browsing is unreliable.")
    lines.append("")
    lines.append("## What to upload")
    lines.append("")
    lines.append("Best option (1 file): upload `BUNDLE.md`.")
    lines.append("Alternate option (7 files): upload the individual `*.md` files listed below.")
    lines.append("")
    lines.append("Then paste the prompt from `PROMPT.md` into ChatGPT Pro.")
    lines.append("")
    lines.append("## Files staged (short names)")
    lines.append("")
    for short_name, _ in staged:
        lines.append(f"- `{short_name}`")
    lines.append("")
    lines.append("## Mechanical access check")
    lines.append("")
    lines.append("- Open `MANIFEST.csv` and confirm there are no `missing` rows.")
    lines.append("")
    (out_dir / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def _write_prompt(out_dir: Path, staged: List[Tuple[str, str]]) -> None:
    filenames = [short for short, _ in staged]
    lines: List[str] = []
    lines.append("# ChatGPT Pro — Deep Research Prompt (Crossroads Mini Pack; 7 files)")
    lines.append("")
    lines.append("Mission: resolve the Crossroads question using only the staged truth-layer artifacts:")
    lines.append("- Where do we lose wins? (CU miss vs lane dropped vs exact dropped)")
    lines.append("- What budget geometry does B36 imply (breadth vs depth)?")
    lines.append("- Propose 2 minimal selection-layer changes (no analyzer edits) with explicit promotion gates.")
    lines.append("")
    lines.append("## Access check (must pass; otherwise stop)")
    lines.append("")
    lines.append("Confirm you can open ALL of these files (quote the first line of each):")
    for fn in filenames:
        lines.append(f"- `{fn}`")
    lines.append("")
    lines.append("## Locked constraints")
    lines.append("")
    lines.append("- No analyzer edits (Stable/DR/VTRAC/Hot Zones). Selection-layer only.")
    lines.append("- Budget fixed: B36 (36 lines).")
    lines.append("- Objective: isolation-first (reduce `CU_LANE_BUT_PLAY_MISS`).")
    lines.append("- Guardrail: OOS strict must not regress vs baseline scoreboard.")
    lines.append("")
    lines.append("## Deliverables")
    lines.append("")
    lines.append("1) Bucket frequency table (from the scoreboards + traces).")
    lines.append("2) Mechanical failure signatures per bucket (what exactly happened in selection).")
    lines.append("3) Geometry diagnosis (breadth collapse vs depth collapse) with evidence.")
    lines.append("4) Two minimal selection-layer changes (no analyzers):")
    lines.append("   - what to change (policy/geometry) and where it would live in code,")
    lines.append("   - what exact scoreboard columns should improve,")
    lines.append("   - promotion gate: improves in-sample isolation-first AND does not regress OOS strict.")
    lines.append("")
    (out_dir / "PROMPT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def _write_bundle(out_dir: Path, staged: List[Tuple[str, str]]) -> None:
    sections: List[str] = []
    sections.append("# Crossroads Truth Layer — Mini Bundle (7 files concatenated)")
    sections.append("")
    sections.append("This is a convenience file: it concatenates the 7 staged markdown files so you can upload 1 file.")
    sections.append("")
    for short_name, source_rel in staged:
        src = (REPO_ROOT / source_rel).resolve()
        content = src.read_text(encoding="utf-8")
        sections.append("---")
        sections.append("")
        sections.append(f"## {short_name}")
        sections.append("")
        sections.append(f"Source: `{source_rel}`")
        sections.append("")
        sections.append(content.rstrip())
        sections.append("")
    (out_dir / "BUNDLE.md").write_text("\n".join(sections).rstrip() + "\n", encoding="utf-8")


def _maybe_zip(out_dir: Path) -> Path:
    base = str(out_dir)
    zip_path = shutil.make_archive(base, "zip", root_dir=out_dir)
    return Path(zip_path)


def main() -> None:
    args = _parse_args()
    out_dir = Path(args.out)
    if not out_dir.is_absolute():
        out_dir = (REPO_ROOT / out_dir).resolve()

    if out_dir.exists():
        if not args.force:
            raise SystemExit(f"Output directory exists (use --force): {out_dir}")
        shutil.rmtree(out_dir)

    out_dir.mkdir(parents=True, exist_ok=True)

    staged: List[Tuple[str, str]] = [
        (
            "01_SCOREBOARD_IN_SAMPLE.md",
            "docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15_to_2026-01-22__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINE4_INDEX_TAIL.md",
        ),
        (
            "02_SCOREBOARD_OOS.md",
            "docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-01_to_2026-01-09__CONVERSION_SCOREBOARD__tool_only__stable10__B36__SPINE4_INDEX_TAIL.md",
        ),
        (
            "03_TRACE_CASE1_ONTARIO_MIDDAY.md",
            "docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__GLASS_BOX_TRACE__OntarioCanada4__Midday__v0_2_default_multi_pack_packheavy_spine4_index_tail__B36__stable10.md",
        ),
        (
            "04_TRACE_CASE2_ONTARIO_EVENING.md",
            "docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__GLASS_BOX_TRACE__OntarioCanada4__Evening__v0_2_default_multi_pack_packheavy_spine4_index_tail__B36__stable10.md",
        ),
        (
            "05_TRACE_CASE3_NEWYORK_MIDDAY.md",
            "docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__GLASS_BOX_TRACE__NewYork4__Midday__v0_2_default_multi_pack_packheavy_spine4_index_tail__B36__stable10.md",
        ),
        (
            "06_TRACE_CASE4_DELAWARE_EVENING.md",
            "docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-16__GLASS_BOX_TRACE__Delaware4__Evening__v0_2_default_multi_pack_packheavy_spine4_index_tail__B36__stable10.md",
        ),
        (
            "07_TRACE_CASE5_NORTHCAROLINA_MIDDAY.md",
            "docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__GLASS_BOX_TRACE__NorthCarolina4__Midday__v0_2_default_multi_pack_packheavy_spine4_index_tail__B36__stable10.md",
        ),
    ]

    manifest_rows: List[Dict[str, object]] = []
    for short_name, src_rel in staged:
        src = (REPO_ROOT / src_rel).resolve()
        dest = (out_dir / short_name).resolve()
        _copy_file(src, dest, manifest_rows=manifest_rows)

    _write_bundle(out_dir, staged)
    _write_prompt(out_dir, staged)
    _write_readme(out_dir, staged)
    _write_manifest(out_dir, manifest_rows)

    zip_path = None
    if args.zip:
        zip_path = _maybe_zip(out_dir)

    print(f"[OK] Mini pack written: {out_dir}")
    if zip_path:
        print(f"[OK] Zip archive: {zip_path}")


if __name__ == "__main__":
    main()

