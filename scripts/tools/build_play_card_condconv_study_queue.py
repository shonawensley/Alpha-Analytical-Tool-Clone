#!/usr/bin/env python3
"""
Build a small, winners-output-linked study queue for conditional conversion experiments.

This is a review/evidence helper:
- Reads existing RUNS grade CSVs + sharepack artifacts (play_card, candidate_universe, winners JSON).
- Writes a Markdown queue into RUNS.
- Does NOT modify sharepacks or analyzers.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _read_json(path: Path) -> object:
    return json.loads(_read_text(path))


def _safe_rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _normalize_experiment_tag(value: str) -> str:
    raw = str(value or "").strip()
    if not raw:
        return ""
    raw = raw.replace(" ", "_")
    cleaned = re.sub(r"[^A-Za-z0-9_-]+", "", raw)
    cleaned = cleaned.strip("_-")
    if not cleaned:
        raise SystemExit(f"Invalid --experiment-tag: {value!r} (must contain A-Z/a-z/0-9/_/-)")
    return cleaned[:60]


def _runs_dir() -> Path:
    return REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"


def _iter_dates(start: str, end: str) -> List[str]:
    d0 = date.fromisoformat(start)
    d1 = date.fromisoformat(end)
    if d1 < d0:
        raise SystemExit("--end must be >= --start")
    out: List[str] = []
    cur = d0
    while cur <= d1:
        out.append(cur.isoformat())
        cur += timedelta(days=1)
    return out


def _grade_csv_path(*, results_date: str, tag: str) -> Path:
    suffix = f"__{tag}" if tag else ""
    return _runs_dir() / f"{results_date}__PLAY_CARD_GRADE__tool_only{suffix}.csv"


def _find_winner_json(*, sharepacks_root: Path, results_date: str, state_key: str, winner: str) -> Optional[Path]:
    winners_dir = sharepacks_root / results_date / state_key / "winners" / state_key
    if not winners_dir.exists():
        return None
    hits = sorted(winners_dir.glob(f"*winner_{winner}_*.json"))
    return hits[0] if hits else None


def _winner_stats_summary(winner_json: Path) -> str:
    raw = _read_json(winner_json)
    if not isinstance(raw, dict):
        return ""
    index = raw.get("index")
    winner_combo = raw.get("winner_combo")
    stats = raw.get("stats") if isinstance(raw.get("stats"), dict) else {}
    occ = stats.get("pattern_occurrence") if isinstance(stats.get("pattern_occurrence"), dict) else {}
    top = sorted(((k, v) for k, v in occ.items() if isinstance(v, int)), key=lambda kv: (-kv[1], kv[0]))[:5]
    top_s = ", ".join([f"{k}:{v}" for k, v in top]) if top else ""
    parts: List[str] = []
    if isinstance(index, int):
        parts.append(f"idx={index}")
    if isinstance(winner_combo, str) and winner_combo:
        parts.append(f"winner={winner_combo}")
    if top_s:
        parts.append(f"top_occ={top_s}")
    return " | ".join(parts)


def _candidate_universe_recall(
    *, sharepacks_root: Path, results_date: str, state_key: str, tag: str, winner: str, winner_canonical: str
) -> str:
    cu_path = sharepacks_root / results_date / state_key / f"candidate_universe__tool_only__{tag}.json"
    if not cu_path.exists():
        return "CU:missing"
    raw = _read_json(cu_path)
    if not isinstance(raw, dict):
        return "CU:invalid"
    union = raw.get("union_combos") if isinstance(raw.get("union_combos"), list) else []
    union = [str(x) for x in union if isinstance(x, str)]
    has_straight = winner in union
    has_canon = any("".join(sorted(x)) == winner_canonical for x in union if x and len(x) == 3 and x.isdigit())
    return f"CU:straight={'Y' if has_straight else 'N'} canon={'Y' if has_canon else 'N'} union={len(union)}"


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Build a conditional conversion study queue (winners-output linked).")
    ap.add_argument("--start", required=True, help="Start date (YYYY-MM-DD), inclusive")
    ap.add_argument("--end", required=True, help="End date (YYYY-MM-DD), inclusive")
    ap.add_argument("--experiment-tag", required=True, help="Experiment tag containing conditional strategies (e.g. condconv_v3)")
    ap.add_argument("--sharepacks-root", default="sharepacks", help="Sharepacks root (default: sharepacks)")
    ap.add_argument("--baseline-strategy", default="play_box_first", help="Baseline strategy name (default: play_box_first)")
    ap.add_argument(
        "--test-strategy",
        default="conversion_box_first_conditional_lenient_presetB",
        help="Test strategy name (default: conversion_box_first_conditional_lenient_presetB)",
    )
    ap.add_argument("--budget", default="B12", help="Budget label (default: B12)")
    ap.add_argument("--out-md", default=None, help="Override output path")
    return ap.parse_args()


def main() -> None:
    args = parse_args()
    tag = _normalize_experiment_tag(args.experiment_tag)
    baseline = str(args.baseline_strategy).strip()
    test = str(args.test_strategy).strip()
    budget = str(args.budget).strip()

    sharepacks_root = Path(args.sharepacks_root)
    if not sharepacks_root.is_absolute():
        sharepacks_root = (REPO_ROOT / sharepacks_root).resolve()

    diffs: List[Dict[str, str]] = []
    for d in _iter_dates(args.start, args.end):
        grade_path = _grade_csv_path(results_date=d, tag=tag)
        if not grade_path.exists():
            continue
        rows = list(csv.DictReader(_read_text(grade_path).splitlines()))
        idx: Dict[Tuple[str, str, str, str], Dict[str, str]] = {
            (r["state_key"], r["winner_label"], r["strategy"], r["budget_label"]): r for r in rows
        }
        for state_key in sorted({r["state_key"] for r in rows}):
            for winner_label in ("Midday", "Evening"):
                base = idx.get((state_key, winner_label, baseline, budget))
                tst = idx.get((state_key, winner_label, test, budget))
                if not base or not tst:
                    continue
                if base.get("winner_missing") == "1":
                    continue

                def ext(r: Dict[str, str]) -> bool:
                    return (r.get("hit_any") == "1") or (r.get("canon_hit_any_perm") == "1") or (r.get("vtrac_index_hit") == "1")

                if (
                    base.get("hit_any") == tst.get("hit_any")
                    and base.get("canon_hit_any_perm") == tst.get("canon_hit_any_perm")
                    and base.get("vtrac_index_hit") == tst.get("vtrac_index_hit")
                    and ext(base) == ext(tst)
                ):
                    continue

                winner = base.get("winner") or ""
                winner_canon = base.get("winner_canonical") or ""
                winner_json = _find_winner_json(sharepacks_root=sharepacks_root, results_date=d, state_key=state_key, winner=winner)

                diffs.append(
                    {
                        "date": d,
                        "state": state_key,
                        "label": winner_label,
                        "winner": winner,
                        "hit_any": f"{base.get('hit_any','0')}→{tst.get('hit_any','0')}",
                        "perm_hit": f"{base.get('canon_hit_any_perm','0')}→{tst.get('canon_hit_any_perm','0')}",
                        "vtrac_hit": f"{base.get('vtrac_index_hit','0')}→{tst.get('vtrac_index_hit','0')}",
                        "ext_hit": f"{'1' if ext(base) else '0'}→{'1' if ext(tst) else '0'}",
                        "winners_json": _safe_rel(winner_json) if winner_json else "",
                        "winner_summary": _winner_stats_summary(winner_json) if winner_json else "",
                        "cu_recall": _candidate_universe_recall(
                            sharepacks_root=sharepacks_root,
                            results_date=d,
                            state_key=state_key,
                            tag=tag,
                            winner=winner,
                            winner_canonical=winner_canon,
                        ),
                        "tables_json": _safe_rel(sharepacks_root / d / state_key / "json" / f"{state_key}_tables.json"),
                        "candidate_universe": _safe_rel(
                            sharepacks_root / d / state_key / f"candidate_universe__tool_only__{tag}.json"
                        ),
                        "play_card": _safe_rel(sharepacks_root / d / state_key / f"play_card__tool_only__{tag}.json"),
                    }
                )

    runs_dir = _runs_dir()
    runs_dir.mkdir(parents=True, exist_ok=True)
    default_out = runs_dir / f"{args.start}_to_{args.end}__COND_CONV_STUDY_QUEUE__{tag}.md"
    out_md = Path(args.out_md) if args.out_md else default_out

    lines: List[str] = [
        f"# Conditional Conversion Study Queue — {args.start} → {args.end}",
        "",
        f"- generated_at: `{_now_iso()}`",
        f"- experiment_tag: `{tag}`",
        f"- sharepacks_root: `{_safe_rel(sharepacks_root)}`",
        f"- baseline: `{baseline}/{budget}`",
        f"- test: `{test}/{budget}`",
        f"- rows_with_deltas: `{len(diffs)}`",
        "",
        "## Cases (only rows where baseline vs test differs)",
        "",
        "| date | state | label | winner | hit_any | perm_hit | vtrac_hit | ext_hit | winners_json | winner_summary | cu_recall |",
        "|---|---|---|---|---:|---:|---:|---:|---|---|---|",
    ]
    for r in diffs:
        lines.append(
            "| "
            + " | ".join(
                [
                    r["date"],
                    r["state"],
                    r["label"],
                    r["winner"],
                    r["hit_any"],
                    r["perm_hit"],
                    r["vtrac_hit"],
                    r["ext_hit"],
                    f"`{r['winners_json']}`" if r.get("winners_json") else "",
                    r.get("winner_summary") or "",
                    r.get("cu_recall") or "",
                ]
            )
            + " |"
        )

    if diffs:
        lines += ["", "## Per-case artifact pointers", ""]
        for r in diffs:
            lines += [
                f"### {r['date']} — {r['state']} — {r['label']} — winner {r['winner']}",
                f"- winners_json: `{r['winners_json']}`" if r.get("winners_json") else "- winners_json: (missing)",
                f"- tables_json: `{r['tables_json']}`",
                f"- candidate_universe: `{r['candidate_universe']}`",
                f"- play_card: `{r['play_card']}`",
                "",
            ]

    out_md.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"Wrote: {_safe_rel(out_md)}")


if __name__ == "__main__":
    main()

