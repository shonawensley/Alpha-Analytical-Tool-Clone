#!/usr/bin/env python3
"""
Create deterministic "play cards" from Candidate Universe artifacts.

Why this exists
---------------
Candidate Universe is the full, gradeable pre-results playset.
Play cards are *budgeted cuts* (e.g., 12/24/36 combos) used for:
- live-style competitions ("what to play now"),
- controlled experimentation with selection variations,
- later grading + rollups without hindsight contamination.

This tool:
- Reads ONLY: `sharepacks/<root>/<D>/<STATE>/candidate_universe*.json`
- Writes ONLY (predictive-safe): `sharepacks/<root>/<D>/<STATE>/play_card*.json`

Notes
-----
- Budget units are "combo lines" (length of the final combos list).
- Built-in strategy variants:
  - play_box_first: prefers full canonical closures (all perms) when available.
  - analysis_prefix: strict prefix cut of the ranked combo list (for comparability).
  - convergence_box_first: prefers full canonical closures, but ranks candidates by
    cross-method + cross-variant convergence (support-count first).
  - conversion_box_first: box-first plus a small lane-closure slot (aimed at converting rail hits into straight hits).
  - vtrac_pack_boxed_*: chooses a single VTRAC numeric index “lane” and emits its boxed-member pack
    (from modules.vtrac_reference.VTRAC_DISPLAY) as a bounded conversion pack.
  - v0_2_default_blackapple_reserve_*: v0.2 budget-split posture, with an optional (default-off) B24/B36
    reservation for Blackapple ALERT candidates when top convergence is tied.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))


SCHEMA_VERSION = "1.0"


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _read_json(path: Path) -> object:
    return json.loads(_read_text(path))


def _write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _write_md(path: Path, payload: Dict[str, Any]) -> None:
    state_key = str(payload.get("state_key") or "?")
    results_date = str(payload.get("results_date") or "?")
    sharepack_root = str(payload.get("sharepack_root") or "")
    cu_path = str(payload.get("candidate_universe_path") or "")

    def chunk(lines: Sequence[str], n: int) -> List[List[str]]:
        return [list(lines[i : i + n]) for i in range(0, len(lines), n)]

    ranked = payload.get("ranked_candidates") or []
    if not isinstance(ranked, list):
        ranked = []

    strategies = payload.get("strategies") or {}
    if not isinstance(strategies, dict):
        strategies = {}

    out: List[str] = []
    out.append(f"# Play Card — {state_key} — D={results_date}")
    out.append("")
    out.append("## Provenance")
    if sharepack_root:
        out.append(f"- Sharepack root: `{sharepack_root}`")
    if cu_path:
        out.append(f"- Candidate Universe: `{cu_path}`")
    out.append("")
    out.append("## Ranked candidates (top 25 by score)")
    for r in ranked[:25]:
        if not isinstance(r, dict):
            continue
        combo = _normalize_pick3_literal(r.get("combo") or "")
        if not combo:
            continue
        score = r.get("score")
        methods = r.get("support_methods") or []
        methods_str = ",".join(str(m) for m in methods) if isinstance(methods, list) else str(methods)
        out.append(f"- `{combo}` score={score} methods={methods_str}")
    if len(out) == 0 or out[-1] != "":
        out.append("")
    out.append("## Play cards (budgeted)")
    for strategy_id in sorted(strategies.keys(), key=str):
        cards = strategies.get(strategy_id)
        if not isinstance(cards, dict):
            continue
        out.append(f"### {strategy_id}")
        for budget_id in sorted(cards.keys(), key=str):
            card = cards.get(budget_id)
            if not isinstance(card, dict):
                continue
            combos = card.get("combos") or []
            if not isinstance(combos, list):
                combos = []
            boxed = card.get("boxed_canonicals") or []
            if not isinstance(boxed, list):
                boxed = []
            out.append(f"#### {budget_id} ({len(combos)} lines; boxed canonicals: {len(boxed)})")
            gate = card.get("conversion_gate")
            if isinstance(gate, dict):
                fired = bool(gate.get("fired"))
                preset = str(gate.get("preset") or "")
                lane_preset = str(gate.get("lane_preset") or "")
                conv_budget = card.get("conversion_budget")
                closure_lines = card.get("closure_lines")
                conversion_lines = card.get("conversion_lines")
                fill_lines = card.get("fill_lines")
                out.append(
                    f"- Conversion gate: `{'ON' if fired else 'OFF'}` preset=`{preset}` lane_preset=`{lane_preset}` reserved=`{conv_budget}`"
                )
                out.append(f"- Lines: closure=`{closure_lines}` conversion=`{conversion_lines}` fill=`{fill_lines}`")
                top_combo = str(gate.get("top_combo") or "")
                top = gate.get("top_convergence") if isinstance(gate.get("top_convergence"), dict) else {}
                closure = gate.get("closure_strength") if isinstance(gate.get("closure_strength"), dict) else {}
                if top_combo:
                    out.append(
                        "- Gate snapshot: "
                        + f"top_combo=`{top_combo}` "
                        + f"methods={top.get('methods_count')} "
                        + f"variants_nn={top.get('variants_non_unknown')} "
                        + f"pack_refs={top.get('pack_refs_count')} "
                        + f"closures_full={closure.get('closures_added_full_budget')}"
                    )
            vtrac_pack = card.get("vtrac_pack")
            if isinstance(vtrac_pack, dict):
                idx = vtrac_pack.get("index")
                pack = vtrac_pack.get("pack_combos") or []
                if not isinstance(pack, list):
                    pack = []
                out.append(f"- VTRAC pack: index=`{idx}` size=`{len(pack)}` pack=`{' '.join(str(x) for x in pack)}`")
            ba_reserve = card.get("blackapple_reserve")
            if isinstance(ba_reserve, dict):
                fired = bool(ba_reserve.get("fired"))
                preset = str(ba_reserve.get("preset") or "")
                reserved = ba_reserve.get("reserve_budget")
                inserted = ba_reserve.get("inserted_count")
                out.append(
                    f"- Blackapple reserve: `{'ON' if fired else 'OFF'}` preset=`{preset}` reserved=`{reserved}` inserted=`{inserted}`"
                )
                if fired:
                    ins = ba_reserve.get("inserted") or []
                    if isinstance(ins, list) and ins:
                        out.append(f"- Blackapple inserted: `{' '.join(str(x) for x in ins)}`")
            if boxed:
                out.append(f"- Boxed canonicals: `{', '.join(str(b) for b in boxed)}`")
            if combos:
                out.append("```text")
                for row in chunk([_normalize_pick3_literal(c) for c in combos if _normalize_pick3_literal(c)], 12):
                    out.append(" ".join(row))
                out.append("```")
            out.append("")

    path.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")


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


def _canon(draw: str) -> str:
    d = _normalize_pick3_literal(draw)
    return "".join(sorted(d)) if d else ""


def _unique_perms(triad: str) -> List[str]:
    from itertools import permutations

    triad = _normalize_pick3_literal(triad)
    if not triad:
        return []
    return sorted({"".join(p) for p in permutations(triad, 3)})


def _boxed_canonicals(combos: Iterable[str]) -> List[str]:
    by_canon: Dict[str, set[str]] = {}
    for c in combos:
        c = _normalize_pick3_literal(c)
        if not c:
            continue
        by_canon.setdefault(_canon(c), set()).add(c)
    boxed: List[str] = []
    for canon, members in by_canon.items():
        perms = set(_unique_perms(canon))
        if perms and perms.issubset(members):
            boxed.append(canon)
    return sorted(boxed)


def _is_predictive_root(root: Path) -> bool:
    return root.name == "_predictive" or "/_predictive" in str(root).replace("\\", "/")


def _normalize_experiment_tag(value: str) -> str:
    raw = str(value or "").strip()
    if not raw:
        return ""
    raw = raw.replace(" ", "_")
    cleaned = re.sub(r"[^A-Za-z0-9_-]+", "", raw)
    cleaned = cleaned.strip("_-")
    if not cleaned:
        raise SystemExit(f"Invalid --experiment-tag: {value!r} (must contain A-Z/a-z/0-9/_/-)")
    return cleaned[:60]


def _parse_budgets(value: str) -> List[int]:
    out: List[int] = []
    for part in (value or "").split(","):
        part = part.strip()
        if not part:
            continue
        try:
            n = int(part)
        except Exception:
            continue
        if n > 0:
            out.append(n)
    return sorted(set(out))


def _method_weight(method_id: str) -> float:
    """
    Default weighting heuristic (discovery-safe; not a learned model).

    Higher weight means higher priority in ranked candidates.
    """
    m = (method_id or "").strip()
    if m == "profit_alerts":
        return 100.0
    if m == "blackapple":
        return 0.0
    if m == "due_doubles":
        return 85.0
    if m in {"due_doubles_mirror_single", "due_doubles_mirror_double"}:
        return 70.0
    if m == "mirror_pair_closure":
        return 65.0
    if m == "mirror_pair_closure_due_doubles":
        return 63.0
    if m == "consensus_double_9":
        return 60.0
    if m == "stable_top":
        return 55.0
    if m == "aux_positional":
        return 45.0
    if m == "digit_reduction_analyzer_v2":
        return 40.0
    if m in {"digit_reduction_envelope_steps", "digit_reduction_dr004", "digit_reduction_dr004_index"}:
        return 33.0
    if m in {"vtrac_enhanced_top", "vtrac_top"}:
        return 35.0
    if m == "hot_zones_top":
        return 30.0
    if m == "hot_zones_index_closure":
        return 28.0
    if m == "aux_vtrac_index_overdue":
        return 25.0
    if m in {"R-perm-4", "PackA_vt8", "PackB_mirror3rd"}:
        return 20.0
    if m in {"doubles_mirror_single", "doubles_mirror_double"}:
        return 18.0
    return 10.0


def _profit_strength_bonus(why_tags: Sequence[str]) -> float:
    for tag in why_tags:
        t = str(tag)
        if t.startswith("strength:"):
            try:
                return float(t.split(":", 1)[1])
            except Exception:
                return 0.0
    return 0.0


def _build_support_index(packs: Sequence[dict]) -> Dict[str, List[Dict[str, str]]]:
    """
    combo -> list of supporting pack references (minimal fields).
    """
    idx: Dict[str, List[Dict[str, str]]] = {}
    for p in packs:
        if not isinstance(p, dict):
            continue
        pack_id = str(p.get("pack_id") or "?")
        method_id = str(p.get("method_id") or "?")
        variant = str(p.get("variant") or "Unknown")
        play_mode = str(p.get("play_mode") or "Unknown")
        combos = p.get("combos") or []
        for c in combos:
            c = _normalize_pick3_literal(c)
            if not c:
                continue
            idx.setdefault(c, []).append(
                {
                    "pack_id": pack_id,
                    "method_id": method_id,
                    "variant": variant,
                    "play_mode": play_mode,
                }
            )
    # stable ordering
    for c in idx:
        idx[c].sort(key=lambda r: (r["method_id"], r["pack_id"], r["variant"], r["play_mode"]))
    return idx


def _rank_combos(payload: Dict[str, Any]) -> List[Dict[str, Any]]:
    packs = payload.get("packs") or []
    if not isinstance(packs, list):
        return []

    support = _build_support_index(packs)
    ranked: List[Dict[str, Any]] = []

    # Also compute per-combo "profit strength" bonus by scanning supporting packs.
    profit_bonus: Dict[str, float] = {}
    for p in packs:
        if not isinstance(p, dict):
            continue
        if str(p.get("method_id") or "") != "profit_alerts":
            continue
        bonus = _profit_strength_bonus(p.get("why_tags") or [])
        for c in p.get("combos") or []:
            c = _normalize_pick3_literal(c)
            if c:
                profit_bonus[c] = max(profit_bonus.get(c, 0.0), bonus)

    for combo, refs in support.items():
        methods = sorted({r["method_id"] for r in refs})
        variants = sorted({r["variant"] for r in refs})
        method_score = sum(_method_weight(m) for m in methods)
        score = method_score + (len(methods) * 2.0) + (len(refs) * 0.1) + (profit_bonus.get(combo, 0.0) * 3.0)
        ranked.append(
            {
                "combo": combo,
                "canonical": _canon(combo),
                "score": round(score, 4),
                "support_packs_count": len(refs),
                "support_methods": methods,
                "support_variants": variants,
                "support": refs,
            }
        )

    ranked.sort(key=lambda r: (-float(r.get("score") or 0.0), str(r.get("combo") or "")))
    return ranked


def _card_from_ranked(*, ranked: Sequence[Dict[str, Any]], budget: int) -> Dict[str, Any]:
    combos: List[str] = []
    for row in ranked:
        if len(combos) >= budget:
            break
        combo = _normalize_pick3_literal(row.get("combo") or "")
        if not combo:
            continue
        combos.append(combo)
    combos = combos[:budget]
    boxed = _boxed_canonicals(combos)
    return {
        "budget": int(budget),
        "combos": combos,
        "combos_count": len(combos),
        "cost_units": len(combos),
        "boxed_canonicals": boxed,
        "boxed_canonicals_count": len(boxed),
    }


def _card_box_first(*, ranked: Sequence[Dict[str, Any]], budget: int) -> Dict[str, Any]:
    """
    Build a budgeted card that prefers full canonical closures when available.
    """
    # canonical -> combos in ranked list
    canon_to_combos: Dict[str, set[str]] = {}
    canon_score: Dict[str, float] = {}
    for row in ranked:
        combo = _normalize_pick3_literal(row.get("combo") or "")
        canon = _canon(combo)
        if not canon:
            continue
        canon_to_combos.setdefault(canon, set()).add(combo)
        canon_score[canon] = max(canon_score.get(canon, float("-inf")), float(row.get("score") or 0.0))

    # Only treat canonicals as "boxable" if the candidate set contains the full perm closure.
    boxable: List[Tuple[str, float, List[str]]] = []
    for canon, seen in canon_to_combos.items():
        perms = sorted(set(_unique_perms(canon)))
        if perms and set(perms).issubset(seen):
            boxable.append((canon, canon_score.get(canon, 0.0), perms))

    boxable.sort(key=lambda t: (-t[1], t[0]))

    selected: List[str] = []
    selected_set: set[str] = set()
    # 1) Add full closures first.
    for canon, _, perms in boxable:
        if len(selected) >= budget:
            break
        needed = [c for c in perms if c not in selected_set]
        if not needed:
            continue
        if len(selected) + len(needed) > budget:
            continue
        selected.extend(needed)
        selected_set.update(needed)

    # 2) Fill remaining with top-ranked combos.
    for row in ranked:
        if len(selected) >= budget:
            break
        combo = _normalize_pick3_literal(row.get("combo") or "")
        if not combo or combo in selected_set:
            continue
        selected.append(combo)
        selected_set.add(combo)

    selected = selected[:budget]
    boxed = _boxed_canonicals(selected)
    return {
        "budget": int(budget),
        "combos": selected,
        "combos_count": len(selected),
        "cost_units": len(selected),
        "boxed_canonicals": boxed,
        "boxed_canonicals_count": len(boxed),
    }


def _card_conversion_box_first(*, ranked: Sequence[Dict[str, Any]], budget: int) -> Dict[str, Any]:
    """
    Box-first with a small "conversion slot" reserved for lane-closure methods.

    Motivation: in many misses we have `vtrac_index_hit_only` (rail correct, combo wrong).
    This strategy keeps the box-first behavior, but ensures we always allocate a
    few lines to VTRAC/lane-derived candidates so we have a chance to convert
    "rail hits" into straight hits under tight budgets.

    Notes:
    - This remains selection-layer only: it does NOT invent combos outside Candidate Universe.
    - It is deterministic and additive (use for grading/experimentation first).
    """
    # canonical -> combos in ranked list
    canon_to_combos: Dict[str, set[str]] = {}
    canon_score: Dict[str, float] = {}
    for row in ranked:
        combo = _normalize_pick3_literal(row.get("combo") or "")
        canon = _canon(combo)
        if not canon:
            continue
        canon_to_combos.setdefault(canon, set()).add(combo)
        canon_score[canon] = max(canon_score.get(canon, float("-inf")), float(row.get("score") or 0.0))

    # Only treat canonicals as "boxable" if the candidate set contains the full perm closure.
    boxable: List[Tuple[str, float, List[str]]] = []
    for canon, seen in canon_to_combos.items():
        perms = sorted(set(_unique_perms(canon)))
        if perms and set(perms).issubset(seen):
            boxable.append((canon, canon_score.get(canon, 0.0), perms))

    boxable.sort(key=lambda t: (-t[1], t[0]))

    # Reserve up to 25% of the budget (bounded) for lane-closure methods.
    conversion_budget = max(0, min(6, budget // 4))
    main_budget = max(0, int(budget) - int(conversion_budget))
    lane_methods = {
        "vtrac_enhanced_top",
        "vtrac_top",
        "hot_zones_top",
        "hot_zones_index_closure",
        "aux_vtrac_index_overdue",
        "mirror_pair_closure",
        "mirror_pair_closure_due_doubles",
    }

    selected: List[str] = []
    selected_set: set[str] = set()

    # 1) Add full closures first.
    for canon, _, perms in boxable:
        if len(selected) >= main_budget:
            break
        needed = [c for c in perms if c not in selected_set]
        if not needed:
            continue
        if len(selected) + len(needed) > main_budget:
            continue
        selected.extend(needed)
        selected_set.update(needed)

    # 2) Conversion slot: add a few lane-method-supported combos.
    if conversion_budget:
        lane_rows: List[Dict[str, Any]] = []
        for r in ranked:
            methods = r.get("support_methods") or []
            if not isinstance(methods, list):
                methods = []
            if any((str(m) in lane_methods) for m in methods):
                lane_rows.append(r)
        # Prefer high-scoring lane candidates, but diversify by canonical where possible.
        lane_rows.sort(key=lambda r: (-float(r.get("score") or 0.0), str(r.get("combo") or "")))
        used_canon: set[str] = set(_canon(c) for c in selected_set if _canon(c))
        added = 0
        for row in lane_rows:
            if added >= conversion_budget or len(selected) >= budget:
                break
            combo = _normalize_pick3_literal(row.get("combo") or "")
            if not combo or combo in selected_set:
                continue
            canon = _canon(combo)
            # Prefer adding new canonicals first, then allow repeats if budget remains.
            if canon and canon in used_canon and added < max(1, conversion_budget // 2):
                continue
            selected.append(combo)
            selected_set.add(combo)
            if canon:
                used_canon.add(canon)
            added += 1

        # If we couldn't fill the conversion slot with unique canonicals, top up with best lane rows.
        for row in lane_rows:
            if added >= conversion_budget or len(selected) >= budget:
                break
            combo = _normalize_pick3_literal(row.get("combo") or "")
            if not combo or combo in selected_set:
                continue
            selected.append(combo)
            selected_set.add(combo)
            added += 1

    # 3) Fill remaining with top-ranked combos.
    for row in ranked:
        if len(selected) >= budget:
            break
        combo = _normalize_pick3_literal(row.get("combo") or "")
        if not combo or combo in selected_set:
            continue
        selected.append(combo)
        selected_set.add(combo)

    selected = selected[:budget]
    boxed = _boxed_canonicals(selected)
    return {
        "budget": int(budget),
        "combos": selected,
        "combos_count": len(selected),
        "cost_units": len(selected),
        "boxed_canonicals": boxed,
        "boxed_canonicals_count": len(boxed),
        "conversion_budget": int(conversion_budget),
        "conversion_methods": sorted(lane_methods),
    }


def _lane_methods_for_preset(*, preset: str) -> set[str]:
    base = {
        "vtrac_enhanced_top",
        "vtrac_top",
        "hot_zones_top",
        "hot_zones_index_closure",
        "aux_vtrac_index_overdue",
        "mirror_pair_closure",
        "mirror_pair_closure_due_doubles",
    }
    if preset == "presetB":
        base.update({"R-perm-4", "PackA_vt8", "PackB_mirror3rd"})
    return base


def _should_fire_conversion_gate(
    *,
    top_convergence: Tuple[int, int, int, int, float],
    closures_added_full_budget: int,
    closure_fill_ratio_full_budget: float,
    gate_preset: str,
) -> bool:
    m, v_nn, _v_all, p, _s = top_convergence
    # In practice, boxable closures are almost always available to fill the full budget.
    # The more meaningful discriminator is *how expensive* those closures are:
    # - closures_added_full_budget == 2 implies two 6-line closures (singles) consumed the budget
    # - closures_added_full_budget == 4 implies four 3-line closures (doubles) consumed the budget
    # When closures are expensive, reserving a small conversion slot is more defensible.
    expensive_closures = int(closures_added_full_budget) <= 3
    if gate_preset == "strict":
        strong = (m >= 5) and (v_nn >= 2) and (p >= 5)
        closures_saturate_budget = closure_fill_ratio_full_budget >= 0.999
        return bool(strong and expensive_closures and closures_saturate_budget)

    # lenient
    strong = (m >= 4) and (v_nn >= 2) and (p >= 4)
    closures_saturate_budget = closure_fill_ratio_full_budget >= 0.999
    return bool(strong and expensive_closures and closures_saturate_budget)


def _reserved_conversion_budget(*, budget: int, gate_preset: str) -> int:
    b = int(budget)
    if b <= 0:
        return 0
    if gate_preset == "strict":
        return max(0, min(6, b // 6))
    # lenient
    return max(0, min(6, b // 9))


def _reserved_blackapple_budget(*, budget: int) -> int:
    """
    Reserve a tiny number of lines for Blackapple candidates (bounded conversion fuel).

    Defaults:
    - B24 => 2
    - B36 => 3
    """
    b = int(budget)
    if b <= 12:
        return 0
    return max(0, min(4, b // 12))


def _top_convergence_tied_snapshot(
    *, ranked: Sequence[Dict[str, Any]], tie_preset: str
) -> Tuple[bool, Dict[str, Any]]:
    ranked_conv = sorted(list(ranked), key=_convergence_sort_key)
    top = ranked_conv[0] if ranked_conv else {}
    second = ranked_conv[1] if len(ranked_conv) > 1 else {}
    top_stats = _convergence_stats(top) if isinstance(top, dict) else (0, 0, 0, 0, 0.0)
    second_stats = _convergence_stats(second) if isinstance(second, dict) else (0, 0, 0, 0, 0.0)
    tied = False
    if len(ranked_conv) >= 2:
        if tie_preset == "strict":
            tied = bool(top_stats[:4] == second_stats[:4])
        else:
            # lenient: tie on the two strongest convergence axes
            tied = bool((top_stats[0] == second_stats[0]) and (top_stats[1] == second_stats[1]))
    snap = {
        "preset": tie_preset,
        "top_combo": _normalize_pick3_literal(top.get("combo") or "") if isinstance(top, dict) else "",
        "second_combo": _normalize_pick3_literal(second.get("combo") or "") if isinstance(second, dict) else "",
        "top_convergence": {
            "methods_count": int(top_stats[0]),
            "variants_non_unknown": int(top_stats[1]),
            "variants_total": int(top_stats[2]),
            "pack_refs_count": int(top_stats[3]),
            "base_score": float(top_stats[4]),
        },
        "second_convergence": {
            "methods_count": int(second_stats[0]),
            "variants_non_unknown": int(second_stats[1]),
            "variants_total": int(second_stats[2]),
            "pack_refs_count": int(second_stats[3]),
            "base_score": float(second_stats[4]),
        },
        "tied": bool(tied),
    }
    return bool(tied), snap


def _card_conversion_box_first_conditional(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
    gate_preset: str,
    lane_preset: str,
) -> Dict[str, Any]:
    """
    Conditional conversion (experiment):
    - Gate conversion on BOTH strong convergence evidence AND weak closure availability.
    - When the gate is OFF: behave exactly like convergence_box_first.
    - When the gate is ON: reserve a small conversion slot and fill it with lane-supported candidates.
    """
    ranked_conv = sorted(list(ranked), key=_convergence_sort_key)
    top_row = ranked_conv[0] if ranked_conv else {}
    top_combo = _normalize_pick3_literal(top_row.get("combo") or "") if isinstance(top_row, dict) else ""
    top_stats = _convergence_stats(top_row) if isinstance(top_row, dict) else (0, 0, 0, 0, 0.0)

    # canonical -> combos in ranked list
    canon_to_combos: Dict[str, set[str]] = {}
    canon_best: Dict[str, Tuple[int, int, int, int, float]] = {}
    for row in ranked:
        combo = _normalize_pick3_literal(row.get("combo") or "")
        canon = _canon(combo)
        if not canon:
            continue
        canon_to_combos.setdefault(canon, set()).add(combo)
        canon_best[canon] = max(canon_best.get(canon, (0, 0, 0, 0, float("-inf"))), _convergence_stats(row))

    # Only treat canonicals as "boxable" if the candidate set contains the full perm closure.
    boxable: List[Tuple[str, Tuple[int, int, int, int, float], List[str]]] = []
    for canon, seen in canon_to_combos.items():
        perms = sorted(set(_unique_perms(canon)))
        if perms and set(perms).issubset(seen):
            boxable.append((canon, canon_best.get(canon, (0, 0, 0, 0, 0.0)), perms))
    boxable.sort(key=lambda t: (-t[1][0], -t[1][1], -t[1][2], -t[1][3], -t[1][4], t[0]))

    # How many closures could we buy if we spent the full budget on box-first?
    closures_added_full = 0
    selected_full: set[str] = set()
    for _canon_id, _stats, perms in boxable:
        if len(selected_full) >= int(budget):
            break
        needed = [c for c in perms if c not in selected_full]
        if not needed:
            continue
        if len(selected_full) + len(needed) > int(budget):
            continue
        selected_full.update(needed)
        closures_added_full += 1

    closure_lines_full_budget = len(selected_full)
    closure_fill_ratio_full_budget = (closure_lines_full_budget / float(budget)) if int(budget) else 0.0

    gate_fired = _should_fire_conversion_gate(
        top_convergence=top_stats,
        closures_added_full_budget=closures_added_full,
        closure_fill_ratio_full_budget=closure_fill_ratio_full_budget,
        gate_preset=gate_preset,
    )

    if not gate_fired:
        selected_gate_off: List[str] = []
        selected_set_gate_off: set[str] = set()

        closure_lines_gate_off = 0
        for _canon_id, _stats, perms in boxable:
            if len(selected_gate_off) >= int(budget):
                break
            needed = [c for c in perms if c not in selected_set_gate_off]
            if not needed:
                continue
            if len(selected_gate_off) + len(needed) > int(budget):
                continue
            selected_gate_off.extend(needed)
            selected_set_gate_off.update(needed)
            closure_lines_gate_off += len(needed)

        fill_lines_gate_off = 0
        for row in ranked_conv:
            if len(selected_gate_off) >= int(budget):
                break
            combo = _normalize_pick3_literal(row.get("combo") or "")
            if not combo or combo in selected_set_gate_off:
                continue
            selected_gate_off.append(combo)
            selected_set_gate_off.add(combo)
            fill_lines_gate_off += 1

        selected_gate_off = selected_gate_off[: int(budget)]
        boxed_gate_off = _boxed_canonicals(selected_gate_off)
        card = {
            "budget": int(budget),
            "combos": selected_gate_off,
            "combos_count": len(selected_gate_off),
            "cost_units": len(selected_gate_off),
            "boxed_canonicals": boxed_gate_off,
            "boxed_canonicals_count": len(boxed_gate_off),
            "closure_lines": int(closure_lines_gate_off),
            "conversion_lines": 0,
            "fill_lines": int(fill_lines_gate_off),
            "conversion_budget": 0,
            "conversion_methods": sorted(_lane_methods_for_preset(preset=lane_preset)),
        }
        card["conversion_gate"] = {
            "fired": False,
            "preset": gate_preset,
            "lane_preset": lane_preset,
            "top_combo": top_combo,
            "top_convergence": {
                "methods_count": int(top_stats[0]),
                "variants_non_unknown": int(top_stats[1]),
                "variants_total": int(top_stats[2]),
                "pack_refs_count": int(top_stats[3]),
                "base_score": float(top_stats[4]),
            },
            "closure_strength": {
                "closures_added_full_budget": int(closures_added_full),
                "closure_lines_full_budget": int(closure_lines_full_budget),
                "closure_fill_ratio_full_budget": float(closure_fill_ratio_full_budget),
            },
        }
        return card

    conversion_budget = _reserved_conversion_budget(budget=budget, gate_preset=gate_preset)
    main_budget = max(0, int(budget) - int(conversion_budget))
    lane_methods = _lane_methods_for_preset(preset=lane_preset)

    selected: List[str] = []
    selected_set: set[str] = set()

    closure_lines = 0
    closures_added_main = 0
    for _canon_id, _stats, perms in boxable:
        if len(selected) >= main_budget:
            break
        needed = [c for c in perms if c not in selected_set]
        if not needed:
            continue
        if len(selected) + len(needed) > main_budget:
            continue
        selected.extend(needed)
        selected_set.update(needed)
        closure_lines += len(needed)
        closures_added_main += 1

    conversion_lines = 0
    if conversion_budget:
        lane_rows: List[Dict[str, Any]] = []
        for r in ranked:
            methods = r.get("support_methods") or []
            if not isinstance(methods, list):
                methods = []
            if any((str(m) in lane_methods) for m in methods):
                lane_rows.append(r)
        lane_rows.sort(key=_convergence_sort_key)

        used_canon: set[str] = {c for c in (_canon(x) for x in selected_set) if c}
        for row in lane_rows:
            if conversion_lines >= conversion_budget or len(selected) >= budget:
                break
            combo = _normalize_pick3_literal(row.get("combo") or "")
            if not combo or combo in selected_set:
                continue
            canon = _canon(combo)
            if canon and canon in used_canon and conversion_lines < max(1, conversion_budget // 2):
                continue
            selected.append(combo)
            selected_set.add(combo)
            if canon:
                used_canon.add(canon)
            conversion_lines += 1

        # Top-up if we couldn't diversify canonicals enough.
        for row in lane_rows:
            if conversion_lines >= conversion_budget or len(selected) >= budget:
                break
            combo = _normalize_pick3_literal(row.get("combo") or "")
            if not combo or combo in selected_set:
                continue
            selected.append(combo)
            selected_set.add(combo)
            conversion_lines += 1

    fill_lines = 0
    for row in ranked_conv:
        if len(selected) >= budget:
            break
        combo = _normalize_pick3_literal(row.get("combo") or "")
        if not combo or combo in selected_set:
            continue
        selected.append(combo)
        selected_set.add(combo)
        fill_lines += 1

    selected = selected[:budget]
    boxed = _boxed_canonicals(selected)
    return {
        "budget": int(budget),
        "combos": selected,
        "combos_count": len(selected),
        "cost_units": len(selected),
        "boxed_canonicals": boxed,
        "boxed_canonicals_count": len(boxed),
        "conversion_budget": int(conversion_budget),
        "conversion_methods": sorted(lane_methods),
        "closure_lines": int(closure_lines),
        "conversion_lines": int(conversion_lines),
        "fill_lines": int(fill_lines),
        "conversion_gate": {
            "fired": True,
            "preset": gate_preset,
            "lane_preset": lane_preset,
            "top_combo": top_combo,
            "top_convergence": {
                "methods_count": int(top_stats[0]),
                "variants_non_unknown": int(top_stats[1]),
                "variants_total": int(top_stats[2]),
                "pack_refs_count": int(top_stats[3]),
                "base_score": float(top_stats[4]),
            },
            "closure_strength": {
                "closures_added_full_budget": int(closures_added_full),
                "closure_lines_full_budget": int(closure_lines_full_budget),
                "closure_fill_ratio_full_budget": float(closure_fill_ratio_full_budget),
                "closures_added_main_budget": int(closures_added_main),
            },
        },
    }


def _convergence_stats(row: Dict[str, Any]) -> Tuple[int, int, int, int, float]:
    """
    Convergence priority for discovery mode (support-count based).

    Returns: (methods_count, variants_non_unknown_count, variants_total_count, pack_refs_count, base_score)
    """
    methods = row.get("support_methods") or []
    if not isinstance(methods, list):
        methods = []
    methods_count = len({str(m) for m in methods if str(m) != "blackapple"})

    variants = row.get("support_variants") or []
    if not isinstance(variants, list):
        variants = []
    variants_norm = [str(v or "Unknown") for v in variants]
    variants_set = set(variants_norm)
    variants_non_unknown = {v for v in variants_set if v != "Unknown"}

    pack_refs_count = int(row.get("support_packs_count") or 0)
    base_score = float(row.get("score") or 0.0)
    return methods_count, len(variants_non_unknown), len(variants_set), pack_refs_count, base_score


def _convergence_sort_key(row: Dict[str, Any]) -> Tuple[int, int, int, int, float, str]:
    m, v_nn, v_all, p, s = _convergence_stats(row)
    combo = _normalize_pick3_literal(row.get("combo") or "")
    return (-m, -v_nn, -v_all, -p, -s, combo)


def _vtrac_display_pack(*, index: int) -> List[str]:
    """
    Return the boxed-member pack for a VTRAC numeric index using `modules.vtrac_reference.VTRAC_DISPLAY`.

    This is the "boxed-member pack" (often 8 for singles; fewer for doubles/triples-like indices),
    not the full straight-line closure returned by `get_index_set`.
    """
    import modules.vtrac_reference as vr

    want = int(index)
    for row in vr.VTRAC_DISPLAY:
        try:
            if int(row.get("Index")) != want:
                continue
        except Exception:
            continue
        combos: List[str] = []
        seen: set[str] = set()
        for key in ("Singles", "Doubles"):
            raw = str(row.get(key) or "").strip()
            if not raw:
                continue
            for token in raw.split():
                c = _normalize_pick3_literal(token)
                if not c or c in seen:
                    continue
                combos.append(c)
                seen.add(c)
        return combos
    return []


def _choose_top_vtrac_index(
    *,
    ranked: Sequence[Dict[str, Any]],
    scan_limit: int = 350,
    allowed_methods: Optional[set[str]] = None,
) -> Tuple[Optional[int], Dict[str, Any]]:
    """
    Choose a single VTRAC numeric index ("lane") based on Candidate Universe evidence.

    Deterministic: aggregates convergence evidence for combos that map to the same index,
    then selects the best index by union support (methods/variants) + strength.
    """
    import modules.vtrac_reference as vr

    evidence: Dict[int, Dict[str, Any]] = {}
    for row in list(ranked)[: int(scan_limit)]:
        if not isinstance(row, dict):
            continue
        combo = _normalize_pick3_literal(row.get("combo") or "")
        if not combo:
            continue
        idx = vr.get_vtrac_index(combo)
        if idx is None:
            continue

        methods = row.get("support_methods") or []
        methods_norm = [str(m) for m in methods] if isinstance(methods, list) else []
        methods_norm = [m for m in methods_norm if m != "blackapple"]
        if allowed_methods is not None and not any(m in allowed_methods for m in methods_norm):
            continue

        ev = evidence.setdefault(
            int(idx),
            {
                "rows_count": 0,
                "score_total": 0.0,
                "packs_total": 0,
                "methods": set(),
                "variants": set(),
                "best_combo": "",
                "best_score": float("-inf"),
                "best_convergence": (0, 0, 0, 0, float("-inf")),
            },
        )

        ev["rows_count"] += 1
        ev["score_total"] += float(row.get("score") or 0.0)
        ev["packs_total"] += int(row.get("support_packs_count") or 0)
        ev["best_score"] = max(ev["best_score"], float(row.get("score") or 0.0))

        if methods_norm:
            ev["methods"].update(methods_norm)
        variants = row.get("support_variants") or []
        if isinstance(variants, list):
            ev["variants"].update(str(v or "Unknown") for v in variants)

        conv = _convergence_stats(row)
        if conv > ev["best_convergence"]:
            ev["best_convergence"] = conv
            ev["best_combo"] = combo

    scored: List[Dict[str, Any]] = []
    for idx, ev in evidence.items():
        methods_count = len(ev["methods"])
        variants_set = set(ev["variants"])
        variants_non_unknown = len({v for v in variants_set if v != "Unknown"})
        variants_total = len(variants_set)
        bm, bv_nn, bv_all, bp, bs = ev["best_convergence"]
        scored.append(
            {
                "index": int(idx),
                "rows_count": int(ev["rows_count"]),
                "methods_count": int(methods_count),
                "variants_non_unknown": int(variants_non_unknown),
                "variants_total": int(variants_total),
                "packs_total": int(ev["packs_total"]),
                "score_total": round(float(ev["score_total"]), 4),
                "best_combo": str(ev["best_combo"] or ""),
                "best_score": round(float(ev["best_score"]), 4),
                "best_convergence": {
                    "methods_count": int(bm),
                    "variants_non_unknown": int(bv_nn),
                    "variants_total": int(bv_all),
                    "pack_refs_count": int(bp),
                    "base_score": float(bs),
                },
            }
        )

    scored.sort(
        key=lambda r: (
            -int(r["methods_count"]),
            -int(r["variants_non_unknown"]),
            -int(r["variants_total"]),
            -int(r["packs_total"]),
            -float(r["score_total"]),
            int(r["index"]),
        )
    )

    chosen_index: Optional[int] = scored[0]["index"] if scored else None
    snapshot = {
        "scan_limit": int(scan_limit),
        "allowed_methods": sorted(list(allowed_methods)) if allowed_methods else [],
        "candidates_found": int(len(scored)),
        "chosen_index": int(chosen_index) if chosen_index is not None else None,
        "top5": scored[:5],
    }
    return chosen_index, snapshot


def _card_vtrac_pack_boxed_only(
    *, ranked: Sequence[Dict[str, Any]], budget: int, allowed_methods: Optional[set[str]] = None
) -> Dict[str, Any]:
    """
    Play the single best boxed-member VTRAC pack, then fill remaining lines from score-ranked candidates.

    This avoids expensive full-closure spending, and targets "lane present → convert" behavior.
    """
    chosen_index, chooser = _choose_top_vtrac_index(ranked=ranked, allowed_methods=allowed_methods)
    if chosen_index is None and allowed_methods is not None:
        fallback_index, fallback_chooser = _choose_top_vtrac_index(ranked=ranked, allowed_methods=None)
        chooser = {"filtered": chooser, "fallback_unfiltered": fallback_chooser}
        chosen_index = fallback_index
    pack: List[str] = _vtrac_display_pack(index=int(chosen_index)) if chosen_index is not None else []

    if chosen_index is None or not pack:
        card = _card_from_ranked(ranked=ranked, budget=budget)
        card["vtrac_pack"] = {
            "index": int(chosen_index) if chosen_index is not None else None,
            "pack_combos": pack,
            "chooser": chooser,
            "fallback": "analysis_prefix",
        }
        return card

    selected: List[str] = list(pack)
    selected_set: set[str] = set(selected)

    for row in ranked:
        if len(selected) >= int(budget):
            break
        combo = _normalize_pick3_literal(row.get("combo") or "")
        if not combo or combo in selected_set:
            continue
        selected.append(combo)
        selected_set.add(combo)

    selected = selected[: int(budget)]
    boxed = _boxed_canonicals(selected)
    return {
        "budget": int(budget),
        "combos": selected,
        "combos_count": len(selected),
        "cost_units": len(selected),
        "boxed_canonicals": boxed,
        "boxed_canonicals_count": len(boxed),
        "vtrac_pack": {
            "index": int(chosen_index),
            "pack_combos": list(pack),
            "chooser": chooser,
        },
    }


def _card_vtrac_pack_boxed_first(
    *, ranked: Sequence[Dict[str, Any]], budget: int, allowed_methods: Optional[set[str]] = None
) -> Dict[str, Any]:
    """
    Play the single best boxed-member VTRAC pack, then fill remaining lines by convergence ranking.
    """
    chosen_index, chooser = _choose_top_vtrac_index(ranked=ranked, allowed_methods=allowed_methods)
    if chosen_index is None and allowed_methods is not None:
        fallback_index, fallback_chooser = _choose_top_vtrac_index(ranked=ranked, allowed_methods=None)
        chooser = {"filtered": chooser, "fallback_unfiltered": fallback_chooser}
        chosen_index = fallback_index
    pack: List[str] = _vtrac_display_pack(index=int(chosen_index)) if chosen_index is not None else []

    if chosen_index is None or not pack:
        card = _card_convergence_box_first(ranked=ranked, budget=budget)
        card["vtrac_pack"] = {
            "index": int(chosen_index) if chosen_index is not None else None,
            "pack_combos": pack,
            "chooser": chooser,
            "fallback": "convergence_box_first",
        }
        return card

    ranked_conv = sorted(list(ranked), key=_convergence_sort_key)

    selected: List[str] = list(pack)
    selected_set: set[str] = set(selected)
    used_canon: set[str] = {c for c in (_canon(x) for x in selected_set) if c}
    prefer_unique = max(1, (int(budget) - len(selected)) // 2) if int(budget) > len(selected) else 0

    added = 0
    for row in ranked_conv:
        if len(selected) >= int(budget):
            break
        combo = _normalize_pick3_literal(row.get("combo") or "")
        if not combo or combo in selected_set:
            continue
        canon = _canon(combo)
        if canon and canon in used_canon and added < prefer_unique:
            continue
        selected.append(combo)
        selected_set.add(combo)
        if canon:
            used_canon.add(canon)
        added += 1

    # Top up if we were too strict about canonical diversity.
    for row in ranked_conv:
        if len(selected) >= int(budget):
            break
        combo = _normalize_pick3_literal(row.get("combo") or "")
        if not combo or combo in selected_set:
            continue
        selected.append(combo)
        selected_set.add(combo)

    selected = selected[: int(budget)]
    boxed = _boxed_canonicals(selected)
    return {
        "budget": int(budget),
        "combos": selected,
        "combos_count": len(selected),
        "cost_units": len(selected),
        "boxed_canonicals": boxed,
        "boxed_canonicals_count": len(boxed),
        "vtrac_pack": {
            "index": int(chosen_index),
            "pack_combos": list(pack),
            "chooser": chooser,
        },
    }


def _should_fire_vtrac_pack_gate(
    *,
    chooser_snapshot: Dict[str, Any],
    pack_size: int,
    budget: int,
    gate_preset: str,
) -> bool:
    """
    Conservative gate for inserting a boxed-member VTRAC pack at tight budgets.

    This is intentionally simple:
    - We only spend B12 lines on a pack when the chosen VTRAC index looks dominant and multi-evidence.
    - We require enough remaining budget after the pack to still carry some non-pack coverage.
    """
    b = int(budget)
    psize = int(pack_size)
    if b <= 0 or psize <= 0:
        return False
    if b - psize < 4:
        return False

    top5 = chooser_snapshot.get("top5")
    if not isinstance(top5, list) or not top5:
        return False
    top = top5[0] if isinstance(top5[0], dict) else {}
    second = top5[1] if len(top5) > 1 and isinstance(top5[1], dict) else {}

    def _int(v: Any) -> int:
        try:
            return int(v)
        except Exception:
            return 0

    def _float(v: Any) -> float:
        try:
            return float(v)
        except Exception:
            return 0.0

    m1 = _int(top.get("methods_count"))
    v1 = _int(top.get("variants_non_unknown"))
    s1 = _float(top.get("score_total"))

    m2 = _int(second.get("methods_count")) if second else 0
    v2 = _int(second.get("variants_non_unknown")) if second else 0
    s2 = _float(second.get("score_total")) if second else 0.0

    if gate_preset == "strict":
        strong = (m1 >= 4) and (v1 >= 2)
        ratio = 1.15
    else:
        strong = (m1 >= 3) and (v1 >= 1)
        ratio = 1.05

    dominant = True
    if second:
        dominant = (m1 > m2) or (v1 > v2)
        if s2 > 0.0:
            dominant = bool(dominant or (s1 >= (s2 * ratio)))

    return bool(strong and dominant)


def _card_v0_2_default(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
) -> Dict[str, Any]:
    """
    v0.2 posture (budget-split), encoded as a single strategy for convenience:
    - B12: analysis_prefix
    - B24/B36: vtrac_pack_boxed_first
    """
    b = int(budget)
    if b <= 12:
        return _card_from_ranked(ranked=ranked, budget=b)
    return _card_vtrac_pack_boxed_first(ranked=ranked, budget=b)


def _card_v0_2_default_b12pack(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
    gate_preset: str,
) -> Dict[str, Any]:
    """
    v0.2 posture + an optional B12-only conservative pack insertion gate (research knob).
    - For budgets > 12: behave like vtrac_pack_boxed_first.
    - For budgets <= 12:
        - Choose the top VTRAC index.
        - Only insert its boxed-member pack when the index looks dominant.
        - Otherwise fall back to analysis_prefix (preserves budget discipline).
    """
    b = int(budget)
    if b > 12:
        return _card_vtrac_pack_boxed_first(ranked=ranked, budget=b)

    chosen_index, chooser = _choose_top_vtrac_index(ranked=ranked, allowed_methods=None)
    candidate_pack: List[str] = _vtrac_display_pack(index=int(chosen_index)) if chosen_index is not None else []
    if chosen_index is None or not candidate_pack:
        card = _card_from_ranked(ranked=ranked, budget=b)
        card["vtrac_pack"] = {
            "index": int(chosen_index) if chosen_index is not None else None,
            "pack_combos": [],
            "pack_combos_candidate": list(candidate_pack),
            "chooser": chooser,
            "gate": {"fired": False, "preset": gate_preset, "reason": "no_pack"},
            "fallback": "analysis_prefix",
        }
        return card

    fired = _should_fire_vtrac_pack_gate(
        chooser_snapshot=chooser,
        pack_size=len(candidate_pack),
        budget=b,
        gate_preset=gate_preset,
    )
    if not fired:
        card = _card_from_ranked(ranked=ranked, budget=b)
        card["vtrac_pack"] = {
            "index": int(chosen_index),
            "pack_combos": [],
            "pack_combos_candidate": list(candidate_pack),
            "chooser": chooser,
            "gate": {"fired": False, "preset": gate_preset, "reason": "gate_off"},
            "fallback": "analysis_prefix",
        }
        return card

    selected: List[str] = list(candidate_pack)
    selected_set: set[str] = set(selected)
    for row in ranked:
        if len(selected) >= b:
            break
        combo = _normalize_pick3_literal(row.get("combo") or "")
        if not combo or combo in selected_set:
            continue
        selected.append(combo)
        selected_set.add(combo)

    selected = selected[:b]
    boxed = _boxed_canonicals(selected)
    return {
        "budget": int(b),
        "combos": selected,
        "combos_count": len(selected),
        "cost_units": len(selected),
        "boxed_canonicals": boxed,
        "boxed_canonicals_count": len(boxed),
        "vtrac_pack": {
            "index": int(chosen_index),
            "pack_combos": list(candidate_pack),
            "pack_combos_candidate": list(candidate_pack),
            "chooser": chooser,
            "gate": {"fired": True, "preset": gate_preset, "reason": "gate_on"},
        },
    }


def _card_v0_2_default_blackapple_reserve(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
    tie_preset: str,
) -> Dict[str, Any]:
    """
    v0.2 posture with an optional Blackapple reserve gate (research-only):
    - B12: analysis_prefix
    - B24/B36: vtrac_pack_boxed_first + BA reserve

    Gate:
    - Candidate Universe must contain Blackapple ALERT pack(s) (so BA rows exist).
    - Top convergence must be tied (strict/lenient presets).

    Selection:
    - Reserve a tiny tail slot (B24=2, B36=3 by default).
    - Prefer BA combos corroborated by another method (support_methods_count >= 2).
    - Keep budget constant by replacing tail filler lines (never remove the VTRAC pack head).
    """
    b = int(budget)
    if b <= 12:
        return _card_from_ranked(ranked=ranked, budget=b)

    base = _card_vtrac_pack_boxed_first(ranked=ranked, budget=b)
    base_combos = list(base.get("combos") or [])
    base_combos = [_normalize_pick3_literal(x) for x in base_combos if _normalize_pick3_literal(x)]
    reserve_budget = _reserved_blackapple_budget(budget=b)

    tied, tie_snapshot = _top_convergence_tied_snapshot(ranked=ranked, tie_preset=tie_preset)
    ranked_conv = sorted(list(ranked), key=_convergence_sort_key)

    ba_rows: List[Dict[str, Any]] = []
    for row in ranked_conv:
        methods = row.get("support_methods") or []
        if not isinstance(methods, list):
            methods = []
        if any(str(m) == "blackapple" for m in methods):
            ba_rows.append(row)

    fired = bool(reserve_budget > 0 and tied and ba_rows and len(base_combos) >= reserve_budget)
    if not fired:
        base["blackapple_reserve"] = {
            "fired": False,
            "preset": tie_preset,
            "reserve_budget": int(reserve_budget),
            "reason": "no_ba_rows" if not ba_rows else ("tie_gate_off" if not tied else "no_budget"),
            "tie_snapshot": tie_snapshot,
            "ba_candidates_count": int(len(ba_rows)),
        }
        return base

    keep = base_combos[:-reserve_budget]
    removed = base_combos[-reserve_budget:]
    selected_set: set[str] = set(keep)
    inserted: List[str] = []

    def _methods_count(r: Dict[str, Any]) -> int:
        methods = r.get("support_methods") or []
        if not isinstance(methods, list):
            methods = []
        return len({str(m) for m in methods})

    preferred = [r for r in ba_rows if _methods_count(r) >= 2]
    fallback = [r for r in ba_rows if r not in preferred]

    def _add(rows: Sequence[Dict[str, Any]]) -> None:
        nonlocal inserted
        for r in rows:
            if len(inserted) >= reserve_budget:
                break
            combo = _normalize_pick3_literal(r.get("combo") or "")
            if not combo or combo in selected_set or combo in inserted:
                continue
            inserted.append(combo)
            selected_set.add(combo)

    _add(preferred)
    _add(fallback)

    # Backfill if we couldn't insert enough BA candidates.
    for c in removed:
        if len(inserted) >= reserve_budget:
            break
        if c and c not in selected_set:
            inserted.append(c)
            selected_set.add(c)

    new_combos = (keep + inserted)[:b]
    base["combos"] = new_combos
    base["combos_count"] = len(new_combos)
    base["cost_units"] = len(new_combos)
    base["boxed_canonicals"] = _boxed_canonicals(new_combos)
    base["boxed_canonicals_count"] = len(base.get("boxed_canonicals") or [])
    base["blackapple_reserve"] = {
        "fired": True,
        "preset": tie_preset,
        "reserve_budget": int(reserve_budget),
        "inserted_count": int(len(inserted)),
        "inserted": list(inserted),
        "preferred_inserted_count": int(
            sum(
                1
                for c in inserted
                if any(_normalize_pick3_literal(r.get("combo") or "") == c for r in preferred)
            )
        ),
        "ba_candidates_count": int(len(ba_rows)),
        "tie_snapshot": tie_snapshot,
    }
    return base


def _card_v0_2_default_blackapple_reserve_conditional(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
    tie_preset: str,
) -> Dict[str, Any]:
    """
    Tighter Blackapple reserve gate (research-only):
    - Only insert BA combos when:
        - BA rows exist, and
        - Top convergence is tied (same tie gate as v1), and
        - Base card's boxed_canonicals_count is low (don't steal closure-rich tails), and
        - At least one BA candidate is corroborated by another method (BA-only isn't enough).

    This is designed to reduce "cute but noisy" BA swaps and focus on the environments
    where BA is more likely to add *incremental* conversion value.
    """
    b = int(budget)
    if b <= 12:
        return _card_from_ranked(ranked=ranked, budget=b)

    base = _card_vtrac_pack_boxed_first(ranked=ranked, budget=b)
    base_combos = list(base.get("combos") or [])
    base_combos = [_normalize_pick3_literal(x) for x in base_combos if _normalize_pick3_literal(x)]
    reserve_budget = _reserved_blackapple_budget(budget=b)

    tied, tie_snapshot = _top_convergence_tied_snapshot(ranked=ranked, tie_preset=tie_preset)
    ranked_conv = sorted(list(ranked), key=_convergence_sort_key)

    ba_rows: List[Dict[str, Any]] = []
    for row in ranked_conv:
        methods = row.get("support_methods") or []
        if not isinstance(methods, list):
            methods = []
        if any(str(m) == "blackapple" for m in methods):
            ba_rows.append(row)

    if not (reserve_budget > 0 and tied and ba_rows and len(base_combos) >= reserve_budget):
        base["blackapple_reserve"] = {
            "version": "v2_conditional",
            "fired": False,
            "preset": tie_preset,
            "reserve_budget": int(reserve_budget),
            "reason": "no_ba_rows"
            if not ba_rows
            else ("tie_gate_off" if not tied else "no_budget"),
            "tie_snapshot": tie_snapshot,
            "ba_candidates_count": int(len(ba_rows)),
        }
        return base

    base_boxed = int(base.get("boxed_canonicals_count") or 0)
    max_boxed = (b // 12) if tie_preset != "strict" else max(0, (b // 12) - 1)
    if base_boxed > max_boxed:
        base["blackapple_reserve"] = {
            "version": "v2_conditional",
            "fired": False,
            "preset": tie_preset,
            "reserve_budget": int(reserve_budget),
            "reason": "boxed_too_strong",
            "tie_snapshot": tie_snapshot,
            "ba_candidates_count": int(len(ba_rows)),
            "boxed_canonicals_count": int(base_boxed),
            "max_boxed_allowed": int(max_boxed),
        }
        return base

    def _other_methods_count(r: Dict[str, Any]) -> int:
        methods = r.get("support_methods") or []
        if not isinstance(methods, list):
            methods = []
        # Count non-BA methods (BA must be present in `ba_rows` already).
        return len({str(m) for m in methods if str(m) != "blackapple"})

    preferred = [r for r in ba_rows if _other_methods_count(r) >= 1]
    if not preferred:
        base["blackapple_reserve"] = {
            "version": "v2_conditional",
            "fired": False,
            "preset": tie_preset,
            "reserve_budget": int(reserve_budget),
            "reason": "no_corroborated_ba",
            "tie_snapshot": tie_snapshot,
            "ba_candidates_count": int(len(ba_rows)),
        }
        return base

    keep = base_combos[:-reserve_budget]
    removed = base_combos[-reserve_budget:]
    selected_set: set[str] = set(keep)
    inserted: List[str] = []

    for r in preferred:
        if len(inserted) >= reserve_budget:
            break
        combo = _normalize_pick3_literal(r.get("combo") or "")
        if not combo or combo in selected_set or combo in inserted:
            continue
        inserted.append(combo)
        selected_set.add(combo)

    if not inserted:
        base["blackapple_reserve"] = {
            "version": "v2_conditional",
            "fired": False,
            "preset": tie_preset,
            "reserve_budget": int(reserve_budget),
            "reason": "no_incremental_ba",
            "tie_snapshot": tie_snapshot,
            "ba_candidates_count": int(len(ba_rows)),
            "corroborated_ba_count": int(len(preferred)),
        }
        return base

    # Backfill any unused reserve slots with removed filler lines (never insert BA-only).
    for c in removed:
        if len(inserted) >= reserve_budget:
            break
        if c and c not in selected_set:
            inserted.append(c)
            selected_set.add(c)

    new_combos = (keep + inserted)[:b]
    base["combos"] = new_combos
    base["combos_count"] = len(new_combos)
    base["cost_units"] = len(new_combos)
    base["boxed_canonicals"] = _boxed_canonicals(new_combos)
    base["boxed_canonicals_count"] = len(base.get("boxed_canonicals") or [])
    base["blackapple_reserve"] = {
        "version": "v2_conditional",
        "fired": True,
        "preset": tie_preset,
        "reserve_budget": int(reserve_budget),
        "inserted_count": int(len(inserted)),
        "inserted": list(inserted),
        "corroborated_inserted_count": int(len(inserted) - sum(1 for c in inserted if c in removed)),
        "ba_candidates_count": int(len(ba_rows)),
        "corroborated_ba_count": int(len(preferred)),
        "boxed_canonicals_count": int(base_boxed),
        "max_boxed_allowed": int(max_boxed),
        "tie_snapshot": tie_snapshot,
    }
    return base


def _card_convergence_box_first(*, ranked: Sequence[Dict[str, Any]], budget: int) -> Dict[str, Any]:
    """
    Box-first, but prefers candidates with higher cross-method + cross-variant support.

    This is intentionally additive: it's an *alternative* cut of the same Candidate Universe,
    useful for discovery/experimentation (not a learned model).
    """
    # canonical -> combos in ranked list
    canon_to_combos: Dict[str, set[str]] = {}
    canon_best: Dict[str, Tuple[int, int, int, int, float]] = {}
    for row in ranked:
        combo = _normalize_pick3_literal(row.get("combo") or "")
        canon = _canon(combo)
        if not canon:
            continue
        canon_to_combos.setdefault(canon, set()).add(combo)
        canon_best[canon] = max(canon_best.get(canon, (0, 0, 0, 0, float("-inf"))), _convergence_stats(row))

    # Only treat canonicals as "boxable" if the candidate set contains the full perm closure.
    boxable: List[Tuple[str, Tuple[int, int, int, int, float], List[str]]] = []
    for canon, seen in canon_to_combos.items():
        perms = sorted(set(_unique_perms(canon)))
        if perms and set(perms).issubset(seen):
            boxable.append((canon, canon_best.get(canon, (0, 0, 0, 0, 0.0)), perms))

    boxable.sort(key=lambda t: (-t[1][0], -t[1][1], -t[1][2], -t[1][3], -t[1][4], t[0]))

    ranked_conv = sorted(list(ranked), key=_convergence_sort_key)

    selected: List[str] = []
    selected_set: set[str] = set()
    # 1) Add full closures first (in convergence priority order).
    for canon, _, perms in boxable:
        if len(selected) >= budget:
            break
        needed = [c for c in perms if c not in selected_set]
        if not needed:
            continue
        if len(selected) + len(needed) > budget:
            continue
        selected.extend(needed)
        selected_set.update(needed)

    # 2) Fill remaining with top convergence-ranked combos.
    for row in ranked_conv:
        if len(selected) >= budget:
            break
        combo = _normalize_pick3_literal(row.get("combo") or "")
        if not combo or combo in selected_set:
            continue
        selected.append(combo)
        selected_set.add(combo)

    selected = selected[:budget]
    boxed = _boxed_canonicals(selected)
    return {
        "budget": int(budget),
        "combos": selected,
        "combos_count": len(selected),
        "cost_units": len(selected),
        "boxed_canonicals": boxed,
        "boxed_canonicals_count": len(boxed),
    }


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Create play_card.json from candidate_universe.json for a sharepack day.")
    ap.add_argument("--date", required=True, help="Sharepack/results date D (YYYY-MM-DD)")
    ap.add_argument(
        "--sharepacks-root",
        default="sharepacks/_predictive",
        help="Sharepacks root directory (default: sharepacks/_predictive)",
    )
    ap.add_argument(
        "--profile",
        choices=["mixed", "tool_only", "profit_only"],
        default="tool_only",
        help="Ablation profile (default: tool_only). Determines input candidate_universe filename and output play_card filename.",
    )
    ap.add_argument(
        "--experiment-tag",
        default="",
        help="Optional experiment tag appended to input/output filenames (default: none).",
    )
    ap.add_argument(
        "--input-experiment-tag",
        default="",
        help="Optional experiment tag used ONLY for the input candidate_universe filename (default: same as --experiment-tag).",
    )
    ap.add_argument("--states", nargs="*", help="Optional subset of states (default: auto-discover).")
    ap.add_argument(
        "--budgets",
        default="12,24,36",
        help="Comma-separated budgets to emit (default: 12,24,36).",
    )
    ap.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing play_card.json files (default: refuse).",
    )
    ap.add_argument(
        "--write-md",
        action="store_true",
        help="Also write play_card.md next to play_card.json (default: off).",
    )
    ap.add_argument(
        "--allow-winners-artifacts",
        action="store_true",
        help="Allow running even if candidate_universe.json indicates winners-dependent artifacts (NOT recommended for predictive packs).",
    )
    return ap.parse_args()


def main() -> None:
    args = parse_args()

    sharepacks_root = Path(args.sharepacks_root)
    if not sharepacks_root.is_absolute():
        sharepacks_root = (REPO_ROOT / sharepacks_root).resolve()
    day_dir = sharepacks_root / args.date
    if not day_dir.exists():
        raise SystemExit(f"Missing sharepack day dir: {_safe_rel(day_dir)}")

    budgets = _parse_budgets(args.budgets)
    if not budgets:
        raise SystemExit("No valid budgets parsed (use --budgets like 12,24,36).")

    states = list(args.states) if args.states else sorted(
        p.name for p in day_dir.iterdir() if p.is_dir() and p.name != "control_center"
    )
    if not states:
        raise SystemExit(f"No states found under: {_safe_rel(day_dir)}")

    strict_predictive = _is_predictive_root(sharepacks_root) and not args.allow_winners_artifacts

    profile = str(args.profile or "mixed").strip()
    out_suffix = "" if profile == "mixed" else f"__{profile}"
    exp_tag = _normalize_experiment_tag(args.experiment_tag)
    input_tag_raw = str(args.input_experiment_tag or "").strip()
    if input_tag_raw.lower() in {"-", "none", "null"}:
        input_exp_tag = ""
    elif input_tag_raw:
        input_exp_tag = _normalize_experiment_tag(input_tag_raw)
    else:
        input_exp_tag = exp_tag
    input_tag_suffix = f"__{input_exp_tag}" if input_exp_tag else ""
    out_tag_suffix = f"__{exp_tag}" if exp_tag else ""

    for state_key in states:
        state_dir = day_dir / state_key
        cu_path = state_dir / f"candidate_universe{out_suffix}{input_tag_suffix}.json"
        if not cu_path.exists():
            raise SystemExit(f"Missing candidate universe: {_safe_rel(cu_path)}")

        out_path = state_dir / f"play_card{out_suffix}{out_tag_suffix}.json"
        if out_path.exists() and not args.force:
            raise SystemExit(f"Refusing to overwrite existing play card (use --force): {_safe_rel(out_path)}")

        md_path = state_dir / f"play_card{out_suffix}{out_tag_suffix}.md"
        if args.write_md and md_path.exists() and not args.force:
            raise SystemExit(f"Refusing to overwrite existing play card markdown (use --force): {_safe_rel(md_path)}")

        raw = _read_json(cu_path)
        if not isinstance(raw, dict):
            raise SystemExit(f"Invalid JSON (expected object): {_safe_rel(cu_path)}")

        if strict_predictive and bool(raw.get("contains_winners_artifacts")):
            raise SystemExit(
                "Candidate Universe indicates winners-dependent artifacts inside predictive sharepack; aborting.\n"
                f"date={args.date} state={state_key} root={_safe_rel(sharepacks_root)} cu={_safe_rel(cu_path)}"
            )

        ranked = _rank_combos(raw)
        ranked_simple = [
            {
                "combo": r["combo"],
                "canonical": r["canonical"],
                "score": r["score"],
                "support_packs_count": r["support_packs_count"],
                "support_methods": r["support_methods"],
                "support_variants": r.get("support_variants") or [],
            }
            for r in ranked
        ]

        strategy_cards: Dict[str, Dict[str, Any]] = {
            "play_box_first": {},
            "analysis_prefix": {},
            "v0_2_default": {},
            "v0_2_default_b12pack_lenient": {},
            "v0_2_default_b12pack_strict": {},
            "v0_2_default_blackapple_reserve_lenient": {},
            "v0_2_default_blackapple_reserve_strict": {},
            "v0_2_default_blackapple_reserve_conditional_lenient": {},
            "v0_2_default_blackapple_reserve_conditional_strict": {},
            "convergence_box_first": {},
            "conversion_box_first": {},
            "vtrac_pack_boxed_only": {},
            "vtrac_pack_boxed_first": {},
            "vtrac_pack_boxed_only_laneonly_presetB": {},
            "vtrac_pack_boxed_first_laneonly_presetB": {},
            "conversion_box_first_conditional_lenient_presetA": {},
            "conversion_box_first_conditional_lenient_presetB": {},
            "conversion_box_first_conditional_strict_presetA": {},
            "conversion_box_first_conditional_strict_presetB": {},
        }
        lane_methods_presetB = _lane_methods_for_preset(preset="presetB")
        for b in budgets:
            strategy_cards["play_box_first"][f"B{b}"] = _card_box_first(ranked=ranked, budget=b)
            strategy_cards["analysis_prefix"][f"B{b}"] = _card_from_ranked(ranked=ranked, budget=b)
            strategy_cards["v0_2_default"][f"B{b}"] = _card_v0_2_default(ranked=ranked, budget=b)
            strategy_cards["v0_2_default_b12pack_lenient"][f"B{b}"] = _card_v0_2_default_b12pack(
                ranked=ranked, budget=b, gate_preset="lenient"
            )
            strategy_cards["v0_2_default_b12pack_strict"][f"B{b}"] = _card_v0_2_default_b12pack(
                ranked=ranked, budget=b, gate_preset="strict"
            )
            strategy_cards["v0_2_default_blackapple_reserve_lenient"][f"B{b}"] = _card_v0_2_default_blackapple_reserve(
                ranked=ranked, budget=b, tie_preset="lenient"
            )
            strategy_cards["v0_2_default_blackapple_reserve_strict"][f"B{b}"] = _card_v0_2_default_blackapple_reserve(
                ranked=ranked, budget=b, tie_preset="strict"
            )
            strategy_cards["v0_2_default_blackapple_reserve_conditional_lenient"][f"B{b}"] = (
                _card_v0_2_default_blackapple_reserve_conditional(ranked=ranked, budget=b, tie_preset="lenient")
            )
            strategy_cards["v0_2_default_blackapple_reserve_conditional_strict"][f"B{b}"] = (
                _card_v0_2_default_blackapple_reserve_conditional(ranked=ranked, budget=b, tie_preset="strict")
            )
            strategy_cards["convergence_box_first"][f"B{b}"] = _card_convergence_box_first(ranked=ranked, budget=b)
            strategy_cards["conversion_box_first"][f"B{b}"] = _card_conversion_box_first(ranked=ranked, budget=b)
            strategy_cards["vtrac_pack_boxed_only"][f"B{b}"] = _card_vtrac_pack_boxed_only(ranked=ranked, budget=b)
            strategy_cards["vtrac_pack_boxed_first"][f"B{b}"] = _card_vtrac_pack_boxed_first(ranked=ranked, budget=b)
            strategy_cards["vtrac_pack_boxed_only_laneonly_presetB"][f"B{b}"] = _card_vtrac_pack_boxed_only(
                ranked=ranked, budget=b, allowed_methods=lane_methods_presetB
            )
            strategy_cards["vtrac_pack_boxed_first_laneonly_presetB"][f"B{b}"] = _card_vtrac_pack_boxed_first(
                ranked=ranked, budget=b, allowed_methods=lane_methods_presetB
            )
            strategy_cards["conversion_box_first_conditional_lenient_presetA"][f"B{b}"] = _card_conversion_box_first_conditional(
                ranked=ranked, budget=b, gate_preset="lenient", lane_preset="presetA"
            )
            strategy_cards["conversion_box_first_conditional_lenient_presetB"][f"B{b}"] = _card_conversion_box_first_conditional(
                ranked=ranked, budget=b, gate_preset="lenient", lane_preset="presetB"
            )
            strategy_cards["conversion_box_first_conditional_strict_presetA"][f"B{b}"] = _card_conversion_box_first_conditional(
                ranked=ranked, budget=b, gate_preset="strict", lane_preset="presetA"
            )
            strategy_cards["conversion_box_first_conditional_strict_presetB"][f"B{b}"] = _card_conversion_box_first_conditional(
                ranked=ranked, budget=b, gate_preset="strict", lane_preset="presetB"
            )

        payload = {
            "schema_version": SCHEMA_VERSION,
            "generated_at": _now_iso(),
            "results_date": args.date,
            "profile": profile,
            "experiment_tag": exp_tag,
            "state_key": state_key,
            "sharepack_root": _safe_rel(sharepacks_root),
            "candidate_universe_path": _safe_rel(cu_path),
            "ranked_candidates": ranked_simple,
            "strategies": strategy_cards,
        }

        _write_json(out_path, payload)
        if args.write_md:
            _write_md(md_path, payload)
            print(f"Wrote: {_safe_rel(out_path)}, {_safe_rel(md_path)} (budgets={','.join(f'B{b}' for b in budgets)})")
        else:
            print(f"Wrote: {_safe_rel(out_path)} (budgets={','.join(f'B{b}' for b in budgets)})")


if __name__ == "__main__":
    main()
