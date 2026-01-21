#!/usr/bin/env python3
"""
Audit the Control Center "Due Doubles" board against sharepack-local Aux draw snapshots.

Goals:
- Verify the exported `Draws Since Double` values match recomputation from the state/variant draws CSV.
- Validate family cells parse cleanly and only reference known VTRAC double combos with consistent severity tags.
- Provide interpretable evaluation metrics (e.g., conditional on double winners) so low raw hit counts
  don't get misread as "broken math".

Reads (winner-safe):
- sharepacks/_predictive/<D>/control_center/due_doubles.csv (preferred when present)
- sharepacks/<D>/control_center/due_doubles.csv (fallback when predictive not present)
- sharepacks/<ROOT>/<D>/<STATE>/aux/draws/*_draws.csv (for DS recomputation)
- data/results/<D>.txt (for evaluation summary; RUNS-only output)

Writes:
- docs/AAT9_KIT/FINAL VALIDATION/RUNS/DUE_DOUBLES__PARITY_AUDIT__<A>_to_<B>.{csv,md}
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
SRC_ROOT = REPO_ROOT / "src"
if SRC_ROOT.exists() and str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))


from modules.draw_catalog import draws_since_last_double  # noqa: E402
from core.vtrac_families import VTRAC_DOUBLE_FAMILIES  # noqa: E402


_TOKEN_RE = re.compile(r"^(?P<combo>\d{3})\((?P<sev>[RB])(?P<var>[CME]):(?P<ds>\d+)\)$")


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _safe_rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _runs_dir() -> Path:
    return REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"


def _list_dates(start_date: str, end_date: str) -> List[str]:
    from datetime import date, timedelta

    def _parse(d: str) -> date:
        return date.fromisoformat(d)

    a = _parse(start_date)
    b = _parse(end_date)
    if b < a:
        raise SystemExit(f"--end-date must be >= --start-date (got {start_date}..{end_date})")
    out: List[str] = []
    cur = a
    while cur <= b:
        out.append(cur.isoformat())
        cur += timedelta(days=1)
    return out


def _read_csv_rows(path: Path) -> List[Dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", errors="replace", newline="") as f:
        reader = csv.DictReader(f)
        return [{k: (v or "") for k, v in (row or {}).items()} for row in reader]


def _normalize_pick3_literal(value: str) -> str:
    digits = "".join(ch for ch in str(value) if ch.isdigit())
    if not digits:
        return ""
    digits = digits.zfill(3) if len(digits) <= 3 else digits
    return digits if len(digits) == 3 else ""


def _canon(draw: str) -> str:
    d = _normalize_pick3_literal(draw)
    return "".join(sorted(d)) if d else ""


def _winner_type(draw: str) -> str:
    d = _normalize_pick3_literal(draw)
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

    text = results_file.read_text(encoding="utf-8", errors="replace")
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
                midday=_normalize_pick3_literal(midday or ""),
                evening=_normalize_pick3_literal(evening or ""),
            )
    return winners


def _find_draws_file(aux_draws_dir: Path, *, variant: str) -> Optional[Path]:
    if not aux_draws_dir.exists():
        return None
    want = variant.strip().lower()
    files = [p for p in aux_draws_dir.glob("*_draws.csv") if p.is_file()]
    if not files:
        return None
    if want in {"combined", "c"}:
        for p in files:
            name = p.name.lower()
            if "_midday_" in name or "_evening_" in name:
                continue
            return p
        return sorted(files)[0]
    if want in {"midday", "m"}:
        for p in files:
            if "_midday_" in p.name.lower():
                return p
        return None
    if want in {"evening", "e"}:
        for p in files:
            if "_evening_" in p.name.lower():
                return p
        return None
    return None


def _read_draws_list(path: Path, *, max_n: int = 1000) -> List[str]:
    if not path.exists():
        return []
    out: List[str] = []
    with path.open("r", encoding="utf-8", errors="replace", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            draw = _normalize_pick3_literal((row or {}).get("Draw", ""))
            if draw:
                out.append(draw)
            if len(out) >= max_n:
                break
    return out


@dataclass
class FamilyParseStats:
    token_count: int = 0
    invalid_token_count: int = 0
    unknown_combo_count: int = 0
    non_double_combo_count: int = 0
    severity_mismatch_count: int = 0
    family_label_unknown_count: int = 0
    unique_combos: set[str] = None  # type: ignore[assignment]
    unique_family_labels: set[str] = None  # type: ignore[assignment]

    def __post_init__(self) -> None:
        if self.unique_combos is None:
            self.unique_combos = set()
        if self.unique_family_labels is None:
            self.unique_family_labels = set()


def _parse_family_cell(
    value: str,
    *,
    known_double_combos: set[str],
    known_family_labels: set[str],
    red_threshold: int,
    blue_threshold: int,
) -> FamilyParseStats:
    stats = FamilyParseStats()
    raw = (value or "").strip()
    if not raw or raw == "-":
        return stats
    # Expected: "<label>: <token> <token> ..."
    if ":" not in raw:
        stats.invalid_token_count += 1
        return stats
    label, rest = raw.split(":", 1)
    label = label.strip()
    rest = rest.strip()
    if label:
        stats.unique_family_labels.add(label)
        if label not in known_family_labels:
            stats.family_label_unknown_count += 1
    if not rest:
        return stats
    for tok in rest.split():
        stats.token_count += 1
        m = _TOKEN_RE.match(tok)
        if not m:
            stats.invalid_token_count += 1
            continue
        combo = m.group("combo")
        sev = m.group("sev")
        ds = int(m.group("ds"))
        stats.unique_combos.add(combo)
        canon = "".join(sorted(combo))
        if canon not in known_double_combos:
            stats.unknown_combo_count += 1
        a, b, c = combo[0], combo[1], combo[2]
        if not (a == b or b == c or a == c):
            stats.non_double_combo_count += 1
        if sev == "R" and ds < red_threshold:
            stats.severity_mismatch_count += 1
        if sev == "B" and not (blue_threshold <= ds < red_threshold):
            stats.severity_mismatch_count += 1
    return stats


def _int(value: str) -> Optional[int]:
    try:
        return int(str(value).strip())
    except (TypeError, ValueError):
        return None


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
    p = argparse.ArgumentParser(description="Audit sharepack Control Center due_doubles.csv parity + metrics.")
    p.add_argument("--start-date", required=True, help="Start date D (YYYY-MM-DD).")
    p.add_argument("--end-date", required=True, help="End date D (YYYY-MM-DD).")
    p.add_argument(
        "--predictive-root",
        default="sharepacks/_predictive",
        help="Predictive sharepacks root (preferred for parity).",
    )
    p.add_argument("--sharepacks-root", default="sharepacks", help="Post-results sharepacks root (fallback).")
    p.add_argument("--results-dir", default="data/results", help="Results dir (for evaluation metrics).")
    p.add_argument("--out-dir", default=str(_runs_dir()), help="RUNS output directory.")
    p.add_argument("--topk-due", type=int, default=5, help="Top-K states by DS to evaluate as 'most due'.")
    p.add_argument("--red-threshold", type=int, default=1000, help="Very-late threshold for combo DS tokens.")
    p.add_argument("--blue-threshold", type=int, default=667, help="Late threshold for combo DS tokens.")
    p.add_argument("--force", action="store_true", help="Overwrite outputs.")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    dates = _list_dates(args.start_date, args.end_date)

    predictive_root = (REPO_ROOT / args.predictive_root).resolve()
    sharepacks_root = (REPO_ROOT / args.sharepacks_root).resolve()
    results_dir = (REPO_ROOT / args.results_dir).resolve()
    out_dir = Path(args.out_dir).resolve()

    out_csv = out_dir / f"DUE_DOUBLES__PARITY_AUDIT__{args.start_date}_to_{args.end_date}.csv"
    out_md = out_dir / f"DUE_DOUBLES__PARITY_AUDIT__{args.start_date}_to_{args.end_date}.md"
    if (out_csv.exists() or out_md.exists()) and not args.force:
        raise SystemExit(f"Outputs exist; pass --force to overwrite: {_safe_rel(out_csv)}")

    families = VTRAC_DOUBLE_FAMILIES
    known_family_labels = {f.label for f in families}
    known_double_combos = {c for f in families for c in f.combos}

    per_row: List[Dict[str, object]] = []
    per_day_summary: List[Dict[str, object]] = []

    total_ds_mismatch = 0
    total_family_invalid = 0
    total_family_unknown_combo = 0
    total_family_non_double = 0
    total_family_sev_mismatch = 0
    total_family_label_unknown = 0

    # For evaluation metrics (interpretation) at the *outcome* level (state×day×period),
    # not the Control Center row level (which includes Combined as a lens row).
    eval_totals = {
        "midday_outcomes": 0,
        "evening_outcomes": 0,
        "midday_double_events": 0,
        "evening_double_events": 0,
        "midday_double_in_family": 0,
        "evening_double_in_family": 0,
        "midday_any_in_family": 0,
        "evening_any_in_family": 0,
        "midday_topk_double_events": 0,
        "evening_topk_double_events": 0,
        "midday_topk_outcomes": 0,
        "evening_topk_outcomes": 0,
    }

    for d in dates:
        day_pred = predictive_root / d
        day_post = sharepacks_root / d
        root_used = "predictive" if (day_pred / "control_center" / "due_doubles.csv").exists() else "post"
        day_dir = day_pred if root_used == "predictive" else day_post

        due_path = day_dir / "control_center" / "due_doubles.csv"
        if not due_path.exists():
            per_day_summary.append(
                {
                    "date": d,
                    "root_used": root_used,
                    "status": "missing_due_doubles_csv",
                    "due_path": _safe_rel(due_path),
                }
            )
            continue

        due_rows = _read_csv_rows(due_path)
        if not due_rows:
            per_day_summary.append(
                {
                    "date": d,
                    "root_used": root_used,
                    "status": "empty_due_doubles_csv",
                    "due_path": _safe_rel(due_path),
                }
            )
            continue

        # Optional parity check vs the other root (predictive vs post-results).
        parity_non_winner_mismatches = 0
        if root_used == "predictive" and (day_post / "control_center" / "due_doubles.csv").exists():
            post_rows = _read_csv_rows(day_post / "control_center" / "due_doubles.csv")
            post_index = {(r.get("StateKey", ""), r.get("Variant", "")): r for r in post_rows}
            for r in due_rows:
                key = (r.get("StateKey", ""), r.get("Variant", ""))
                pr = post_index.get(key)
                if not pr:
                    parity_non_winner_mismatches += 1
                    continue
                # Compare only the stable columns; winners are expected to differ.
                stable_cols = ["State", "StateKey", "Variant", "Draws Since Double", "Family 1", "Family 2", "Family 3", "Family 4", "Family 5"]
                for col in stable_cols:
                    if (r.get(col, "") or "") != (pr.get(col, "") or ""):
                        parity_non_winner_mismatches += 1
                        break

        results_file = results_dir / f"{d}.txt"
        winners_by_state = _load_results_winners(results_file)

        # Build per-state summary (families + DS by period) for evaluation metrics.
        state_summaries: Dict[str, Dict[str, object]] = {}
        for r in due_rows:
            state_key = (r.get("StateKey") or "").strip()
            if not state_key:
                continue
            entry = state_summaries.setdefault(state_key, {"state_label": (r.get("State") or "").strip(), "ds": {}, "family_combos": set()})
            variant = (r.get("Variant") or "").strip()
            ds_val = _int(r.get("Draws Since Double", ""))
            if ds_val is not None and variant in {"Midday", "Evening", "Combined"}:
                ds_map = entry.get("ds")
                if not isinstance(ds_map, dict):
                    ds_map = {}
                    entry["ds"] = ds_map
                ds_map[variant] = ds_val
            # Families are stable across variants for a given state/day; parse once.
            if entry.get("family_combos"):
                continue
            family_stats = FamilyParseStats()
            for i in range(1, 6):
                cell = r.get(f"Family {i}", "")
                st = _parse_family_cell(
                    cell,
                    known_double_combos=known_double_combos,
                    known_family_labels=known_family_labels,
                    red_threshold=int(args.red_threshold),
                    blue_threshold=int(args.blue_threshold),
                )
                family_stats.unique_combos |= st.unique_combos
            entry["family_combos"] = set(family_stats.unique_combos)

        # Build per-period DS ranking for "most due" evaluation (per day).
        topk = int(args.topk_due)
        ds_midday = [(k, int(v["ds"]["Midday"])) for k, v in state_summaries.items() if "Midday" in (v.get("ds") or {})]  # type: ignore[index]
        ds_evening = [(k, int(v["ds"]["Evening"])) for k, v in state_summaries.items() if "Evening" in (v.get("ds") or {})]  # type: ignore[index]
        ds_midday.sort(key=lambda t: t[1], reverse=True)
        ds_evening.sort(key=lambda t: t[1], reverse=True)
        topk_midday = [k for k, _ in ds_midday[:topk]]
        topk_evening = [k for k, _ in ds_evening[:topk]]

        # Row-level parity checks.
        ds_mismatch = 0
        family_invalid = 0
        family_unknown_combo = 0
        family_non_double = 0
        family_sev_mismatch = 0
        family_label_unknown = 0

        for r in due_rows:
            state_key = (r.get("StateKey") or "").strip()
            variant = (r.get("Variant") or "").strip()
            state_label = (r.get("State") or "").strip()
            ds_reported = _int(r.get("Draws Since Double", ""))

            aux_draws_dir = day_dir / state_key / "aux" / "draws"
            draws_file = _find_draws_file(aux_draws_dir, variant=variant)
            draws_list = _read_draws_list(draws_file, max_n=1000) if draws_file else []
            ds_recomputed, last_double = draws_since_last_double(draws_list) if draws_list else (None, None)
            ds_match = bool(ds_reported is not None and ds_recomputed is not None and ds_reported == ds_recomputed)
            if ds_reported is not None and ds_recomputed is not None and not ds_match:
                ds_mismatch += 1
                total_ds_mismatch += 1

            # Parse family cells for validity.
            family_stats = FamilyParseStats()
            for i in range(1, 6):
                cell = r.get(f"Family {i}", "")
                st = _parse_family_cell(
                    cell,
                    known_double_combos=known_double_combos,
                    known_family_labels=known_family_labels,
                    red_threshold=int(args.red_threshold),
                    blue_threshold=int(args.blue_threshold),
                )
                family_stats.token_count += st.token_count
                family_stats.invalid_token_count += st.invalid_token_count
                family_stats.unknown_combo_count += st.unknown_combo_count
                family_stats.non_double_combo_count += st.non_double_combo_count
                family_stats.severity_mismatch_count += st.severity_mismatch_count
                family_stats.family_label_unknown_count += st.family_label_unknown_count
                family_stats.unique_combos |= st.unique_combos
                family_stats.unique_family_labels |= st.unique_family_labels

            family_invalid += family_stats.invalid_token_count
            family_unknown_combo += family_stats.unknown_combo_count
            family_non_double += family_stats.non_double_combo_count
            family_sev_mismatch += family_stats.severity_mismatch_count
            family_label_unknown += family_stats.family_label_unknown_count

            total_family_invalid += family_stats.invalid_token_count
            total_family_unknown_combo += family_stats.unknown_combo_count
            total_family_non_double += family_stats.non_double_combo_count
            total_family_sev_mismatch += family_stats.severity_mismatch_count
            total_family_label_unknown += family_stats.family_label_unknown_count

            # Winner eval (RUNS-only) for CSV row. Summary metrics are computed at the outcome-level below.
            w = winners_by_state.get(state_key)
            winner_midday = w.midday if w else ""
            winner_evening = w.evening if w else ""
            wt_midday = _winner_type(winner_midday) if winner_midday else ""
            wt_evening = _winner_type(winner_evening) if winner_evening else ""
            in_family_midday = bool(winner_midday and _canon(winner_midday) in family_stats.unique_combos)
            in_family_evening = bool(winner_evening and _canon(winner_evening) in family_stats.unique_combos)

            per_row.append(
                {
                    "date": d,
                    "root_used": root_used,
                    "state_key": state_key,
                    "state_label": state_label,
                    "variant": variant,
                    "ds_reported": ds_reported if ds_reported is not None else "",
                    "ds_recomputed": ds_recomputed if ds_recomputed is not None else "",
                    "ds_match": ds_match,
                    "last_double_draw": last_double or "",
                    "draws_file": _safe_rel(draws_file) if draws_file else "",
                    "family_unique_combos": len(family_stats.unique_combos),
                    "family_unique_labels": len(family_stats.unique_family_labels),
                    "family_tokens": family_stats.token_count,
                    "family_invalid_tokens": family_stats.invalid_token_count,
                    "family_unknown_combos": family_stats.unknown_combo_count,
                    "family_non_double_combos": family_stats.non_double_combo_count,
                    "family_severity_mismatch": family_stats.severity_mismatch_count,
                    "family_label_unknown": family_stats.family_label_unknown_count,
                    "winner_midday": winner_midday or "",
                    "winner_midday_type": wt_midday or "",
                    "winner_midday_in_family": in_family_midday,
                    "winner_evening": winner_evening or "",
                    "winner_evening_type": wt_evening or "",
                    "winner_evening_in_family": in_family_evening,
                }
            )

        per_day_summary.append(
            {
                "date": d,
                "root_used": root_used,
                "due_rows": len(due_rows),
                "parity_non_winner_mismatches": parity_non_winner_mismatches,
                "ds_mismatches": ds_mismatch,
                "family_invalid_tokens": family_invalid,
                "family_unknown_combos": family_unknown_combo,
                "family_non_double_combos": family_non_double,
                "family_severity_mismatch": family_sev_mismatch,
                "family_label_unknown": family_label_unknown,
                "due_path": _safe_rel(due_path),
                "results_file": _safe_rel(results_file) if results_file.exists() else "",
            }
        )

        # Outcome-level evaluation metrics (state×day×period), using the single family set per state.
        for state_key, meta in state_summaries.items():
            fam = meta.get("family_combos") or set()
            w = winners_by_state.get(state_key)
            if not w:
                continue
            if w.midday:
                eval_totals["midday_outcomes"] += 1
                in_family = bool(_canon(w.midday) in fam)
                if in_family:
                    eval_totals["midday_any_in_family"] += 1
                wt = _winner_type(w.midday)
                if wt in {"double", "triple"}:
                    eval_totals["midday_double_events"] += 1
                    if in_family:
                        eval_totals["midday_double_in_family"] += 1
            if w.evening:
                eval_totals["evening_outcomes"] += 1
                in_family = bool(_canon(w.evening) in fam)
                if in_family:
                    eval_totals["evening_any_in_family"] += 1
                wt = _winner_type(w.evening)
                if wt in {"double", "triple"}:
                    eval_totals["evening_double_events"] += 1
                    if in_family:
                        eval_totals["evening_double_in_family"] += 1

        # "Most due" (DS topK) evaluation: does high DS correlate with next-day double events?
        if topk_midday:
            eval_totals["midday_topk_outcomes"] += len(topk_midday)
            for state_key in topk_midday:
                w = winners_by_state.get(state_key)
                if not w or not w.midday:
                    continue
                if _winner_type(w.midday) in {"double", "triple"}:
                    eval_totals["midday_topk_double_events"] += 1
        if topk_evening:
            eval_totals["evening_topk_outcomes"] += len(topk_evening)
            for state_key in topk_evening:
                w = winners_by_state.get(state_key)
                if not w or not w.evening:
                    continue
                if _winner_type(w.evening) in {"double", "triple"}:
                    eval_totals["evening_topk_double_events"] += 1

    _write_csv(out_csv, per_row)

    def _rate(num: int, den: int) -> str:
        return f"{(num/den):.4f}" if den else "-"

    md_lines: List[str] = []
    md_lines.append(f"# Due Doubles — Parity Audit ({args.start_date} → {args.end_date})")
    md_lines.append("")
    md_lines.append(f"- Generated: `{_now_iso()}`")
    md_lines.append(f"- Predictive root (preferred): `{_safe_rel(predictive_root)}`")
    md_lines.append(f"- Post-results root (fallback): `{_safe_rel(sharepacks_root)}`")
    md_lines.append(f"- Output CSV: `{_safe_rel(out_csv)}`")
    md_lines.append("")
    md_lines.append("## 1) Parity summary")
    md_lines.append("")
    md_lines.append(f"- Rows audited: **{len(per_row)}**")
    md_lines.append(f"- DS mismatches: **{total_ds_mismatch}**")
    md_lines.append(f"- Family invalid tokens: **{total_family_invalid}**")
    md_lines.append(f"- Family unknown combos: **{total_family_unknown_combo}**")
    md_lines.append(f"- Family non-double combos: **{total_family_non_double}**")
    md_lines.append(f"- Family severity mismatches: **{total_family_sev_mismatch}**")
    md_lines.append(f"- Family unknown labels: **{total_family_label_unknown}**")
    md_lines.append("")
    md_lines.append("Per-day notes (only non-OK rows shown):")
    for s in per_day_summary:
        if s.get("status"):
            md_lines.append(f"- `{s['date']}`: {s['status']} (`{s.get('due_path','')}`)")
            continue
        if any(int(s.get(k, 0) or 0) for k in ("parity_non_winner_mismatches", "ds_mismatches", "family_invalid_tokens", "family_unknown_combos", "family_non_double_combos", "family_severity_mismatch", "family_label_unknown")):
            md_lines.append(
                f"- `{s['date']}` root={s['root_used']} parity_mismatch={s['parity_non_winner_mismatches']} ds_mismatch={s['ds_mismatches']} "
                f"family_invalid={s['family_invalid_tokens']} unknown_combo={s['family_unknown_combos']} sev_mismatch={s['family_severity_mismatch']} "
                f"label_unknown={s['family_label_unknown']}"
            )
    md_lines.append("")
    md_lines.append("## 2) Interpretable evaluation metrics (RUNS-only; results labels)")
    md_lines.append("")
    md_lines.append("These are meant to prevent misreading low raw counts as a data bug.")
    md_lines.append("")
    md_lines.append("### 2.1 Base rates")
    md_lines.append("")
    md_lines.append(f"- Midday outcomes: **{eval_totals['midday_outcomes']}**")
    md_lines.append(f"- Evening outcomes: **{eval_totals['evening_outcomes']}**")
    md_lines.append(f"- Midday double+triple events: **{eval_totals['midday_double_events']}** (rate={_rate(eval_totals['midday_double_events'], eval_totals['midday_outcomes'])})")
    md_lines.append(f"- Evening double+triple events: **{eval_totals['evening_double_events']}** (rate={_rate(eval_totals['evening_double_events'], eval_totals['evening_outcomes'])})")
    md_lines.append("")
    md_lines.append("### 2.2 'Winner in due-doubles family' (strict membership)")
    md_lines.append("")
    md_lines.append(
        f"- Midday any-type in-family: **{eval_totals['midday_any_in_family']}** / {eval_totals['midday_outcomes']} (rate={_rate(eval_totals['midday_any_in_family'], eval_totals['midday_outcomes'])})"
    )
    md_lines.append(
        f"- Evening any-type in-family: **{eval_totals['evening_any_in_family']}** / {eval_totals['evening_outcomes']} (rate={_rate(eval_totals['evening_any_in_family'], eval_totals['evening_outcomes'])})"
    )
    md_lines.append("")
    md_lines.append(
        f"- Midday double-only in-family: **{eval_totals['midday_double_in_family']}** / {eval_totals['midday_double_events']} (rate={_rate(eval_totals['midday_double_in_family'], eval_totals['midday_double_events'])})"
    )
    md_lines.append(
        f"- Evening double-only in-family: **{eval_totals['evening_double_in_family']}** / {eval_totals['evening_double_events']} (rate={_rate(eval_totals['evening_double_in_family'], eval_totals['evening_double_events'])})"
    )
    md_lines.append("")
    md_lines.append("### 2.3 'Most due' evaluation (DS ranking → next-day double events)")
    md_lines.append("")
    md_lines.append(f"- TopK used: **{int(args.topk_due)}** states per day/period (ranked by `Draws Since Double`).")
    md_lines.append(
        f"- Midday topK double events: **{eval_totals['midday_topk_double_events']}** / {eval_totals['midday_topk_outcomes']} (rate={_rate(eval_totals['midday_topk_double_events'], eval_totals['midday_topk_outcomes'])})"
    )
    md_lines.append(
        f"- Evening topK double events: **{eval_totals['evening_topk_double_events']}** / {eval_totals['evening_topk_outcomes']} (rate={_rate(eval_totals['evening_topk_double_events'], eval_totals['evening_topk_outcomes'])})"
    )
    md_lines.append("")
    md_lines.append("Interpretation:")
    md_lines.append("- DS is a 'state due for any double' indicator; family membership is a stricter 'which double' indicator.")
    md_lines.append("- Family membership should be interpreted mainly on double/triple winners (conditional rate above).")
    md_lines.append("")
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text("\n".join(md_lines).rstrip() + "\n", encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
