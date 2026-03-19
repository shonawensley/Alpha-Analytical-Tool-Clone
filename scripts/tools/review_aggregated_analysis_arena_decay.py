#!/usr/bin/env python3
"""Measure frozen-snapshot decay for aggregated analysis arena artifacts.

This keeps same-day arena review separate from later-resolution measurement.
Each snapshot date/state is frozen, then its dominant arena objects and context
episodes are checked against future results for the same state.
"""

from __future__ import annotations

import argparse
import csv
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

import sys

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from modules.vtrac_reference import get_vtrac_index
from scripts.tools.grade_candidate_universe import _load_results_winners
from scripts.tools.review_aggregated_analysis_arena import (
    RUNS_DIR,
    _canon,
    _context_arena_objects,
    _load_day_meta,
    _load_or_build_arena,
    _load_winner_family_ids,
    _load_winners_for_day,
    _normalize_pick3_literal,
    _resolve_dates,
    _resolve_states,
    _safe_rel,
)


@dataclass(frozen=True)
class OutcomeEvent:
    date: str
    outcome: str
    winner: str
    canonical: str
    vtrac_index: Optional[int]
    family_id: str
    day_offset: int
    draw_offset: int


def _to_int(value: object, default: int = -1) -> int:
    try:
        text = str(value or "").strip()
        if not text:
            return int(default)
        return int(float(text))
    except Exception:
        return int(default)


def _ordered_unique(values: Iterable[str]) -> List[str]:
    out: List[str] = []
    seen = set()
    for value in values:
        text = str(value or "").strip()
        if not text or text in seen:
            continue
        seen.add(text)
        out.append(text)
    return out


def _future_dates(start_date: str, decay_days: int) -> List[str]:
    start_dt = datetime.strptime(start_date, "%Y-%m-%d").date()
    return [(start_dt + timedelta(days=offset)).isoformat() for offset in range(max(0, int(decay_days)) + 1)]


def _load_outcomes_for_state(sharepacks_root: Path, *, snapshot_date: str, state_key: str, decay_days: int) -> List[OutcomeEvent]:
    rows: List[OutcomeEvent] = []
    draw_offset = 0
    for day_offset, date in enumerate(_future_dates(snapshot_date, decay_days)):
        day_dir = sharepacks_root / date
        winners_by_state: Dict[str, Dict[str, str]]
        if day_dir.exists():
            winners_by_state = _load_winners_for_day(day_dir, date)
        else:
            parsed = _load_results_winners(REPO_ROOT / "data" / "results" / f"{date}.txt")
            winners_by_state = {}
            winner = parsed.get(state_key)
            if winner is not None:
                clean: Dict[str, str] = {}
                if winner.midday:
                    clean["Midday"] = _normalize_pick3_literal(winner.midday)
                if winner.evening:
                    clean["Evening"] = _normalize_pick3_literal(winner.evening)
                winners_by_state[state_key] = clean
        winners = winners_by_state.get(state_key) or {}
        family_ids: Dict[str, str] = {}
        if day_dir.exists() and (day_dir / state_key).exists():
            family_ids = _load_winner_family_ids(day_dir / state_key, state_key, winners)
        for outcome in ("Midday", "Evening"):
            winner = _normalize_pick3_literal(winners.get(outcome))
            if not winner:
                continue
            rows.append(
                OutcomeEvent(
                    date=date,
                    outcome=outcome,
                    winner=winner,
                    canonical=_canon(winner),
                    vtrac_index=get_vtrac_index(winner),
                    family_id=str(family_ids.get(outcome) or ""),
                    day_offset=day_offset,
                    draw_offset=draw_offset,
                )
            )
            draw_offset += 1
    return rows


