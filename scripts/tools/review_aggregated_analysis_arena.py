#!/usr/bin/env python3
"""Review aggregated analysis arena artifacts against frozen winners.

This harness is the first arena-native review scoreboard. It grades what the
arena preserved, compares that with current downstream consumers, and classifies
the miss layer without collapsing everything into ticket-only outcomes.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from modules.vtrac_reference import get_vtrac_index
from scripts.tools.build_aggregated_analysis_arena import (
    _default_out_name,
    build_aggregated_analysis_arena_payload,
    write_aggregated_analysis_arena_files,
)
from scripts.tools.grade_candidate_universe import _load_results_winners


RUNS_DIR = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"


@dataclass(frozen=True)
class WinnerRecord:
    date: str
    state_key: str
    outcome: str
    winner: str


def _read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8", errors="replace"))


def _safe_rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _normalize_pick3_literal(value: object) -> str:
    digits = "".join(ch for ch in str(value or "") if ch.isdigit())
    if not digits:
        return ""
    digits = digits.zfill(3) if len(digits) <= 3 else digits
    return digits if len(digits) == 3 else ""


def _canon(value: object) -> str:
    digits = _normalize_pick3_literal(value)
    return "".join(sorted(digits)) if digits else ""


def _to_int(value: object, default: int = 0) -> int:
    try:
        text = str(value or "").strip()
        if not text:
            return int(default)
        return int(float(text))
    except Exception:
        return int(default)


def _to_float(value: object, default: float = 0.0) -> float:
    try:
        text = str(value or "").strip()
        if not text:
            return float(default)
        return float(text)
    except Exception:
        return float(default)


def _section_sort_key(value: str) -> Tuple[int, str]:
    order = {"Combined": 0, "Midday": 1, "Evening": 2}
    title = str(value or "").strip().title()
    return (order.get(title, 99), title)


def _daterange(start: str, end: str) -> List[str]:
    start_dt = datetime.strptime(start, "%Y-%m-%d").date()
    end_dt = datetime.strptime(end, "%Y-%m-%d").date()
    out: List[str] = []
    current = start_dt
    while current <= end_dt:
        out.append(current.isoformat())
        current += timedelta(days=1)
    return out


def _load_day_meta(day_dir: Path) -> Dict[str, Any]:
    meta_path = day_dir / "control_center" / "meta.json"
    if meta_path.exists():
        raw = _read_json(meta_path)
        if isinstance(raw, dict):
            return raw
    return {}


def _resolve_dates(sharepacks_root: Path, args: argparse.Namespace) -> List[str]:
    if args.dates:
        return [str(d).strip() for d in args.dates if str(d).strip()]
    if args.start and args.end:
        return [d for d in _daterange(args.start, args.end) if (sharepacks_root / d).exists()]
    if args.date:
        return [args.date]
    raise SystemExit("Provide --date, --dates, or --start/--end")


def _resolve_states(day_dir: Path, meta: Dict[str, Any], states: Sequence[str]) -> List[str]:
    if states:
        return [str(s).strip() for s in states if str(s).strip()]
    meta_states = [
        str(row.get("state_key") or "").strip()
        for row in (meta.get("states") or [])
        if isinstance(row, dict) and str(row.get("state_key") or "").strip()
    ]
    if meta_states:
        return meta_states
    return sorted(path.name for path in day_dir.iterdir() if path.is_dir() and path.name != "control_center")


def _load_winners_for_day(day_dir: Path, date: str) -> Dict[str, Dict[str, str]]:
    meta = _load_day_meta(day_dir)
    winners_by_state: Dict[str, Dict[str, str]] = {}
    for row in (meta.get("states") or []):
        if not isinstance(row, dict):
            continue
        state_key = str(row.get("state_key") or "").strip()
        winners = row.get("winners")
        if state_key and isinstance(winners, dict):
            clean = {}
            for label, value in winners.items():
                winner = _normalize_pick3_literal(value)
                if label in {"Midday", "Evening"} and winner:
                    clean[label] = winner
            winners_by_state[state_key] = clean
    if winners_by_state:
        return winners_by_state

    results_file = REPO_ROOT / "data" / "results" / f"{date}.txt"
    parsed = _load_results_winners(results_file)
    for state_key, winner in parsed.items():
        clean: Dict[str, str] = {}
        if winner.midday:
            clean["Midday"] = _normalize_pick3_literal(winner.midday)
        if winner.evening:
            clean["Evening"] = _normalize_pick3_literal(winner.evening)
        winners_by_state[state_key] = clean
    return winners_by_state


def _load_winner_family_ids(state_dir: Path, state_key: str, winners: Dict[str, str]) -> Dict[str, str]:
    metrics_path = state_dir / "stable" / state_key / f"{state_key}_metrics.json"
    if not metrics_path.exists():
        return {}
    raw = _read_json(metrics_path)
    if not isinstance(raw, dict):
        return {}
    fam_ids = [str(x) for x in (raw.get("winner_family_ids") or []) if str(x).strip()]
    out: Dict[str, str] = {}
    if len(fam_ids) == 1 and len(winners) == 1:
        only_label = next(iter(winners.keys()))
        out[only_label] = fam_ids[0]
        return out
    if len(fam_ids) >= 1 and "Midday" in winners:
        out["Midday"] = fam_ids[0]
    if len(fam_ids) >= 2 and "Evening" in winners:
        out["Evening"] = fam_ids[1]
    return out


def _load_or_build_arena(
    *,
    sharepacks_root: Path,
    day_dir: Path,
    state_key: str,
    profile: str,
    experiment_tag: str,
    build_missing: bool,
    rebuild: bool,
    top_items: int,
) -> Tuple[Optional[Dict[str, Any]], Optional[Path]]:
    state_dir = day_dir / state_key
    arena_path = state_dir / "analysis" / _default_out_name(profile, experiment_tag)
    history_date = str((_load_day_meta(day_dir) or {}).get("history_date") or "").strip() or None
    if rebuild or (build_missing and not arena_path.exists()):
        payload = build_aggregated_analysis_arena_payload(
            day_dir=day_dir,
            state_key=state_key,
            results_date=day_dir.name,
            history_date=history_date,
            profile=profile,
            experiment_tag=experiment_tag,
            sharepacks_root=sharepacks_root,
            repo_root=REPO_ROOT,
            top_items=top_items,
        )
        write_aggregated_analysis_arena_files(out_json_path=arena_path, payload=payload, write_md=True)
        return payload, arena_path
    if arena_path.exists():
        raw = _read_json(arena_path)
        if isinstance(raw, dict):
            return raw, arena_path
    return None, None


def _rank_map(items: Sequence[Dict[str, Any]], key: str) -> Dict[str, int]:
    out: Dict[str, int] = {}
    for idx, item in enumerate(items, start=1):
        value = item.get(key)
        if value is None:
            continue
        out[str(value)] = idx
    return out


def _recursive_contains_exact(value: Any, target: str) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return value == target
    if isinstance(value, list):
        return any(_recursive_contains_exact(item, target) for item in value)
    if isinstance(value, dict):
        return any(_recursive_contains_exact(item, target) for item in value.values())
    return False


def _recursive_collect_indices(value: Any) -> set[str]:
    found: set[str] = set()
    if isinstance(value, dict):
        for key, item in value.items():
            key_text = str(key)
            if key_text in {"index", "vtrac_index", "index_hint", "current_index", "heat_index"}:
                if isinstance(item, (int, float)) and 0 <= int(item) <= 119:
                    found.add(str(int(item)))
                elif isinstance(item, str) and item.strip().isdigit():
                    num = int(item.strip())
                    if 0 <= num <= 119:
                        found.add(str(num))
            else:
                found.update(_recursive_collect_indices(item))
    elif isinstance(value, list):
        for item in value:
            found.update(_recursive_collect_indices(item))
    return found


def _recursive_collect_family_ids(value: Any) -> set[str]:
    found: set[str] = set()
    if isinstance(value, dict):
        for key, item in value.items():
            key_text = str(key)
            if key_text in {"family_id", "stable_family_id"}:
                text = str(item or "").strip()
                if text:
                    found.add(text)
            elif key_text == "family_ids" and isinstance(item, list):
                for entry in item:
                    text = str(entry or "").strip()
                    if text:
                        found.add(text)
            else:
                found.update(_recursive_collect_family_ids(item))
    elif isinstance(value, list):
        for item in value:
            found.update(_recursive_collect_family_ids(item))
    return found


def _winner_presence_any(payload: Dict[str, Any], winner_canon: str, winner_idx: Optional[int], winner_family_id: Optional[str]) -> Dict[str, bool]:
    searchable = {
        "string_tools": payload.get("string_tools") or {},
        "context_tools": payload.get("context_tools") or {},
        "cross_tool_relations": payload.get("cross_tool_relations") or {},
        "arena_synthesis": payload.get("arena_synthesis") or {},
    }
    present_canon = _recursive_contains_exact(searchable, winner_canon)
    indices = _recursive_collect_indices(searchable)
    families = _recursive_collect_family_ids(searchable)
    return {
        "canonical_any_present": present_canon,
        "vtrac_any_present": bool(winner_idx is not None and str(winner_idx) in indices),
        "family_any_present": bool(winner_family_id and winner_family_id in families),
    }


def _context_presence_for_winner(payload: Dict[str, Any], winner_canon: str, winner_idx: Optional[int], winner_family_id: Optional[str]) -> Dict[str, bool]:
    synthesis = payload.get("arena_synthesis") if isinstance(payload.get("arena_synthesis"), dict) else {}
    reinforced = synthesis.get("context_reinforced_canonicals") if isinstance(synthesis.get("context_reinforced_canonicals"), list) else []
    context_only = synthesis.get("context_only_pressure") if isinstance(synthesis.get("context_only_pressure"), list) else []
    vtrac_consensus = (payload.get("cross_tool_relations") or {}).get("vtrac_index_consensus_top")
    family_consensus = (payload.get("cross_tool_relations") or {}).get("family_consensus_top")
    return {
        "winner_canonical_context_reinforced": any(str(item.get("value")) == winner_canon for item in reinforced if isinstance(item, dict)),
        "winner_canonical_context_only": any(str(item.get("value")) == winner_canon for item in context_only if isinstance(item, dict)),
        "winner_vtrac_context_reinforced": any(
            str(item.get("value")) == str(winner_idx) and int(item.get("context_source_count") or 0) > 0
            for item in (vtrac_consensus or [])
            if isinstance(item, dict) and winner_idx is not None
        ),
        "winner_family_context_reinforced": any(
            str(item.get("value")) == str(winner_family_id) and int(item.get("context_source_count") or 0) > 0
            for item in (family_consensus or [])
            if isinstance(item, dict) and winner_family_id
        ),
    }


def _load_candidate_universe_presence(state_dir: Path, winner: str, winner_canon: str, winner_idx: Optional[int]) -> Dict[str, Any]:
    path = state_dir / "candidate_universe__tool_only.json"
    if not path.exists():
        return {"available": False}
    raw = _read_json(path)
    if not isinstance(raw, dict):
        return {"available": False}
    union = [_normalize_pick3_literal(x) for x in (raw.get("union_combos") or []) if _normalize_pick3_literal(x)]
    union_set = set(union)
    boxed = {_canon(x) for x in union_set}
    return {
        "available": True,
        "path": _safe_rel(path),
        "union_combos_count": len(union_set),
        "straight_present": winner in union_set,
        "box_present": winner_canon in boxed,
        "vtrac_present": bool(winner_idx is not None and any(get_vtrac_index(combo) == winner_idx for combo in union_set)),
    }


def _load_play_card_presence(state_dir: Path, winner: str, winner_canon: str, winner_idx: Optional[int]) -> Dict[str, Any]:
    path = state_dir / "play_card__tool_only.json"
    if not path.exists():
        return {"available": False}
    raw = _read_json(path)
    if not isinstance(raw, dict):
        return {"available": False}
    ranked = raw.get("ranked_candidates") if isinstance(raw.get("ranked_candidates"), list) else []
    straight_rank = None
    box_rank = None
    vtrac_rank = None
    for idx, row in enumerate(ranked, start=1):
        if not isinstance(row, dict):
            continue
        combo = _normalize_pick3_literal(row.get("combo") or row.get("candidate"))
        canonical = str(row.get("canonical") or _canon(combo))
        if straight_rank is None and combo == winner:
            straight_rank = idx
        if box_rank is None and canonical == winner_canon:
            box_rank = idx
        if vtrac_rank is None and winner_idx is not None and combo and get_vtrac_index(combo) == winner_idx:
            vtrac_rank = idx
    return {
        "available": True,
        "path": _safe_rel(path),
        "ranked_candidate_count": len(ranked),
        "straight_present": straight_rank is not None,
        "box_present": box_rank is not None,
        "vtrac_present": vtrac_rank is not None,
        "straight_rank": straight_rank,
        "box_rank": box_rank,
        "vtrac_rank": vtrac_rank,
    }


def _gap_class(
    *,
    play_card: Dict[str, Any],
    candidate_universe: Dict[str, Any],
    arena_canon_rank: Optional[int],
    arena_any: Dict[str, bool],
    arena_vtrac_rank: Optional[int],
    arena_family_rank: Optional[int],
) -> str:
    if bool(play_card.get("straight_present") or play_card.get("box_present")):
        return "downstream_present"
    if bool(candidate_universe.get("straight_present") or candidate_universe.get("box_present")):
        return "budget_gap"
    if arena_canon_rank is not None or arena_any["canonical_any_present"]:
        return "arena_present_but_underweighted"
    if arena_vtrac_rank is not None or arena_family_rank is not None or arena_any["vtrac_any_present"] or arena_any["family_any_present"]:
        return "conversion_gap"
    return "arena_missing"


def _build_rows_for_state(
    *,
    date: str,
    state_key: str,
    state_dir: Path,
    arena: Dict[str, Any],
    arena_path: Optional[Path],
    winners: Dict[str, str],
    winner_family_ids: Dict[str, str],
) -> List[Dict[str, str]]:
    relations = arena.get("cross_tool_relations") if isinstance(arena.get("cross_tool_relations"), dict) else {}
    synthesis = arena.get("arena_synthesis") if isinstance(arena.get("arena_synthesis"), dict) else {}
    canonical_rank = _rank_map(relations.get("canonical_consensus_top") or [], "value")
    vtrac_rank = _rank_map(relations.get("vtrac_index_consensus_top") or [], "value")
    family_rank = _rank_map(relations.get("family_consensus_top") or [], "value")

    rows: List[Dict[str, str]] = []
    regime_flags = ",".join(str(x) for x in (relations.get("regime_flags") or []) if str(x))
    contradiction_flags = ",".join(str(x) for x in (relations.get("contradiction_flags") or []) if str(x))
    dominant_canonical = str((synthesis.get("state_regime") or {}).get("dominant_canonical") or "")
    dominant_vtrac = str((synthesis.get("state_regime") or {}).get("dominant_vtrac_index") or "")
    dominant_family = str((synthesis.get("state_regime") or {}).get("dominant_family") or "")

    for outcome in ("Midday", "Evening"):
        winner = _normalize_pick3_literal(winners.get(outcome))
        if not winner:
            continue
        winner_canon = _canon(winner)
        winner_idx = get_vtrac_index(winner)
        winner_family_id = winner_family_ids.get(outcome)

        any_presence = _winner_presence_any(arena, winner_canon, winner_idx, winner_family_id)
        context_presence = _context_presence_for_winner(arena, winner_canon, winner_idx, winner_family_id)
        cu = _load_candidate_universe_presence(state_dir, winner, winner_canon, winner_idx)
        pc = _load_play_card_presence(state_dir, winner, winner_canon, winner_idx)

        arena_canon_rank = canonical_rank.get(winner_canon)
        arena_vtrac_rank = vtrac_rank.get(str(winner_idx)) if winner_idx is not None else None
        arena_family_consensus_rank = family_rank.get(str(winner_family_id)) if winner_family_id else None

        row = {
            "date": date,
            "state_key": state_key,
            "outcome": outcome,
            "winner": winner,
            "winner_canonical": winner_canon,
            "winner_vtrac_index": str(winner_idx) if winner_idx is not None else "",
            "winner_family_id": str(winner_family_id or ""),
            "arena_canonical_rank": str(arena_canon_rank or ""),
            "arena_vtrac_rank": str(arena_vtrac_rank or ""),
            "arena_family_rank": str(arena_family_consensus_rank or ""),
            "arena_canonical_any_present": "1" if any_presence["canonical_any_present"] else "0",
            "arena_vtrac_any_present": "1" if any_presence["vtrac_any_present"] else "0",
            "arena_family_any_present": "1" if any_presence["family_any_present"] else "0",
            "winner_canonical_context_reinforced": "1" if context_presence["winner_canonical_context_reinforced"] else "0",
            "winner_vtrac_context_reinforced": "1" if context_presence["winner_vtrac_context_reinforced"] else "0",
            "winner_family_context_reinforced": "1" if context_presence["winner_family_context_reinforced"] else "0",
            "winner_canonical_context_only": "1" if context_presence["winner_canonical_context_only"] else "0",
            "candidate_universe_straight_present": "1" if cu.get("straight_present") else "0",
            "candidate_universe_box_present": "1" if cu.get("box_present") else "0",
            "candidate_universe_vtrac_present": "1" if cu.get("vtrac_present") else "0",
            "candidate_universe_union_count": str(cu.get("union_combos_count") or 0),
            "play_card_straight_present": "1" if pc.get("straight_present") else "0",
            "play_card_box_present": "1" if pc.get("box_present") else "0",
            "play_card_vtrac_present": "1" if pc.get("vtrac_present") else "0",
            "play_card_straight_rank": str(pc.get("straight_rank") or ""),
            "play_card_box_rank": str(pc.get("box_rank") or ""),
            "play_card_vtrac_rank": str(pc.get("vtrac_rank") or ""),
            "gap_class": _gap_class(
                play_card=pc,
                candidate_universe=cu,
                arena_canon_rank=arena_canon_rank,
                arena_any=any_presence,
                arena_vtrac_rank=arena_vtrac_rank,
                arena_family_rank=arena_family_consensus_rank,
            ),
            "arena_dominant_canonical": dominant_canonical,
            "arena_dominant_vtrac_index": dominant_vtrac,
            "arena_dominant_family": dominant_family,
            "arena_regime_flags": regime_flags,
            "arena_contradiction_flags": contradiction_flags,
            "arena_path": _safe_rel(arena_path) if arena_path else "",
        }
        rows.append(row)
    return rows


def _csv_fieldnames() -> List[str]:
    return [
        "date",
        "state_key",
        "outcome",
        "winner",
        "winner_canonical",
        "winner_vtrac_index",
        "winner_family_id",
        "arena_canonical_rank",
        "arena_vtrac_rank",
        "arena_family_rank",
        "arena_canonical_any_present",
        "arena_vtrac_any_present",
        "arena_family_any_present",
        "winner_canonical_context_reinforced",
        "winner_vtrac_context_reinforced",
        "winner_family_context_reinforced",
        "winner_canonical_context_only",
        "candidate_universe_straight_present",
        "candidate_universe_box_present",
        "candidate_universe_vtrac_present",
        "candidate_universe_union_count",
        "play_card_straight_present",
        "play_card_box_present",
        "play_card_vtrac_present",
        "play_card_straight_rank",
        "play_card_box_rank",
        "play_card_vtrac_rank",
        "gap_class",
        "arena_dominant_canonical",
        "arena_dominant_vtrac_index",
        "arena_dominant_family",
        "arena_regime_flags",
        "arena_contradiction_flags",
        "arena_path",
    ]


def _write_csv(path: Path, rows: List[Dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=_csv_fieldnames())
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def _summary_markdown(*, rows: List[Dict[str, str]], score_path: Path, label: str) -> str:
    gap_counts = Counter(row["gap_class"] for row in rows)
    total = len(rows)

    def _truth_count(field: str) -> int:
        return sum(1 for row in rows if row.get(field) == "1")

    def _rank_hits(field: str, ceiling: int) -> int:
        total_hits = 0
        for row in rows:
            text = str(row.get(field) or "").strip()
            if text.isdigit() and int(text) <= ceiling:
                total_hits += 1
        return total_hits

    lines = [
        f"# Aggregated Analysis Arena Review — {label}",
        "",
        "Purpose: score the aggregated arena itself against frozen winners, then compare that with current downstream Candidate Universe / Play Card behavior.",
        "",
        "## Summary",
        "",
        f"- scoreboard_csv: `{_safe_rel(score_path)}`",
        f"- outcome_rows: `{total}`",
        f"- arena canonical any-present: `{_truth_count('arena_canonical_any_present')}/{total}`",
        f"- arena VTRAC any-present: `{_truth_count('arena_vtrac_any_present')}/{total}`",
        f"- arena family any-present: `{_truth_count('arena_family_any_present')}/{total}`",
        f"- arena context-reinforced any: `{sum(1 for row in rows if row.get('winner_canonical_context_reinforced') == '1' or row.get('winner_vtrac_context_reinforced') == '1' or row.get('winner_family_context_reinforced') == '1')}/{total}`",
        f"- arena VTRAC top3: `{_rank_hits('arena_vtrac_rank', 3)}/{total}`",
        f"- arena VTRAC top5: `{_rank_hits('arena_vtrac_rank', 5)}/{total}`",
        f"- candidate_universe any present: `{sum(1 for row in rows if row.get('candidate_universe_straight_present') == '1' or row.get('candidate_universe_box_present') == '1' or row.get('candidate_universe_vtrac_present') == '1')}/{total}`",
        f"- candidate_universe straight/box present: `{sum(1 for row in rows if row.get('candidate_universe_straight_present') == '1' or row.get('candidate_universe_box_present') == '1')}/{total}`",
        f"- play_card any present: `{sum(1 for row in rows if row.get('play_card_straight_present') == '1' or row.get('play_card_box_present') == '1' or row.get('play_card_vtrac_present') == '1')}/{total}`",
        f"- play_card straight/box present: `{sum(1 for row in rows if row.get('play_card_straight_present') == '1' or row.get('play_card_box_present') == '1')}/{total}`",
        "",
        "## Gap Classes",
        "",
    ]
    for key, count in sorted(gap_counts.items()):
        lines.append(f"- {key}: `{count}`")

    lines.extend(["", "## Notable Rows", "", "| Date | State | Outcome | Winner | Canon Rank | VTRAC Rank | Family Rank | Context Reinforced | CU | Play Card | Gap |", "|---|---|---|---|---:|---:|---:|---|---|---|---|"])
    ranked = sorted(
        rows,
        key=lambda row: (
            999 if not str(row.get("arena_vtrac_rank") or "").isdigit() else int(row["arena_vtrac_rank"]),
            999 if not str(row.get("arena_canonical_rank") or "").isdigit() else int(row["arena_canonical_rank"]),
            row.get("date", ""),
            row.get("state_key", ""),
            row.get("outcome", ""),
        ),
    )
    for row in ranked[:20]:
        context_flag = "Y" if (row.get("winner_canonical_context_reinforced") == "1" or row.get("winner_vtrac_context_reinforced") == "1") else "N"
        cu_flag = "Y" if (row.get("candidate_universe_straight_present") == "1" or row.get("candidate_universe_box_present") == "1") else "N"
        pc_flag = "Y" if (row.get("play_card_straight_present") == "1" or row.get("play_card_box_present") == "1") else "N"
        lines.append(
            f"| {row['date']} | {row['state_key']} | {row['outcome']} | {row['winner']} | {row['arena_canonical_rank'] or '-'} | {row['arena_vtrac_rank'] or '-'} | {row['arena_family_rank'] or '-'} | {context_flag} | {cu_flag} | {pc_flag} | {row['gap_class']} |"
        )
    return "\n".join(lines).rstrip() + "\n"


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Review aggregated analysis arena artifacts against winners.")
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
    ap.add_argument("--out-prefix")
    return ap.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    sharepacks_root = Path(args.sharepacks_root)
    if not sharepacks_root.is_absolute():
        sharepacks_root = (REPO_ROOT / sharepacks_root).resolve()

    dates = _resolve_dates(sharepacks_root, args)
    all_rows: List[Dict[str, str]] = []

    for date in dates:
        day_dir = sharepacks_root / date
        if not day_dir.exists():
            continue
        meta = _load_day_meta(day_dir)
        winners_by_state = _load_winners_for_day(day_dir, date)
        for state_key in _resolve_states(day_dir, meta, args.states):
            state_dir = day_dir / state_key
            if not state_dir.exists():
                continue
            arena, arena_path = _load_or_build_arena(
                sharepacks_root=sharepacks_root,
                day_dir=day_dir,
                state_key=state_key,
                profile=args.profile,
                experiment_tag=args.experiment_tag,
                build_missing=args.build_missing or args.rebuild,
                rebuild=args.rebuild,
                top_items=int(args.top_items),
            )
            if arena is None:
                print(f"[skip] missing arena for {date} {state_key}")
                continue
            winners = winners_by_state.get(state_key) or {}
            if not winners:
                continue
            winner_family_ids = _load_winner_family_ids(state_dir, state_key, winners)
            all_rows.extend(
                _build_rows_for_state(
                    date=date,
                    state_key=state_key,
                    state_dir=state_dir,
                    arena=arena,
                    arena_path=arena_path,
                    winners=winners,
                    winner_family_ids=winner_family_ids,
                )
            )

    if not all_rows:
        raise SystemExit("No review rows produced.")

    prefix = args.out_prefix or (
        f"{dates[0]}__AGGREGATED_ANALYSIS_ARENA__REVIEW"
        if len(dates) == 1
        else f"{dates[0]}_to_{dates[-1]}__AGGREGATED_ANALYSIS_ARENA__REVIEW"
    )
    score_path = RUNS_DIR / f"{prefix}.csv"
    md_path = RUNS_DIR / f"{prefix}.md"
    _write_csv(score_path, all_rows)
    md_path.write_text(_summary_markdown(rows=all_rows, score_path=score_path, label=prefix), encoding="utf-8")
    print(f"[ok] scoreboard -> {_safe_rel(score_path)}")
    print(f"[ok] memo -> {_safe_rel(md_path)}")
    print(f"[ok] rows -> {len(all_rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
