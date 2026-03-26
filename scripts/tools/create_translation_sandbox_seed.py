#!/usr/bin/env python3
"""Create a translation-sandbox companion from arena/runtime/control-arm artifacts.

This script is intentionally research-first. It does not perform live
combination forming. Its purpose is to capture the strongest near-final
cluster/candidate intelligence per state so later translator work can learn
from real runs without polluting Brain 1, Brain 2, or the current control arm.
"""

from __future__ import annotations

import argparse
import json
from collections import OrderedDict
from datetime import datetime, timezone
from pathlib import Path
import re
import sys
from typing import Any, Dict, Iterable, List, Mapping, MutableMapping, Optional, Sequence, Tuple

REPO_ROOT = Path(__file__).resolve().parents[2]
RUNS_DIR = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS_2" / "ANALYSIS_ARENA"

if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.tools.build_board_spillover_overlay import _default_out_name as _overlay_default_out_name
from scripts.tools.create_board_scoreboard import _default_out_name as _scoreboard_default_out_name
from scripts.tools.build_shadow_decision_policy import _default_out_name as _dpl_default_out_name


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _safe_rel(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT.resolve()))
    except Exception:
        return str(path)


def _read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8", errors="replace"))


def _write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _slugify(value: str) -> str:
    lowered = re.sub(r"[^a-zA-Z0-9]+", "_", str(value or "").strip()).strip("_").lower()
    return lowered or "board"


def _ordered_unique(values: Iterable[object]) -> List[str]:
    seen = set()
    out: List[str] = []
    for value in values:
        text = str(value or "").strip()
        if not text or text in seen:
            continue
        seen.add(text)
        out.append(text)
    return out


def _to_int(value: object, default: int = 0) -> int:
    try:
        text = str(value or "").strip()
        if not text:
            return int(default)
        return int(float(text))
    except Exception:
        return int(default)


def _top_dicts(values: Sequence[Mapping[str, Any]], limit: int) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for row in values[: max(0, int(limit))]:
        if isinstance(row, Mapping):
            out.append(dict(row))
    return out


def _profile_suffix(profile: str) -> str:
    profile_text = str(profile or "mixed").strip()
    return "" if profile_text == "mixed" else f"__{profile_text}"


def _tag_suffix(experiment_tag: str) -> str:
    tag = str(experiment_tag or "").strip()
    return f"__{tag}" if tag else ""


def _default_state_out_name(profile: str, experiment_tag: str) -> str:
    return f"translation_sandbox_seed{_profile_suffix(profile)}{_tag_suffix(experiment_tag)}.md"


def _default_manifest_out_name(results_date: str, board_name: str) -> str:
    return f"{results_date}__TRANSLATION_SANDBOX_SEED__{_slugify(board_name)}.md"


def _resolve_runs_json_paths(
    *,
    results_date: str,
    board_name: str,
    runs_dir: Path,
) -> Tuple[Path, Path, Path]:
    overlay_json = runs_dir / _overlay_default_out_name(results_date, board_name)
    scoreboard_json = runs_dir / _scoreboard_default_out_name(
        {
            "results_date": results_date,
            "generated_from_overlay": board_name,
        }
    ).replace(".md", ".json")
    dpl_json = runs_dir / _dpl_default_out_name(results_date, board_name).replace(".md", ".json")
    return overlay_json, scoreboard_json, dpl_json


def _collect_seed_rows(source_map: Mapping[str, Sequence[object]], *, limit: int) -> List[Dict[str, Any]]:
    support_map: MutableMapping[str, set[str]] = OrderedDict()
    first_seen: Dict[str, int] = {}
    idx = 0
    for source_tag, values in source_map.items():
        for value in values:
            text = str(value or "").strip()
            if not text:
                continue
            if text not in support_map:
                support_map[text] = set()
                first_seen[text] = idx
                idx += 1
            support_map[text].add(str(source_tag))
    rows = [
        {
            "value": value,
            "support_count": len(tags),
            "source_tags": sorted(tags),
        }
        for value, tags in support_map.items()
    ]
    rows.sort(key=lambda row: (-_to_int(row.get("support_count"), 0), first_seen.get(str(row.get("value") or ""), 999999), str(row.get("value") or "")))
    return rows[: max(0, int(limit))]


def _candidate_universe_path(*, state_dir: Path, profile: str, experiment_tag: str) -> Optional[Path]:
    suffix = _profile_suffix(profile)
    tag_suffix = _tag_suffix(experiment_tag)
    exact = state_dir / f"candidate_universe{suffix}{tag_suffix}.json"
    if exact.exists():
        return exact
    for pattern in [f"candidate_universe{suffix}*.json", "candidate_universe*.json"]:
        candidates = sorted(state_dir.glob(pattern))
        if candidates:
            return candidates[0]
    return None


