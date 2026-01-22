#!/usr/bin/env python3
"""
Windowed grading for play_card.json artifacts.

Purpose:
- Training docs often frame success as "hit within 2–5 draws", not necessarily same-draw.
- This tool evaluates: if you took a Play Card emitted on date D and replayed it
  across the next N draw-slots (Midday/Evening), would it have hit?

This is analysis-only:
- Reads:
  - sharepacks/<root>/<D>/<STATE>/play_card*.json
  - data/results/<D>.txt (and subsequent dates as needed)
- Writes: docs/AAT9_KIT/FINAL VALIDATION/RUNS/* (never into predictive sharepacks).
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Set, Tuple


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))


def _runs_dir() -> Path:
    return REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"


def _safe_rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _read_json(path: Path) -> object:
    return json.loads(_read_text(path))


def _normalize_pick3_literal(value: str) -> str:
    digits = "".join(ch for ch in str(value) if ch.isdigit())
    if not digits:
        return ""
    digits = digits.zfill(3) if len(digits) <= 3 else digits
    return digits if len(digits) == 3 else ""


def _canon(draw: str) -> str:
    d = _normalize_pick3_literal(draw)
    return "".join(sorted(d)) if d else ""


def _unique_perms(triad: str) -> Set[str]:
    from itertools import permutations

    triad = _normalize_pick3_literal(triad)
    if not triad:
        return set()
    return {"".join(p) for p in permutations(triad, 3)}


def _boxed_canonicals(combos: Sequence[str]) -> Set[str]:
    by_canon: Dict[str, Set[str]] = {}
    for c in combos:
        c = _normalize_pick3_literal(c)
        if not c:
            continue
        by_canon.setdefault(_canon(c), set()).add(c)
    boxed: Set[str] = set()
    for canon, members in by_canon.items():
        perms = _unique_perms(canon)
        if perms and perms.issubset(members):
            boxed.add(canon)
    return boxed


def _pack_vtrac_indices(combos: Sequence[str]) -> Set[int]:
    import modules.vtrac_reference as vr

    indices: Set[int] = set()
    for combo in combos:
        c = _normalize_pick3_literal(combo)
        if not c:
            continue
        idx = vr.get_vtrac_index(c)
        if isinstance(idx, int):
            indices.add(idx)
    return indices


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


def _iter_state_dirs(day_dir: Path, *, states: Sequence[str] | None) -> List[Path]:
    if states:
        return [day_dir / s for s in states]
    out: List[Path] = []
    for p in sorted(day_dir.iterdir(), key=lambda q: q.name):
        if not p.is_dir():
            continue
        if p.name == "control_center":
            continue
        out.append(p)
    return out


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


def _parse_date(s: str) -> date:
    parts = (s or "").strip().split("-")
    if len(parts) != 3:
        raise ValueError(f"Invalid date: {s!r} (expected YYYY-MM-DD)")
    try:
        return date(int(parts[0]), int(parts[1]), int(parts[2]))
    except Exception as exc:
        raise ValueError(f"Invalid date: {s!r} (expected YYYY-MM-DD)") from exc


def _iter_dates_between(sharepacks_root: Path, start: date, end: date) -> List[str]:
    out: List[str] = []
    for p in sorted(sharepacks_root.iterdir(), key=lambda q: q.name):
        if not p.is_dir():
            continue
        try:
            d = _parse_date(p.name)
        except Exception:
            continue
        if start <= d <= end:
            out.append(p.name)
    return out


def _draw_slots_for_state(
    *,
    start_date: str,
    window_draws: int,
    state_key: str,
) -> List[Tuple[str, str, str]]:
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


def _first_hit_index(flags: Sequence[bool]) -> str:
    for i, v in enumerate(flags):
        if v:
            return str(i + 1)
    return ""


def main() -> None:
    ap = argparse.ArgumentParser(description="Windowed grading for play_card artifacts (hit within N draws).")
    ap.add_argument("--start-date", required=True, help="Start date (YYYY-MM-DD)")
    ap.add_argument("--end-date", required=True, help="End date (YYYY-MM-DD)")
    ap.add_argument(
        "--window-draws",
        type=int,
        default=5,
        help="Draw slots to evaluate per play card (default: 5; Midday/Evening slots).",
    )
    ap.add_argument(
        "--sharepacks-root",
        default="sharepacks/_predictive",
        help="Sharepacks root directory (default: sharepacks/_predictive)",
    )
    ap.add_argument(
        "--profile",
        choices=["mixed", "tool_only", "profit_only"],
        default="tool_only",
        help="Ablation profile (default: tool_only). Determines play_card filename suffix.",
    )
    ap.add_argument(
        "--experiment-tag",
        default="",
        help="Optional experiment tag suffix selecting play_card files (default: none).",
    )
    ap.add_argument("--states", nargs="*", help="Optional subset of state keys to grade.")
    ap.add_argument("--force", action="store_true", help="Overwrite existing outputs (default: refuse).")
    ap.add_argument("--out-csv", default=None, help="Override output CSV path (default: RUNS/play_card_windowed_grade*.csv)")
    ap.add_argument("--out-md", default=None, help="Override output Markdown path (default: RUNS/play_card_windowed_grade*.md)")
    ap.add_argument("--out-rollup-csv", default=None, help="Override rollup CSV path (default: RUNS/play_card_windowed_rollup*.csv)")
    ap.add_argument("--out-rollup-md", default=None, help="Override rollup Markdown path (default: RUNS/play_card_windowed_rollup*.md)")
    args = ap.parse_args()

    try:
        start = _parse_date(args.start_date)
        end = _parse_date(args.end_date)
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc
    if end < start:
        raise SystemExit("--end-date must be >= --start-date")
    window_draws = int(args.window_draws)
    if window_draws <= 0:
        raise SystemExit("--window-draws must be >= 1")

    sharepacks_root = Path(args.sharepacks_root)
    if not sharepacks_root.is_absolute():
        sharepacks_root = (REPO_ROOT / sharepacks_root).resolve()
    if not sharepacks_root.exists():
        raise SystemExit(f"Missing sharepacks root: {_safe_rel(sharepacks_root)}")

    profile = str(args.profile or "mixed").strip()
    out_suffix = "" if profile == "mixed" else f"__{profile}"
    exp_tag = _normalize_experiment_tag(args.experiment_tag)
    tag_suffix = f"__{exp_tag}" if exp_tag else ""

    dates = _iter_dates_between(sharepacks_root, start, end)
    if not dates:
        raise SystemExit(f"No sharepack days found under: {_safe_rel(sharepacks_root)} in range {start}..{end}")

    runs_dir = _runs_dir()
    runs_dir.mkdir(parents=True, exist_ok=True)

    window_prefix = f"{start.isoformat()}_to_{end.isoformat()}__PLAY_CARD_WINDOWED_GRADE{out_suffix}{tag_suffix}__N{window_draws}"
    out_csv = Path(args.out_csv) if args.out_csv else runs_dir / f"{window_prefix}.csv"
    out_md = Path(args.out_md) if args.out_md else runs_dir / f"{window_prefix}.md"
    out_rollup_csv = (
        Path(args.out_rollup_csv)
        if args.out_rollup_csv
        else runs_dir / f"play_card_windowed_rollup{out_suffix}{tag_suffix}__N{window_draws}__{start.isoformat()}_to_{end.isoformat()}.csv"
    )
    out_rollup_md = (
        Path(args.out_rollup_md)
        if args.out_rollup_md
        else runs_dir / f"play_card_windowed_rollup{out_suffix}{tag_suffix}__N{window_draws}__{start.isoformat()}_to_{end.isoformat()}.md"
    )
    if any(p.exists() for p in (out_csv, out_md, out_rollup_csv, out_rollup_md)) and not args.force:
        raise SystemExit("Refusing to overwrite existing outputs (use --force).")

    fieldnames = [
        "start_date",
        "sharepacks_root",
        "profile",
        "experiment_tag",
        "state_key",
        "play_card_path",
        "strategy",
        "budget_label",
        "combos_count",
        "boxed_canonicals_count",
        "vtrac_pack_size",
        "filler_size",
        "window_draws",
        "window_measured",
        "hit_any_strict_window",
        "hit_any_box_window",
        "hit_any_inclusive_window",
        "pack_hit_any_inclusive_window",
        "filler_hit_any_inclusive_window",
        "pack_only_hit_any_inclusive_window",
        "filler_only_hit_any_inclusive_window",
        "pack_and_filler_hit_any_inclusive_window",
        "first_hit_any_strict_draw",
        "first_hit_any_box_draw",
        "first_hit_any_inclusive_draw",
        "first_pack_hit_any_inclusive_draw",
        "first_filler_hit_any_inclusive_draw",
    ]

    rows_out: List[Dict[str, str]] = []
    by_key: Dict[Tuple[str, str], Dict[str, int]] = {}

    for d in dates:
        day_dir = sharepacks_root / d
        state_dirs = _iter_state_dirs(day_dir, states=args.states)
        for state_dir in state_dirs:
            state_key = state_dir.name
            pc_path = state_dir / f"play_card{out_suffix}{tag_suffix}.json"
            if not pc_path.exists():
                continue
            raw = _read_json(pc_path)
            if not isinstance(raw, dict):
                continue
            profile_in_payload = str(raw.get("profile") or profile or "mixed").strip()
            strategies = raw.get("strategies") or {}
            if not isinstance(strategies, dict):
                continue

            slots = _draw_slots_for_state(start_date=d, window_draws=window_draws, state_key=state_key)

            for strat_name, strat_payload in sorted(strategies.items(), key=lambda kv: kv[0]):
                if not isinstance(strat_payload, dict):
                    continue
                for budget_label, card in sorted(strat_payload.items(), key=lambda kv: kv[0]):
                    if not isinstance(card, dict):
                        continue
                    combos = [_normalize_pick3_literal(c) for c in (card.get("combos") or [])]
                    combos = [c for c in combos if c]
                    combos_set = set(combos)
                    canonicals_any_perm = {c for c in (_canon(x) for x in combos_set) if c}
                    boxed = _boxed_canonicals(combos)
                    indices = _pack_vtrac_indices(combos)

                    vtrac_pack = card.get("vtrac_pack") if isinstance(card, dict) else None
                    pack_raw = []
                    if isinstance(vtrac_pack, dict):
                        pack_raw = vtrac_pack.get("pack_combos") or []
                    pack_norm = [_normalize_pick3_literal(c) for c in pack_raw] if isinstance(pack_raw, list) else []
                    pack_norm = [c for c in pack_norm if c]
                    pack_set = set(pack_norm) & combos_set
                    filler_set = combos_set - pack_set
                    pack_canonicals_any_perm = {c for c in (_canon(x) for x in pack_set) if c}
                    pack_indices = _pack_vtrac_indices(list(pack_set))
                    filler_canonicals_any_perm = {c for c in (_canon(x) for x in filler_set) if c}
                    filler_indices = _pack_vtrac_indices(list(filler_set))

                    strict_flags: List[bool] = []
                    box_flags: List[bool] = []
                    inclusive_flags: List[bool] = []
                    pack_inclusive_flags: List[bool] = []
                    filler_inclusive_flags: List[bool] = []
                    measured = 0
                    for _slot_date, _slot_label, winner in slots:
                        w = _normalize_pick3_literal(winner or "")
                        if not w:
                            strict_flags.append(False)
                            box_flags.append(False)
                            inclusive_flags.append(False)
                            pack_inclusive_flags.append(False)
                            filler_inclusive_flags.append(False)
                            continue
                        measured += 1
                        wcanon = _canon(w)
                        wvt = _winner_vtrac_index(w)
                        straight_hit = bool(w in combos_set)
                        box_hit = bool(wcanon and wcanon in boxed)
                        perm_hit = bool(wcanon and wcanon in canonicals_any_perm)
                        vtrac_hit = bool(wvt is not None and wvt in indices)

                        strict_flags.append(bool(straight_hit or box_hit))
                        box_flags.append(bool(straight_hit or perm_hit))
                        inclusive_flags.append(bool(straight_hit or perm_hit or vtrac_hit))

                        pack_straight_hit = bool(w in pack_set)
                        pack_perm_hit = bool(wcanon and wcanon in pack_canonicals_any_perm)
                        pack_vtrac_hit = bool(wvt is not None and wvt in pack_indices)
                        pack_inclusive_flags.append(bool(pack_straight_hit or pack_perm_hit or pack_vtrac_hit))

                        filler_straight_hit = bool(w in filler_set)
                        filler_perm_hit = bool(wcanon and wcanon in filler_canonicals_any_perm)
                        filler_vtrac_hit = bool(wvt is not None and wvt in filler_indices)
                        filler_inclusive_flags.append(bool(filler_straight_hit or filler_perm_hit or filler_vtrac_hit))

                    hit_any_strict = any(strict_flags) and measured > 0
                    hit_any_box = any(box_flags) and measured > 0
                    hit_any_inclusive = any(inclusive_flags) and measured > 0
                    pack_hit_any_inclusive = any(pack_inclusive_flags) and measured > 0
                    filler_hit_any_inclusive = any(filler_inclusive_flags) and measured > 0
                    pack_only_hit_any_inclusive = bool(pack_hit_any_inclusive and not filler_hit_any_inclusive)
                    filler_only_hit_any_inclusive = bool(filler_hit_any_inclusive and not pack_hit_any_inclusive)
                    pack_and_filler_hit_any_inclusive = bool(pack_hit_any_inclusive and filler_hit_any_inclusive)

                    rows_out.append(
                        {
                            "start_date": d,
                            "sharepacks_root": _safe_rel(sharepacks_root),
                            "profile": profile_in_payload,
                            "experiment_tag": exp_tag,
                            "state_key": state_key,
                            "play_card_path": _safe_rel(pc_path),
                            "strategy": strat_name,
                            "budget_label": budget_label,
                            "combos_count": str(len(combos)),
                            "boxed_canonicals_count": str(len(boxed)),
                            "vtrac_pack_size": str(len(pack_set)),
                            "filler_size": str(len(filler_set)),
                            "window_draws": str(window_draws),
                            "window_measured": str(measured),
                            "hit_any_strict_window": "1" if hit_any_strict else "0",
                            "hit_any_box_window": "1" if hit_any_box else "0",
                            "hit_any_inclusive_window": "1" if hit_any_inclusive else "0",
                            "pack_hit_any_inclusive_window": "1" if pack_hit_any_inclusive else "0",
                            "filler_hit_any_inclusive_window": "1" if filler_hit_any_inclusive else "0",
                            "pack_only_hit_any_inclusive_window": "1" if pack_only_hit_any_inclusive else "0",
                            "filler_only_hit_any_inclusive_window": "1" if filler_only_hit_any_inclusive else "0",
                            "pack_and_filler_hit_any_inclusive_window": "1" if pack_and_filler_hit_any_inclusive else "0",
                            "first_hit_any_strict_draw": _first_hit_index(strict_flags),
                            "first_hit_any_box_draw": _first_hit_index(box_flags),
                            "first_hit_any_inclusive_draw": _first_hit_index(inclusive_flags),
                            "first_pack_hit_any_inclusive_draw": _first_hit_index(pack_inclusive_flags),
                            "first_filler_hit_any_inclusive_draw": _first_hit_index(filler_inclusive_flags),
                        }
                    )

                    agg = by_key.setdefault(
                        (strat_name, budget_label),
                        {
                            "rows": 0,
                            "strict": 0,
                            "box": 0,
                            "inc": 0,
                            "pack_inc": 0,
                            "filler_inc": 0,
                            "pack_only_inc": 0,
                            "pack_both_inc": 0,
                        },
                    )
                    if measured > 0:
                        agg["rows"] += 1
                        agg["strict"] += 1 if hit_any_strict else 0
                        agg["box"] += 1 if hit_any_box else 0
                        agg["inc"] += 1 if hit_any_inclusive else 0
                        agg["pack_inc"] += 1 if pack_hit_any_inclusive else 0
                        agg["filler_inc"] += 1 if filler_hit_any_inclusive else 0
                        agg["pack_only_inc"] += 1 if pack_only_hit_any_inclusive else 0
                        agg["pack_both_inc"] += 1 if pack_and_filler_hit_any_inclusive else 0

    rows_out.sort(key=lambda r: (r["start_date"], r["state_key"], r["strategy"], r["budget_label"]))

    with out_csv.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows_out:
            w.writerow(r)

    rollup_rows: List[Dict[str, str]] = []
    for (strategy, budget_label), agg in sorted(by_key.items()):
        d = int(agg["rows"])
        rollup_rows.append(
            {
                "strategy": strategy,
                "budget_label": budget_label,
                "rows_measured": str(d),
                "hit_any_strict_window_rate": f"{(agg['strict'] / d):.4f}" if d else "",
                "hit_any_box_window_rate": f"{(agg['box'] / d):.4f}" if d else "",
                "hit_any_inclusive_window_rate": f"{(agg['inc'] / d):.4f}" if d else "",
                "pack_hit_any_inclusive_window_rate": f"{(agg['pack_inc'] / d):.4f}" if d else "",
                "filler_hit_any_inclusive_window_rate": f"{(agg['filler_inc'] / d):.4f}" if d else "",
                "pack_only_hit_any_inclusive_window_rate": f"{(agg['pack_only_inc'] / d):.4f}" if d else "",
                "pack_and_filler_hit_any_inclusive_window_rate": f"{(agg['pack_both_inc'] / d):.4f}" if d else "",
            }
        )
    rollup_fieldnames = [
        "strategy",
        "budget_label",
        "rows_measured",
        "hit_any_strict_window_rate",
        "hit_any_box_window_rate",
        "hit_any_inclusive_window_rate",
        "pack_hit_any_inclusive_window_rate",
        "filler_hit_any_inclusive_window_rate",
        "pack_only_hit_any_inclusive_window_rate",
        "pack_and_filler_hit_any_inclusive_window_rate",
    ]
    with out_rollup_csv.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=rollup_fieldnames)
        w.writeheader()
        for r in rollup_rows:
            w.writerow(r)

    lines = [
        "# Play Card Windowed Grade",
        "",
        f"- sharepacks_root: `{_safe_rel(sharepacks_root)}`",
        f"- profile: `{profile}`",
        f"- experiment_tag: `{exp_tag or '—'}`",
        f"- date_range: `{dates[0]}` → `{dates[-1]}`",
        f"- window_draws: `{window_draws}` (Midday/Evening slots)",
        f"- rows: `{len(rows_out)}`",
        "",
        "## Rollup (by strategy + budget)",
        "",
        "| strategy | budget | rows | hit_any_strict | hit_any_box | hit_any_inclusive | pack_hit | pack_only | filler_hit |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for r in rollup_rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{r['strategy']}`",
                    str(r["budget_label"]),
                    str(r["rows_measured"]),
                    str(r["hit_any_strict_window_rate"]),
                    str(r["hit_any_box_window_rate"]),
                    str(r["hit_any_inclusive_window_rate"]),
                    str(r["pack_hit_any_inclusive_window_rate"]),
                    str(r["pack_only_hit_any_inclusive_window_rate"]),
                    str(r["filler_hit_any_inclusive_window_rate"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            f"- CSV: `{_safe_rel(out_csv)}`",
            f"- Rollup CSV: `{_safe_rel(out_rollup_csv)}`",
        ]
    )
    out_md.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    out_rollup_md.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

    print(f"Wrote: {_safe_rel(out_csv)}")
    print(f"Wrote: {_safe_rel(out_rollup_csv)}")
    print(f"Wrote: {_safe_rel(out_md)}")


if __name__ == "__main__":
    main()
