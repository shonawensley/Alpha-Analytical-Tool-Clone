#!/usr/bin/env python3
"""Create a post-run evidence-utilization audit for an Analysis Arena window.

This report is intentionally downstream/read-only. It joins completed window
artifacts and asks whether winner-relevant evidence was captured, promoted, and
converted, without changing prediction or cadence logic.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.tools.analysis_arena_window_utils import (  # type: ignore
    iter_window_dates,
    load_scoreboard,
    load_state_seed_from_manifest_entry,
    load_translation_manifest,
    safe_rel,
)
from scripts.tools.grade_candidate_universe import _canon  # type: ignore


WINDOW_RE = re.compile(r"WINDOW_(?P<start>\d{4}-\d{2}-\d{2})_to_(?P<end>\d{4}-\d{2}-\d{2})$")
BOOL_TRUE = {"1", "true", "yes", "y"}
PROFILE_HIT = {"direct_same_outcome", "same_day_precursor_plus_same_day", "same_day_carryforward", "future_day_decay"}


@dataclass(frozen=True)
class BoolSignalSpec:
    field: str
    source_family: str
    source_tool: str
    tier: str
    target_lane: str
    match_mode: str
    promoted_stage: str


@dataclass(frozen=True)
class SignalValue:
    source_family: str
    source_tool: str
    source_path: str
    value: str
    value_kind: str
    rank: str = ""
    raw_score: str = ""
    normalized_score: str = ""
    badge_or_alert: str = ""
    support_count: str = ""
    source_tags: str = ""
    promoted_stage: str = ""


BOOL_SIGNAL_SPECS: List[BoolSignalSpec] = [
    BoolSignalSpec("arena_primary_box", "arena", "brain1_dominant_canonicals", "A", "boxed", "BOX", "arena"),
    BoolSignalSpec("arena_context_box", "arena", "brain1_context_canonicals", "A", "boxed", "BOX", "arena"),
    BoolSignalSpec("arena_primary_vt", "arena", "brain1_dominant_vtrac", "B", "vtrac", "VTRAC_BOX", "arena"),
    BoolSignalSpec("sandbox_box_seed", "translation_sandbox", "diagnostic_boxed_seed", "A", "boxed", "BOX", "arena"),
    BoolSignalSpec("sandbox_exact_seed", "translation_sandbox", "diagnostic_straight_seed", "A", "straight", "EXACT", "arena"),
    BoolSignalSpec("sandbox_vt_seed", "translation_sandbox", "diagnostic_vt_seed", "B", "vtrac", "VTRAC_BOX", "arena"),
    BoolSignalSpec("preserved_not_budgeted", "control_arm", "preserved_not_budgeted", "B", "boxed", "BOX", "control"),
    BoolSignalSpec("arena_box_signal", "arena", "arena_box_rollup", "A", "boxed", "BOX", "arena"),
    BoolSignalSpec("arena_exact_signal", "arena", "arena_exact_rollup", "A", "straight", "EXACT", "arena"),
    BoolSignalSpec("cu_exact", "old_candidate_universe", "candidate_universe_exact", "B", "straight", "EXACT", "candidate_universe"),
    BoolSignalSpec("cu_box", "old_candidate_universe", "candidate_universe_box", "B", "boxed", "BOX", "candidate_universe"),
    BoolSignalSpec("play_card_any_exact", "old_play_card", "play_card_exact_any", "A", "straight", "EXACT", "play_card"),
    BoolSignalSpec("play_card_any_box", "old_play_card", "play_card_box_any", "A", "boxed", "BOX", "play_card"),
    BoolSignalSpec("b12_exact", "old_play_card", "play_card_b12_exact", "A", "straight", "EXACT", "play_card"),
    BoolSignalSpec("b12_box", "old_play_card", "play_card_b12_box", "A", "boxed", "BOX", "play_card"),
    BoolSignalSpec("b24_exact", "old_play_card", "play_card_b24_exact", "A", "straight", "EXACT", "play_card"),
    BoolSignalSpec("b24_box", "old_play_card", "play_card_b24_box", "A", "boxed", "BOX", "play_card"),
    BoolSignalSpec("b36_exact", "old_play_card", "play_card_b36_exact", "A", "straight", "EXACT", "play_card"),
    BoolSignalSpec("b36_box", "old_play_card", "play_card_b36_box", "A", "boxed", "BOX", "play_card"),
    BoolSignalSpec("profit_alert_direct_match", "tracker", "profit_alert_direct_match", "A", "boxed", "BOX", "tracker"),
    BoolSignalSpec("profit_alert_implied_match", "tracker", "profit_alert_implied_match", "A", "boxed", "BOX", "tracker"),
    BoolSignalSpec("compound_event_present", "tracker", "compound_event_present", "B", "context", "CONTEXT", "tracker"),
    BoolSignalSpec("profit_alert_support", "tracker", "profit_alert_support", "C", "context", "CONTEXT", "tracker"),
    BoolSignalSpec("compound_event_support", "tracker", "compound_event_support", "C", "context", "CONTEXT", "tracker"),
    BoolSignalSpec("due_double_support", "tracker", "due_double_support", "C", "context", "CONTEXT", "tracker"),
    BoolSignalSpec("blackapple_support", "tracker", "blackapple_support", "C", "context", "CONTEXT", "tracker"),
    BoolSignalSpec("positional_support", "tracker", "positional_support", "C", "context", "CONTEXT", "tracker"),
    BoolSignalSpec("r_consensus_support", "tracker", "r_consensus_support", "C", "context", "CONTEXT", "tracker"),
    BoolSignalSpec("survivor_support", "tracker", "survivor_support", "C", "context", "CONTEXT", "tracker"),
]


DECAY_SPECS = [
    ("board_top_box_core", "board_top_box_values", "board_scoreboard", "top_canonicals", "B", "boxed", "canonical"),
    ("board_top_vt_core", "board_top_vt_values", "board_scoreboard", "top_vtrac_indices", "B", "vtrac", "vtrac_index"),
    ("brain1_box_core", "brain1_box_values", "brain1", "box_core", "B", "boxed", "canonical"),
    ("brain1_vt_core", "brain1_vt_values", "brain1", "vtrac_core", "B", "vtrac", "vtrac_index"),
    ("sandbox_box_seed", "sandbox_box_values", "translation_sandbox", "boxed_seed", "A", "boxed", "canonical"),
    ("sandbox_exact_seed", "sandbox_exact_values", "translation_sandbox", "straight_seed", "A", "straight", "literal"),
    ("sandbox_vt_seed", "sandbox_vt_values", "translation_sandbox", "vt_seed", "B", "vtrac", "vtrac_index"),
    ("preserved_not_budgeted", "preserved_values", "control_arm", "preserved", "B", "boxed", "canonical"),
    ("arena_box_total", "arena_box_total_values", "arena", "box_total", "B", "boxed", "canonical"),
    ("arena_vt_total", "arena_vt_total_values", "arena", "vtrac_total", "B", "vtrac", "vtrac_index"),
]


def _parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--window-root", required=True, help="RUNS_2 window root.")
    ap.add_argument(
        "--final-docs-dir",
        default=str(REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "final docs"),
        help="Directory for repeatable protocol docs.",
    )
    ap.add_argument("--case-limit", type=int, default=30, help="Maximum deep case dossiers to render.")
    ap.add_argument("--force", action="store_true", help="Overwrite existing audit outputs.")
    return ap.parse_args()


def _resolve_path(value: str) -> Path:
    path = Path(value).expanduser()
    if not path.is_absolute():
        path = (REPO_ROOT / path).resolve()
    return path


def _read_csv_rows(path: Path) -> List[Dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", errors="replace", newline="") as fh:
        return [{k: (v or "") for k, v in row.items()} for row in csv.DictReader(fh)]


def _write_text(path: Path, text: str, *, force: bool) -> None:
    if path.exists() and not force:
        raise SystemExit(f"Refusing to overwrite existing file without --force: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _write_json(path: Path, payload: Any, *, force: bool) -> None:
    _write_text(path, json.dumps(payload, indent=2, sort_keys=True) + "\n", force=force)


def _write_csv(path: Path, rows: Sequence[Dict[str, Any]], *, force: bool) -> None:
    if path.exists() and not force:
        raise SystemExit(f"Refusing to overwrite existing file without --force: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames: List[str] = []
    for row in rows:
        for key in row.keys():
            if key not in fieldnames:
                fieldnames.append(key)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def _truthy(value: Any) -> bool:
    return str(value or "").strip().lower() in BOOL_TRUE


def _safe_int(value: Any, default: int = 0) -> int:
    try:
        text = str(value or "").strip()
        if not text:
            return default
        return int(float(text))
    except Exception:
        return default


def _safe_float(value: Any, default: float = 0.0) -> float:
    try:
        text = str(value or "").strip()
        if not text:
            return default
        return float(text)
    except Exception:
        return default


def _pct(count: int, total: int) -> str:
    return f"{100.0 * count / total:.1f}%" if total else "0.0%"


def _rate(count: int, total: int) -> float:
    return count / total if total else 0.0


def _digits_only(value: Any) -> str:
    return "".join(ch for ch in str(value or "") if ch.isdigit())


def _split_pipe(value: Any) -> List[str]:
    return [part.strip() for part in str(value or "").split("|") if part.strip()]


def _split_csvish(value: Any) -> List[str]:
    raw = str(value or "").strip()
    if not raw or raw == "-":
        return []
    return [part.strip() for part in re.split(r"[|, ]+", raw) if part.strip() and part.strip() != "-"]


def _ordered_unique(values: Iterable[str]) -> List[str]:
    out: List[str] = []
    seen: set[str] = set()
    for value in values:
        text = str(value or "").strip()
        if not text or text in seen:
            continue
        seen.add(text)
        out.append(text)
    return out


def _event_key(row: Dict[str, str]) -> Tuple[str, str, str, str]:
    return (
        str(row.get("date") or "").strip(),
        str(row.get("state_key") or row.get("state") or "").strip(),
        str(row.get("period") or "").strip(),
        str(row.get("winner") or "").strip(),
    )


def _frontier_key(row: Dict[str, str]) -> Tuple[str, str, str]:
    return (
        str(row.get("date") or "").strip(),
        str(row.get("state_key") or "").strip(),
        str(row.get("winner") or "").strip(),
    )


def _event_id(row: Dict[str, Any]) -> str:
    return f"{row.get('date', '')}|{row.get('state_key', '')}|{row.get('period', '')}|{row.get('winner', '')}"


def _vtrac_pattern(draw: str) -> str:
    import modules.vtrac_reference as vr  # type: ignore

    out: List[str] = []
    for ch in _digits_only(draw):
        mapped = vr.DIGIT2V.get(ch)
        if mapped is not None:
            out.append(str(mapped))
    return "".join(out)


def _vtrac_index(value: str) -> str:
    import modules.vtrac_reference as vr  # type: ignore

    literal = _digits_only(value)
    if len(literal) != 3:
        return ""
    idx = vr.get_vtrac_index(literal)
    return str(idx) if isinstance(idx, int) else ""


def _match_value(value: str, value_kind: str, event: Dict[str, Any]) -> Dict[str, Any]:
    clean = _digits_only(value)
    winner = _digits_only(event.get("winner"))
    winner_canon = str(event.get("winner_canonical") or _canon(winner) or "")
    winner_vt_index = str(event.get("winner_vtrac_index") or "").strip()
    winner_vt_pattern = _vtrac_pattern(winner)

    exact = False
    box = False
    vt_straight = False
    vt_box = False

    if value_kind == "literal":
        exact = clean == winner
        box = bool(clean and _canon(clean) == winner_canon)
        vt_straight = bool(clean and _vtrac_pattern(clean) == winner_vt_pattern)
        vt_box = bool(clean and _vtrac_index(clean) == winner_vt_index)
    elif value_kind == "canonical":
        canon = _canon(clean) if len(clean) == 3 else clean
        box = bool(canon and canon == winner_canon)
        vt_box = bool(canon and _vtrac_index(canon) == winner_vt_index)
    elif value_kind == "vtrac_index":
        vt_box = str(value).strip() == winner_vt_index
    elif value_kind == "vtrac_pattern":
        pattern = "".join(ch for ch in str(value or "") if ch.isdigit())
        vt_straight = bool(pattern and pattern == winner_vt_pattern)
        vt_box = bool(pattern and sorted(pattern) == sorted(winner_vt_pattern))

    modes: List[str] = []
    if exact:
        modes.append("EXACT")
    if box:
        modes.append("BOX")
    if vt_straight:
        modes.append("VTRAC_STRAIGHT")
    if vt_box:
        modes.append("VTRAC_BOX")

    best = ""
    for mode in ("EXACT", "BOX", "VTRAC_STRAIGHT", "VTRAC_BOX"):
        if mode in modes:
            best = mode
            break
    return {
        "match_exact": exact,
        "match_box": box,
        "match_vtrac_straight": vt_straight,
        "match_vtrac_box": vt_box,
        "match_best_mode": best,
        "matched_any": bool(modes),
        "match_modes": "|".join(modes),
    }


def _outcome_class(row: Dict[str, str]) -> str:
    if _truthy(row.get("opportunity_gap_exact")):
        return "EXACT_GAP"
    if _truthy(row.get("opportunity_gap_box")):
        return "BOX_GAP"
    if _truthy(row.get("play_straight_hit")) or _truthy(row.get("play_card_any_exact")):
        return "STRAIGHT"
    if _truthy(row.get("play_box_strict_hit")):
        return "STRICT_BOX"
    if _truthy(row.get("play_box_any_hit")) or _truthy(row.get("play_card_any_box")):
        return "BOX_ANY"
    if _truthy(row.get("play_vtrac_only_hit")) or str(row.get("hit_class") or "").upper() == "VTRAC_ONLY":
        return "VTRAC_ONLY"
    if _truthy(row.get("candidate_hit_any")):
        return "CANDIDATE_ONLY"
    return "NO_CONVERSION"


def _sharp_signal_count(row: Dict[str, str]) -> int:
    fields = [
        "arena_box_signal",
        "arena_exact_signal",
        "arena_primary_box",
        "sandbox_box_seed",
        "sandbox_exact_seed",
        "profit_alert_direct_match",
        "profit_alert_implied_match",
    ]
    return sum(1 for field in fields if _truthy(row.get(field)))


def _territory_signal_count(row: Dict[str, str]) -> int:
    fields = [
        "arena_primary_vt",
        "sandbox_vt_seed",
        "preserved_not_budgeted",
        "cu_box",
        "cu_exact",
    ]
    return sum(1 for field in fields if _truthy(row.get(field)))


def _broad_context_count(row: Dict[str, str]) -> int:
    fields = [
        "profit_alert_support",
        "compound_event_support",
        "due_double_support",
        "blackapple_support",
        "positional_support",
        "r_consensus_support",
        "survivor_support",
    ]
    return sum(1 for field in fields if _truthy(row.get(field)))


def _frontier_quality(frontier: Dict[str, str]) -> str:
    strength = str(frontier.get("signature_strength") or frontier.get("frontier_signature_strength") or "").strip().upper()
    signature = str(frontier.get("frontier_signature_type") or "").strip().upper()
    score = _safe_float(frontier.get("frontier_strength_score"))
    if signature in {"LITERAL_FRONTIER", "FAMILY_FRONTIER"} or strength == "STRONG" or score >= 68:
        return "sharp_frontier"
    if signature:
        return "territory_frontier"
    return ""


def _evidence_status(row: Dict[str, str], decay: Dict[str, str], frontier: Dict[str, str]) -> str:
    sharp = _sharp_signal_count(row)
    territory = _territory_signal_count(row)
    broad = _broad_context_count(row)
    play_exact = _truthy(row.get("play_card_any_exact")) or _truthy(row.get("play_straight_hit"))
    play_box = _truthy(row.get("play_card_any_box")) or _truthy(row.get("play_box_any_hit"))
    vt_only = _truthy(row.get("play_vtrac_only_hit")) or str(row.get("hit_class") or "").upper() == "VTRAC_ONLY"
    decay_profile = str(decay.get("arena_any_signal_profile") or "")
    frontier_q = _frontier_quality(frontier)

    if _truthy(row.get("opportunity_gap_exact")) or _truthy(row.get("opportunity_gap_box")):
        return "CAPTURED_BUT_UNDERUSED"
    if (play_exact or play_box) and (sharp or territory):
        return "CAPTURED_AND_USED"
    if vt_only and territory and not (play_exact or play_box):
        return "CAPTURED_BUT_WRONG_LANE"
    if decay_profile == "future_day_decay":
        return "DECAY_VALIDATED"
    if sharp or territory or frontier_q:
        return "CAPTURED_BUT_NOT_PROMOTED"
    if broad:
        return "BROAD_CONTEXT_ONLY"
    return "NOT_CAPTURED"


def _default_paths(window_root: Path, final_docs_dir: Path) -> Dict[str, Path]:
    stem = window_root.name
    prefix = f"{stem}__ANALYSIS_ARENA"
    return {
        "perf": window_root / f"{prefix}__PERFORMANCE_GAP__ledger.csv",
        "hit_roster": window_root / f"{prefix}__HIT_ROSTER.csv",
        "translator": window_root / f"{prefix}__TRANSLATOR_LEARNING_LEDGER.csv",
        "frontier": window_root / f"{prefix}__C1_C2_FRONTIER_CASES.csv",
        "decay": window_root / f"{prefix}__DECAY_CARRYOVER_ROWS.csv",
        "audit_md": window_root / f"{prefix}__EVIDENCE_UTILIZATION_AUDIT.md",
        "audit_json": window_root / f"{prefix}__EVIDENCE_UTILIZATION_AUDIT.json",
        "util_csv": window_root / f"{prefix}__EVIDENCE_UTILIZATION_LEDGER.csv",
        "signal_csv": window_root / f"{prefix}__WINNER_SIGNAL_ATTRIBUTION_LEDGER.csv",
        "signal_md": window_root / f"{prefix}__WINNER_SIGNAL_ATTRIBUTION_SCORECARD.md",
        "case_md": window_root / f"{prefix}__CASE_DOSSIERS.md",
        "redesign_md": window_root / f"{prefix}__TRANSLATOR_REDESIGN_LESSONS.md",
        "dictionary_md": window_root / f"{prefix}__SIGNAL_SOURCE_DICTIONARY.md",
        "protocol_md": final_docs_dir / "AAT9_ANALYSIS_ARENA__POST_RUN_AUDIT_PROTOCOL.md",
    }


def _load_lookup(rows: Sequence[Dict[str, str]], key_fn) -> Dict[Any, Dict[str, str]]:
    return {key_fn(row): row for row in rows}


def _load_scoreboard_rows(window_root: Path, dates: Sequence[str]) -> Dict[Tuple[str, str], Dict[str, Any]]:
    out: Dict[Tuple[str, str], Dict[str, Any]] = {}
    for date in dates:
        try:
            scoreboard = load_scoreboard(window_root, date)
        except Exception:
            continue
        for row in scoreboard.get("scoreboard_rows") or []:
            if not isinstance(row, dict):
                continue
            state_key = str(row.get("state_key") or "").strip()
            if state_key:
                out[(date, state_key)] = row
    return out


def _load_seed_rows(window_root: Path, dates: Sequence[str]) -> Dict[Tuple[str, str], Dict[str, Any]]:
    out: Dict[Tuple[str, str], Dict[str, Any]] = {}
    for date in dates:
        try:
            manifest = load_translation_manifest(window_root, date)
        except Exception:
            continue
        for entry in manifest.get("state_receipts") or []:
            if not isinstance(entry, dict):
                continue
            state_key = str(entry.get("state_key") or "").strip()
            if not state_key:
                continue
            seed = load_state_seed_from_manifest_entry(entry)
            if isinstance(seed, dict) and seed:
                out[(date, state_key)] = seed
    return out


def _append_list_values(
    signals: List[SignalValue],
    values: Iterable[Any],
    *,
    source_family: str,
    source_tool: str,
    source_path: str,
    value_kind: str,
    promoted_stage: str,
) -> None:
    for idx, value in enumerate(values, start=1):
        text = str(value or "").strip()
        if not text:
            continue
        signals.append(
            SignalValue(
                source_family=source_family,
                source_tool=source_tool,
                source_path=source_path,
                value=text,
                value_kind=value_kind,
                rank=str(idx),
                promoted_stage=promoted_stage,
            )
        )


def _append_dict_values(
    signals: List[SignalValue],
    values: Iterable[Any],
    *,
    source_family: str,
    source_tool: str,
    source_path: str,
    value_key: str,
    value_kind: str,
    promoted_stage: str,
) -> None:
    for idx, item in enumerate(values, start=1):
        if not isinstance(item, dict):
            continue
        text = str(item.get(value_key) or "").strip()
        if not text:
            continue
        tags = item.get("source_tags") or item.get("why_tags") or item.get("support_methods") or item.get("tags") or []
        if isinstance(tags, list):
            tag_text = "|".join(str(tag) for tag in tags if str(tag).strip())
        else:
            tag_text = str(tags or "")
        score = item.get("score", "")
        if not score:
            score = item.get("support_packs", "")
        signals.append(
            SignalValue(
                source_family=source_family,
                source_tool=source_tool,
                source_path=source_path,
                value=text,
                value_kind=value_kind,
                rank=str(idx),
                raw_score=str(score or ""),
                badge_or_alert=str(item.get("alert_id") or item.get("badges") or ""),
                support_count=str(item.get("support_count") or item.get("support_packs_count") or item.get("support_packs") or ""),
                source_tags=tag_text,
                promoted_stage=promoted_stage,
            )
        )


def _signals_from_seed(seed: Dict[str, Any], scoreboard_row: Dict[str, Any]) -> List[SignalValue]:
    signals: List[SignalValue] = []
    _append_list_values(
        signals,
        scoreboard_row.get("top_canonicals") or [],
        source_family="board_scoreboard",
        source_tool="top_canonicals",
        source_path="scoreboard_rows.top_canonicals",
        value_kind="canonical",
        promoted_stage="brain2_board",
    )
    _append_list_values(
        signals,
        scoreboard_row.get("top_vtrac_indices") or [],
        source_family="board_scoreboard",
        source_tool="top_vtrac_indices",
        source_path="scoreboard_rows.top_vtrac_indices",
        value_kind="vtrac_index",
        promoted_stage="brain2_board",
    )

    brain1 = seed.get("brain1_core") or {}
    _append_list_values(signals, brain1.get("dominant_canonicals") or [], source_family="brain1", source_tool="dominant_canonicals", source_path="brain1_core.dominant_canonicals", value_kind="canonical", promoted_stage="arena")
    _append_list_values(signals, brain1.get("context_reinforced_canonicals") or [], source_family="brain1", source_tool="context_reinforced_canonicals", source_path="brain1_core.context_reinforced_canonicals", value_kind="canonical", promoted_stage="arena")
    _append_list_values(signals, brain1.get("secondary_canonicals") or [], source_family="brain1", source_tool="secondary_canonicals", source_path="brain1_core.secondary_canonicals", value_kind="canonical", promoted_stage="arena")
    _append_list_values(signals, brain1.get("survivor_frontier_canonicals") or [], source_family="survivor", source_tool="survivor_frontier_canonicals", source_path="brain1_core.survivor_frontier_canonicals", value_kind="canonical", promoted_stage="arena")
    _append_list_values(signals, brain1.get("survivor_last_remaining_canonicals") or [], source_family="survivor", source_tool="survivor_last_remaining_canonicals", source_path="brain1_core.survivor_last_remaining_canonicals", value_kind="canonical", promoted_stage="arena")
    _append_list_values(signals, brain1.get("dominant_vtrac_indices") or [], source_family="brain1", source_tool="dominant_vtrac_indices", source_path="brain1_core.dominant_vtrac_indices", value_kind="vtrac_index", promoted_stage="arena")
    _append_list_values(signals, brain1.get("watchlist_indices") or [], source_family="brain1", source_tool="watchlist_indices", source_path="brain1_core.watchlist_indices", value_kind="vtrac_index", promoted_stage="arena")

    brain2 = seed.get("brain2_context") or {}
    _append_list_values(signals, brain2.get("blackapple_recommended_canonicals") or [], source_family="blackapple", source_tool="recommended_canonicals", source_path="brain2_context.blackapple_recommended_canonicals", value_kind="canonical", promoted_stage="tracker")
    _append_list_values(signals, brain2.get("due_double_example_canonicals") or [], source_family="due_doubles", source_tool="example_canonicals", source_path="brain2_context.due_double_example_canonicals", value_kind="canonical", promoted_stage="tracker")
    _append_list_values(signals, brain2.get("profit_alert_implied_canonicals") or [], source_family="profit_alerts", source_tool="implied_canonicals", source_path="brain2_context.profit_alert_implied_canonicals", value_kind="canonical", promoted_stage="tracker")
    _append_dict_values(signals, brain2.get("top_profit_alerts") or [], source_family="profit_alerts", source_tool="top_profit_alerts", source_path="brain2_context.top_profit_alerts", value_key="canonical", value_kind="canonical", promoted_stage="tracker")
    _append_dict_values(signals, brain2.get("positional_shortlist_top") or [], source_family="positional", source_tool="positional_combo", source_path="brain2_context.positional_shortlist_top.combo", value_key="combo", value_kind="literal", promoted_stage="tracker")
    _append_dict_values(signals, brain2.get("positional_shortlist_top") or [], source_family="positional", source_tool="positional_canonical", source_path="brain2_context.positional_shortlist_top.canonical", value_key="canonical", value_kind="canonical", promoted_stage="tracker")

    sandbox = seed.get("sandbox_hypotheses") or {}
    _append_dict_values(signals, sandbox.get("diagnostic_boxed_seed") or [], source_family="translation_sandbox", source_tool="diagnostic_boxed_seed", source_path="sandbox_hypotheses.diagnostic_boxed_seed", value_key="value", value_kind="canonical", promoted_stage="arena")
    _append_dict_values(signals, sandbox.get("diagnostic_straight_seed") or [], source_family="translation_sandbox", source_tool="diagnostic_straight_seed", source_path="sandbox_hypotheses.diagnostic_straight_seed", value_key="value", value_kind="literal", promoted_stage="arena")
    _append_dict_values(signals, sandbox.get("diagnostic_vt_box_seed") or [], source_family="translation_sandbox", source_tool="diagnostic_vt_box_seed", source_path="sandbox_hypotheses.diagnostic_vt_box_seed", value_key="value", value_kind="vtrac_index", promoted_stage="arena")

    control = seed.get("control_arm") or {}
    cu = control.get("candidate_universe") or {}
    play_card = control.get("play_card") or {}
    _append_dict_values(signals, cu.get("top_canonicals") or [], source_family="old_candidate_universe", source_tool="top_canonicals", source_path="control_arm.candidate_universe.top_canonicals", value_key="canonical", value_kind="canonical", promoted_stage="candidate_universe")
    for pack_idx, pack in enumerate(cu.get("top_packs") or [], start=1):
        if not isinstance(pack, dict):
            continue
        for idx, value in enumerate(pack.get("canonicals") or [], start=1):
            signals.append(
                SignalValue(
                    source_family="old_candidate_universe",
                    source_tool=f"pack:{pack.get('method_id') or pack.get('pack_id') or 'unknown'}",
                    source_path="control_arm.candidate_universe.top_packs",
                    value=str(value),
                    value_kind="canonical",
                    rank=f"{pack_idx}.{idx}",
                    badge_or_alert=str(pack.get("play_mode") or ""),
                    source_tags="|".join(str(tag) for tag in (pack.get("why_tags") or []) if str(tag).strip()),
                    promoted_stage="candidate_universe",
                )
            )
    _append_list_values(signals, play_card.get("budgeted_canonicals_top") or [], source_family="old_play_card", source_tool="budgeted_canonicals_top", source_path="control_arm.play_card.budgeted_canonicals_top", value_kind="canonical", promoted_stage="play_card")
    _append_dict_values(signals, play_card.get("ranked_candidates_top") or [], source_family="old_play_card", source_tool="ranked_candidate_combo", source_path="control_arm.play_card.ranked_candidates_top.combo", value_key="combo", value_kind="literal", promoted_stage="play_card")
    _append_dict_values(signals, play_card.get("ranked_candidates_top") or [], source_family="old_play_card", source_tool="ranked_candidate_canonical", source_path="control_arm.play_card.ranked_candidates_top.canonical", value_key="canonical", value_kind="canonical", promoted_stage="play_card")
    for card in play_card.get("strategy_cards") or []:
        if not isinstance(card, dict):
            continue
        budget = str(card.get("budget_id") or "")
        strategy = str(card.get("strategy_id") or "")
        for idx, value in enumerate(card.get("boxed_canonicals_top") or [], start=1):
            signals.append(
                SignalValue(
                    source_family="old_play_card",
                    source_tool=f"strategy_card:{strategy}:{budget}",
                    source_path="control_arm.play_card.strategy_cards.boxed_canonicals_top",
                    value=str(value),
                    value_kind="canonical",
                    rank=str(idx),
                    badge_or_alert=budget,
                    promoted_stage="play_card",
                )
            )

    shadow = seed.get("shadow_decision_policy") or {}
    focus = shadow.get("candidate_focus") or {}
    primary_cluster = focus.get("primary_cluster") or {}
    _append_list_values(signals, primary_cluster.get("canonicals") or [], source_family="shadow_policy", source_tool="primary_cluster_canonicals", source_path="shadow_decision_policy.candidate_focus.primary_cluster.canonicals", value_kind="canonical", promoted_stage="shadow")
    _append_list_values(signals, primary_cluster.get("context_reinforced_canonicals") or [], source_family="shadow_policy", source_tool="primary_cluster_context", source_path="shadow_decision_policy.candidate_focus.primary_cluster.context_reinforced_canonicals", value_kind="canonical", promoted_stage="shadow")
    _append_list_values(signals, primary_cluster.get("survivor_frontier_canonicals") or [], source_family="shadow_policy", source_tool="primary_cluster_survivor_frontier", source_path="shadow_decision_policy.candidate_focus.primary_cluster.survivor_frontier_canonicals", value_kind="canonical", promoted_stage="shadow")

    return signals


def _field_attribution_rows(event: Dict[str, str]) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for spec in BOOL_SIGNAL_SPECS:
        if not _truthy(event.get(spec.field)):
            continue
        rows.append(
            {
                "event_id": _event_id(event),
                "date": event.get("date", ""),
                "state_key": event.get("state_key", ""),
                "period": event.get("period", ""),
                "winner": event.get("winner", ""),
                "winner_canonical": event.get("winner_canonical", ""),
                "winner_vtrac_index": event.get("winner_vtrac_index", ""),
                "source_family": spec.source_family,
                "source_tool": spec.source_tool,
                "source_path": f"event_field.{spec.field}",
                "signal_id": spec.field,
                "signal_value": "TRUE",
                "signal_value_kind": "boolean_alignment",
                "signal_rank": "",
                "raw_score": "",
                "normalized_score": "",
                "badge_or_alert": "",
                "support_count": "",
                "source_tags": "",
                "tier": spec.tier,
                "target_lane": spec.target_lane,
                "pre_draw_available": "True",
                "match_exact": str(spec.match_mode == "EXACT"),
                "match_box": str(spec.match_mode == "BOX"),
                "match_vtrac_straight": str(spec.match_mode == "VTRAC_STRAIGHT"),
                "match_vtrac_box": str(spec.match_mode == "VTRAC_BOX"),
                "match_best_mode": spec.match_mode,
                "match_modes": spec.match_mode,
                "promoted_stage": spec.promoted_stage,
                "evidence_status": "FIRED_AND_ALIGNED",
                "notes": "Boolean field is already a post-result alignment from the existing window ledger.",
            }
        )
    return rows


def _value_attribution_rows(
    *,
    event: Dict[str, str],
    signals: Sequence[SignalValue],
    source_examined: Counter[str],
    source_matched: Counter[str],
) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for signal in signals:
        source_key = f"{signal.source_family}:{signal.source_tool}"
        source_examined[source_key] += 1
        match = _match_value(signal.value, signal.value_kind, event)
        if not match["matched_any"]:
            continue
        source_matched[source_key] += 1
        tier = "A" if match["match_exact"] or match["match_box"] else "B"
        target_lane = "straight" if match["match_exact"] else ("boxed" if match["match_box"] else "vtrac")
        rows.append(
            {
                "event_id": _event_id(event),
                "date": event.get("date", ""),
                "state_key": event.get("state_key", ""),
                "period": event.get("period", ""),
                "winner": event.get("winner", ""),
                "winner_canonical": event.get("winner_canonical", ""),
                "winner_vtrac_index": event.get("winner_vtrac_index", ""),
                "source_family": signal.source_family,
                "source_tool": signal.source_tool,
                "source_path": signal.source_path,
                "signal_id": f"{signal.source_family}:{signal.source_tool}:{signal.rank}",
                "signal_value": signal.value,
                "signal_value_kind": signal.value_kind,
                "signal_rank": signal.rank,
                "raw_score": signal.raw_score,
                "normalized_score": signal.normalized_score,
                "badge_or_alert": signal.badge_or_alert,
                "support_count": signal.support_count,
                "source_tags": signal.source_tags,
                "tier": tier,
                "target_lane": target_lane,
                "pre_draw_available": "True",
                "match_exact": str(match["match_exact"]),
                "match_box": str(match["match_box"]),
                "match_vtrac_straight": str(match["match_vtrac_straight"]),
                "match_vtrac_box": str(match["match_vtrac_box"]),
                "match_best_mode": match["match_best_mode"],
                "match_modes": match["match_modes"],
                "promoted_stage": signal.promoted_stage,
                "evidence_status": "FIRED_AND_ALIGNED",
                "notes": "",
            }
        )
    return rows


def _decay_attribution_rows(event: Dict[str, str], decay: Dict[str, str]) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for metric_name, values_field, family, tool, tier, target_lane, value_kind in DECAY_SPECS:
        profile = str(decay.get(f"{metric_name}_profile") or "").strip()
        if profile not in PROFILE_HIT:
            continue
        event_text = str(decay.get(f"{metric_name}_event") or "").strip()
        rows.append(
            {
                "event_id": _event_id(event),
                "date": event.get("date", ""),
                "state_key": event.get("state_key", ""),
                "period": event.get("period", ""),
                "winner": event.get("winner", ""),
                "winner_canonical": event.get("winner_canonical", ""),
                "winner_vtrac_index": event.get("winner_vtrac_index", ""),
                "source_family": family,
                "source_tool": f"{tool}_decay_resolution",
                "source_path": f"decay_rows.{metric_name}",
                "signal_id": metric_name,
                "signal_value": event_text,
                "signal_value_kind": value_kind,
                "signal_rank": "",
                "raw_score": "",
                "normalized_score": "",
                "badge_or_alert": profile,
                "support_count": "",
                "source_tags": str(decay.get(values_field) or ""),
                "tier": tier,
                "target_lane": target_lane,
                "pre_draw_available": "True",
                "match_exact": str(value_kind == "literal"),
                "match_box": str(value_kind == "canonical"),
                "match_vtrac_straight": "False",
                "match_vtrac_box": str(value_kind == "vtrac_index"),
                "match_best_mode": "EXACT" if value_kind == "literal" else ("BOX" if value_kind == "canonical" else "VTRAC_BOX"),
                "match_modes": "EXACT" if value_kind == "literal" else ("BOX" if value_kind == "canonical" else "VTRAC_BOX"),
                "promoted_stage": "decay_scorecard",
                "evidence_status": "FIRED_AND_DECAY_VALIDATED",
                "notes": f"Decay profile `{profile}` resolved at `{event_text}`.",
            }
        )
    return rows


def _frontier_attribution_rows(event: Dict[str, str], frontier: Dict[str, str]) -> List[Dict[str, Any]]:
    if not frontier:
        return []
    rows: List[Dict[str, Any]] = []
    signature = str(frontier.get("frontier_signature_type") or "").strip()
    strength = str(frontier.get("signature_strength") or "").strip()
    score = str(frontier.get("frontier_strength_score") or "").strip()
    fired_tests = _split_csvish(frontier.get("fired_tests") or "")
    quality = _frontier_quality(frontier)
    tier = "A" if quality == "sharp_frontier" else "B"
    if signature:
        rows.append(
            {
                "event_id": _event_id(event),
                "date": event.get("date", ""),
                "state_key": event.get("state_key", ""),
                "period": event.get("period", ""),
                "winner": event.get("winner", ""),
                "winner_canonical": event.get("winner_canonical", ""),
                "winner_vtrac_index": event.get("winner_vtrac_index", ""),
                "source_family": "frontier",
                "source_tool": "c1_c2_signature",
                "source_path": "c1_c2_frontier_cases.frontier_signature_type",
                "signal_id": signature,
                "signal_value": signature,
                "signal_value_kind": "frontier_signature",
                "signal_rank": "",
                "raw_score": score,
                "normalized_score": score,
                "badge_or_alert": strength,
                "support_count": frontier.get("terminal_signal_cells", ""),
                "source_tags": "|".join(fired_tests),
                "tier": tier,
                "target_lane": "boxed" if signature in {"LITERAL_FRONTIER", "FAMILY_FRONTIER", "DOUBLE_FRONTIER"} else "vtrac",
                "pre_draw_available": "False",
                "match_exact": str(signature == "LITERAL_FRONTIER"),
                "match_box": str(signature in {"FAMILY_FRONTIER", "DOUBLE_FRONTIER"}),
                "match_vtrac_straight": "False",
                "match_vtrac_box": str(signature in {"VTRAC_FRONTIER", "HIDDEN_COMPRESSED_FRONTIER", "FEEDER_TO_FRONTIER"}),
                "match_best_mode": "BOX" if signature in {"FAMILY_FRONTIER", "DOUBLE_FRONTIER"} else ("EXACT" if signature == "LITERAL_FRONTIER" else "VTRAC_BOX"),
                "match_modes": signature,
                "promoted_stage": "frontier_audit",
                "evidence_status": "POST_RESULT_FRONTIER_ATTRIBUTION",
                "notes": "Frontier evidence is post-result explanatory evidence, not a pre-draw live firing source yet.",
            }
        )
    for test in fired_tests:
        rows.append(
            {
                "event_id": _event_id(event),
                "date": event.get("date", ""),
                "state_key": event.get("state_key", ""),
                "period": event.get("period", ""),
                "winner": event.get("winner", ""),
                "winner_canonical": event.get("winner_canonical", ""),
                "winner_vtrac_index": event.get("winner_vtrac_index", ""),
                "source_family": "frontier",
                "source_tool": "fired_test",
                "source_path": "c1_c2_frontier_cases.fired_tests",
                "signal_id": test,
                "signal_value": test,
                "signal_value_kind": "frontier_test",
                "signal_rank": "",
                "raw_score": score,
                "normalized_score": score,
                "badge_or_alert": strength,
                "support_count": "",
                "source_tags": signature,
                "tier": tier,
                "target_lane": "frontier",
                "pre_draw_available": "False",
                "match_exact": "False",
                "match_box": "False",
                "match_vtrac_straight": "False",
                "match_vtrac_box": "False",
                "match_best_mode": "FRONTIER_CONTEXT",
                "match_modes": "FRONTIER_CONTEXT",
                "promoted_stage": "frontier_audit",
                "evidence_status": "POST_RESULT_FRONTIER_ATTRIBUTION",
                "notes": "Fired frontier test is explanatory context for future translator training.",
            }
        )
    return rows


def _merge_event_row(
    perf: Dict[str, str],
    hit_lookup: Dict[Tuple[str, str, str, str], Dict[str, str]],
    translator_lookup: Dict[Tuple[str, str, str, str], Dict[str, str]],
) -> Dict[str, str]:
    key = _event_key(perf)
    merged = dict(perf)
    for source in (hit_lookup.get(key) or {}, translator_lookup.get(key) or {}):
        for k, v in source.items():
            if v and (k not in merged or not merged[k]):
                merged[k] = v
    return merged


def _build_utilization_rows(
    *,
    perf_rows: Sequence[Dict[str, str]],
    hit_rows: Sequence[Dict[str, str]],
    translator_rows: Sequence[Dict[str, str]],
    frontier_lookup: Dict[Tuple[str, str, str], Dict[str, str]],
    decay_lookup: Dict[Tuple[str, str], Dict[str, str]],
    attribution_by_event: Dict[str, List[Dict[str, Any]]],
) -> List[Dict[str, Any]]:
    hit_lookup = _load_lookup(hit_rows, _event_key)
    translator_lookup = _load_lookup(translator_rows, _event_key)
    rows: List[Dict[str, Any]] = []
    for perf in perf_rows:
        event = _merge_event_row(perf, hit_lookup, translator_lookup)
        frontier = frontier_lookup.get((event.get("date", ""), event.get("state_key", ""), event.get("winner", ""))) or {}
        decay = decay_lookup.get((event.get("date", ""), event.get("state_key", ""))) or {}
        outcome = _outcome_class(event)
        status = _evidence_status(event, decay, frontier)
        event_attrib = attribution_by_event.get(_event_id(event), [])
        pre_draw_attrib = [row for row in event_attrib if str(row.get("pre_draw_available")) == "True"]
        exact_sources = [row["source_tool"] for row in event_attrib if str(row.get("match_exact")) == "True"]
        box_sources = [row["source_tool"] for row in event_attrib if str(row.get("match_box")) == "True"]
        vt_sources = [
            row["source_tool"]
            for row in event_attrib
            if str(row.get("match_vtrac_straight")) == "True" or str(row.get("match_vtrac_box")) == "True"
        ]
        rows.append(
            {
                "event_id": _event_id(event),
                "date": event.get("date", ""),
                "state_key": event.get("state_key", ""),
                "period": event.get("period", ""),
                "winner": event.get("winner", ""),
                "winner_canonical": event.get("winner_canonical", ""),
                "winner_vtrac_index": event.get("winner_vtrac_index", ""),
                "outcome_class": outcome,
                "evidence_status": status,
                "display_order": event.get("display_order", ""),
                "display_order_source": event.get("display_order_source", ""),
                "board_rank": event.get("board_rank", ""),
                "analytical_rank": event.get("analytical_rank", ""),
                "legacy_static_rank": event.get("legacy_static_rank", ""),
                "rank_signal_valid": event.get("rank_signal_valid", ""),
                "rank_integrity_status": event.get("rank_integrity_status", ""),
                "board_rank_tier": event.get("board_rank_tier", ""),
                "board_priority_score": event.get("board_priority_score", ""),
                "top_primary_target": event.get("top_primary_target", ""),
                "secondary_target": event.get("secondary_target", ""),
                "best_clean_host": event.get("best_clean_host", ""),
                "sharp_signal_count": _sharp_signal_count(event),
                "territory_signal_count": _territory_signal_count(event),
                "broad_context_count": _broad_context_count(event),
                "pre_draw_attribution_count": len(pre_draw_attrib),
                "post_result_attribution_count": len(event_attrib) - len(pre_draw_attrib),
                "exact_source_count": len(exact_sources),
                "box_source_count": len(box_sources),
                "vtrac_source_count": len(vt_sources),
                "exact_sources": "|".join(_ordered_unique(exact_sources)[:16]),
                "box_sources": "|".join(_ordered_unique(box_sources)[:16]),
                "vtrac_sources": "|".join(_ordered_unique(vt_sources)[:16]),
                "arena_box_signal": event.get("arena_box_signal", ""),
                "arena_exact_signal": event.get("arena_exact_signal", ""),
                "arena_primary_box": event.get("arena_primary_box", ""),
                "arena_primary_vt": event.get("arena_primary_vt", ""),
                "sandbox_box_seed": event.get("sandbox_box_seed", ""),
                "sandbox_exact_seed": event.get("sandbox_exact_seed", ""),
                "sandbox_vt_seed": event.get("sandbox_vt_seed", ""),
                "cu_exact": event.get("cu_exact", ""),
                "cu_box": event.get("cu_box", ""),
                "play_card_any_exact": event.get("play_card_any_exact", ""),
                "play_card_any_box": event.get("play_card_any_box", ""),
                "opportunity_gap_box": event.get("opportunity_gap_box", ""),
                "opportunity_gap_exact": event.get("opportunity_gap_exact", ""),
                "play_straight_hit": event.get("play_straight_hit", ""),
                "play_box_strict_hit": event.get("play_box_strict_hit", ""),
                "play_box_any_hit": event.get("play_box_any_hit", ""),
                "play_vtrac_only_hit": event.get("play_vtrac_only_hit", ""),
                "hit_class": event.get("hit_class", ""),
                "arena_final_candidate_signature": event.get("arena_final_candidate_signature", ""),
                "frontier_signature_type": frontier.get("frontier_signature_type", ""),
                "frontier_signature_strength": frontier.get("signature_strength", ""),
                "frontier_strength_score": frontier.get("frontier_strength_score", ""),
                "double_context_strength": event.get("double_context_strength") or frontier.get("double_context_strength_best", ""),
                "inventory_type": event.get("inventory_type", ""),
                "decay_any_profile": decay.get("arena_any_signal_profile", ""),
                "decay_any_event": decay.get("arena_any_signal_event", ""),
                "active_decay_metric_count": decay.get("active_metric_count", ""),
                "active_decay_metrics": decay.get("active_metric_names", ""),
                "reason_codes": event.get("reason_codes", ""),
                "interpretation": _event_interpretation(status, outcome),
            }
        )
    return rows


def _event_interpretation(status: str, outcome: str) -> str:
    if status == "CAPTURED_AND_USED":
        return "Evidence reached downstream conversion; preserve as positive translator example."
    if status == "CAPTURED_BUT_UNDERUSED":
        return "High-value training case: evidence existed but old final selection did not budget/select it cleanly."
    if status == "CAPTURED_BUT_WRONG_LANE":
        return "Territory/VTRAC evidence was present, but boxed/straight conversion lane was not strong enough."
    if status == "DECAY_VALIDATED":
        return "Same-day-only judgment would under-credit this state-day; keep in carryforward/decay lane."
    if status == "CAPTURED_BUT_NOT_PROMOTED":
        return "Some useful evidence existed, but final promotion remains unclear."
    if status == "BROAD_CONTEXT_ONLY":
        return "Only broad context is visible; do not treat as conversion-grade evidence."
    return "No strong machine-readable capture found in current audit sources."


def _score_boolean_signals(util_rows: Sequence[Dict[str, Any]]) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    total = len(util_rows)
    for spec in BOOL_SIGNAL_SPECS:
        present = [row for row in util_rows if _truthy(row.get(spec.field))]
        if not present:
            continue
        converted = [row for row in present if row.get("outcome_class") in {"STRAIGHT", "STRICT_BOX", "BOX_ANY"}]
        gap = [row for row in present if row.get("outcome_class") in {"BOX_GAP", "EXACT_GAP"}]
        vt_only = [row for row in present if row.get("outcome_class") == "VTRAC_ONLY"]
        no_conv = [row for row in present if row.get("outcome_class") == "NO_CONVERSION"]
        rows.append(
            {
                "signal": spec.field,
                "source_family": spec.source_family,
                "source_tool": spec.source_tool,
                "tier": spec.tier,
                "target_lane": spec.target_lane,
                "present_events": len(present),
                "present_rate": _rate(len(present), total),
                "converted_events": len(converted),
                "converted_rate_within_signal": _rate(len(converted), len(present)),
                "gap_events": len(gap),
                "gap_rate_within_signal": _rate(len(gap), len(present)),
                "vt_only_events": len(vt_only),
                "vt_only_rate_within_signal": _rate(len(vt_only), len(present)),
                "no_conversion_events": len(no_conv),
                "no_conversion_rate_within_signal": _rate(len(no_conv), len(present)),
                "read": _signal_read(spec, len(present), total, len(converted), len(gap)),
            }
        )
    rows.sort(key=lambda row: (row["tier"], -float(row["converted_rate_within_signal"]), -int(row["present_events"])))
    return rows


def _signal_read(spec: BoolSignalSpec, present: int, total: int, converted: int, gap: int) -> str:
    if spec.tier == "C":
        return "Ambient/context flag; use only as support unless paired with sharper evidence."
    if present and gap / present >= 0.35:
        return "High-priority translator-learning signal; often saw value that old final layer missed."
    if spec.tier == "B" and present and converted / present >= 0.40:
        return "Strong territory signal; promote to conversion only when paired with sharper exact/box evidence."
    if present and converted / present >= 0.40:
        return "Conversion-grade candidate signal in this window."
    if present and gap / present >= 0.25:
        return "Translator-learning signal; often saw value that old final layer missed."
    if present and present / max(total, 1) > 0.50:
        return "Broad presence; useful for territory but weak as a standalone discriminator."
    return "Track as supporting evidence; confirm stability in next window."


def _score_attribution_sources(
    attribution_rows: Sequence[Dict[str, Any]],
    source_examined: Counter[str],
    source_matched: Counter[str],
) -> List[Dict[str, Any]]:
    grouped: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for row in attribution_rows:
        key = f"{row.get('source_family')}:{row.get('source_tool')}"
        grouped[key].append(row)
    out: List[Dict[str, Any]] = []
    for key, rows in grouped.items():
        families = Counter(str(row.get("source_family") or "") for row in rows)
        tools = Counter(str(row.get("source_tool") or "") for row in rows)
        exact = sum(1 for row in rows if str(row.get("match_exact")) == "True")
        box = sum(1 for row in rows if str(row.get("match_box")) == "True")
        vt = sum(
            1
            for row in rows
            if str(row.get("match_vtrac_straight")) == "True" or str(row.get("match_vtrac_box")) == "True"
        )
        pre = sum(1 for row in rows if str(row.get("pre_draw_available")) == "True")
        examined = source_examined.get(key, 0)
        matched = source_matched.get(key, 0)
        out.append(
            {
                "source_key": key,
                "source_group": "emitted_values" if examined else "boolean_or_derived",
                "source_family": families.most_common(1)[0][0] if families else "",
                "source_tool": tools.most_common(1)[0][0] if tools else "",
                "attribution_rows": len(rows),
                "pre_draw_rows": pre,
                "post_result_rows": len(rows) - pre,
                "exact_rows": exact,
                "box_rows": box,
                "vtrac_rows": vt,
                "source_values_examined": examined,
                "source_values_winner_aligned": matched,
                "winner_alignment_rate_within_emitted_values": _rate(matched, examined),
            }
        )
    out.sort(
        key=lambda row: (
            0 if row["source_group"] == "emitted_values" else 1,
            -int(row["source_values_winner_aligned"]),
            -int(row["pre_draw_rows"]),
            -int(row["box_rows"]),
            row["source_key"],
        )
    )
    return out


def _select_case_rows(
    util_rows: Sequence[Dict[str, Any]],
    frontier_lookup: Dict[Tuple[str, str, str], Dict[str, str]],
    *,
    case_limit: int,
) -> List[Dict[str, Any]]:
    selected: List[Dict[str, Any]] = []
    seen: set[str] = set()

    def add(label: str, candidates: Iterable[Dict[str, Any]], limit: int) -> None:
        ranked = sorted(
            candidates,
            key=lambda row: (
                -int(row.get("sharp_signal_count") or 0),
                -int(row.get("box_source_count") or 0),
                -_safe_float(row.get("frontier_strength_score")),
                str(row.get("date") or ""),
                str(row.get("state_key") or ""),
            ),
        )
        count = 0
        for row in ranked:
            if len(selected) >= case_limit:
                return
            eid = str(row.get("event_id") or "")
            if eid in seen:
                continue
            out = dict(row)
            out["case_category"] = label
            selected.append(out)
            seen.add(eid)
            count += 1
            if count >= limit:
                return

    add("successful_straight_or_exact", [r for r in util_rows if r.get("outcome_class") == "STRAIGHT"], 4)
    add("successful_box_conversion", [r for r in util_rows if r.get("outcome_class") in {"STRICT_BOX", "BOX_ANY"}], 4)
    add("box_gap", [r for r in util_rows if r.get("outcome_class") == "BOX_GAP"], 6)
    add("exact_gap", [r for r in util_rows if r.get("outcome_class") == "EXACT_GAP"], 3)
    add("vtrac_only_wrong_lane", [r for r in util_rows if r.get("outcome_class") == "VTRAC_ONLY"], 4)
    add("future_decay", [r for r in util_rows if r.get("decay_any_profile") == "future_day_decay"], 4)

    promotion_cases = []
    for row in util_rows:
        frontier = frontier_lookup.get((row.get("date", ""), row.get("state_key", ""), row.get("winner", ""))) or {}
        if str(frontier.get("signature_strength") or "").upper() == "STRONG" and row.get("outcome_class") in {"BOX_GAP", "EXACT_GAP", "NO_CONVERSION", "VTRAC_ONLY"}:
            promotion_cases.append(row)
    add("frontier_promotion_candidate", promotion_cases, 5)
    add("no_conversion_control", [r for r in util_rows if r.get("outcome_class") == "NO_CONVERSION"], 4)
    return selected


def _render_audit_markdown(payload: Dict[str, Any], paths: Dict[str, Path]) -> str:
    summary = payload["summary"]
    counts = summary["counts"]
    status_counts = summary["evidence_status_counts"]
    outcome_counts = summary["outcome_class_counts"]
    lines = [
        "# Analysis Arena Evidence Utilization Audit",
        "",
        "Purpose: measure whether March-window winner evidence was captured, promoted, converted, underused, or only present as broad context.",
        "",
        "## 1. Scope",
        "",
        f"- Window root: `{summary['window_root']}`",
        f"- Winner events audited: `{counts['winner_events']}`",
        f"- Utilization ledger: `{safe_rel(paths['util_csv'])}`",
        f"- Signal attribution ledger: `{safe_rel(paths['signal_csv'])}`",
        f"- Case dossiers: `{safe_rel(paths['case_md'])}`",
        f"- Translator redesign memo: `{safe_rel(paths['redesign_md'])}`",
        "",
        "## 2. Evidence Status Counts",
        "",
    ]
    for key, count in status_counts.items():
        lines.append(f"- {key}: `{count}` ({_pct(count, counts['winner_events'])})")
    lines.extend(["", "## 3. Outcome Class Counts", ""])
    for key, count in outcome_counts.items():
        lines.append(f"- {key}: `{count}` ({_pct(count, counts['winner_events'])})")
    lines.extend(
        [
            "",
            "## 4. Core Reads",
            "",
            f"- Captured-and-used events: `{counts['captured_and_used']}`.",
            f"- Captured-but-underused events: `{counts['captured_but_underused']}`.",
            f"- Captured-but-not-promoted events: `{counts['captured_but_not_promoted']}`.",
            f"- Captured-but-wrong-lane events: `{counts['captured_but_wrong_lane']}`.",
            f"- Decay-validated events: `{counts['decay_validated']}`.",
            f"- Broad-context-only events: `{counts['broad_context_only']}`.",
            f"- Not-captured events in current machine-readable audit sources: `{counts['not_captured']}`.",
            f"- Pre-draw winner-aligned attribution rows: `{counts['pre_draw_attribution_rows']}`.",
            f"- Post-result explanatory frontier/decay attribution rows: `{counts['post_result_attribution_rows']}`.",
            "",
            "## 5. Interpretation",
            "",
            "- The audit separates `FIRED`, `ALIGNED`, `PROMOTED`, and `CONVERTED`; a tracked signal is not automatically a final decision signal.",
            "- Box-gap and exact-gap rows are treated as high-value translator training cases, not ordinary misses.",
            "- Broad support flags remain visible, but they are downgraded unless paired with sharper exact/box/frontier/decay evidence.",
            "- Brain2 ranking is included as context, but static rank behavior must still be checked before treating top-primary as dynamic proof.",
            "",
            "## 6. Files Generated",
            "",
        ]
    )
    for key in ("util_csv", "signal_csv", "signal_md", "case_md", "redesign_md", "dictionary_md", "protocol_md", "audit_json"):
        lines.append(f"- `{safe_rel(paths[key])}`")
    return "\n".join(lines) + "\n"


def _render_signal_scorecard(
    *,
    bool_scores: Sequence[Dict[str, Any]],
    attribution_scores: Sequence[Dict[str, Any]],
    source_examined: Counter[str],
    source_matched: Counter[str],
    util_rows: Sequence[Dict[str, Any]],
    signal_rows: Sequence[Dict[str, Any]],
) -> str:
    lines = [
        "# Winner Signal Attribution Scorecard",
        "",
        "Purpose: show which indicators fired toward winners, by exact/box/VTRAC modes, and whether they are sharp enough for future Brain scoring work.",
        "",
        "## 1. Totals",
        "",
        f"- Winner events: `{len(util_rows)}`",
        f"- Winner-aligned attribution rows: `{len(signal_rows)}`",
        f"- Source keys with emitted-value denominators: `{len(source_examined)}`",
        "",
        "## 2. Boolean Alignment Signals",
        "",
        "| Signal | Tier | Present | Converted | Gap | VT-only | Read |",
        "|---|---:|---:|---:|---:|---:|---|",
    ]
    for row in bool_scores:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{row['signal']}`",
                    f"`{row['tier']}`",
                    f"`{row['present_events']}` ({_pct(int(row['present_events']), len(util_rows))})",
                    f"`{row['converted_events']}` ({_pct(int(row['converted_events']), int(row['present_events']))})",
                    f"`{row['gap_events']}` ({_pct(int(row['gap_events']), int(row['present_events']))})",
                    f"`{row['vt_only_events']}` ({_pct(int(row['vt_only_events']), int(row['present_events']))})",
                    str(row["read"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. Matched Emitted Source Values",
            "",
            "| Source | Pre-draw aligned rows | Exact | Box | VTRAC | Values examined | Alignment rate |",
            "|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    emitted_rows = [row for row in attribution_scores if int(row.get("source_values_examined") or 0) > 0]
    for row in emitted_rows[:40]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{row['source_key']}`",
                    f"`{row['pre_draw_rows']}`",
                    f"`{row['exact_rows']}`",
                    f"`{row['box_rows']}`",
                    f"`{row['vtrac_rows']}`",
                    f"`{row['source_values_examined']}`",
                    f"{100.0 * float(row['winner_alignment_rate_within_emitted_values']):.2f}%",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 4. Boolean / Derived Attribution Rows",
            "",
            "| Source | Pre-draw aligned rows | Exact | Box | VTRAC | Notes |",
            "|---|---:|---:|---:|---:|---|",
        ]
    )
    derived_rows = [row for row in attribution_scores if int(row.get("source_values_examined") or 0) == 0]
    for row in derived_rows[:30]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{row['source_key']}`",
                    f"`{row['pre_draw_rows']}`",
                    f"`{row['exact_rows']}`",
                    f"`{row['box_rows']}`",
                    f"`{row['vtrac_rows']}`",
                    "Boolean, decay, or post-result explanatory row; denominator is not an emitted-value list.",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 5. Practical Read",
            "",
            "- Treat this as winner-alignment attribution, not final predictive lift by itself.",
            "- Stage 2 should add a full false-positive/exposure denominator for the same source keys across non-winning emitted values.",
            "- Exact and box rows are most relevant to future straight/boxed lanes; VTRAC rows are territory and decay-lane evidence unless paired with sharper evidence.",
        ]
    )
    return "\n".join(lines) + "\n"


def _render_case_dossiers(case_rows: Sequence[Dict[str, Any]], attribution_by_event: Dict[str, List[Dict[str, Any]]]) -> str:
    lines = [
        "# Analysis Arena Case Dossiers",
        "",
        "These are representative March-window cases chosen to inspect how evidence moved from tools into Arena, candidates, play-card, frontier, and decay.",
        "",
    ]
    for idx, row in enumerate(case_rows, start=1):
        eid = str(row.get("event_id") or "")
        attribs = attribution_by_event.get(eid, [])
        pre = [a for a in attribs if str(a.get("pre_draw_available")) == "True"]
        deduped_pre: List[Dict[str, Any]] = []
        seen_pre: set[Tuple[str, str, str]] = set()
        for item in pre:
            key = (
                str(item.get("source_family") or ""),
                str(item.get("source_tool") or ""),
                str(item.get("signal_value") or ""),
            )
            if key in seen_pre:
                continue
            seen_pre.add(key)
            deduped_pre.append(item)
        top_pre = sorted(
            deduped_pre,
            key=lambda a: (
                0 if a.get("tier") == "A" else 1,
                str(a.get("source_family") or ""),
                str(a.get("source_tool") or ""),
            ),
        )[:12]
        lines.extend(
            [
                f"## {idx}. {row.get('case_category', '')}: {row.get('date', '')} {row.get('state_key', '')} {row.get('period', '')} winner `{row.get('winner', '')}`",
                "",
                f"- Outcome: `{row.get('outcome_class', '')}`",
                f"- Evidence status: `{row.get('evidence_status', '')}`",
                (
                    f"- Analytical board rank: `{row.get('board_rank', '')}`; "
                    if _truthy(row.get("rank_signal_valid"))
                    else "- Analytical board rank: `NOT_EVALUABLE` (`INVALID_STATIC_ORDER`); "
                )
                + f"sharp=`{row.get('sharp_signal_count', '')}`, territory=`{row.get('territory_signal_count', '')}`, broad=`{row.get('broad_context_count', '')}`",
                f"- Frontier: `{row.get('frontier_signature_type', '') or '-'}` strength=`{row.get('frontier_signature_strength', '') or '-'}` score=`{row.get('frontier_strength_score', '') or '-'}`",
                f"- State-day decay first resolution: `{row.get('decay_any_profile', '') or '-'}` event=`{row.get('decay_any_event', '') or '-'}`",
                f"- Exact sources: `{row.get('exact_sources', '') or '-'}`",
                f"- Box sources: `{row.get('box_sources', '') or '-'}`",
                f"- VTRAC sources: `{row.get('vtrac_sources', '') or '-'}`",
                f"- Diagnosis: {row.get('interpretation', '')}",
                "",
                "Top winner-aligned pre-draw signals:",
            ]
        )
        if not top_pre:
            lines.append("- _No pre-draw winner-aligned source rows in current parser coverage._")
        else:
            for a in top_pre:
                lines.append(
                    f"- `{a.get('source_family', '')}:{a.get('source_tool', '')}` value=`{a.get('signal_value', '')}` "
                    f"mode=`{a.get('match_best_mode', '')}` tier=`{a.get('tier', '')}` stage=`{a.get('promoted_stage', '')}`"
                )
        lines.append("")
    return "\n".join(lines)


def _render_redesign_lessons(
    *,
    util_rows: Sequence[Dict[str, Any]],
    bool_scores: Sequence[Dict[str, Any]],
    attribution_scores: Sequence[Dict[str, Any]],
) -> str:
    status_counts = Counter(str(row.get("evidence_status") or "") for row in util_rows)
    outcome_counts = Counter(str(row.get("outcome_class") or "") for row in util_rows)
    strong_bool = [row for row in bool_scores if row["tier"] == "A" and int(row["present_events"]) > 0]
    top_sources = [row for row in attribution_scores if int(row.get("pre_draw_rows") or 0) > 0][:12]
    lines = [
        "# Translator Redesign Lessons From Evidence Utilization Audit",
        "",
        "This memo converts the March audit into design guidance for a future Analysis Arena-native candidate translator.",
        "",
        "## 1. Main Finding",
        "",
        "- The primary redesign target is not more broad evidence capture; it is cleaner promotion from evidence into separated boxed, straight, VTRAC, and decay lanes.",
        f"- Captured-and-used: `{status_counts.get('CAPTURED_AND_USED', 0)}`; captured-but-underused: `{status_counts.get('CAPTURED_BUT_UNDERUSED', 0)}`; wrong-lane: `{status_counts.get('CAPTURED_BUT_WRONG_LANE', 0)}`.",
        f"- Box/exact gaps: `{outcome_counts.get('BOX_GAP', 0) + outcome_counts.get('EXACT_GAP', 0)}`; VTRAC-only: `{outcome_counts.get('VTRAC_ONLY', 0)}`.",
        "",
        "## 2. Candidate Lane Implications",
        "",
        "- Boxed lane should prioritize exact/box-aligned Arena, sandbox, play-card, profit-alert, double-anchor, family-frontier, and box-gap evidence.",
        "- Straight lane should remain stricter: exact sandbox, exact play-card, literal frontier, positional combo exactness, and direct profit-alert evidence should carry more weight than broad canonical context.",
        "- VTRAC lane should be treated as territory/carryforward unless paired with box/exact evidence or a strong frontier/double signal.",
        "- Decay lane should remain separate from same-day grading but feed carryforward watch decisions.",
        "",
        "## 3. Signals Worth Promoting Into Future Scoring Experiments",
        "",
    ]
    for row in strong_bool[:12]:
        lines.append(
            f"- `{row['signal']}`: present `{row['present_events']}`, converted `{row['converted_events']}`, gap `{row['gap_events']}`; {row['read']}"
        )
    lines.extend(["", "## 4. Source Rows Worth Preserving For Brain1/Brain2 Training", ""])
    for row in top_sources:
        lines.append(
            f"- `{row['source_key']}`: pre-draw aligned `{row['pre_draw_rows']}`, exact `{row['exact_rows']}`, box `{row['box_rows']}`, VTRAC `{row['vtrac_rows']}`."
        )
    lines.extend(
        [
            "",
            "## 5. Guardrails",
            "",
            "- Do not build one master score yet; first add exposure/false-positive denominators for source keys.",
            "- Keep Brain2 rank diagnostics active because static rank can make top-primary metrics look stronger than they are.",
            "- Keep bonus/fireball sidecar separate from standard boxed/straight metrics.",
            "- Use this audit to choose fixtures for future translator tests before rewriting candidate generation.",
        ]
    )
    return "\n".join(lines) + "\n"


def _render_dictionary(paths: Dict[str, Path]) -> str:
    lines = [
        "# Signal Source Dictionary And Parser Coverage",
        "",
        "This dictionary documents what the post-run audit can currently parse and where each source lives.",
        "",
        "## 1. Parsed Sources",
        "",
        "- `performance_gap__ledger.csv`: event-level winner alignment booleans, old play-card hits, candidate universe flags, broad support flags, opportunity gaps.",
        "- `HIT_ROSTER.csv`: credited hit fields, strategy hit metadata, profit-alert direct/implied matches, due-double ranks, blackapple status, compound events, final candidate signatures.",
        "- `TRANSLATOR_LEARNING_LEDGER.csv`: translator cohorts, hit classes, frontier columns copied into teaching rows.",
        "- `C1_C2_FRONTIER_CASES.csv`: post-result C1/C2 vertical frontier signatures, strengths, fired tests, double-anchor and compression scores.",
        "- `DECAY_CARRYOVER_ROWS.csv`: state-day signal values and bounded future resolution profiles.",
        "- `BOARD_SCOREBOARD` JSON: board rank, top canonicals, top VTRAC indices, tracker hints.",
        "- `TRANSLATION_SANDBOX_SEED` JSON: Brain1 core, Brain2 context, sandbox hypotheses, control-arm candidate universe, old play-card, and shadow-policy focus.",
        "",
        "## 2. Match Modes",
        "",
        "- `EXACT`: ordered 3-digit signal value equals the winner.",
        "- `BOX`: canonical sorted digits equal the winner canonical.",
        "- `VTRAC_STRAIGHT`: ordered VTRAC digit pattern equals the winner VTRAC pattern when a literal combo is available.",
        "- `VTRAC_BOX`: VTRAC index/family equals the winner VTRAC index.",
        "",
        "## 3. Current Coverage Limits",
        "",
        "- Broad flags such as due-double support, blackapple support, survivor support, and profit-alert support are retained as context unless exact/canonical value lists are available.",
        "- Frontier evidence is post-result explanatory evidence in this audit; it is not counted as a live pre-draw firing source unless future tooling exports pre-draw frontier candidates.",
        "- Family labels that are not canonical digits are not force-matched; they need a separate family parser if we want them credited directly.",
        "- Stage 2 should add a full exposure/false-positive ledger for emitted signals that did not match winners.",
        "",
        "## 4. Generated Outputs",
        "",
    ]
    for key in ("util_csv", "signal_csv", "signal_md", "case_md", "redesign_md", "audit_md"):
        lines.append(f"- `{safe_rel(paths[key])}`")
    return "\n".join(lines) + "\n"


def _render_protocol() -> str:
    return """# Analysis Arena Post-Run Audit Protocol