def _play_card_path(*, state_dir: Path, profile: str, experiment_tag: str) -> Optional[Path]:
    suffix = _profile_suffix(profile)
    tag_suffix = _tag_suffix(experiment_tag)
    exact = state_dir / f"play_card{suffix}{tag_suffix}.json"
    if exact.exists():
        return exact
    for pattern in [f"play_card{suffix}*.json", "play_card*.json"]:
        candidates = sorted(state_dir.glob(pattern))
        if candidates:
            return candidates[0]
    return None


def _summarize_candidate_universe(payload: Optional[Mapping[str, Any]], path: Optional[Path]) -> Dict[str, Any]:
    if not isinstance(payload, Mapping):
        return {
            "available": False,
            "path": _safe_rel(path) if isinstance(path, Path) else None,
            "union_combos_count": 0,
            "pack_count": 0,
            "top_canonicals": [],
            "top_packs": [],
        }

    packs = payload.get("packs") if isinstance(payload.get("packs"), list) else []
    aggregate: MutableMapping[str, Dict[str, Any]] = OrderedDict()
    for row in packs:
        if not isinstance(row, Mapping):
            continue
        method_id = str(row.get("method_id") or row.get("pack_id") or "").strip()
        variant = str(row.get("variant") or "").strip()
        play_mode = str(row.get("play_mode") or "").strip()
        why_tags = _ordered_unique(row.get("why_tags") or [])
        for canonical in _ordered_unique(row.get("canonicals") or []):
            entry = aggregate.setdefault(
                canonical,
                {
                    "canonical": canonical,
                    "support_packs": 0,
                    "methods": set(),
                    "variants": set(),
                    "play_modes": set(),
                    "why_tags": set(),
                },
            )
            entry["support_packs"] += 1
            if method_id:
                entry["methods"].add(method_id)
            if variant:
                entry["variants"].add(variant)
            if play_mode:
                entry["play_modes"].add(play_mode)
            entry["why_tags"].update(why_tags)

    canonicals: List[Dict[str, Any]] = []
    for canonical, row in aggregate.items():
        canonicals.append(
            {
                "canonical": canonical,
                "support_packs": _to_int(row.get("support_packs"), 0),
                "methods": sorted(row.get("methods") or []),
                "variants": sorted(row.get("variants") or []),
                "play_modes": sorted(row.get("play_modes") or []),
                "why_tags": sorted(row.get("why_tags") or []),
            }
        )
    canonicals.sort(
        key=lambda row: (
            -_to_int(row.get("support_packs"), 0),
            -len(row.get("methods") or []),
            -len(row.get("variants") or []),
            str(row.get("canonical") or ""),
        )
    )

    top_packs: List[Dict[str, Any]] = []
    for row in packs:
        if not isinstance(row, Mapping):
            continue
        top_packs.append(
            {
                "pack_id": row.get("pack_id"),
                "method_id": row.get("method_id"),
                "variant": row.get("variant"),
                "play_mode": row.get("play_mode"),
                "canonicals": _ordered_unique(row.get("canonicals") or [])[:8],
                "combos_count": _to_int(row.get("combos_count"), len(row.get("combos") or [])),
                "cost_units": _to_int(row.get("cost_units"), 0),
                "why_tags": _ordered_unique(row.get("why_tags") or [])[:6],
            }
        )
    top_packs.sort(
        key=lambda row: (
            -_to_int(row.get("combos_count"), 0),
            -len(row.get("canonicals") or []),
            str(row.get("method_id") or row.get("pack_id") or ""),
        )
    )

    return {
        "available": True,
        "path": _safe_rel(path) if isinstance(path, Path) else None,
        "union_combos_count": _to_int(payload.get("union_combos_count"), 0),
        "pack_count": len(packs),
        "top_canonicals": canonicals[:12],
        "top_packs": top_packs[:10],
    }


def _summarize_play_card(payload: Optional[Mapping[str, Any]], path: Optional[Path]) -> Dict[str, Any]:
    if not isinstance(payload, Mapping):
        return {
            "available": False,
            "path": _safe_rel(path) if isinstance(path, Path) else None,
            "ranked_candidates_top": [],
            "strategy_cards": [],
            "budgeted_canonicals_top": [],
        }

    ranked = payload.get("ranked_candidates") if isinstance(payload.get("ranked_candidates"), list) else []
    ranked_top = []
    for row in ranked[:15]:
        if not isinstance(row, Mapping):
            continue
        ranked_top.append(
            {
                "combo": row.get("combo"),
                "canonical": row.get("canonical"),
                "score": row.get("score"),
                "support_packs_count": row.get("support_packs_count"),
                "support_methods": _ordered_unique(row.get("support_methods") or []),
                "support_variants": _ordered_unique(row.get("support_variants") or []),
            }
        )

    strategies = payload.get("strategies") if isinstance(payload.get("strategies"), Mapping) else {}
    strategy_cards: List[Dict[str, Any]] = []
    budgeted_canonicals: List[str] = []
    for strategy_id, cards in sorted(strategies.items(), key=lambda item: str(item[0])):
        if not isinstance(cards, Mapping):
            continue
        for budget_id, card in sorted(cards.items(), key=lambda item: str(item[0])):
            if not isinstance(card, Mapping):
                continue
            canonicals = _ordered_unique(card.get("boxed_canonicals") or [])
            budgeted_canonicals.extend(canonicals)
            strategy_cards.append(
                {
                    "strategy_id": strategy_id,
                    "budget_id": budget_id,
                    "combos_count": _to_int(card.get("combos_count"), len(card.get("combos") or [])),
                    "boxed_canonicals_top": canonicals[:8],
                }
            )

    return {
        "available": True,
        "path": _safe_rel(path) if isinstance(path, Path) else None,
        "ranked_candidates_top": ranked_top,
        "strategy_cards": strategy_cards[:18],
        "budgeted_canonicals_top": _ordered_unique(budgeted_canonicals)[:20],
    }


