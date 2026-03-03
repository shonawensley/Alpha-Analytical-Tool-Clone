#!/usr/bin/env python3
"""
Export "compound co-fire" Profit Alert events as a compact Control Center board.

Goal:
  - Make the Blueprint's "compound profiles" first-class and visible.
  - Remain shadow-only: this does NOT feed tool_only Candidate Universe / Play Cards.
  - Prefer existing evaluation artifacts when present, but can fall back to the board.

Inputs (per day D):
  - sharepacks/<D>/control_center/profit_alerts.csv (required)
  - sharepacks/<D>/control_center/profit_alerts_eval_merged.csv (optional; adds episode outcomes)

Outputs (per day D):
  - sharepacks/<D>/control_center/profit_compound_events.csv
  - sharepacks/<D>/control_center/profit_compound_events.md

Usage:
  python3 scripts/tools/export_profit_compound_events.py --date 2025-06-21
  python3 scripts/tools/export_profit_compound_events.py --start 2025-12-30 --end 2026-01-09
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Set, Tuple


ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


PROMOTER_ALERT_IDS = {"A03", "A08"}


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


def safe_int(value: str) -> Optional[int]:
    v = (value or "").strip()
    if not v:
        return None
    try:
        return int(float(v))
    except Exception:
        return None


def load_csv_rows(path: Path) -> Iterable[Dict[str, str]]:
    with path.open(encoding="utf-8", errors="replace", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield {k: (v or "").strip() for k, v in row.items()}


def write_csv(path: Path, fieldnames: Sequence[str], rows: Sequence[Dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        dw = csv.DictWriter(f, fieldnames=list(fieldnames), extrasaction="ignore")
        dw.writeheader()
        for row in rows:
            dw.writerow(row)


def write_md(path: Path, lines: List[str]) -> None:
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def parse_json_obj(raw: str) -> Dict[str, object]:
    s = (raw or "").strip()
    if not s or s == "-":
        return {}
    try:
        obj = json.loads(s)
        return obj if isinstance(obj, dict) else {}
    except Exception:
        return {}


def parse_json_list(raw: str) -> List[str]:
    s = (raw or "").strip()
    if not s or s == "-":
        return []
    try:
        obj = json.loads(s)
    except Exception:
        return []
    if not isinstance(obj, list):
        return []
    out: List[str] = []
    for item in obj:
        if isinstance(item, str):
            out.append(item.strip())
        else:
            out.append(str(item))
    return out


def parse_csv_list(raw: str) -> List[str]:
    s = (raw or "").strip()
    if not s or s == "-":
        return []
    parts = [p.strip().upper() for p in s.split(",") if p.strip()]
    return parts


def md_table(rows: Sequence[Tuple[str, str]]) -> str:
    out: List[str] = []
    out.append("| Field | Value |")
    out.append("|---|---|")
    for k, v in rows:
        out.append(f"| {k} | {v} |")
    return "\n".join(out)


def md_simple_table(headers: Sequence[str], rows: Sequence[Sequence[str]]) -> str:
    h = list(headers)
    out = ["| " + " | ".join(h) + " |", "|" + "|".join(["---"] * len(h)) + "|"]
    for r in rows:
        out.append("| " + " | ".join(str(x) for x in r) + " |")
    return "\n".join(out)


@dataclass
class EnvAgg:
    state_key: str
    variant: str
    candidate_ids: Set[str]
    promoter_ids: Set[str]
    a11_star_level_max: int
    a11_star_score_max: float
    a12_sizes: Set[int]
    min_cap_lines: Optional[int]
    min_implied_set_size: Optional[int]
    strength_max: Optional[int]
    decay_min: Optional[int]
    decay_max: Optional[int]

    # Optional (if eval_merged exists)
    merged_rows_total: int = 0
    merged_hits: int = 0
    merged_any_hit_within_decay: str = ""
    merged_hit_types: Set[str] = None  # type: ignore[assignment]
    merged_any_hit_types: Set[str] = None  # type: ignore[assignment]

    def __post_init__(self) -> None:
        if self.merged_hit_types is None:
            self.merged_hit_types = set()
        if self.merged_any_hit_types is None:
            self.merged_any_hit_types = set()


TAG_WEIGHTS: Dict[str, int] = {
    "CLAMP_1": 100,
    "CARRY_PERM_HARDLOCK": 95,
    "ENGINE_GOV": 85,
    "STRAIGHT_GATE": 80,
    "CARRY_PERM_GOV": 75,
    "CARRY_PERM": 70,
    "IDX_ECHO_CLAMP": 65,
    "IDX_ECHO_BASE": 60,
    "XVAR_IDX_ECHO": 55,
    "DBL_BA_MIRROR": 50,
    "DBL_BA": 45,
    "DBL_MIRROR": 40,
    "CLAMP_2": 40,
    "CLAMP_4": 25,
    "CLAMP_ANY": 20,
}


def compute_watchlist_tags(*, candidates: Set[str], promoters: Set[str], a12_sizes: Set[int], a11_star_level: int) -> List[str]:
    tags: List[str] = []
    c = {x.strip().upper() for x in candidates if x}
    p = {x.strip().upper() for x in promoters if x}

    if {"A01", "A11"} <= c:
        tags.append("ENGINE_GOV")

    if "A11" in c and (("A05" in c) or ("A12" in c)):
        # "Straight overlay gate" (governor present + clamp/perm evidence present).
        tags.append("STRAIGHT_GATE")
        if a11_star_level >= 3:
            tags.append("STRAIGHT_GATE_STAR3PLUS")

    if "A12" in c:
        tags.append("CLAMP_ANY")
        if 1 in a12_sizes:
            tags.append("CLAMP_1")
        if 2 in a12_sizes:
            tags.append("CLAMP_2")
        if 4 in a12_sizes:
            tags.append("CLAMP_4")

    if {"A04", "A05"} <= c:
        tags.append("CARRY_PERM")
        if "A11" in c:
            tags.append("CARRY_PERM_GOV")
        if "A11" in c and "A03" in p:
            tags.append("CARRY_PERM_HARDLOCK")

    base = {"A01", "A04", "A06", "A11"}
    if "A09" in c and (c & base):
        tags.append("IDX_ECHO_BASE")
        if "A05" in c:
            tags.append("IDX_ECHO_CLAMP")

    if "A09" in c and "A03" in p:
        tags.append("XVAR_IDX_ECHO")

    # Doubles bundle: A02 timing + BA (A08) and/or mirror routing (A07).
    if "A02" in c and "A08" in p:
        tags.append("DBL_BA")
    if "A02" in c and "A07" in c:
        tags.append("DBL_MIRROR")
    if "A02" in c and "A07" in c and "A08" in p:
        tags.append("DBL_BA_MIRROR")

    # Stable deterministic order (highest weight first, then name)
    return sorted(tags, key=lambda t: (-TAG_WEIGHTS.get(t, 0), t))


def pick_top_event(tags: Sequence[str]) -> str:
    if not tags:
        return ""
    return sorted(tags, key=lambda t: (-TAG_WEIGHTS.get(t, 0), t))[0]


def tag_priority(tags: Sequence[str]) -> int:
    if not tags:
        return 0
    return max(TAG_WEIGHTS.get(t, 0) for t in tags)


def _row_type(alert_id: str, suggested: str) -> str:
    aid = (alert_id or "").strip().upper()
    sug = (suggested or "").strip().upper()
    if sug in {"OVERLAY", "SKIP"} or aid in PROMOTER_ALERT_IDS:
        return "PROMOTER"
    if aid == "A11":
        return "GOVERNOR"
    return "CANDIDATE"


def aggregate_environment_from_board(board_rows: Iterable[Dict[str, str]]) -> Dict[Tuple[str, str], EnvAgg]:
    env: Dict[Tuple[str, str], EnvAgg] = {}

    for row in board_rows:
        state_key = (row.get("StateKey") or "").strip()
        variant = (row.get("Variant") or "").strip()
        if not state_key or not variant:
            continue

        alert_id = (row.get("AlertId") or "").strip().upper()
        suggested = (row.get("Suggested") or "").strip()
        rt = _row_type(alert_id, suggested)

        key = (state_key, variant)
        if key not in env:
            env[key] = EnvAgg(
                state_key=state_key,
                variant=variant,
                candidate_ids=set(),
                promoter_ids=set(),
                a11_star_level_max=0,
                a11_star_score_max=0.0,
                a12_sizes=set(),
                min_cap_lines=None,
                min_implied_set_size=None,
                strength_max=None,
                decay_min=None,
                decay_max=None,
            )
        e = env[key]

        if rt == "PROMOTER":
            e.promoter_ids.add(alert_id)
        else:
            e.candidate_ids.add(alert_id)

        strength = safe_int(row.get("Strength") or "")
        if strength is not None:
            e.strength_max = strength if e.strength_max is None else max(e.strength_max, strength)

        cap = safe_int(row.get("CapLines") or "")
        if cap is not None:
            e.min_cap_lines = cap if e.min_cap_lines is None else min(e.min_cap_lines, cap)

        decay = safe_int(row.get("DecayDraws") or "")
        if decay is not None:
            e.decay_max = decay if e.decay_max is None else max(e.decay_max, decay)
            e.decay_min = decay if e.decay_min is None else min(e.decay_min, decay)

        implied = parse_json_list(row.get("ImpliedSet") or "")
        if implied:
            e.min_implied_set_size = len(implied) if e.min_implied_set_size is None else min(e.min_implied_set_size, len(implied))

        if alert_id == "A12":
            if implied:
                e.a12_sizes.add(len(implied))

        if alert_id == "A11":
            evidence = parse_json_obj(row.get("Evidence") or "")
            star_level = safe_int(str(evidence.get("star_level") or "")) or 0
            try:
                star_score = float(evidence.get("a11_star_score") or 0.0)
            except Exception:
                star_score = 0.0
            e.a11_star_level_max = max(e.a11_star_level_max, star_level)
            e.a11_star_score_max = max(e.a11_star_score_max, star_score)

    return env


def enrich_with_merged_eval(env: Dict[Tuple[str, str], EnvAgg], merged_rows: Iterable[Dict[str, str]]) -> None:
    for row in merged_rows:
        state_key = (row.get("state_key") or "").strip()
        variant = (row.get("variant") or "").strip()
        if not state_key or not variant:
            continue
        key = (state_key, variant)
        e = env.get(key)
        if e is None:
            continue
        e.merged_rows_total += 1
        status = (row.get("status") or "").strip().upper()
        if status == "HIT":
            e.merged_hits += 1
        had = (row.get("hit_any_within_decay") or "").strip().upper()
        if had == "Y":
            e.merged_any_hit_within_decay = "Y"
        elif had == "N" and e.merged_any_hit_within_decay != "Y":
            e.merged_any_hit_within_decay = "N"
        for t in parse_csv_list(row.get("hit_type") or ""):
            e.merged_hit_types.add(t)
        for t in parse_csv_list(row.get("hit_any_type") or ""):
            e.merged_any_hit_types.add(t)


def export_day(*, date: str, sharepacks_root: Path, include_all: bool) -> Optional[Tuple[Path, Path]]:
    cc_dir = sharepacks_root / date / "control_center"
    board_csv = cc_dir / "profit_alerts.csv"
    if not board_csv.exists():
        return None

    env = aggregate_environment_from_board(load_csv_rows(board_csv))

    merged_csv = cc_dir / "profit_alerts_eval_merged.csv"
    if merged_csv.exists():
        enrich_with_merged_eval(env, load_csv_rows(merged_csv))

    # Build rows
    out_rows: List[Dict[str, object]] = []
    tag_counts: Counter[str] = Counter()
    for (state_key, variant), e in sorted(env.items(), key=lambda kv: (kv[0][0], kv[0][1])):
        tags = compute_watchlist_tags(
            candidates=e.candidate_ids,
            promoters=e.promoter_ids,
            a12_sizes=e.a12_sizes,
            a11_star_level=e.a11_star_level_max,
        )
        if not tags and not include_all:
            continue
        for t in tags:
            tag_counts[t] += 1
        out_rows.append(
            {
                "results_date": date,
                "state_key": state_key,
                "variant": variant,
                "top_event": pick_top_event(tags),
                "priority": tag_priority(tags),
                "watchlist_tags": "|".join(tags),
                "candidate_alert_ids": ",".join(sorted(e.candidate_ids)),
                "promoter_alert_ids": ",".join(sorted(e.promoter_ids)),
                "a11_star_level_max": e.a11_star_level_max or 0,
                "a11_star_score_max": f"{e.a11_star_score_max:.3f}",
                "a12_pack_sizes": ",".join(str(x) for x in sorted(e.a12_sizes)),
                "min_implied_set_size": "" if e.min_implied_set_size is None else str(e.min_implied_set_size),
                "min_cap_lines": "" if e.min_cap_lines is None else str(e.min_cap_lines),
                "strength_max": "" if e.strength_max is None else str(e.strength_max),
                "decay_min": "" if e.decay_min is None else str(e.decay_min),
                "decay_max": "" if e.decay_max is None else str(e.decay_max),
                "merged_rows_total": e.merged_rows_total,
                "merged_hits": e.merged_hits,
                "merged_any_hit_within_decay": e.merged_any_hit_within_decay or "",
                "merged_hit_types": ",".join(sorted(e.merged_hit_types)),
                "merged_any_hit_types": ",".join(sorted(e.merged_any_hit_types)),
            }
        )

    # Deterministic sort for the CSV and MD view
    out_rows_sorted = sorted(
        out_rows,
        key=lambda r: (
            -int(r.get("priority") or 0),
            -(safe_int(str(r.get("a11_star_level_max") or "")) or 0),
            safe_int(str(r.get("min_implied_set_size") or "")) or 9999,
            str(r.get("state_key") or ""),
            str(r.get("variant") or ""),
        ),
    )

    out_csv = cc_dir / "profit_compound_events.csv"
    out_md = cc_dir / "profit_compound_events.md"

    fields = [
        "results_date",
        "state_key",
        "variant",
        "top_event",
        "priority",
        "watchlist_tags",
        "candidate_alert_ids",
        "promoter_alert_ids",
        "a11_star_level_max",
        "a11_star_score_max",
        "a12_pack_sizes",
        "min_implied_set_size",
        "min_cap_lines",
        "strength_max",
        "decay_min",
        "decay_max",
        "merged_rows_total",
        "merged_hits",
        "merged_any_hit_within_decay",
        "merged_hit_types",
        "merged_any_hit_types",
    ]
    write_csv(out_csv, fields, out_rows_sorted)

    # Markdown view
    md: List[str] = []
    md.append(f"# Profit Compound Events — {date}")
    md.append("")
    md.append("This is a **shadow-only** triage board derived from Profit Alerts.")
    md.append("It flags “watchlist” compound co-fire environments defined in:")
    md.append("- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Compound_Events_Watchlist.md`")
    md.append("")
    md.append("## Counts")
    md.append(md_table([("Tagged rows", str(len(out_rows_sorted))), ("Unique tags", str(len(tag_counts)))]))
    md.append("")
    if tag_counts:
        md.append("## Tag counts")
        md.append("")
        md.append(
            md_simple_table(
                ["Tag", "Count", "Weight"],
                [[t, str(n), str(TAG_WEIGHTS.get(t, 0))] for t, n in sorted(tag_counts.items(), key=lambda kv: (-kv[1], -TAG_WEIGHTS.get(kv[0], 0), kv[0]))],
            )
        )
        md.append("")
    md.append("## Rows (sorted)")
    md.append("")
    headers = [
        "Priority",
        "StateKey",
        "Variant",
        "TopEvent",
        "Tags",
        "A11★",
        "A12 sizes",
        "MinSet",
        "MinCap",
        "MergedHit",
    ]
    table_rows: List[List[str]] = []
    for r in out_rows_sorted[:60]:
        table_rows.append(
            [
                str(r.get("priority") or ""),
                str(r.get("state_key") or ""),
                str(r.get("variant") or ""),
                str(r.get("top_event") or ""),
                str(r.get("watchlist_tags") or ""),
                str(r.get("a11_star_level_max") or ""),
                str(r.get("a12_pack_sizes") or ""),
                str(r.get("min_implied_set_size") or ""),
                str(r.get("min_cap_lines") or ""),
                ("Y" if int(r.get("merged_hits") or 0) > 0 else ("N" if str(r.get("merged_any_hit_within_decay") or "") == "N" else "")),
            ]
        )
    md.append(md_simple_table(headers, table_rows) if table_rows else "_No tagged rows._")
    md.append("")
    md.append("## Regenerate")
    md.append("```bash")
    md.append(f"python3 scripts/tools/export_profit_compound_events.py --date {date}")
    md.append("```")
    md.append("")
    write_md(out_md, md)

    return (out_csv, out_md)


def main() -> None:
    ap = argparse.ArgumentParser(description="Export Profit compound co-fire events for one or more sharepack days.")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--date", help="Results date D (YYYY-MM-DD)")
    g.add_argument("--start", help="Window start date (YYYY-MM-DD)")
    ap.add_argument("--end", help="Window end date (YYYY-MM-DD) (required with --start)")
    ap.add_argument("--sharepacks-dir", default=str(ROOT / "sharepacks"), help="Sharepacks root directory")
    ap.add_argument("--include-all", action="store_true", help="Include non-tagged state/variant rows")
    args = ap.parse_args()

    sharepacks_root = Path(args.sharepacks_dir)
    dates = [args.date] if args.date else daterange(args.start, args.end)
    if args.start and not args.end:
        raise SystemExit("--end is required with --start")

    wrote = 0
    for d in dates:
        res = export_day(date=d, sharepacks_root=sharepacks_root, include_all=bool(args.include_all))
        if not res:
            continue
        out_csv, out_md = res
        wrote += 1
        print(f"Wrote: {out_csv}")
        print(f"Wrote: {out_md}")
    if wrote == 0:
        raise SystemExit("No days exported (missing profit_alerts.csv).")


if __name__ == "__main__":
    main()