def _extract_snapshot_targets(arena: Dict[str, Any]) -> Dict[str, List[str]]:
    synthesis = arena.get("arena_synthesis") if isinstance(arena.get("arena_synthesis"), dict) else {}
    context_objects = _context_arena_objects(arena)

    dominant_canonicals = [str(item.get("value") or "") for item in (synthesis.get("dominant_canonicals") or [])[:5] if isinstance(item, dict)]
    dominant_vtrac_indices = [str(item.get("value") or "") for item in (synthesis.get("dominant_vtrac_indices") or [])[:5] if isinstance(item, dict)]
    dominant_families = [str(item.get("value") or "") for item in (synthesis.get("dominant_families") or [])[:4] if isinstance(item, dict)]

    watchlist_canonicals: List[str] = []
    for item in (synthesis.get("vtrac_literal_watchlist") or [])[:5]:
        if not isinstance(item, dict):
            continue
        watchlist_canonicals.extend(str(x or "") for x in (item.get("candidate_canonicals") or [])[:4])

    profit_alert_canonicals = [
        str(row.get("canonical") or "")
        for row in ((context_objects.get("cc_profit_alert_context") or {}).get("top_alerts") or [])[:8]
        if isinstance(row, dict)
    ]

    blackapple_canonicals: List[str] = []
    for row in ((context_objects.get("aux_blackapple_context") or {}).get("control_center_top") or [])[:8]:
        if not isinstance(row, dict):
            continue
        blackapple_canonicals.extend(_canon(x) for x in (row.get("examples") or [])[:6] if _normalize_pick3_literal(x))

    due_doubles_canonicals: List[str] = []
    for payload in ((context_objects.get("aux_due_doubles_family_pressure") or {}).get("by_variant") or {}).values():
        if not isinstance(payload, dict):
            continue
        for family in (payload.get("families") or [])[:4]:
            if not isinstance(family, dict):
                continue
            due_doubles_canonicals.extend(_canon(x) for x in (family.get("examples") or [])[:4] if _normalize_pick3_literal(x))

    repeat_watch_indices: List[str] = []
    for payload in ((context_objects.get("aux_repeat_watch_context") or {}).get("aux_by_variant") or {}).values():
        if not isinstance(payload, dict):
            continue
        repeat_watch_indices.extend(str(payload.get(key)) for key in ("current_index", "last_repeat_index") if _to_int(payload.get(key), default=-1) >= 0)
    for row in ((context_objects.get("aux_repeat_watch_context") or {}).get("control_center_top") or [])[:8]:
        if not isinstance(row, dict):
            continue
        repeat_watch_indices.extend(str(row.get(key)) for key in ("current_index", "heat_index") if _to_int(row.get(key), default=-1) >= 0)

    aux_overdue_indices: List[str] = []
    aux_vtrac_pressure = context_objects.get("aux_vtrac_pressure") if isinstance(context_objects.get("aux_vtrac_pressure"), dict) else {}
    for rows in (aux_vtrac_pressure.get("overlay_top") or {}).values():
        if not isinstance(rows, list):
            continue
        aux_overdue_indices.extend(str(row.get("index")) for row in rows[:6] if isinstance(row, dict) and str(row.get("index", "")).strip())
    for rows in (aux_vtrac_pressure.get("heatboard_top") or {}).values():
        if not isinstance(rows, list):
            continue
        aux_overdue_indices.extend(str(row.get("index")) for row in rows[:6] if isinstance(row, dict) and str(row.get("index", "")).strip())

    badge_canonicals = [
        str(row.get("canonical") or "")
        for row in ((context_objects.get("aux_badge_pressure") or {}).get("top_combo_alerts") or [])[:8]
        if isinstance(row, dict)
    ]
    badge_indices: List[str] = []
    for payload in (((context_objects.get("aux_badge_pressure") or {}).get("index_pressure") or {}).get("by_variant") or {}).values():
        if not isinstance(payload, dict):
            continue
        badge_indices.extend(str(row.get("index")) for row in (payload.get("top_indices") or [])[:6] if isinstance(row, dict) and str(row.get("index", "")).strip())

    return {
        "dominant_canonicals": _ordered_unique(dominant_canonicals),
        "dominant_vtrac_indices": _ordered_unique(dominant_vtrac_indices),
        "dominant_families": _ordered_unique(dominant_families),
        "watchlist_canonicals": _ordered_unique(watchlist_canonicals),
        "profit_alert_canonicals": _ordered_unique(profit_alert_canonicals),
        "blackapple_canonicals": _ordered_unique(blackapple_canonicals),
        "due_doubles_canonicals": _ordered_unique(due_doubles_canonicals),
        "repeat_watch_indices": _ordered_unique(repeat_watch_indices),
        "aux_overdue_indices": _ordered_unique(aux_overdue_indices),
        "badge_canonicals": _ordered_unique(badge_canonicals),
        "badge_indices": _ordered_unique(badge_indices),
    }