def _top_shortlist_canonicals(rows: Sequence[Mapping[str, Any]]) -> List[str]:
    out: List[str] = []
    for row in rows:
        canonical = str(row.get("canonical") or "").strip()
        if canonical:
            out.append(canonical)
    return _ordered_unique(out)


def _top_shortlist_combos(rows: Sequence[Mapping[str, Any]]) -> List[str]:
    out: List[str] = []
    for row in rows:
        combo = str(row.get("combo") or "").strip()
        if combo:
            out.append(combo)
    return _ordered_unique(out)


def _open_translator_hypotheses(
    *,
    decision_row: Mapping[str, Any],
    boxed_seed: Sequence[Mapping[str, Any]],
    straight_seed: Sequence[Mapping[str, Any]],
    vt_box_seed: Sequence[Mapping[str, Any]],
    preserved_not_budgeted: Sequence[str],
) -> List[str]:
    posture = str(decision_row.get("posture") or "").upper()
    mode = str(decision_row.get("mode") or "").strip()
    cap_class = str(decision_row.get("cap_class") or "").strip()
    reason_codes = _ordered_unique(decision_row.get("reason_codes") or [])
    notes: List[str] = []
    if posture:
        notes.append(f"Shadow DPL posture is `{posture}` with mode `{mode or '-'}` and cap `{cap_class or '-'}`.")
    if boxed_seed:
        lead = boxed_seed[0]
        notes.append(
            "Diagnostic boxed seed currently centers on "
            f"`{lead.get('value')}` from `{', '.join(lead.get('source_tags') or []) or '-'}`."
        )
    if straight_seed:
        lead = straight_seed[0]
        notes.append(
            "Straight-side diagnostic seed remains bounded and review-only, led by "
            f"`{lead.get('value')}` from `{', '.join(lead.get('source_tags') or []) or '-'}`."
        )
    if vt_box_seed:
        lead = vt_box_seed[0]
        notes.append(
            "VT-box diagnostic seed currently points to VTRAC index "
            f"`{lead.get('value')}` with `{', '.join(lead.get('source_tags') or []) or '-'}` support."
        )
    if preserved_not_budgeted:
        notes.append(
            "These Candidate Universe canonicals were preserved but not budgeted by the current control arm: "
            f"`{', '.join(preserved_not_budgeted[:8])}`."
        )
    if any(code in reason_codes for code in {"R_CONSENSUS_PRESENT", "LAST_REMAINING", "HIDDEN_TERMINAL_SUPPORT"}):
        notes.append(
            "Special-event and survivor objects are present; preserve them as translator-learning signals rather than forcing immediate production conversion."
        )
    return notes[:8]


