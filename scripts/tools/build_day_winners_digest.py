#!/usr/bin/env python3
"""
Build a single, paste-friendly "winners lens" digest for a sharepack day.

Why this exists:
  - The raw winners HTML/JSON artifacts are extremely valuable for reasoning about
    winning pattern progression, but they are too large/noisy to publish in GitHub
    for multi-day deep-research packs.
  - This script creates a compact Markdown view that links:
      results file (Midday/Evening winners)
        -> sharepacks/<D>/<STATE>/winners/<STATE>/*_winner_*.json
        -> a small stats digest per winner (top-N + winner ranks)

Output is intended for:
  - ChatGPT Pro deep research sessions
  - Human scanability (single scroll file per day)

Usage:
  python3 scripts/tools/build_day_winners_digest.py --date 2025-12-30
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
SRC = ROOT / "src"
if SRC.exists() and str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))


def normalize_pick3_literal(value: str) -> str:
    digits = "".join(ch for ch in str(value) if ch.isdigit())
    if not digits:
        return ""
    return digits.zfill(3) if len(digits) <= 3 else digits


def canonical_of_literal(literal: str) -> str:
    literal = normalize_pick3_literal(literal)
    return "".join(sorted(literal)) if literal else ""


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8", errors="replace"))


def parse_timestamp(value: Any) -> str:
    s = str(value or "")
    return s if re.fullmatch(r"\d{8}_\d{6}", s) else ""


def summarize_stats_dict(
    stats: Dict[str, Any],
    *,
    winner: str,
    canonical: str,
    top_n: int,
) -> List[str]:
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

        top_key, top_val = items[0]
        top_list = ", ".join(
            [f"{k}:{int(v) if v.is_integer() else v}" for k, v in items[:top_n]]
        )
        lines.append(
            f"- {key}: {details_str} | top={top_key}:{int(top_val) if top_val.is_integer() else top_val} | top{top_n}={top_list}"
        )
    return lines


@dataclass(frozen=True)
class WinnerJsonSummary:
    path: Path
    winner: str
    canonical: str
    index: Any
    rank: Any
    score: Any
    stats_lines: List[str]
    stamp: str


def select_latest_by_stamp(candidates: List[WinnerJsonSummary]) -> WinnerJsonSummary:
    # Prefer JSON-provided timestamp if present; otherwise use filename suffix.
    def key(row: WinnerJsonSummary) -> tuple[str, str]:
        return (row.stamp, row.path.name)

    return sorted(candidates, key=key)[-1]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", required=True, help="Results date D (sharepacks/<D>/...)")
    ap.add_argument("--out", help="Write digest to this path (default: RUNS/<D>__WINNERS_DIGEST.md)")
    ap.add_argument("--top-n", type=int, default=5, help="Top N patterns per stats dict (default: 5)")
    args = ap.parse_args()

    date = args.date
    day_dir = Path("sharepacks") / date
    if not day_dir.exists():
        raise SystemExit(f"sharepack day not found: {day_dir}")

    results_path = Path("data") / "results" / f"{date}.txt"
    if not results_path.exists():
        raise SystemExit(f"results file not found: {results_path}")

    try:
        from alpha_analytical.control_center import batch_runner as br
    except Exception as exc:  # pragma: no cover
        raise SystemExit(f"Failed to import batch_runner.parse_winner_sheet: {exc}")

    entries = br.parse_winner_sheet(results_path.read_text(encoding="utf-8", errors="replace"))
    winners_by_canonical: Dict[str, Dict[str, Optional[str]]] = {}
    for entry in entries:
        winners_by_canonical[entry.canonical] = {"Midday": entry.midday, "Evening": entry.evening}

    project_to_canonical: Dict[str, str] = {}
    for canonical, candidates in getattr(br, "_PROJECT_STATE_CANDIDATES", {}).items():
        for candidate in candidates:
            project_to_canonical[candidate] = canonical

    meta = {}
    meta_path = day_dir / "control_center" / "meta.json"
    if meta_path.exists():
        try:
            meta = load_json(meta_path)
        except Exception:
            meta = {}

    out_path = Path(args.out) if args.out else (Path("docs") / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS" / f"{date}__WINNERS_DIGEST.md")

    lines: List[str] = []
    lines.append(f"# Winners Lens Digest — {date}")
    lines.append("")
    lines.append(f"- sharepack day: `{day_dir}`")
    lines.append(f"- results file: `{results_path}`")
    if meta:
        history_date = meta.get("history_date")
        history_excel = meta.get("history_excel_path")
        if history_date:
            lines.append(f"- history_date (H): `{history_date}`")
        if history_excel:
            lines.append(f"- history workbook: `{history_excel}`")
    lines.append("")
    lines.append("Notes:")
    lines.append("- Midday/Evening winners come from the results file; Combined is a lens (not a separate draw).")
    lines.append("- This digest summarizes winner JSON stats so it is shareable; raw winners HTML/JSON may be omitted from GitHub packs for size.")
    lines.append("")

    state_dirs = sorted([p for p in day_dir.iterdir() if p.is_dir() and p.name != "control_center"], key=lambda p: p.name)
    for state_dir in state_dirs:
        state = state_dir.name
        canonical_label = project_to_canonical.get(state, state)
        period_winners = winners_by_canonical.get(canonical_label, {})
        midday_winner = normalize_pick3_literal(period_winners.get("Midday") or "")
        evening_winner = normalize_pick3_literal(period_winners.get("Evening") or "")

        winners_dir = state_dir / "winners" / state
        lines.append(f"## {state} ({canonical_label})")
        if not period_winners:
            lines.append("- results: <no entry in results file>")
        else:
            lines.append(f"- results: Midday `{midday_winner or '-'}` | Evening `{evening_winner or '-'}`")
        lines.append(f"- winners_dir: `{winners_dir}`")

        if not winners_dir.exists():
            lines.append("- winners JSON: <missing>")
            lines.append("")
            continue

        json_files = sorted(winners_dir.glob("*_winner_*.json"))
        if not json_files:
            lines.append("- winners JSON: <none>")
            lines.append("")
            continue

        by_winner: Dict[str, List[WinnerJsonSummary]] = {}
        other_files: List[str] = []
        for jf in json_files:
            data = load_json(jf)
            winner_literal = normalize_pick3_literal(str(data.get("winner_combo") or ""))
            if not winner_literal:
                other_files.append(jf.name)
                continue
            canon = canonical_of_literal(winner_literal)
            stamp = parse_timestamp(data.get("timestamp")) or _extract_stamp_from_name(jf.name)
            stats = data.get("stats") or {}
            stats_lines = summarize_stats_dict(stats, winner=winner_literal, canonical=canon, top_n=args.top_n) if isinstance(stats, dict) else []
            by_winner.setdefault(winner_literal, []).append(
                WinnerJsonSummary(
                    path=jf,
                    winner=winner_literal,
                    canonical=canon,
                    index=data.get("index"),
                    rank=data.get("rank"),
                    score=data.get("score"),
                    stats_lines=stats_lines,
                    stamp=stamp,
                )
            )

        def emit(period: str, winner_literal: str) -> None:
            if not winner_literal:
                lines.append(f"- {period}: <no winner>")
                return
            candidates = by_winner.get(winner_literal) or []
            if not candidates:
                lines.append(f"- {period}: winner `{winner_literal}` (canonical `{canonical_of_literal(winner_literal)}`) — JSON <missing>")
                return
            row = select_latest_by_stamp(candidates)
            lines.append(f"### {period} winner `{row.winner}` (canonical `{row.canonical}`) — vtrac index `{row.index}`")
            lines.append(f"- rank `{row.rank}` | score `{row.score}` | file `{row.path.name}`")
            if row.stats_lines:
                lines.extend(row.stats_lines)

        emit("Midday", midday_winner)
        lines.append("")
        emit("Evening", evening_winner)
        lines.append("")

        unmatched = sorted([w for w in by_winner.keys() if w not in {midday_winner, evening_winner}])
        if unmatched:
            lines.append(f"- other winner JSON combos: {', '.join(f'`{u}`' for u in unmatched)}")
        if other_files:
            lines.append(f"- other JSON files: {', '.join(f'`{f}`' for f in sorted(other_files))}")
        lines.append("")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def _extract_stamp_from_name(name: str) -> str:
    stem = name.rsplit(".", 1)[0]
    m = re.search(r"_(\d{8}_\d{6})$", stem)
    return m.group(1) if m else ""


if __name__ == "__main__":
    main()
