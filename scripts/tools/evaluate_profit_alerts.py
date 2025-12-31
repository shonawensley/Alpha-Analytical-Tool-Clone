#!/usr/bin/env python3
"""
Evaluate sharepack-aligned Profit Alerts (A01–A12) against results timelines.

Inputs (for a results date D):
  - sharepacks/<D>/control_center/profit_alerts.csv
  - data/results/<YYYY-MM-DD>.txt (D and future days for windowed evaluation)

Outputs:
  - sharepacks/<D>/control_center/profit_alerts_eval.csv
  - sharepacks/<D>/control_center/profit_alerts_eval_merged.csv
  - sharepacks/<D>/control_center/profit_alerts_eval.md

Notes:
  - This is evaluation-only (no wagering engine).
  - Combined is an analytic lens; only Midday/Evening are gradeable outcomes.
  - See: docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Alerts_Evaluation_Charter.md
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from itertools import permutations
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from modules.vtrac_reference import get_vtrac_index


RESULTS_NAME_RE = re.compile(r"^\d{4}-\d{2}-\d{2}\.txt$")


def _norm_state(label: str) -> str:
    return "".join(ch for ch in (label or "").lower() if ch.isalpha())


def _normalize_pick3_literal(value: str) -> str:
    digits = "".join(ch for ch in str(value or "") if ch.isdigit())
    if not digits:
        return ""
    return digits.zfill(3) if len(digits) <= 3 else digits


def _canon_draw(draw: str) -> str:
    literal = _normalize_pick3_literal(draw)
    if len(literal) != 3 or not literal.isdigit():
        return ""
    return "".join(sorted(literal))


def _permutations3(value: str) -> List[str]:
    digits = _normalize_pick3_literal(value)
    if len(digits) != 3 or not digits.isdigit():
        return []
    return sorted({"".join(p) for p in set(permutations(digits, 3))})


def _parse_implied_set(value: str) -> List[str]:
    raw = (value or "").strip()
    if not raw or raw == "-" or raw.lower() == "nan":
        return []
    try:
        parsed = json.loads(raw)
    except Exception:
        return []
    if not isinstance(parsed, list):
        return []
    out: List[str] = []
    for item in parsed:
        lit = _normalize_pick3_literal(item)
        if len(lit) == 3 and lit.isdigit():
            out.append(lit)
    return sorted(set(out))


def _parse_results_file(results_file: Path) -> Dict[str, Dict[str, str]]:
    """
    Parse data/results/<D>.txt into {norm_state: {"Midday": "123", "Evening": "456"}}.

    Robustness note:
      results files can contain non-tab lines (extra draw rows for some states).
      We only consume well-formed TSV rows with >=3 columns.
    """
    winners: Dict[str, Dict[str, str]] = {}
    with results_file.open(newline="", encoding="utf-8", errors="replace") as fh:
        reader = csv.reader(fh, delimiter="\t")
        for row in reader:
            if not row:
                continue
            state_raw = (row[0] or "").strip()
            if not state_raw or state_raw.lower() == "state":
                continue
            if state_raw.lower() in {"midday", "evening"}:
                continue
            if len(row) < 3:
                continue
            midday = _normalize_pick3_literal((row[1] or "").strip())
            evening = _normalize_pick3_literal((row[2] or "").strip())
            entry: Dict[str, str] = {}
            if len(midday) == 3 and midday.isdigit():
                entry["Midday"] = midday
            if len(evening) == 3 and evening.isdigit():
                entry["Evening"] = evening
            if entry:
                winners[_norm_state(state_raw)] = entry
    return winners


def _list_results(results_dir: Path) -> List[str]:
    dates: List[str] = []
    for p in sorted(results_dir.iterdir()):
        if not p.is_file():
            continue
        if RESULTS_NAME_RE.match(p.name):
            dates.append(p.stem)
    return dates


def _load_results_timeline(results_dir: Path) -> Dict[str, Dict[str, Dict[str, str]]]:
    timeline: Dict[str, Dict[str, Dict[str, str]]] = {}
    for date in _list_results(results_dir):
        timeline[date] = _parse_results_file(results_dir / f"{date}.txt")
    return timeline


def _iter_draw_steps(
    *,
    start_date: str,
    dates: Sequence[str],
    winners_timeline: Dict[str, Dict[str, Dict[str, str]]],
    state_norm: str,
    variant: str,
) -> Iterable[Tuple[str, str, str]]:
    """
    Yield (date, period, winner_literal) draw-steps starting at start_date, using charter rules.

    Missing periods are skipped (do not yield; do not consume a step).
    """
    try:
        start_idx = dates.index(start_date)
    except ValueError:
        return

    if variant not in {"Midday", "Evening", "Combined"}:
        return

    periods = ["Midday"] if variant == "Midday" else ["Evening"] if variant == "Evening" else ["Midday", "Evening"]
    for date in dates[start_idx:]:
        day = winners_timeline.get(date, {}).get(state_norm, {})
        for period in periods:
            winner = (day.get(period) or "").strip()
            if winner:
                yield date, period, winner


def _when_key(date: str, period: str) -> Tuple[str, int]:
    # Dates are ISO YYYY-MM-DD strings (lexicographically sortable).
    return date, 0 if period == "Midday" else 1


def _iter_outcome_steps_from_when(
    *,
    start_date: str,
    start_period: str,
    dates: Sequence[str],
    winners_timeline: Dict[str, Dict[str, Dict[str, str]]],
    state_norm: str,
) -> Iterable[Tuple[str, str, str]]:
    """
    Yield (date, period, winner_literal) for real outcomes (Midday/Evening),
    starting at a specific (date, period) boundary.

    Missing periods are skipped (do not yield).
    """
    try:
        start_idx = dates.index(start_date)
    except ValueError:
        return

    for date in dates[start_idx:]:
        day = winners_timeline.get(date, {}).get(state_norm, {})
        for period in ["Midday", "Evening"]:
            if date == start_date and start_period == "Evening" and period == "Midday":
                continue
            winner = (day.get(period) or "").strip()
            if winner:
                yield date, period, winner


def _match_hit_types(
    *,
    winner: str,
    candidate_canon: str,
    suggested: str,
    implied_set: Sequence[str],
    evidence: Dict[str, Any],
) -> List[str]:
    winner = _normalize_pick3_literal(winner)
    types: List[str] = []

    if implied_set and winner in implied_set:
        if suggested == "BOX":
            types.append("Boxed")
        elif suggested.startswith("STR8"):
            types.append("Straight")
        else:
            types.append("Set")

    orders = _normalize_pick3_literal(str(evidence.get("orders_modal_value") or ""))
    if orders and winner == orders:
        types.append("Straight")

    if candidate_canon:
        if _canon_draw(winner) == candidate_canon:
            types.append("Boxed")

    current_index = evidence.get("current_index")
    if isinstance(current_index, int):
        idx = get_vtrac_index(winner)
        if idx is not None and idx == current_index:
            types.append("VTRAC")

    # Stable ordering for display
    ordering = {"Straight": 0, "Boxed": 1, "VTRAC": 2, "Set": 3}
    return sorted(set(types), key=lambda t: ordering.get(t, 99))


@dataclass(frozen=True)
class EpisodeEval:
    row_num: int
    results_date: str
    start_when: str
    expiry_when: str
    state: str
    state_key: str
    variant: str
    alert_id: str
    strength: int
    suggested: str
    row_type: str
    implied_set_size: int
    a11_star_level: int
    a11_star_score: float
    cap_lines: int
    decay_draws: int
    badges: str
    canonical_raw: str
    canonical: str
    stable_contains_canonical: str
    evidence_ok: bool
    evidence_error: str
    strict_hit: str
    strict_hit_type: str
    strict_hit_when: str
    status: str
    time_to_hit_steps: str
    hit_when: str
    hit_type: str
    hit_within_decay: str
    hit_within_7: str
    hit_within_14: str
    hit_any_within_decay: str
    hit_any_when: str
    hit_any_type: str
    hit_any_within_7: str
    hit_any_within_14: str


@dataclass(frozen=True)
class MergedEpisodeEval:
    results_date: str
    state: str
    state_key: str
    variant: str
    implied_set_size: int
    implied_set: str
    alert_ids: str
    suggested_kinds: str
    strength_max: int
    decay_min: int
    decay_max: int
    promoters: str
    status: str
    time_to_hit_steps: str
    hit_when: str
    hit_type: str
    hit_within_7: str
    hit_within_14: str
    hit_any_within_decay: str
    hit_any_when: str
    hit_any_type: str
    hit_any_within_7: str
    hit_any_within_14: str


def _parse_int(value: str, *, default: int = 0) -> int:
    try:
        return int(str(value).strip())
    except Exception:
        return default


def _truthy(value: Optional[bool]) -> str:
    if value is True:
        return "Y"
    if value is False:
        return "N"
    return "?"


def _load_stable_canonicals_by_section(stable_scores_csv: Path) -> Dict[str, set[str]]:
    """
    Return {section: {Canonical}} from a sharepack Stable patterns scores CSV.

    This is used as an integrity check only (evidence traceability), not as an
    input to the hit evaluation itself.
    """
    by_section: Dict[str, set[str]] = {}
    if not stable_scores_csv.exists():
        return by_section
    with stable_scores_csv.open(newline="", encoding="utf-8", errors="replace") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            section = (row.get("section") or "").strip()
            canon = _canon_draw(row.get("Canonical") or "")
            if not section or not canon:
                continue
            by_section.setdefault(section, set()).add(canon)
    return by_section


def _merge_candidate_rows(
    *,
    results_date: str,
    rows: Sequence[Dict[str, str]],
    dates: Sequence[str],
    winners_timeline: Dict[str, Dict[str, Dict[str, str]]],
) -> List[MergedEpisodeEval]:
    """
    Build a "merged episodes" view so co-firing rows that imply the same play-set
    are not double-counted.

    v0 rule:
      - Candidate identity = (state_key, variant, implied_set)
      - Promoters (OVERLAY/SKIP) attach as tags; they are not evaluated as a
        standalone candidate set.
    """
    # Index promoters (A03/A08/etc) by state+variant, with Combined treated as a state-wide tag.
    promoters_by_state_variant: Dict[Tuple[str, str], set[str]] = {}

    def _add_promoter(state_key: str, variant: str, alert_id: str) -> None:
        if not state_key or not alert_id:
            return
        key = (state_key, "*" if variant == "Combined" else variant)
        promoters_by_state_variant.setdefault(key, set()).add(alert_id)

    for row in rows:
        alert_id = (row.get("AlertId") or "").strip()
        suggested = (row.get("Suggested") or "").strip()
        if suggested in {"OVERLAY", "SKIP"} or alert_id in {"A03", "A08"}:
            _add_promoter((row.get("StateKey") or "").strip(), (row.get("Variant") or "").strip(), alert_id)

    # Group candidate rows by the implied play-set.
    groups: Dict[Tuple[str, str, str], Dict[str, Any]] = {}
    for row in rows:
        alert_id = (row.get("AlertId") or "").strip()
        suggested = (row.get("Suggested") or "").strip()
        if suggested in {"OVERLAY", "SKIP"} or alert_id in {"A03", "A08"}:
            continue

        state = (row.get("State") or "").strip()
        state_key = (row.get("StateKey") or "").strip()
        variant = (row.get("Variant") or "").strip()
        if not state_key or not variant:
            continue

        canonical = _canon_draw(row.get("Canonical") or "")
        implied = _parse_implied_set(row.get("ImpliedSet") or "")
        if not implied and canonical and suggested in {"BOX", "STR8_3"}:
            implied = _permutations3(canonical)
        if not implied:
            continue

        implied_json = json.dumps(sorted(implied), separators=(",", ":"))
        key = (state_key, variant, implied_json)
        g = groups.setdefault(
            key,
            {
                "state": state,
                "state_key": state_key,
                "variant": variant,
                "implied_json": implied_json,
                "implied": sorted(implied),
                "alert_ids": set(),
                "suggested_kinds": set(),
                "strength_max": 0,
                "decay_min": None,
                "decay_max": 0,
            },
        )
        g["alert_ids"].add(alert_id or "?")
        if suggested:
            g["suggested_kinds"].add(suggested)
        g["strength_max"] = max(int(g["strength_max"]), _parse_int(row.get("Strength") or "", default=0))
        dd = _parse_int(row.get("DecayDraws") or "", default=0)
        g["decay_max"] = max(int(g["decay_max"]), dd)
        g["decay_min"] = dd if g["decay_min"] is None else min(int(g["decay_min"]), dd)

    merged: List[MergedEpisodeEval] = []

    for (_, _, _), g in sorted(groups.items(), key=lambda kv: (kv[0][0], kv[0][1], kv[0][2])):
        state = str(g.get("state") or "")
        state_key = str(g.get("state_key") or "")
        variant = str(g.get("variant") or "")
        implied: List[str] = list(g.get("implied") or [])
        implied_json = str(g.get("implied_json") or "")
        alert_ids = sorted({str(a) for a in (g.get("alert_ids") or set()) if a})
        suggested_kinds = sorted({str(s) for s in (g.get("suggested_kinds") or set()) if s})
        strength_max = int(g.get("strength_max") or 0)
        decay_min = int(g.get("decay_min") or 0)
        decay_max = int(g.get("decay_max") or 0)

        state_norm = _norm_state(state)
        max_horizon = max([decay_max, 7, 14, 1])
        steps: List[Tuple[str, str, str]] = []
        for date, period, winner in _iter_draw_steps(
            start_date=results_date, dates=dates, winners_timeline=winners_timeline, state_norm=state_norm, variant=variant
        ):
            steps.append((date, period, winner))
            if len(steps) >= max_horizon:
                break

        def first_hit(within_steps: int) -> Tuple[Optional[int], str]:
            if within_steps <= 0:
                return None, ""
            for step_idx, (date, period, winner) in enumerate(steps[:within_steps]):
                if _normalize_pick3_literal(winner) in implied:
                    return step_idx, f"{date} {period}"
            return None, ""

        start_step = steps[0] if steps else None

        def first_hit_any(within_variant_steps: int) -> Tuple[Optional[int], str, bool]:
            """
            Cross-variant diagnostic:
              - boundary is defined by the variant-faithful Nth step (time-span),
              - search any real outcome (Midday/Evening) within that time-span.
            """
            if within_variant_steps <= 0 or not start_step:
                return None, "", False
            boundary_known = len(steps) >= within_variant_steps
            boundary_key: Optional[Tuple[str, int]] = None
            if boundary_known:
                boundary_key = _when_key(steps[within_variant_steps - 1][0], steps[within_variant_steps - 1][1])

            out_idx = 0
            for date, period, winner in _iter_outcome_steps_from_when(
                start_date=start_step[0],
                start_period=start_step[1],
                dates=dates,
                winners_timeline=winners_timeline,
                state_norm=state_norm,
            ):
                if boundary_key is not None and _when_key(date, period) > boundary_key:
                    break
                if _normalize_pick3_literal(winner) in implied:
                    return out_idx, f"{date} {period}", boundary_known
                out_idx += 1
            return None, "", boundary_known

        def hit_within(h: int) -> str:
            if h <= 0:
                return "?"
            hit_idx, _ = first_hit(h)
            if hit_idx is not None:
                return "Y"
            return "N" if len(steps) >= h else "?"

        hit_idx, hit_when = first_hit(decay_max)
        if hit_idx is not None:
            status = "HIT"
            time_to_hit_steps = str(hit_idx)
            hit_within_decay = "Y"
        else:
            if len(steps) >= max(decay_max, 1):
                status = "EXPIRED"
                time_to_hit_steps = ""
                hit_when = ""
                hit_within_decay = "N"
            else:
                status = "CENSORED"
                time_to_hit_steps = ""
                hit_when = ""
                hit_within_decay = "?"

        # Primary hit label for the merged play-set.
        hit_type = ""
        if status == "HIT":
            if any(str(s).startswith("STR8") for s in suggested_kinds):
                hit_type = "Straight"
            elif "BOX" in suggested_kinds:
                hit_type = "Boxed"
            else:
                hit_type = "Set"

        any_hit_idx, any_hit_when, any_boundary_known = first_hit_any(decay_max)
        if any_hit_idx is not None:
            hit_any_within_decay = "Y"
            hit_any_when = any_hit_when
        else:
            hit_any_within_decay = "N" if any_boundary_known else "?"
            hit_any_when = ""

        hit_any_type = ""
        if hit_any_within_decay == "Y":
            if any(str(s).startswith("STR8") for s in suggested_kinds):
                hit_any_type = "Straight"
            elif "BOX" in suggested_kinds:
                hit_any_type = "Boxed"
            else:
                hit_any_type = "Set"

        def hit_any_within(h: int) -> str:
            if h <= 0:
                return "?"
            hit_idx, _, boundary_known = first_hit_any(h)
            if hit_idx is not None:
                return "Y"
            return "N" if boundary_known else "?"

        promos: set[str] = set()
        promos |= promoters_by_state_variant.get((state_key, "*"), set())
        promos |= promoters_by_state_variant.get((state_key, variant), set())
        if variant == "Combined":
            promos |= promoters_by_state_variant.get((state_key, "Midday"), set())
            promos |= promoters_by_state_variant.get((state_key, "Evening"), set())
        promoters = ",".join(sorted(promos))

        merged.append(
            MergedEpisodeEval(
                results_date=results_date,
                state=state,
                state_key=state_key,
                variant=variant,
                implied_set_size=len(implied),
                implied_set=implied_json,
                alert_ids=",".join(alert_ids),
                suggested_kinds=",".join(suggested_kinds),
                strength_max=strength_max,
                decay_min=decay_min,
                decay_max=decay_max,
                promoters=promoters,
                status=status,
                time_to_hit_steps=time_to_hit_steps,
                hit_when=hit_when,
                hit_type=hit_type,
                hit_within_7=hit_within(7),
                hit_within_14=hit_within(14),
                hit_any_within_decay=hit_any_within_decay,
                hit_any_when=hit_any_when,
                hit_any_type=hit_any_type,
                hit_any_within_7=hit_any_within(7),
                hit_any_within_14=hit_any_within(14),
            )
        )

    return merged


def evaluate_day(
    *,
    results_date: str,
    sharepack_day_dir: Path,
    results_dir: Path,
) -> Tuple[List[EpisodeEval], List[MergedEpisodeEval], Dict[str, Any]]:
    cc_dir = sharepack_day_dir / "control_center"
    alerts_path = cc_dir / "profit_alerts.csv"
    if not alerts_path.exists():
        raise SystemExit(f"profit_alerts.csv not found: {alerts_path}")

    timeline = _load_results_timeline(results_dir)
    dates = sorted(timeline.keys())
    if results_date not in timeline:
        raise SystemExit(f"results date not found under {results_dir}: {results_date}.txt")

    rows: List[Dict[str, str]] = []
    with alerts_path.open(newline="", encoding="utf-8", errors="replace") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            rows.append({k: (v or "").strip() for k, v in row.items()})

    evals: List[EpisodeEval] = []
    integrity = {
        "evidence_parse_errors": 0,
        "non_3digit_canonical": 0,
        "missing_results_state": 0,
        "stable_scores_missing": 0,
        "stable_candidate_missing": 0,
        "rows_total": len(rows),
    }

    stable_cache: Dict[str, Dict[str, set[str]]] = {}

    for idx, row in enumerate(rows, start=1):
        state = row.get("State", "")
        state_key = row.get("StateKey", "")
        variant = row.get("Variant", "")
        alert_id = row.get("AlertId", "")
        strength = _parse_int(row.get("Strength", ""), default=0)
        suggested = row.get("Suggested", "")
        row_type = "PROMOTER" if suggested in {"OVERLAY", "SKIP"} else ("GOVERNOR" if alert_id == "A11" else "CANDIDATE")
        cap_lines = _parse_int(row.get("CapLines", ""), default=0)
        decay_draws = _parse_int(row.get("DecayDraws", ""), default=0)
        badges = row.get("Badges", "")
        canonical_raw = row.get("Canonical", "")
        implied_set = _parse_implied_set(row.get("ImpliedSet", ""))

        canonical = _canon_draw(canonical_raw)
        if canonical_raw not in {"", "-"} and not canonical:
            integrity["non_3digit_canonical"] += 1
        if not implied_set and canonical and suggested in {"BOX", "STR8_3"}:
            implied_set = _permutations3(canonical)
        implied_set_size = len(implied_set)

        evidence_ok = True
        evidence_error = ""
        evidence: Dict[str, Any] = {}
        ev_raw = row.get("Evidence", "")
        if ev_raw:
            try:
                parsed = json.loads(ev_raw)
                if isinstance(parsed, dict):
                    evidence = parsed
                else:
                    evidence_ok = False
                    evidence_error = f"evidence not dict ({type(parsed).__name__})"
            except Exception as exc:
                evidence_ok = False
                evidence_error = f"evidence json parse error: {exc}"
        if not evidence_ok:
            integrity["evidence_parse_errors"] += 1

        a11_star_level = _parse_int(str(evidence.get("star_level") or ""), default=0) if alert_id == "A11" else 0
        a11_star_score = 0.0
        if alert_id == "A11":
            try:
                a11_star_score = float(evidence.get("a11_star_score") or 0.0)
            except Exception:
                a11_star_score = 0.0

        state_norm = _norm_state(state)
        if state_norm not in timeline.get(results_date, {}):
            integrity["missing_results_state"] += 1

        # Secondary horizons are fixed (see Evaluation Charter).
        max_horizon = max([decay_draws, 7, 14, 1])
        steps: List[Tuple[str, str, str]] = []
        for date, period, winner in _iter_draw_steps(
            start_date=results_date, dates=dates, winners_timeline=timeline, state_norm=state_norm, variant=variant
        ):
            steps.append((date, period, winner))
            if len(steps) >= max_horizon:
                break

        start_step = steps[0] if steps else None

        # Episode boundaries (charter semantics)
        start_when = f"{results_date} Midday" if variant != "Evening" else f"{results_date} Evening"
        expiry_when = ""
        if decay_draws > 0:
            if len(steps) >= decay_draws:
                expiry_when = f"{steps[decay_draws - 1][0]} {steps[decay_draws - 1][1]}"
            else:
                needed = decay_draws - len(steps)
                expiry_when = f"(needs {needed} more steps)"

        stable_contains = "-"
        stable_sourced = alert_id in {"A01", "A02", "A04", "A05", "A07", "A11", "A12"}
        if stable_sourced and canonical and state_key:
            stable_scores = (
                sharepack_day_dir
                / state_key
                / "stable"
                / state_key
                / f"{state_key}_stable_patterns_scores.csv"
            )
            if state_key not in stable_cache:
                stable_cache[state_key] = _load_stable_canonicals_by_section(stable_scores)
                if not stable_cache[state_key]:
                    integrity["stable_scores_missing"] += 1
            canonicals = stable_cache.get(state_key, {}).get(variant, set())
            if canonicals:
                stable_contains = "Y" if canonical in canonicals else "N"
                if stable_contains == "N":
                    integrity["stable_candidate_missing"] += 1

        def first_hit(within_steps: int) -> Tuple[Optional[int], str, str, str]:
            if within_steps <= 0:
                return None, "", "", ""
            for step_idx, (date, period, winner) in enumerate(steps[:within_steps]):
                hit_types = _match_hit_types(
                    winner=winner,
                    candidate_canon=canonical,
                    suggested=suggested,
                    implied_set=implied_set,
                    evidence=evidence,
                )
                if hit_types:
                    when = f"{date} {period}"
                    return step_idx, when, "+".join(hit_types), winner
            return None, "", "", ""

        def first_hit_any(within_variant_steps: int) -> Tuple[Optional[int], str, str, bool]:
            """
            Cross-variant diagnostic:
              - boundary is defined by the variant-faithful Nth step (time-span),
              - search any real outcome (Midday/Evening) within that time-span.
            """
            if within_variant_steps <= 0 or not start_step:
                return None, "", "", False
            boundary_known = len(steps) >= within_variant_steps
            boundary_key: Optional[Tuple[str, int]] = None
            if boundary_known:
                boundary_key = _when_key(steps[within_variant_steps - 1][0], steps[within_variant_steps - 1][1])

            out_idx = 0
            for date, period, winner in _iter_outcome_steps_from_when(
                start_date=start_step[0],
                start_period=start_step[1],
                dates=dates,
                winners_timeline=timeline,
                state_norm=state_norm,
            ):
                if boundary_key is not None and _when_key(date, period) > boundary_key:
                    break
                hit_types = _match_hit_types(
                    winner=winner,
                    candidate_canon=canonical,
                    suggested=suggested,
                    implied_set=implied_set,
                    evidence=evidence,
                )
                if hit_types:
                    when = f"{date} {period}"
                    return out_idx, when, "+".join(hit_types), boundary_known
                out_idx += 1
            return None, "", "", boundary_known

        if row_type == "PROMOTER":
            evals.append(
                EpisodeEval(
                    row_num=idx,
                    results_date=results_date,
                    start_when=start_when,
                    expiry_when=expiry_when,
                    state=state,
                    state_key=state_key,
                    variant=variant,
                    alert_id=alert_id,
                    strength=strength,
                    suggested=suggested,
                    row_type=row_type,
                    implied_set_size=implied_set_size,
                    a11_star_level=a11_star_level,
                    a11_star_score=a11_star_score,
                    cap_lines=cap_lines,
                    decay_draws=decay_draws,
                    badges=badges,
                    canonical_raw=canonical_raw,
                    canonical=canonical or "",
                    stable_contains_canonical=stable_contains,
                    evidence_ok=evidence_ok,
                    evidence_error=evidence_error,
                    strict_hit="NA",
                    strict_hit_type="",
                    strict_hit_when="",
                    status="PROMOTER",
                    time_to_hit_steps="",
                    hit_when="",
                    hit_type="",
                    hit_within_decay="NA",
                    hit_within_7="NA",
                    hit_within_14="NA",
                    hit_any_within_decay="NA",
                    hit_any_when="",
                    hit_any_type="",
                    hit_any_within_7="NA",
                    hit_any_within_14="NA",
                )
            )
            continue

        # Strict diagnostic: grade against date D only (not “next day”).
        strict_hit = "?"
        strict_type = ""
        strict_when = ""
        strict_candidates = [(results_date, "Midday"), (results_date, "Evening")]
        if variant == "Midday":
            strict_candidates = [(results_date, "Midday")]
        elif variant == "Evening":
            strict_candidates = [(results_date, "Evening")]

        any_applicable = False
        strict_hits: List[str] = []
        strict_types: set[str] = set()
        for d, period in strict_candidates:
            winner = (timeline.get(d, {}).get(state_norm, {}).get(period) or "").strip()
            if not winner:
                continue
            any_applicable = True
            hit_types = _match_hit_types(
                winner=winner,
                candidate_canon=canonical,
                suggested=suggested,
                implied_set=implied_set,
                evidence=evidence,
            )
            if hit_types:
                strict_hits.append(f"{d} {period} ({'+'.join(hit_types)})")
                strict_types.update(hit_types)
        if any_applicable:
            strict_hit = "Y" if strict_hits else "N"
            if strict_hits:
                strict_type = "+".join(sorted(strict_types))
                strict_when = "; ".join(strict_hits)
        else:
            strict_hit = "?"
            strict_when = "no results on D for variant periods"

        # Primary: per-row decay window
        decay_hit_idx, decay_when, decay_hit_type, _ = first_hit(decay_draws)
        if decay_hit_idx is not None:
            status = "HIT"
            time_to_hit_steps = str(decay_hit_idx)
            hit_when = decay_when
            hit_type = decay_hit_type
            hit_within_decay = "Y"
        else:
            if len(steps) >= max(decay_draws, 1):
                status = "EXPIRED"
                time_to_hit_steps = ""
                hit_when = ""
                hit_type = ""
                hit_within_decay = "N"
            else:
                status = "CENSORED"
                time_to_hit_steps = ""
                hit_when = ""
                hit_type = ""
                hit_within_decay = "?"

        # Secondary horizons
        def hit_within(h: int) -> str:
            if h <= 0:
                return "?"
            hit_idx, _, _, _ = first_hit(h)
            if hit_idx is not None:
                return "Y"
            return "N" if len(steps) >= h else "?"

        any_hit_idx, any_hit_when, any_hit_type, any_boundary_known = first_hit_any(decay_draws)
        if any_hit_idx is not None:
            hit_any_within_decay = "Y"
            hit_any_when = any_hit_when
            hit_any_type = any_hit_type
        else:
            hit_any_within_decay = "N" if any_boundary_known and decay_draws > 0 else "?"
            hit_any_when = ""
            hit_any_type = ""

        def hit_any_within(h: int) -> str:
            if h <= 0:
                return "?"
            hit_idx, _, _, boundary_known = first_hit_any(h)
            if hit_idx is not None:
                return "Y"
            return "N" if boundary_known else "?"

        evals.append(
            EpisodeEval(
                row_num=idx,
                results_date=results_date,
                start_when=start_when,
                expiry_when=expiry_when,
                state=state,
                state_key=state_key,
                variant=variant,
                alert_id=alert_id,
                strength=strength,
                suggested=suggested,
                row_type=row_type,
                implied_set_size=implied_set_size,
                a11_star_level=a11_star_level,
                a11_star_score=a11_star_score,
                cap_lines=cap_lines,
                decay_draws=decay_draws,
                badges=badges,
                canonical_raw=canonical_raw,
                canonical=canonical or "",
                stable_contains_canonical=stable_contains,
                evidence_ok=evidence_ok,
                evidence_error=evidence_error,
                strict_hit=strict_hit,
                strict_hit_type=strict_type,
                strict_hit_when=strict_when,
                status=status,
                time_to_hit_steps=time_to_hit_steps,
                hit_when=hit_when,
                hit_type=hit_type,
                hit_within_decay=hit_within_decay,
                hit_within_7=hit_within(7),
                hit_within_14=hit_within(14),
                hit_any_within_decay=hit_any_within_decay,
                hit_any_when=hit_any_when,
                hit_any_type=hit_any_type,
                hit_any_within_7=hit_any_within(7),
                hit_any_within_14=hit_any_within(14),
            )
        )

    merged = _merge_candidate_rows(
        results_date=results_date,
        rows=rows,
        dates=dates,
        winners_timeline=timeline,
    )
    return evals, merged, integrity


def _write_eval_csv(path: Path, rows: Sequence[EpisodeEval]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow([field.name for field in EpisodeEval.__dataclass_fields__.values()])  # type: ignore[attr-defined]
        for r in rows:
            w.writerow(
                [
                    r.row_num,
                    r.results_date,
                    r.start_when,
                    r.expiry_when,
                    r.state,
                    r.state_key,
                    r.variant,
                    r.alert_id,
                    r.strength,
                    r.suggested,
                    r.row_type,
                    r.implied_set_size,
                    r.a11_star_level,
                    r.a11_star_score,
                    r.cap_lines,
                    r.decay_draws,
                    r.badges,
                    r.canonical_raw,
                    r.canonical,
                    r.stable_contains_canonical,
                    "Y" if r.evidence_ok else "N",
                    r.evidence_error,
                    r.strict_hit,
                    r.strict_hit_type,
                    r.strict_hit_when,
                    r.status,
                    r.time_to_hit_steps,
                    r.hit_when,
                    r.hit_type,
                    r.hit_within_decay,
                    r.hit_within_7,
                    r.hit_within_14,
                    r.hit_any_within_decay,
                    r.hit_any_when,
                    r.hit_any_type,
                    r.hit_any_within_7,
                    r.hit_any_within_14,
                ]
            )


def _write_merged_csv(path: Path, rows: Sequence[MergedEpisodeEval]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow([field.name for field in MergedEpisodeEval.__dataclass_fields__.values()])  # type: ignore[attr-defined]
        for r in rows:
            w.writerow(
                [
                    r.results_date,
                    r.state,
                    r.state_key,
                    r.variant,
                    r.implied_set_size,
                    r.implied_set,
                    r.alert_ids,
                    r.suggested_kinds,
                    r.strength_max,
                    r.decay_min,
                    r.decay_max,
                    r.promoters,
                    r.status,
                    r.time_to_hit_steps,
                    r.hit_when,
                    r.hit_type,
                    r.hit_within_7,
                    r.hit_within_14,
                    r.hit_any_within_decay,
                    r.hit_any_when,
                    r.hit_any_type,
                    r.hit_any_within_7,
                    r.hit_any_within_14,
                ]
            )


def _render_scorecard(rows: Sequence[EpisodeEval]) -> List[str]:
    candidates = [r for r in rows if r.row_type != "PROMOTER"]
    promoters = [r for r in rows if r.row_type == "PROMOTER"]

    # Aggregate by alert_id (with A11 stratified by star level)
    by_id: Dict[str, Dict[str, Any]] = {}
    for r in candidates:
        key = r.alert_id or "?"
        if r.alert_id == "A11":
            key = f"A11:S{r.a11_star_level or 0}"
        entry = by_id.setdefault(
            key,
            {
                "fired": 0,
                "hit_decay": 0,
                "expired": 0,
                "censored": 0,
                "hit7": 0,
                "hit14": 0,
                "t_hit": [],
            },
        )
        entry["fired"] += 1
        if r.status == "HIT":
            entry["hit_decay"] += 1
            try:
                entry["t_hit"].append(int(r.time_to_hit_steps))
            except Exception:
                pass
        elif r.status == "EXPIRED":
            entry["expired"] += 1
        elif r.status == "CENSORED":
            entry["censored"] += 1
        if r.hit_within_7 == "Y":
            entry["hit7"] += 1
        if r.hit_within_14 == "Y":
            entry["hit14"] += 1

    def mean(values: List[int]) -> str:
        if not values:
            return "-"
        return f"{sum(values)/len(values):.2f}"

    lines: List[str] = []
    lines.append("| AlertId | Fired | HIT(decay) | EXPIRED | CENSORED | HIT<=7 | HIT<=14 | mean t_hit |")
    lines.append("|---:|---:|---:|---:|---:|---:|---:|---:|")
    for alert_id in sorted(by_id.keys()):
        e = by_id[alert_id]
        lines.append(
            f"| {alert_id} | {e['fired']} | {e['hit_decay']} | {e['expired']} | {e['censored']} | {e['hit7']} | {e['hit14']} | {mean(e['t_hit'])} |"
        )

    if promoters:
        by_pid: Dict[str, int] = {}
        for r in promoters:
            by_pid[r.alert_id or "?"] = by_pid.get(r.alert_id or "?", 0) + 1
        lines.append("")
        lines.append("Promoters fired (not gradeable as winner hits):")
        for pid in sorted(by_pid.keys()):
            lines.append(f"- {pid}: {by_pid[pid]}")
    return lines


def _render_scorecard_any(rows: Sequence[EpisodeEval]) -> List[str]:
    candidates = [r for r in rows if r.row_type != "PROMOTER"]

    by_id: Dict[str, Dict[str, Any]] = {}
    for r in candidates:
        key = r.alert_id or "?"
        if r.alert_id == "A11":
            key = f"A11:S{r.a11_star_level or 0}"
        entry = by_id.setdefault(
            key,
            {"fired": 0, "hit_decay": 0, "expired": 0, "censored": 0, "hit7": 0, "hit14": 0},
        )
        entry["fired"] += 1
        if r.hit_any_within_decay == "Y":
            entry["hit_decay"] += 1
        elif r.hit_any_within_decay == "N":
            entry["expired"] += 1
        elif r.hit_any_within_decay == "?":
            entry["censored"] += 1
        if r.hit_any_within_7 == "Y":
            entry["hit7"] += 1
        if r.hit_any_within_14 == "Y":
            entry["hit14"] += 1

    lines: List[str] = []
    lines.append("| AlertId | Fired | HIT_any(decay) | EXPIRED_any | CENSORED_any | HIT_any<=7 | HIT_any<=14 |")
    lines.append("|---:|---:|---:|---:|---:|---:|---:|")
    for alert_id in sorted(by_id.keys()):
        e = by_id[alert_id]
        lines.append(
            f"| {alert_id} | {e['fired']} | {e['hit_decay']} | {e['expired']} | {e['censored']} | {e['hit7']} | {e['hit14']} |"
        )
    return lines


def _write_eval_md(
    path: Path,
    *,
    rows: Sequence[EpisodeEval],
    merged: Sequence[MergedEpisodeEval],
    integrity: Dict[str, Any],
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

    now = datetime.now(timezone.utc).isoformat()
    results_date = rows[0].results_date if rows else "?"
    lines: List[str] = []
    lines.append(f"# Profit Alerts Evaluation — {results_date}")
    lines.append("")
    lines.append(f"- Generated: `{now}`")
    lines.append(f"- Inputs:")
    lines.append(f"  - `sharepacks/{results_date}/control_center/profit_alerts.csv`")
    lines.append(f"  - `data/results/*.txt` (local only)")
    lines.append(f"- Charter: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Profit_Alerts_Evaluation_Charter.md`")
    lines.append("")

    lines.append("## Integrity summary")
    lines.append(f"- rows_total: `{integrity.get('rows_total')}`")
    lines.append(f"- evidence_parse_errors: `{integrity.get('evidence_parse_errors')}`")
    lines.append(f"- non_3digit_canonical: `{integrity.get('non_3digit_canonical')}`")
    lines.append(f"- missing_results_state (state not found on D): `{integrity.get('missing_results_state')}`")
    lines.append(f"- stable_scores_missing (per-state Stable scores missing/unreadable): `{integrity.get('stable_scores_missing')}`")
    lines.append(f"- stable_candidate_missing (canonical not found in Stable scores section): `{integrity.get('stable_candidate_missing')}`")
    lines.append("")

    lines.append("## Scorecard (variant-faithful lens, by AlertId)")
    lines.extend(_render_scorecard(rows))
    lines.append("")

    lines.append("## Scorecard (any-outcome lens, by AlertId)")
    lines.append("")
    lines.append(
        "For `Midday` / `Evening` variant rows, this counts a hit if the episode resolves on either `Midday` or `Evening` within the same time-span boundary as the variant-faithful window."
    )
    lines.append("")
    lines.extend(_render_scorecard_any(rows))
    lines.append("")

    lines.append("## Merged episodes (deduped play-sets)")
    lines.append("")
    lines.append(
        "This view dedupes rows that imply the same concrete play-set (same `StateKey × Variant × implied_set`) so co-firing alerts do not get double-counted."
    )
    lines.append("")
    lines.append(f"- merged_rows_total: `{len(merged)}`")
    lines.append("")
    lines.append("| StateKey | Variant | Strength | Alerts | Promoters | DecayMax | Status | t_hit | HitWhen | HitType | Hit<=7 | Hit<=14 | Any(decay) | AnyWhen |")
    lines.append("|---|---|---:|---|---|---:|---|---:|---|---|---|---|---|---|")

    def m_sort_key(r: MergedEpisodeEval) -> Tuple[int, int, str, str, int]:
        status_rank = {"HIT": 0, "EXPIRED": 1, "CENSORED": 2}.get(r.status, 99)
        t_hit = int(r.time_to_hit_steps) if r.time_to_hit_steps.isdigit() else 999
        return (status_rank, -r.strength_max, r.state_key, r.variant, t_hit)

    for r in sorted(merged, key=m_sort_key)[:25]:
        t_hit = r.time_to_hit_steps if r.time_to_hit_steps else "-"
        lines.append(
            f"| {r.state_key} | {r.variant} | {r.strength_max} | {r.alert_ids or '-'} | {r.promoters or '-'} | {r.decay_max} | {r.status} | {t_hit} | {r.hit_when or '-'} | {r.hit_type or '-'} | {r.hit_within_7} | {r.hit_within_14} | {r.hit_any_within_decay} | {r.hit_any_when or '-'} |"
        )
    lines.append("")
    lines.append("Full merged evaluation:")
    lines.append(f"- `sharepacks/{results_date}/control_center/profit_alerts_eval_merged.csv`")
    lines.append("")

    lines.append("## Top episodes (by Strength, then earliest hit)")
    lines.append("")
    lines.append("| # | StateKey | Variant | AlertId | Strength | Suggested | Decay | Status | t_hit | HitWhen | HitType | Hit<=7 | Hit<=14 | Any(decay) | AnyWhen | Strict |")
    lines.append("|---:|---|---|---|---:|---|---:|---|---:|---|---|---|---|---|---|---|")

    def sort_key(r: EpisodeEval) -> Tuple[int, int, str, str, int]:
        # HIT episodes first, then strength desc, then t_hit asc
        status_rank = {"HIT": 0, "EXPIRED": 1, "CENSORED": 2}.get(r.status, 99)
        t_hit = int(r.time_to_hit_steps) if r.time_to_hit_steps.isdigit() else 999
        return (status_rank, -r.strength, r.alert_id, r.state_key, t_hit)

    top = sorted([r for r in rows if r.row_type != "PROMOTER"], key=sort_key)[:25]
    for r in top:
        t_hit = r.time_to_hit_steps if r.time_to_hit_steps else "-"
        lines.append(
            f"| {r.row_num} | {r.state_key} | {r.variant} | {r.alert_id} | {r.strength} | {r.suggested} | {r.decay_draws} | {r.status} | {t_hit} | {r.hit_when or '-'} | {r.hit_type or '-'} | {r.hit_within_7} | {r.hit_within_14} | {r.hit_any_within_decay} | {r.hit_any_when or '-'} | {r.strict_hit} |"
        )
    lines.append("")
    lines.append("Full per-row evaluation:")
    lines.append(f"- `sharepacks/{results_date}/control_center/profit_alerts_eval.csv`")
    lines.append("")

    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", required=True, help="Results date D (sharepack folder name), e.g. 2025-06-21")
    ap.add_argument("--results-dir", default="data/results", help="Directory containing YYYY-MM-DD.txt results files")
    ap.add_argument("--sharepacks-dir", default="sharepacks", help="Sharepacks root (default: sharepacks)")
    args = ap.parse_args()

    results_date = str(args.date).strip()
    results_dir = Path(args.results_dir)
    sharepacks_dir = Path(args.sharepacks_dir)
    day_dir = sharepacks_dir / results_date
    if not day_dir.exists():
        raise SystemExit(f"sharepack day folder not found: {day_dir}")
    if not results_dir.exists():
        raise SystemExit(f"results dir not found: {results_dir}")

    rows, merged, integrity = evaluate_day(
        results_date=results_date,
        sharepack_day_dir=day_dir,
        results_dir=results_dir,
    )
    cc_dir = day_dir / "control_center"
    csv_out = cc_dir / "profit_alerts_eval.csv"
    md_out = cc_dir / "profit_alerts_eval.md"
    merged_out = cc_dir / "profit_alerts_eval_merged.csv"
    _write_eval_csv(csv_out, rows)
    _write_merged_csv(merged_out, merged)
    _write_eval_md(md_out, rows=rows, merged=merged, integrity=integrity)
    print(f"Wrote: {csv_out}")
    print(f"Wrote: {merged_out}")
    print(f"Wrote: {md_out}")


if __name__ == "__main__":
    main()
