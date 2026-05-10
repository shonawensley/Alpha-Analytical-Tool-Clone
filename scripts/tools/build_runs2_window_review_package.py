#!/usr/bin/env python3
"""
Build a human-review package for one Analysis Arena RUNS_2 window.

This adds packaging on top of canonical evidence without moving or renaming
the underlying artifacts. The package is designed for human review first:

- PREDICTIVE/ review shells for each day/state
- REVIEW_INDEX.md
- REVIEW_MANIFEST.json
- CONTROL_ARM_INDEX.md

Canonical evidence remains in place:

- RUNS_2/WINDOW_<...>/ANALYSIS_ARENA/
- RUNS_2/WINDOW_<...>/VALIDATION/
- sharepacks/_predictive/<D>/<STATE>/
- RUNS/ control-arm grades
- window-root learning artifacts
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
from datetime import date as _date
from datetime import datetime, timedelta
from pathlib import Path
from typing import Iterable

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.tools.create_predictive_run_report import build_predictive_run_report

RUNS_ROOT = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"
RUNS2_PREDICTIVE_ROOT = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS_2" / "PREDICTIVE"
FINAL_DOCS_ROOT = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "final docs"

WINDOW_RE = re.compile(r"^WINDOW_(\d{4}-\d{2}-\d{2})_to_(\d{4}-\d{2}-\d{2})$")
STATE_FILE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})__([A-Za-z0-9]+)\.md$")

WINDOW_DIAGNOSTIC_FILES = [
    "ANALYSIS_ARENA__CYCLE__WINDOW_CLOSE__tool_only__arena_v0.md",
    "__ANALYSIS_ARENA__PERFORMANCE_GAP.md",
    "__ANALYSIS_ARENA__PURE_FINALIST_SCORECARD.md",
    "__ANALYSIS_ARENA__TRANSLATOR_LEARNING_LEDGER.md",
    "__ANALYSIS_ARENA__DEEP_HIT_ANALYSIS.md",
    "__ANALYSIS_ARENA__HIT_ROSTER.csv",
    "__ANALYSIS_ARENA__SIGNAL_SOURCE_DICTIONARY.md",
    "__ANALYSIS_ARENA__C1_C2_FRONTIER_ANALYSIS.md",
    "__ANALYSIS_ARENA__C1_C2_FRONTIER_CASES.csv",
    "__ANALYSIS_ARENA__STAGE3_CASEBOOK.md",
    "__ANALYSIS_ARENA__STAGE3_CASEBOOK.csv",
    "__ANALYSIS_ARENA__CASE_DOSSIERS.md",
]


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Build a review package for one RUNS_2 Analysis Arena window.")
    ap.add_argument(
        "--window-root",
        required=True,
        help="Path to RUNS_2/WINDOW_<start>_to_<end> directory",
    )
    ap.add_argument("--sharepacks-root", default="sharepacks/_predictive")
    ap.add_argument("--runs-root", default=str(RUNS_ROOT))
    ap.add_argument("--runs2-predictive-root", default=str(RUNS2_PREDICTIVE_ROOT))
    ap.add_argument("--profile", default="tool_only")
    ap.add_argument("--experiment-tag", default="arena_v0")
    ap.add_argument("--force", action="store_true")
    return ap.parse_args()


def parse_iso_date(value: str) -> _date:
    return _date.fromisoformat(value)


def daterange(start: str, end: str) -> list[str]:
    d0 = parse_iso_date(start)
    d1 = parse_iso_date(end)
    out: list[str] = []
    cur = d0
    while cur <= d1:
        out.append(cur.isoformat())
        cur += timedelta(days=1)
    return out


def safe_rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def rel_link(src_dir: Path, target: Path) -> str:
    return os.path.relpath(target, src_dir).replace("\\", "/")


def md_link(label: str, src_dir: Path, target: Path) -> str:
    return f"[{label}]({rel_link(src_dir, target)})"


def write_text(path: Path, content: str, *, force: bool) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not force:
        raise SystemExit(f"Refusing to overwrite existing file without --force: {safe_rel(path)}")
    path.write_text(content, encoding="utf-8")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def collect_validation_states(validation_dir: Path, start_date: str) -> list[str]:
    states: list[str] = []
    for path in sorted(validation_dir.glob(f"{start_date}__*.md")):
        name = path.name
        if name.endswith("__BRAIN2_MASTER_VALIDATION.md"):
            continue
        if name.endswith("__CONTROL_CENTER.md"):
            continue
        if name.endswith("__DAY_SYNTHESIS.md"):
            continue
        m = STATE_FILE_RE.match(name)
        if not m:
            continue
        state = m.group(2)
        states.append(state)
    return states


def collect_sharepack_states(sharepacks_root: Path, start_date: str) -> list[str]:
    day_dir = sharepacks_root / start_date
    out: list[str] = []
    for path in sorted(day_dir.iterdir()):
        if path.is_dir() and path.name != "control_center":
            out.append(path.name)
    return out


def window_bounds(window_root: Path) -> tuple[str, str]:
    m = WINDOW_RE.match(window_root.name)
    if not m:
        raise SystemExit(f"Window root does not match expected name: {window_root}")
    return m.group(1), m.group(2)


def detect_window_close_files(window_root: Path, start: str, end: str) -> dict[str, str]:
    out: dict[str, str] = {}
    prefix = f"WINDOW_{start}_to_{end}"
    for marker in WINDOW_DIAGNOSTIC_FILES:
        if marker.startswith("ANALYSIS_ARENA__CYCLE__WINDOW_CLOSE"):
            path = window_root / marker
        else:
            path = window_root / f"{prefix}{marker}"
        if path.exists():
            out[path.name] = safe_rel(path)
    return out


def build_control_arm_index(
    *,
    window_root: Path,
    dates: list[str],
    runs_root: Path,
    start: str,
    end: str,
) -> str:
    lines: list[str] = []
    lines.append(f"# March Control-Arm Index — {start} to {end}")
    lines.append("")
    lines.append("Purpose")
    lines.append("- Provide one review surface for the old downstream realized-output arm.")
    lines.append("- Keep Candidate Universe / Play Card grading visible while preserving the rule that this arm is baseline only, not Arena truth.")
    lines.append("")
    lines.append("Interpretation")
    lines.append("- Candidate Universe and Play Card are the old downstream expression surfaces.")
    lines.append("- Use them to compare realized narrowing/expression against what the Arena preserved elsewhere in this package.")
    lines.append("- Do not treat control-arm performance as the definition of Brain 1 or Brain 2 truth.")
    lines.append("")
    lines.append("## Window-Level Entry")
    lines.append("")
    windowed_play_card = runs_root / f"{start}_to_{end}__PLAY_CARD_WINDOWED_GRADE__tool_only__arena_v0__N5.md"
    if windowed_play_card.exists():
        lines.append(f"- Windowed Play Card grade: {md_link(windowed_play_card.name, window_root, windowed_play_card)}")
    else:
        lines.append("- Windowed Play Card grade: _missing_")
    lines.append("")
    lines.append("## Daily Control-Arm Grades")
    lines.append("")
    lines.append("| Date | Candidate Universe | Play Card |")
    lines.append("|---|---|---|")
    for day in dates:
        cu = runs_root / f"{day}__CANDIDATE_UNIVERSE_GRADE__tool_only__arena_v0.md"
        pc = runs_root / f"{day}__PLAY_CARD_GRADE__tool_only__arena_v0.md"
        cu_link = md_link(cu.name, window_root, cu) if cu.exists() else "_missing_"
        pc_link = md_link(pc.name, window_root, pc) if pc.exists() else "_missing_"
        lines.append(f"| `{day}` | {cu_link} | {pc_link} |")
    lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def build_review_index(
    *,
    window_root: Path,
    dates: list[str],
    states: list[str],
    start: str,
    end: str,
    window_close_files: dict[str, str],
) -> str:
    global_guide = FINAL_DOCS_ROOT / "AAT9_ANALYSIS_ARENA__RUNS2_ARTIFACT_REVIEW_MAP.md"
    manifest = window_root / "REVIEW_MANIFEST.json"
    control_arm_index = window_root / "CONTROL_ARM_INDEX.md"
    predictive_dir = window_root / "PREDICTIVE"
    prefix = f"WINDOW_{start}_to_{end}"

    lines: list[str] = []
    lines.append(f"# March Review Index — {start} to {end}")
    lines.append("")
    lines.append("Purpose")
    lines.append("- Give one human-facing navigation surface for the March 15-day Analysis Arena review package.")
    lines.append("- Keep the five-layer model visible while making pre, post, control-arm, and window-close learning artifacts practical to review.")
    lines.append("")
    lines.append("## Core Model")
    lines.append("")
    lines.append(f"- Global 5-layer guide: {md_link(global_guide.name, window_root, global_guide)}")
    lines.append("- Predictive Brain 1 SSOT: state-local Arena evidence under `sharepacks/_predictive/<D>/<STATE>/analysis/`.")
    lines.append("- Predictive Brain 2 SSOT: day-level board/runtime receipts under `ANALYSIS_ARENA/`.")
    lines.append("- Post-results validation SSOT: reverse-engineering reports under `VALIDATION/`.")
    lines.append("- Control-arm comparison SSOT: old downstream grades indexed in `CONTROL_ARM_INDEX.md`.")
    lines.append("- Window-close learning SSOT: March closeout diagnostics at the window root.")
    lines.append("")
    lines.append("## Dual-Performance Model")
    lines.append("")
    lines.append("- Old realized-output control arm: Candidate Universe / Play Card grading and windowed downstream results.")
    lines.append("- Arena-native diagnostic/performance arm: performance gap, pure finalist scorecard, translator ledger, deep-hit analysis, preserved-not-budgeted and opportunity-gap surfaces.")
    lines.append("- Review rule: compare these two arms, but do not blend them. The control arm is baseline expression; the Arena diagnostic arm explains preserved truth and missed conversion opportunity.")
    lines.append("")
    lines.append("## Package Entry Points")
    lines.append("")
    lines.append(f"- Machine manifest: {md_link(manifest.name, window_root, manifest)}")
    lines.append(f"- Control-arm index: {md_link(control_arm_index.name, window_root, control_arm_index)}")
    lines.append("- Generated predictive review shells: `PREDICTIVE/<D>__<STATE>__PREDICTIVE__tool_only__arena_v0.md`")
    if "ANALYSIS_ARENA__CYCLE__WINDOW_CLOSE__tool_only__arena_v0.md" in window_close_files:
        lines.append(
            f"- Window-close cadence receipt: {md_link('ANALYSIS_ARENA__CYCLE__WINDOW_CLOSE__tool_only__arena_v0.md', window_root, window_root / 'ANALYSIS_ARENA__CYCLE__WINDOW_CLOSE__tool_only__arena_v0.md')}"
        )
    for name in [
        f"{prefix}__ANALYSIS_ARENA__PERFORMANCE_GAP.md",
        f"{prefix}__ANALYSIS_ARENA__PURE_FINALIST_SCORECARD.md",
        f"{prefix}__ANALYSIS_ARENA__TRANSLATOR_LEARNING_LEDGER.md",
        f"{prefix}__ANALYSIS_ARENA__DEEP_HIT_ANALYSIS.md",
        f"{prefix}__ANALYSIS_ARENA__STAGE3_CASEBOOK.md",
        f"{prefix}__ANALYSIS_ARENA__SIGNAL_SOURCE_DICTIONARY.md",
    ]:
        path = window_root / name
        if path.exists():
            lines.append(f"- {md_link(name, window_root, path)}")
    doubles_inventory = window_root / "VALIDATION" / f"{start}_to_{end}__DOUBLES_MIRROR_DOUBLES__INVENTORY.md"
    if doubles_inventory.exists():
        lines.append(f"- {md_link(doubles_inventory.name, window_root, doubles_inventory)}")
    lines.append("")
    lines.append("## Recommended Review Order")
    lines.append("")
    lines.append("1. Read the global 5-layer guide and this index.")
    lines.append("2. For any date, start with Brain 2 board posture in `ANALYSIS_ARENA/`.")
    lines.append("3. Move to Brain 2 Master Validation, Control Center, Day Synthesis, and per-state Master Validation in `VALIDATION/`.")
    lines.append("4. Use `PREDICTIVE/` for the generated state-local predictive review shells and copied portfolio triage.")
    lines.append("5. Use `CONTROL_ARM_INDEX.md` when comparing Arena-preserved truth to old downstream expression.")
    lines.append("6. End with the window-close learning surfaces at the root.")
    lines.append("")
    lines.append("## Day-Level Navigation")
    lines.append("")
    lines.append("| Date | Board Review | Scoreboard | Shadow Policy | Brain2 MV | Control Center | Day Synthesis | Predictive Portfolio |")
    lines.append("|---|---|---|---|---|---|---|---|")
    for day in dates:
        board = window_root / "ANALYSIS_ARENA" / f"{day}__BOARD_REVIEW_BUNDLE__analysis_arena_day_review.md"
        score = window_root / "ANALYSIS_ARENA" / f"{day}__BOARD_SCOREBOARD__analysis_arena_day_review.md"
        shadow = window_root / "ANALYSIS_ARENA" / f"{day}__SHADOW_DECISION_POLICY__analysis_arena_day_review.md"
        b2 = window_root / "VALIDATION" / f"{day}__BRAIN2_MASTER_VALIDATION.md"
        cc = window_root / "VALIDATION" / f"{day}__CONTROL_CENTER.md"
        syn = window_root / "VALIDATION" / f"{day}__DAY_SYNTHESIS.md"
        port = predictive_dir / f"{day}__PREDICTIVE_PORTFOLIO__tool_only__arena_v0.md"
        lines.append(
            "| "
            f"`{day}` | "
            f"{md_link('bundle', window_root, board)} | "
            f"{md_link('scoreboard', window_root, score)} | "
            f"{md_link('shadow', window_root, shadow)} | "
            f"{md_link('brain2', window_root, b2)} | "
            f"{md_link('cc', window_root, cc)} | "
            f"{md_link('synth', window_root, syn)} | "
            f"{md_link('portfolio', window_root, port)} |"
        )
    lines.append("")
    lines.append("## State-Local Navigation")
    lines.append("")
    lines.append("- Generated predictive review shells live in `PREDICTIVE/` and follow the pattern:")
    lines.append("  - `<D>__<STATE>__PREDICTIVE__tool_only__arena_v0.md`")
    lines.append("- These predictive shells are review wrappers over canonical sharepack evidence, not new predictive truth artifacts.")
    lines.append("- Post-draw Master Validation lives in `VALIDATION/` and follows the pattern:")
    lines.append("  - `<D>__<STATE>.md`")
    lines.append("- Canonical Brain 1 sharepack evidence remains in:")
    lines.append("  - `sharepacks/_predictive/<D>/<STATE>/analysis/aggregated_analysis_arena__tool_only__arena_v0.{md,json}`")
    lines.append("  - `sharepacks/_predictive/<D>/<STATE>/analysis/translation_sandbox_seed__tool_only__arena_v0.{md,json}`")
    lines.append("")
    lines.append(f"- States in this March package (`{len(states)}`): " + ", ".join(f"`{state}`" for state in states))
    lines.append("")
    lines.append("## Practical Use")
    lines.append("")
    lines.append("- Use the predictive review shell when you want one state/day pre-draw thesis.")
    lines.append("- Use Master Validation when you want the post-draw reverse-engineering view of that same state/day.")
    lines.append("- Use Performance Gap / Pure Finalist / Translator Learning when the question is not “did it hit?” but “what did the Arena preserve that the downstream arm failed to realize?”")
    lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def build_manifest(
    *,
    window_root: Path,
    predictive_dir: Path,
    validation_dir: Path,
    analysis_dir: Path,
    runs_root: Path,
    sharepacks_root: Path,
    runs2_predictive_root: Path,
    dates: list[str],
    states: list[str],
    start: str,
    end: str,
    window_close_files: dict[str, str],
) -> dict:
    generated_at = datetime.now().astimezone().isoformat(timespec="seconds")
    daily: dict[str, dict] = {}
    portfolio_copies = 0
    predictive_shells = 0
    for day in dates:
        day_states: dict[str, dict] = {}
        for state in states:
            predictive_shell = predictive_dir / f"{day}__{state}__PREDICTIVE__tool_only__arena_v0.md"
            if predictive_shell.exists():
                predictive_shells += 1
            state_dir = sharepacks_root / day / state
            analysis_state_dir = state_dir / "analysis"
            day_states[state] = {
                "predictive_review_shell": safe_rel(predictive_shell),
                "predictive_sharepack_dir": safe_rel(state_dir),
                "aggregated_analysis_arena_md": safe_rel(analysis_state_dir / "aggregated_analysis_arena__tool_only__arena_v0.md"),
                "translation_sandbox_seed_md": safe_rel(analysis_state_dir / "translation_sandbox_seed__tool_only__arena_v0.md"),
                "candidate_universe_json": safe_rel(state_dir / "candidate_universe__tool_only__arena_v0.json"),
                "play_card_md": safe_rel(state_dir / "play_card__tool_only__arena_v0.md"),
                "post_draw_master_validation_md": safe_rel(validation_dir / f"{day}__{state}.md"),
            }
        portfolio_copy = predictive_dir / f"{day}__PREDICTIVE_PORTFOLIO__tool_only__arena_v0.md"
        if portfolio_copy.exists():
            portfolio_copies += 1
        daily[day] = {
            "brain2_board": {
                "board_review_bundle_md": safe_rel(analysis_dir / f"{day}__BOARD_REVIEW_BUNDLE__analysis_arena_day_review.md"),
                "board_scoreboard_md": safe_rel(analysis_dir / f"{day}__BOARD_SCOREBOARD__analysis_arena_day_review.md"),
                "board_spillover_overlay_md": safe_rel(analysis_dir / f"{day}__BOARD_SPILLOVER_OVERLAY__analysis_arena_day_review.md"),
                "shadow_decision_policy_md": safe_rel(analysis_dir / f"{day}__SHADOW_DECISION_POLICY__analysis_arena_day_review.md"),
                "translation_sandbox_seed_md": safe_rel(analysis_dir / f"{day}__TRANSLATION_SANDBOX_SEED__analysis_arena_day_review.md"),
            },
            "predictive": {
                "portfolio_review_copy_md": safe_rel(portfolio_copy),
                "canonical_portfolio_md": safe_rel(runs2_predictive_root / portfolio_copy.name),
                "states": day_states,
            },
            "post_validation": {
                "brain2_master_validation_md": safe_rel(validation_dir / f"{day}__BRAIN2_MASTER_VALIDATION.md"),
                "brain2_tracker_ledger_json": safe_rel(validation_dir / f"{day}__BRAIN2_TRACKER_LEDGER.json"),
                "control_center_md": safe_rel(validation_dir / f"{day}__CONTROL_CENTER.md"),
                "day_synthesis_md": safe_rel(validation_dir / f"{day}__DAY_SYNTHESIS.md"),
            },
            "control_arm": {
                "candidate_universe_grade_md": safe_rel(runs_root / f"{day}__CANDIDATE_UNIVERSE_GRADE__tool_only__arena_v0.md"),
                "play_card_grade_md": safe_rel(runs_root / f"{day}__PLAY_CARD_GRADE__tool_only__arena_v0.md"),
            },
        }
    return {
        "package_meta": {
            "status": "march_pilot_review_package",
            "generated_at_local": generated_at,
            "window_root": safe_rel(window_root),
            "generated_predictive_shell_count": predictive_shells,
            "copied_predictive_portfolio_count": portfolio_copies,
            "state_count": len(states),
            "day_count": len(dates),
            "profile": "tool_only",
            "experiment_tag": "arena_v0",
        },
        "window": {
            "name": window_root.name,
            "start_date": start,
            "end_date": end,
            "dates": dates,
            "states": states,
        },
        "layers": [
            {
                "id": "predictive_brain1_ssot",
                "purpose": "Per-state pre-draw Arena evidence.",
                "root": safe_rel(sharepacks_root),
            },
            {
                "id": "predictive_brain2_ssot",
                "purpose": "Cross-state board/runtime receipts before results.",
                "root": safe_rel(analysis_dir),
            },
            {
                "id": "post_results_validation_ssot",
                "purpose": "Per-state and Brain 2 reverse-engineering after results.",
                "root": safe_rel(validation_dir),
            },
            {
                "id": "control_arm_comparison_ssot",
                "purpose": "Old downstream realized-output grading baseline.",
                "root": safe_rel(runs_root),
            },
            {
                "id": "window_close_learning_ssot",
                "purpose": "Cross-day learning and opportunity-gap diagnostics.",
                "root": safe_rel(window_root),
            },
        ],
        "daily": daily,
        "window_close_learning": window_close_files,
        "doubles_window_artifacts": [
            safe_rel(path)
            for path in sorted(validation_dir.glob(f"{start}_to_{end}__DOUBLES_MIRROR_DOUBLES__*"))
        ],
        "residual_gaps": [
            "Predictive review shells are generated wrappers over canonical predictive sharepacks, not new predictive truth artifacts.",
            "Copied predictive portfolio reports in WINDOW_<...>/PREDICTIVE mirror canonical RUNS_2/PREDICTIVE files for review convenience only.",
            "The control arm remains the old downstream realized-output baseline; do not blend it with Arena-preserved truth surfaces.",
        ],
    }


def main() -> None:
    args = parse_args()
    window_root = Path(args.window_root)
    if not window_root.is_absolute():
        window_root = (REPO_ROOT / window_root).resolve()
    sharepacks_root = Path(args.sharepacks_root)
    if not sharepacks_root.is_absolute():
        sharepacks_root = (REPO_ROOT / sharepacks_root).resolve()
    runs_root = Path(args.runs_root)
    if not runs_root.is_absolute():
        runs_root = (REPO_ROOT / runs_root).resolve()
    runs2_predictive_root = Path(args.runs2_predictive_root)
    if not runs2_predictive_root.is_absolute():
        runs2_predictive_root = (REPO_ROOT / runs2_predictive_root).resolve()

    analysis_dir = window_root / "ANALYSIS_ARENA"
    validation_dir = window_root / "VALIDATION"
    predictive_dir = window_root / "PREDICTIVE"
    start, end = window_bounds(window_root)
    dates = daterange(start, end)
    validation_states = collect_validation_states(validation_dir, start)
    sharepack_states = collect_sharepack_states(sharepacks_root, start)
    states = sorted(set(validation_states) & set(sharepack_states))
    if not states:
        raise SystemExit("No overlapping March states found between validation and predictive sharepacks.")

    predictive_dir.mkdir(parents=True, exist_ok=True)

    for day in dates:
        canonical_portfolio = runs2_predictive_root / f"{day}__PREDICTIVE_PORTFOLIO__tool_only__arena_v0.md"
        if canonical_portfolio.exists():
            portfolio_copy = predictive_dir / canonical_portfolio.name
            if portfolio_copy.exists() and not args.force:
                raise SystemExit(f"Refusing to overwrite existing file without --force: {safe_rel(portfolio_copy)}")
            shutil.copy2(canonical_portfolio, portfolio_copy)
        for state in states:
            report = build_predictive_run_report(
                results_date=day,
                state=state,
                profile=args.profile,
                experiment_tag=args.experiment_tag,
                sharepacks_root=sharepacks_root,
            )
            out_path = predictive_dir / f"{day}__{state}__PREDICTIVE__{args.profile}__{args.experiment_tag}.md"
            write_text(out_path, report, force=args.force)

    window_close_files = detect_window_close_files(window_root, start, end)
    control_arm_index = build_control_arm_index(
        window_root=window_root,
        dates=dates,
        runs_root=runs_root,
        start=start,
        end=end,
    )
    write_text(window_root / "CONTROL_ARM_INDEX.md", control_arm_index, force=args.force)

    review_index = build_review_index(
        window_root=window_root,
        dates=dates,
        states=states,
        start=start,
        end=end,
        window_close_files=window_close_files,
    )
    write_text(window_root / "REVIEW_INDEX.md", review_index, force=args.force)

    manifest = build_manifest(
        window_root=window_root,
        predictive_dir=predictive_dir,
        validation_dir=validation_dir,
        analysis_dir=analysis_dir,
        runs_root=runs_root,
        sharepacks_root=sharepacks_root,
        runs2_predictive_root=runs2_predictive_root,
        dates=dates,
        states=states,
        start=start,
        end=end,
        window_close_files=window_close_files,
    )
    write_text(
        window_root / "REVIEW_MANIFEST.json",
        json.dumps(manifest, indent=2, sort_keys=False) + "\n",
        force=args.force,
    )
    print(
        f"Built review package for {window_root.name}: "
        f"{len(dates)} days, {len(states)} states, {len(dates) * len(states)} predictive shells"
    )


if __name__ == "__main__":
    main()
