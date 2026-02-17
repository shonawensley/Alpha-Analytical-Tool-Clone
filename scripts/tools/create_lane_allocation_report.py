#!/usr/bin/env python3
"""
Create a lane-allocation report from an existing conversion ladder CSV.

Why:
- After we improve lane retention (pack_any_correct / hit_any_inclusive),
  the next bottleneck is usually "within-lane depth/selection".
- This report answers, per outcome:
  - how many VTRAC indices ("lanes") the Play Card actually touched
  - how many lines were allocated to the winner's index (when defined)

This is reporting-only (selection layer):
- Reads: RUNS/*__CONVERSION_LADDER__*.csv (grade-output driven)
- Reads: Play Card JSONs referenced by ladder rows
- Writes: RUNS/*__LANE_ALLOCATION__*.{csv,md}

Safety note:
- The default output filename encodes `strategy` to prevent accidental overwrites when generating
  multiple lane-allocation reports in a sweep.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import re
import statistics
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple


REPO_ROOT = Path(__file__).resolve().parents[2]
RUNS_DIR = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"

if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import modules.vtrac_reference as vr  # noqa: E402


def _normalize_tag(value: str) -> str:
    raw = str(value or "").strip()
    if raw.lower() in {"", "-", "none", "null"}:
        return ""
    raw = raw.replace(" ", "_")
    cleaned = re.sub(r"[^A-Za-z0-9_-]+", "", raw).strip("_-")
    return cleaned[:60]


def _normalize_label(value: str) -> str:
    raw = str(value or "").strip()
    if not raw:
        return ""
    raw = raw.replace(" ", "_")
    cleaned = re.sub(r"[^A-Za-z0-9_-]+", "", raw).strip("_-")
    limit = 80
    if len(cleaned) <= limit:
        return cleaned
    digest = hashlib.sha1(cleaned.encode("utf-8")).hexdigest()[:8]
    head_len = max(0, limit - 2 - len(digest))
    return f"{cleaned[:head_len]}__{digest}"


def bool01(value: object) -> int:
    s = str(value or "").strip().lower()
    if s in {"1", "true", "yes", "y"}:
        return 1
    if s in {"0", "false", "no", "n", ""}:
        return 0
    try:
        return 1 if int(s) else 0
    except Exception:
        return 0


def safe_int(value: object) -> Optional[int]:
    try:
        s = str(value or "").strip()
        if not s:
            return None
        return int(s)
    except Exception:
        return None


def load_csv_rows(path: Path) -> List[Dict[str, str]]:
    with path.open("r", encoding="utf-8", errors="replace", newline="") as f:
        return [{k: (v or "") for k, v in row.items()} for row in csv.DictReader(f)]


def load_json(path: Path) -> Dict[str, object]:
    with path.open("r", encoding="utf-8", errors="replace") as f:
        raw = json.load(f)
    return raw if isinstance(raw, dict) else {}


def _ladder_csv_path(*, date_from: str, date_to: str, profile: str, strategy: str, experiment_tag: str) -> Path:
    tag = _normalize_tag(experiment_tag)
    suffix = f"__{tag}" if tag else ""
    return RUNS_DIR / f"{date_from}_to_{date_to}__CONVERSION_LADDER__{profile}__{strategy}{suffix}.csv"


def _out_base_path(
    *,
    date_from: str,
    date_to: str,
    profile: str,
    strategy: str,
    experiment_tag: str,
    budget_label: str,
    label: str,
) -> Path:
    tag = _normalize_tag(experiment_tag)
    suffix = f"__{tag}" if tag else ""
    strat = _normalize_label(strategy)
    lbl = _normalize_label(label)
    extra = f"__{budget_label}"
    if lbl:
        extra += f"__{lbl}"
    return RUNS_DIR / f"{date_from}_to_{date_to}__LANE_ALLOCATION__{profile}__{strat}{suffix}{extra}"


def pct(values: List[int], p: float) -> Optional[float]:
    if not values:
        return None
    xs = sorted(values)
    if len(xs) == 1:
        return float(xs[0])
    k = (len(xs) - 1) * p
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return float(xs[int(k)])
    return xs[f] * (c - k) + xs[c] * (k - f)


@dataclass(frozen=True)
class RowOut:
    results_date: str
    state_key: str
    winner_label: str
    winner: str
    winner_canonical: str
    winner_vtrac_index: str
    strategy: str
    budget_label: str
    play_card_path: str
    play_hit_any: str
    play_hit_any_inclusive: str
    play_straight_hit: str
    play_box_hit: str
    play_vtrac_index_hit: str
    cu_union_hit_any: str
    cu_union_vtrac_index_hit: str
    combos_count: int
    combos_without_index_count: int
    indices_touched_count: int
    winner_lane_present: str
    winner_lane_lines: str
    max_lines_single_index: int


def main() -> None:
    ap = argparse.ArgumentParser(description="Create a lane-allocation report from an existing conversion ladder CSV.")
    ap.add_argument("--date-from", required=True, help="Start date (YYYY-MM-DD)")
    ap.add_argument("--date-to", required=True, help="End date (YYYY-MM-DD)")
    ap.add_argument("--profile", default="tool_only", help="Profile in ladder filenames (default: tool_only).")
    ap.add_argument("--experiment-tag", default="", help="Optional experiment tag suffix (e.g., stable10).")
    ap.add_argument("--strategy", required=True, help="Play Card strategy (must already have ladder CSV).")
    ap.add_argument("--budget", default="B36", help="Budget label to analyze (default: B36).")
    ap.add_argument("--label", default="", help="Optional short label added to output filenames.")
    ap.add_argument("--out", default=None, help="Override output path base (without extension).")
    args = ap.parse_args()

    date_from = str(args.date_from).strip()
    date_to = str(args.date_to).strip()
    profile = str(args.profile or "tool_only").strip()
    exp_tag = _normalize_tag(args.experiment_tag)
    strategy = str(args.strategy).strip()
    budget_label = str(args.budget or "B36").strip()
    label = str(args.label or "").strip()

    ladder_csv = _ladder_csv_path(
        date_from=date_from,
        date_to=date_to,
        profile=profile,
        strategy=strategy,
        experiment_tag=exp_tag,
    )
    if not ladder_csv.exists():
        raise SystemExit(f"Missing ladder CSV: {ladder_csv}")

    out_base = (
        Path(args.out)
        if args.out
        else _out_base_path(
            date_from=date_from,
            date_to=date_to,
            profile=profile,
            strategy=strategy,
            experiment_tag=exp_tag,
            budget_label=budget_label,
            label=label,
        )
    )
    if not out_base.is_absolute():
        out_base = (REPO_ROOT / out_base).resolve()
    out_base.parent.mkdir(parents=True, exist_ok=True)
    out_csv = out_base.with_suffix(".csv")
    out_md = out_base.with_suffix(".md")

    rows = load_csv_rows(ladder_csv)
    focus = [r for r in rows if (r.get("budget_label") or "") == budget_label and bool01(r.get("winner_missing")) == 0]

    out_rows: List[Dict[str, str]] = []
    derived: List[RowOut] = []
    missing_play_cards = 0

    for r in focus:
        pc_rel = (r.get("play_card_path") or "").strip()
        if not pc_rel:
            missing_play_cards += 1
            continue
        pc_path = (REPO_ROOT / pc_rel).resolve()
        if not pc_path.exists():
            missing_play_cards += 1
            continue

        payload = load_json(pc_path)
        strategies = payload.get("strategies")
        if not isinstance(strategies, dict):
            missing_play_cards += 1
            continue
        strat = strategies.get(strategy)
        if not isinstance(strat, dict):
            missing_play_cards += 1
            continue
        budget_obj = strat.get(budget_label)
        if not isinstance(budget_obj, dict):
            missing_play_cards += 1
            continue
        combos_raw = budget_obj.get("combos")
        combos = [str(x) for x in combos_raw] if isinstance(combos_raw, list) else []

        counts_by_idx: Dict[int, int] = {}
        no_idx = 0
        for c in combos:
            idx = vr.get_vtrac_index(str(c))
            if isinstance(idx, int):
                counts_by_idx[int(idx)] = counts_by_idx.get(int(idx), 0) + 1
            else:
                no_idx += 1

        winner_idx = safe_int(r.get("winner_vtrac_index", ""))
        winner_lines = counts_by_idx.get(int(winner_idx), 0) if isinstance(winner_idx, int) else None
        winner_present = (winner_lines is not None and winner_lines > 0)

        max_lines = max(counts_by_idx.values()) if counts_by_idx else 0
        indices_touched = len(counts_by_idx)

        ro = RowOut(
            results_date=r.get("results_date", ""),
            state_key=r.get("state_key", ""),
            winner_label=r.get("winner_label", ""),
            winner=r.get("winner", ""),
            winner_canonical=r.get("winner_canonical", ""),
            winner_vtrac_index=r.get("winner_vtrac_index", ""),
            strategy=r.get("strategy", ""),
            budget_label=r.get("budget_label", ""),
            play_card_path=pc_rel,
            play_hit_any=r.get("play_hit_any", ""),
            play_hit_any_inclusive=r.get("play_hit_any_inclusive", ""),
            play_straight_hit=r.get("play_straight_hit", ""),
            play_box_hit=r.get("play_box_hit", ""),
            play_vtrac_index_hit=r.get("play_vtrac_index_hit", ""),
            cu_union_hit_any=r.get("cu_union_hit_any", ""),
            cu_union_vtrac_index_hit=r.get("cu_union_vtrac_index_hit", ""),
            combos_count=len(combos),
            combos_without_index_count=int(no_idx),
            indices_touched_count=int(indices_touched),
            winner_lane_present="1" if winner_present else "0" if winner_lines is not None else "",
            winner_lane_lines=str(winner_lines) if winner_lines is not None else "",
            max_lines_single_index=int(max_lines),
        )
        derived.append(ro)

    derived.sort(key=lambda x: (x.results_date, x.state_key, x.winner_label))

    # CSV
    fieldnames = [
        "results_date",
        "state_key",
        "winner_label",
        "winner",
        "winner_canonical",
        "winner_vtrac_index",
        "strategy",
        "budget_label",
        "play_hit_any",
        "play_hit_any_inclusive",
        "play_straight_hit",
        "play_box_hit",
        "play_vtrac_index_hit",
        "cu_union_hit_any",
        "cu_union_vtrac_index_hit",
        "play_card_path",
        "combos_count",
        "combos_without_index_count",
        "indices_touched_count",
        "winner_lane_present",
        "winner_lane_lines",
        "max_lines_single_index",
    ]
    with out_csv.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for ro in derived:
            w.writerow({k: str(getattr(ro, k)) for k in fieldnames})

    # Markdown summary
    indices_touched = [ro.indices_touched_count for ro in derived]
    max_lines = [ro.max_lines_single_index for ro in derived]
    winner_lines_all: List[int] = []
    winner_lines_defined: List[int] = []
    for ro in derived:
        if ro.winner_lane_lines.strip() != "":
            winner_lines_defined.append(int(ro.winner_lane_lines))
            if ro.winner_lane_present == "1":
                winner_lines_all.append(int(ro.winner_lane_lines))

    def _fmt(v: Optional[float]) -> str:
        return "NA" if v is None else f"{v:.1f}"

    lines: List[str] = []
    lines.append(f"# Lane Allocation — {date_from}..{date_to}")
    lines.append("")
    lines.append("Source:")
    lines.append(f"- Ladder CSV: `{ladder_csv.relative_to(REPO_ROOT)}`")
    lines.append(f"- Strategy: `{strategy}`")
    lines.append(f"- Budget: `{budget_label}`")
    if exp_tag:
        lines.append(f"- Experiment tag: `{exp_tag}`")
    lines.append("")
    lines.append("Notes:")
    lines.append("- This is selection-layer instrumentation; no analyzers are executed.")
    lines.append("- Rows with `winner_missing=1` are excluded (censored outcomes).")
    lines.append("")
    lines.append("## Coverage")
    lines.append(f"- Rows (winner present): `{len(focus)}`")
    lines.append(f"- Rows measured (play card loaded): `{len(derived)}`")
    lines.append(f"- Rows missing play cards: `{missing_play_cards}`")
    lines.append("")
    lines.append("## Indices touched per Play Card")
    lines.append(f"- mean: `{_fmt(statistics.mean(indices_touched) if indices_touched else None)}`")
    lines.append(f"- min/p50/p75/p90/max: `{_fmt(min(indices_touched) if indices_touched else None)}` / `{_fmt(pct(indices_touched,0.50))}` / `{_fmt(pct(indices_touched,0.75))}` / `{_fmt(pct(indices_touched,0.90))}` / `{_fmt(max(indices_touched) if indices_touched else None)}`")
    lines.append("")
    lines.append("## Winner index depth (lines allocated to winner lane)")
    lines.append(f"- outcomes where winner index is defined: `{len(winner_lines_defined)}`")
    if winner_lines_defined:
        present = sum(1 for x in winner_lines_defined if x > 0)
        lines.append(f"- winner lane present rate (among defined): `{(present/len(winner_lines_defined))*100:.1f}%`")
        lines.append(f"- lines on winner lane (including 0): mean `{_fmt(statistics.mean(winner_lines_defined))}`; p50 `{_fmt(pct(winner_lines_defined,0.50))}`; p90 `{_fmt(pct(winner_lines_defined,0.90))}`; max `{_fmt(max(winner_lines_defined))}`")
    lines.append("")
    lines.append("## Max lines on any single index (how “spiky” the card is)")
    lines.append(f"- mean: `{_fmt(statistics.mean(max_lines) if max_lines else None)}`")
    lines.append(f"- min/p50/p90/max: `{_fmt(min(max_lines) if max_lines else None)}` / `{_fmt(pct(max_lines,0.50))}` / `{_fmt(pct(max_lines,0.90))}` / `{_fmt(max(max_lines) if max_lines else None)}`")
    lines.append("")
    lines.append("## Output CSV")
    lines.append(f"- `{out_csv.relative_to(REPO_ROOT)}`")
    out_md.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", errors="replace")


if __name__ == "__main__":
    main()
