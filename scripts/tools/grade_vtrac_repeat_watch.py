#!/usr/bin/env python3
"""
Grade Control Center "VTRAC Repeat Watch" board against posted results.

Scope:
- Reads per-day board rows from:
    sharepacks/<root>/<D>/control_center/vtrac_repeat_watch.csv
- Writes grading outputs ONLY to RUNS:
    docs/AAT9_KIT/FINAL VALIDATION/RUNS/...

Why:
- Repeat Watch is a Brain-2 "pressure / lane" surface (index + streak), not a
  direct candidate caller. Same-day hits can look weak even when the lane is
  visible and converts over a short horizon.
- This harness measures same-day and windowed (N draws) conversion of the
  row's `Current Index` into winner VTRAC indices.
"""

from __future__ import annotations

import argparse
import csv
import sys
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
SRC_ROOT = REPO_ROOT / "src"
if SRC_ROOT.exists() and str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))


def _runs_dir() -> Path:
    return REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"


def _safe_rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _normalize_pick3_literal(value: str) -> str:
    digits = "".join(ch for ch in str(value) if ch.isdigit())
    if not digits:
        return ""
    digits = digits.zfill(3) if len(digits) <= 3 else digits
    return digits if len(digits) == 3 else ""


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


def _date_add_days(d: str, days: int) -> str:
    return (_parse_date(d) + timedelta(days=int(days))).isoformat()


def _window_dates(start_date: str, *, window_draws: int) -> List[str]:
    # One draw-slot per day per period (Midday/Evening).
    return [_date_add_days(start_date, i) for i in range(max(0, int(window_draws)))]


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

    text = results_file.read_text(encoding="utf-8", errors="replace")
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


def _winner_for_period(w: Winner, period: str) -> str:
    if period == "Midday":
        return w.midday or ""
    if period == "Evening":
        return w.evening or ""
    return ""


def _vtrac_index(draw: str) -> Optional[int]:
    from modules.vtrac_reference import get_vtrac_index

    d = _normalize_pick3_literal(draw)
    if not d:
        return None
    idx = get_vtrac_index(d)
    return idx if isinstance(idx, int) else None


