#!/usr/bin/env python3
"""Study bounded arena-to-conversion bridge rules on front-band rows.

This is intentionally research-only. It consumes the front-band review rows and
the aggregated arena artifacts, applies narrow watchlist-based bridge rules, and
grades same-day plus short-horizon closure without touching production
conversion or packaging.
"""

from __future__ import annotations

import argparse
import csv
import itertools
import json
from collections import defaultdict
from pathlib import Path
import sys
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.tools.review_aggregated_analysis_arena_decay import _load_outcomes_for_state

RUNS_DIR = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"

DEFAULT_COHORTS = (
    "aux_overdue+aux_badge",
    "due_doubles+aux_overdue+aux_badge",
    "due_doubles",
)
BRIDGE_ROW_FIELDS = [
    "rule_name",
    "date",
    "state_key",
    "outcome",
    "winner",
    "winner_canonical",
    "gap_detail",
    "source_mix",
    "arena_vtrac_rank",
    "watch_items_used",
    "watchlist_canonical_count",
    "watchlist_exact_count",
    "same_day_box_hit",
    "same_day_exact_hit",
    "within_3d_box_hit",
    "within_3d_exact_hit",
    "first_box_event",
    "first_exact_event",
    "candidate_universe_box_present",
    "candidate_universe_straight_present",
    "play_card_box_present",
    "play_card_straight_present",
    "baseline_same_day_literal",
]
BRIDGE_SUMMARY_FIELDS = [
    "group_type",
    "rule_name",
    "source_mix",
    "rows",
    "avg_watch_items_used",
    "avg_watchlist_canonical_count",
    "same_day_box_hit",
    "same_day_exact_hit",
    "within_3d_box_hit",
    "within_3d_exact_hit",
    "baseline_same_day_literal",
]


def _read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8", errors="replace"))


