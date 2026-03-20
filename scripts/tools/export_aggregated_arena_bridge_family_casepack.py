#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path
from typing import Dict, Iterable, List


def _window_from_path(path: Path) -> str:
    stem = path.stem
    marker = "__AGGREGATED_ANALYSIS_ARENA__"
    return stem.split(marker, 1)[0] if marker in stem else stem


def _load_rows(paths: Iterable[Path], rule_name: str) -> List[Dict[str, str]]:
    rows: List[Dict[str, str]] = []
    for path in paths:
        if not path.exists():
            continue
        window = _window_from_path(path)
        with path.open(newline="", encoding="utf-8") as handle:
            for row in csv.DictReader(handle):
                if row.get("rule_name") != rule_name:
                    continue
                enriched = dict(row)
                enriched["window"] = window
                rows.append(enriched)
    return rows


def _group_rows(rows: Iterable[Dict[str, str]]) -> Dict[str, List[Dict[str, str]]]:
    grouped: Dict[str, List[Dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[row["source_mix"]].append(row)
    for source_mix in grouped:
        grouped[source_mix].sort(
            key=lambda row: (
                row.get("window", ""),
                row.get("date", ""),
                row.get("state_key", ""),
                row.get("outcome", ""),
            )
        )
    return dict(grouped)


def _profile_counts(rows: Iterable[Dict[str, str]]) -> Dict[str, int]:
    counts = {
        "direct_same_outcome": 0,
        "same_day_precursor_plus_same_day": 0,
        "same_day_carryforward": 0,
        "future_day_decay": 0,
        "miss": 0,
    }
    for row in rows:
        profile = row.get("box_resolution_profile", "") or "miss"
        counts.setdefault(profile, 0)
        counts[profile] += 1
    return counts


def _render_md(grouped: Dict[str, List[Dict[str, str]]], source_mixes: List[str], rule_name: str) -> str:
    lines: List[str] = []
    lines.append("# Aggregated Arena Bridge Family Casepack")
    lines.append("")
    lines.append("- Purpose: inspect bridge families as concrete state/day rows instead of only aggregate scoreboards.")
    lines.append(f"- Rule analyzed: `{rule_name}`")
    lines.append(f"- Families: `{', '.join(source_mixes)}`")
    lines.append("")

    for source_mix in source_mixes:
        rows = grouped.get(source_mix, [])
        lines.append(f"## `{source_mix}`")
        lines.append("")
        if not rows:
            lines.append("- No rows found.")
            lines.append("")
            continue

        counts = _profile_counts(rows)
        lines.append(f"- Rows: `{len(rows)}`")
        lines.append(
            "- Resolution profile: "
            f"`{counts.get('direct_same_outcome', 0)}` direct, "
            f"`{counts.get('same_day_precursor_plus_same_day', 0)}` same-day precursor+same-day, "
            f"`{counts.get('same_day_carryforward', 0)}` carry-forward, "
            f"`{counts.get('future_day_decay', 0)}` future-day decay, "
            f"`{counts.get('miss', 0)}` miss"
        )
        lines.append("")
        lines.append(
            "| window | date | state | outcome | gap_detail | vt_rank | box_profile | first_box_event | "
            "watch_items | watch_canonicals | baseline_literal |"
        )
        lines.append("|---|---|---|---|---|---:|---|---|---:|---:|---:|")
        for row in rows:
            first_box_event = row.get("first_box_event", "") or "-"
            lines.append(
                f"| {row.get('window', '')} | {row.get('date', '')} | {row.get('state_key', '')} | "
                f"{row.get('outcome', '')} | {row.get('gap_detail', '')} | {row.get('arena_vtrac_rank', '')} | "
                f"{row.get('box_resolution_profile', '')} | {first_box_event} | "
                f"{row.get('watch_items_used', '')} | {row.get('watchlist_canonical_count', '')} | "
                f"{row.get('baseline_same_day_literal', '')} |"
            )
        lines.append("")

    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Export bridge family casepacks from measured bridge-study rows.")
    parser.add_argument(
        "--bridge-rows-csv",
        nargs="*",
        default=[],
        help="Measured bridge-study row CSVs.",
    )
    parser.add_argument(
        "--rule-name",
        default="top4_perm",
        help="Rule name to include from the measured bridge-study rows.",
    )
    parser.add_argument(
        "--source-mix",
        nargs="*",
        default=[],
        help="Optional source families to include. Defaults to every family present in the filtered rows.",
    )
    parser.add_argument("--out-md", required=True, help="Markdown casepack output path.")
    args = parser.parse_args()

    paths = [Path(p) for p in args.bridge_rows_csv]
    rows = _load_rows(paths, args.rule_name)
    grouped = _group_rows(rows)
    source_mixes = args.source_mix or sorted(grouped.keys())

    out_md = Path(args.out_md)
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text(_render_md(grouped, source_mixes, args.rule_name), encoding="utf-8")
    print(f"casepack_md={out_md}")
    print(f"families={len(source_mixes)}")


if __name__ == "__main__":
    main()
