#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
SRC_ROOT = REPO_ROOT / "src"
if SRC_ROOT.exists() and str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from scripts.tools.grade_candidate_universe import (  # type: ignore
    _canon,
    _load_results_winners,
    _normalize_pick3_literal,
)


SCOREBOARD_RE = re.compile(r"(?P<date>\d{4}-\d{2}-\d{2})__BOARD_SCOREBOARD__.+\.json$")


@dataclass(frozen=True)
class WinnerEvent:
    date: str
    state_key: str
    period: str
    literal: str
    canonical: str
    vtrac_index: Optional[int]


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def read_json(path: Path) -> Any:
    return json.loads(_read_text(path))


def safe_rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def analysis_dir(window_root: Path) -> Path:
    return window_root / "ANALYSIS_ARENA"


def validation_dir(window_root: Path) -> Path:
    return window_root / "VALIDATION"


def iter_window_dates(window_root: Path) -> List[str]:
    out: List[str] = []
    for path in sorted(analysis_dir(window_root).glob("*__BOARD_SCOREBOARD__*.json")):
        m = SCOREBOARD_RE.match(path.name)
        if m:
            out.append(m.group("date"))
    return out


def results_file_for_date(*, results_root: Path, results_date: str) -> Path:
    return results_root / f"{results_date}.txt"


def winners_for_date(*, results_root: Path, results_date: str) -> Dict[str, Any]:
    return _load_results_winners(results_file_for_date(results_root=results_root, results_date=results_date))


def winner_events_for_state(*, date: str, state_key: str, winners_by_state: Dict[str, Any]) -> List[WinnerEvent]:
    winner = winners_by_state.get(state_key)
    if not winner:
        return []

    import modules.vtrac_reference as vr  # type: ignore

    events: List[WinnerEvent] = []
    for period, literal in (("Midday", winner.midday), ("Evening", winner.evening)):
        lit = _normalize_pick3_literal(literal or "")
        if not lit:
            continue
        idx = vr.get_vtrac_index(lit)
        events.append(
            WinnerEvent(
                date=date,
                state_key=state_key,
                period=period,
                literal=lit,
                canonical=_canon(lit),
                vtrac_index=idx if isinstance(idx, int) else None,
            )
        )
    return events


def load_scoreboard(window_root: Path, results_date: str) -> Dict[str, Any]:
    return read_json(analysis_dir(window_root) / f"{results_date}__BOARD_SCOREBOARD__analysis_arena_day_review.json")


def load_shadow(window_root: Path, results_date: str) -> Dict[str, Any]:
    return read_json(analysis_dir(window_root) / f"{results_date}__SHADOW_DECISION_POLICY__analysis_arena_day_review.json")


def load_translation_manifest(window_root: Path, results_date: str) -> Dict[str, Any]:
    return read_json(analysis_dir(window_root) / f"{results_date}__TRANSLATION_SANDBOX_SEED__analysis_arena_day_review.json")


def load_state_seed_from_manifest_entry(entry: Dict[str, Any]) -> Dict[str, Any]:
    seed_json = entry.get("seed_json")
    if not seed_json:
        return {}
    seed_path = (REPO_ROOT / seed_json).resolve()
    if not seed_path.exists():
        return {}
    return read_json(seed_path)


def set_from_iter(values: Iterable[str]) -> set[str]:
    return {str(v) for v in values if str(v).strip()}


def union_canonicals_from_combos(combos: Iterable[str]) -> set[str]:
    out: set[str] = set()
    for combo in combos:
        c = _canon(str(combo))
        if c:
            out.add(c)
    return out


def extract_candidate_universe_metrics(candidate_universe: Dict[str, Any], winner: WinnerEvent) -> Dict[str, bool]:
    union_combos = set_from_iter(candidate_universe.get("union_combos") or [])
    union_canonicals = union_canonicals_from_combos(union_combos)
    return {
        "cu_exact": winner.literal in union_combos,
        "cu_box": winner.canonical in union_canonicals,
    }


def extract_play_card_metrics(play_card: Dict[str, Any], winner: WinnerEvent, *, strategy_name: str) -> Dict[str, bool]:
    strategies = play_card.get("strategies") or {}
    strategy = strategies.get(strategy_name) or {}
    out: Dict[str, bool] = {}
    for budget in ("B12", "B24", "B36"):
        pack = strategy.get(budget) or {}
        combos = set_from_iter(pack.get("combos") or [])
        boxed = set_from_iter(pack.get("boxed_canonicals") or [])
        out[f"{budget.lower()}_exact"] = winner.literal in combos
        out[f"{budget.lower()}_box"] = winner.canonical in boxed
    return out


def diagnostic_membership(seed: Dict[str, Any], winner: WinnerEvent) -> Dict[str, bool]:
    brain1 = seed.get("brain1_core") or {}
    sandbox = seed.get("sandbox_hypotheses") or {}
    control_arm = seed.get("control_arm") or {}

    primary = set_from_iter(brain1.get("dominant_canonicals") or [])
    context = set_from_iter(brain1.get("context_reinforced_canonicals") or [])
    vtrac_indices = set_from_iter(brain1.get("dominant_vtrac_indices") or [])
    boxed_seed = {str(item.get("value")) for item in (sandbox.get("diagnostic_boxed_seed") or []) if isinstance(item, dict)}
    straight_seed = {str(item.get("value")) for item in (sandbox.get("diagnostic_straight_seed") or []) if isinstance(item, dict)}
    vt_box_seed = {str(item.get("value")) for item in (sandbox.get("diagnostic_vt_box_seed") or []) if isinstance(item, dict)}
    preserved_not_budgeted = set_from_iter(control_arm.get("preserved_not_budgeted_canonicals_top") or [])

    winner_vt = str(winner.vtrac_index) if winner.vtrac_index is not None else ""
    return {
        "arena_primary_box": winner.canonical in primary,
        "arena_context_box": winner.canonical in context,
        "arena_primary_vt": bool(winner_vt and winner_vt in vtrac_indices),
        "sandbox_box_seed": winner.canonical in boxed_seed,
        "sandbox_exact_seed": winner.literal in straight_seed,
        "sandbox_vt_seed": bool(winner_vt and winner_vt in vt_box_seed),
        "preserved_not_budgeted": winner.canonical in preserved_not_budgeted,
    }


def dominant_box_signal(flags: Dict[str, bool]) -> bool:
    return any(
        flags.get(k, False)
        for k in ("arena_primary_box", "arena_context_box", "sandbox_box_seed")
    )


def exact_signal(flags: Dict[str, bool]) -> bool:
    return flags.get("sandbox_exact_seed", False)
