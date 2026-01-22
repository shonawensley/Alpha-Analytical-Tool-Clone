#!/usr/bin/env python3
"""
Build a small, winners-output-linked study queue for VTRAC boxed-member pack experiments.

This is a review/evidence helper:
- Reads existing RUNS windowed-grade CSVs + sharepack artifacts (play_card, winners JSON/HTML).
- Writes a Markdown queue into RUNS.
- Does NOT modify sharepacks or analyzers.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple


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


def _parse_date(s: str) -> date:
    return date.fromisoformat(str(s).strip())


def _iter_dates(start: str, end: str) -> List[str]:
    d0 = _parse_date(start)
    d1 = _parse_date(end)
    if d1 < d0:
        raise SystemExit("--end-date must be >= --start-date")
    out: List[str] = []
    cur = d0
    while cur <= d1:
        out.append(cur.isoformat())
        cur += timedelta(days=1)
    return out


def _normalize_pick3_literal(value: str) -> str:
    digits = "".join(ch for ch in str(value) if ch.isdigit())
    if not digits:
        return ""
    digits = digits.zfill(3) if len(digits) <= 3 else digits
    return digits if len(digits) == 3 else ""


def _winner_vtrac_index(winner: str) -> Optional[int]:
    import modules.vtrac_reference as vr

    w = _normalize_pick3_literal(winner)
    if not w:
        return None
    idx = vr.get_vtrac_index(w)
    return idx if isinstance(idx, int) else None


@dataclass(frozen=True)
class Winner:
    midday: Optional[str]
    evening: Optional[str]


def _load_results_winners(results_file: Path) -> Dict[str, Winner]:
    if not results_file.exists():
        return {}
    from alpha_analytical.control_center.batch_runner import (  # type: ignore
        parse_winner_sheet,
        _PROJECT_STATE_CANDIDATES,
    )

    text = _read_text(results_file)
    entries = parse_winner_sheet(text)

    winners: Dict[str, Winner] = {}
    for entry in entries:
        canonical = getattr(entry, "canonical", None)
        midday = getattr(entry, "midday", None)
        evening = getattr(entry, "evening", None)
        if not canonical:
            continue
        candidates = _PROJECT_STATE_CANDIDATES.get(canonical)
        if not candidates:
            project_state = getattr(entry, "project_state", None)
            candidates = (project_state,) if project_state else ()
        for state_key in candidates:
            if not state_key:
                continue
            winners[state_key] = Winner(
                midday=_normalize_pick3_literal(midday or ""),
                evening=_normalize_pick3_literal(evening or ""),
            )
    return winners


def _draw_slots_for_state(*, start_date: str, window_draws: int, state_key: str) -> List[Tuple[str, str, str]]:
    """
    Returns [(date, label, winner)] for up to window_draws slots.
    label is Midday/Evening.
    """
    start = _parse_date(start_date)
    slots: List[Tuple[str, str, str]] = []
    offset_days = 0
    while len(slots) < int(window_draws) and offset_days < 31:
        d = start.fromordinal(start.toordinal() + offset_days)
        dstr = d.isoformat()
        winners = _load_results_winners(REPO_ROOT / "data" / "results" / f"{dstr}.txt")
        w = winners.get(state_key, Winner(midday=None, evening=None))
        slots.append((dstr, "Midday", _normalize_pick3_literal(w.midday or "")))
        if len(slots) >= int(window_draws):
            break
        slots.append((dstr, "Evening", _normalize_pick3_literal(w.evening or "")))
        offset_days += 1
    return slots[: int(window_draws)]


def _find_winners_artifacts(
    *, sharepacks_root: Path, results_date: str, state_key: str, winner: str
) -> Tuple[Optional[Path], Optional[Path]]:
    winners_dir = sharepacks_root / results_date / state_key / "winners" / state_key
    if not winners_dir.exists():
        return None, None
    winner_norm = _normalize_pick3_literal(winner)
    if not winner_norm:
        return None, None
    json_hits = sorted(winners_dir.glob(f"*winner_{winner_norm}_*.json"))
    html_hits = sorted(winners_dir.glob(f"*winner_{winner_norm}_*.html"))
    j = json_hits[-1] if json_hits else None
    h = html_hits[-1] if html_hits else None
    return j, h


def _windowed_grade_csv_path(*, start: str, end: str, tag: str, n: int) -> Path:
    suffix = f"__{tag}" if tag else ""
    return _runs_dir() / f"{start}_to_{end}__PLAY_CARD_WINDOWED_GRADE__tool_only{suffix}__N{n}.csv"


def _chosen_vtrac_pack_index(
    *, sharepacks_root: Path, start_date: str, state_key: str, tag: str, strategy: str, budget: str
) -> Tuple[Optional[int], List[str]]:
    pc_path = sharepacks_root / start_date / state_key / f"play_card__tool_only__{tag}.json"
    raw = _read_json(pc_path) if pc_path.exists() else None
    if not isinstance(raw, dict):
        return None, []
    strategies = raw.get("strategies")
    if not isinstance(strategies, dict):
        return None, []
    card = strategies.get(strategy, {})
    if not isinstance(card, dict):
        return None, []
    b = card.get(budget, {})
    if not isinstance(b, dict):
        return None, []
    vp = b.get("vtrac_pack")
    if not isinstance(vp, dict):
        return None, []
    idx = vp.get("index")
    pack = vp.get("pack_combos") or []
    if not isinstance(pack, list):
        pack = []
    pack_norm = [_normalize_pick3_literal(x) for x in pack]
    pack_norm = [x for x in pack_norm if x]
    return (int(idx) if isinstance(idx, int) else None), pack_norm


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Build a VTRAC pack study queue (winners-output linked).")
    ap.add_argument("--start-date", required=True, help="Start date (YYYY-MM-DD), inclusive")
    ap.add_argument("--end-date", required=True, help="End date (YYYY-MM-DD), inclusive")
    ap.add_argument("--experiment-tag", required=True, help="Play card experiment tag (e.g., vtracpack_v1)")
    ap.add_argument("--sharepacks-root", default="sharepacks", help="Sharepacks root (default: sharepacks)")
    ap.add_argument("--window-draws", type=int, default=5, help="Window draw slots (default: 5)")
    ap.add_argument("--budget", default="B12", help="Budget label (default: B12)")
    ap.add_argument("--baseline-strategy", default="analysis_prefix", help="Baseline strategy (default: analysis_prefix)")
    ap.add_argument(
        "--test-strategy",
        default="vtrac_pack_boxed_first",
        help="Test strategy (default: vtrac_pack_boxed_first)",
    )
    ap.add_argument(
        "--mode",
        choices=["diffs", "misses", "all"],
        default="diffs",
        help="Which cases to include: diffs (baseline != test), misses (test miss only), all (default: diffs)",
    )
    ap.add_argument("--out-md", default=None, help="Override output path")
    return ap.parse_args()


def main() -> None:
    args = parse_args()
    tag = _normalize_experiment_tag(args.experiment_tag)
    baseline = str(args.baseline_strategy).strip()
    test = str(args.test_strategy).strip()
    budget = str(args.budget).strip()
    window_draws = int(args.window_draws)

    sharepacks_root = Path(args.sharepacks_root)
    if not sharepacks_root.is_absolute():
        sharepacks_root = (REPO_ROOT / sharepacks_root).resolve()

    grade_csv = _windowed_grade_csv_path(start=args.start_date, end=args.end_date, tag=tag, n=window_draws)
    if not grade_csv.exists():
        raise SystemExit(f"Missing windowed-grade CSV: {_safe_rel(grade_csv)}")

    rows = list(csv.DictReader(_read_text(grade_csv).splitlines()))
    idx: Dict[Tuple[str, str, str], Dict[str, str]] = {
        (r["start_date"], r["state_key"], r["strategy"]): r for r in rows if r.get("budget_label") == budget
    }

    out_rows: List[Dict[str, str]] = []
    for start_date in _iter_dates(args.start_date, args.end_date):
        for state_key in sorted({r["state_key"] for r in rows if r.get("start_date") == start_date}):
            base = idx.get((start_date, state_key, baseline))
            tst = idx.get((start_date, state_key, test))
            if not base or not tst:
                continue

            base_hit = base.get("hit_any_inclusive_window") == "1"
            tst_hit = tst.get("hit_any_inclusive_window") == "1"
            if args.mode == "diffs" and base_hit == tst_hit:
                continue
            if args.mode == "misses" and tst_hit:
                continue

            chosen_idx, pack = _chosen_vtrac_pack_index(
                sharepacks_root=sharepacks_root,
                start_date=start_date,
                state_key=state_key,
                tag=tag,
                strategy=test,
                budget=budget,
            )

            first_hit_n = int(tst.get("first_hit_any_inclusive_draw") or "0")
            slots = _draw_slots_for_state(start_date=start_date, window_draws=window_draws, state_key=state_key)
            hit_date, hit_label, hit_winner = ("", "", "")
            if 1 <= first_hit_n <= len(slots):
                hit_date, hit_label, hit_winner = slots[first_hit_n - 1]

            hit_idx = _winner_vtrac_index(hit_winner) if hit_winner else None
            wj, wh = _find_winners_artifacts(
                sharepacks_root=sharepacks_root, results_date=hit_date or start_date, state_key=state_key, winner=hit_winner
            )

            out_rows.append(
                {
                    "start_date": start_date,
                    "state": state_key,
                    "baseline_hit": "1" if base_hit else "0",
                    "test_hit": "1" if tst_hit else "0",
                    "test_first_hit_draw": str(first_hit_n) if first_hit_n else "",
                    "hit_date": hit_date,
                    "hit_label": hit_label,
                    "hit_winner": hit_winner,
                    "hit_winner_index": str(hit_idx) if hit_idx is not None else "",
                    "chosen_index": str(chosen_idx) if chosen_idx is not None else "",
                    "chosen_eq_hit_index": "1" if (chosen_idx is not None and hit_idx is not None and chosen_idx == hit_idx) else "0",
                    "pack": " ".join(pack),
                    "winners_json": _safe_rel(wj) if wj else "",
                    "winners_html": _safe_rel(wh) if wh else "",
                    "play_card": _safe_rel(sharepacks_root / start_date / state_key / f"play_card__tool_only__{tag}.json"),
                }
            )

    runs_dir = _runs_dir()
    runs_dir.mkdir(parents=True, exist_ok=True)
    default_out = runs_dir / f"{args.start_date}_to_{args.end_date}__VTRAC_PACK_STUDY_QUEUE__{tag}__N{window_draws}.md"
    out_md = Path(args.out_md) if args.out_md else default_out

    lines: List[str] = [
        f"# VTRAC Pack Study Queue — {args.start_date} → {args.end_date}",
        "",
        f"- generated_at: `{_now_iso()}`",
        f"- sharepacks_root: `{_safe_rel(sharepacks_root)}`",
        f"- experiment_tag: `{tag}`",
        f"- window_draws: `{window_draws}` (Midday/Evening slots)",
        f"- budget: `{budget}`",
        f"- baseline_strategy: `{baseline}`",
        f"- test_strategy: `{test}`",
        f"- mode: `{args.mode}`",
        "",
        "## Cases",
        "",
        "| start_date | state | base_hit | test_hit | first_hit | hit_date | hit_label | winner | idx | chosen | eq | pack | winners_html | play_card |",
        "|---|---|---:|---:|---:|---|---|---|---:|---:|---:|---|---|---|",
    ]

    for r in out_rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    r["start_date"],
                    r["state"],
                    r["baseline_hit"],
                    r["test_hit"],
                    r["test_first_hit_draw"],
                    r["hit_date"],
                    r["hit_label"],
                    r["hit_winner"],
                    r["hit_winner_index"],
                    r["chosen_index"],
                    r["chosen_eq_hit_index"],
                    r["pack"],
                    f"`{r['winners_html']}`" if r["winners_html"] else "",
                    f"`{r['play_card']}`" if r["play_card"] else "",
                ]
            )
            + " |"
        )

    out_md.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"Wrote: {_safe_rel(out_md)} (rows={len(out_rows)})")


if __name__ == "__main__":
    main()