def build_translation_sandbox_state_payload(
    *,
    results_date: str,
    board_name: str,
    profile: str,
    experiment_tag: str,
    sharepacks_root: Path,
    overlay_path: Path,
    scoreboard_path: Path,
    decision_policy_path: Path,
    overlay_summary: Mapping[str, Any],
    scoreboard_row: Optional[Mapping[str, Any]],
    decision_row: Optional[Mapping[str, Any]],
    candidate_universe_payload: Optional[Mapping[str, Any]],
    candidate_universe_path: Optional[Path],
    play_card_payload: Optional[Mapping[str, Any]],
    play_card_path: Optional[Path],
) -> Dict[str, Any]:
    state_key = str(overlay_summary.get("state_key") or "").strip()
    scoreboard = dict(scoreboard_row or {})
    decision = dict(decision_row or {})
    positional_rows = [row for row in (overlay_summary.get("positional_shortlist_top") or []) if isinstance(row, Mapping)]
    candidate_summary = _summarize_candidate_universe(candidate_universe_payload, candidate_universe_path)
    play_card_summary = _summarize_play_card(play_card_payload, play_card_path)

    boxed_seed = _collect_seed_rows(
        OrderedDict(
            [
                ("brain1.primary", overlay_summary.get("primary_canonicals") or []),
                ("brain1.context_reinforced", overlay_summary.get("context_reinforced_canonicals") or []),
                ("brain1.survivor_frontier", overlay_summary.get("survivor_frontier_canonicals") or []),
                ("brain1.last_remaining", overlay_summary.get("survivor_last_remaining_canonicals") or []),
                ("brain1.r_consensus", overlay_summary.get("r_consensus_support_canonicals") or []),
                ("brain2.profit_alert_implied", overlay_summary.get("profit_alert_implied_canonicals") or []),
                ("brain2.blackapple", overlay_summary.get("blackapple_recommended_canonicals") or []),
                ("brain2.positional", _top_shortlist_canonicals(positional_rows)),
                ("brain2.due_double", overlay_summary.get("due_double_example_canonicals") or []),
                ("control_arm.cu", [row.get("canonical") for row in candidate_summary.get("top_canonicals") or []]),
                ("control_arm.play_card", [row.get("canonical") for row in play_card_summary.get("ranked_candidates_top") or []]),
            ]
        ),
        limit=16,
    )
    straight_seed = _collect_seed_rows(
        OrderedDict(
            [
                ("brain2.positional_combo", _top_shortlist_combos(positional_rows)),
                ("control_arm.play_card_ranked", [row.get("combo") for row in play_card_summary.get("ranked_candidates_top") or []]),
            ]
        ),
        limit=16,
    )
    vt_box_seed = _collect_seed_rows(
        OrderedDict(
            [
                ("brain1.primary_vtrac", overlay_summary.get("primary_vtrac_indices") or []),
                ("brain1.secondary_vtrac", overlay_summary.get("secondary_vtrac_indices") or []),
                ("brain1.survivor_vtrac", overlay_summary.get("survivor_frontier_vtrac_indices") or []),
                ("brain1.last_remaining_vtrac", overlay_summary.get("survivor_last_remaining_vtrac_indices") or []),
                ("brain1.r_consensus_vtrac", overlay_summary.get("r_consensus_support_vtrac_indices") or []),
                ("brain2.positional_vtrac", [row.get("vtrac_index") for row in positional_rows]),
            ]
        ),
        limit=12,
    )

    budgeted_canonicals = _ordered_unique(play_card_summary.get("budgeted_canonicals_top") or [])
    preserved_not_budgeted = [
        row.get("canonical")
        for row in candidate_summary.get("top_canonicals") or []
        if str(row.get("canonical") or "").strip()
        and str(row.get("canonical") or "").strip() not in set(budgeted_canonicals)
    ][:10]

    payload = {
        "schema_version": "translation_sandbox_seed_v0",
        "metadata": {
            "generated_at": _now_iso(),
            "results_date": results_date,
            "board_name": board_name,
            "state_key": state_key,
            "profile": profile,
            "experiment_tag": experiment_tag,
            "sharepacks_root": _safe_rel(sharepacks_root),
            "overlay_json": _safe_rel(overlay_path),
            "scoreboard_json": _safe_rel(scoreboard_path),
            "shadow_decision_policy_json": _safe_rel(decision_policy_path),
            "candidate_universe_path": _safe_rel(candidate_universe_path) if isinstance(candidate_universe_path, Path) else None,
            "play_card_path": _safe_rel(play_card_path) if isinstance(play_card_path, Path) else None,
        },
        "brain1_core": {
            "dominant_canonicals": _ordered_unique(overlay_summary.get("primary_canonicals") or [])[:12],
            "secondary_canonicals": _ordered_unique(overlay_summary.get("secondary_canonicals") or [])[:12],
            "dominant_families": _ordered_unique(overlay_summary.get("dominant_families") or [])[:12],
            "dominant_vtrac_indices": _ordered_unique(overlay_summary.get("primary_vtrac_indices") or [])[:12],
            "watchlist_indices": _ordered_unique(overlay_summary.get("watchlist_indices") or [])[:12],
            "context_reinforced_canonicals": _ordered_unique(overlay_summary.get("context_reinforced_canonicals") or [])[:12],
            "survivor_frontier_canonicals": _ordered_unique(overlay_summary.get("survivor_frontier_canonicals") or [])[:12],
            "survivor_last_remaining_canonicals": _ordered_unique(overlay_summary.get("survivor_last_remaining_canonicals") or [])[:12],
            "survivor_terminal_profiles": _ordered_unique(overlay_summary.get("survivor_terminal_profiles") or [])[:8],
            "r_consensus_context": dict(overlay_summary.get("r_consensus_context") or {}),
            "state_regime": dict(overlay_summary.get("state_regime") or {}),
        },
        "brain2_context": {
            "scoreboard_row": scoreboard,
            "top_profit_alerts": _top_dicts(overlay_summary.get("top_profit_alerts") or [], 6),
            "profit_alert_implied_canonicals": _ordered_unique(overlay_summary.get("profit_alert_implied_canonicals") or [])[:12],
            "blackapple_statuses": _top_dicts(overlay_summary.get("blackapple_statuses") or [], 6),
            "blackapple_recommended_canonicals": _ordered_unique(overlay_summary.get("blackapple_recommended_canonicals") or [])[:12],
            "positional_shortlist_top": _top_dicts(positional_rows, 10),
            "positional_signal_notes": _ordered_unique(overlay_summary.get("positional_signal_notes") or [])[:10],
            "due_double_families": _top_dicts(overlay_summary.get("due_double_families") or [], 6),
            "due_double_example_canonicals": _ordered_unique(overlay_summary.get("due_double_example_canonicals") or [])[:12],
            "compound_events_top": _top_dicts(overlay_summary.get("compound_events_top") or [], 6),
        },
        "shadow_decision_policy": decision,
        "control_arm": {
            "candidate_universe": candidate_summary,
            "play_card": play_card_summary,
            "preserved_not_budgeted_canonicals_top": _ordered_unique(preserved_not_budgeted),
        },
        "sandbox_hypotheses": {
            "diagnostic_boxed_seed": boxed_seed,
            "diagnostic_straight_seed": straight_seed,
            "diagnostic_vt_box_seed": vt_box_seed,
            "open_translator_hypotheses": _open_translator_hypotheses(
                decision_row=decision,
                boxed_seed=boxed_seed,
                straight_seed=straight_seed,
                vt_box_seed=vt_box_seed,
                preserved_not_budgeted=preserved_not_budgeted,
            ),
            "carryover_decay_note": str(decision.get("carryover_action") or "").strip() or None,
        },
    }
    return payload


