#!/usr/bin/env python3
"""Build a shadow Decision Policy Layer artifact from Brain 2 review objects.

This is intentionally read-only and shadow-mode. It does not replace current
downstream consumers or form combinations. Its job is to convert the current
Brain 1 + Brain 2 evidence stack into explicit decision records:

- posture: PLAY / WATCH / SKIP
- mode: boxed / vt_box / perm_only / hybrid
- cap class: low / medium / high
- translator route: boxed / vt_box / straight / none

The goal is to let the branch learn policy behavior without prematurely
allowing the policy layer to control runtime outputs.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.tools.brain2_rank_contract import (
    DISPLAY_ORDER_SOURCE_INPUT_ROSTER,
    RANK_INTEGRITY_INVALID_STATIC_ORDER,
    analytical_rank,
    analytical_score,
    display_order_contract_from_row,
    rank_contract_from_row,
    rank_signal_is_valid,
    unavailable_rank_contract,
)


def _read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8", errors="replace"))


def _safe_rel(path: Path, repo_root: Path = REPO_ROOT) -> str:
    try:
        return str(path.resolve().relative_to(repo_root.resolve()))
    except Exception:
        return str(path)


def _slugify(value: str) -> str:
    lowered = re.sub(r"[^a-zA-Z0-9]+", "_", str(value or "").strip()).strip("_").lower()
    return lowered or "board"


def _to_int(value: object, default: int = 0) -> int:
    try:
        text = str(value or "").strip()
        if not text:
            return int(default)
        return int(float(text))
    except Exception:
        return int(default)


def _ordered_unique(values: Iterable[str]) -> List[str]:
    seen = set()
    out: List[str] = []
    for value in values:
        text = str(value or "").strip()
        if not text or text in seen:
            continue
        seen.add(text)
        out.append(text)
    return out


def _top_slice(values: Sequence[str], limit: int) -> List[str]:
    return _ordered_unique(list(values)[: max(0, int(limit))])


def _best_alert(summary: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    rows = summary.get("top_profit_alerts") if isinstance(summary.get("top_profit_alerts"), list) else []
    alerts = [row for row in rows if isinstance(row, dict)]
    if not alerts:
        return None
    alerts.sort(
        key=lambda row: (
            -_to_int(row.get("strength"), 0),
            0 if str(row.get("variant") or "") == "Combined" else 1,
            str(row.get("alert_id") or ""),
        )
    )
    return alerts[0]


def _best_blackapple_status(summary: Dict[str, Any]) -> str:
    rows = summary.get("blackapple_statuses") if isinstance(summary.get("blackapple_statuses"), list) else []
    statuses = [str(row.get("status") or "").upper() for row in rows if isinstance(row, dict)]
    if "ALERT" in statuses:
        return "ALERT"
    if "WATCH" in statuses:
        return "WATCH"
    if "OFF" in statuses:
        return "OFF"
    return ""


def _best_compound(summary: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    rows = summary.get("compound_events_top") if isinstance(summary.get("compound_events_top"), list) else []
    events = [row for row in rows if isinstance(row, dict)]
    if not events:
        return None
    events.sort(
        key=lambda row: (
            -_to_int(row.get("priority"), 0),
            -_to_int(row.get("strength_max"), 0),
            str(row.get("variant") or ""),
        )
    )
    return events[0]


def _has_due_double_pressure(summary: Dict[str, Any]) -> bool:
    rows = summary.get("due_double_families") if isinstance(summary.get("due_double_families"), list) else []
    for row in rows:
        if not isinstance(row, dict):
            continue
        if _to_int(row.get("draws_since_double"), 0) > 0:
            return True
    return False


def _consensus_signal(summary: Dict[str, Any]) -> bool:
    ctx = summary.get("r_consensus_context") if isinstance(summary.get("r_consensus_context"), dict) else {}
    if bool(ctx.get("available")) and _to_int(ctx.get("event_count"), 0) > 0:
        return True
    best_alert = _best_alert(summary)
    if isinstance(best_alert, dict):
        badges = [str(badge).upper() for badge in (best_alert.get("badges") or []) if str(badge)]
        if any("CONS" in badge for badge in badges):
            return True
    best_compound = _best_compound(summary)
    if isinstance(best_compound, dict):
        tags = [str(tag).upper() for tag in (best_compound.get("watchlist_tags") or []) if str(tag)]
        if any("CONS" in tag for tag in tags):
            return True
    return False


def _straight_signal(summary: Dict[str, Any]) -> bool:
    best_alert = _best_alert(summary)
    if isinstance(best_alert, dict):
        suggested = str(best_alert.get("suggested") or "").upper()
        if "STRAIGHT" in suggested or "PERM" in suggested:
            return True
    notes = summary.get("positional_signal_notes") if isinstance(summary.get("positional_signal_notes"), list) else []
    for note in notes:
        upper = str(note or "").upper()
        if "STRAIGHT" in upper or "PERM" in upper:
            return True
    rows = summary.get("positional_shortlist_top") if isinstance(summary.get("positional_shortlist_top"), list) else []
    for row in rows:
        if not isinstance(row, dict):
            continue
        tags = [str(tag).upper() for tag in (row.get("tags") or []) if str(tag)]
        if any("STRAIGHT" in tag or "PERM" in tag for tag in tags):
            return True
    return False


def _survivor_regime(summary: Dict[str, Any]) -> Dict[str, Any]:
    regime = summary.get("state_regime") if isinstance(summary.get("state_regime"), dict) else {}
    return {
        "survivor_pressure": bool(regime.get("survivor_pressure")),
        "survivor_progression": bool(regime.get("survivor_progression")),
        "last_remaining": bool(regime.get("last_remaining")),
        "hidden_terminal_support": bool(regime.get("hidden_terminal_support")),
        "survivor_frontier_count": _to_int(regime.get("survivor_frontier_count"), 0),
        "survivor_progression_count": _to_int(regime.get("survivor_progression_count"), 0),
        "last_remaining_rows": _to_int(regime.get("last_remaining_rows"), 0),
    }


def _mode_from_signals(summary: Dict[str, Any], scoreboard_row: Dict[str, Any], posture: str) -> str:
    if posture == "SKIP":
        return "boxed"

    regime = summary.get("state_regime") if isinstance(summary.get("state_regime"), dict) else {}
    survivor = _survivor_regime(summary)
    best_alert = _best_alert(summary)
    alert_suggested = str(best_alert.get("suggested") or "").upper() if isinstance(best_alert, dict) else ""
    straight_signal = _straight_signal(summary)
    vtrac_alignment = str(regime.get("vtrac_alignment") or "").lower()
    watchlist_indices = summary.get("watchlist_indices") if isinstance(summary.get("watchlist_indices"), list) else []
    r_consensus = summary.get("r_consensus_context") if isinstance(summary.get("r_consensus_context"), dict) else {}

    boxed_score = 0
    vt_box_score = 0
    straight_score = 0

    if "BOX" in alert_suggested:
        boxed_score += 3
    if _has_due_double_pressure(summary):
        boxed_score += 2
    if bool(regime.get("double_heavy")):
        boxed_score += 2
    if str(scoreboard_row.get("targeting_bucket") or "") == "tight_core":
        boxed_score += 1
    if survivor["survivor_pressure"]:
        boxed_score += 2
    if survivor["last_remaining"]:
        boxed_score += 2
    if survivor["survivor_progression"]:
        boxed_score += 1
    if bool(r_consensus.get("trial_eligible")) and _to_int(r_consensus.get("two_digit_count"), 0) > 0:
        boxed_score += 1

    if vtrac_alignment == "aligned" and watchlist_indices:
        vt_box_score += 2
    if len(watchlist_indices) >= 2:
        vt_box_score += 1
    if str(scoreboard_row.get("role") or "") in {"shared_host", "clean_host"}:
        vt_box_score += 1
    if survivor["hidden_terminal_support"] and vtrac_alignment == "aligned":
        vt_box_score += 1
    if survivor["last_remaining"] and summary.get("survivor_last_remaining_vtrac_indices"):
        vt_box_score += 1
    if bool(r_consensus.get("trial_eligible")) and (r_consensus.get("cross_variant_tail_values") or []) and vtrac_alignment == "aligned":
        vt_box_score += 1

    if straight_signal:
        straight_score += 3
    if "STRAIGHT" in alert_suggested or "PERM" in alert_suggested:
        straight_score += 2

    if posture == "WATCH":
        straight_score = max(0, straight_score - 1)

    if boxed_score > 0 and straight_score > 0 and abs(boxed_score - straight_score) <= 1:
        return "hybrid"
    if boxed_score >= vt_box_score and boxed_score >= straight_score:
        return "boxed"
    if vt_box_score >= straight_score:
        return "vt_box"
    return "perm_only"


def _cap_class(scoreboard_row: Dict[str, Any], posture: str) -> str:
    if not rank_signal_is_valid(scoreboard_row):
        return "unavailable"
    if posture != "PLAY":
        return "not_applicable"
    priority = analytical_score(scoreboard_row) or 0.0
    overlap = _to_int(scoreboard_row.get("overlap_score"), 0)
    tracker_posture = str(scoreboard_row.get("tracker_posture") or "")
    spent_status = str(scoreboard_row.get("spent_status") or "")
    if (
        priority >= 40
        and overlap <= 35
        and tracker_posture in {"tracker-strong", "tracker-rich"}
        and spent_status == "mostly_unspent"
    ):
        return "high"
    if priority >= 28:
        return "medium"
    return "low"


def _board_priority(scoreboard_row: Dict[str, Any]) -> str:
    score_rank = analytical_rank(scoreboard_row)
    if score_rank is None:
        return "unavailable"
    if score_rank <= 2:
        return "tier1"
    if score_rank <= 4:
        return "tier2"
    return "tier3"


def _posture(scoreboard_row: Dict[str, Any]) -> Tuple[str, List[str]]:
    blockers: List[str] = []
    role = str(scoreboard_row.get("role") or "")
    spent_status = str(scoreboard_row.get("spent_status") or "")
    evening_bias = str(scoreboard_row.get("evening_bias") or "")
    targeting_bucket = str(scoreboard_row.get("targeting_bucket") or "")
    priority = analytical_score(scoreboard_row) or 0.0
    tracker_posture = str(scoreboard_row.get("tracker_posture") or "")
    direct_cross_hits = _to_int(scoreboard_row.get("direct_cross_hits"), 0)

    if spent_status == "locally_spent" or evening_bias == "de_emphasize":
        blockers.append("LOCAL_SPENT")
        return "SKIP", blockers

    if not rank_signal_is_valid(scoreboard_row):
        blockers.append("RANK_SIGNAL_UNAVAILABLE")
        return "UNRESOLVED", blockers

    if targeting_bucket == "tight_core" and spent_status == "mostly_unspent" and priority >= 24:
        return "PLAY", blockers

    if targeting_bucket == "tight_core" and evening_bias in {"still_live", "soft_watch"}:
        blockers.append("SPENT_OR_SPLIT")
        return "WATCH", blockers

    if targeting_bucket == "small_shoulder":
        blockers.append("SHOULDER_STATE")
        return "WATCH", blockers

    if targeting_bucket in {"watch_only", "echo_only"}:
        if direct_cross_hits > 0 or tracker_posture in {"tracker-strong", "tracker-rich"}:
            blockers.append("WATCH_RELATIONSHIP")
            return "WATCH", blockers
        blockers.append("LOW_BOARD_PRIORITY")
        return "SKIP", blockers

    if role == "echo":
        blockers.append("ECHO_STATE")
        return "WATCH", blockers

    blockers.append("LOW_BOARD_PRIORITY")
    return "SKIP", blockers


def _translator_route(mode: str, posture: str) -> str:
    if posture != "PLAY":
        return "none"
    if mode == "vt_box":
        return "vt_box"
    if mode == "perm_only":
        return "straight"
    if mode == "hybrid":
        return "boxed"
    return "boxed"


def _carryover_action(scoreboard_row: Dict[str, Any], posture: str) -> str:
    spent_status = str(scoreboard_row.get("spent_status") or "")
    if spent_status == "locally_spent":
        return "close"
    if not rank_signal_is_valid(scoreboard_row):
        return "unresolved"
    if posture == "PLAY" and spent_status == "mostly_unspent":
        return "new"
    if posture == "WATCH":
        return "continue"
    if spent_status == "cross_state_spent":
        return "continue"
    return "ignore"


def _reason_codes(summary: Dict[str, Any], scoreboard_row: Dict[str, Any], posture: str, mode: str) -> List[str]:
    out: List[str] = []
    regime = summary.get("state_regime") if isinstance(summary.get("state_regime"), dict) else {}
    survivor = _survivor_regime(summary)
    r_consensus = summary.get("r_consensus_context") if isinstance(summary.get("r_consensus_context"), dict) else {}
    role = str(scoreboard_row.get("role") or "")
    spent_status = str(scoreboard_row.get("spent_status") or "")
    targeting_bucket = str(scoreboard_row.get("targeting_bucket") or "")

    if role in {"clean_host", "shared_host"}:
        out.append("HOST_STATE")
    if role == "echo":
        out.append("ECHO_STATE")
    if targeting_bucket == "tight_core":
        out.append("TIGHT_CORE")
    if spent_status == "mostly_unspent":
        out.append("MOSTLY_UNSPENT")
    elif spent_status == "cross_state_spent":
        out.append("CROSS_STATE_SPENT")
    elif spent_status == "lane_spent":
        out.append("LANE_SPENT")
    elif spent_status == "locally_spent":
        out.append("LOCAL_SPENT")

    if bool(regime.get("double_heavy")):
        out.append("DOUBLE_HEAVY")
    if bool(regime.get("context_reinforced")):
        out.append("CTX_REINFORCED")
    if str(regime.get("vtrac_alignment") or "").lower() == "aligned":
        out.append("VTRAC_ALIGNED")
    if survivor["survivor_pressure"]:
        out.append("SURVIVOR_PRESSURE")
    if survivor["survivor_progression"]:
        out.append("SURVIVOR_PROGRESSION")
    if survivor["last_remaining"]:
        out.append("LAST_REMAINING")
    if survivor["hidden_terminal_support"]:
        out.append("HIDDEN_TERMINAL_SUPPORT")

    best_alert = _best_alert(summary)
    if isinstance(best_alert, dict):
        out.append("PROFIT_ALERT")
        if _to_int(best_alert.get("strength"), 0) >= 4:
            out.append("PROFIT_ALERT_STRONG")
        if _consensus_signal(summary):
            out.append("CONSENSUS_EVENT")
    elif _consensus_signal(summary):
        out.append("CONSENSUS_EVENT")

    if bool(r_consensus.get("available")) and _to_int(r_consensus.get("event_count"), 0) > 0:
        out.append("R_CONSENSUS_PRESENT")
    if _to_int(r_consensus.get("event_count"), 0) > 1:
        out.append("R_CONSENSUS_MULTI_EVENT")
    if r_consensus.get("cross_variant_tail_values"):
        out.append("R_CONSENSUS_CROSS_VARIANT")
    if bool(r_consensus.get("trial_eligible")):
        out.append("R_CONSENSUS_TRIAL_ELIGIBLE")

    ba_status = _best_blackapple_status(summary)
    if ba_status == "ALERT":
        out.append("BA_ALERT")
    elif ba_status == "WATCH":
        out.append("BA_WATCH")

    if _best_compound(summary):
        out.append("COMPOUND_EVENT")
    if _has_due_double_pressure(summary):
        out.append("DUE_DOUBLE_ACTIVE")
    if summary.get("positional_signal_notes"):
        out.append("POSITIONAL_SIGNAL")
    if _to_int(scoreboard_row.get("direct_cross_hits"), 0) > 0:
        out.append("DIRECT_CROSS_RECEIPT")

    if mode == "boxed":
        out.append("MODE_BOXED")
    elif mode == "vt_box":
        out.append("MODE_VT_BOX")
    elif mode == "perm_only":
        out.append("MODE_PERM_ONLY")
    elif mode == "hybrid":
        out.append("MODE_HYBRID")

    if posture == "PLAY":
        out.append("PLAY_STATE")
    elif posture == "WATCH":
        out.append("WATCH_STATE")
    elif posture == "SKIP":
        out.append("SKIP_STATE")
    else:
        out.extend(["RANK_SIGNAL_UNAVAILABLE", "UNRESOLVED_STATE"])
    return _ordered_unique(out)


def _environment_object(summary: Dict[str, Any], scoreboard_row: Dict[str, Any]) -> Dict[str, Any]:
    regime = summary.get("state_regime") if isinstance(summary.get("state_regime"), dict) else {}
    survivor = _survivor_regime(summary)
    r_consensus = summary.get("r_consensus_context") if isinstance(summary.get("r_consensus_context"), dict) else {}
    return {
        "targeting_bucket": str(scoreboard_row.get("targeting_bucket") or ""),
        "role": str(scoreboard_row.get("role") or ""),
        "spent_status": str(scoreboard_row.get("spent_status") or ""),
        "evening_bias": str(scoreboard_row.get("evening_bias") or ""),
        "tracker_posture": str(scoreboard_row.get("tracker_posture") or ""),
        "legacy_priority_score": _to_int(
            scoreboard_row.get("legacy_priority_score") or scoreboard_row.get("priority_score"),
            0,
        ),
        "analytical_rank": analytical_rank(scoreboard_row),
        "analytical_score": analytical_score(scoreboard_row),
        "rank_integrity_status": rank_contract_from_row(scoreboard_row).get("rank_integrity_status"),
        "overlap_score": _to_int(scoreboard_row.get("overlap_score"), 0),
        "direct_cross_hits": _to_int(scoreboard_row.get("direct_cross_hits"), 0),
        "primary_overlap_hits": _to_int(scoreboard_row.get("primary_overlap_hits"), 0),
        "dominant_canonical": str(regime.get("dominant_canonical") or ""),
        "dominant_vtrac_index": str(regime.get("dominant_vtrac_index") or ""),
        "double_heavy": bool(regime.get("double_heavy")),
        "context_reinforced": bool(regime.get("context_reinforced")),
        "vtrac_alignment": str(regime.get("vtrac_alignment") or ""),
        "survivor_pressure": survivor["survivor_pressure"],
        "survivor_progression": survivor["survivor_progression"],
        "last_remaining": survivor["last_remaining"],
        "hidden_terminal_support": survivor["hidden_terminal_support"],
        "survivor_frontier_count": survivor["survivor_frontier_count"],
        "survivor_progression_count": survivor["survivor_progression_count"],
        "last_remaining_rows": survivor["last_remaining_rows"],
        "tail_consensus_present": bool(regime.get("tail_consensus_present")),
        "tail_consensus_value": str(regime.get("tail_consensus_value") or ""),
        "tail_consensus_column": str(regime.get("tail_consensus_column") or ""),
        "consensus_strength_class": str(regime.get("consensus_strength_class") or r_consensus.get("signal_strength_class") or ""),
        "consensus_trial_eligible": bool(regime.get("consensus_trial_eligible") or r_consensus.get("trial_eligible")),
        "r_consensus_event_count": _to_int(r_consensus.get("event_count"), 0),
        "r_consensus_cross_variant_tail_count": len(r_consensus.get("cross_variant_tail_values") or []),
        "profit_alert_hint": str(scoreboard_row.get("profit_alert_hint") or "-"),
        "compound_event_hint": str(scoreboard_row.get("compound_event_hint") or "-"),
        "positional_hint": str(scoreboard_row.get("positional_hint") or "-"),
        "due_double_hint": str(scoreboard_row.get("due_double_hint") or "-"),
        "blackapple_hint": str(scoreboard_row.get("best_blackapple") or "-"),
    }


def _candidate_focus(summary: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "primary_cluster": {
            "canonicals": _top_slice(summary.get("primary_canonicals") or [], 6),
            "vtrac_indices": _top_slice(summary.get("primary_vtrac_indices") or [], 6),
            "families": _top_slice(summary.get("dominant_families") or [], 4),
            "context_reinforced_canonicals": _top_slice(summary.get("context_reinforced_canonicals") or [], 4),
            "survivor_frontier_canonicals": _top_slice(summary.get("survivor_frontier_canonicals") or [], 4),
            "survivor_last_remaining_canonicals": _top_slice(summary.get("survivor_last_remaining_canonicals") or [], 4),
            "r_consensus_support_canonicals": _top_slice(summary.get("r_consensus_support_canonicals") or [], 4),
        },
        "secondary_cluster": {
            "canonicals": _top_slice(summary.get("secondary_canonicals") or [], 6),
            "vtrac_indices": _top_slice(summary.get("secondary_vtrac_indices") or [], 6),
            "context_only_pressure": _top_slice(summary.get("context_only_pressure") or [], 4),
            "profit_alert_implied_canonicals": _top_slice(summary.get("profit_alert_implied_canonicals") or [], 6),
            "survivor_terminal_profiles": _top_slice(summary.get("survivor_terminal_profiles") or [], 4),
            "r_consensus_top_tail_values": _top_slice(summary.get("r_consensus_top_tail_values") or [], 4),
            "r_consensus_support_vtrac_indices": _top_slice(summary.get("r_consensus_support_vtrac_indices") or [], 4),
        },
    }


def build_shadow_decision_policy_payload(
    *,
    overlay_payload: Dict[str, Any],
    scoreboard_payload: Dict[str, Any],
) -> Dict[str, Any]:
    overlay_meta = overlay_payload.get("metadata") if isinstance(overlay_payload.get("metadata"), dict) else {}
    scoreboard_meta = scoreboard_payload.get("metadata") if isinstance(scoreboard_payload.get("metadata"), dict) else {}
    summaries = overlay_payload.get("state_summaries") if isinstance(overlay_payload.get("state_summaries"), list) else []
    summary_by_state = {
        str(row.get("state_key") or ""): row
        for row in summaries
        if isinstance(row, dict) and str(row.get("state_key") or "").strip()
    }
    scoreboard_rows = scoreboard_payload.get("scoreboard_rows") if isinstance(scoreboard_payload.get("scoreboard_rows"), list) else []

    state_decisions: List[Dict[str, Any]] = []
    for row in scoreboard_rows:
        if not isinstance(row, dict):
            continue
        state_key = str(row.get("state_key") or "")
        summary = summary_by_state.get(state_key, {})
        rank_contract = rank_contract_from_row(row)
        posture, blockers = _posture(row)
        mode = _mode_from_signals(summary, row, posture)
        cap_class = _cap_class(row, posture)
        decision = {
            "state_key": state_key,
            "input_order": _to_int(row.get("input_order") or row.get("input_rank"), len(state_decisions) + 1),
            **display_order_contract_from_row(row),
            "legacy_static_rank": _to_int(row.get("legacy_static_rank") or row.get("score_rank"), len(state_decisions) + 1),
            "legacy_priority_score": _to_int(row.get("legacy_priority_score") or row.get("priority_score"), 0),
            "score_rank": _to_int(row.get("score_rank"), len(state_decisions) + 1),
            "analytical_rank": rank_contract.get("analytical_rank"),
            "analytical_score": rank_contract.get("analytical_score"),
            "rank_contract": rank_contract,
            "board_priority": _board_priority(row),
            "posture": posture,
            "mode": mode,
            "cap_class": cap_class,
            "translator_route": _translator_route(mode, posture),
            "carryover_action": _carryover_action(row, posture),
            "reason_codes": _reason_codes(summary, row, posture, mode),
            "blockers": _ordered_unique(blockers),
            "environment": _environment_object(summary, row),
            "candidate_focus": _candidate_focus(summary),
        }
        state_decisions.append(decision)

    play_states = [row["state_key"] for row in state_decisions if row.get("posture") == "PLAY"]
    watch_states = [row["state_key"] for row in state_decisions if row.get("posture") == "WATCH"]
    skip_states = [row["state_key"] for row in state_decisions if row.get("posture") == "SKIP"]
    unresolved_states = [row["state_key"] for row in state_decisions if row.get("posture") == "UNRESOLVED"]

    return {
        "schema_version": "shadow_decision_policy_v1",
        "metadata": {
            "results_date": overlay_meta.get("results_date"),
            "board_name": overlay_meta.get("board_name"),
            "profile": overlay_meta.get("profile") or scoreboard_meta.get("profile"),
            "experiment_tag": overlay_meta.get("experiment_tag") or scoreboard_meta.get("experiment_tag"),
            "mode": "shadow",
            "rank_integrity_status": RANK_INTEGRITY_INVALID_STATIC_ORDER,
        },
        "rank_contract": unavailable_rank_contract(),
        "display_order_contract": {
            "display_order_source": DISPLAY_ORDER_SOURCE_INPUT_ROSTER,
            "display_order_is_analytical": False,
        },
        "artifacts": {
            "overlay_board_name": overlay_meta.get("board_name"),
            "scoreboard_source": scoreboard_meta.get("generated_from_overlay"),
        },
        "state_decisions": state_decisions,
        "shadow_verdict": {
            "top_play_state": play_states[0] if play_states else None,
            "top_watch_state": watch_states[0] if watch_states else None,
            "play_states": play_states,
            "watch_states": watch_states,
            "skip_states": skip_states,
            "unresolved_states": unresolved_states,
            "rank_dependent_decisions_available": False,
        },
    }


def build_shadow_decision_policy_markdown(payload: Dict[str, Any]) -> str:
    metadata = payload.get("metadata") if isinstance(payload.get("metadata"), dict) else {}
    state_decisions = payload.get("state_decisions") if isinstance(payload.get("state_decisions"), list) else []
    verdict = payload.get("shadow_verdict") if isinstance(payload.get("shadow_verdict"), dict) else {}

    lines = [
        f"# Shadow Decision Policy — {metadata.get('board_name') or 'Board'}",
        "",
        "Purpose: shadow-only decision policy receipt derived from the existing Brain 2 overlay and scoreboard.",
        "",
        "**RANK INTEGRITY STATUS: `INVALID_STATIC_ORDER`.** Rank-dependent posture, tier, cap, and route decisions are unresolved; structural evidence remains visible.",
        "",
        "**DISPLAY ORDER:** `INPUT_ROSTER_NON_ANALYTICAL`; navigation only, with no analytical meaning.",
        "",
        "## Shadow Verdict",
        "",
        f"- top_play_state: `{verdict.get('top_play_state') or '-'}`",
        f"- top_watch_state: `{verdict.get('top_watch_state') or '-'}`",
        f"- play_states: `{', '.join(verdict.get('play_states') or []) or '-'}`",
        f"- watch_states: `{', '.join(verdict.get('watch_states') or []) or '-'}`",
        f"- skip_states: `{', '.join(verdict.get('skip_states') or []) or '-'}`",
        f"- unresolved_states: `{', '.join(verdict.get('unresolved_states') or []) or '-'}`",
        "",
        "## Decisions",
        "",
        "| Input Order | Legacy Rank | Analytical Rank | State | Posture | Mode | Cap | Route | Carryover | Reasons |",
        "|---:|---:|---:|---|---|---|---|---|---|---|",
    ]
    for row in state_decisions:
        if not isinstance(row, dict):
            continue
        lines.append(
            f"| {row.get('input_order')} | {row.get('legacy_static_rank')} | {row.get('analytical_rank') or '-'} | {row.get('state_key')} | {row.get('posture')} | {row.get('mode')} | {row.get('cap_class')} | {row.get('translator_route')} | {row.get('carryover_action')} | {', '.join(row.get('reason_codes') or []) or '-'} |"
        )

    lines.append("")
    lines.append("## Environment Notes")
    lines.append("")
    for row in state_decisions[:6]:
        if not isinstance(row, dict):
            continue
        env = row.get("environment") if isinstance(row.get("environment"), dict) else {}
        focus = row.get("candidate_focus") if isinstance(row.get("candidate_focus"), dict) else {}
        primary = focus.get("primary_cluster") if isinstance(focus.get("primary_cluster"), dict) else {}
        lines.append(f"- `{row.get('state_key')}` posture=`{row.get('posture')}` mode=`{row.get('mode')}` target=`{env.get('targeting_bucket')}` role=`{env.get('role')}` primary=`{', '.join(primary.get('canonicals') or []) or '-'}`")

    return "\n".join(lines).rstrip() + "\n"


def write_shadow_decision_policy_files(
    *,
    out_md_path: Path,
    payload: Dict[str, Any],
    write_json: bool = True,
) -> Tuple[Path, Optional[Path]]:
    out_md_path.parent.mkdir(parents=True, exist_ok=True)
    out_md_path.write_text(build_shadow_decision_policy_markdown(payload), encoding="utf-8")
    json_path: Optional[Path] = None
    if write_json:
        json_path = out_md_path.with_suffix(".json")
        json_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return out_md_path, json_path


def _default_out_name(results_date: str, board_name: str) -> str:
    return f"{results_date}__SHADOW_DECISION_POLICY__{_slugify(board_name)}.md"


def main(argv: Optional[Sequence[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Build a shadow decision policy receipt from board review artifacts.")
    ap.add_argument("--overlay-json", required=True)
    ap.add_argument("--scoreboard-json", required=True)
    ap.add_argument("--out-md", required=True)
    args = ap.parse_args(argv)

    overlay_payload = _read_json(Path(args.overlay_json))
    scoreboard_payload = _read_json(Path(args.scoreboard_json))
    payload = build_shadow_decision_policy_payload(
        overlay_payload=overlay_payload,
        scoreboard_payload=scoreboard_payload,
    )
    out_md_path, out_json_path = write_shadow_decision_policy_files(
        out_md_path=Path(args.out_md),
        payload=payload,
        write_json=True,
    )
    print(f"[ok] shadow DPL -> {_safe_rel(out_md_path)}")
    if out_json_path is not None:
        print(f"     json -> {_safe_rel(out_json_path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
