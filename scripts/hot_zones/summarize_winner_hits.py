#!/usr/bin/env python3
"""
Summarize EB/ES/VB/VS counts per date from reports/stable/hot_zones_winner_hits.json.

Usage:
    PYTHONPATH=.:src python3 scripts/hot_zones/summarize_winner_hits.py
"""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from typing import Dict, Iterable, Tuple

LEDGER_PATH = Path("reports/stable/hot_zones_winner_hits.json")


def _load_rows(path: Path) -> Iterable[Dict]:
    try:
        with path.open("r", encoding="utf-8") as fh:
            data = json.load(fh)
    except FileNotFoundError as exc:
        raise SystemExit(f"Ledger not found: {path}") from exc
    if not isinstance(data, list):
        raise SystemExit("Ledger JSON must be a list of rows.")
    return data


def _row_flags(row: Dict) -> Tuple[bool, bool, bool, bool]:
    eb_entry = row.get("eb_entry") or {}
    vb_entry = row.get("vb_entry") or {}

    eb = bool(eb_entry)
    es = eb and (eb_entry.get("vt_straight_hits", 0) or 0) > 0
    vb = bool(vb_entry)
    vs = vb and (vb_entry.get("vt_straight_hits", 0) or 0) > 0
    return eb, es, vb, vs


def summarize(rows: Iterable[Dict]) -> Dict[str, Dict[str, int]]:
    summary: Dict[str, Dict[str, int]] = defaultdict(lambda: {"EB": 0, "ES": 0, "VB": 0, "VS": 0})
    for row in rows:
        date = row.get("date")
        if not date:
            raise SystemExit("Ledger row missing 'date'.")
        eb, es, vb, vs = _row_flags(row)
        metrics = summary[date]
        metrics["EB"] += int(eb)
        metrics["ES"] += int(es)
        metrics["VB"] += int(vb)
        metrics["VS"] += int(vs)
    return dict(sorted(summary.items()))


def main() -> None:
    rows = _load_rows(LEDGER_PATH)
    summary = summarize(rows)
    for date, metrics in summary.items():
        print(
            f"{date}  EB={metrics['EB']:02d}  ES={metrics['ES']:02d}  "
            f"VB={metrics['VB']:02d}  VS={metrics['VS']:02d}"
        )


if __name__ == "__main__":
    main()