def build_translation_sandbox_state_markdown(payload: Mapping[str, Any]) -> str:
    metadata = payload.get("metadata") if isinstance(payload.get("metadata"), Mapping) else {}
    brain1 = payload.get("brain1_core") if isinstance(payload.get("brain1_core"), Mapping) else {}
    brain2 = payload.get("brain2_context") if isinstance(payload.get("brain2_context"), Mapping) else {}
    decision = payload.get("shadow_decision_policy") if isinstance(payload.get("shadow_decision_policy"), Mapping) else {}
    control_arm = payload.get("control_arm") if isinstance(payload.get("control_arm"), Mapping) else {}
    hypotheses = payload.get("sandbox_hypotheses") if isinstance(payload.get("sandbox_hypotheses"), Mapping) else {}
    scoreboard = brain2.get("scoreboard_row") if isinstance(brain2.get("scoreboard_row"), Mapping) else {}

    lines = [
        f"# Translation Sandbox Seed — {metadata.get('state_key') or '?'}",
        "",
        "Purpose: capture near-final translator-learning surfaces without promoting active combination-forming logic.",
        "",
        "## Metadata",
        "",
        f"- Results date: `{metadata.get('results_date') or '-'}`",
        f"- Board name: `{metadata.get('board_name') or '-'}`",
        f"- Profile: `{metadata.get('profile') or '-'}`",
        f"- Experiment tag: `{metadata.get('experiment_tag') or '-'}`",
        f"- Overlay JSON: `{metadata.get('overlay_json') or '-'}`",
        f"- Scoreboard JSON: `{metadata.get('scoreboard_json') or '-'}`",
        f"- Shadow DPL JSON: `{metadata.get('shadow_decision_policy_json') or '-'}`",
        f"- Candidate Universe: `{metadata.get('candidate_universe_path') or '-'}`",
        f"- Play Card: `{metadata.get('play_card_path') or '-'}`",
        "",
        "## Brain 1 Core",
        "",
        f"- Dominant canonicals: `{', '.join(brain1.get('dominant_canonicals') or []) or '-'}`",
        f"- Dominant families: `{', '.join(brain1.get('dominant_families') or []) or '-'}`",
        f"- Dominant VTRAC indices: `{', '.join(brain1.get('dominant_vtrac_indices') or []) or '-'}`",
        f"- Survivor frontier canonicals: `{', '.join(brain1.get('survivor_frontier_canonicals') or []) or '-'}`",
        f"- Last-remaining canonicals: `{', '.join(brain1.get('survivor_last_remaining_canonicals') or []) or '-'}`",
        f"- Survivor terminal profiles: `{', '.join(brain1.get('survivor_terminal_profiles') or []) or '-'}`",
        f"- R-Consensus available: `{bool((brain1.get('r_consensus_context') or {}).get('available'))}`",
        "",
        "## Brain 2 / Shadow DPL",
        "",
        f"- Score rank: `{scoreboard.get('score_rank') or '-'}`",
        f"- Priority score: `{scoreboard.get('priority_score') or '-'}`",
        f"- Role: `{scoreboard.get('role') or '-'}`",
        f"- Posture: `{decision.get('posture') or '-'}`",
        f"- Mode: `{decision.get('mode') or '-'}`",
        f"- Cap class: `{decision.get('cap_class') or '-'}`",
        f"- Translator route: `{decision.get('translator_route') or '-'}`",
        f"- Reason codes: `{', '.join(decision.get('reason_codes') or []) or '-'}`",
        "",
        "## Control Center / Shortlist Pull-Ins",
        "",
        f"- Profit-alert implied canonicals: `{', '.join(brain2.get('profit_alert_implied_canonicals') or []) or '-'}`",
        f"- Blackapple recommended canonicals: `{', '.join(brain2.get('blackapple_recommended_canonicals') or []) or '-'}`",
        f"- Due-double example canonicals: `{', '.join(brain2.get('due_double_example_canonicals') or []) or '-'}`",
        f"- Positional notes: `{', '.join(brain2.get('positional_signal_notes') or []) or '-'}`",
        "",
        "## Control Arm",
        "",
        f"- Candidate Universe available: `{bool((control_arm.get('candidate_universe') or {}).get('available'))}`",
        f"- Candidate Universe top canonicals: `{', '.join(row.get('canonical') for row in ((control_arm.get('candidate_universe') or {}).get('top_canonicals') or [])[:8]) or '-'}`",
        f"- Play Card available: `{bool((control_arm.get('play_card') or {}).get('available'))}`",
        f"- Play Card budgeted canonicals: `{', '.join((control_arm.get('play_card') or {}).get('budgeted_canonicals_top') or []) or '-'}`",
        f"- Preserved-not-budgeted canonicals: `{', '.join(control_arm.get('preserved_not_budgeted_canonicals_top') or []) or '-'}`",
    ]

    boxed_seed = hypotheses.get("diagnostic_boxed_seed") if isinstance(hypotheses.get("diagnostic_boxed_seed"), list) else []
    if boxed_seed:
        lines.extend(["", "## Diagnostic Boxed Seed", "", "| Value | Support | Sources |", "|---|---:|---|"])
        for row in boxed_seed:
            if not isinstance(row, Mapping):
                continue
            lines.append(
                f"| {row.get('value')} | {row.get('support_count')} | {', '.join(row.get('source_tags') or []) or '-'} |"
            )

    straight_seed = hypotheses.get("diagnostic_straight_seed") if isinstance(hypotheses.get("diagnostic_straight_seed"), list) else []
    if straight_seed:
        lines.extend(["", "## Diagnostic Straight Seed", "", "| Value | Support | Sources |", "|---|---:|---|"])
        for row in straight_seed:
            if not isinstance(row, Mapping):
                continue
            lines.append(
                f"| {row.get('value')} | {row.get('support_count')} | {', '.join(row.get('source_tags') or []) or '-'} |"
            )

    vt_box_seed = hypotheses.get("diagnostic_vt_box_seed") if isinstance(hypotheses.get("diagnostic_vt_box_seed"), list) else []
    if vt_box_seed:
        lines.extend(["", "## Diagnostic VT-Box Seed", "", "| Index | Support | Sources |", "|---|---:|---|"])
        for row in vt_box_seed:
            if not isinstance(row, Mapping):
                continue
            lines.append(
                f"| {row.get('value')} | {row.get('support_count')} | {', '.join(row.get('source_tags') or []) or '-'} |"
            )

    notes = hypotheses.get("open_translator_hypotheses") if isinstance(hypotheses.get("open_translator_hypotheses"), list) else []
    if notes:
        lines.extend(["", "## Open Translator Hypotheses", ""])
        for note in notes:
            lines.append(f"- {note}")

    carryover_note = hypotheses.get("carryover_decay_note")
    if carryover_note:
        lines.extend(["", "## Carryover / Decay Note", "", f"- `{carryover_note}`"])

    return "\n".join(lines).rstrip() + "\n"


