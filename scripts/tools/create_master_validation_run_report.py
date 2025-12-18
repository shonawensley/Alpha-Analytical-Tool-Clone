"""
Create a per-date/per-state Master Validation run report Markdown file.

Goal
----
Provide a single artifact you can share with a second analyst (e.g., ChatGPT Pro)
WITHOUT pasting raw CSV/JSON outputs:

- It links to the sharepack artifacts (winners + tool outputs).
- It embeds the per-tool summarizer Markdown blocks (Stable/DR/VTRAC/Hot Zones) if present.
- It provides placeholders to answer Part A + Part 2 questions in one place.
- It includes scaffolding for Part 3 (Aux), Part 4 (candidate pack), and Part 5 (final summary).

This script DOES NOT run analyzers or rebuild tables. It is purely a reporting/helper
utility that stitches together already-generated artifacts.

Usage
-----
python3 scripts/tools/create_master_validation_run_report.py \\
  --date 2025-06-21 \\
  --state OntarioCanada4
"""

from __future__ import annotations

import argparse
from datetime import date as _date
from datetime import timedelta
from pathlib import Path
from typing import Dict, List, Tuple


REPO_ROOT = Path(__file__).resolve().parents[2]


def parse_iso_date(value: str) -> _date:
    try:
        return _date.fromisoformat(value)
    except ValueError as exc:
        raise SystemExit(f"Invalid --date (expected YYYY-MM-DD): {value}") from exc


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def list_winner_artifacts(winners_dir: Path) -> Tuple[List[str], List[str]]:
    if not winners_dir.exists():
        return [], []
    html = sorted([p.name for p in winners_dir.glob("*.html") if "winner" in p.name.lower()])
    json = sorted([p.name for p in winners_dir.glob("*.json") if "winner" in p.name.lower()])
    return html, json


def tool_sharepack_paths(history_date: str, state: str) -> Dict[str, Path]:
    date_root = REPO_ROOT / "sharepacks" / history_date
    base = date_root / state
    return {
        "date_root": date_root,
        "stable": base / "stable" / state,
        "digit_reduction": base / "digit_reduction" / state,
        "vtrac": base / "vtrac" / state,
        "hot_zones": base / "hot_zones" / state,
        "winners": base / "winners" / state,
        "aux": base / "aux" / state,
        "aux_draws": base / "aux" / "draws",
    }


def expected_files_for_tool(state: str) -> Dict[str, Dict[str, List[str]]]:
    """
    Minimal "final outputs" checklist per tool (sharepack-relative).
    This is not exhaustive, but it matches the lean-output contracts and the
    sharepack layouts used by the summarizers.
    """
    return {
        "stable": {
            "brain": [
                f"{state}_stable_patterns_scores.csv",
                f"{state}_stable_patterns_families.csv",
                f"{state}_stable_patterns_compound.csv",
                f"{state}_metrics.json",
                f"{state}_stable_patterns_report.html",
            ],
            "winners": [
                f"{state}_winner_family_spotlight_raw.csv",
                f"{state}_winner_family_spotlight_families.csv",
            ],
        },
        "digit_reduction": {
            "brain": [
                f"{state}_digit_reduction_report.html",
                f"{state}_digit_reduction_report_stacked.html",
                f"{state}_digit_reduction_scores.csv",
                "analyzer_v2/" + f"{state}_analyzer_v2_per_item.csv",
                "analyzer_v2/" + f"{state}_analyzer_v2_top_candidates.csv",
                "analyzer_v2/" + f"{state}_analyzer_v2_meta.json",
                "training/" + f"{state}_digit_reduction_logs.json",
                "training/" + f"{state}_digit_reduction_steps.csv",
            ],
            "winners": [
                "analyzer_v2/winners/*winner_map*.json",
                "analyzer_v2/winners/*winner_flags*.csv",
                "analyzer_v2/winners/*winner_hits*.csv",
            ],
        },
        "vtrac": {
            "brain": [
                f"{state}_vtrac_enhanced_*.json",
                "summary.md",
                "validation_report.json",
                "validation_report.md",
            ],
            "winners": [
                # Centralized winners lens (not emitted by the VTRAC analyzer itself)
                "*vtrac*_winner_*.json",
                "*vtrac*_winner_*.html",
            ],
        },
        "hot_zones": {
            "brain": [
                f"{state}_hot_zones_per_lane.csv",
                f"{state}_hot_zones_top_lanes.csv",
                f"{state}_hot_zones_meta.json",
            ],
            "winners": [
                "*hot_zones_winner_map.json",
                "*hot_zones_winner_map.csv",
            ],
        },
    }


def check_exists(tool_dir: Path, patterns: List[str]) -> List[str]:
    missing: List[str] = []
    for pattern in patterns:
        if "*" in pattern:
            hits = list(tool_dir.glob(pattern))
            if not hits:
                missing.append(pattern)
        else:
            if not (tool_dir / pattern).exists():
                missing.append(pattern)
    return missing


