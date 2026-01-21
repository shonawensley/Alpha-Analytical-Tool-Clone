#!/usr/bin/env python3
"""
Aux Badge Pressure Harness (Index Pressure Contract)

Purpose:
- Convert the per-combo Aux "boxed VTRAC badge matrix" signal into a compact, gradeable
  per-index pressure surface (state × variant × vtrac_index).
- Evaluate whether "pressure-ranked indices" outperform "overdue-ranked indices" at
  locating the winning vtrac_index across windows (without touching analyzers).

This is an evaluation / reporting tool only:
- Reads sharepack-local Aux draw snapshots (pre-results evidence snapshot)
- Reads posted results (labels) from data/results/<D>.txt
- Writes outputs only to RUNS.

Outputs:
- AUX_BADGE_PRESSURE__HARNESS__<A>_to_<B>.{md,csv} (event-level evaluation)
- AUX_BADGE_PRESSURE__INDEX_STATS__<A>_to_<B>.csv (per-index contract rows)
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from contextlib import redirect_stdout
from dataclasses import dataclass
from datetime import date as date_mod
from datetime import datetime, timedelta, timezone
from io import StringIO
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
SRC_ROOT = REPO_ROOT / "src"
if SRC_ROOT.exists() and str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))


from modules.analyze_pairs import get_vtrac_statuses  # noqa: E402
from modules.vtrac_reference import VTRAC_DISPLAY, get_vtrac_index  # noqa: E402


VARIANTS: Tuple[str, ...] = ("midday", "evening", "combined")


def _runs_dir() -> Path:
    return REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _safe_rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _read_json(path: Path) -> object:
    return json.loads(_read_text(path))


def _normalize_pick3(value: str) -> str:
    digits = "".join(ch for ch in str(value) if ch.isdigit())
    if not digits:
        return ""
    digits = digits.zfill(3) if len(digits) <= 3 else digits
    return digits if len(digits) == 3 else ""


def _canon(draw: str) -> str:
    d = _normalize_pick3(draw)
    return "".join(sorted(d)) if d else ""


def _winner_type(draw: str) -> str:
    d = _normalize_pick3(draw)
    if not d:
        return ""
    a, b, c = d[0], d[1], d[2]
    if a == b == c:
        return "triple"
    if a == b or b == c or a == c:
        return "double"
    mirror_pairs = {("0", "5"), ("1", "6"), ("2", "7"), ("3", "8"), ("4", "9")}
    digits = {a, b, c}
    for x, y in mirror_pairs:
        if x in digits and y in digits:
            return "mirror_double"
    return "single"


@dataclass(frozen=True)
class Winners:
    midday: str
    evening: str


def _load_results_winners(results_file: Path) -> Dict[str, Winners]:
    if not results_file.exists():
        return {}
    from alpha_analytical.control_center.batch_runner import (  # type: ignore
        parse_winner_sheet,
        _PROJECT_STATE_CANDIDATES,
    )

    text = _read_text(results_file)
    entries = parse_winner_sheet(text)

    winners: Dict[str, Winners] = {}
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
            winners[state_key] = Winners(
                midday=_normalize_pick3(midday or ""),
                evening=_normalize_pick3(evening or ""),
            )
    return winners


def _list_dates(start_date: str, end_date: str) -> List[str]:
    a = date_mod.fromisoformat(start_date)
    b = date_mod.fromisoformat(end_date)
    if b < a:
        raise SystemExit(f"--end-date must be >= --start-date (got {start_date}..{end_date})")
    out: List[str] = []
    cur = a
    while cur <= b:
        out.append(cur.isoformat())
        cur += timedelta(days=1)
    return out


def _load_states_from_meta(day_dir: Path) -> List[str]:
    meta = day_dir / "control_center" / "meta.json"
    if not meta.exists():
        return []
    try:
        payload = _read_json(meta)
    except Exception:
        return []
    if not isinstance(payload, dict):
        return []
    states = payload.get("states")
    if not isinstance(states, list):
        return []
    out: List[str] = []
    for s in states:
        if isinstance(s, dict):
            key = str(s.get("state_key") or "").strip()
            if key:
                out.append(key)
    return out


def _find_draws_file(aux_draws_dir: Path, *, variant: str) -> Optional[Path]:
    if not aux_draws_dir.exists():
        return None
    want = variant.strip().lower()
    files = [p for p in aux_draws_dir.glob("*_draws.csv") if p.is_file()]
    if not files:
        return None
    if want == "combined":
        for p in files:
            name = p.name.lower()
            if "_midday_" in name or "_evening_" in name:
                continue
            return p
        return sorted(files)[0]
    if want == "midday":
        for p in files:
            if "_midday_" in p.name.lower():
                return p
        return None
    if want == "evening":
        for p in files:
            if "_evening_" in p.name.lower():
                return p
        return None
    return None


def _read_draws_csv(path: Path, *, max_n: int = 1000) -> List[str]:
    if not path.exists():
        return []
    out: List[str] = []
    with path.open("r", encoding="utf-8", errors="replace", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            draw = _normalize_pick3((row or {}).get("Draw", ""))
            if draw:
                out.append(draw)
            if len(out) >= max_n:
                break
    return out


def _index_draws_since(draws: Sequence[str]) -> Dict[int, int]:
    """Compute draws-since for each vtrac_index (1..35) using newest-first draws list."""
    first_seen: Dict[int, int] = {}
    total = len(draws)
    for i, d in enumerate(draws):
        if not d or len(d) != 3:
            continue
        if len(set(d)) == 1:
            continue  # skip triples
        idx = get_vtrac_index(d)
        if idx is None:
            continue
        if idx not in first_seen:
            first_seen[idx] = i
    return {idx: first_seen.get(idx, total) for idx in range(1, 36)}


def _shape_label(status: dict) -> str:
    if status.get("shape_red_circle"):
        return "RC"
    if status.get("shape_blue_square"):
        return "BS"
    return ""


def _color_weight(color: str) -> int:
    c = (color or "").strip().lower()
    if c == "red":
        return 3
    if c == "blue":
        return 2
    if c == "purple":
        return 1
    return 0


def _shape_weight(shape: str) -> int:
    s = (shape or "").strip().upper()
    if s == "RC":
        return 2
    if s == "BS":
        return 1
    return 0


def _vtrac_entries() -> List[dict]:
    out: List[dict] = []
    for entry in VTRAC_DISPLAY:
        try:
            idx = int(entry.get("Index"))
        except Exception:
            continue
        singles = str(entry.get("Singles") or "").strip()
        doubles = str(entry.get("Doubles") or "").strip()
        out.append(
            {
                "index": idx,
                "singles": [c for c in singles.split() if _normalize_pick3(c)],
                "doubles": [c for c in doubles.split() if _normalize_pick3(c)],
            }
        )
    return out


def _write_csv(path: Path, rows: Sequence[Dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    keys: List[str] = []
    for r in rows:
        for k in r.keys():
            if k not in keys:
                keys.append(k)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for r in rows:
            writer.writerow({k: r.get(k, "") for k in keys})


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Aux badge pressure harness (index pressure contract).")
    p.add_argument("--start-date", required=True, help="Start results date D (YYYY-MM-DD).")
    p.add_argument("--end-date", required=True, help="End results date D (YYYY-MM-DD).")
    p.add_argument("--sharepacks-root", default="sharepacks", help="Sharepacks root (post-results day dirs).")
    p.add_argument("--results-dir", default="data/results", help="Results dir (labels).")
    p.add_argument("--out-dir", default=str(_runs_dir()), help="RUNS output dir.")
    p.add_argument("--k", type=int, default=5, help="Top-K indices for hit-rate evaluation.")
    p.add_argument(
        "--rank-by",
        choices=("pressure_density", "pressure_raw"),
        default="pressure_density",
        help="Primary pressure ranking key.",
    )
    p.add_argument("--force", action="store_true", help="Overwrite outputs.")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    dates = _list_dates(args.start_date, args.end_date)
    sharepacks_root = (REPO_ROOT / args.sharepacks_root).resolve()
    results_dir = (REPO_ROOT / args.results_dir).resolve()
    out_dir = Path(args.out_dir).resolve()

    out_event_csv = out_dir / f"AUX_BADGE_PRESSURE__HARNESS__{args.start_date}_to_{args.end_date}.csv"
    out_md = out_dir / f"AUX_BADGE_PRESSURE__HARNESS__{args.start_date}_to_{args.end_date}.md"
    out_index_csv = out_dir / f"AUX_BADGE_PRESSURE__INDEX_STATS__{args.start_date}_to_{args.end_date}.csv"
    if (out_event_csv.exists() or out_md.exists() or out_index_csv.exists()) and not args.force:
        raise SystemExit(f"Outputs exist; pass --force to overwrite: {_safe_rel(out_md)}")

    entries = _vtrac_entries()
    index_rows: List[Dict[str, object]] = []
    event_rows: List[Dict[str, object]] = []

    # Summary counters (only events with a defined vtrac_index are evaluable).
    totals = {
        "midday_events": 0,
        "evening_events": 0,
        "midday_evaluable": 0,
        "evening_evaluable": 0,
        "midday_overlay_hit": 0,
        "evening_overlay_hit": 0,
        "midday_pressure_hit": 0,
        "evening_pressure_hit": 0,
        "midday_xvar_intersection_hit": 0,
        "evening_xvar_intersection_hit": 0,
    }

    for d in dates:
        day_dir = sharepacks_root / d
        if not day_dir.exists():
            continue

        states = _load_states_from_meta(day_dir)
        if not states:
            states = [p.name for p in sorted(day_dir.iterdir()) if p.is_dir() and p.name != "control_center"]
        if not states:
            continue

        winners_by_state = _load_results_winners(results_dir / f"{d}.txt")

        # Build per-state, per-variant index pressure rows.
        per_state_variant: Dict[Tuple[str, str], Dict[int, Dict[str, object]]] = {}
        for state_key in states:
            aux_draws_dir = day_dir / state_key / "aux" / "draws"
            if not aux_draws_dir.exists():
                continue
            for variant in VARIANTS:
                draw_path = _find_draws_file(aux_draws_dir, variant=variant)
                if not draw_path:
                    continue
                draws = _read_draws_csv(draw_path, max_n=1000)
                if not draws:
                    continue

                with redirect_stdout(StringIO()):
                    vstat = get_vtrac_statuses(draws[:100], draws[:1000])
                idx_ds = _index_draws_since(draws[:1000])

                key = (state_key, variant)
                per_index: Dict[int, Dict[str, object]] = {}
                for entry in entries:
                    idx = int(entry["index"])
                    payload = vstat.get(idx, {}) if isinstance(vstat, dict) else {}
                    singles_status = payload.get("singles_status", {}) if isinstance(payload, dict) else {}
                    doubles_status = payload.get("doubles_status", {}) if isinstance(payload, dict) else {}

                    red = blue = purple = 0
                    rc = bs = 0
                    canon_count = 0
                    raw_score = 0

                    for combo in entry["singles"]:
                        canon_count += 1
                        st = singles_status.get(combo, {}) if isinstance(singles_status, dict) else {}
                        color = str(st.get("color") or "")
                        shape = _shape_label(st) if isinstance(st, dict) else ""
                        if color.strip().lower() == "red":
                            red += 1
                        elif color.strip().lower() == "blue":
                            blue += 1
                        elif color.strip().lower() == "purple":
                            purple += 1
                        if shape == "RC":
                            rc += 1
                        elif shape == "BS":
                            bs += 1
                        raw_score += _color_weight(color) + _shape_weight(shape)

                    for combo in entry["doubles"]:
                        canon_count += 1
                        st = doubles_status.get(combo, {}) if isinstance(doubles_status, dict) else {}
                        color = str(st.get("color") or "")
                        shape = _shape_label(st) if isinstance(st, dict) else ""
                        if color.strip().lower() == "red":
                            red += 1
                        elif color.strip().lower() == "blue":
                            blue += 1
                        elif color.strip().lower() == "purple":
                            purple += 1
                        if shape == "RC":
                            rc += 1
                        elif shape == "BS":
                            bs += 1
                        raw_score += _color_weight(color) + _shape_weight(shape)

                    density = (raw_score / canon_count) if canon_count else 0.0
                    per_index[idx] = {
                        "date": d,
                        "sharepacks_root": _safe_rel(sharepacks_root),
                        "state_key": state_key,
                        "variant": variant,
                        "vtrac_index": idx,
                        "index_ds_1000": idx_ds.get(idx, len(draws)),
                        "canon_count": canon_count,
                        "red_count": red,
                        "blue_count": blue,
                        "purple_count": purple,
                        "rc_count": rc,
                        "bs_count": bs,
                        "pressure_raw": raw_score,
                        "pressure_density": round(density, 6),
                    }
                    index_rows.append(dict(per_index[idx]))
                per_state_variant[key] = per_index

        # Event evaluation (state×period).
        k = max(1, int(args.k))
        for state_key in states:
            w = winners_by_state.get(state_key)
            if not w:
                continue

            def _topk_indices(state_key: str, variant: str) -> Tuple[List[int], List[int]]:
                per_idx = per_state_variant.get((state_key, variant)) or {}
                if not per_idx:
                    return [], []
                by_overdue = sorted(per_idx.values(), key=lambda r: int(r.get("index_ds_1000", 0) or 0), reverse=True)
                overlay_top = [int(r["vtrac_index"]) for r in by_overdue[:k]]
                if args.rank_by == "pressure_raw":
                    by_pressure = sorted(
                        per_idx.values(),
                        key=lambda r: (int(r.get("pressure_raw", 0) or 0), int(r.get("index_ds_1000", 0) or 0)),
                        reverse=True,
                    )
                else:
                    by_pressure = sorted(
                        per_idx.values(),
                        key=lambda r: (float(r.get("pressure_density", 0.0) or 0.0), int(r.get("index_ds_1000", 0) or 0)),
                        reverse=True,
                    )
                pressure_top = [int(r["vtrac_index"]) for r in by_pressure[:k]]
                return overlay_top, pressure_top

            # Cross-variant convergence: intersection of topK pressure indices (M ∩ E).
            overlay_mid, pressure_mid = _topk_indices(state_key, "midday")
            overlay_eve, pressure_eve = _topk_indices(state_key, "evening")
            xvar_pressure = sorted(set(pressure_mid).intersection(pressure_eve))

            # Midday outcome
            if w.midday:
                totals["midday_events"] += 1
                win_idx = get_vtrac_index(w.midday)
                win_type = _winner_type(w.midday)
                evaluable = isinstance(win_idx, int)
                if evaluable:
                    totals["midday_evaluable"] += 1
                overlay_hit = bool(evaluable and win_idx in overlay_mid)
                pressure_hit = bool(evaluable and win_idx in pressure_mid)
                xvar_hit = bool(evaluable and win_idx in xvar_pressure)
                if overlay_hit:
                    totals["midday_overlay_hit"] += 1
                if pressure_hit:
                    totals["midday_pressure_hit"] += 1
                if xvar_hit:
                    totals["midday_xvar_intersection_hit"] += 1
                event_rows.append(
                    {
                        "date": d,
                        "state_key": state_key,
                        "period": "Midday",
                        "winner": w.midday,
                        "winner_type": win_type,
                        "winner_vtrac_index": win_idx if evaluable else "",
                        "k": k,
                        "overlay_topk": ",".join(map(str, overlay_mid)),
                        "pressure_topk": ",".join(map(str, pressure_mid)),
                        "xvar_pressure_intersection": ",".join(map(str, xvar_pressure)),
                        "hit_overlay_topk": overlay_hit,
                        "hit_pressure_topk": pressure_hit,
                        "hit_xvar_pressure_intersection": xvar_hit,
                    }
                )

            # Evening outcome
            if w.evening:
                totals["evening_events"] += 1
                win_idx = get_vtrac_index(w.evening)
                win_type = _winner_type(w.evening)
                evaluable = isinstance(win_idx, int)
                if evaluable:
                    totals["evening_evaluable"] += 1
                overlay_hit = bool(evaluable and win_idx in overlay_eve)
                pressure_hit = bool(evaluable and win_idx in pressure_eve)
                xvar_hit = bool(evaluable and win_idx in xvar_pressure)
                if overlay_hit:
                    totals["evening_overlay_hit"] += 1
                if pressure_hit:
                    totals["evening_pressure_hit"] += 1
                if xvar_hit:
                    totals["evening_xvar_intersection_hit"] += 1
                event_rows.append(
                    {
                        "date": d,
                        "state_key": state_key,
                        "period": "Evening",
                        "winner": w.evening,
                        "winner_type": win_type,
                        "winner_vtrac_index": win_idx if evaluable else "",
                        "k": k,
                        "overlay_topk": ",".join(map(str, overlay_eve)),
                        "pressure_topk": ",".join(map(str, pressure_eve)),
                        "xvar_pressure_intersection": ",".join(map(str, xvar_pressure)),
                        "hit_overlay_topk": overlay_hit,
                        "hit_pressure_topk": pressure_hit,
                        "hit_xvar_pressure_intersection": xvar_hit,
                    }
                )

    _write_csv(out_event_csv, event_rows)
    _write_csv(out_index_csv, index_rows)

    def _rate(n: int, d: int) -> str:
        return f"{(n/d):.4f}" if d else "-"

    md: List[str] = []
    md.append(f"# Aux Badge Pressure Harness — {args.start_date} → {args.end_date}")
    md.append("")
    md.append(f"- Generated: `{_now_iso()}`")
    md.append(f"- Sharepacks root: `{_safe_rel(sharepacks_root)}`")
    md.append(f"- Rank-by: `{args.rank_by}` (colors: red=3 blue=2 purple=1; shapes: RC=2 BS=1)")
    md.append(f"- K: `{int(args.k)}`")
    md.append(f"- Event CSV: `{_safe_rel(out_event_csv)}`")
    md.append(f"- Index contract CSV: `{_safe_rel(out_index_csv)}`")
    md.append("")
    md.append("## Summary (evaluable events = winner has a vtrac_index)")
    md.append("")
    md.append(f"- Midday events: {totals['midday_events']} (evaluable={totals['midday_evaluable']})")
    md.append(f"  - Overlay topK hit: {totals['midday_overlay_hit']} / {totals['midday_evaluable']} (rate={_rate(totals['midday_overlay_hit'], totals['midday_evaluable'])})")
    md.append(f"  - Pressure topK hit: {totals['midday_pressure_hit']} / {totals['midday_evaluable']} (rate={_rate(totals['midday_pressure_hit'], totals['midday_evaluable'])})")
    md.append(
        f"  - Cross-variant pressure intersection hit: {totals['midday_xvar_intersection_hit']} / {totals['midday_evaluable']} (rate={_rate(totals['midday_xvar_intersection_hit'], totals['midday_evaluable'])})"
    )
    md.append(f"- Evening events: {totals['evening_events']} (evaluable={totals['evening_evaluable']})")
    md.append(f"  - Overlay topK hit: {totals['evening_overlay_hit']} / {totals['evening_evaluable']} (rate={_rate(totals['evening_overlay_hit'], totals['evening_evaluable'])})")
    md.append(f"  - Pressure topK hit: {totals['evening_pressure_hit']} / {totals['evening_evaluable']} (rate={_rate(totals['evening_pressure_hit'], totals['evening_evaluable'])})")
    md.append(
        f"  - Cross-variant pressure intersection hit: {totals['evening_xvar_intersection_hit']} / {totals['evening_evaluable']} (rate={_rate(totals['evening_xvar_intersection_hit'], totals['evening_evaluable'])})"
    )
    md.append("")
    md.append("Notes:")
    md.append("- Combined is treated as a lens only; event evaluation uses Midday→midday and Evening→evening.")
    md.append("- The cross-variant intersection is computed as (topK pressure Midday) ∩ (topK pressure Evening) for the same state/day.")
    md.append("")
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text("\n".join(md).rstrip() + "\n", encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

