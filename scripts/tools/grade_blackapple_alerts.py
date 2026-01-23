#!/usr/bin/env python3
"""
Grade Blackapple (BA) signals against posted results.

Scope:
- Reads BA outputs from sharepack-local Aux summaries:
    sharepacks/<root>/<D>/<STATE>/aux/<STATE>/summary.json
- Optionally cross-checks Control Center board rows:
    sharepacks/<root>/<D>/control_center/blackapple_alerts.csv
- Writes grading outputs ONLY to RUNS:
    docs/AAT9_KIT/FINAL VALIDATION/RUNS/...

Why:
- Blackapple is a Brain-2 tracker-like signal (status OFF/WATCH/ALERT) that emits
  a small candidate list (default cap 12) when triggers overlap.
- We need a repeatable measurement harness (same-day + windowed) so "ALERT" is
  either proven useful or explicitly research-only.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
SRC_ROOT = REPO_ROOT / "src"
if SRC_ROOT.exists() and str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))


VARIANT_SPECS: List[Tuple[str, str]] = [
    ("Combined", "combined"),
    ("Midday", "midday"),
    ("Evening", "evening"),
]


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


def _canon(value: str) -> str:
    v = _normalize_pick3_literal(value)
    return "".join(sorted(v)) if v else ""


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


def _render_ba_triggers(triggers: Dict[str, Any]) -> str:
    if not triggers:
        return "-"
    parts: List[str] = []
    if triggers.get("mirror"):
        parts.append("Mirror")
    roots = triggers.get("root_due") or []
    if roots:
        parts.append("Root " + "/".join(str(r) for r in roots))
    pattern = triggers.get("pattern") or {}
    if isinstance(pattern, dict) and pattern.get("extreme_due"):
        parts.append("SSS/TTT")
    if isinstance(pattern, dict) and pattern.get("mixed_due"):
        parts.append("SST/STS/TSS")
    floats = triggers.get("floating") or []
    if floats:
        parts.append("Float " + "".join(str(d) for d in floats))
    pairs = triggers.get("pairs") or {}
    if isinstance(pairs, dict):
        remaining = pairs.get("remaining_count")
        if isinstance(remaining, int):
            parts.append(f"Pairs {remaining}")
    return ", ".join(parts) if parts else "-"


def _load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8", errors="replace"))


def _load_csv_rows(path: Path) -> List[Dict[str, str]]:
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


def _summarize_hit_labels(*, candidate: str, winner: str) -> List[str]:
    from modules.vtrac_reference import get_vtrac_index

    c = _normalize_pick3_literal(candidate)
    w = _normalize_pick3_literal(winner)
    if not c or not w:
        return []
    labels: List[str] = []
    if c == w:
        labels.append("Straight")
    if _canon(c) == _canon(w) and c != w:
        labels.append("Boxed")
    ci = get_vtrac_index(c)
    wi = get_vtrac_index(w)
    if isinstance(ci, int) and isinstance(wi, int) and ci == wi:
        labels.append("VTRAC")
    return labels


def _hit_flags_for_candidates(*, candidates: Sequence[str], winner: str) -> Tuple[bool, bool, bool, str]:
    straight = False
    boxed = False
    vtrac = False
    label_set: set[str] = set()
    for c in candidates:
        labels = _summarize_hit_labels(candidate=c, winner=winner)
        if not labels:
            continue
        label_set.update(labels)
        straight = straight or ("Straight" in labels)
        boxed = boxed or ("Boxed" in labels) or ("Straight" in labels)
        vtrac = vtrac or ("VTRAC" in labels)
    label = ", ".join(sorted(label_set)) if label_set else "-"
    return straight, boxed, vtrac, label


def _window_dates(start_date: str, *, window_draws: int) -> List[str]:
    # For Midday-only and Evening-only variants, one draw-slot per day.
    # We treat window_draws as "days forward including D" for that period.
    return [_date_add_days(start_date, i) for i in range(max(0, int(window_draws)))]


def _first_window_hit_offset(
    *,
    candidates: Sequence[str],
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
        _, boxed, vtrac, _ = _hit_flags_for_candidates(candidates=candidates, winner=ww)
        if boxed or vtrac:
            return offset
    return None


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Grade Blackapple alerts from sharepacks against results.")
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
        help="Window draws (per-period, days forward including D) to evaluate per BA list (default: 5).",
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
        help="Skip cross-check against control_center/blackapple_alerts.csv (default: audit).",
    )
    return ap.parse_args()


def main() -> None:
    args = parse_args()

    try:
        start = _parse_date(args.start_date)
        end = _parse_date(args.end_date)
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc
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

    # Preload winners for the whole evaluation horizon.
    # We may need up to end_date + (window_draws-1) days for windowed checks.
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

    prefix = f"{start.isoformat()}_to_{end.isoformat()}__BLACKAPPLE_GRADE__N{window_draws}"
    out_csv = Path(args.out_csv) if args.out_csv else runs_dir / f"{prefix}.csv"
    out_md = Path(args.out_md) if args.out_md else runs_dir / f"{prefix}.md"
    out_rollup_csv = Path(args.out_rollup_csv) if args.out_rollup_csv else runs_dir / f"blackapple_rollup__N{window_draws}__{start.isoformat()}_to_{end.isoformat()}.csv"
    out_rollup_md = Path(args.out_rollup_md) if args.out_rollup_md else runs_dir / f"blackapple_rollup__N{window_draws}__{start.isoformat()}_to_{end.isoformat()}.md"

    if any(p.exists() for p in (out_csv, out_md, out_rollup_csv, out_rollup_md)) and not args.force:
        raise SystemExit("Refusing to overwrite existing outputs (use --force).")

    rows_out: List[Dict[str, object]] = []

    # (state_key, VariantTitle) -> control_center row (for audit)
    cc_by_date: Dict[str, Dict[Tuple[str, str], Dict[str, str]]] = {}
    if not args.skip_control_center_audit:
        for d in dates:
            cc_csv = sharepacks_root / d / "control_center" / "blackapple_alerts.csv"
            cc_rows = _load_csv_rows(cc_csv)
            cc_map: Dict[Tuple[str, str], Dict[str, str]] = {}
            for r in cc_rows:
                sk = (r.get("StateKey") or "").strip()
                vt = (r.get("Variant") or "").strip()
                if sk and vt:
                    cc_map[(sk, vt)] = r
            cc_by_date[d] = cc_map

    for d in dates:
        day_dir = sharepacks_root / d
        meta_path = day_dir / "control_center" / "meta.json"
        meta = _load_json(meta_path) if meta_path.exists() else {}
        states_meta = meta.get("states") if isinstance(meta, dict) else None
        state_entries = states_meta if isinstance(states_meta, list) else []

        for entry in state_entries:
            if not isinstance(entry, dict):
                continue
            state_key = str(entry.get("state_key") or "").strip()
            aux_state_label = str(entry.get("aux_state_label") or "").strip() or state_key
            aux_summary = str(entry.get("aux_summary") or "").strip()
            if not state_key or not aux_summary:
                continue
            if states_filter and state_key not in states_filter:
                continue

            aux_summary_path = (REPO_ROOT / aux_summary).resolve()
            if not aux_summary_path.exists():
                continue

            payload = _load_json(aux_summary_path)
            if not isinstance(payload, dict):
                continue
            ba = payload.get("blackapple") or {}
            by_variant = ba.get("by_variant") if isinstance(ba, dict) else None
            if not isinstance(by_variant, dict):
                continue

            winners_today = winners_by_date.get(d) or {}
            w = winners_today.get(state_key)
            if not w:
                w = Winner(midday=None, evening=None)

            for variant_title, variant_key in VARIANT_SPECS:
                analysis = by_variant.get(variant_key) or {}
                if not isinstance(analysis, dict):
                    continue
                score = int(analysis.get("score") or 0)
                triggers = analysis.get("triggers") or {}
                candidates_raw = analysis.get("candidates") or []
                candidates: List[str] = []
                for c in candidates_raw:
                    if not isinstance(c, dict):
                        continue
                    combo = _normalize_pick3_literal(c.get("combo") or "")
                    if combo:
                        candidates.append(combo)

                # same-day winners
                w_mid = _winner_for_period(w, "Midday")
                w_eve = _winner_for_period(w, "Evening")
                mid_straight, mid_boxed, mid_vtrac, mid_label = _hit_flags_for_candidates(
                    candidates=candidates, winner=w_mid
                )
                eve_straight, eve_boxed, eve_vtrac, eve_label = _hit_flags_for_candidates(
                    candidates=candidates, winner=w_eve
                )

                # windowed (per-period, days forward including D)
                window_days = _window_dates(d, window_draws=window_draws)
                mid_measured = 0
                eve_measured = 0
                for wd in window_days:
                    ww = (winners_by_date.get(wd) or {}).get(state_key)
                    if ww and _winner_for_period(ww, "Midday"):
                        mid_measured += 1
                    if ww and _winner_for_period(ww, "Evening"):
                        eve_measured += 1
                mid_first = _first_window_hit_offset(
                    candidates=candidates,
                    dates=window_days,
                    winners_by_date=winners_by_date,
                    state_key=state_key,
                    period="Midday",
                )
                eve_first = _first_window_hit_offset(
                    candidates=candidates,
                    dates=window_days,
                    winners_by_date=winners_by_date,
                    state_key=state_key,
                    period="Evening",
                )
                mid_hit_window = mid_first is not None
                eve_hit_window = eve_first is not None

                # audit vs control_center CSV row (if present)
                cc = (cc_by_date.get(d) or {}).get((state_key, variant_title))
                cc_score_match = None
                cc_candidates_match = None
                cc_examples_match = None
                if cc is not None:
                    try:
                        cc_score = int((cc.get("BA-Score") or "0").strip() or "0")
                        cc_score_match = bool(cc_score == score)
                    except Exception:
                        cc_score_match = False
                    try:
                        cc_n = int((cc.get("#Candidates") or "0").strip() or "0")
                        cc_candidates_match = bool(cc_n == len(candidates))
                    except Exception:
                        cc_candidates_match = False
                    cc_examples = (cc.get("Examples") or "").strip()
                    our_examples = " ".join(candidates[:3]).strip() or "-"
                    cc_examples_match = bool(cc_examples == our_examples)

                rows_out.append(
                    {
                        "results_date": d,
                        "sharepacks_root": _safe_rel(sharepacks_root),
                        "state_key": state_key,
                        "state_label": aux_state_label,
                        "variant": variant_title,
                        "ba_score": score,
                        "ba_status": str(analysis.get("status") or "").strip() or "",  # may be absent
                        "ba_status_label": "ALERT" if score >= 3 else ("WATCH" if score == 2 else "OFF"),
                        "triggers": _render_ba_triggers(triggers if isinstance(triggers, dict) else {}),
                        "candidates_count": len(candidates),
                        "candidates": " ".join(candidates),
                        "examples": " ".join(candidates[:3]).strip() or "-",
                        "winner_midday": w_mid or "-",
                        "winner_evening": w_eve or "-",
                        "midday_winner_missing": 1 if not w_mid else 0,
                        "evening_winner_missing": 1 if not w_eve else 0,
                        "midday_straight_hit": 1 if mid_straight else 0,
                        "midday_boxed_hit": 1 if mid_boxed else 0,
                        "midday_vtrac_hit": 1 if mid_vtrac else 0,
                        "midday_hit_any_inclusive": 1 if (mid_boxed or mid_vtrac) else 0,
                        "midday_hits_label": mid_label,
                        "evening_straight_hit": 1 if eve_straight else 0,
                        "evening_boxed_hit": 1 if eve_boxed else 0,
                        "evening_vtrac_hit": 1 if eve_vtrac else 0,
                        "evening_hit_any_inclusive": 1 if (eve_boxed or eve_vtrac) else 0,
                        "evening_hits_label": eve_label,
                        "window_draws": window_draws,
                        "midday_window_measured": mid_measured,
                        "evening_window_measured": eve_measured,
                        "midday_hit_any_inclusive_window": 1 if mid_hit_window else 0,
                        "evening_hit_any_inclusive_window": 1 if eve_hit_window else 0,
                        "midday_first_hit_offset": "" if mid_first is None else int(mid_first),
                        "evening_first_hit_offset": "" if eve_first is None else int(eve_first),
                        "cc_row_present": 1 if cc is not None else 0,
                        "cc_score_match": "" if cc_score_match is None else (1 if cc_score_match else 0),
                        "cc_candidates_match": "" if cc_candidates_match is None else (1 if cc_candidates_match else 0),
                        "cc_examples_match": "" if cc_examples_match is None else (1 if cc_examples_match else 0),
                    }
                )

    fieldnames = [
        "results_date",
        "sharepacks_root",
        "state_key",
        "state_label",
        "variant",
        "ba_score",
        "ba_status",
        "ba_status_label",
        "triggers",
        "candidates_count",
        "candidates",
        "examples",
        "winner_midday",
        "winner_evening",
        "midday_winner_missing",
        "evening_winner_missing",
        "midday_straight_hit",
        "midday_boxed_hit",
        "midday_vtrac_hit",
        "midday_hit_any_inclusive",
        "midday_hits_label",
        "evening_straight_hit",
        "evening_boxed_hit",
        "evening_vtrac_hit",
        "evening_hit_any_inclusive",
        "evening_hits_label",
        "window_draws",
        "midday_window_measured",
        "evening_window_measured",
        "midday_hit_any_inclusive_window",
        "evening_hit_any_inclusive_window",
        "midday_first_hit_offset",
        "evening_first_hit_offset",
        "cc_row_present",
        "cc_score_match",
        "cc_candidates_match",
        "cc_examples_match",
    ]
    _write_csv(out_csv, fieldnames=fieldnames, rows=rows_out)

    # Rollup (by status label + period)
    def _truthy(v: object) -> bool:
        return str(v).strip() == "1"

    def _rate(n: int, d: int) -> str:
        return "" if d == 0 else f"{(n / d):.4f}"

    roll_rows: List[Dict[str, object]] = []
    by_key: Dict[Tuple[str, str, str], Dict[str, int]] = {}
    # key = (variant, status, period)
    for r in rows_out:
        variant = str(r.get("variant") or "")
        status = str(r.get("ba_status_label") or "")
        for period in ("Midday", "Evening"):
            wmiss = _truthy(r.get(f"{period.lower()}_winner_missing", 0))
            if wmiss:
                continue
            key = (variant, status, period)
            agg = by_key.setdefault(
                key,
                {
                    "rows_measured": 0,
                    "hit_any_inclusive": 0,
                    "straight_hit": 0,
                    "boxed_hit": 0,
                    "vtrac_hit": 0,
                    "hit_any_inclusive_window": 0,
                },
            )
            agg["rows_measured"] += 1
            agg["hit_any_inclusive"] += 1 if _truthy(r.get(f"{period.lower()}_hit_any_inclusive", 0)) else 0
            agg["straight_hit"] += 1 if _truthy(r.get(f"{period.lower()}_straight_hit", 0)) else 0
            agg["boxed_hit"] += 1 if _truthy(r.get(f"{period.lower()}_boxed_hit", 0)) else 0
            agg["vtrac_hit"] += 1 if _truthy(r.get(f"{period.lower()}_vtrac_hit", 0)) else 0
            agg["hit_any_inclusive_window"] += 1 if _truthy(r.get(f"{period.lower()}_hit_any_inclusive_window", 0)) else 0

    for (variant, status, period), agg in sorted(by_key.items(), key=lambda t: (t[0][0], t[0][1], t[0][2])):
        dcount = agg["rows_measured"]
        roll_rows.append(
            {
                "variant": variant,
                "ba_status": status,
                "period": period,
                "rows_measured": dcount,
                "hit_any_inclusive_rate": _rate(agg["hit_any_inclusive"], dcount),
                "boxed_hit_rate": _rate(agg["boxed_hit"], dcount),
                "straight_hit_rate": _rate(agg["straight_hit"], dcount),
                "vtrac_hit_rate": _rate(agg["vtrac_hit"], dcount),
                "hit_any_inclusive_window_rate": _rate(agg["hit_any_inclusive_window"], dcount),
            }
        )

    _write_csv(
        out_rollup_csv,
        fieldnames=[
            "variant",
            "ba_status",
            "period",
            "rows_measured",
            "hit_any_inclusive_rate",
            "boxed_hit_rate",
            "straight_hit_rate",
            "vtrac_hit_rate",
            "hit_any_inclusive_window_rate",
        ],
        rows=roll_rows,
    )

    # Markdown
    lines: List[str] = []
    lines.append(f"# Blackapple grade — {start.isoformat()} → {end.isoformat()} (N={window_draws})")
    lines.append("")
    lines.append("Purpose")
    lines.append("- Grade Blackapple (Aux) candidates vs posted winners (same-day + windowed).")
    lines.append(f"- Sharepacks root: `{_safe_rel(sharepacks_root)}`")
    lines.append(f"- Detailed CSV: `{_safe_rel(out_csv)}`")
    lines.append(f"- Rollup CSV: `{_safe_rel(out_rollup_csv)}`")
    lines.append("")
    lines.append("Notes")
    lines.append("- `#Candidates` is the full BA candidate list size (cap is typically 12).")
    lines.append("- `Examples` is only the first 3 candidates (Control Center table readability).")
    lines.append("- `hit_any_inclusive` counts `boxed` (includes straight) OR `vtrac` lane hit.")
    lines.append("")
    lines.append("## Rollup (rates)")
    lines.append("")
    lines.append("| Variant | Status | Period | Rows | hit_any_inclusive | hit_any_inclusive_window | boxed | straight | vtrac |")
    lines.append("|---|---|---|---:|---:|---:|---:|---:|---:|")
    for r in roll_rows:
        lines.append(
            "| {variant} | {ba_status} | {period} | {rows_measured} | {hit_any_inclusive_rate} | {hit_any_inclusive_window_rate} | {boxed_hit_rate} | {straight_hit_rate} | {vtrac_hit_rate} |".format(
                **r
            )
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