def _read_csv_rows(path: Path) -> List[Dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", errors="replace", newline="") as f:
        return [{k: (v or "") for k, v in row.items()} for row in csv.DictReader(f)]


def _write_csv(path: Path, fieldnames: Sequence[str], rows: Sequence[Dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(fieldnames), extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow(r)


def _first_window_hit_offset(
    *,
    current_index: int,
    dates: Sequence[str],
    winners_by_date: Dict[str, Dict[str, Winner]],
    state_key: str,
    period: str,
) -> Optional[int]:
    for offset, d in enumerate(dates):
        w = (winners_by_date.get(d) or {}).get(state_key)
        if not w:
            continue
        ww = _winner_for_period(w, period)
        if not ww:
            continue
        wi = _vtrac_index(ww)
        if wi is None:
            continue
        if wi == current_index:
            return offset
    return None


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Grade vtrac_repeat_watch.csv rows against results (same-day + windowed).")
    ap.add_argument("--start-date", required=True, help="Start date D (YYYY-MM-DD)")
    ap.add_argument("--end-date", required=True, help="End date D (YYYY-MM-DD)")
    ap.add_argument(
        "--sharepacks-root",
        default="sharepacks/_predictive",
        help="Sharepacks root directory (default: sharepacks/_predictive)",
    )
    ap.add_argument(
        "--window-draws",
        type=int,
        default=5,
        help="Window draws (per-period, days forward including D) to evaluate (default: 5).",
    )
    ap.add_argument("--states", nargs="*", help="Optional subset of states to grade.")
    ap.add_argument("--force", action="store_true", help="Overwrite existing outputs (default: refuse).")
    ap.add_argument("--out-csv", default=None, help="Override output CSV path (default: RUNS/...)")
    ap.add_argument("--out-md", default=None, help="Override output Markdown path (default: RUNS/...)")
    ap.add_argument("--out-rollup-csv", default=None, help="Override rollup CSV path (default: RUNS/...)")
    ap.add_argument("--out-rollup-md", default=None, help="Override rollup Markdown path (default: RUNS/...)")
    ap.add_argument(
        "--skip-control-center-audit",
        action="store_true",
        help="Skip cross-check against control_center/vtrac_repeat_watch.csv winner fields (default: audit).",
    )
    return ap.parse_args()


def main() -> None:
    args = parse_args()

    start = _parse_date(args.start_date)
    end = _parse_date(args.end_date)
    if end < start:
        raise SystemExit("--end-date must be >= --start-date")

    sharepacks_root = Path(args.sharepacks_root)
    if not sharepacks_root.is_absolute():
        sharepacks_root = (REPO_ROOT / sharepacks_root).resolve()
    if not sharepacks_root.exists():
        raise SystemExit(f"Missing sharepacks root: {_safe_rel(sharepacks_root)}")

    window_draws = int(args.window_draws)
    if window_draws <= 0:
        raise SystemExit("--window-draws must be >= 1")

    dates = _iter_dates_between(sharepacks_root, start, end)
    if not dates:
        raise SystemExit(f"No sharepack days found under: {_safe_rel(sharepacks_root)} in range {start}..{end}")

    horizon_end = end + timedelta(days=window_draws - 1)
    winners_by_date: Dict[str, Dict[str, Winner]] = {}
    cur = start
    while cur <= horizon_end:
        d = cur.isoformat()
        winners_by_date[d] = _load_results_winners(REPO_ROOT / "data" / "results" / f"{d}.txt")
        cur += timedelta(days=1)

    states_filter = set(args.states or [])

    runs_dir = _runs_dir()
    runs_dir.mkdir(parents=True, exist_ok=True)

    prefix = f"{start.isoformat()}_to_{end.isoformat()}__VTRAC_REPEAT_WATCH_GRADE__N{window_draws}"
    out_csv = Path(args.out_csv) if args.out_csv else runs_dir / f"{prefix}.csv"
    out_md = Path(args.out_md) if args.out_md else runs_dir / f"{prefix}.md"
    out_rollup_csv = (
        Path(args.out_rollup_csv)
        if args.out_rollup_csv
        else runs_dir / f"vtrac_repeat_watch_rollup__N{window_draws}__{start.isoformat()}_to_{end.isoformat()}.csv"
    )
    out_rollup_md = (
        Path(args.out_rollup_md)
        if args.out_rollup_md
        else runs_dir / f"vtrac_repeat_watch_rollup__N{window_draws}__{start.isoformat()}_to_{end.isoformat()}.md"
    )

    if any(p.exists() for p in (out_csv, out_md, out_rollup_csv, out_rollup_md)) and not args.force:
        raise SystemExit("Refusing to overwrite existing outputs (use --force).")

    rows_out: List[Dict[str, object]] = []
    cc_by_date: Dict[str, Dict[Tuple[str, str], Dict[str, str]]] = {}
    if not args.skip_control_center_audit:
        for d in dates:
            cc_csv = sharepacks_root / d / "control_center" / "vtrac_repeat_watch.csv"
            cc_rows = _read_csv_rows(cc_csv)
            cc_map: Dict[Tuple[str, str], Dict[str, str]] = {}
            for r in cc_rows:
                sk = (r.get("StateKey") or "").strip()
                vt = (r.get("Variant") or "").strip()
                if sk and vt:
                    cc_map[(sk, vt)] = r
            cc_by_date[d] = cc_map

    for d in dates:
        day_dir = sharepacks_root / d / "control_center"
        rows = _read_csv_rows(day_dir / "vtrac_repeat_watch.csv")
        if not rows:
            continue
        window_days = _window_dates(d, window_draws=window_draws)

        winners_today = winners_by_date.get(d) or {}
        for r in rows:
            state_key = (r.get("StateKey") or "").strip()
            if not state_key:
                continue
            if states_filter and state_key not in states_filter:
                continue
            variant = (r.get("Variant") or "").strip() or ""
            state_label = (r.get("State") or "").strip() or ""
            try:
                current_index = int((r.get("Current Index") or "").strip())
            except Exception:
                continue
            try:
                current_streak = int((r.get("Current Streak") or "").strip() or "0")
            except Exception:
                current_streak = 0

            w = winners_today.get(state_key)
            w_mid = _winner_for_period(w, "Midday") if w else ""
            w_eve = _winner_for_period(w, "Evening") if w else ""
            w_mid_v = _vtrac_index(w_mid) if w_mid else None
            w_eve_v = _vtrac_index(w_eve) if w_eve else None

            mid_hit = bool(w_mid_v is not None and w_mid_v == current_index)
            eve_hit = bool(w_eve_v is not None and w_eve_v == current_index)

            mid_first = _first_window_hit_offset(
                current_index=current_index,
                dates=window_days,
                winners_by_date=winners_by_date,
                state_key=state_key,
                period="Midday",
            )
            eve_first = _first_window_hit_offset(
                current_index=current_index,
                dates=window_days,
                winners_by_date=winners_by_date,
                state_key=state_key,
                period="Evening",
            )

            mid_measured = sum(
                1
                for dd in window_days
                if (winners_by_date.get(dd) or {}).get(state_key) and _winner_for_period((winners_by_date.get(dd) or {}).get(state_key), "Midday")
            )
            eve_measured = sum(
                1
                for dd in window_days
                if (winners_by_date.get(dd) or {}).get(state_key) and _winner_for_period((winners_by_date.get(dd) or {}).get(state_key), "Evening")
            )

            cc = (cc_by_date.get(d) or {}).get((state_key, variant))
            cc_winner_vtrac_match = None
            cc_eq_match = None
            if cc is not None:
                cc_v = (cc.get("Winner VTRAC") or "").strip()
                cc_eq = (cc.get("Current==WinnerVTRAC") or "").strip()
                cc_has_winner = bool(cc_v and cc_v != "-")
                if cc_has_winner:
                    try:
                        want = w_mid_v if variant == "Midday" else (w_eve_v if variant == "Evening" else None)
                        cc_winner_vtrac_match = bool(want is not None and int(cc_v) == int(want))
                    except Exception:
                        cc_winner_vtrac_match = False
                if cc_has_winner and cc_eq and cc_eq in {"True", "False"}:
                    want_hit = mid_hit if variant == "Midday" else (eve_hit if variant == "Evening" else False)
                    cc_eq_match = bool((cc_eq == "True") == bool(want_hit))

            rows_out.append(
                {
                    "results_date": d,
                    "sharepacks_root": _safe_rel(sharepacks_root),
                    "state_key": state_key,
                    "state_label": state_label,
                    "variant": variant,
                    "current_index": current_index,
                    "current_streak": current_streak,
                    "winner_midday": w_mid or "-",
                    "winner_midday_vtrac": "" if w_mid_v is None else int(w_mid_v),
                    "winner_evening": w_eve or "-",
                    "winner_evening_vtrac": "" if w_eve_v is None else int(w_eve_v),
                    "midday_hit_same_day": 1 if mid_hit else 0,
                    "evening_hit_same_day": 1 if eve_hit else 0,
                    "window_draws": window_draws,
                    "midday_window_measured": mid_measured,
                    "evening_window_measured": eve_measured,
                    "midday_hit_window": 1 if mid_first is not None else 0,
                    "evening_hit_window": 1 if eve_first is not None else 0,
                    "midday_first_hit_offset": "" if mid_first is None else int(mid_first),
                    "evening_first_hit_offset": "" if eve_first is None else int(eve_first),
                    "cc_row_present": 1 if cc is not None else 0,
                    "cc_winner_vtrac_match": "" if cc_winner_vtrac_match is None else (1 if cc_winner_vtrac_match else 0),
                    "cc_current_eq_match": "" if cc_eq_match is None else (1 if cc_eq_match else 0),
                }
            )

    fieldnames = [
        "results_date",
        "sharepacks_root",
        "state_key",
        "state_label",
        "variant",
        "current_index",
        "current_streak",
        "winner_midday",
        "winner_midday_vtrac",
        "winner_evening",
        "winner_evening_vtrac",
        "midday_hit_same_day",
        "evening_hit_same_day",
        "window_draws",
        "midday_window_measured",
        "evening_window_measured",
        "midday_hit_window",
        "evening_hit_window",
        "midday_first_hit_offset",
        "evening_first_hit_offset",
        "cc_row_present",
        "cc_winner_vtrac_match",
        "cc_current_eq_match",
    ]
    _write_csv(out_csv, fieldnames=fieldnames, rows=rows_out)

    # Rollup by (variant, current_streak, period)
    def _truthy(v: object) -> bool:
        return str(v).strip() == "1"

    def _rate(n: int, d: int) -> str:
        return "" if d == 0 else f"{(n / d):.4f}"

    by_key: Dict[Tuple[str, int, str], Dict[str, int]] = {}
    for r in rows_out:
        variant = str(r.get("variant") or "")
        try:
            streak = int(r.get("current_streak") or 0)
        except Exception:
            streak = 0
        for period in ("Midday", "Evening"):
            winner = str(r.get(f"winner_{period.lower()}") or "")
            if not winner or winner == "-":
                continue
            key = (variant, streak, period)
            agg = by_key.setdefault(key, {"rows_measured": 0, "same_day_hits": 0, "window_hits": 0})
            agg["rows_measured"] += 1
            agg["same_day_hits"] += 1 if _truthy(r.get(f"{period.lower()}_hit_same_day", 0)) else 0
            agg["window_hits"] += 1 if _truthy(r.get(f"{period.lower()}_hit_window", 0)) else 0

    roll_rows: List[Dict[str, object]] = []
    for (variant, streak, period), agg in sorted(by_key.items(), key=lambda t: (t[0][0], t[0][1], t[0][2])):
        dcount = agg["rows_measured"]
        roll_rows.append(
            {
                "variant": variant,
                "current_streak": streak,
                "period": period,
                "rows_measured": dcount,
                "same_day_hit_rate": _rate(agg["same_day_hits"], dcount),
                "window_hit_rate": _rate(agg["window_hits"], dcount),
            }
        )

    _write_csv(
        out_rollup_csv,
        fieldnames=["variant", "current_streak", "period", "rows_measured", "same_day_hit_rate", "window_hit_rate"],
        rows=roll_rows,
    )

    # Markdown
    lines: List[str] = []
    lines.append(f"# VTRAC Repeat Watch grade — {start.isoformat()} → {end.isoformat()} (N={window_draws})")
    lines.append("")
    lines.append("Purpose")
    lines.append("- Grade VTRAC repeat-watch (index + streak) vs posted winners (same-day + windowed).")
    lines.append(f"- Sharepacks root: `{_safe_rel(sharepacks_root)}`")
    lines.append(f"- Detailed CSV: `{_safe_rel(out_csv)}`")
    lines.append(f"- Rollup CSV: `{_safe_rel(out_rollup_csv)}`")
    lines.append("")
    lines.append("Notes")
    lines.append("- `same_day` checks whether `Current Index == winner VTRAC` for that period.")
    lines.append("- `window` checks D..D+(N-1) for that period (days forward including D).")
    lines.append("")
    lines.append("## Rollup (rates)")
    lines.append("")
    lines.append("| Variant | Streak | Period | Rows | same_day_hit | window_hit |")
    lines.append("|---|---:|---|---:|---:|---:|")
    for r in roll_rows:
        lines.append(
            "| {variant} | {current_streak} | {period} | {rows_measured} | {same_day_hit_rate} | {window_hit_rate} |".format(**r)
        )
    lines.append("")

    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    out_rollup_md.parent.mkdir(parents=True, exist_ok=True)
    out_rollup_md.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

    print(f"Wrote: {_safe_rel(out_csv)}")
    print(f"Wrote: {_safe_rel(out_rollup_csv)}")
    print(f"Wrote: {_safe_rel(out_md)}")
    print(f"Wrote: {_safe_rel(out_rollup_md)}")


if __name__ == "__main__":
    main()