def _first_match(
    outcomes: Sequence[OutcomeEvent],
    *,
    canonicals: Optional[Sequence[str]] = None,
    indices: Optional[Sequence[str]] = None,
    families: Optional[Sequence[str]] = None,
) -> Optional[OutcomeEvent]:
    canon_set = {str(x) for x in (canonicals or []) if str(x).strip()}
    idx_set = {str(x) for x in (indices or []) if str(x).strip()}
    fam_set = {str(x) for x in (families or []) if str(x).strip()}
    for event in outcomes:
        if canon_set and event.canonical in canon_set:
            return event
        if idx_set and event.vtrac_index is not None and str(event.vtrac_index) in idx_set:
            return event
        if fam_set and event.family_id and event.family_id in fam_set:
            return event
    return None


def _hit_fields(prefix: str, event: Optional[OutcomeEvent]) -> Dict[str, str]:
    return {
        f"{prefix}_hit": "1" if event is not None else "0",
        f"{prefix}_day_offset": str(event.day_offset) if event is not None else "",
        f"{prefix}_draw_offset": str(event.draw_offset) if event is not None else "",
        f"{prefix}_event": f"{event.date} {event.outcome} {event.winner}" if event is not None else "",
        f"{prefix}_same_day": "1" if event is not None and event.day_offset == 0 else "0",
        f"{prefix}_within_1d": "1" if event is not None and event.day_offset <= 1 else "0",
        f"{prefix}_within_3d": "1" if event is not None and event.day_offset <= 3 else "0",
        f"{prefix}_within_7d": "1" if event is not None and event.day_offset <= 7 else "0",
    }


def build_decay_rows(
    *,
    sharepacks_root: Path,
    dates: Sequence[str],
    states: Sequence[str],
    profile: str,
    experiment_tag: str,
    build_missing: bool,
    rebuild: bool,
    top_items: int,
    decay_days: int,
) -> List[Dict[str, str]]:
    rows: List[Dict[str, str]] = []
    for date in dates:
        day_dir = sharepacks_root / date
        if not day_dir.exists():
            continue
        meta = _load_day_meta(day_dir)
        state_keys = _resolve_states(day_dir, meta, states)
        for state_key in state_keys:
            state_dir = day_dir / state_key
            if not state_dir.exists():
                continue
            arena, arena_path = _load_or_build_arena(
                sharepacks_root=sharepacks_root,
                day_dir=day_dir,
                state_key=state_key,
                profile=profile,
                experiment_tag=experiment_tag,
                build_missing=build_missing or rebuild,
                rebuild=rebuild,
                top_items=top_items,
            )
            if arena is None:
                continue
            targets = _extract_snapshot_targets(arena)
            outcomes = _load_outcomes_for_state(sharepacks_root, snapshot_date=date, state_key=state_key, decay_days=decay_days)

            dominant_canonical_event = _first_match(outcomes, canonicals=targets["dominant_canonicals"])
            watchlist_event = _first_match(outcomes, canonicals=targets["watchlist_canonicals"])
            dominant_vtrac_event = _first_match(outcomes, indices=targets["dominant_vtrac_indices"])
            dominant_family_event = _first_match(outcomes, families=targets["dominant_families"])
            profit_alert_event = _first_match(outcomes, canonicals=targets["profit_alert_canonicals"])
            blackapple_event = _first_match(outcomes, canonicals=targets["blackapple_canonicals"])
            due_doubles_event = _first_match(outcomes, canonicals=targets["due_doubles_canonicals"])
            repeat_watch_event = _first_match(outcomes, indices=targets["repeat_watch_indices"])
            aux_overdue_event = _first_match(outcomes, indices=targets["aux_overdue_indices"])
            badge_canonical_event = _first_match(outcomes, canonicals=targets["badge_canonicals"])
            badge_index_event = _first_match(outcomes, indices=targets["badge_indices"])

            row = {
                "snapshot_date": date,
                "state_key": state_key,
                "future_draws_observed": str(len(outcomes)),
                "arena_path": _safe_rel(arena_path) if arena_path else "",
                "dominant_canonicals": ",".join(targets["dominant_canonicals"][:6]),
                "dominant_vtrac_indices": ",".join(targets["dominant_vtrac_indices"][:6]),
                "dominant_families": ",".join(targets["dominant_families"][:6]),
                "watchlist_canonicals": ",".join(targets["watchlist_canonicals"][:10]),
                "profit_alert_active": "1" if targets["profit_alert_canonicals"] else "0",
                "blackapple_active": "1" if targets["blackapple_canonicals"] else "0",
                "due_doubles_active": "1" if targets["due_doubles_canonicals"] else "0",
                "repeat_watch_active": "1" if targets["repeat_watch_indices"] else "0",
                "aux_overdue_active": "1" if targets["aux_overdue_indices"] else "0",
                "badge_active": "1" if targets["badge_canonicals"] or targets["badge_indices"] else "0",
            }
            row.update(_hit_fields("dominant_canonical_box", dominant_canonical_event))
            row.update(_hit_fields("watchlist_box", watchlist_event))
            row.update(_hit_fields("dominant_vtrac", dominant_vtrac_event))
            row.update(_hit_fields("dominant_family", dominant_family_event))
            row.update(_hit_fields("profit_alert_box", profit_alert_event))
            row.update(_hit_fields("blackapple_box", blackapple_event))
            row.update(_hit_fields("due_doubles_box", due_doubles_event))
            row.update(_hit_fields("repeat_watch_vtrac", repeat_watch_event))
            row.update(_hit_fields("aux_overdue_vtrac", aux_overdue_event))
            row.update(_hit_fields("badge_box", badge_canonical_event))
            row.update(_hit_fields("badge_vtrac", badge_index_event))
            rows.append(row)
    return rows


