#!/usr/bin/env python3
"""Aggregate bridge-study rows across windows and split a focus cohort.

This stays in research mode. It combines one or more bridge-study row CSVs,
produces a corpus-level summary for a selected rule, and then drills into a
focus source mix (default: aux_overdue+aux_badge) to separate:

- immediate same-day bridge closures
- decay-only closures
- misses
"""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence

REPO_ROOT = Path(__file__).resolve().parents[2]
RUNS_DIR = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"

DEFAULT_ROWS = (
    RUNS_DIR / "2025-12-30_to_2026-01-04__AGGREGATED_ANALYSIS_ARENA__BRIDGE_STUDY_ROWS.csv",
    RUNS_DIR / "2026-01-05_to_2026-01-09__AGGREGATED_ANALYSIS_ARENA__BRIDGE_STUDY_ROWS.csv",
    RUNS_DIR / "2025-06-21_to_2025-06-24__AGGREGATED_ANALYSIS_ARENA__BRIDGE_STUDY_ROWS.csv",
)


def _read_csv(path: Path) -> List[Dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        return [dict(row) for row in csv.DictReader(fh)]


def _infer_window(path: Path) -> str:
    name = path.name
    marker = "__AGGREGATED_ANALYSIS_ARENA__BRIDGE_STUDY_ROWS.csv"
    return name.split(marker)[0] if marker in name else path.stem


def _to_int(value: object) -> Optional[int]:
    text = str(value or "").strip()
    if not text:
        return None
    try:
        return int(text)
    except ValueError:
        return None


def _to_bool_flag(value: object) -> bool:
    return str(value or "").strip() == "1"


def _outcome_class(row: Dict[str, str]) -> str:
    if _to_bool_flag(row.get("same_day_box_hit")) or _to_bool_flag(row.get("same_day_exact_hit")):
        return "same_day"
    if _to_bool_flag(row.get("within_3d_box_hit")) or _to_bool_flag(row.get("within_3d_exact_hit")):
        return "decay_only"
    return "miss"


def _rank_band(rank: Optional[int]) -> str:
    if rank is None:
        return "unknown"
    if rank <= 3:
        return "front3"
    if rank <= 5:
        return "front5"
    return "wider"


def _watchlist_band(count: Optional[int]) -> str:
    if count is None:
        return "unknown"
    if count <= 10:
        return "small"
    if count <= 13:
        return "medium"
    return "large"


def _matches_focus_gate(row: Dict[str, str], *, gap_details: Sequence[str], max_vtrac_rank: Optional[int]) -> bool:
    if gap_details and str(row.get("gap_detail") or "") not in set(gap_details):
        return False
    if max_vtrac_rank is not None:
        rank = _to_int(row.get("arena_vtrac_rank"))
        if rank is None or rank > max_vtrac_rank:
            return False
    return True


def _normalize_row(row: Dict[str, str], *, window: str) -> Dict[str, str]:
    rank = _to_int(row.get("arena_vtrac_rank"))
    watch_count = _to_int(row.get("watchlist_canonical_count"))
    out = dict(row)
    out["window"] = window
    out["outcome_class"] = _outcome_class(row)
    out["arena_vtrac_rank_band"] = _rank_band(rank)
    out["watchlist_band"] = _watchlist_band(watch_count)
    return out


def _group_counts(rows: Sequence[Dict[str, str]], *, key: str) -> List[Dict[str, str]]:
    grouped: Dict[str, List[Dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[str(row.get(key) or "")].append(row)

    out: List[Dict[str, str]] = []
    for group_key, picked in sorted(grouped.items(), key=lambda item: item[0]):
        total = len(picked)
        out.append(
            {
                key: group_key,
                "rows": str(total),
                "same_day": f"{sum(r['outcome_class'] == 'same_day' for r in picked)}/{total}",
                "decay_only": f"{sum(r['outcome_class'] == 'decay_only' for r in picked)}/{total}",
                "miss": f"{sum(r['outcome_class'] == 'miss' for r in picked)}/{total}",
            }
        )
    return out


def _write_csv(path: Path, rows: Sequence[Dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fieldnames: List[str] = []
    seen = set()
    for row in rows:
        for key in row.keys():
            if key not in seen:
                seen.add(key)
                fieldnames.append(key)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def _md_table(rows: Sequence[Dict[str, str]], columns: Sequence[str]) -> List[str]:
    if not rows:
        return ["_None._"]
    lines = [
        "| " + " | ".join(columns) + " |",
        "|---" * len(columns) + "|",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(row.get(col, "")) for col in columns) + " |")
    return lines


def _build_markdown(
    *,
    all_rows: Sequence[Dict[str, str]],
    selected_rows: Sequence[Dict[str, str]],
    focus_rows: Sequence[Dict[str, str]],
    gated_focus_rows: Sequence[Dict[str, str]],
    focus_source_mix: str,
    rule_name: str,
    summary_csv: Path,
    focus_csv: Path,
    gated_focus_csv: Path,
    focus_gap_details: Sequence[str],
    focus_max_vtrac_rank: Optional[int],
) -> str:
    lines: List[str] = [
        "# Aggregated Arena Bridge Corpus Readback",
        "",
        "- Purpose: combine bridge-study rows across measured windows, then split one repeated cohort into same-day, decay-only, and miss cases before any promotion decision.",
        f"- Rule analyzed: `{rule_name}`",
        f"- Focus source mix: `{focus_source_mix}`",
        f"- summary_csv: `{summary_csv}`",
        f"- focus_csv: `{focus_csv}`",
        f"- gated_focus_csv: `{gated_focus_csv}`",
        f"- total selected rows: `{len(selected_rows)}`",
        f"- focus rows: `{len(focus_rows)}`",
        f"- gated focus rows: `{len(gated_focus_rows)}`",
        "",
        "## Source Mix Summary",
        "",
    ]
    lines.extend(_md_table(_group_counts(selected_rows, key="source_mix"), ["source_mix", "rows", "same_day", "decay_only", "miss"]))
    lines.extend([
        "",
        "## Focus Cohort Split By Window",
        "",
    ])
    lines.extend(_md_table(_group_counts(focus_rows, key="window"), ["window", "rows", "same_day", "decay_only", "miss"]))
    lines.extend([
        "",
        "## Focus Cohort Split By Gap Detail",
        "",
    ])
    lines.extend(_md_table(_group_counts(focus_rows, key="gap_detail"), ["gap_detail", "rows", "same_day", "decay_only", "miss"]))
    lines.extend([
        "",
        "## Focus Cohort Split By VTRAC Rank Band",
        "",
    ])
    lines.extend(_md_table(_group_counts(focus_rows, key="arena_vtrac_rank_band"), ["arena_vtrac_rank_band", "rows", "same_day", "decay_only", "miss"]))
    lines.extend([
        "",
        "## Focus Cohort Split By Watchlist Band",
        "",
    ])
    lines.extend(_md_table(_group_counts(focus_rows, key="watchlist_band"), ["watchlist_band", "rows", "same_day", "decay_only", "miss"]))
    lines.extend([
        "",
        "## Focus Cohort Rows",
        "",
    ])
    focus_columns = [
        "window",
        "date",
        "state_key",
        "outcome",
        "winner",
        "gap_detail",
        "arena_vtrac_rank",
        "arena_vtrac_rank_band",
        "watchlist_canonical_count",
        "watchlist_band",
        "same_day_box_hit",
        "within_3d_box_hit",
        "first_box_event",
        "outcome_class",
    ]
    lines.extend(_md_table(focus_rows, focus_columns))
    lines.extend([
        "",
        "## Gated Focus Cohort",
        "",
        f"- gap_details: `{', '.join(focus_gap_details) if focus_gap_details else '-'} `",
        f"- max_vtrac_rank: `{focus_max_vtrac_rank if focus_max_vtrac_rank is not None else '-'}`",
        "",
    ])
    lines.extend(_md_table(_group_counts(gated_focus_rows, key="window"), ["window", "rows", "same_day", "decay_only", "miss"]))
    lines.extend([
        "",
        "## Gated Focus Rows",
        "",
    ])
    lines.extend(_md_table(gated_focus_rows, focus_columns))
    lines.extend([
        "",
        "## Notes",
        "",
        "- `same_day` means the bridge candidate set already boxed or hit the reviewed winner on the same outcome row.",
        "- `decay_only` means the same frozen bridge candidate set did not close same-day but did resolve within the next 3 days.",
        "- `miss` means no bridge closure within the measured horizon.",
    ])
    return "\n".join(lines).rstrip() + "\n"


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Aggregate bridge-study rows across windows and split a focus cohort.")
    ap.add_argument("--bridge-rows-csv", nargs="*", default=[str(p) for p in DEFAULT_ROWS])
    ap.add_argument("--rule-name", default="top4_perm")
    ap.add_argument("--focus-source-mix", default="aux_overdue+aux_badge")
    ap.add_argument("--focus-gap-details", nargs="*", default=[])
    ap.add_argument("--focus-max-vtrac-rank", type=int, default=0)
    ap.add_argument(
        "--out-summary-csv",
        default=str(RUNS_DIR / "2026-03-20__AGGREGATED_ARENA__BRIDGE_CORPUS_SUMMARY.csv"),
    )
    ap.add_argument(
        "--out-focus-csv",
        default=str(RUNS_DIR / "2026-03-20__AGGREGATED_ARENA__BRIDGE_CORPUS_FOCUS_ROWS.csv"),
    )
    ap.add_argument(
        "--out-gated-focus-csv",
        default=str(RUNS_DIR / "2026-03-20__AGGREGATED_ARENA__BRIDGE_CORPUS_GATED_FOCUS_ROWS.csv"),
    )
    ap.add_argument(
        "--out-md",
        default=str(RUNS_DIR / "2026-03-20__AGGREGATED_ARENA__BRIDGE_CORPUS_READBACK.md"),
    )
    return ap.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    all_rows: List[Dict[str, str]] = []
    for raw_path in args.bridge_rows_csv:
        path = Path(raw_path)
        window = _infer_window(path)
        for row in _read_csv(path):
            all_rows.append(_normalize_row(row, window=window))

    selected_rows = [row for row in all_rows if row.get("rule_name") == args.rule_name]
    focus_rows = [row for row in selected_rows if row.get("source_mix") == args.focus_source_mix]
    focus_rows.sort(key=lambda row: (row.get("window", ""), row.get("date", ""), row.get("state_key", ""), row.get("outcome", "")))
    focus_gap_details = [str(x).strip() for x in args.focus_gap_details if str(x).strip()]
    focus_max_rank = int(args.focus_max_vtrac_rank) if int(args.focus_max_vtrac_rank) > 0 else None
    gated_focus_rows = [
        row
        for row in focus_rows
        if _matches_focus_gate(row, gap_details=focus_gap_details, max_vtrac_rank=focus_max_rank)
    ]
    gated_focus_rows.sort(key=lambda row: (row.get("window", ""), row.get("date", ""), row.get("state_key", ""), row.get("outcome", "")))

    summary_rows = []
    for row in _group_counts(selected_rows, key="source_mix"):
        merged = dict(row)
        merged["group"] = "source_mix"
        summary_rows.append(merged)
    for row in _group_counts(focus_rows, key="window"):
        merged = dict(row)
        merged["group"] = "focus_window"
        summary_rows.append(merged)
    for row in _group_counts(focus_rows, key="gap_detail"):
        merged = dict(row)
        merged["group"] = "focus_gap_detail"
        summary_rows.append(merged)
    for row in _group_counts(focus_rows, key="arena_vtrac_rank_band"):
        merged = dict(row)
        merged["group"] = "focus_rank_band"
        summary_rows.append(merged)
    for row in _group_counts(focus_rows, key="watchlist_band"):
        merged = dict(row)
        merged["group"] = "focus_watchlist_band"
        summary_rows.append(merged)

    out_summary_csv = Path(args.out_summary_csv)
    out_focus_csv = Path(args.out_focus_csv)
    out_gated_focus_csv = Path(args.out_gated_focus_csv)
    out_md = Path(args.out_md)
    _write_csv(out_summary_csv, summary_rows)
    _write_csv(out_focus_csv, focus_rows)
    _write_csv(out_gated_focus_csv, gated_focus_rows)
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text(
        _build_markdown(
            all_rows=all_rows,
            selected_rows=selected_rows,
            focus_rows=focus_rows,
            gated_focus_rows=gated_focus_rows,
            focus_source_mix=str(args.focus_source_mix),
            rule_name=str(args.rule_name),
            summary_csv=out_summary_csv,
            focus_csv=out_focus_csv,
            gated_focus_csv=out_gated_focus_csv,
            focus_gap_details=focus_gap_details,
            focus_max_vtrac_rank=focus_max_rank,
        ),
        encoding="utf-8",
    )
    print(f"summary_csv={out_summary_csv}")
    print(f"focus_csv={out_focus_csv}")
    print(f"gated_focus_csv={out_gated_focus_csv}")
    print(f"report_md={out_md}")
    print(f"selected_rows={len(selected_rows)} focus_rows={len(focus_rows)} gated_focus_rows={len(gated_focus_rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
