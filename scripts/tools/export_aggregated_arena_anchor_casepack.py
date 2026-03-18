#!/usr/bin/env python3
"""Export a compact casepack for the strongest aggregated-arena anchors.

This is intentionally diagnostic only. It reads one arena review scoreboard,
selects the highest-value underweighted / conversion-gap rows, and emits a
markdown casepack with direct artifact paths for follow-up review.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple


REPO_ROOT = Path(__file__).resolve().parents[2]
RUNS_DIR = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"


def _to_int(value: object, default: int = 0) -> int:
    try:
        text = str(value or "").strip()
        if not text:
            return int(default)
        return int(float(text))
    except Exception:
        return int(default)


def _load_rows(path: Path) -> List[Dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        return [dict(row) for row in csv.DictReader(fh)]


def _resolve_repo_path(raw: str) -> Optional[Path]:
    text = str(raw or "").strip()
    if not text:
        return None
    path = REPO_ROOT / text
    return path if path.exists() else None


def _winner_artifacts(state_dir: Path, state_key: str, winner: str, winner_vtrac_index: str) -> List[Path]:
    winners_dir = state_dir / "winners" / state_key
    if not winners_dir.exists():
        return []
    found: List[Path] = []
    digest = winners_dir / "digest.md"
    if digest.exists():
        found.append(digest)
    pattern = f"*vtrac{winner_vtrac_index}_winner_{winner}_*"
    found.extend(sorted(winners_dir.glob(pattern + ".html")))
    found.extend(sorted(winners_dir.glob(pattern + ".json")))
    return found


def _score_key(row: Dict[str, str]) -> Tuple[int, int, int, int, str, str, str]:
    context_flag = 1 if any(str(row.get(key) or "").strip() == "1" for key in (
        "winner_canonical_context_reinforced",
        "winner_vtrac_context_reinforced",
        "winner_family_context_reinforced",
    )) else 0
    return (
        _to_int(row.get("arena_vtrac_rank"), 999),
        _to_int(row.get("arena_family_rank"), 999),
        _to_int(row.get("arena_canonical_rank"), 999),
        -context_flag,
        str(row.get("date") or ""),
        str(row.get("state_key") or ""),
        str(row.get("outcome") or ""),
    )


def _pick_rows(rows: Sequence[Dict[str, str]], *, gap_detail: str, limit: int) -> List[Dict[str, str]]:
    picked = [row for row in rows if str(row.get("gap_detail") or "") == gap_detail]
    picked.sort(key=_score_key)
    return picked[:limit]


def _emit_section(lines: List[str], *, title: str, rows: Sequence[Dict[str, str]]) -> None:
    lines.append(f"## {title}")
    lines.append("")
    if not rows:
        lines.append("_None_")
        lines.append("")
        return
    for row in rows:
        state_dir = REPO_ROOT / "sharepacks" / str(row.get("date") or "") / str(row.get("state_key") or "")
        arena_path = _resolve_repo_path(row.get("arena_path", ""))
        arena_md = arena_path.with_suffix(".md") if arena_path is not None else None
        candidate_universe = state_dir / "candidate_universe__tool_only.json"
        play_card = state_dir / "play_card__tool_only.json"
        winners = _winner_artifacts(
            state_dir=state_dir,
            state_key=str(row.get("state_key") or ""),
            winner=str(row.get("winner") or ""),
            winner_vtrac_index=str(row.get("winner_vtrac_index") or ""),
        )
        context_flag = "Y" if any(str(row.get(key) or "").strip() == "1" for key in (
            "winner_canonical_context_reinforced",
            "winner_vtrac_context_reinforced",
            "winner_family_context_reinforced",
        )) else "N"
        lines.append(
            f"### {row.get('date','')} / {row.get('state_key','')} / {row.get('outcome','')} / {row.get('winner','')} / VT {row.get('winner_vtrac_index','')}"
        )
        lines.append(
            f"- gap: `{row.get('gap_class') or '-'}` / `{row.get('gap_detail') or '-'}` | canonical_rank: `{row.get('arena_canonical_rank') or '-'}` | vtrac_rank: `{row.get('arena_vtrac_rank') or '-'}` | family_rank: `{row.get('arena_family_rank') or '-'}` | context_reinforced: `{context_flag}`"
        )
        lines.append(
            f"- downstream: CU literal `{row.get('candidate_universe_straight_present') or '0'}/{row.get('candidate_universe_box_present') or '0'}` | Play Card literal `{row.get('play_card_straight_present') or '0'}/{row.get('play_card_box_present') or '0'}`"
        )
        lines.append(
            f"- dominant regime: canonical `{row.get('arena_dominant_canonical') or '-'}` | vtrac `{row.get('arena_dominant_vtrac_index') or '-'}` | family `{row.get('arena_dominant_family') or '-'}`"
        )
        if arena_path is not None:
            lines.append(f"- arena_json: `{arena_path}`")
        if arena_md is not None and arena_md.exists():
            lines.append(f"- arena_md: `{arena_md}`")
        if candidate_universe.exists():
            lines.append(f"- candidate_universe: `{candidate_universe}`")
        if play_card.exists():
            lines.append(f"- play_card: `{play_card}`")
        for path in winners:
            lines.append(f"- winner_artifact: `{path}`")
        lines.append("")


def build_casepack(*, review_csv: Path, out_md: Path, per_section_limit: int) -> None:
    rows = _load_rows(review_csv)
    sections = [
        ("Lane Alive Literal Missing Top3", _pick_rows(rows, gap_detail="lane_alive_literal_missing_top3", limit=per_section_limit)),
        ("Lane Alive Literal Missing Top5", _pick_rows(rows, gap_detail="lane_alive_literal_missing_top5", limit=per_section_limit)),
        ("Family Alive Literal Missing Top5", _pick_rows(rows, gap_detail="family_alive_literal_missing_top5", limit=per_section_limit)),
        ("Context Reinforced Underweighted", _pick_rows(rows, gap_detail="context_reinforced_underweighted", limit=per_section_limit)),
        ("Thin Conversion Gap", _pick_rows(rows, gap_detail="thin_conversion_gap", limit=per_section_limit)),
    ]

    lines: List[str] = []
    lines.append("# Aggregated Arena Anchor Casepack")
    lines.append("")
    lines.append("- Purpose: preserve the strongest arena-native anchor rows from the current frozen-window review.")
    lines.append(f"- Review scoreboard: `{review_csv}`")
    lines.append(f"- Per-section limit: `{per_section_limit}`")
    lines.append("")
    for title, picked in sections:
        _emit_section(lines, title=title, rows=picked)

    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Export a compact aggregated-arena anchor casepack.")
    ap.add_argument(
        "--review-csv",
        default=str(RUNS_DIR / "2025-12-30_to_2026-01-04__AGGREGATED_ANALYSIS_ARENA__REVIEW.csv"),
    )
    ap.add_argument(
        "--out-md",
        default=str(RUNS_DIR / "2026-03-18__AGGREGATED_ANALYSIS_ARENA__ANCHOR_CASEPACK.md"),
    )
    ap.add_argument("--per-section-limit", type=int, default=8)
    return ap.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    build_casepack(
        review_csv=Path(args.review_csv),
        out_md=Path(args.out_md),
        per_section_limit=int(args.per_section_limit),
    )
    print(f"casepack={args.out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