Purpose: make post-window learning repeatable, so high-value findings are not left only in narrative chat or one-off reports.

## 1. Required Inputs

- Completed Analysis Arena window root under `docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/`.
- Performance gap ledger.
- Hit roster.
- Translator learning ledger.
- C1/C2 frontier cases with non-zero case count.
- Decay carryover rows with tail coverage noted.
- Per-day board scoreboard JSON.
- Per-day translation sandbox seed manifest and seed JSONs.

## 2. Run Commands

```bash
python3 scripts/tools/create_window_evidence_utilization_audit.py --window-root "docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_<START>_to_<END>" --force
python3 scripts/tools/create_window_audit_interpretation_report.py --window-root "docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/WINDOW_<START>_to_<END>" --force
```

## 3. Required Outputs

- Evidence utilization ledger CSV.
- Evidence utilization audit Markdown/JSON.
- Winner signal attribution ledger CSV.
- Winner signal attribution scorecard Markdown.
- Case dossiers Markdown.
- Translator redesign lessons Markdown.
- Signal source dictionary Markdown.
- Audit interpretation pass Markdown/JSON.
- Audit interpretation priority cases CSV.
- Audit interpretation signal decisions CSV.

## 4. Review Order

1. Confirm event count equals the window performance-gap denominator.
2. Confirm winner signal attribution has both pre-draw and post-result rows.
3. Review captured-but-underused and wrong-lane cases before judging final candidate quality.
4. Review box-gap and exact-gap dossiers as translator training examples.
5. Review source dictionary coverage before assuming an indicator was absent.
6. Run and review the audit interpretation pass before choosing future candidate/Brain scoring experiments.
7. Use interpretation priority cases as fixture candidates, not as immediate scoring weights.