def _fieldnames() -> List[str]:
    base = [
        "snapshot_date",
        "state_key",
        "future_draws_observed",
        "arena_path",
        "dominant_canonicals",
        "dominant_vtrac_indices",
        "dominant_families",
        "watchlist_canonicals",
        "profit_alert_active",
        "blackapple_active",
        "due_doubles_active",
        "repeat_watch_active",
        "aux_overdue_active",
        "badge_active",
    ]
    metric_prefixes = [
        "dominant_canonical_box",
        "watchlist_box",
        "dominant_vtrac",
        "dominant_family",
        "profit_alert_box",
        "blackapple_box",
        "due_doubles_box",
        "repeat_watch_vtrac",
        "aux_overdue_vtrac",
        "badge_box",
        "badge_vtrac",
    ]
    for prefix in metric_prefixes:
        base.extend(
            [
                f"{prefix}_hit",
                f"{prefix}_day_offset",
                f"{prefix}_draw_offset",
                f"{prefix}_event",
                f"{prefix}_same_day",
                f"{prefix}_within_1d",
                f"{prefix}_within_3d",
                f"{prefix}_within_7d",
            ]
        )
    return base


def _write_csv(path: Path, rows: List[Dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=_fieldnames())
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def _window_summary(rows: Sequence[Dict[str, str]], active_field: Optional[str], hit_field: str) -> str:
    scoped = [row for row in rows if active_field is None or row.get(active_field) == "1"]
    if not scoped:
        return "0/0"
    hits = sum(1 for row in scoped if row.get(hit_field) == "1")
    return f"{hits}/{len(scoped)}"


def build_decay_markdown(*, rows: List[Dict[str, str]], score_path: Path, label: str, decay_days: int) -> str:
    lines = [
        f"# Aggregated Analysis Arena Decay Review — {label}",
        "",
        "Purpose: freeze each arena snapshot, then measure whether its dominant objects and context episodes resolve over future draws.",
        "",
        "## Summary",
        "",
        f"- scoreboard_csv: `{_safe_rel(score_path)}`",
        f"- snapshot_rows: `{len(rows)}`",
        f"- decay_days: `{decay_days}`",
        f"- dominant_canonical_box <=1d: `{_window_summary(rows, None, 'dominant_canonical_box_within_1d')}`",
        f"- dominant_canonical_box <=3d: `{_window_summary(rows, None, 'dominant_canonical_box_within_3d')}`",
        f"- watchlist_box <=1d: `{_window_summary(rows, None, 'watchlist_box_within_1d')}`",
        f"- watchlist_box <=3d: `{_window_summary(rows, None, 'watchlist_box_within_3d')}`",
        f"- dominant_vtrac <=1d: `{_window_summary(rows, None, 'dominant_vtrac_within_1d')}`",
        f"- dominant_vtrac <=3d: `{_window_summary(rows, None, 'dominant_vtrac_within_3d')}`",
        f"- dominant_family <=1d: `{_window_summary(rows, None, 'dominant_family_within_1d')}`",
        f"- dominant_family <=3d: `{_window_summary(rows, None, 'dominant_family_within_3d')}`",
        "",
        "## Context Episodes",
        "",
        f"- profit_alert_box <=3d: `{_window_summary(rows, 'profit_alert_active', 'profit_alert_box_within_3d')}`",
        f"- blackapple_box <=3d: `{_window_summary(rows, 'blackapple_active', 'blackapple_box_within_3d')}`",
        f"- due_doubles_box <=3d: `{_window_summary(rows, 'due_doubles_active', 'due_doubles_box_within_3d')}`",
        f"- repeat_watch_vtrac <=3d: `{_window_summary(rows, 'repeat_watch_active', 'repeat_watch_vtrac_within_3d')}`",
        f"- aux_overdue_vtrac <=3d: `{_window_summary(rows, 'aux_overdue_active', 'aux_overdue_vtrac_within_3d')}`",
        f"- badge_box <=3d: `{_window_summary(rows, 'badge_active', 'badge_box_within_3d')}`",
        f"- badge_vtrac <=3d: `{_window_summary(rows, 'badge_active', 'badge_vtrac_within_3d')}`",
        "",
        "## Earliest Conversions",
        "",
        "| Snapshot | State | Dominant Canonical | Watchlist | Dominant VTRAC | Profit Alerts | Aux Overdue |",
        "|---|---|---|---|---|---|---|",
    ]
    ranked = sorted(
        rows,
        key=lambda row: (
            999 if not str(row.get("dominant_vtrac_day_offset") or "").isdigit() else int(row["dominant_vtrac_day_offset"]),
            999 if not str(row.get("watchlist_box_day_offset") or "").isdigit() else int(row["watchlist_box_day_offset"]),
            row.get("snapshot_date", ""),
            row.get("state_key", ""),
        ),
    )
    for row in ranked[:20]:
        lines.append(
            f"| {row.get('snapshot_date','')} | {row.get('state_key','')} | {row.get('dominant_canonical_box_event') or '-'} | {row.get('watchlist_box_event') or '-'} | {row.get('dominant_vtrac_event') or '-'} | {row.get('profit_alert_box_event') or '-'} | {row.get('aux_overdue_vtrac_event') or '-'} |"
        )
    return "\n".join(lines).rstrip() + "\n"


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Measure frozen-snapshot decay for aggregated analysis arena artifacts.")
    ap.add_argument("--sharepacks-root", default="sharepacks")
    ap.add_argument("--date")
    ap.add_argument("--dates", nargs="*")
    ap.add_argument("--start")
    ap.add_argument("--end")
    ap.add_argument("--states", nargs="*", default=[])
    ap.add_argument("--profile", default="tool_only")
    ap.add_argument("--experiment-tag", default="arena_v0")
    ap.add_argument("--build-missing", action="store_true")
    ap.add_argument("--rebuild", action="store_true")
    ap.add_argument("--top-items", type=int, default=12)
    ap.add_argument("--decay-days", type=int, default=3)
    ap.add_argument("--out-prefix")
    return ap.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    sharepacks_root = Path(args.sharepacks_root)
    if not sharepacks_root.is_absolute():
        sharepacks_root = (REPO_ROOT / sharepacks_root).resolve()

    dates = _resolve_dates(sharepacks_root, args)
    rows = build_decay_rows(
        sharepacks_root=sharepacks_root,
        dates=dates,
        states=args.states,
        profile=args.profile,
        experiment_tag=args.experiment_tag,
        build_missing=args.build_missing,
        rebuild=args.rebuild,
        top_items=int(args.top_items),
        decay_days=int(args.decay_days),
    )
    if not rows:
        raise SystemExit("No decay rows produced.")

    prefix = args.out_prefix or (
        f"{dates[0]}__AGGREGATED_ANALYSIS_ARENA__DECAY_D{int(args.decay_days)}"
        if len(dates) == 1
        else f"{dates[0]}_to_{dates[-1]}__AGGREGATED_ANALYSIS_ARENA__DECAY_D{int(args.decay_days)}"
    )
    score_path = RUNS_DIR / f"{prefix}.csv"
    md_path = RUNS_DIR / f"{prefix}.md"
    _write_csv(score_path, rows)
    md_path.write_text(build_decay_markdown(rows=rows, score_path=score_path, label=prefix, decay_days=int(args.decay_days)), encoding="utf-8")
    print(f"[ok] scoreboard -> {_safe_rel(score_path)}")
    print(f"[ok] memo -> {_safe_rel(md_path)}")
    print(f"[ok] rows -> {len(rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
