#!/usr/bin/env python3
"""
Create a small Markdown digest from winners lens JSON files.

Why this exists:
  - Winners JSON can be very large (thousands of lines). This script extracts a
    paste-friendly summary for template Part A without attaching/pasting the full JSON.

Usage:
  python3 scripts/tools/winners_json_digest.py \
    --winners-dir sharepacks/2025-06-22/Florida4/winners/Florida4 \
    --md-out sharepacks/2025-06-22/Florida4/winners/Florida4/winners_digest.md
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


def normalize_pick3_literal(value: str) -> str:
    digits = "".join(ch for ch in str(value) if ch.isdigit())
    if not digits:
        return ""
    return digits.zfill(3) if len(digits) <= 3 else digits


def canonical_of_literal(literal: str) -> str:
    literal = normalize_pick3_literal(literal)
    if not literal:
        return ""
    return "".join(sorted(literal))


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8", errors="replace"))


def parse_sharepack_context(winners_dir: Path) -> Dict[str, str]:
    """
    Try to infer {results_date, state} from a typical winners directory:
      sharepacks/<D>/<STATE>/winners/<STATE>/
    """
    parts = list(winners_dir.parts)
    out: Dict[str, str] = {}
    try:
        idx = parts.index("sharepacks")
        out["results_date"] = parts[idx + 1]
        out["state"] = parts[idx + 2]
    except Exception:
        pass
    return out


def extract_timestamp_from_name(path: Path) -> str:
    # Typical: Florida4_vtrac13_winner_330_20251221_222111.json
    m = re.search(r"_(\d{8}_\d{6})$", path.stem)
    return m.group(1) if m else path.stem


@dataclass(frozen=True)
class WinnerDigestRow:
    file: str
    timestamp: str
    winner: str
    canonical: str
    index: Any
    rank: Any
    score: Any
    stats_keys: List[str]
    stats_lines: List[str]


def _summarize_stats_dict(stats: Dict[str, Any], *, winner: str, canonical: str, top_n: int) -> List[str]:
    lines: List[str] = []
    for key, value in sorted(stats.items()):
        if not isinstance(value, dict):
            continue
        items: List[Tuple[str, float]] = []
        for k, v in value.items():
            try:
                items.append((str(k), float(v)))
            except Exception:
                continue
        if not items:
            continue
        items.sort(key=lambda kv: (-kv[1], kv[0]))
        top_key, top_val = items[0]

        def val_rank(needle: str) -> tuple[Optional[float], Optional[int]]:
            if not needle or needle not in value:
                return None, None
            try:
                val = float(value[needle])
            except Exception:
                return None, None
            rank = None
            for i, (k, _) in enumerate(items, start=1):
                if k == needle:
                    rank = i
                    break
            return val, rank

        literal_val, literal_rank = val_rank(winner)
        canon_val, canon_rank = val_rank(canonical) if canonical and canonical != winner else (None, None)

        details: List[str] = []
        if literal_val is not None:
            details.append(f"literal {winner}={literal_val} (rank {literal_rank}/{len(items)})")
        if canon_val is not None:
            details.append(f"canonical {canonical}={canon_val} (rank {canon_rank}/{len(items)})")
        details_str = " | ".join(details) if details else "winner=<missing>"

        top_list = ", ".join([f"{k}:{int(v) if v.is_integer() else v}" for k, v in items[:top_n]])
        lines.append(
            f"- {key}: {details_str} | top={top_key}:{int(top_val) if top_val.is_integer() else top_val} | top{top_n}={top_list}"
        )
    return lines


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--winners-dir", required=True, help="Path to sharepacks/<D>/<STATE>/winners/<STATE>")
    ap.add_argument("--md-out", help="Write Markdown digest to this path (otherwise prints to stdout)")
    ap.add_argument("--top-n", type=int, default=5, help="Top N patterns to show per stats dict (default: 5)")
    args = ap.parse_args()

    winners_dir = Path(args.winners_dir)
    if not winners_dir.exists():
        raise SystemExit(f"winners dir not found: {winners_dir}")

    json_files = sorted(winners_dir.glob("*_winner_*.json"))
    if not json_files:
        raise SystemExit(f"No winners JSON files found under: {winners_dir}")

    ctx = parse_sharepack_context(winners_dir)
    header = "# Winners JSON Digest"
    if ctx.get("state") and ctx.get("results_date"):
        header = f"# Winners JSON Digest — {ctx['state']} ({ctx['results_date']})"

    rows: List[WinnerDigestRow] = []
    for jf in json_files:
        data = load_json(jf)
        winner = normalize_pick3_literal(str(data.get("winner_combo") or ""))
        canon = canonical_of_literal(winner)
        ts = str(data.get("timestamp") or extract_timestamp_from_name(jf))
        stats = data.get("stats") or {}
        stats_lines = _summarize_stats_dict(stats, winner=winner, canonical=canon, top_n=args.top_n)
        rows.append(
            WinnerDigestRow(
                file=jf.name,
                timestamp=ts,
                winner=winner or str(data.get("winner_combo") or ""),
                canonical=canon or "-",
                index=data.get("index"),
                rank=data.get("rank"),
                score=data.get("score"),
                stats_keys=sorted(stats.keys()) if isinstance(stats, dict) else [],
                stats_lines=stats_lines,
            )
        )

    lines: List[str] = []
    lines.append(header)
    lines.append("")
    lines.append(f"- winners_dir: `{winners_dir}`")
    if ctx.get("results_date"):
        lines.append(f"- results_date (D): `{ctx.get('results_date')}`")
    lines.append("")

    for row in rows:
        lines.append(f"## {row.file}")
        lines.append(f"- winner {row.winner} (canonical {row.canonical}) | index {row.index} | rank {row.rank} | score {row.score} | ts {row.timestamp}")
        if row.stats_keys:
            lines.append(f"- stats keys: {', '.join(row.stats_keys)}")
        if row.stats_lines:
            lines.extend(row.stats_lines)
        lines.append("")

    md = "\n".join(lines).rstrip() + "\n"
    if args.md_out:
        Path(args.md_out).write_text(md, encoding="utf-8")
    else:
        print(md)


if __name__ == "__main__":
    main()