## 5. Interpretation Rules

- `CAPTURED_AND_USED` means evidence reached final conversion.
- `CAPTURED_BUT_UNDERUSED` means evidence existed but old final selection did not fully use it.
- `CAPTURED_BUT_WRONG_LANE` means territory/VTRAC support existed but boxed/straight conversion failed.
- `DECAY_VALIDATED` means same-day grading under-credits a signal that resolved inside the configured horizon.
- `BROAD_CONTEXT_ONLY` means a signal may be useful context but is not sharp enough alone.
- `NOT_CAPTURED` means no strong machine-readable evidence was found by current parser coverage.
- Audit interpretation counts are teaching-cohort labels. They do not replace raw performance totals.

## 6. Guardrails

- Do not redesign prediction/budget logic directly from winner-only attribution.
- Add false-positive exposure denominators before building a new master score.
- Keep bonus/fireball metrics separate from standard exact/box/VTRAC metrics.
- Keep Brain2 rank-static diagnostics active.
- Treat the interpretation pass as design guidance; scoring changes still require Stage-2 exposure/false-positive measurement.
"""


def build_payload(window_root: Path, final_docs_dir: Path, *, case_limit: int) -> Tuple[Dict[str, Any], Dict[str, Path]]:
    paths = _default_paths(window_root, final_docs_dir)
    dates = iter_window_dates(window_root)
    perf_rows = _read_csv_rows(paths["perf"])
    hit_rows = _read_csv_rows(paths["hit_roster"])
    translator_rows = _read_csv_rows(paths["translator"])
    frontier_rows = _read_csv_rows(paths["frontier"])
    decay_rows = _read_csv_rows(paths["decay"])

    hit_lookup = _load_lookup(hit_rows, _event_key)
    translator_lookup = _load_lookup(translator_rows, _event_key)
    frontier_lookup = _load_lookup(frontier_rows, _frontier_key)
    decay_lookup = {(row.get("snapshot_date", ""), row.get("state_key", "")): row for row in decay_rows}
    scoreboard_rows = _load_scoreboard_rows(window_root, dates)
    seed_rows = _load_seed_rows(window_root, dates)

    source_examined: Counter[str] = Counter()
    source_matched: Counter[str] = Counter()
    signal_rows: List[Dict[str, Any]] = []

    for perf in perf_rows:
        event = _merge_event_row(perf, hit_lookup, translator_lookup)
        seed = seed_rows.get((event.get("date", ""), event.get("state_key", ""))) or {}
        scoreboard_row = scoreboard_rows.get((event.get("date", ""), event.get("state_key", ""))) or {}
        seed_signals = _signals_from_seed(seed, scoreboard_row) if seed or scoreboard_row else []
        decay = decay_lookup.get((event.get("date", ""), event.get("state_key", ""))) or {}
        frontier = frontier_lookup.get((event.get("date", ""), event.get("state_key", ""), event.get("winner", ""))) or {}
        signal_rows.extend(_field_attribution_rows(event))
        signal_rows.extend(
            _value_attribution_rows(
                event=event,
                signals=seed_signals,
                source_examined=source_examined,
                source_matched=source_matched,
            )
        )
        signal_rows.extend(_decay_attribution_rows(event, decay))
        signal_rows.extend(_frontier_attribution_rows(event, frontier))

    attribution_by_event: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for row in signal_rows:
        attribution_by_event[str(row.get("event_id") or "")].append(row)

    util_rows = _build_utilization_rows(
        perf_rows=perf_rows,
        hit_rows=hit_rows,
        translator_rows=translator_rows,
        frontier_lookup=frontier_lookup,
        decay_lookup=decay_lookup,
        attribution_by_event=attribution_by_event,
    )
    bool_scores = _score_boolean_signals(util_rows)
    attribution_scores = _score_attribution_sources(signal_rows, source_examined, source_matched)
    case_rows = _select_case_rows(util_rows, frontier_lookup, case_limit=case_limit)

    status_counts = Counter(str(row.get("evidence_status") or "") for row in util_rows)
    outcome_counts = Counter(str(row.get("outcome_class") or "") for row in util_rows)
    pre_count = sum(1 for row in signal_rows if str(row.get("pre_draw_available")) == "True")
    post_count = len(signal_rows) - pre_count
    m = WINDOW_RE.match(window_root.name)
    window_dates = [m.group("start"), m.group("end")] if m else ([dates[0], dates[-1]] if dates else [])
    payload: Dict[str, Any] = {
        "schema_version": "analysis_arena_evidence_utilization_audit/v1",
        "summary": {
            "window_root": safe_rel(window_root),
            "window_dates": window_dates,
            "counts": {
                "winner_events": len(perf_rows),
                "hit_roster_rows": len(hit_rows),
                "translator_rows": len(translator_rows),
                "frontier_rows": len(frontier_rows),
                "decay_rows": len(decay_rows),
                "utilization_rows": len(util_rows),
                "signal_attribution_rows": len(signal_rows),
                "pre_draw_attribution_rows": pre_count,
                "post_result_attribution_rows": post_count,
                "captured_and_used": status_counts.get("CAPTURED_AND_USED", 0),
                "captured_but_underused": status_counts.get("CAPTURED_BUT_UNDERUSED", 0),
                "captured_but_not_promoted": status_counts.get("CAPTURED_BUT_NOT_PROMOTED", 0),
                "captured_but_wrong_lane": status_counts.get("CAPTURED_BUT_WRONG_LANE", 0),
                "decay_validated": status_counts.get("DECAY_VALIDATED", 0),
                "broad_context_only": status_counts.get("BROAD_CONTEXT_ONLY", 0),
                "not_captured": status_counts.get("NOT_CAPTURED", 0),
            },
            "evidence_status_counts": dict(status_counts.most_common()),
            "outcome_class_counts": dict(outcome_counts.most_common()),
        },
        "boolean_signal_scorecard": bool_scores,
        "attribution_source_scorecard": attribution_scores,
        "case_event_ids": [row.get("event_id") for row in case_rows],
        "source_coverage": {
            "source_values_examined": dict(source_examined.most_common()),
            "source_values_winner_aligned": dict(source_matched.most_common()),
        },
    }
    payload["_rows"] = {
        "utilization": util_rows,
        "signals": signal_rows,
        "case_rows": case_rows,
        "attribution_by_event": attribution_by_event,
    }
    return payload, paths


def main() -> None:
    args = _parse_args()
    window_root = _resolve_path(args.window_root)
    final_docs_dir = _resolve_path(args.final_docs_dir)
    payload, paths = build_payload(window_root, final_docs_dir, case_limit=args.case_limit)

    rows = payload.pop("_rows")
    util_rows = rows["utilization"]
    signal_rows = rows["signals"]
    case_rows = rows["case_rows"]
    attribution_by_event = rows["attribution_by_event"]
    bool_scores = payload["boolean_signal_scorecard"]
    attribution_scores = payload["attribution_source_scorecard"]
    source_examined = Counter(payload["source_coverage"]["source_values_examined"])
    source_matched = Counter(payload["source_coverage"]["source_values_winner_aligned"])

    _write_csv(paths["util_csv"], util_rows, force=args.force)
    _write_csv(paths["signal_csv"], signal_rows, force=args.force)
    _write_text(paths["audit_md"], _render_audit_markdown(payload, paths), force=args.force)
    _write_json(paths["audit_json"], payload, force=args.force)
    _write_text(
        paths["signal_md"],
        _render_signal_scorecard(
            bool_scores=bool_scores,
            attribution_scores=attribution_scores,
            source_examined=source_examined,
            source_matched=source_matched,
            util_rows=util_rows,
            signal_rows=signal_rows,
        ),
        force=args.force,
    )
    _write_text(paths["case_md"], _render_case_dossiers(case_rows, attribution_by_event), force=args.force)
    _write_text(
        paths["redesign_md"],
        _render_redesign_lessons(util_rows=util_rows, bool_scores=bool_scores, attribution_scores=attribution_scores),
        force=args.force,
    )
    _write_text(paths["dictionary_md"], _render_dictionary(paths), force=args.force)
    _write_text(paths["protocol_md"], _render_protocol(), force=args.force)

    for key in ("util_csv", "signal_csv", "audit_md", "signal_md", "case_md", "redesign_md", "dictionary_md", "protocol_md", "audit_json"):
        print(f"Wrote: {safe_rel(paths[key])}")


if __name__ == "__main__":
    main()
