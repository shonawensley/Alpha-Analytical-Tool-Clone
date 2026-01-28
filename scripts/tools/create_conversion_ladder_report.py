"""
Create a conversion-ladder report that makes the pipeline break explicit:

Evidence -> Candidate Universe (CU union) -> Play Card (budgeted selection)

This is intentionally *predictive-safe* and uses only grade outputs under
docs/AAT9_KIT/FINAL VALIDATION/RUNS/.

Outputs:
- docs/AAT9_KIT/FINAL VALIDATION/RUNS/<RANGE>__CONVERSION_LADDER__<PROFILE>__<STRATEGY>.csv
- docs/AAT9_KIT/FINAL VALIDATION/RUNS/<RANGE>__CONVERSION_LADDER__<PROFILE>__<STRATEGY>.md
"""

from __future__ import annotations

import argparse
import csv
import re
import statistics
from dataclasses import dataclass
from datetime import date as _date
from datetime import timedelta
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple


REPO_ROOT = Path(__file__).resolve().parents[2]
RUNS_DIR = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"


def parse_iso_date(value: str) -> _date:
    try:
        return _date.fromisoformat(value)
    except ValueError as exc:
        raise SystemExit(f"Invalid ISO date (expected YYYY-MM-DD): {value}") from exc


def daterange(date_from: _date, date_to: _date) -> Iterable[_date]:
    if date_to < date_from:
        raise SystemExit("--date-to must be >= --date-from")
    cur = date_from
    while cur <= date_to:
        yield cur
        cur += timedelta(days=1)


def safe_float(value: str) -> Optional[float]:
    try:
        return float(value)
    except Exception:
        return None


def safe_int(value: str) -> Optional[int]:
    try:
        return int(str(value).strip())
    except Exception:
        return None


def bool01(value: object) -> int:
    s = str(value or "").strip().lower()
    if s in {"1", "true", "yes", "y"}:
        return 1
    if s in {"0", "false", "no", "n", ""}:
        return 0
    i = safe_int(s)
    return 1 if i else 0


def load_csv_rows(path: Path) -> List[Dict[str, str]]:
    with path.open("r", encoding="utf-8", errors="replace", newline="") as f:
        return [{k: (v or "") for k, v in row.items()} for row in csv.DictReader(f)]


@dataclass(frozen=True)
class UnionKey:
    state_key: str
    winner_label: str  # Midday / Evening


@dataclass(frozen=True)
class CuUnion:
    results_date: str
    history_date: str
    state_key: str
    winner_label: str
    candidate_universe_path: str
    winner: str
    winner_canonical: str
    winner_vtrac_index: str
    winner_missing: int
    hit_any: int
    straight_hit: int
    box_hit: int
    vtrac_index_hit: int
    vtrac_index_hit_only: int


def _normalize_tag(value: str) -> str:
    raw = str(value or "").strip()
    if raw.lower() in {"", "-", "none", "null"}:
        return ""
    raw = raw.replace(" ", "_")
    cleaned = re.sub(r"[^A-Za-z0-9_-]+", "", raw).strip("_-")
    return cleaned[:60]


def load_cu_union(*, date_str: str, profile: str, experiment_tag: str) -> Dict[UnionKey, CuUnion]:
    tag = _normalize_tag(experiment_tag)
    suffix = f"__{tag}" if tag else ""
    path = RUNS_DIR / f"{date_str}__CANDIDATE_UNIVERSE_GRADE__{profile}{suffix}.csv"
    if not path.exists():
        return {}
    rows = load_csv_rows(path)
    out: Dict[UnionKey, CuUnion] = {}
    for r in rows:
        if (r.get("pack_id") or "") != "__UNION__":
            continue
        k = UnionKey(state_key=r.get("state_key", ""), winner_label=r.get("winner_label", ""))
        out[k] = CuUnion(
            results_date=r.get("results_date", date_str),
            history_date=r.get("history_date", ""),
            state_key=r.get("state_key", ""),
            winner_label=r.get("winner_label", ""),
            candidate_universe_path=r.get("candidate_universe_path", ""),
            winner=r.get("winner", ""),
            winner_canonical=r.get("winner_canonical", ""),
            winner_vtrac_index=r.get("winner_vtrac_index", ""),
            winner_missing=bool01(r.get("winner_missing")),
            hit_any=bool01(r.get("hit_any")),
            straight_hit=bool01(r.get("straight_hit")),
            box_hit=bool01(r.get("box_hit")),
            vtrac_index_hit=bool01(r.get("vtrac_index_hit")),
            vtrac_index_hit_only=bool01(r.get("vtrac_index_hit_only")),
        )
    return out