def _load_csv(path: Path) -> List[Dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        return [dict(row) for row in csv.DictReader(fh)]


def _normalize_literal(value: object) -> str:
    digits = "".join(ch for ch in str(value or "") if ch.isdigit())
    return digits if len(digits) == 3 else ""


def _canon(value: object) -> str:
    lit = _normalize_literal(value)
    return "".join(sorted(lit)) if lit else ""


def _parse_rule(rule_name: str) -> int:
    text = str(rule_name or "").strip().lower()
    if text.startswith("top") and text.endswith("_perm"):
        return int(text.removeprefix("top").removesuffix("_perm"))
    if text.startswith("top"):
        return int(text.removeprefix("top"))
    raise ValueError(f"Unsupported bridge rule: {rule_name}")


def _to_int(value: object) -> Optional[int]:
    text = str(value or "").strip()
    if not text:
        return None
    try:
        return int(text)
    except ValueError:
        return None


def _matches_gate(row: Dict[str, str], *, gap_details: Sequence[str], max_vtrac_rank: Optional[int]) -> bool:
    if gap_details and str(row.get("gap_detail") or "") not in set(gap_details):
        return False
    if max_vtrac_rank is not None:
        rank = _to_int(row.get("arena_vtrac_rank"))
        if rank is None or rank > max_vtrac_rank:
            return False
    return True


def _build_candidate_sets(watchlist: Sequence[Dict[str, Any]], *, top_n: int) -> Tuple[List[Dict[str, Any]], List[str], List[str]]:
    selected = [item for item in watchlist if isinstance(item, dict)][:top_n]
    canonicals: List[str] = []
    exact_literals: List[str] = []
    seen_canons = set()
    seen_literals = set()

    for item in selected:
        for canonical in (item.get("candidate_canonicals") or []):
            text = str(canonical or "").strip()
            if len(text) != 3 or not text.isdigit():
                continue
            if text not in seen_canons:
                seen_canons.add(text)
                canonicals.append(text)
            for perm in set(itertools.permutations(text, 3)):
                literal = "".join(perm)
                if literal not in seen_literals:
                    seen_literals.add(literal)
                    exact_literals.append(literal)
        for literal in (item.get("example_literals") or []):
            text = _normalize_literal(literal)
            if not text:
                continue
            if text not in seen_literals:
                seen_literals.add(text)
                exact_literals.append(text)
            canonical = _canon(text)
            if canonical and canonical not in seen_canons:
                seen_canons.add(canonical)
                canonicals.append(canonical)
    return selected, canonicals, exact_literals


def _first_future_box_event(outcomes, candidate_canonicals: Iterable[str]) -> Tuple[str, str, str]:
    canons = {str(x) for x in candidate_canonicals if str(x).strip()}
    for event in outcomes:
        if event.canonical in canons:
            return event.date, event.outcome, event.winner
    return "", "", ""


def _first_future_exact_event(outcomes, exact_literals: Iterable[str]) -> Tuple[str, str, str]:
    literals = {str(x) for x in exact_literals if str(x).strip()}
    for event in outcomes:
        if event.winner in literals:
            return event.date, event.outcome, event.winner
    return "", "", ""


def build_bridge_rows(
    *,
    front_rows_csv: Path,
    sharepacks_root: Path,
    cohort_mixes: Sequence[str],
    rules: Sequence[str],
    decay_days: int,
    gap_details: Sequence[str],
    max_vtrac_rank: Optional[int],
) -> List[Dict[str, str]]:
    cohort_set = {str(x).strip() for x in cohort_mixes if str(x).strip()}
    rows = _load_csv(front_rows_csv)
    out: List[Dict[str, str]] = []

    for row in rows:
        source_mix = str(row.get("source_mix") or "").strip()
        if cohort_set and source_mix not in cohort_set:
            continue
        if not _matches_gate(row, gap_details=gap_details, max_vtrac_rank=max_vtrac_rank):
            continue
        arena_rel = str(row.get("arena_path") or "").strip()
        if not arena_rel:
            continue
        arena_path = Path(arena_rel)
        if not arena_path.is_absolute():
            candidates = [
                REPO_ROOT / arena_rel,
                front_rows_csv.parent / arena_rel,
                sharepacks_root.parent / arena_rel,
            ]
            arena_path = next((candidate for candidate in candidates if candidate.exists()), candidates[0])
        if not arena_path.exists():
            continue
        arena = _read_json(arena_path)
        watchlist = (arena.get("arena_synthesis") or {}).get("vtrac_literal_watchlist", [])
        outcomes = _load_outcomes_for_state(
            sharepacks_root,
            snapshot_date=str(row.get("date") or ""),
            state_key=str(row.get("state_key") or ""),
            decay_days=decay_days,
        )

        for rule_name in rules:
            top_n = _parse_rule(rule_name)
            selected, candidate_canonicals, exact_literals = _build_candidate_sets(watchlist, top_n=top_n)
            same_day_box_hit = "1" if str(row.get("winner_canonical") or "") in set(candidate_canonicals) else "0"
            same_day_exact_hit = "1" if str(row.get("winner") or "") in set(exact_literals) else "0"
            box_date, box_outcome, box_winner = _first_future_box_event(outcomes, candidate_canonicals)
            exact_date, exact_outcome, exact_winner = _first_future_exact_event(outcomes, exact_literals)

            out.append(
                {
                    "rule_name": rule_name,
                    "date": str(row.get("date") or ""),
                    "state_key": str(row.get("state_key") or ""),
                    "outcome": str(row.get("outcome") or ""),
                    "winner": str(row.get("winner") or ""),
                    "winner_canonical": str(row.get("winner_canonical") or ""),
                    "gap_detail": str(row.get("gap_detail") or ""),
                    "source_mix": source_mix,
                    "arena_vtrac_rank": str(row.get("arena_vtrac_rank") or ""),
                    "watch_items_used": str(len(selected)),
                    "watchlist_canonical_count": str(len(candidate_canonicals)),
                    "watchlist_exact_count": str(len(exact_literals)),
                    "same_day_box_hit": same_day_box_hit,
                    "same_day_exact_hit": same_day_exact_hit,
                    "within_3d_box_hit": "1" if box_date else "0",
                    "within_3d_exact_hit": "1" if exact_date else "0",
                    "first_box_event": f"{box_date} {box_outcome} {box_winner}".strip(),
                    "first_exact_event": f"{exact_date} {exact_outcome} {exact_winner}".strip(),
                    "candidate_universe_box_present": str(row.get("candidate_universe_box_present") or "0"),
                    "candidate_universe_straight_present": str(row.get("candidate_universe_straight_present") or "0"),
                    "play_card_box_present": str(row.get("play_card_box_present") or "0"),
                    "play_card_straight_present": str(row.get("play_card_straight_present") or "0"),
                    "baseline_same_day_literal": "1"
                    if str(row.get("candidate_universe_box_present") or "0") == "1"
                    or str(row.get("candidate_universe_straight_present") or "0") == "1"
                    or str(row.get("play_card_box_present") or "0") == "1"
                    or str(row.get("play_card_straight_present") or "0") == "1"
                    else "0",
                }
            )
    return out


def _group_summary(rows: Sequence[Dict[str, str]], *, key: str) -> List[Dict[str, str]]:
    grouped: Dict[str, List[Dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[str(row.get(key) or "")].append(row)

    out: List[Dict[str, str]] = []
    for group_key, picked in grouped.items():
        den = len(picked)
        if not den:
            continue
        out.append(
            {
                key: group_key,
                "rows": str(den),
                "avg_watch_items_used": f"{sum(int(row['watch_items_used']) for row in picked) / den:.2f}",
                "avg_watchlist_canonical_count": f"{sum(int(row['watchlist_canonical_count']) for row in picked) / den:.2f}",
                "same_day_box_hit": f"{sum(row['same_day_box_hit'] == '1' for row in picked)}/{den}",
                "same_day_exact_hit": f"{sum(row['same_day_exact_hit'] == '1' for row in picked)}/{den}",
                "within_3d_box_hit": f"{sum(row['within_3d_box_hit'] == '1' for row in picked)}/{den}",
                "within_3d_exact_hit": f"{sum(row['within_3d_exact_hit'] == '1' for row in picked)}/{den}",
                "baseline_same_day_literal": f"{sum(row['baseline_same_day_literal'] == '1' for row in picked)}/{den}",
            }
        )
    out.sort(key=lambda row: (row[key],))
    return out


def write_bridge_outputs(
    *,
    rows: Sequence[Dict[str, str]],
    out_rows_csv: Path,
    out_summary_csv: Path,
    out_md: Path,
    cohort_mixes: Sequence[str],
    rules: Sequence[str],
    gap_details: Sequence[str],
    max_vtrac_rank: Optional[int],
) -> None:
    out_rows_csv.parent.mkdir(parents=True, exist_ok=True)
    with out_rows_csv.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=BRIDGE_ROW_FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

    rule_summary = _group_summary(rows, key="rule_name")
    mix_summary = _group_summary(rows, key="source_mix")
    summary_rows = []
    for row in rule_summary:
        merged = dict(row)
        merged["group_type"] = "rule_name"
        summary_rows.append(merged)
    for row in mix_summary:
        merged = dict(row)
        merged["group_type"] = "source_mix"
        summary_rows.append(merged)

    with out_summary_csv.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=BRIDGE_SUMMARY_FIELDS)
        writer.writeheader()
        for row in summary_rows:
            writer.writerow(row)

    lines: List[str] = []
    lines.append("# Aggregated Arena Bridge Study")
    lines.append("")
    lines.append("- Purpose: test bounded watchlist-based lane-to-literal bridge rules on the strongest measured cohorts before any production conversion change.")
    lines.append(f"- Cohort mixes: `{', '.join(cohort_mixes)}`")
    lines.append(f"- Rules: `{', '.join(rules)}`")
    lines.append(f"- Gap details: `{', '.join(gap_details) if gap_details else '-'}`")
    lines.append(f"- Max VTRAC rank: `{max_vtrac_rank if max_vtrac_rank is not None else '-'}`")
    lines.append(f"- Row count: `{len(rows)}`")
    lines.append("")
    lines.append("## Rule Summary")
    lines.append("")
    if rule_summary:
        lines.append("| rule | rows | avg_watch_items | avg_watchlist_canonicals | same_day_box | same_day_exact | within_3d_box | within_3d_exact | baseline_same_day_literal |")
        lines.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|")
        for row in rule_summary:
            lines.append(
                f"| {row['rule_name']} | {row['rows']} | {row['avg_watch_items_used']} | {row['avg_watchlist_canonical_count']} | {row['same_day_box_hit']} | {row['same_day_exact_hit']} | {row['within_3d_box_hit']} | {row['within_3d_exact_hit']} | {row['baseline_same_day_literal']} |"
            )
    else:
        lines.append("_No bridge rows._")
    lines.append("")
    lines.append("## Cohort Summary")
    lines.append("")
    if mix_summary:
        lines.append("| source_mix | rows | avg_watch_items | avg_watchlist_canonicals | same_day_box | same_day_exact | within_3d_box | within_3d_exact | baseline_same_day_literal |")
        lines.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|")
        for row in mix_summary:
            lines.append(
                f"| {row['source_mix']} | {row['rows']} | {row['avg_watch_items_used']} | {row['avg_watchlist_canonical_count']} | {row['same_day_box_hit']} | {row['same_day_exact_hit']} | {row['within_3d_box_hit']} | {row['within_3d_exact_hit']} | {row['baseline_same_day_literal']} |"
            )
    else:
        lines.append("_No cohort rows._")
    lines.append("")
    lines.append("## Notes")
    lines.append("")
    lines.append("- `same_day_*` compares the bridge candidates against the reviewed outcome row itself.")
    lines.append("- `within_3d_*` freezes the same bridge candidates and checks later outcomes for the same state through the next 3 days.")
    lines.append("- `baseline_same_day_literal` is the current downstream literal presence from Candidate Universe / Play Card for the same reviewed row.")
    lines.append("")

    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Study bounded arena-to-conversion bridge rules.")
    ap.add_argument(
        "--front-rows-csv",
        default=str(RUNS_DIR / "2025-12-30_to_2026-01-04__AGGREGATED_ANALYSIS_ARENA__FRONT_BAND_ROWS.csv"),
    )
    ap.add_argument(
        "--sharepacks-root",
        default=str(REPO_ROOT / "sharepacks"),
    )
    ap.add_argument(
        "--cohort-mixes",
        nargs="*",
        default=list(DEFAULT_COHORTS),
    )
    ap.add_argument(
        "--rules",
        nargs="*",
        default=["top3_perm", "top4_perm"],
    )
    ap.add_argument("--gap-details", nargs="*", default=[])
    ap.add_argument("--max-vtrac-rank", type=int, default=0)
    ap.add_argument("--decay-days", type=int, default=3)
    ap.add_argument(
        "--out-rows-csv",
        default=str(RUNS_DIR / "2025-12-30_to_2026-01-04__AGGREGATED_ANALYSIS_ARENA__BRIDGE_STUDY_ROWS.csv"),
    )
    ap.add_argument(
        "--out-summary-csv",
        default=str(RUNS_DIR / "2025-12-30_to_2026-01-04__AGGREGATED_ANALYSIS_ARENA__BRIDGE_STUDY_SUMMARY.csv"),
    )
    ap.add_argument(
        "--out-md",
        default=str(RUNS_DIR / "2026-03-19__AGGREGATED_ARENA__BRIDGE_STUDY.md"),
    )
    return ap.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    max_vtrac_rank = int(args.max_vtrac_rank) if int(args.max_vtrac_rank) > 0 else None
    rows = build_bridge_rows(
        front_rows_csv=Path(args.front_rows_csv),
        sharepacks_root=Path(args.sharepacks_root),
        cohort_mixes=args.cohort_mixes,
        rules=args.rules,
        decay_days=int(args.decay_days),
        gap_details=args.gap_details,
        max_vtrac_rank=max_vtrac_rank,
    )
    write_bridge_outputs(
        rows=rows,
        out_rows_csv=Path(args.out_rows_csv),
        out_summary_csv=Path(args.out_summary_csv),
        out_md=Path(args.out_md),
        cohort_mixes=args.cohort_mixes,
        rules=args.rules,
        gap_details=args.gap_details,
        max_vtrac_rank=max_vtrac_rank,
    )
    print(f"bridge_rows={len(rows)}")
    print(f"summary_csv={args.out_summary_csv}")
    print(f"report_md={args.out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
