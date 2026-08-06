#!/usr/bin/env python3
"""Build lightweight day-level training kits for RUNS_2 review.

These kits are human-facing wrappers only. They do not move or rename
canonical evidence. They create link-rich folders under a window's
`TRAINING_KITS/` directory so review can move from:

- Arena orientation docs
- day-level macro artifacts
- per-state Brain 1 / truth-side artifacts

without manual path hunting.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
from urllib.parse import quote
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


REPO_ROOT = Path(__file__).resolve().parents[2]
FINAL_DOCS = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "final docs"
RUNS_ROOT = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"
RUNS2_ROOT = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS_2"
REPORTS_ROOT = REPO_ROOT / "reports"
PREDICTIVE_ROOT = REPO_ROOT / "sharepacks" / "_predictive"


@dataclass
class StateKit:
    state_key: str
    state_dir: Path
    validation_md: Path
    predictive_wrapper_md: Path
    winners_html: list[Path]


def rel_link(src_file: Path, target: Path) -> str:
    rel = os.path.relpath(target.resolve(), src_file.parent.resolve()).replace("\\", "/")
    return quote(rel, safe="/.-_~")


def link(src_file: Path, label: str, path: Path) -> str:
    return f"- [{label}]({rel_link(src_file, path)})"


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def read_scoreboard_states(scoreboard_csv: Path) -> list[str]:
    with scoreboard_csv.open(newline="", encoding="utf-8") as fh:
        return [row["state_key"] for row in csv.DictReader(fh)]


def first_existing(paths: Iterable[Path]) -> Path | None:
    for path in paths:
        if path.exists():
            return path
    return None


def window_artifact(window_root: Path, suffix: str) -> Path:
    return window_root / f"{window_root.name}__ANALYSIS_ARENA__{suffix}"


def load_csv_rows(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        return list(reader.fieldnames or []), list(reader)


def filter_rows_by_date(rows: list[dict[str, str]], date_str: str) -> list[dict[str, str]]:
    return [row for row in rows if row.get("date") == date_str]


def collect_state_kit(window_root: Path, date_str: str, state_key: str) -> StateKit:
    predictive_state_dir = PREDICTIVE_ROOT / date_str / state_key
    validation_md = window_root / "VALIDATION" / f"{date_str}__{state_key}.md"
    predictive_wrapper_md = (
        window_root / "PREDICTIVE" / f"{date_str}__{state_key}__PREDICTIVE__tool_only__arena_v0.md"
    )
    winners_dir = (
        REPORTS_ROOT / "stable" / "winners_by_date_fixed" / date_str / state_key
    )
    winners_html = sorted(winners_dir.glob("*.html")) if winners_dir.exists() else []
    return StateKit(
        state_key=state_key,
        state_dir=predictive_state_dir,
        validation_md=validation_md,
        predictive_wrapper_md=predictive_wrapper_md,
        winners_html=winners_html,
    )


def build_reference_orientation_kit(window_root: Path) -> None:
    out_dir = window_root / "TRAINING_KITS" / "REFERENCE__ARENA_ORIENTATION"
    out_file = out_dir / "START_HERE.md"
    lines = [
        "# Arena Orientation Kit",
        "",
        "Use this kit when you want the branch-level explanation first, before reviewing a day or state.",
        "",
        "## Core Orientation",
        "",
        link(out_file, "Analysis Arena System Map", FINAL_DOCS / "AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md"),
        link(out_file, "Analysis Arena Operating Flow", FINAL_DOCS / "AAT9_ANALYSIS_ARENA_OPERATING_FLOW__FRESH_RUNS.md"),
        link(out_file, "RUNS_2 Artifact Review Map", FINAL_DOCS / "AAT9_ANALYSIS_ARENA__RUNS2_ARTIFACT_REVIEW_MAP.md"),
        link(out_file, "Metric Legend", FINAL_DOCS / "AAT9_ANALYSIS_ARENA__METRIC_LEGEND.md"),
        "",
        "## Brain 1 / Feed Contracts",
        "",
        link(out_file, "Aggregated Analysis Arena Contract", FINAL_DOCS / "AAT9_AGGREGATED_ANALYSIS_ARENA_CONTRACT_v0.md"),
        link(out_file, "String Tool -> Arena Feed", FINAL_DOCS / "AAT9_FINAL_STRING_TOOL_OUTPUTS__ANALYSIS_ARENA_FEED.md"),
        link(out_file, "Context Tool -> Arena Feed", FINAL_DOCS / "AAT9_FINAL_CONTEXT_TOOL_OUTPUTS__ANALYSIS_ARENA_FEED.md"),
        "",
        "## Cadence And Reading Order",
        "",
        link(out_file, "Fresh-Runs Cadence Quickstart", FINAL_DOCS / "AAT9_ANALYSIS_ARENA_FRESH_RUNS_CADENCE__QUICKSTART.md"),
        link(out_file, "Window Review Index (March pilot)", window_root / "REVIEW_INDEX.md"),
        "",
        "## What These Docs Answer",
        "",
        "- where Brain 1 ends and the old control arm begins",
        "- what the Arena preserves from each tool",
        "- how Brain 2 ranks and compares states",
        "- why control-arm metrics and Arena metrics must stay separate",
        "- which artifacts are predictive SSOT versus post-results learning surfaces",
        "",
    ]
    write_text(out_file, "\n".join(lines) + "\n")


def build_top_level_index(window_root: Path, date_str: str) -> None:
    out_dir = window_root / "TRAINING_KITS"
    out_file = out_dir / "START_HERE.md"
    custom_hit_report = out_dir / f"{date_str}__CUSTOM_HIT_REPORT" / f"{date_str}__CUSTOM_HIT_REPORT.md"
    lines = [
        "# March Training Kits",
        "",
        "Use this folder when you want the most practical review entry points for the",
        "March pilot window without hunting through the canonical artifact tree first.",
        "",
        "## Primary Entry Points",
        "",
        link(out_file, "Arena Orientation Kit", out_dir / "REFERENCE__ARENA_ORIENTATION" / "START_HERE.md"),
        link(out_file, f"{date_str} Macro Starter Kit", out_dir / f"{date_str}__MACRO_STARTER" / "START_HERE.md"),
        link(out_file, f"{date_str} Custom Hit Report", custom_hit_report),
        link(out_file, f"{date_str} Quantification Stack", out_dir / f"{date_str}__QUANTIFICATION_STACK" / "START_HERE.md"),
        link(out_file, f"{date_str} State Kits", out_dir / f"{date_str}__STATE_KITS" / "START_HERE.md"),
        "",
        "## Direct Window Areas",
        "",
        link(out_file, "Raw ANALYSIS_ARENA folder", window_root / "ANALYSIS_ARENA"),
        link(out_file, "Raw PREDICTIVE folder", window_root / "PREDICTIVE"),
        link(out_file, "Raw VALIDATION folder", window_root / "VALIDATION"),
        link(out_file, "Window root", window_root),
        "",
        "## Suggested Use",
        "",
        "1. Start with the orientation kit if you want the branch/layer explanation.",
        "2. Use the macro starter kit for day-level Brain 2, trackers, and rankings vs hits.",
        "3. Use the quantification stack when you want the formal winner-attribution,",
        "   evidence-utilization, false-positive, stack, and translator-learning audit layer.",
        "4. Use the state kits when you want to drill into one state's Brain 1 surfaces,",
        "   predictive wrappers, and truth-side winner HTML.",
        "",
    ]
    write_text(out_file, "\n".join(lines))


def build_state_kit(window_root: Path, date_str: str, state: StateKit) -> None:
    out_dir = window_root / "TRAINING_KITS" / f"{date_str}__STATE_KITS" / state.state_key
    out_file = out_dir / "START_HERE.md"
    analysis_dir = state.state_dir / "analysis"
    stable_dir = state.state_dir / "stable" / state.state_key
    dr_dir = state.state_dir / "digit_reduction" / state.state_key
    dr_v2_dir = dr_dir / "analyzer_v2"
    hot_dir = state.state_dir / "hot_zones" / state.state_key
    aux_dir = state.state_dir / "aux" / state.state_key
    json_dir = state.state_dir / "json"
    tables_dir = state.state_dir / "tables"

    lines = [
        f"# {date_str} — {state.state_key} Brain 1 State Kit",
        "",
        "This kit is a state-local wrapper. It does not replace canonical evidence.",
        "",
        "## Start With These",
        "",
        link(out_file, "Predictive Review Shell", state.predictive_wrapper_md),
        link(out_file, "Per-State Master Validation", state.validation_md),
    ]

    aggregated_md = analysis_dir / "aggregated_analysis_arena__tool_only__arena_v0.md"
    aggregated_json = analysis_dir / "aggregated_analysis_arena__tool_only__arena_v0.json"
    sandbox_md = analysis_dir / "translation_sandbox_seed__tool_only__arena_v0.md"
    sandbox_json = analysis_dir / "translation_sandbox_seed__tool_only__arena_v0.json"

    lines += [
        "",
        "## Arena Core",
        "",
        link(out_file, "Aggregated Analysis Arena (MD)", aggregated_md),
        link(out_file, "Aggregated Analysis Arena (JSON)", aggregated_json),
        link(out_file, "Translation Sandbox Seed (MD)", sandbox_md),
        link(out_file, "Translation Sandbox Seed (JSON)", sandbox_json),
    ]

    lines += [
        "",
        "## Predictive Tool Surfaces",
        "",
        link(out_file, "Stable Patterns Report (HTML)", stable_dir / f"{state.state_key}_stable_patterns_report.html"),
        link(out_file, "Stable Scores CSV", stable_dir / f"{state.state_key}_stable_patterns_scores.csv"),
        link(out_file, "Stable Families CSV", stable_dir / f"{state.state_key}_stable_patterns_families.csv"),
        link(out_file, "Stable Compound CSV", stable_dir / f"{state.state_key}_stable_patterns_compound.csv"),
        link(out_file, "Stable Metrics JSON", stable_dir / f"{state.state_key}_metrics.json"),
        link(out_file, "Digit Reduction Report (HTML)", dr_dir / f"{state.state_key}_digit_reduction_report.html"),
        link(out_file, "Digit Reduction Stacked Report (HTML)", dr_dir / f"{state.state_key}_digit_reduction_report_stacked.html"),
        link(out_file, "Digit Reduction Scores CSV", dr_dir / f"{state.state_key}_digit_reduction_scores.csv"),
        link(out_file, "Digit Reduction Analyzer Meta", dr_v2_dir / f"{state.state_key}_analyzer_v2_meta.json"),
        link(out_file, "Digit Reduction Top Candidates CSV", dr_v2_dir / f"{state.state_key}_analyzer_v2_top_candidates.csv"),
        link(out_file, "Digit Reduction Per-Item CSV", dr_v2_dir / f"{state.state_key}_analyzer_v2_per_item.csv"),
        link(out_file, "Digit Reduction Stacked Combined", dr_v2_dir / f"{state.state_key}_stacked_combined.html"),
        link(out_file, "Digit Reduction Stacked Midday", dr_v2_dir / f"{state.state_key}_stacked_midday.html"),
        link(out_file, "Digit Reduction Stacked Evening", dr_v2_dir / f"{state.state_key}_stacked_evening.html"),
        link(out_file, "Hot Zones Top Lanes CSV", hot_dir / f"{state.state_key}_hot_zones_top_lanes.csv"),
        link(out_file, "Hot Zones Per-Lane CSV", hot_dir / f"{state.state_key}_hot_zones_per_lane.csv"),
        link(out_file, "Hot Zones Meta JSON", hot_dir / f"{state.state_key}_hot_zones_meta.json"),
        link(out_file, "Hot Zones Winner Map CSV", hot_dir / f"{date_str}_hot_zones_winner_map.csv"),
        link(out_file, "Hot Zones Winner Map JSON", hot_dir / f"{date_str}_hot_zones_winner_map.json"),
        link(out_file, "Aux Summary (MD)", aux_dir / "summary.md"),
        link(out_file, "Aux Summary (JSON)", aux_dir / "summary.json"),
    ]

    vtrac_json = first_existing((state.state_dir / "vtrac" / state.state_key).glob("*.json"))
    if vtrac_json:
        lines.append(link(out_file, "VTRAC Enhanced JSON", vtrac_json))

    lines += [
        "",
        "## Downstream / Control-Arm Bridges",
        "",
        link(out_file, "Signals Bundle JSON", state.state_dir / "signals_bundle__tool_only__arena_v0.json"),
        link(out_file, "Candidate Universe JSON", state.state_dir / "candidate_universe__tool_only__arena_v0.json"),
        link(out_file, "Candidate Universe Evidence (MD)", state.state_dir / "candidate_universe_evidence__tool_only__arena_v0.md"),
        link(out_file, "Candidate Universe Evidence (CSV)", state.state_dir / "candidate_universe_evidence__tool_only__arena_v0.csv"),
        link(out_file, "Play Card (MD)", state.state_dir / "play_card__tool_only__arena_v0.md"),
        link(out_file, "Play Card (JSON)", state.state_dir / "play_card__tool_only__arena_v0.json"),
    ]

    lines += [
        "",
        "## Raw Table / Snapshot Aids",
        "",
        link(out_file, "State README", state.state_dir / "README.md"),
        link(out_file, "Combined Table CSV", tables_dir / "Combined_Combined.csv"),
        link(out_file, "Midday Table CSV", tables_dir / "Midday_Combined.csv"),
        link(out_file, "Evening Table CSV", tables_dir / "Evening_Combined.csv"),
        link(out_file, "Tables JSON Bundle", json_dir / f"{state.state_key}_tables.json"),
    ]

    lines += [
        "",
        "## Winner / Truth-Side HTML",
        "",
    ]
    if state.winners_html:
        for html_path in state.winners_html:
            lines.append(link(out_file, html_path.name, html_path))
    else:
        lines.append("- No stable winner HTML surfaced for this state/date.")

    lines += [
        "",
        "## How To Use This Kit",
        "",
        "1. Start with the predictive review shell and aggregated arena.",
        "2. Use the Stable / DR / Hot Zones links when you want the underlying tool view.",
        "3. Open the per-state Master Validation to compare predictive evidence against the actual winners.",
        "4. Use the winner HTML links when you want the truth-side table view directly.",
        "",
    ]
    write_text(out_file, "\n".join(lines) + "\n")


def build_state_kits_index(window_root: Path, date_str: str, states: list[StateKit]) -> None:
    out_dir = window_root / "TRAINING_KITS" / f"{date_str}__STATE_KITS"
    out_file = out_dir / "START_HERE.md"
    custom_hit_report = (
        window_root
        / "TRAINING_KITS"
        / f"{date_str}__CUSTOM_HIT_REPORT"
        / f"{date_str}__CUSTOM_HIT_REPORT.md"
    )
    lines = [
        f"# {date_str} State Kits",
        "",
        "Use this folder when you want to move from the day-level macro read into per-state Brain 1 and post-draw review.",
        "",
        "## Related Entry Points",
        "",
        link(out_file, "Custom Hit Report", custom_hit_report),
        link(out_file, "Macro Starter", window_root / "TRAINING_KITS" / f"{date_str}__MACRO_STARTER" / "START_HERE.md"),
        link(out_file, "Quantification Stack", window_root / "TRAINING_KITS" / f"{date_str}__QUANTIFICATION_STACK" / "START_HERE.md"),
        link(out_file, "Arena Orientation Kit", window_root / "TRAINING_KITS" / "REFERENCE__ARENA_ORIENTATION" / "START_HERE.md"),
        link(out_file, "Raw PREDICTIVE folder", window_root / "PREDICTIVE"),
        link(out_file, "Raw VALIDATION folder", window_root / "VALIDATION"),
        "",
        "## States",
        "",
    ]
    for state in states:
        lines.append(link(out_file, state.state_key, out_dir / state.state_key / "START_HERE.md"))
    lines.append("")
    write_text(out_file, "\n".join(lines))


def build_quantification_kit(window_root: Path, date_str: str) -> None:
    out_dir = window_root / "TRAINING_KITS" / f"{date_str}__QUANTIFICATION_STACK"
    filters_dir = out_dir / "FILTERED_ROWS"
    out_file = out_dir / "START_HERE.md"

    protocol_md = FINAL_DOCS / "AAT9_ANALYSIS_ARENA__POST_RUN_AUDIT_PROTOCOL.md"
    performance_gap_md = window_artifact(window_root, "PERFORMANCE_GAP.md")
    deep_hit_md = window_artifact(window_root, "DEEP_HIT_ANALYSIS.md")
    hit_roster_csv = window_artifact(window_root, "HIT_ROSTER.csv")
    winner_attr_md = window_artifact(window_root, "WINNER_SIGNAL_ATTRIBUTION_SCORECARD.md")
    winner_attr_csv = window_artifact(window_root, "WINNER_SIGNAL_ATTRIBUTION_LEDGER.csv")
    evidence_audit_md = window_artifact(window_root, "EVIDENCE_UTILIZATION_AUDIT.md")
    evidence_audit_csv = window_artifact(window_root, "EVIDENCE_UTILIZATION_LEDGER.csv")
    stage2_fp_md = window_artifact(window_root, "STAGE2_SIGNAL_FALSE_POSITIVE_SCORECARD.md")
    stage2b_stack_md = window_artifact(window_root, "STAGE2B_SIGNAL_STACK_SCORECARD.md")
    stage2b_pairs_csv = window_artifact(window_root, "STAGE2B_SIGNAL_PAIRING_LEDGER.csv")
    positive_csv = window_artifact(window_root, "POSITIVE_CONVERSION_REGRESSION_SET.csv")
    translator_ledger_md = window_artifact(window_root, "TRANSLATOR_LEARNING_LEDGER.md")
    translator_hyp_md = window_artifact(window_root, "TRANSLATOR_RULE_HYPOTHESIS_QUEUE.md")
    translator_hyp_csv = window_artifact(window_root, "TRANSLATOR_RULE_HYPOTHESIS_QUEUE.csv")
    custom_hit_report = (
        window_root
        / "TRAINING_KITS"
        / f"{date_str}__CUSTOM_HIT_REPORT"
        / f"{date_str}__CUSTOM_HIT_REPORT.md"
    )

    filtered_outputs: list[tuple[str, Path]] = []
    for src_path, out_name in (
        (winner_attr_csv, "winner_signal_attribution__filtered.csv"),
        (evidence_audit_csv, "evidence_utilization__filtered.csv"),
        (stage2b_pairs_csv, "signal_pairing__filtered.csv"),
        (positive_csv, "positive_conversion_regression__filtered.csv"),
    ):
        fieldnames, rows = load_csv_rows(src_path)
        filtered_rows = filter_rows_by_date(rows, date_str)
        out_path = filters_dir / out_name
        write_csv(out_path, fieldnames, filtered_rows)
        filtered_outputs.append((f"{out_name} ({len(filtered_rows)} rows)", out_path))

    lines = [
        f"# {date_str} Quantification Stack",
        "",
        "Use this kit when you want the formal audit layer behind hits, near-hits,",
        "winner alignment, denominator pressure, and signal-stack behavior.",
        "",
        "## Status",
        "",
        "- This audit stack is official and documented.",
        "- It is not just an ad-hoc note or one-off report.",
        "- It is partly downstream of the normal window-close flow rather than fully",
        "  collapsed into one core cadence wrapper.",
        "- That means it should be treated as a durable follow-on audit subsystem,",
        "  not as something you are expected to remember manually.",
        "",
        "## Read These First",
        "",
        link(out_file, "Custom Hit Report", custom_hit_report),
        link(out_file, "Post-Run Audit Protocol", protocol_md),
        link(out_file, "Performance Gap", performance_gap_md),
        link(out_file, "Deep Hit Analysis", deep_hit_md),
        link(out_file, "Winner Signal Attribution Scorecard", winner_attr_md),
        link(out_file, "Evidence Utilization Audit", evidence_audit_md),
        link(out_file, "Stage 2 False-Positive Scorecard", stage2_fp_md),
        link(out_file, "Stage 2B Signal Stack Scorecard", stage2b_stack_md),
        link(out_file, "Translator Learning Ledger", translator_ledger_md),
        "",
        "## Row-Level Drilldowns For This Day",
        "",
    ]
    for label, path in filtered_outputs:
        lines.append(link(out_file, label, path))

    lines += [
        "",
        "## Window-Wide Supporting Files",
        "",
        link(out_file, "Hit Roster CSV", hit_roster_csv),
        link(out_file, "Winner Signal Attribution Ledger", winner_attr_csv),
        link(out_file, "Evidence Utilization Ledger", evidence_audit_csv),
        link(out_file, "Stage 2B Signal Pairing Ledger", stage2b_pairs_csv),
        link(out_file, "Positive Conversion Regression Set", positive_csv),
        link(out_file, "Translator Rule Hypothesis Queue (MD)", translator_hyp_md),
        link(out_file, "Translator Rule Hypothesis Queue (CSV)", translator_hyp_csv),
        "",
        "## What This Kit Answers",
        "",
        "- which signal families aligned with winners on this day",
        "- whether aligned evidence was used, underused, or kept in the wrong lane",
        "- which signals carried too much denominator pressure to promote directly",
        "- which stacks look sharper than their individual parts",
        "- where the Arena preserved truth but the control arm failed to convert it",
        "",
        "## How To Use This Kit",
        "",
        "1. Read `Performance Gap` first to separate Arena truth, control-arm realization,",
        "   and opportunity-gap cases.",
        "2. Read `Winner Signal Attribution` and `Evidence Utilization` together.",
        "3. Use the filtered CSVs for this exact gold day when you want row-level detail",
        "   without scanning the full-window ledgers.",
        "4. Use Stage 2 and Stage 2B scorecards only after you understand the raw day-level",
        "   winner-side and utilization rows.",
        "",
    ]
    write_text(out_file, "\n".join(lines))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--window-root", required=True, help="RUNS_2 window root")
    parser.add_argument("--date", required=True, help="Target results date YYYY-MM-DD")
    args = parser.parse_args()

    window_root = (REPO_ROOT / args.window_root).resolve() if not args.window_root.startswith("/") else Path(args.window_root).resolve()
    date_str = args.date

    scoreboard_csv = window_root / "ANALYSIS_ARENA" / f"{date_str}__BOARD_SCOREBOARD__analysis_arena_day_review.csv"
    if not scoreboard_csv.exists():
        raise SystemExit(f"Missing scoreboard CSV: {scoreboard_csv}")

    build_top_level_index(window_root, date_str)
    build_reference_orientation_kit(window_root)
    build_quantification_kit(window_root, date_str)
    states = [collect_state_kit(window_root, date_str, state_key) for state_key in read_scoreboard_states(scoreboard_csv)]
    build_state_kits_index(window_root, date_str, states)
    for state in states:
        build_state_kit(window_root, date_str, state)

    summary = {
        "window_root": str(window_root),
        "date": date_str,
        "state_count": len(states),
        "top_level_index": str(window_root / "TRAINING_KITS" / "START_HERE.md"),
        "orientation_kit": str(window_root / "TRAINING_KITS" / "REFERENCE__ARENA_ORIENTATION" / "START_HERE.md"),
        "custom_hit_report": str(
            window_root
            / "TRAINING_KITS"
            / f"{date_str}__CUSTOM_HIT_REPORT"
            / f"{date_str}__CUSTOM_HIT_REPORT.md"
        ),
        "quantification_kit": str(window_root / "TRAINING_KITS" / f"{date_str}__QUANTIFICATION_STACK" / "START_HERE.md"),
        "state_kits_index": str(window_root / "TRAINING_KITS" / f"{date_str}__STATE_KITS" / "START_HERE.md"),
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