def maybe_embed_summary(tool_dir: Path) -> str:
    summary_path = tool_dir / "summary.md"
    if not summary_path.exists():
        return "_(summary.md not found — run the tool summarizer first)_\n"
    return read_text(summary_path).rstrip() + "\n"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--date",
        required=True,
        help="Sharepack date folder (typically the results/winners date, YYYY-MM-DD)",
    )
    ap.add_argument("--state", required=True, help="State key (e.g., OntarioCanada4)")
    ap.add_argument(
        "--out",
        help="Output Markdown file path (default: docs/AAT9_KIT/FINAL VALIDATION/RUNS/<DATE>__<STATE>.md)",
    )
    ap.add_argument(
        "--force",
        action="store_true",
        help="Overwrite the run report if it already exists (default: refuse to overwrite).",
    )
    args = ap.parse_args()

    sharepack_date = args.date
    state = args.state
    # For the existing sharepacks, the folder date matches the winners/results date.
    # The source workbook is typically "day before"; we compute it for labeling only.
    results_date = parse_iso_date(sharepack_date)
    history_workbook_date = results_date - timedelta(days=1)

    paths = tool_sharepack_paths(sharepack_date, state)

    default_out = (
        REPO_ROOT
        / "docs"
        / "AAT9_KIT"
        / "FINAL VALIDATION"
        / "RUNS"
        / f"{sharepack_date}__{state}.md"
    )
    out_path = Path(args.out) if args.out else default_out
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if out_path.exists() and not args.force:
        raise SystemExit(
            f"Run report already exists: {out_path}. Refusing to overwrite. "
            "Use --force to overwrite or --out to write a new file."
        )

    winners_html, winners_json = list_winner_artifacts(paths["winners"])

    expected = expected_files_for_tool(state)

    lines: List[str] = []
    lines.append(
        f"# Master Validation Run Report — {state} — results {results_date.isoformat()} (history workbook ~ {history_workbook_date.isoformat()})"
    )
    lines.append("")
    lines.append("Reference template:")
    lines.append(f"- `docs/AAT9_KIT/FINAL VALIDATION/final docs/master_validation_FINAL_TEMPLATE_FINAL_VERSION.md`")
    lines.append("")
    lines.append("Sharepack pointers:")
    lines.append(f"- Sharepack root: `sharepacks/{sharepack_date}/{state}/`")
    lines.append(f"- Winners lens: `{paths['winners'].relative_to(REPO_ROOT)}/`")
    lines.append(f"- Stable: `{paths['stable'].relative_to(REPO_ROOT)}/`")
    lines.append(f"- Digit Reduction: `{paths['digit_reduction'].relative_to(REPO_ROOT)}/`")
    lines.append(f"- VTRAC: `{paths['vtrac'].relative_to(REPO_ROOT)}/`")
    lines.append(f"- Hot Zones: `{paths['hot_zones'].relative_to(REPO_ROOT)}/`")
    lines.append(f"- Aux: `{paths['aux'].relative_to(REPO_ROOT)}/`")
    lines.append(f"- Aux draws snapshot: `{paths['aux_draws'].relative_to(REPO_ROOT)}/`")
    lines.append("")

    lines.append("## Part A — Winners HTML/JSON (environment lens)")
    if winners_html:
        lines.append("Winners HTML files (open in browser/editor):")
        for name in winners_html:
            lines.append(f"- `{paths['winners'].relative_to(REPO_ROOT)}/{name}`")
    else:
        lines.append("_No winners HTML found in the winners sharepack folder._")
    lines.append("")
    if winners_json:
        lines.append("Winners JSON files:")
        for name in winners_json:
            lines.append(f"- `{paths['winners'].relative_to(REPO_ROOT)}/{name}`")
    else:
        lines.append("_No winners JSON found in the winners sharepack folder._")
    lines.append("")
    lines.append("Part A answers (fill using the template’s Part A questions):")
    for i in range(1, 15):
        lines.append(f"- Q{i}: …")
    lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Part 2 — Tool-by-tool (paste blocks + answers)")
    lines.append("Paste blocks: the `summary.md` embedded under each tool below is the “evidence dump” (with source labels). Then fill Q1–Q10 for that tool.")
    lines.append("")

    for tool_key, title in [
        ("stable", "Stable"),
        ("digit_reduction", "Digit Reduction"),
        ("vtrac", "VTRAC Analyzer"),
        ("hot_zones", "Hot Zones"),
    ]:
        tool_dir = paths[tool_key]
        lines.append(f"### 2.{title} — {state} — {sharepack_date}")
        lines.append("")
        if not tool_dir.exists():
            lines.append(f"_(Tool folder not found: `{tool_dir.relative_to(REPO_ROOT)}`)_")
            lines.append("")
            continue

        missing_brain = check_exists(tool_dir, expected[tool_key]["brain"])
        if tool_key == "vtrac":
            # Some VTRAC artifacts are date-global (not state-scoped inside the VTRAC folder).
            missing_global = check_exists(
                paths["date_root"],
                ["vtrac_compact_report.json", "vtrac_compact_report.csv", "summary.md", "summary.csv"],
            )
            missing_brain.extend([f"GLOBAL:{m}" for m in missing_global])
        if tool_key == "vtrac":
            missing_winners = check_exists(paths["winners"], expected[tool_key]["winners"])
        else:
            missing_winners = check_exists(tool_dir, expected[tool_key]["winners"])

        lines.append("0) Outputs reviewed")
        lines.append("   - Brain: (see file list below)")
        lines.append("   - Winners: (see file list below)")
        lines.append(f"   - Missing brain?: {', '.join(missing_brain) if missing_brain else 'none'}")
        lines.append(f"   - Missing winners?: {', '.join(missing_winners) if missing_winners else 'none'}")
        lines.append("")
        lines.append("   Summarizer block (embedded from summary.md):")
        lines.append("")
        lines.append("```markdown")
        lines.append(maybe_embed_summary(tool_dir))
        lines.append("```")
        lines.append("")
        lines.append("Tool answers (fill using the template’s Part 2 Q1–Q10 prompts):")
        for i in range(1, 11):
            lines.append(f"- Q{i}: …")
        lines.append("")
        lines.append("---")
        lines.append("")

    lines.append("## 2B — Cross-tool synthesis (after all tools)")
    lines.append("- Shared clusters/signals: …")
    lines.append("- Conflicts/noise: …")
    lines.append("- Aggregator/aux hooks to test next: …")
    lines.append("")

    lines.append("## Part 3 — Aux Features (paste block + answers)")
    lines.append("Paste block: `summary.md` embedded below is the Aux evidence dump (with source labels). Then fill Q1–Q10 using Part 3 prompts in the master template.")
    lines.append("")
    aux_dir = paths["aux"]
    if not aux_dir.exists():
        lines.append(f"_(Aux folder not found: `{aux_dir.relative_to(REPO_ROOT)}` — run `python3 scripts/tools/aux_sharepack_summary.py --date {sharepack_date} --state {state}`)_")
        lines.append("")
    else:
        lines.append(f"Aux draws snapshot dir: `{paths['aux_draws'].relative_to(REPO_ROOT)}/`")
        lines.append("")
        lines.append("0) Outputs reviewed")
        lines.append("   - Draw CSV snapshot: (see aux draws folder)")
        lines.append("   - Evidence dump: summary.md/summary.json")
        lines.append("")
        lines.append("   Summarizer block (embedded from summary.md):")
        lines.append("")
        lines.append("```markdown")
        lines.append(maybe_embed_summary(aux_dir))
        lines.append("```")
        lines.append("")
        lines.append("Part 3 answers (fill using the template’s Part 3 Q1–Q10 prompts):")
        for i in range(1, 11):
            lines.append(f"- Q{i}: …")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Part 4 — Combination / Permutation Translation (candidate pack)")
    lines.append("Use Part 4 prompts in the master template to produce:")
    lines.append("- A small candidate universe per draw (Midday/Evening)")
    lines.append("- Evidence vectors per candidate (tools + aux signals)")
    lines.append("- Coverage mapping (perm-only vs boxed vs VTRAC-straight vs full index-box)")
    lines.append("")
    lines.append("Reference:")
    lines.append("- `TOOLS/VTRAC_REFERENCE_STRAIGHT.MD`")
    lines.append("")
    lines.append("Part 4 notes / answers:")
    lines.append("- Candidate universe (Midday): …")
    lines.append("- Candidate universe (Evening): …")
    lines.append("- Evidence vectors: …")
    lines.append("- Coverage mapping + pack decision: …")
    lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Part 5 — Overall Summary (key insights + fix/future hooks)")
    lines.append("Use Part 5 prompts in the master template to summarize:")
    lines.append("- Pack vs winners (post-hoc)")
    lines.append("- Key environment tags")
    lines.append("- What drove the win (best evidence)")
    lines.append("- Conflicts/miss patterns + fix-now vs fix-later")
    lines.append("")
    lines.append("Part 5 notes / answers:")
    lines.append("- Pack vs winners: …")
    lines.append("- Key tags: …")
    lines.append("- Drivers: …")
    lines.append("- Conflicts: …")
    lines.append("- Fix-now vs fix-later: …")
    lines.append("- Next run: …")
    lines.append("")

    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote: {out_path}")


if __name__ == "__main__":
    main()
