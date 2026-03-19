#!/usr/bin/env python3
"""Roll up source-attributed front-band arena rows against decay outcomes.

This is a measurement-side helper. It joins the aggregated arena review
scoreboard to the frozen-snapshot decay scoreboard, filters to the strongest
front-band rows, and emits row-level and grouped summaries for bridge studies.
"""

from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


REPO_ROOT = Path(__file__).resolve().parents[2]
RUNS_DIR = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"

FRONT_GAP_DETAILS = (
    "lane_alive_literal_missing_front3",
    "lane_alive_literal_missing_front5",
    "family_alive_literal_missing_front5",
)

SOURCE_MAPPING: Tuple[Tuple[str, Tuple[str, ...]], ...] = (
    ("profit_alert", ("winner_canonical_profit_alert_present", "winner_vtrac_profit_alert_present")),
    ("blackapple", ("winner_canonical_blackapple_present", "winner_vtrac_blackapple_present")),
    ("due_doubles", ("winner_canonical_due_doubles_present", "winner_vtrac_due_doubles_present")),
    ("repeat_watch", ("winner_vtrac_repeat_watch_present",)),
    ("aux_overdue", ("winner_vtrac_aux_overdue_present",)),
    ("aux_badge", ("winner_canonical_aux_badge_present", "winner_vtrac_aux_badge_present")),
)


def _to_int(value: object, default: int = 0) -> int:
    try:
        text = str(value or "").strip()
        if not text:
            return int(default)
        return int(float(text))
    except Exception:
        return int(default)


def _to_rate(num: int, den: int) -> str:
    return f"{num}/{den}" if den else "0/0"