def write_translation_sandbox_state_files(
    *,
    out_md_path: Path,
    payload: Mapping[str, Any],
    write_json: bool = True,
) -> Tuple[Path, Optional[Path]]:
    out_md_path.parent.mkdir(parents=True, exist_ok=True)
    out_md_path.write_text(build_translation_sandbox_state_markdown(payload), encoding="utf-8")
    json_path: Optional[Path] = None
    if write_json:
        json_path = out_md_path.with_suffix(".json")
        _write_json(json_path, payload)
    return out_md_path, json_path


def build_translation_sandbox_manifest_payload(
    *,
    results_date: str,
    board_name: str,
    profile: str,
    experiment_tag: str,
    overlay_path: Path,
    scoreboard_path: Path,
    decision_policy_path: Path,
    state_receipts: Sequence[Mapping[str, Any]],
) -> Dict[str, Any]:
    return {
        "schema_version": "translation_sandbox_manifest_v0",
        "metadata": {
            "generated_at": _now_iso(),
            "results_date": results_date,
            "board_name": board_name,
            "profile": profile,
            "experiment_tag": experiment_tag,
            "overlay_json": _safe_rel(overlay_path),
            "scoreboard_json": _safe_rel(scoreboard_path),
            "shadow_decision_policy_json": _safe_rel(decision_policy_path),
        },
        "state_receipts": [dict(row) for row in state_receipts],
        "workflow_manifest": {
            "role": "Research/collection layer between shadow DPL and future translators.",
            "next_step": "Use these seeds to study provisional boxed / straight / vt-box theses without promoting live combination-forming.",
        },
    }


