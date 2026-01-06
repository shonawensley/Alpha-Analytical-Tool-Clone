#!/usr/bin/env python3
"""
Create a corpus-level frequency report for literal doubles vs "mirror doubles" in VTRAC space.

Definition used here (reporting-only):
  - literal double: the winner literal has 2 distinct digits (e.g., 899)
  - literal triple: all digits the same (e.g., 777)
  - mirror-double-ish: the VTRAC reduced signature has repeats (e.g., 489 -> 344 in mod-5 space)

This does NOT assert wagering strategy. It just measures how often these patterns occur so future
"mirror closure" pack-builder ideas can be evaluated with evidence.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, List


ROOT = Path(__file__).resolve().parents[2]


def parse_date(value: str) -> dt.date:
    return dt.date.fromisoformat(value)


def daterange(start: str, end: str) -> List[str]:
    s = parse_date(start)
    e = parse_date(end)
    if e < s:
        raise SystemExit("--end must be >= --start")
    out: List[str] = []
    cur = s
    while cur <= e:
        out.append(cur.isoformat())
        cur += dt.timedelta(days=1)
    return out


def pct(n: int, d: int) -> str:
    return "0.0%" if d == 0 else f"{(100.0 * n / d):.1f}%"


def truthy(value: str) -> bool:
    return str(value).strip() in {"1", "true", "True", "YES", "yes"}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", required=True, help="Start results date D (YYYY-MM-DD)")
    ap.add_argument("--end", required=True, help="End results date D (YYYY-MM-DD)")
    ap.add_argument(
        "--metrics-csv",
        default=str(ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS" / "corpus_tool_metrics.csv"),
        help="Path to corpus_tool_metrics.csv",
    )
    ap.add_argument(
        "--out",
        default=str(ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS" / "2025-12-30_to_2026-01-04__MIRROR_DOUBLE_FREQUENCY.md"),
        help="Output markdown path",
    )
    args = ap.parse_args()

    dates = set(daterange(args.start, args.end))
    metrics_path = Path(args.metrics_csv)
    if not metrics_path.exists():
        raise SystemExit(f"metrics file not found: {metrics_path}")
    try:
        metrics_display = str(metrics_path.relative_to(ROOT))
    except Exception:
        metrics_display = str(metrics_path)

    rows: List[Dict[str, str]] = []
    with metrics_path.open(encoding="utf-8", errors="replace", newline="") as f:
        dr = csv.DictReader(f)
        for row in dr:
            if row.get("date") in dates and row.get("winner_literal"):
                rows.append(row)

    total = len(rows)

    literal_counts = Counter()
    mirror_counts = Counter()
    by_state = defaultdict(lambda: Counter())
    examples_mirror_only: List[Dict[str, str]] = []

    for r in rows:
        winner = r.get("winner_literal", "")
        if truthy(r.get("winner_is_triple", "")):
            literal = "triple"
        elif truthy(r.get("winner_is_double", "")):
            literal = "double"
        else:
            literal = "single"
        literal_counts[literal] += 1

        mirror = "mirror_repeat" if truthy(r.get("winner_vtrac_signature_has_repeat", "")) else "mirror_distinct"
        mirror_counts[mirror] += 1

        state = r.get("state", "")
        by_state[state][literal] += 1
        by_state[state][mirror] += 1

        if mirror == "mirror_repeat" and literal == "single":
            examples_mirror_only.append(r)

    examples_mirror_only.sort(key=lambda r: (r.get("date", ""), r.get("state", ""), r.get("period", "")))

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    lines: List[str] = []
    lines.append(f"# Mirror‑Double Frequency — {args.start} → {args.end}")
    lines.append("")
    lines.append("This report measures how often winners show *repeat structure* in VTRAC‑space even when they are not literal doubles.")
    lines.append("")
    lines.append(f"- metrics: `{metrics_display}`")
    lines.append(f"- total outcomes: **{total}** (state×period rows)")
    lines.append("")

    lines.append("## Literal winner composition")
    lines.append("")
    lines.append("| Type | Count | % |")
    lines.append("|---|---:|---:|")
    for key in ["single", "double", "triple"]:
        n = literal_counts.get(key, 0)
        lines.append(f"| {key} | {n} | {pct(n, total)} |")
    lines.append("")

    lines.append("## VTRAC‑signature repeats (mirror‑double‑ish)")
    lines.append("")
    n_repeat = mirror_counts.get("mirror_repeat", 0)
    lines.append(f"- signature has repeats: **{n_repeat}/{total}** ({pct(n_repeat, total)})")
    n_mirror_only = len(examples_mirror_only)
    lines.append(f"- mirror‑repeat but literal SINGLE: **{n_mirror_only}/{total}** ({pct(n_mirror_only, total)})")
    lines.append("")

    lines.append("## Per‑state frequency (mirror‑repeat)")
    lines.append("")
    lines.append("| State | Outcomes | mirror_repeat | % | literal_double | % |")
    lines.append("|---|---:|---:|---:|---:|---:|")
    for state in sorted(by_state.keys()):
        c = by_state[state]
        outcomes = c.get("single", 0) + c.get("double", 0) + c.get("triple", 0)
        mr = c.get("mirror_repeat", 0)
        ld = c.get("double", 0)
        lines.append(f"| {state} | {outcomes} | {mr} | {pct(mr, outcomes)} | {ld} | {pct(ld, outcomes)} |")
    lines.append("")

    lines.append("## Examples (mirror‑repeat but not literal double)")
    lines.append("")
    if not examples_mirror_only:
        lines.append("- <none>")
        lines.append("")
    else:
        lines.append("| date | state | period | winner | canonical | vtrac_sig | vtrac_index |")
        lines.append("|---|---|---|---|---|---|---:|")
        for r in examples_mirror_only[:60]:
            lines.append(
                "| "
                + " | ".join(
                    [
                        r.get("date", ""),
                        r.get("state", ""),
                        r.get("period", ""),
                        r.get("winner_literal", ""),
                        r.get("winner_canonical", ""),
                        r.get("winner_vtrac_signature", ""),
                        r.get("winner_vtrac_index", ""),
                    ]
                )
                + " |"
            )
        lines.append("")

    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
