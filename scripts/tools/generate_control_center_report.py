#!/usr/bin/env python3
"""Generate a Control Center performance report (Blackapple + Due Doubles) for a given results file.

Assumes the corresponding Pick3 workbook has already been staged and
`data/cleaned/draws/` contains the Combined/Midday/Evening draw CSVs
(produced via scripts/auxiliary/generate_draws_csv.py).

Usage:
    python3 scripts/tools/generate_control_center_report.py \
        --results-file data/results/2025-06-22.txt \
        --output reports/control_center/2025-06-22.md
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Dict, List, Tuple

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import pandas as pd

from modules.aux_loaders import load_state_draws
from modules.blackapple import analyze_blackapple
from modules.draw_catalog import draws_since_last_double
from modules.module_d_auxiliary_tools.refactored import draws_extractor_p3_columns as column_map
from modules.vtrac_reference import get_vtrac_index
from src.core.aux_config import COMBO_DOUBLE_LATE, COMBO_DOUBLE_VERY_LATE
from src.core.vtrac_family_ranker import rank_double_families

Variant = Tuple[str, str]
VARIANT_SPECS: List[Variant] = [
    ("Combined", "combined"),
    ("Midday", "midday"),
    ("Evening", "evening"),
]

STATE_OVERRIDES: Dict[str, str] = {
    "connecticut": "Connecticut4",
    "delaware": "Delaware4",
    "florida": "Florida4",
    "georgia": "Georgia4",
    "idaho": "Idaho4",
    "illinois": "Illinois4",
    "indiana": "Indiana4",
    "iowa": "Iowa4",
    "kansas": "Kansas4",
    "kentucky": "Kentucky4",
    "louisiana": "Louisiana4",
    "maryland": "Maryland4",
    "michigan": "Michigan4",
    "minnesota": "Minnesota4",
    "mississippi": "Mississippi4",
    "missouri": "Missouri4",
    "nebraska": "Nebraska4",
    "newjersey": "NewJersey4",
    "newmexico": "NewMexico4",
    "newyork": "NewYork4",
    "northcarolina": "NorthCarolina4",
    "ohio": "Ohio4",
    "ontario": "OntarioCanada4",
    "pennsylvania": "Pennsylvania4",
    "puertorico": "PuertoRico4",
    "southcarolina": "SouthCarolina4",
    "tennessee": "Tennessee4",
    "texas": "Texas4",
    "virginia": "Virginia4",
    "washington": "Washington4",
    "washingtondc": "DistrictOfColumbia4",
    "westvirginia": "WestVirginia4",
    "wisconsin": "Wisconsin4",
}


def _normalize(label: str) -> str:
    return "".join(ch for ch in label.lower() if ch.isalnum())


def parse_results(results_path: Path) -> Dict[str, Dict[str, str]]:
    winners: Dict[str, Dict[str, str]] = {}
    for raw_line in results_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.lower().startswith("pick") or line.lower().startswith("midday"):
            continue
        tokens = [tok for tok in line.replace("\t", " ").split(" ") if tok]
        digits = [tok for tok in tokens if tok.isdigit() and len(tok) == 3]
        if not digits:
            continue
        state_part = line
        for tok in digits:
            state_part = state_part.replace(tok, " ")
        state_code = STATE_OVERRIDES.get(_normalize(state_part), None)
        if not state_code:
            continue
        entry: Dict[str, str] = {}
        if digits:
            entry["Midday"] = digits[0]
        if len(digits) >= 2:
            entry["Evening"] = digits[1]
        winners[state_code] = entry
    return winners


def summarize_hits(combo: str, winners: Dict[str, str]) -> Dict[str, str]:
    summary: Dict[str, str] = {}
    combo_sorted = "".join(sorted(combo))
    combo_index = get_vtrac_index(combo)
    for period, winner in winners.items():
        flags = []
        if combo == winner:
            flags.append("Straight")
        winner_sorted = "".join(sorted(winner))
        if combo_sorted == winner_sorted and combo != winner:
            flags.append("Boxed")
        winner_index = get_vtrac_index(winner)
        if combo_index is not None and winner_index is not None and combo_index == winner_index:
            flags.append("VTRAC")
        summary[period] = ", ".join(flags) if flags else "-"
    return summary


def aggregate_period_hits(hits: List[Dict[str, str]]) -> Dict[str, str]:
    agg: Dict[str, List[str]] = {}
    for entry in hits:
        for period, label in entry.items():
            if not label or label == "-":
                continue
            agg.setdefault(period, []).append(label)
    return {period: ", ".join(sorted(set(labels))) if labels else "-" for period, labels in agg.items()}


def render_triggers(triggers: Dict) -> str:
    parts = []
    if not triggers:
        return "-"
    if triggers.get("mirror"):
        parts.append("MIR")
    roots = triggers.get("root_due")
    if roots:
        parts.append(f"RS[{','.join(str(r) for r in roots)}]")
    pattern = triggers.get("pattern", {})
    pat_bits = []
    if pattern.get("extreme_due"):
        pat_bits.append("EXT")
    if pattern.get("mixed_due"):
        pat_bits.append("MIX")
    if pat_bits:
        parts.append("PAT:" + "/".join(pat_bits))
    floating = triggers.get("floating")
    if floating:
        parts.append(f"FLT[{','.join(floating)}]")
    pairs = triggers.get("pairs", {})
    if pairs:
        parts.append(f"PAIR[{pairs.get('remaining_count')}]")
    return ", ".join(parts) if parts else "-"


def format_candidates(candidates: List[Dict]) -> str:
    if not candidates:
        return "-"
    display = []
    for entry in candidates[:5]:
        combo = entry.get("combo", "")
        tags = "/".join(sorted(entry.get("tags", [])))
        if tags:
            display.append(f"{combo}({tags})")
        else:
            display.append(combo)
    return ", ".join(display)


def build_blackapple_table(states: List[str], winners: Dict[str, Dict[str, str]]) -> pd.DataFrame:
    rows = []
    for state in states:
        draws, _ = load_state_draws(state, variant="combined")
        if not draws:
            continue
        try:
            analysis = analyze_blackapple(draws)
        except Exception:
            continue
        candidates = analysis.get("candidates", [])
        hits = []
        for entry in candidates:
            combo = entry.get("combo")
            if not combo:
                continue
            hits.append(summarize_hits(combo, winners.get(state, {})))
        agg_hits = aggregate_period_hits(hits)
        rows.append(
            {
                "State": state,
                "Score": analysis.get("score", 0),
                "Triggers": render_triggers(analysis.get("triggers", {})),
                "#Candidates": len(candidates),
                "Candidates": format_candidates(candidates),
                "Midday Hits": agg_hits.get("Midday", "-"),
                "Evening Hits": agg_hits.get("Evening", "-"),
            }
        )
    if not rows:
        return pd.DataFrame()
    df = pd.DataFrame(rows)
    df.sort_values(["Score", "State"], ascending=[False, True], inplace=True)
    return df


def build_due_doubles_table(states: List[str], winners: Dict[str, Dict[str, str]]) -> pd.DataFrame:
    records = []
    for state in states:
        variant_map = {}
        stats_per_variant = {}
        for title, key in VARIANT_SPECS:
            draws, _ = load_state_draws(state, variant=key)
            if draws:
                variant_map[key] = draws
                ds, last_combo = draws_since_last_double(draws)
                stats_per_variant[key] = (title, ds)
        if not variant_map:
            continue
        rankings = rank_double_families(
            variant_map,
            red_threshold=COMBO_DOUBLE_VERY_LATE,
            blue_threshold=COMBO_DOUBLE_LATE,
            limit=3,
        )
        for key, (title, draws_since) in stats_per_variant.items():
            winners_for_period = {}
            if key == "midday":
                winners_for_period = {"Midday": winners.get(state, {}).get("Midday", "")}
            elif key == "evening":
                winners_for_period = {"Evening": winners.get(state, {}).get("Evening", "")}
            else:
                winners_for_period = winners.get(state, {})
            hits: List[Dict[str, str]] = []
            families_display = []
            for family in rankings:
                members = [m for m in family.get("members", []) if m.get("variant") == key or key == "combined"]
                if not members:
                    continue
                combo_hits = []
                combos_text = []
                for member in members:
                    combo = member.get("combo", "")
                    severity = member.get("severity", "")
                    badge = member.get("variant", "")[:1].upper()
                    combos_text.append(f"{combo}({severity}{badge})")
                    if combo:
                        combo_hits.append(summarize_hits(combo, winners_for_period))
                families_display.append(f"{family.get('label')}: {' '.join(combos_text)}")
                hits.extend(combo_hits)
            agg_hits = aggregate_period_hits(hits)
            records.append(
                {
                    "State": state,
                    "Variant": title,
                    "Draws Since Double": draws_since,
                    "Families": "; ".join(families_display) if families_display else "-",
                    "Midday Hits": agg_hits.get("Midday", "-"),
                    "Evening Hits": agg_hits.get("Evening", "-"),
                }
            )
    if not records:
        return pd.DataFrame()
    df = pd.DataFrame(records)
    df.sort_values(["Draws Since Double", "State", "Variant"], ascending=[False, True, True], inplace=True)
    return df


def generate_report(results_file: Path, output_path: Path) -> None:
    winners = parse_results(results_file)
    states = column_map.get_tracked_states()
    blackapple_df = build_blackapple_table(states, winners)
    due_df = build_due_doubles_table(states, winners)

    lines = [f"# Control Center Report — {results_file.stem}", ""]
    if blackapple_df.empty:
        lines.append("## Blackapple Alerts\nNo Blackapple data available.\n")
    else:
        lines.append("## Blackapple Alerts")
        lines.append("```")
        lines.append(blackapple_df.to_string(index=False))
        lines.append("```")
        lines.append("")
    if due_df.empty:
        lines.append("## Due Doubles\nNo due-doubles data available.\n")
    else:
        lines.append("## Due Doubles")
        lines.append("```")
        lines.append(due_df.to_string(index=False))
        lines.append("```")
        lines.append("")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate Control Center report")
    parser.add_argument("--results-file", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    generate_report(Path(args.results_file), Path(args.output))


if __name__ == "__main__":
    main()