def build_translation_sandbox_manifest_markdown(payload: Mapping[str, Any]) -> str:
    metadata = payload.get("metadata") if isinstance(payload.get("metadata"), Mapping) else {}
    state_rows = payload.get("state_receipts") if isinstance(payload.get("state_receipts"), list) else []
    workflow = payload.get("workflow_manifest") if isinstance(payload.get("workflow_manifest"), Mapping) else {}
    lines = [
        f"# Translation Sandbox Seed Manifest — {metadata.get('board_name') or 'Board'}",
        "",
        "Purpose: collect per-state translator-learning seed artifacts for the arena branch.",
        "",
        "## Metadata",
        "",
        f"- Results date: `{metadata.get('results_date') or '-'}`",
        f"- Profile: `{metadata.get('profile') or '-'}`",
        f"- Experiment tag: `{metadata.get('experiment_tag') or '-'}`",
        f"- Overlay JSON: `{metadata.get('overlay_json') or '-'}`",
        f"- Scoreboard JSON: `{metadata.get('scoreboard_json') or '-'}`",
        f"- Shadow DPL JSON: `{metadata.get('shadow_decision_policy_json') or '-'}`",
        "",
        "## State Seeds",
        "",
        "| State | Rank | Role | Posture | Mode | Seed MD | Seed JSON |",
        "|---|---:|---|---|---|---|---|",
    ]
    for row in state_rows:
        if not isinstance(row, Mapping):
            continue
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row.get("state_key") or "-"),
                    str(row.get("score_rank") or "-"),
                    str(row.get("role") or "-"),
                    str(row.get("posture") or "-"),
                    str(row.get("mode") or "-"),
                    f"`{row.get('seed_md') or '-'}`",
                    f"`{row.get('seed_json') or '-'}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Workflow",
            "",
            f"- role: `{workflow.get('role') or '-'}`",
            f"- next_step: `{workflow.get('next_step') or '-'}`",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def write_translation_sandbox_manifest_files(
    *,
    out_md_path: Path,
    payload: Mapping[str, Any],
    write_json: bool = True,
) -> Tuple[Path, Optional[Path]]:
    out_md_path.parent.mkdir(parents=True, exist_ok=True)
    out_md_path.write_text(build_translation_sandbox_manifest_markdown(payload), encoding="utf-8")
    json_path: Optional[Path] = None
    if write_json:
        json_path = out_md_path.with_suffix(".json")
        _write_json(json_path, payload)
    return out_md_path, json_path


def run_translation_sandbox_seed(
    *,
    sharepacks_root: Path,
    results_date: str,
    profile: str,
    experiment_tag: str,
    board_name: str,
    overlay_json_path: Path,
    scoreboard_json_path: Path,
    decision_policy_json_path: Path,
    runs_dir: Path,
    states: Sequence[str],
) -> Dict[str, Any]:
    overlay_payload = _read_json(overlay_json_path)
    scoreboard_payload = _read_json(scoreboard_json_path)
    decision_payload = _read_json(decision_policy_json_path)

    if not isinstance(overlay_payload, Mapping):
        raise SystemExit(f"Invalid overlay JSON: {_safe_rel(overlay_json_path)}")
    if not isinstance(scoreboard_payload, Mapping):
        raise SystemExit(f"Invalid scoreboard JSON: {_safe_rel(scoreboard_json_path)}")
    if not isinstance(decision_payload, Mapping):
        raise SystemExit(f"Invalid shadow DPL JSON: {_safe_rel(decision_policy_json_path)}")

    overlay_rows = {
        str(row.get("state_key") or "").strip(): row
        for row in (overlay_payload.get("state_summaries") or [])
        if isinstance(row, Mapping) and str(row.get("state_key") or "").strip()
    }
    scoreboard_rows = {
        str(row.get("state_key") or "").strip(): row
        for row in (scoreboard_payload.get("scoreboard_rows") or [])
        if isinstance(row, Mapping) and str(row.get("state_key") or "").strip()
    }
    decision_rows = {
        str(row.get("state_key") or "").strip(): row
        for row in (decision_payload.get("state_decisions") or [])
        if isinstance(row, Mapping) and str(row.get("state_key") or "").strip()
    }

    state_keys = list(states or overlay_rows.keys())
    if not state_keys:
        raise SystemExit("No states found in overlay for translation sandbox.")

    day_dir = sharepacks_root / results_date
    if not day_dir.exists():
        raise SystemExit(f"Missing sharepack day dir: {_safe_rel(day_dir)}")

    state_receipts: List[Dict[str, Any]] = []
    for state_key in state_keys:
        overlay_summary = overlay_rows.get(state_key)
        if not isinstance(overlay_summary, Mapping):
            continue
        state_dir = day_dir / state_key
        analysis_dir = state_dir / "analysis"
        analysis_dir.mkdir(parents=True, exist_ok=True)

        candidate_path = _candidate_universe_path(state_dir=state_dir, profile=profile, experiment_tag=experiment_tag)
        candidate_payload = _read_json(candidate_path) if isinstance(candidate_path, Path) and candidate_path.exists() else None
        play_card_path = _play_card_path(state_dir=state_dir, profile=profile, experiment_tag=experiment_tag)
        play_card_payload = _read_json(play_card_path) if isinstance(play_card_path, Path) and play_card_path.exists() else None

        state_payload = build_translation_sandbox_state_payload(
            results_date=results_date,
            board_name=board_name,
            profile=profile,
            experiment_tag=experiment_tag,
            sharepacks_root=sharepacks_root,
            overlay_path=overlay_json_path,
            scoreboard_path=scoreboard_json_path,
            decision_policy_path=decision_policy_json_path,
            overlay_summary=overlay_summary,
            scoreboard_row=scoreboard_rows.get(state_key),
            decision_row=decision_rows.get(state_key),
            candidate_universe_payload=candidate_payload if isinstance(candidate_payload, Mapping) else None,
            candidate_universe_path=candidate_path,
            play_card_payload=play_card_payload if isinstance(play_card_payload, Mapping) else None,
            play_card_path=play_card_path,
        )

        out_md = analysis_dir / _default_state_out_name(profile, experiment_tag)
        seed_md, seed_json = write_translation_sandbox_state_files(
            out_md_path=out_md,
            payload=state_payload,
            write_json=True,
        )
        scoreboard_row = scoreboard_rows.get(state_key) or {}
        decision_row = decision_rows.get(state_key) or {}
        state_receipts.append(
            {
                "state_key": state_key,
                "score_rank": scoreboard_row.get("score_rank"),
                "priority_score": scoreboard_row.get("priority_score"),
                "role": scoreboard_row.get("role"),
                "posture": decision_row.get("posture"),
                "mode": decision_row.get("mode"),
                "seed_md": _safe_rel(seed_md),
                "seed_json": _safe_rel(seed_json) if seed_json is not None else None,
            }
        )

    manifest_payload = build_translation_sandbox_manifest_payload(
        results_date=results_date,
        board_name=board_name,
        profile=profile,
        experiment_tag=experiment_tag,
        overlay_path=overlay_json_path,
        scoreboard_path=scoreboard_json_path,
        decision_policy_path=decision_policy_json_path,
        state_receipts=state_receipts,
    )
    manifest_md = runs_dir / _default_manifest_out_name(results_date, board_name)
    manifest_md_path, manifest_json_path = write_translation_sandbox_manifest_files(
        out_md_path=manifest_md,
        payload=manifest_payload,
        write_json=True,
    )
    return {
        "results_date": results_date,
        "board_name": board_name,
        "manifest_md": _safe_rel(manifest_md_path),
        "manifest_json": _safe_rel(manifest_json_path) if manifest_json_path is not None else None,
        "state_receipts": state_receipts,
    }