def fmt_pct(x: Optional[float]) -> str:
    if x is None:
        return "NA"
    return f"{x * 100:.1f}%"


def rate(*, rows: List[Dict[str, str]], key: str) -> Optional[float]:
    if not rows:
        return None
    return sum(bool01(r.get(key)) for r in rows) / float(len(rows))


def rate_ints(values: List[int]) -> Optional[float]:
    if not values:
        return None
    return sum(values) / float(len(values))


def write_csv(path: Path, rows: List[Dict[str, str]], fieldnames: List[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow({k: (r.get(k, "") or "") for k in fieldnames})


def write_md(
    *,
    out_path: Path,
    csv_path: Path,
    date_from: str,
    date_to: str,
    included_dates: List[str],
    excluded_dates: List[str],
    strategy: str,
    summary_lines: List[str],
) -> None:
    lines: List[str] = []
    lines.append(f"# Conversion Ladder — {date_from}..{date_to}")
    lines.append("")
    lines.append("Purpose: make the break explicit across the predictive substrate:")
    lines.append("- Candidate Universe (`__UNION__` row) = what the system *could* play (unbounded).")
    lines.append("- Play Card = what we *would* play under a fixed budget (B12/B24/B36).")
    lines.append("")
    lines.append("Notes (critical):")
    lines.append("- Always filter out `winner_missing=1` rows when interpreting hit rates.")
    lines.append("- This report is grade-output driven; it does not read sharepacks directly.")
    lines.append("")
    lines.append("## Coverage")
    lines.append(f"- Requested range: `{date_from}..{date_to}`")
    lines.append(f"- Included dates (grade files present): `{', '.join(included_dates) if included_dates else 'NONE'}`")
    if excluded_dates:
        lines.append(f"- Excluded dates (missing grades): `{', '.join(excluded_dates)}`")
    lines.append("")
    lines.append(f"## Summary (`{strategy}`)")
    lines.extend(summary_lines)
    lines.append("")
    lines.append("## Output CSV")
    lines.append(f"- `{csv_path.relative_to(REPO_ROOT)}`")
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8", errors="replace")


def _bucket(row: Dict[str, str]) -> str:
    if bool01(row.get("winner_missing")) == 1:
        return "CENSORED"
    cu_hit_any_raw = (row.get("cu_union_hit_any") or "").strip()
    cu_lane_raw = (row.get("cu_union_vtrac_index_hit") or "").strip()
    if not cu_hit_any_raw and not cu_lane_raw:
        return "NO_CU_JOIN"
    if bool01(row.get("play_hit_any_inclusive")) == 1:
        return "HIT_INCLUSIVE"
    if bool01(cu_hit_any_raw) == 1:
        return "CU_EXACT_BUT_PLAY_MISS"
    if bool01(cu_lane_raw) == 1:
        return "CU_LANE_BUT_PLAY_MISS"
    return "CU_MISS"


def _derived_artifact_paths(*, candidate_universe_path: str, play_card_path: str) -> List[str]:
    """
    Best-effort helpers for opening adjacent artifacts without assuming they exist.
    """
    out: List[str] = []
    if candidate_universe_path:
        out.append(candidate_universe_path)
        base = str(candidate_universe_path)
        out.append(base.replace("candidate_universe", "candidate_universe_evidence").replace(".json", ".csv"))
        out.append(base.replace("candidate_universe", "signals_bundle"))
    if play_card_path:
        out.append(play_card_path)
    seen = set()
    uniq: List[str] = []
    for p in out:
        if not p or p in seen:
            continue
        seen.add(p)
        uniq.append(p)
    return uniq


def write_casebook(*, out_path: Path, rows: List[Dict[str, str]], budget_label: str, max_cases: int) -> None:
    b = str(budget_label).strip()
    max_n = max(1, int(max_cases))
    focus = [r for r in rows if (r.get("budget_label") or "") == b and bool01(r.get("winner_missing")) == 0]
    focus.sort(key=lambda r: (r.get("results_date", ""), r.get("state_key", ""), r.get("winner_label", "")))

    groups: Dict[str, List[Dict[str, str]]] = {}
    for r in focus:
        groups.setdefault(_bucket(r), []).append(r)

    lines: List[str] = []
    lines.append(f"# Conversion Casebook — {b}")
    lines.append("")
    lines.append("Purpose: a small set of concrete cases per bucket so we can debug conversion without re-reading everything.")
    lines.append("")
    lines.append("Buckets:")
    lines.append("- `HIT_INCLUSIVE`: Play Card retained the winner lane (or better).")
    lines.append("- `CU_EXACT_BUT_PLAY_MISS`: CU contains winner (box/straight) but Play Card lost it.")
    lines.append("- `CU_LANE_BUT_PLAY_MISS`: CU touches winner VTRAC index but Play Card lost it.")
    lines.append("- `CU_MISS`: CU does not contain winner (exact or lane).")
    lines.append("")

    order = ["CU_MISS", "CU_LANE_BUT_PLAY_MISS", "CU_EXACT_BUT_PLAY_MISS", "HIT_INCLUSIVE"]
    for bucket in order:
        cases = groups.get(bucket, [])[:max_n]
        if not cases:
            continue
        lines.append(f"## {bucket} ({len(cases)})")
        for r in cases:
            date = r.get("results_date", "")
            state = r.get("state_key", "")
            label = r.get("winner_label", "")
            winner = r.get("winner", "")
            widx = r.get("winner_vtrac_index", "")
            pack_idx = r.get("vtrac_pack_index", "")
            pack_indices = r.get("vtrac_pack_indices", "")
            pack_correct = r.get("pack_correct", "")
            pack_any_correct = r.get("pack_any_correct", "")
            cu_any = r.get("cu_union_hit_any", "")
            cu_lane = r.get("cu_union_vtrac_index_hit", "")
            play_inc = r.get("play_hit_any_inclusive", "")
            play_any = r.get("play_hit_any", "")
            cu_path = r.get("candidate_universe_path", "")
            pc_path = r.get("play_card_path", "")
            lines.append(
                f"- `{date} {state} {label}` winner=`{winner}` idx=`{widx}` "
                f"CU(hit_any={cu_any}, lane={cu_lane}) "
                f"Play(inclusive={play_inc}, hit_any={play_any}) "
                f"pack_idx=`{pack_idx}` pack_indices=`{pack_indices}` "
                f"pack_correct=`{pack_correct}` pack_any_correct=`{pack_any_correct}`"
            )
            lines.append(f"  - Results: `data/results/{date}.txt`")
            for p in _derived_artifact_paths(candidate_universe_path=cu_path, play_card_path=pc_path):
                lines.append(f"  - Artifact: `{p}`")
        lines.append("")

    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8", errors="replace")


def main() -> None:
    ap = argparse.ArgumentParser(description="Create a predictive conversion-ladder report from grade outputs.")
    ap.add_argument("--date-from", required=True, help="Inclusive start date (YYYY-MM-DD).")
    ap.add_argument("--date-to", required=True, help="Inclusive end date (YYYY-MM-DD).")
    ap.add_argument("--profile", default="tool_only", help="Ablation profile (default: tool_only).")
    ap.add_argument("--strategy", default="v0_2_default", help="Play card strategy to summarize (default: v0_2_default).")
    ap.add_argument(
        "--experiment-tag",
        default="",
        help="Optional experiment tag suffix on grade filenames (e.g., stable10 reads ...__PLAY_CARD_GRADE__tool_only__stable10.csv).",
    )
    ap.add_argument(
        "--budgets",
        default="B12,B24,B36",
        help="Comma-separated budget labels to include (default: B12,B24,B36).",
    )
    ap.add_argument("--write-casebook", action="store_true", help="Also write a small per-bucket casebook (default: off).")
    ap.add_argument("--casebook-budget", default="B24", help="Budget to build casebook for (default: B24).")
    ap.add_argument("--casebook-n", type=int, default=5, help="Cases per bucket (default: 5).")
    args = ap.parse_args()

    date_from = parse_iso_date(args.date_from)
    date_to = parse_iso_date(args.date_to)
    profile = str(args.profile)
    strategy = str(args.strategy)
    exp_tag = _normalize_tag(str(args.experiment_tag))
    budgets = [b.strip() for b in str(args.budgets).split(",") if b.strip()]
    if not budgets:
        raise SystemExit("--budgets must be non-empty")

    included_dates: List[str] = []
    excluded_dates: List[str] = []

    out_rows: List[Dict[str, str]] = []
    for d in daterange(date_from, date_to):
        ds = d.isoformat()
        cu_union = load_cu_union(date_str=ds, profile=profile, experiment_tag=exp_tag)

        suffix = f"__{exp_tag}" if exp_tag else ""
        play_path = RUNS_DIR / f"{ds}__PLAY_CARD_GRADE__{profile}{suffix}.csv"
        if not play_path.exists():
            excluded_dates.append(ds)
            continue
        included_dates.append(ds)

        play_rows = load_csv_rows(play_path)
        for r in play_rows:
            if (r.get("strategy") or "") != strategy:
                continue
            budget = (r.get("budget_label") or "").strip()
            if budget not in budgets:
                continue
            k = UnionKey(state_key=r.get("state_key", ""), winner_label=r.get("winner_label", ""))
            cu = cu_union.get(k)

            winner_missing = bool01(r.get("winner_missing"))
            pack_idx_raw = (r.get("vtrac_pack_index") or "").strip()
            pack_indices_raw = (r.get("vtrac_pack_indices") or "").strip()
            pack_correct: str = ""
            if not winner_missing and pack_idx_raw:
                pack_idx = safe_int(pack_idx_raw)
                win_idx = safe_int(r.get("winner_vtrac_index") or "")
                if pack_idx is not None and win_idx is not None:
                    pack_correct = "1" if pack_idx == win_idx else "0"

            pack_any_correct: str = (r.get("pack_any_correct") or "").strip()
            if not winner_missing and not pack_any_correct and pack_indices_raw:
                win_idx = safe_int(r.get("winner_vtrac_index") or "")
                indices: List[int] = []
                for tok in re.split(r"[\\s,]+", pack_indices_raw):
                    tok = tok.strip()
                    if not tok:
                        continue
                    val = safe_int(tok)
                    if val is not None:
                        indices.append(int(val))
                if win_idx is not None and indices:
                    pack_any_correct = "1" if int(win_idx) in set(indices) else "0"

            out_rows.append(
                {
                    "results_date": r.get("results_date", ds),
                    "history_date": (cu.history_date if cu else ""),
                    "state_key": r.get("state_key", ""),
                    "winner_label": r.get("winner_label", ""),
                    "candidate_universe_path": (cu.candidate_universe_path if cu else ""),
                    "play_card_path": r.get("play_card_path", ""),
                    "winner": r.get("winner", ""),
                    "winner_canonical": r.get("winner_canonical", ""),
                    "winner_vtrac_index": r.get("winner_vtrac_index", ""),
                    "winner_missing": str(winner_missing),
                    # CU union (best-effort join)
                    "cu_union_hit_any": str(cu.hit_any if cu else ""),
                    "cu_union_straight_hit": str(cu.straight_hit if cu else ""),
                    "cu_union_box_hit": str(cu.box_hit if cu else ""),
                    "cu_union_vtrac_index_hit": str(cu.vtrac_index_hit if cu else ""),
                    "cu_union_vtrac_index_hit_only": str(cu.vtrac_index_hit_only if cu else ""),
                    # Play card row (budgeted conversion)
                    "strategy": strategy,
                    "budget_label": budget,
                    "combos_count": r.get("combos_count", ""),
                    "boxed_canonicals_count": r.get("boxed_canonicals_count", ""),
                    "play_hit_any": r.get("hit_any", ""),
                    "play_straight_hit": r.get("straight_hit", ""),
                    "play_box_hit": r.get("box_hit", ""),
                    "play_vtrac_index_hit": r.get("vtrac_index_hit", ""),
                    "play_vtrac_index_hit_only": r.get("vtrac_index_hit_only", ""),
                    "play_hit_any_inclusive": r.get("hit_any_inclusive", ""),
                    # Pack vs filler attribution (where did the hit come from?)
                    "vtrac_pack_index": pack_idx_raw,
                    "vtrac_pack_indices": pack_indices_raw,
                    "vtrac_pack_size": r.get("vtrac_pack_size", ""),
                    "filler_size": r.get("filler_size", ""),
                    "pack_vtrac_index_hit": r.get("pack_vtrac_index_hit", ""),
                    # Pack-only strict hits (VTRAC semantics; helps align to the 4-criteria mental model).
                    # Note: play-card grade exports `pack_canon_hit_any_perm` (boxed membership by canonical perm).
                    "pack_box_hit": r.get("pack_canon_hit_any_perm", ""),
                    "pack_straight_hit": r.get("pack_straight_hit", ""),
                    "pack_hit_any_inclusive": r.get("pack_hit_any_inclusive", ""),
                    "filler_hit_any_inclusive": r.get("filler_hit_any_inclusive", ""),
                    "pack_correct": pack_correct,
                    "pack_any_correct": pack_any_correct,
                }
            )

    out_rows.sort(key=lambda r: (r.get("results_date", ""), r.get("state_key", ""), r.get("winner_label", ""), r.get("budget_label", "")))

    range_tag = f"{date_from.isoformat()}_to_{date_to.isoformat()}"
    tag_suffix = f"__{exp_tag}" if exp_tag else ""
    out_csv = RUNS_DIR / f"{range_tag}__CONVERSION_LADDER__{profile}__{strategy}{tag_suffix}.csv"
    out_md = RUNS_DIR / f"{range_tag}__CONVERSION_LADDER__{profile}__{strategy}{tag_suffix}.md"

    fieldnames = [
        "results_date",
        "history_date",
        "state_key",
        "winner_label",
        "candidate_universe_path",
        "play_card_path",
        "winner",
        "winner_canonical",
        "winner_vtrac_index",
        "winner_missing",
        "cu_union_hit_any",
        "cu_union_straight_hit",
        "cu_union_box_hit",
        "cu_union_vtrac_index_hit",
        "cu_union_vtrac_index_hit_only",
        "strategy",
        "budget_label",
        "combos_count",
        "boxed_canonicals_count",
        "play_hit_any",
        "play_straight_hit",
        "play_box_hit",
        "play_vtrac_index_hit",
        "play_vtrac_index_hit_only",
        "play_hit_any_inclusive",
        "vtrac_pack_index",
        "vtrac_pack_indices",
        "vtrac_pack_size",
        "filler_size",
        "pack_vtrac_index_hit",
        "pack_box_hit",
        "pack_straight_hit",
        "pack_hit_any_inclusive",
        "filler_hit_any_inclusive",
        "pack_correct",
        "pack_any_correct",
    ]
    write_csv(out_csv, out_rows, fieldnames)

    # Summaries (exclude censored rows).
    known = [r for r in out_rows if bool01(r.get("winner_missing")) == 0]

    # CU union recall (take one budget per outcome to avoid triple-counting).
    # We'll use B24 rows when present, otherwise any budget row.
    seen_outcomes = set()
    cu_rows: List[Dict[str, str]] = []
    for r in known:
        key = (r.get("results_date", ""), r.get("state_key", ""), r.get("winner_label", ""))
        if key in seen_outcomes:
            continue
        seen_outcomes.add(key)
        cu_rows.append(r)

    # Budgeted conversion summaries.
    by_budget: Dict[str, List[Dict[str, str]]] = {b: [] for b in budgets}
    for r in known:
        b = r.get("budget_label", "")
        if b in by_budget:
            by_budget[b].append(r)

    summary_lines: List[str] = []
    summary_lines.append(f"- Rows in CSV: `{len(out_rows)}` (known winners: `{len(known)}`; censored: `{len(out_rows) - len(known)}`)")
    summary_lines.append("")
    summary_lines.append("### Candidate Universe (`__UNION__`) recall (per outcome)")
    summary_lines.append(f"- outcomes: `{len(cu_rows)}`")
    summary_lines.append(f"- CU union hit_any: `{fmt_pct(rate(rows=cu_rows, key='cu_union_hit_any'))}`")
    summary_lines.append(f"- CU union box_hit: `{fmt_pct(rate(rows=cu_rows, key='cu_union_box_hit'))}`")
    summary_lines.append(f"- CU union straight_hit: `{fmt_pct(rate(rows=cu_rows, key='cu_union_straight_hit'))}`")
    summary_lines.append(f"- CU union vtrac_index_hit: `{fmt_pct(rate(rows=cu_rows, key='cu_union_vtrac_index_hit'))}`")
    summary_lines.append("")
    summary_lines.append(f"### Play Card conversion (per budget; `{strategy}`)")
    summary_lines.append(
        "| Budget | rows | hit_any | hit_any_inclusive | box_hit | straight_hit | vtrac_index_hit | pack_box_hit | pack_straight_hit | pack_correct | pack_any_correct |"
    )
    summary_lines.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
    for b in budgets:
        rows_b = by_budget.get(b, [])
        pack_correct_vals = [bool01(r.get("pack_correct")) for r in rows_b if (r.get("pack_correct") or "").strip() != ""]
        pack_correct_rate = rate_ints(pack_correct_vals)
        pack_any_correct_vals = [
            bool01(r.get("pack_any_correct")) for r in rows_b if (r.get("pack_any_correct") or "").strip() != ""
        ]
        pack_any_correct_rate = rate_ints(pack_any_correct_vals)
        summary_lines.append(
            "| "
            + " | ".join(
                [
                    b,
                    str(len(rows_b)),
                    fmt_pct(rate(rows=rows_b, key="play_hit_any")),
                    fmt_pct(rate(rows=rows_b, key="play_hit_any_inclusive")),
                    fmt_pct(rate(rows=rows_b, key="play_box_hit")),
                    fmt_pct(rate(rows=rows_b, key="play_straight_hit")),
                    fmt_pct(rate(rows=rows_b, key="play_vtrac_index_hit")),
                    fmt_pct(rate(rows=rows_b, key="pack_box_hit")),
                    fmt_pct(rate(rows=rows_b, key="pack_straight_hit")),
                    (fmt_pct(pack_correct_rate) if pack_correct_rate is not None else "NA"),
                    (fmt_pct(pack_any_correct_rate) if pack_any_correct_rate is not None else "NA"),
                ]
            )
            + " |"
        )

    # Conditional conversion: how often does Play Card retain CU evidence?
    summary_lines.append("")
    summary_lines.append(f"### Conditional conversion (`{strategy}`)")
    summary_lines.append("- `P(play_hit_any_inclusive | CU_vtrac_index_hit)` answers: when CU touches the winner lane, how often does the budgeted card retain it?")
    summary_lines.append("- `P(play_hit_any_inclusive | CU_hit_any)` answers: when CU contains the exact winner (box/straight), how often does the budgeted card keep it?")
    summary_lines.append("")
    summary_lines.append("| Budget | P(play_hit_any_inclusive) | P(play_hit_any_inclusive \\| CU_vtrac_index_hit) | P(play_hit_any_inclusive \\| CU_hit_any) |")
    summary_lines.append("|---|---:|---:|---:|")
    for b in budgets:
        rows_b = by_budget.get(b, [])
        cu_lane = [r for r in rows_b if bool01(r.get("cu_union_vtrac_index_hit")) == 1]
        cu_exact = [r for r in rows_b if bool01(r.get("cu_union_hit_any")) == 1]
        summary_lines.append(
            "| "
            + " | ".join(
                [
                    b,
                    fmt_pct(rate(rows=rows_b, key="play_hit_any_inclusive")),
                    fmt_pct(rate(rows=cu_lane, key="play_hit_any_inclusive")),
                    fmt_pct(rate(rows=cu_exact, key="play_hit_any_inclusive")),
                ]
            )
            + " |"
        )

    # Attribution: pack vs filler (where did the inclusive hit come from?)
    summary_lines.append("")
    summary_lines.append("### Inclusive hit attribution (pack vs filler)")
    summary_lines.append("- `pack_hit_any_inclusive` / `filler_hit_any_inclusive` are already emitted by the play-card grader.")
    summary_lines.append("- If most inclusive hits come from `filler`, the chosen VTRAC pack is not doing the work we think it is.")
    summary_lines.append("")
    summary_lines.append("| Budget | pack_hit_any_inclusive | filler_hit_any_inclusive | among inclusive hits: pack share | among inclusive hits: filler share |")
    summary_lines.append("|---|---:|---:|---:|---:|")
    for b in budgets:
        rows_b = by_budget.get(b, [])
        rows_hit = [r for r in rows_b if bool01(r.get("play_hit_any_inclusive")) == 1]
        pack_share = None
        filler_share = None
        if rows_hit:
            pack_share = sum(bool01(r.get("pack_hit_any_inclusive")) for r in rows_hit) / float(len(rows_hit))
            filler_share = sum(bool01(r.get("filler_hit_any_inclusive")) for r in rows_hit) / float(len(rows_hit))
        summary_lines.append(
            "| "
            + " | ".join(
                [
                    b,
                    fmt_pct(rate(rows=rows_b, key="pack_hit_any_inclusive")),
                    fmt_pct(rate(rows=rows_b, key="filler_hit_any_inclusive")),
                    fmt_pct(pack_share),
                    fmt_pct(filler_share),
                ]
            )
            + " |"
        )

    # Bucket counts: where does it break?
    summary_lines.append("")
    summary_lines.append("### Break buckets (per budget)")
    summary_lines.append(
        "Bucket definitions (winner present only): `HIT_INCLUSIVE`, `CU_EXACT_BUT_PLAY_MISS`, `CU_LANE_BUT_PLAY_MISS`, `CU_MISS`, `NO_CU_JOIN`."
    )
    summary_lines.append("")
    summary_lines.append("| Budget | HIT_INCLUSIVE | CU_EXACT_BUT_PLAY_MISS | CU_LANE_BUT_PLAY_MISS | CU_MISS | NO_CU_JOIN |")
    summary_lines.append("|---|---:|---:|---:|---:|---:|")
    for b in budgets:
        rows_b = by_budget.get(b, [])
        total = len(rows_b) or 1
        hit = 0
        cu_exact_miss = 0
        cu_lane_miss = 0
        cu_miss = 0
        no_join = 0
        for r in rows_b:
            if (r.get("cu_union_hit_any") or "").strip() == "" and (r.get("cu_union_vtrac_index_hit") or "").strip() == "":
                no_join += 1
                continue
            if bool01(r.get("play_hit_any_inclusive")) == 1:
                hit += 1
                continue
            if bool01(r.get("cu_union_hit_any")) == 1:
                cu_exact_miss += 1
                continue
            if bool01(r.get("cu_union_vtrac_index_hit")) == 1:
                cu_lane_miss += 1
                continue
            cu_miss += 1
        summary_lines.append(
            "| "
            + " | ".join(
                [
                    b,
                    f"{hit} ({hit/total*100:.1f}%)",
                    f"{cu_exact_miss} ({cu_exact_miss/total*100:.1f}%)",
                    f"{cu_lane_miss} ({cu_lane_miss/total*100:.1f}%)",
                    f"{cu_miss} ({cu_miss/total*100:.1f}%)",
                    f"{no_join} ({no_join/total*100:.1f}%)",
                ]
            )
            + " |"
        )

    write_md(
        out_path=out_md,
        csv_path=out_csv,
        date_from=date_from.isoformat(),
        date_to=date_to.isoformat(),
        included_dates=included_dates,
        excluded_dates=excluded_dates,
        strategy=strategy,
        summary_lines=summary_lines,
    )

    if bool(args.write_casebook):
        cb_budget = str(args.casebook_budget).strip()
        tag_suffix = f"__{exp_tag}" if exp_tag else ""
        out_casebook = RUNS_DIR / f"{range_tag}__CONVERSION_CASEBOOK__{profile}__{strategy}{tag_suffix}__{cb_budget}.md"
        write_casebook(out_path=out_casebook, rows=out_rows, budget_label=cb_budget, max_cases=int(args.casebook_n))
        print(f"Wrote: {out_casebook.relative_to(REPO_ROOT)}")

    print(f"Wrote: {out_csv.relative_to(REPO_ROOT)}")
    print(f"Wrote: {out_md.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