def _load_csv(path: Path) -> List[Dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        return [dict(row) for row in csv.DictReader(fh)]


def _join_decay(rows: Sequence[Dict[str, str]], decay_rows: Sequence[Dict[str, str]]) -> List[Dict[str, str]]:
    decay_map: Dict[Tuple[str, str], Dict[str, str]] = {}
    for row in decay_rows:
        key = (str(row.get("snapshot_date") or ""), str(row.get("state_key") or ""))
        if key[0] and key[1]:
            decay_map[key] = row

    out: List[Dict[str, str]] = []
    for row in rows:
        key = (str(row.get("date") or ""), str(row.get("state_key") or ""))
        merged = dict(row)
        decay = decay_map.get(key) or {}
        for k, v in decay.items():
            if k in {"snapshot_date", "state_key"}:
                continue
            merged[f"decay_{k}"] = v
        out.append(merged)
    return out


def _source_labels(row: Dict[str, str]) -> List[str]:
    labels: List[str] = []
    for label, keys in SOURCE_MAPPING:
        if any(str(row.get(key) or "").strip() == "1" for key in keys):
            labels.append(label)
    return labels


def _front_rows(rows: Sequence[Dict[str, str]]) -> List[Dict[str, str]]:
    picked: List[Dict[str, str]] = []
    for row in rows:
        if str(row.get("gap_detail") or "") not in FRONT_GAP_DETAILS:
            continue
        merged = dict(row)
        labels = _source_labels(row)
        merged["source_labels"] = ",".join(labels)
        merged["source_mix"] = "+".join(labels) if labels else "none"
        merged["source_count"] = str(len(labels))
        picked.append(merged)
    return picked


def _metric_hit(row: Dict[str, str], key: str) -> int:
    return 1 if str(row.get(key) or "").strip() == "1" else 0


def _summarize_sources(rows: Sequence[Dict[str, str]]) -> List[Dict[str, str]]:
    total = len(rows)
    out: List[Dict[str, str]] = []
    for label, _keys in SOURCE_MAPPING:
        matched = [row for row in rows if label in (row.get("source_labels") or "").split(",")]
        den = len(matched)
        out.append(
            {
                "source": label,
                "rows": str(den),
                "rows_share": f"{den}/{total}",
                "front3_rows": str(sum(1 for row in matched if row.get("gap_detail") == "lane_alive_literal_missing_front3")),
                "front5_rows": str(sum(1 for row in matched if row.get("gap_detail") == "lane_alive_literal_missing_front5")),
                "family_front5_rows": str(sum(1 for row in matched if row.get("gap_detail") == "family_alive_literal_missing_front5")),
                "dominant_vtrac_same_day": _to_rate(sum(_metric_hit(row, "decay_dominant_vtrac_same_day") for row in matched), den),
                "dominant_vtrac_within_3d": _to_rate(sum(_metric_hit(row, "decay_dominant_vtrac_within_3d") for row in matched), den),
                "watchlist_box_same_day": _to_rate(sum(_metric_hit(row, "decay_watchlist_box_same_day") for row in matched), den),
                "watchlist_box_within_3d": _to_rate(sum(_metric_hit(row, "decay_watchlist_box_within_3d") for row in matched), den),
            }
        )
    out.sort(key=lambda row: (-_to_int(row["rows"]), row["source"]))
    return out


def _summarize_source_mixes(rows: Sequence[Dict[str, str]], *, min_rows: int) -> List[Dict[str, str]]:
    grouped: Dict[str, List[Dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[str(row.get("source_mix") or "none")].append(row)

    out: List[Dict[str, str]] = []
    for mix, picked in grouped.items():
        den = len(picked)
        if den < min_rows:
            continue
        out.append(
            {
                "source_mix": mix,
                "rows": str(den),
                "front3_rows": str(sum(1 for row in picked if row.get("gap_detail") == "lane_alive_literal_missing_front3")),
                "front5_rows": str(sum(1 for row in picked if row.get("gap_detail") == "lane_alive_literal_missing_front5")),
                "family_front5_rows": str(sum(1 for row in picked if row.get("gap_detail") == "family_alive_literal_missing_front5")),
                "median_vtrac_rank_hint": str(sorted(_to_int(row.get("arena_vtrac_rank"), 999) for row in picked)[den // 2]),
                "dominant_vtrac_same_day": _to_rate(sum(_metric_hit(row, "decay_dominant_vtrac_same_day") for row in picked), den),
                "dominant_vtrac_within_3d": _to_rate(sum(_metric_hit(row, "decay_dominant_vtrac_within_3d") for row in picked), den),
                "watchlist_box_same_day": _to_rate(sum(_metric_hit(row, "decay_watchlist_box_same_day") for row in picked), den),
                "watchlist_box_within_3d": _to_rate(sum(_metric_hit(row, "decay_watchlist_box_within_3d") for row in picked), den),
                "downstream_literal_present": _to_rate(
                    sum(
                        1
                        for row in picked
                        if row.get("candidate_universe_box_present") == "1"
                        or row.get("candidate_universe_straight_present") == "1"
                        or row.get("play_card_box_present") == "1"
                        or row.get("play_card_straight_present") == "1"
                    ),
                    den,
                ),
            }
        )
    out.sort(
        key=lambda row: (
            -_to_int(row["rows"]),
            -(_to_int(row["watchlist_box_within_3d"].split("/")[0]) if "/" in row["watchlist_box_within_3d"] else 0),
            row["source_mix"],
        )
    )
    return out


def _build_bridge_candidates(mix_rows: Sequence[Dict[str, str]]) -> List[Dict[str, str]]:
    out: List[Dict[str, str]] = []
    for row in mix_rows:
        rows = _to_int(row.get("rows"), 0)
        dvt_num, dvt_den = (_to_int(x) for x in str(row.get("dominant_vtrac_within_3d") or "0/0").split("/", 1))
        wlb_num, wlb_den = (_to_int(x) for x in str(row.get("watchlist_box_within_3d") or "0/0").split("/", 1))
        if rows < 2:
            continue
        if dvt_den and dvt_num == 0:
            continue
        if wlb_den and wlb_num == 0:
            continue
        out.append(
            {
                "source_mix": str(row.get("source_mix") or ""),
                "rows": str(rows),
                "bridge_reason": "dominant_vtrac_alive_and_watchlist_resolves",
                "dominant_vtrac_within_3d": str(row.get("dominant_vtrac_within_3d") or ""),
                "watchlist_box_within_3d": str(row.get("watchlist_box_within_3d") or ""),
            }
        )
    return out


def build_front_band_rollup(
    *,
    review_csv: Path,
    decay_csv: Path,
    out_rows_csv: Path,
    out_source_csv: Path,
    out_mix_csv: Path,
    out_md: Path,
    min_mix_rows: int,
) -> Dict[str, object]:
    review_rows = _load_csv(review_csv)
    decay_rows = _load_csv(decay_csv)
    merged_rows = _join_decay(_front_rows(review_rows), decay_rows)
    source_rows = _summarize_sources(merged_rows)
    mix_rows = _summarize_source_mixes(merged_rows, min_rows=min_mix_rows)
    bridge_rows = _build_bridge_candidates(mix_rows)

    counters = Counter(str(row.get("gap_detail") or "") for row in merged_rows)
    total = len(merged_rows)

    for path, rows in (
        (out_rows_csv, merged_rows),
        (out_source_csv, source_rows),
        (out_mix_csv, mix_rows),
    ):
        path.parent.mkdir(parents=True, exist_ok=True)
        fieldnames = list(rows[0].keys()) if rows else []
        with path.open("w", encoding="utf-8", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=fieldnames)
            if fieldnames:
                writer.writeheader()
                for row in rows:
                    writer.writerow(row)

    lines: List[str] = []
    lines.append("# Aggregated Arena Front-Band Source Rollup")
    lines.append("")
    lines.append("- Purpose: summarize the strongest front-band rows by source mix and short-horizon decay before a bounded bridge study.")
    lines.append(f"- Review scoreboard: `{review_csv}`")
    lines.append(f"- Decay scoreboard: `{decay_csv}`")
    lines.append(f"- Front-band rows: `{total}`")
    lines.append("")
    lines.append("## Gap Split")
    lines.append("")
    for key in FRONT_GAP_DETAILS:
        lines.append(f"- `{key}`: `{counters.get(key, 0)}/{total}`")
    lines.append("")
    lines.append("## Source Presence")
    lines.append("")
    lines.append("| source | rows | front3 | front5 | family_front5 | dominant_vtrac_same_day | dominant_vtrac_<=3d | watchlist_box_same_day | watchlist_box_<=3d |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|")
    for row in source_rows:
        lines.append(
            f"| {row['source']} | {row['rows']} | {row['front3_rows']} | {row['front5_rows']} | {row['family_front5_rows']} | {row['dominant_vtrac_same_day']} | {row['dominant_vtrac_within_3d']} | {row['watchlist_box_same_day']} | {row['watchlist_box_within_3d']} |"
        )
    lines.append("")
    lines.append("## Source Mixes")
    lines.append("")
    if mix_rows:
        lines.append("| source_mix | rows | front3 | front5 | family_front5 | median_vtrac_rank_hint | dominant_vtrac_same_day | dominant_vtrac_<=3d | watchlist_box_same_day | watchlist_box_<=3d | downstream_literal_present |")
        lines.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
        for row in mix_rows:
            lines.append(
                f"| {row['source_mix']} | {row['rows']} | {row['front3_rows']} | {row['front5_rows']} | {row['family_front5_rows']} | {row['median_vtrac_rank_hint']} | {row['dominant_vtrac_same_day']} | {row['dominant_vtrac_within_3d']} | {row['watchlist_box_same_day']} | {row['watchlist_box_within_3d']} | {row['downstream_literal_present']} |"
            )
    else:
        lines.append("_No source mix met the row threshold._")
    lines.append("")
    lines.append("## Bridge Candidates")
    lines.append("")
    if bridge_rows:
        for row in bridge_rows:
            lines.append(
                f"- `{row['source_mix']}` rows `{row['rows']}` | dominant_vtrac `<=3d {row['dominant_vtrac_within_3d']}` | watchlist_box `<=3d {row['watchlist_box_within_3d']}`"
            )
    else:
        lines.append("_No repeated source mix cleared the bridge threshold yet._")
    lines.append("")

    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

    return {
        "total_rows": total,
        "gap_counts": dict(counters),
        "source_rows": source_rows,
        "mix_rows": mix_rows,
        "bridge_rows": bridge_rows,
    }


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Roll up source-attributed front-band arena rows against decay.")
    ap.add_argument(
        "--review-csv",
        default=str(RUNS_DIR / "2025-12-30_to_2026-01-04__AGGREGATED_ANALYSIS_ARENA__REVIEW.csv"),
    )
    ap.add_argument(
        "--decay-csv",
        default=str(RUNS_DIR / "2025-12-30_to_2026-01-04__AGGREGATED_ANALYSIS_ARENA__DECAY_D3.csv"),
    )
    ap.add_argument(
        "--out-rows-csv",
        default=str(RUNS_DIR / "2025-12-30_to_2026-01-04__AGGREGATED_ANALYSIS_ARENA__FRONT_BAND_ROWS.csv"),
    )
    ap.add_argument(
        "--out-source-csv",
        default=str(RUNS_DIR / "2025-12-30_to_2026-01-04__AGGREGATED_ANALYSIS_ARENA__FRONT_BAND_SOURCES.csv"),
    )
    ap.add_argument(
        "--out-mix-csv",
        default=str(RUNS_DIR / "2025-12-30_to_2026-01-04__AGGREGATED_ANALYSIS_ARENA__FRONT_BAND_SOURCE_MIXES.csv"),
    )
    ap.add_argument(
        "--out-md",
        default=str(RUNS_DIR / "2026-03-19__AGGREGATED_ARENA__FRONT_BAND_SOURCE_ROLLUP.md"),
    )
    ap.add_argument("--min-mix-rows", type=int, default=2)
    return ap.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    summary = build_front_band_rollup(
        review_csv=Path(args.review_csv),
        decay_csv=Path(args.decay_csv),
        out_rows_csv=Path(args.out_rows_csv),
        out_source_csv=Path(args.out_source_csv),
        out_mix_csv=Path(args.out_mix_csv),
        out_md=Path(args.out_md),
        min_mix_rows=int(args.min_mix_rows),
    )
    print(f"front_band_rows={summary['total_rows']}")
    print(f"source_csv={args.out_source_csv}")
    print(f"mix_csv={args.out_mix_csv}")
    print(f"report_md={args.out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