def main(argv: Optional[Sequence[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Create translation sandbox seed artifacts from arena/runtime/control-arm outputs.")
    ap.add_argument("--sharepacks-root", default="sharepacks/_predictive")
    ap.add_argument("--date", required=True)
    ap.add_argument("--profile", default="tool_only")
    ap.add_argument("--experiment-tag", default="arena_v0")
    ap.add_argument("--board-name", default="analysis_arena_day_review")
    ap.add_argument("--states", nargs="*", default=[])
    ap.add_argument("--runs-dir", default=str(RUNS_DIR))
    ap.add_argument("--overlay-json", default="")
    ap.add_argument("--scoreboard-json", default="")
    ap.add_argument("--decision-policy-json", default="")
    args = ap.parse_args(argv)

    sharepacks_root = Path(args.sharepacks_root)
    if not sharepacks_root.is_absolute():
        sharepacks_root = (REPO_ROOT / sharepacks_root).resolve()
    runs_dir = Path(args.runs_dir)
    if not runs_dir.is_absolute():
        runs_dir = (REPO_ROOT / runs_dir).resolve()
    runs_dir.mkdir(parents=True, exist_ok=True)

    overlay_json_path: Optional[Path] = Path(args.overlay_json).resolve() if args.overlay_json else None
    scoreboard_json_path: Optional[Path] = Path(args.scoreboard_json).resolve() if args.scoreboard_json else None
    decision_policy_json_path: Optional[Path] = Path(args.decision_policy_json).resolve() if args.decision_policy_json else None
    if overlay_json_path is None or scoreboard_json_path is None or decision_policy_json_path is None:
        inferred_overlay, inferred_scoreboard, inferred_dpl = _resolve_runs_json_paths(
            results_date=args.date,
            board_name=args.board_name,
            runs_dir=runs_dir,
        )
        overlay_json_path = overlay_json_path or inferred_overlay
        scoreboard_json_path = scoreboard_json_path or inferred_scoreboard
        decision_policy_json_path = decision_policy_json_path or inferred_dpl

    receipt = run_translation_sandbox_seed(
        sharepacks_root=sharepacks_root,
        results_date=args.date,
        profile=args.profile,
        experiment_tag=args.experiment_tag,
        board_name=args.board_name,
        overlay_json_path=overlay_json_path,
        scoreboard_json_path=scoreboard_json_path,
        decision_policy_json_path=decision_policy_json_path,
        runs_dir=runs_dir,
        states=args.states,
    )
    print(f"[ok] translation sandbox -> {receipt['manifest_md']}")
    print(f"     states: {len(receipt.get('state_receipts') or [])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
