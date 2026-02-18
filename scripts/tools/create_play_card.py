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


def _score_first_sort_key(row: Dict[str, Any]) -> Tuple[float, int, int, int, int, str]:
    """
    Like `_convergence_sort_key`, but prioritize the numeric score first.

    Used for within-lane/tail representative selection experiments where we want the single tail line
    to be the highest-score candidate, not necessarily the highest method/variant corroboration row.
    """
    m, v_nn, v_all, p, s = _convergence_stats(row)
    combo = _normalize_pick3_literal(row.get("combo") or "")
    return (-float(s), -int(m), -int(v_nn), -int(v_all), -int(p), combo)


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


def _state_draws_prefix(*, state_key: str) -> str:
    """
    Map sharepack state folder names like "Florida4" to their aux/draws CSV prefix ("Florida").
    """
    return re.sub(r"\d+$", "", str(state_key or "").strip())


def _read_draws_csv_head(*, path: Path, n: int) -> List[str]:
    want = max(0, int(n))
    if want <= 0:
        return []
    try:
        raw = _read_text(path).splitlines()
    except Exception:
        return []
    out: List[str] = []
    for line in raw:
        s = str(line or "").strip()
        if not s or s.lower() == "draw":
            continue
        s = "".join(ch for ch in s if ch.isdigit())
        if not s:
            continue
        if len(s) < 3:
            s = s.zfill(3)
        if len(s) != 3:
            continue
        out.append(s)
        if len(out) >= want:
            break
    return out


def _recent_vtrac_indices_from_draws(*, draws: Sequence[str]) -> List[int]:
    import modules.vtrac_reference as vr

    out: List[int] = []
    for d in draws:
        combo = _normalize_pick3_literal(d or "")
        if not combo:
            continue
        idx = vr.get_vtrac_index(combo)
        if idx is None:
            continue
        out.append(int(idx))
    return out


def _recent_indices_snapshot(
    *,
    state_dir: Path,
    state_key: str,
    midday_draws: int,
    evening_draws: int,
    combined_draws: int,
) -> Dict[str, Any]:
    """
    Predictive-safe recency snapshot:
    - Reads sharepack-local `aux/draws/*_draws.csv` (newest-first).
    - Computes VTRAC numeric indices for the most recent N draws per variant.
    """
    prefix = _state_draws_prefix(state_key=state_key)
    draws_dir = state_dir / "aux" / "draws"
    out: Dict[str, Any] = {
        "spec": {
            "midday_draws": int(midday_draws),
            "evening_draws": int(evening_draws),
            "combined_draws": int(combined_draws),
        },
        "prefix": prefix,
        "paths": {},
        "draws": {},
        "vtrac_indices": {},
    }
    if not prefix or not draws_dir.exists():
        out["error"] = "missing_draws_dir"
        return out

    paths = {
        "Midday": draws_dir / f"{prefix}_Midday_draws.csv",
        "Evening": draws_dir / f"{prefix}_Evening_draws.csv",
        "Combined": draws_dir / f"{prefix}_draws.csv",
    }
    out["paths"] = {k: _safe_rel(p) for k, p in paths.items()}

    want = {"Midday": int(midday_draws), "Evening": int(evening_draws), "Combined": int(combined_draws)}
    for k, p in paths.items():
        if not p.exists():
            out["draws"][k] = []
            out["vtrac_indices"][k] = []
            continue
        head = _read_draws_csv_head(path=p, n=want.get(k, 0))
        out["draws"][k] = head
        out["vtrac_indices"][k] = _recent_vtrac_indices_from_draws(draws=head)
    return out


def _vtrac_recency_absence_score(*, index: int, snap: Dict[str, Any]) -> int:
    idx = int(index)
    score = 0
    vt = snap.get("vtrac_indices") if isinstance(snap, dict) else None
    if not isinstance(vt, dict):
        return 0
    for key in ("Midday", "Evening", "Combined"):
        vals = vt.get(key) or []
        if isinstance(vals, list) and vals and idx not in {int(x) for x in vals if isinstance(x, int)}:
            score += 1
    return int(score)


def _choose_top_vtrac_index_recency_tiebreak(
    *,
    ranked: Sequence[Dict[str, Any]],
    state_dir: Path,
    state_key: str,
    tie_preset: str,
    midday_draws: int = 2,
    evening_draws: int = 2,
    combined_draws: int = 4,
    allowed_methods: Optional[set[str]] = None,
) -> Tuple[Optional[int], Dict[str, Any]]:
    """
    Choose the top VTRAC index with an optional short-horizon recency tie-break.

    Intended behavior:
    - Use Candidate Universe evidence as the primary selector.
    - Only apply recency as a bounded tie-break between top-2 indices.
    - Recency is measured as "index absent from the last N posted draws" (per variant).
    """
    chosen, chooser = _choose_top_vtrac_index(ranked=ranked, allowed_methods=allowed_methods)

    recency = _recent_indices_snapshot(
        state_dir=state_dir,
        state_key=state_key,
        midday_draws=midday_draws,
        evening_draws=evening_draws,
        combined_draws=combined_draws,
    )

    top5 = chooser.get("top5") if isinstance(chooser, dict) else None
    if not isinstance(top5, list) or len(top5) < 2:
        return chosen, {"chooser": chooser, "recency": recency, "tiebreak": {"applied": False, "reason": "no_runner_up"}}

    top = top5[0] if isinstance(top5[0], dict) else {}
    second = top5[1] if isinstance(top5[1], dict) else {}
    top_idx = top.get("index")
    second_idx = second.get("index")
    if not isinstance(top_idx, int) or not isinstance(second_idx, int):
        return chosen, {"chooser": chooser, "recency": recency, "tiebreak": {"applied": False, "reason": "bad_top_indices"}}

    strict = str(tie_preset or "").strip().lower() == "strict"
    top_key = (
        int(top.get("methods_count") or 0),
        int(top.get("variants_non_unknown") or 0),
        int(top.get("variants_total") or 0),
        int(top.get("packs_total") or 0),
    )
    second_key = (
        int(second.get("methods_count") or 0),
        int(second.get("variants_non_unknown") or 0),
        int(second.get("variants_total") or 0),
        int(second.get("packs_total") or 0),
    )
    methods_diff = int(top_key[0] - second_key[0])
    variants_diff = int(top_key[1] - second_key[1])
    eligible = bool(methods_diff == 0) if strict else bool(methods_diff <= 1)
    if not eligible:
        return chosen, {
            "chooser": chooser,
            "recency": recency,
            "tiebreak": {
                "applied": False,
                "reason": "not_eligible",
                "preset": tie_preset,
                "methods_diff": int(methods_diff),
                "variants_diff": int(variants_diff),
            },
        }

    top_abs = _vtrac_recency_absence_score(index=top_idx, snap=recency)
    second_abs = _vtrac_recency_absence_score(index=second_idx, snap=recency)
    if top_abs == second_abs:
        return chosen, {
            "chooser": chooser,
            "recency": recency,
            "tiebreak": {
                "applied": False,
                "reason": "no_absence_diff",
                "preset": tie_preset,
                "top_absence": int(top_abs),
                "second_absence": int(second_abs),
                "methods_diff": int(methods_diff),
                "variants_diff": int(variants_diff),
            },
        }

    prefer = int(top_idx) if top_abs > second_abs else int(second_idx)
    candidate_pack = _vtrac_display_pack(index=int(prefer))
    if not candidate_pack:
        return chosen, {
            "chooser": chooser,
            "recency": recency,
            "tiebreak": {
                "applied": False,
                "reason": "no_pack_for_preferred",
                "preset": tie_preset,
                "preferred_index": int(prefer),
                "top_absence": int(top_abs),
                "second_absence": int(second_abs),
            },
        }

    return int(prefer), {
        "chooser": chooser,
        "recency": recency,
        "tiebreak": {
            "applied": True,
            "preset": tie_preset,
            "base_chosen_index": int(chosen) if chosen is not None else None,
            "top_index": int(top_idx),
            "second_index": int(second_idx),
            "top_absence": int(top_abs),
            "second_absence": int(second_abs),
            "methods_diff": int(methods_diff),
            "variants_diff": int(variants_diff),
            "chosen_index": int(prefer),
        },
    }


def _choose_top_vtrac_index(
    *,
    ranked: Sequence[Dict[str, Any]],
    scan_limit: int = 350,
    allowed_methods: Optional[set[str]] = None,
    sort_preset: str = "methods_first",
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

    preset = str(sort_preset or "methods_first").strip().lower()
    if preset not in {"methods_first", "score_total_first", "packs_first"}:
        raise SystemExit(f"Invalid sort_preset: {sort_preset!r} (expected methods_first|score_total_first|packs_first)")

    if preset == "score_total_first":
        scored.sort(
            key=lambda r: (
                -float(r["score_total"]),
                -int(r["packs_total"]),
                -int(r["methods_count"]),
                -int(r["variants_non_unknown"]),
                -int(r["variants_total"]),
                int(r["index"]),
            )
        )
    elif preset == "packs_first":
        scored.sort(
            key=lambda r: (
                -int(r["packs_total"]),
                -int(r["methods_count"]),
                -int(r["variants_non_unknown"]),
                -int(r["variants_total"]),
                -float(r["score_total"]),
                int(r["index"]),
            )
        )
    else:
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
        "sort_preset": preset,
        "allowed_methods": sorted(list(allowed_methods)) if allowed_methods else [],
        "candidates_found": int(len(scored)),
        "chosen_index": int(chosen_index) if chosen_index is not None else None,
        "top5": scored[:5],
    }
    return chosen_index, snapshot


def _choose_top_vtrac_indices(
    *,
    ranked: Sequence[Dict[str, Any]],
    count: int,
    scan_limit: int = 350,
    allowed_methods: Optional[set[str]] = None,
    sort_preset: str = "methods_first",
) -> Tuple[List[int], Dict[str, Any]]:
    """
    Choose the top-N VTRAC indices using the same evidence ranking as `_choose_top_vtrac_index`.

    Intended for multi-pack strategies (e.g., B24 can spend 3 boxed-member packs of ~8 lines each).
    """
    n = max(0, int(count))
    if n <= 0:
        return [], {"candidates_found": 0, "chosen_indices": [], "top5": []}

    _, chooser = _choose_top_vtrac_index(
        ranked=ranked,
        scan_limit=scan_limit,
        allowed_methods=allowed_methods,
        sort_preset=sort_preset,
    )
    top5 = chooser.get("top5") if isinstance(chooser, dict) else None
    if not isinstance(top5, list):
        top5 = []

    indices: List[int] = []
    for row in top5:
        if not isinstance(row, dict):
            continue
        idx = row.get("index")
        if isinstance(idx, int):
            indices.append(int(idx))
        else:
            try:
                indices.append(int(idx))
            except Exception:
                continue
        if len(indices) >= n:
            break

    chooser2 = dict(chooser) if isinstance(chooser, dict) else {}
    chooser2["chosen_indices"] = list(indices)
    return indices, chooser2


def _choose_top_vtrac_indices_full(
    *,
    ranked: Sequence[Dict[str, Any]],
    count: int,
    scan_limit: int = 350,
    allowed_methods: Optional[set[str]] = None,
    sort_preset: str = "methods_first",
) -> Tuple[List[int], Dict[str, Any]]:
    """
    Choose top-N indices using the same evidence model as `_choose_top_vtrac_index`,
    but without truncating to the top-5 snapshot.
    """
    import modules.vtrac_reference as vr

    n = max(0, int(count))
    if n <= 0:
        return [], {"candidates_found": 0, "chosen_indices": [], "topN": []}

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
            },
        )

        ev["rows_count"] += 1
        ev["score_total"] += float(row.get("score") or 0.0)
        ev["packs_total"] += int(row.get("support_packs_count") or 0)

        if methods_norm:
            ev["methods"].update(methods_norm)
        variants = row.get("support_variants") or []
        if isinstance(variants, list):
            ev["variants"].update(str(v or "Unknown") for v in variants)

    scored: List[Dict[str, Any]] = []
    for idx, ev in evidence.items():
        methods_count = len(ev["methods"])
        variants_set = set(ev["variants"])
        variants_non_unknown = len({v for v in variants_set if v != "Unknown"})
        variants_total = len(variants_set)
        scored.append(
            {
                "index": int(idx),
                "rows_count": int(ev["rows_count"]),
                "methods_count": int(methods_count),
                "variants_non_unknown": int(variants_non_unknown),
                "variants_total": int(variants_total),
                "packs_total": int(ev["packs_total"]),
                "score_total": round(float(ev["score_total"]), 4),
            }
        )

    preset = str(sort_preset or "methods_first").strip().lower()
    if preset not in {"methods_first", "score_total_first", "packs_first"}:
        raise SystemExit(f"Invalid sort_preset: {sort_preset!r} (expected methods_first|score_total_first|packs_first)")

    if preset == "score_total_first":
        scored.sort(
            key=lambda r: (
                -float(r["score_total"]),
                -int(r["packs_total"]),
                -int(r["methods_count"]),
                -int(r["variants_non_unknown"]),
                -int(r["variants_total"]),
                int(r["index"]),
            )
        )
    elif preset == "packs_first":
        scored.sort(
            key=lambda r: (
                -int(r["packs_total"]),
                -int(r["methods_count"]),
                -int(r["variants_non_unknown"]),
                -int(r["variants_total"]),
                -float(r["score_total"]),
                int(r["index"]),
            )
        )
    else:
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

    indices = [int(r["index"]) for r in scored[:n]]
    snapshot = {
        "scan_limit": int(scan_limit),
        "sort_preset": preset,
        "allowed_methods": sorted(list(allowed_methods)) if allowed_methods else [],
        "candidates_found": int(len(scored)),
        "chosen_indices": indices,
        "topN": scored[: max(0, min(len(scored), n))],
    }
    return indices, snapshot


def _choose_top_vtrac_indices_diverse(
    *,
    ranked: Sequence[Dict[str, Any]],
    count: int,
    scan_limit: int = 350,
    allowed_methods: Optional[set[str]] = None,
) -> Tuple[List[int], Dict[str, Any]]:
    """
    Choose top-N indices, but intentionally diversify ranking lenses.

    Motivation:
    - The system is a multi-hypothesis environment: the "winner lane" is often present in CU,
      but not necessarily #1 under a single chooser lens.
    - This strategy reduces over-commitment by mixing top candidates from multiple sort presets.

    Implementation:
    - Take ~half of N from `methods_first` (corroboration),
    - Fill remaining from `packs_first` (pack-referenced strength),
    - Then `score_total_first` (aggregate strength) as a final backstop.
    """
    n = max(0, int(count))
    if n <= 0:
        return [], {"candidates_found": 0, "chosen_indices": [], "top5": []}

    # Pull small ranked lists under multiple lenses (each returns a top5).
    _, chooser_methods = _choose_top_vtrac_index(
        ranked=ranked,
        scan_limit=int(scan_limit),
        allowed_methods=allowed_methods,
        sort_preset="methods_first",
    )
    _, chooser_packs = _choose_top_vtrac_index(
        ranked=ranked,
        scan_limit=int(scan_limit),
        allowed_methods=allowed_methods,
        sort_preset="packs_first",
    )
    _, chooser_score = _choose_top_vtrac_index(
        ranked=ranked,
        scan_limit=int(scan_limit),
        allowed_methods=allowed_methods,
        sort_preset="score_total_first",
    )

    def _top5(chooser: Dict[str, Any]) -> List[Dict[str, Any]]:
        top = chooser.get("top5")
        return top if isinstance(top, list) else []

    indices: List[int] = []
    seen: set[int] = set()

    def _add(rows: List[Dict[str, Any]], *, limit: Optional[int] = None) -> None:
        for row in rows:
            if not isinstance(row, dict):
                continue
            idx = row.get("index")
            try:
                val = int(idx)
            except Exception:
                continue
            if val in seen:
                continue
            indices.append(val)
            seen.add(val)
            if limit is not None and len(indices) >= limit:
                return
            if len(indices) >= n:
                return

    # First pass: corroboration-heavy (methods/variants).
    first_quota = (n + 1) // 2 if n > 1 else 1
    _add(_top5(chooser_methods), limit=first_quota)
    if len(indices) < n:
        _add(_top5(chooser_packs))
    if len(indices) < n:
        _add(_top5(chooser_score))

    chooser = {
        "scan_limit": int(scan_limit),
        "allowed_methods": sorted(list(allowed_methods)) if allowed_methods else [],
        "mix": {
            "methods_first": chooser_methods,
            "packs_first": chooser_packs,
            "score_total_first": chooser_score,
        },
        "chosen_indices": list(indices),
    }
    return indices, chooser


def _choose_top_vtrac_indices_round_robin_mix(
    *,
    ranked: Sequence[Dict[str, Any]],
    count: int,
    scan_limit: int = 350,
    allowed_methods: Optional[set[str]] = None,
    snapshot_top_k: int = 12,
) -> Tuple[List[int], Dict[str, Any]]:
    """
    Choose top-N indices by mixing multiple sort presets deterministically.

    Why:
    - Under fixed posture (tool_only + stable10), many "filters" are near-no-ops because
      the top-ranked indices already satisfy them.
    - This lever is intended to *materially change the touched index set* while keeping
      the allocation geometry constant.

    How:
    - Build three ranked lists under different lenses:
        - methods_first (corroboration)
        - packs_first (pack-referenced strength)
        - score_total_first (aggregate strength)
    - Merge them with a deterministic round-robin interleave, skipping duplicates.
    - Backstop-fill with the score_total_first list to ensure we reach N.
    """
    n = max(0, int(count))
    if n <= 0:
        return [], {"candidates_found": 0, "chosen_indices": []}

    presets = ("methods_first", "packs_first", "score_total_first")
    ranked_lists: Dict[str, List[int]] = {}
    snapshots: Dict[str, Dict[str, Any]] = {}
    for preset in presets:
        indices, snapshot = _choose_top_vtrac_indices_full(
            ranked=ranked,
            count=n,
            scan_limit=int(scan_limit),
            allowed_methods=allowed_methods,
            sort_preset=preset,
        )
        ranked_lists[preset] = [int(x) for x in indices]
        snapshots[preset] = snapshot

    lists = [ranked_lists[p] for p in presets]
    merged: List[int] = []
    seen: set[int] = set()

    i = 0
    while len(merged) < n and any(i < len(lst) for lst in lists):
        for lst in lists:
            if i >= len(lst):
                continue
            idx = int(lst[i])
            if idx in seen:
                continue
            merged.append(idx)
            seen.add(idx)
            if len(merged) >= n:
                break
        i += 1

    if len(merged) < n:
        # Backstop fill: keep determinism and ensure rank_count is satisfied.
        for idx in ranked_lists["score_total_first"] + ranked_lists["methods_first"] + ranked_lists["packs_first"]:
            val = int(idx)
            if val in seen:
                continue
            merged.append(val)
            seen.add(val)
            if len(merged) >= n:
                break

    top_k = max(0, int(snapshot_top_k))
    def _cand_found(name: str) -> int:
        snap = snapshots.get(name) or {}
        try:
            return int(snap.get("candidates_found") or 0)
        except Exception:
            return 0
    chooser = {
        "scan_limit": int(scan_limit),
        "allowed_methods": sorted(list(allowed_methods)) if allowed_methods else [],
        "sort_preset": "round_robin_mix_methods_packs_score_total",
        "candidates_found": int(max(_cand_found("methods_first"), _cand_found("packs_first"), _cand_found("score_total_first"))),
        "mix": {
            "presets": list(presets),
            "source_indices": {p: ranked_lists[p][:top_k] for p in presets},
            "merged_indices": list(merged),
        },
        "chosen_indices": list(merged),
    }
    return list(merged), chooser


def _card_vtrac_packs_boxed_first_from_indices(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
    packs_target: int,
    indices: Sequence[int],
    chooser: Dict[str, Any],
) -> Dict[str, Any]:
    """
    Like `_card_vtrac_packs_boxed_first`, but uses a precomputed list of indices.
    """
    b = int(budget)
    want = max(1, int(packs_target))
    chosen: List[int] = []
    for raw in list(indices)[:want]:
        try:
            chosen.append(int(raw))
        except Exception:
            continue

    pack_combos: List[str] = []
    pack_combos_by_index: Dict[int, List[str]] = {}
    seen: set[str] = set()
    for idx in chosen:
        full = _vtrac_display_pack(index=int(idx))
        if not full:
            continue
        included: List[str] = []
        for token in full:
            c = _normalize_pick3_literal(token)
            if not c or c in seen:
                continue
            if len(pack_combos) >= b:
                break
            pack_combos.append(c)
            seen.add(c)
            included.append(c)
        if included:
            pack_combos_by_index[int(idx)] = included
        if len(pack_combos) >= b:
            break

    if not pack_combos:
        card = _card_convergence_box_first(ranked=ranked, budget=b)
        card["vtrac_pack"] = {
            "index": None,
            "indices": [],
            "packs_target": int(want),
            "pack_combos": [],
            "pack_combos_by_index": {},
            "chooser": chooser,
            "fallback": "convergence_box_first",
        }
        return card

    ranked_conv = sorted(list(ranked), key=_convergence_sort_key)

    selected: List[str] = list(pack_combos)
    selected_set: set[str] = set(selected)
    used_canon: set[str] = {c for c in (_canon(x) for x in selected_set) if c}
    prefer_unique = max(1, (b - len(selected)) // 2) if b > len(selected) else 0

    added = 0
    for row in ranked_conv:
        if len(selected) >= b:
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
        if len(selected) >= b:
            break
        combo = _normalize_pick3_literal(row.get("combo") or "")
        if not combo or combo in selected_set:
            continue
        selected.append(combo)
        selected_set.add(combo)

    selected = selected[:b]
    boxed = _boxed_canonicals(selected)
    used_indices = list(pack_combos_by_index.keys())
    return {
        "budget": int(b),
        "combos": selected,
        "combos_count": len(selected),
        "cost_units": len(selected),
        "boxed_canonicals": boxed,
        "boxed_canonicals_count": len(boxed),
        "vtrac_pack": {
            "index": int(used_indices[0]) if used_indices else None,
            "indices": list(used_indices),
            "packs_target": int(want),
            "pack_combos": list(pack_combos),
            "pack_combos_by_index": {int(k): list(v) for k, v in pack_combos_by_index.items()},
            "chooser": chooser,
        },
    }


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


def _card_vtrac_packs_boxed_first(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
    packs_target: int,
    allowed_methods: Optional[set[str]] = None,
    scan_limit: int = 350,
    sort_preset: str = "methods_first",
) -> Dict[str, Any]:
    """
    Like `_card_vtrac_pack_boxed_first`, but inserts multiple boxed-member packs (top-N indices).

    Motivation: the single-index chooser can miss the winner index even when CU evidence contains it.
    For Pick3, boxed-member packs are often ~8 lines, so B24 can represent ~3 indices directly.
    """
    b = int(budget)
    want = max(1, int(packs_target))

    indices, chooser = _choose_top_vtrac_indices(
        ranked=ranked,
        count=want,
        allowed_methods=allowed_methods,
        scan_limit=int(scan_limit),
        sort_preset=sort_preset,
    )
    if not indices and allowed_methods is not None:
        fallback_indices, fallback_chooser = _choose_top_vtrac_indices(
            ranked=ranked,
            count=want,
            allowed_methods=None,
            scan_limit=int(scan_limit),
            sort_preset=sort_preset,
        )
        chooser = {"filtered": chooser, "fallback_unfiltered": fallback_chooser}
        indices = fallback_indices

    pack_combos: List[str] = []
    pack_combos_by_index: Dict[int, List[str]] = {}
    seen: set[str] = set()
    for idx in indices:
        full = _vtrac_display_pack(index=int(idx))
        if not full:
            continue
        included: List[str] = []
        for token in full:
            c = _normalize_pick3_literal(token)
            if not c or c in seen:
                continue
            if len(pack_combos) >= b:
                break
            pack_combos.append(c)
            seen.add(c)
            included.append(c)
        if included:
            pack_combos_by_index[int(idx)] = included
        if len(pack_combos) >= b:
            break

    if not pack_combos:
        card = _card_convergence_box_first(ranked=ranked, budget=b)
        card["vtrac_pack"] = {
            "index": None,
            "indices": [],
            "packs_target": int(want),
            "pack_combos": [],
            "pack_combos_by_index": {},
            "chooser": chooser,
            "fallback": "convergence_box_first",
        }
        return card

    ranked_conv = sorted(list(ranked), key=_convergence_sort_key)

    selected: List[str] = list(pack_combos)
    selected_set: set[str] = set(selected)
    used_canon: set[str] = {c for c in (_canon(x) for x in selected_set) if c}
    prefer_unique = max(1, (b - len(selected)) // 2) if b > len(selected) else 0

    added = 0
    for row in ranked_conv:
        if len(selected) >= b:
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
        if len(selected) >= b:
            break
        combo = _normalize_pick3_literal(row.get("combo") or "")
        if not combo or combo in selected_set:
            continue
        selected.append(combo)
        selected_set.add(combo)

    selected = selected[:b]
    boxed = _boxed_canonicals(selected)
    used_indices = list(pack_combos_by_index.keys())
    return {
        "budget": int(b),
        "combos": selected,
        "combos_count": len(selected),
        "cost_units": len(selected),
        "boxed_canonicals": boxed,
        "boxed_canonicals_count": len(boxed),
        "vtrac_pack": {
            "index": int(used_indices[0]) if used_indices else None,
            "indices": list(used_indices),
            "packs_target": int(want),
            "pack_combos": list(pack_combos),
            "pack_combos_by_index": {int(k): list(v) for k, v in pack_combos_by_index.items()},
            "chooser": chooser,
        },
    }


def _card_vtrac_packs_boxed_first_lane_diverse_filler(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
    packs_target: int,
    allowed_methods: Optional[set[str]] = None,
    scan_limit: int = 350,
    sort_preset: str = "methods_first",
) -> Dict[str, Any]:
    """
    Hybrid selection policy:
    - Keep the same multi-pack "boxed-member packs first" behavior,
    - But use the small remaining filler budget to intentionally cover *additional* VTRAC indices
      (not already represented by the chosen packs).

    Motivation:
    - `CU_LANE_BUT_PLAY_MISS` indicates CU touched the winner lane, but the card failed to retain it.
    - Baseline packheavy often relies on filler to retain lanes; this makes filler lane-aware instead
      of duplicating pack lanes.
    """
    import modules.vtrac_reference as vr

    base = _card_vtrac_packs_boxed_first(
        ranked=ranked,
        budget=budget,
        packs_target=packs_target,
        allowed_methods=allowed_methods,
        scan_limit=scan_limit,
        sort_preset=sort_preset,
    )

    if not isinstance(base, dict):
        return base
    b = int(base.get("budget") or budget)
    vtrac_pack = base.get("vtrac_pack")
    if not isinstance(vtrac_pack, dict):
        return base

    pack_combos = vtrac_pack.get("pack_combos")
    pack_indices = vtrac_pack.get("indices")
    if not isinstance(pack_combos, list) or not pack_combos:
        return base
    if not isinstance(pack_indices, list) or not pack_indices:
        return base

    pack_index_set: set[int] = set()
    for raw in pack_indices:
        try:
            pack_index_set.add(int(raw))
        except Exception:
            continue

    # Start with pack combos (as-is), then re-fill using a lane-aware filler policy.
    selected: List[str] = []
    selected_set: set[str] = set()
    for token in pack_combos:
        c = _normalize_pick3_literal(token)
        if not c or c in selected_set:
            continue
        if len(selected) >= b:
            break
        selected.append(c)
        selected_set.add(c)

    ranked_conv = sorted(list(ranked), key=_convergence_sort_key)
    used_canon: set[str] = {c for c in (_canon(x) for x in selected_set) if c}
    prefer_unique = max(1, (b - len(selected)) // 2) if b > len(selected) else 0

    filler_slots = max(0, b - len(selected))
    outside_quota = filler_slots  # prefer outside-pack lanes for all filler slots when possible
    outside_added = 0
    added = 0

    # Phase A: fill from lanes NOT already represented by the chosen packs.
    for row in ranked_conv:
        if len(selected) >= b or outside_added >= outside_quota:
            break
        combo = _normalize_pick3_literal(row.get("combo") or "")
        if not combo or combo in selected_set:
            continue
        idx = vr.get_vtrac_index(combo)
        try:
            if idx is None or int(idx) in pack_index_set:
                continue
        except Exception:
            continue
        canon = _canon(combo)
        if canon and canon in used_canon and added < prefer_unique:
            continue
        selected.append(combo)
        selected_set.add(combo)
        if canon:
            used_canon.add(canon)
        added += 1
        outside_added += 1

    # Phase B: normal convergence fill (canonical-diverse first).
    for row in ranked_conv:
        if len(selected) >= b:
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
        if len(selected) >= b:
            break
        combo = _normalize_pick3_literal(row.get("combo") or "")
        if not combo or combo in selected_set:
            continue
        selected.append(combo)
        selected_set.add(combo)

    selected = selected[:b]
    boxed = _boxed_canonicals(selected)
    base["combos"] = selected
    base["combos_count"] = len(selected)
    base["cost_units"] = len(selected)
    base["boxed_canonicals"] = boxed
    base["boxed_canonicals_count"] = len(boxed)
    base["vtrac_pack"] = {**vtrac_pack, "filler_policy": "lane_diverse"}
    return base


def _card_vtrac_packs_boxed_then_box_first(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
    packs_target: int,
    allowed_methods: Optional[set[str]] = None,
    scan_limit: int = 350,
    sort_preset: str = "methods_first",
) -> Dict[str, Any]:
    """
    Hybrid conversion policy:
    1) Insert top-N boxed-member VTRAC packs (lane anchoring),
    2) Complete any high-scoring full BOX closures that fit (precision),
    3) Fill remaining lines by convergence ranking.

    This is selection-layer only and remains predictive-safe.
    """
    b = int(budget)
    want = max(1, int(packs_target))

    indices, chooser = _choose_top_vtrac_indices(
        ranked=ranked,
        count=want,
        allowed_methods=allowed_methods,
        scan_limit=int(scan_limit),
        sort_preset=sort_preset,
    )
    if not indices and allowed_methods is not None:
        fallback_indices, fallback_chooser = _choose_top_vtrac_indices(
            ranked=ranked,
            count=want,
            allowed_methods=None,
            scan_limit=int(scan_limit),
            sort_preset=sort_preset,
        )
        chooser = {"filtered": chooser, "fallback_unfiltered": fallback_chooser}
        indices = fallback_indices

    pack_combos: List[str] = []
    pack_combos_by_index: Dict[int, List[str]] = {}
    seen: set[str] = set()
    for idx in indices:
        full = _vtrac_display_pack(index=int(idx))
        if not full:
            continue
        included: List[str] = []
        for token in full:
            c = _normalize_pick3_literal(token)
            if not c or c in seen:
                continue
            if len(pack_combos) >= b:
                break
            pack_combos.append(c)
            seen.add(c)
            included.append(c)
        if included:
            pack_combos_by_index[int(idx)] = included
        if len(pack_combos) >= b:
            break

    if not pack_combos:
        card = _card_convergence_box_first(ranked=ranked, budget=b)
        card["vtrac_pack"] = {
            "index": None,
            "indices": [],
            "packs_target": int(want),
            "pack_combos": [],
            "pack_combos_by_index": {},
            "chooser": chooser,
            "fallback": "convergence_box_first",
        }
        return card

    selected: List[str] = list(pack_combos)
    selected_set: set[str] = set(selected)

    canon_to_combos: Dict[str, set[str]] = {}
    canon_score: Dict[str, float] = {}
    for row in ranked:
        combo = _normalize_pick3_literal(row.get("combo") or "")
        canon = _canon(combo)
        if not canon:
            continue
        canon_to_combos.setdefault(canon, set()).add(combo)
        canon_score[canon] = max(canon_score.get(canon, float("-inf")), float(row.get("score") or 0.0))

    boxable: List[Tuple[str, float, List[str]]] = []
    for canon, seen_combos in canon_to_combos.items():
        perms = sorted(set(_unique_perms(canon)))
        if perms and set(perms).issubset(seen_combos):
            boxable.append((canon, canon_score.get(canon, 0.0), perms))

    boxable.sort(key=lambda t: (-t[1], t[0]))
    for canon, _, perms in boxable:
        if len(selected) >= b:
            break
        needed = [c for c in perms if c not in selected_set]
        if not needed:
            continue
        if len(selected) + len(needed) > b:
            continue
        selected.extend(needed)
        selected_set.update(needed)

    ranked_conv = sorted(list(ranked), key=_convergence_sort_key)
    for row in ranked_conv:
        if len(selected) >= b:
            break
        combo = _normalize_pick3_literal(row.get("combo") or "")
        if not combo or combo in selected_set:
            continue
        selected.append(combo)
        selected_set.add(combo)

    selected = selected[:b]
    boxed = _boxed_canonicals(selected)
    used_indices = list(pack_combos_by_index.keys())
    return {
        "budget": int(b),
        "combos": selected,
        "combos_count": len(selected),
        "cost_units": len(selected),
        "boxed_canonicals": boxed,
        "boxed_canonicals_count": len(boxed),
        "vtrac_pack": {
            "index": int(used_indices[0]) if used_indices else None,
            "indices": list(used_indices),
            "packs_target": int(want),
            "pack_combos": list(pack_combos),
            "pack_combos_by_index": {int(k): list(v) for k, v in pack_combos_by_index.items()},
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


def _card_vtrac_pack_boxed_first_recency_tiebreak(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
    state_dir: Path,
    state_key: str,
    tie_preset: str,
    allowed_methods: Optional[set[str]] = None,
) -> Dict[str, Any]:
    """
    vtrac_pack_boxed_first + a short-horizon recency tie-break on index choice.

    This is a bounded *tie-break*, not a global penalization of repeats:
    - We only intervene when the top-2 indices are effectively tied on evidence.
    - We then prefer the index that has been absent from recent draw results.
    """
    chosen_index, chooser = _choose_top_vtrac_index_recency_tiebreak(
        ranked=ranked,
        state_dir=state_dir,
        state_key=state_key,
        tie_preset=tie_preset,
        allowed_methods=allowed_methods,
    )
    if chosen_index is None and allowed_methods is not None:
        fallback_index, fallback_chooser = _choose_top_vtrac_index_recency_tiebreak(
            ranked=ranked,
            state_dir=state_dir,
            state_key=state_key,
            tie_preset=tie_preset,
            allowed_methods=None,
        )
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
            "recency_tiebreak": {"preset": str(tie_preset), "spec": {"midday_draws": 2, "evening_draws": 2, "combined_draws": 4}},
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


def _card_v0_2_default_multi_pack(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
) -> Dict[str, Any]:
    """
    v0.2 posture variant: for B24/B36, insert multiple VTRAC boxed-member packs (top indices),
    then fill remaining lines by convergence ranking.
    """
    b = int(budget)
    if b <= 12:
        return _card_from_ranked(ranked=ranked, budget=b)
    # Balanced default: keep meaningful filler so we don't collapse lane diversity.
    # (Pick3 boxed-member packs are often ~8 lines.)
    packs_target = max(1, min(5, b // 12))
    return _card_vtrac_packs_boxed_first(ranked=ranked, budget=b, packs_target=packs_target)


def _card_v0_2_default_multi_pack_laneonly_presetB(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
) -> Dict[str, Any]:
    """
    v0.2 posture variant: multi-pack, but choose lanes using only "lane evidence" methods (presetB).
    """
    b = int(budget)
    if b <= 12:
        return _card_from_ranked(ranked=ranked, budget=b)
    packs_target = max(1, min(5, b // 12))
    lane_methods_presetB = _lane_methods_for_preset(preset="presetB")
    return _card_vtrac_packs_boxed_first(
        ranked=ranked, budget=b, packs_target=packs_target, allowed_methods=lane_methods_presetB
    )

def _card_v0_2_default_multi_pack_laneonly_presetB_packheavy(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
) -> Dict[str, Any]:
    """
    Conversion experiment (selection-only):
    - Choose lanes using only "lane evidence" methods (presetB),
    - Spend more of B36 on boxed-member VTRAC packs (4 indices when possible),
    - Keep B24 behavior unchanged (so we don't re-optimize coverage mid-experiment).

    Goal: improve B36 `pack_any_correct` / pack-attribution without touching analyzers.
    """
    b = int(budget)
    if b <= 12:
        return _card_from_ranked(ranked=ranked, budget=b)
    # Default pack targets (B24->2, B36->3), but pack-heavy at B36.
    packs_target = 4 if b >= 36 else max(1, min(5, b // 12))
    lane_methods_presetB = _lane_methods_for_preset(preset="presetB")
    return _card_vtrac_packs_boxed_first(
        ranked=ranked, budget=b, packs_target=packs_target, allowed_methods=lane_methods_presetB
    )


def _card_v0_2_default_multi_pack_laneonly_presetB_packheavy_scan2000(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
) -> Dict[str, Any]:
    """
    Conversion experiment (selection-only): same as packheavy, but scan deeper into ranked candidates
    when choosing VTRAC indices so we don't miss winner lanes that show up below the top-350.
    """
    b = int(budget)
    if b <= 12:
        return _card_from_ranked(ranked=ranked, budget=b)
    packs_target = 4 if b >= 36 else max(1, min(5, b // 12))
    lane_methods_presetB = _lane_methods_for_preset(preset="presetB")
    return _card_vtrac_packs_boxed_first(
        ranked=ranked,
        budget=b,
        packs_target=packs_target,
        allowed_methods=lane_methods_presetB,
        scan_limit=2000,
        sort_preset="methods_first",
    )


def _card_v0_2_default_multi_pack_laneonly_presetB_packheavy_scorefirst_scan2000(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
) -> Dict[str, Any]:
    """
    Conversion experiment (selection-only): packheavy + deeper scan + different lane chooser ordering.

    Chooser change: prioritize indices with higher `score_total` first, then corroboration.
    """
    b = int(budget)
    if b <= 12:
        return _card_from_ranked(ranked=ranked, budget=b)
    packs_target = 4 if b >= 36 else max(1, min(5, b // 12))
    lane_methods_presetB = _lane_methods_for_preset(preset="presetB")
    return _card_vtrac_packs_boxed_first(
        ranked=ranked,
        budget=b,
        packs_target=packs_target,
        allowed_methods=lane_methods_presetB,
        scan_limit=2000,
        sort_preset="score_total_first",
    )


def _card_v0_2_default_multi_pack_packheavy(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
) -> Dict[str, Any]:
    """
    Conversion experiment (selection-only): increase B36 pack count (4 indices), without restricting
    lane selection to presetB methods.
    """
    b = int(budget)
    if b <= 12:
        return _card_from_ranked(ranked=ranked, budget=b)
    packs_target = 4 if b >= 36 else max(1, min(5, b // 12))
    return _card_vtrac_packs_boxed_first(ranked=ranked, budget=b, packs_target=packs_target)


def _card_v0_2_default_multi_pack_packheavy_lane_diverse_filler(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
) -> Dict[str, Any]:
    """
    Conversion experiment (selection-only): packheavy at B36, but allocate the small filler tail
    to cover additional lanes (outside the chosen packs).
    """
    b = int(budget)
    if b <= 12:
        return _card_from_ranked(ranked=ranked, budget=b)
    if b < 36:
        return _card_v0_2_default_multi_pack_packheavy(ranked=ranked, budget=b)
    return _card_vtrac_packs_boxed_first_lane_diverse_filler(ranked=ranked, budget=b, packs_target=4)


def _card_v0_2_default_multi_pack_mop_24_12(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
) -> Dict[str, Any]:
    """
    Mixture-of-Policies (selection-only): B36-only deterministic blend (24/12).

    Motivation: treat B36 as a multi-hypothesis environment. Rather than committing the entire
    budget to one policy, allocate a fixed split across two complementary micro-policies and merge.

    A (24): pack semantics baseline (packheavy + lane-diverse filler) — truncated to 24 lines.
    B (12): strict hedge via convergence ranking (no pack semantics).
    """
    b = int(budget)
    if b <= 12:
        return _card_from_ranked(ranked=ranked, budget=b)
    if b < 36:
        return _card_v0_2_default_multi_pack_packheavy(ranked=ranked, budget=b)

    a_budget = 24
    b_budget = 12
    a_full = _card_v0_2_default_multi_pack_packheavy_lane_diverse_filler(ranked=ranked, budget=36)
    b_card = _card_convergence_box_first(ranked=ranked, budget=b_budget)

    a_full_combos = [_normalize_pick3_literal(x) for x in (a_full.get("combos") or [])]
    a_full_combos = [x for x in a_full_combos if x]

    # IMPORTANT: preserve some lane-diverse filler inside the A slice; a naive prefix truncation would
    # often become "pack-only", collapsing `hit_any_inclusive` (lane retention).
    a_list: List[str] = []
    vtrac_pack_raw = a_full.get("vtrac_pack")
    if isinstance(vtrac_pack_raw, dict) and isinstance(vtrac_pack_raw.get("pack_combos"), list):
        pack_raw = [_normalize_pick3_literal(x) for x in (vtrac_pack_raw.get("pack_combos") or [])]
        pack_raw = [x for x in pack_raw if x]
        pack_set = set(pack_raw)
        filler = [c for c in a_full_combos if c not in pack_set]

        filler_keep = min(len(filler), a_budget)
        pack_keep = max(0, a_budget - filler_keep)
        pack_take: List[str] = []
        seen: set[str] = set()
        for c in pack_raw:
            if c in seen:
                continue
            pack_take.append(c)
            seen.add(c)
            if len(pack_take) >= pack_keep:
                break

        a_list = list(pack_take) + list(filler[:filler_keep])

        # Top up deterministically if we couldn't reach a_budget (rare).
        for c in a_full_combos:
            if len(a_list) >= a_budget:
                break
            if c in set(a_list):
                continue
            a_list.append(c)
    else:
        a_list = list(a_full_combos[:a_budget])

    a_list = a_list[:a_budget]
    b_list = [_normalize_pick3_literal(x) for x in (b_card.get("combos") or [])]
    b_list = [x for x in b_list if x][:b_budget]

    selected: List[str] = []
    selected_set: set[str] = set()
    combo_source: Dict[str, str] = {}

    def _add(combo: str, source: str) -> bool:
        c = _normalize_pick3_literal(combo)
        if not c or c in selected_set:
            return False
        if len(selected) >= b:
            return False
        selected.append(c)
        selected_set.add(c)
        combo_source[c] = source
        return True

    for c in a_list:
        _add(c, "A")

    overlap = 0
    for c in b_list:
        if _normalize_pick3_literal(c) in selected_set:
            overlap += 1
        _add(c, "B")

    ranked_conv = sorted(list(ranked), key=_convergence_sort_key)
    topup_added = 0
    for row in ranked_conv:
        if len(selected) >= b:
            break
        combo = _normalize_pick3_literal(row.get("combo") or "")
        if _add(combo, "topup"):
            topup_added += 1

    selected = selected[:b]
    boxed = _boxed_canonicals(selected)

    vtrac_pack: Optional[Dict[str, Any]] = None
    if isinstance(vtrac_pack_raw, dict):
        pack_combos = vtrac_pack_raw.get("pack_combos")
        pack_by_idx = vtrac_pack_raw.get("pack_combos_by_index")
        if isinstance(pack_combos, list) and isinstance(pack_by_idx, dict):
            pack_combos_filtered = [
                _normalize_pick3_literal(x) for x in pack_combos if _normalize_pick3_literal(x) in selected_set
            ]
            pack_combos_filtered = [x for x in pack_combos_filtered if x]

            pack_by_idx_filtered: Dict[int, List[str]] = {}
            for k, v in pack_by_idx.items():
                try:
                    idx = int(k)
                except Exception:
                    continue
                if not isinstance(v, list):
                    continue
                included = [
                    _normalize_pick3_literal(x) for x in v if _normalize_pick3_literal(x) in selected_set
                ]
                included = [x for x in included if x]
                if included:
                    pack_by_idx_filtered[idx] = included

            indices = [int(x) for x in vtrac_pack_raw.get("indices") or [] if str(x).lstrip("-").isdigit()]
            indices = [i for i in indices if i in set(pack_by_idx_filtered.keys())]

            vtrac_pack = {
                **vtrac_pack_raw,
                "indices": indices,
                "pack_combos": pack_combos_filtered,
                "pack_combos_by_index": {int(k): list(v) for k, v in pack_by_idx_filtered.items()},
                "filler_policy": "mop_24_12",
            }

    return {
        "budget": int(b),
        "combos": selected,
        "combos_count": len(selected),
        "cost_units": len(selected),
        "boxed_canonicals": boxed,
        "boxed_canonicals_count": len(boxed),
        "vtrac_pack": vtrac_pack,
        "mop": {
            "split": {"A": int(a_budget), "B": int(b_budget)},
            "A_policy": "v0_2_default_multi_pack_packheavy_lane_diverse_filler",
            "B_policy": "convergence_box_first",
            "overlap_count": int(overlap),
            "topup_count": int(topup_added),
            "combo_source": combo_source,
        },
    }


def _card_v0_2_default_multi_pack_index_alloc_top12_4_3_2(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
    scan_limit: int = 350,
    sort_preset: str = "methods_first",
) -> Dict[str, Any]:
    """
    Allocation geometry experiment (selection-only): spread B36 across MORE indices.

    Policy:
    - Choose top-12 VTRAC indices by CU evidence (full ranking, not top-5 truncated).
    - Allocate lines per index using a fixed schedule: 4/4/4/4/3/3/3/3/2/2/2/2 (sum=36).
    - Pick top combos *within each index* by convergence priority (not by VTRAC_DISPLAY order).
    """
    import modules.vtrac_reference as vr

    b = int(budget)
    if b <= 12:
        return _card_from_ranked(ranked=ranked, budget=b)
    if b < 36:
        return _card_v0_2_default_multi_pack_packheavy_lane_diverse_filler(ranked=ranked, budget=b)

    indices_target = 12
    quotas = [4, 4, 4, 4, 3, 3, 3, 3, 2, 2, 2, 2]
    if len(quotas) != indices_target or sum(quotas) != b:
        raise SystemExit("Internal error: allocation schedule must be 12 entries summing to 36.")

    ranked_conv = sorted(list(ranked), key=_convergence_sort_key)

    indices, chooser = _choose_top_vtrac_indices_full(
        ranked=ranked,
        count=indices_target,
        scan_limit=int(scan_limit),
        allowed_methods=None,
        sort_preset=sort_preset,
    )

    if not indices:
        card = _card_convergence_box_first(ranked=ranked, budget=b)
        card["vtrac_pack"] = {
            "index": None,
            "indices": [],
            "packs_target": int(indices_target),
            "pack_combos": [],
            "pack_combos_by_index": {},
            "chooser": chooser,
            "fallback": "convergence_box_first",
            "filler_policy": "index_alloc_top12_4_3_2",
        }
        return card

    selected: List[str] = []
    selected_set: set[str] = set()
    pack_combos: List[str] = []
    pack_combos_by_index: Dict[int, List[str]] = {}

    row_by_combo: Dict[str, Dict[str, Any]] = {}
    for row in ranked:
        if not isinstance(row, dict):
            continue
        c = _normalize_pick3_literal(row.get("combo") or "")
        if c and c not in row_by_combo:
            row_by_combo[c] = row

    # Index -> ranked candidates within that lane (in convergence order).
    lane_rows: Dict[int, List[Dict[str, Any]]] = {}
    for row in ranked_conv:
        if not isinstance(row, dict):
            continue
        combo = _normalize_pick3_literal(row.get("combo") or "")
        if not combo:
            continue
        idx = vr.get_vtrac_index(combo)
        if not isinstance(idx, int):
            continue
        lane_rows.setdefault(int(idx), []).append(row)

    for i, idx in enumerate(indices[:indices_target]):
        want = int(quotas[i]) if i < len(quotas) else 0
        if want <= 0:
            continue
        included: List[str] = []

        # Phase A: prefer the VTRAC display pack members (boxed-member pack), ordered by CU evidence
        # when available (convergence key), so we don't pick arbitrary members.
        full = _vtrac_display_pack(index=int(idx))
        scored_display: List[Tuple[Tuple[int, int, int, int, float, str], str]] = []
        seen_display: set[str] = set()
        for token in full:
            c = _normalize_pick3_literal(token)
            if not c or c in seen_display:
                continue
            seen_display.add(c)
            row = row_by_combo.get(c)
            if isinstance(row, dict):
                key = _convergence_sort_key(row)
            else:
                # Missing from CU evidence: sort after any evidence-backed display members.
                key = (0, 0, 0, 0, 0.0, c)
            scored_display.append((key, c))

        scored_display.sort(key=lambda t: t[0])
        for _key, combo in scored_display:
            if len(included) >= want or len(selected) >= b:
                break
            if combo in selected_set:
                continue
            selected.append(combo)
            selected_set.add(combo)
            pack_combos.append(combo)
            included.append(combo)

        # Phase B: if we couldn't fill the quota from display members, top up from CU lane candidates.
        if len(included) < want:
            for row in lane_rows.get(int(idx), []):
                if len(included) >= want or len(selected) >= b:
                    break
                combo = _normalize_pick3_literal(row.get("combo") or "")
                if not combo or combo in selected_set:
                    continue
                selected.append(combo)
                selected_set.add(combo)
                pack_combos.append(combo)
                included.append(combo)

        if included:
            pack_combos_by_index[int(idx)] = included

    # If some indices had insufficient candidates, top up remaining budget from convergence (global).
    for row in ranked_conv:
        if len(selected) >= b:
            break
        combo = _normalize_pick3_literal(row.get("combo") or "")
        if not combo or combo in selected_set:
            continue
        selected.append(combo)
        selected_set.add(combo)

    selected = selected[:b]
    boxed = _boxed_canonicals(selected)
    used_indices = list(pack_combos_by_index.keys())
    return {
        "budget": int(b),
        "combos": selected,
        "combos_count": len(selected),
        "cost_units": len(selected),
        "boxed_canonicals": boxed,
        "boxed_canonicals_count": len(boxed),
        "vtrac_pack": {
            "index": int(used_indices[0]) if used_indices else None,
            "indices": list(used_indices),
            "packs_target": int(indices_target),
            "pack_combos": list(pack_combos),
            "pack_combos_by_index": {int(k): list(v) for k, v in pack_combos_by_index.items()},
            "chooser": chooser,
            "filler_policy": "index_alloc_top12_4_3_2",
            "allocation": {
                "indices_target": int(indices_target),
                "quotas": list(quotas),
                "scan_limit": int(scan_limit),
                "sort_preset": str(sort_preset),
            },
        },
    }

def _card_v0_2_default_multi_pack_packheavy_spine4_index_tail(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
    scan_limit: int = 350,
    sort_preset: str = "methods_first",
) -> Dict[str, Any]:
    """
    Hybrid conversion (selection-only): preserve a deep packheavy spine (full boxed-member packs),
    then spend remaining budget touching additional *ranked* VTRAC indices (1 combo per index).

    Goal: increase lane retention (reduce CU_LANE_BUT_PLAY_MISS) without sacrificing strict hits
    from the deep spine packs.
    """
    import modules.vtrac_reference as vr

    b = int(budget)
    if b <= 12:
        return _card_from_ranked(ranked=ranked, budget=b)
    if b < 36:
        return _card_v0_2_default_multi_pack_packheavy_lane_diverse_filler(ranked=ranked, budget=b)

    spine_packs_target = 4
    rank_count = 35  # max known display indices is ~35; safe ceiling
    indices_ranked, chooser_ranked = _choose_top_vtrac_indices_full(
        ranked=ranked,
        count=rank_count,
        scan_limit=int(scan_limit),
        allowed_methods=None,
        sort_preset=sort_preset,
    )
    if not indices_ranked:
        return _card_v0_2_default_multi_pack_packheavy_lane_diverse_filler(ranked=ranked, budget=b)

    ranked_conv = sorted(list(ranked), key=_convergence_sort_key)
    lane_rows: Dict[int, List[Dict[str, Any]]] = {}
    for row in ranked_conv:
        if not isinstance(row, dict):
            continue
        combo = _normalize_pick3_literal(row.get("combo") or "")
        if not combo:
            continue
        idx = vr.get_vtrac_index(combo)
        if not isinstance(idx, int):
            continue
        lane_rows.setdefault(int(idx), []).append(row)

    selected: List[str] = []
    selected_set: set[str] = set()
    pack_combos: List[str] = []
    pack_combos_by_index: Dict[int, List[str]] = {}

    def _add_pack(idx: int, combo: str) -> bool:
        c = _normalize_pick3_literal(combo)
        if not c or c in selected_set:
            return False
        if len(selected) >= b:
            return False
        selected.append(c)
        selected_set.add(c)
        pack_combos.append(c)
        pack_combos_by_index.setdefault(int(idx), []).append(c)
        return True

    used_indices: set[int] = set()

    # Spine: insert full boxed-member packs for the top-N ranked indices.
    for raw in indices_ranked[:spine_packs_target]:
        idx = int(raw)
        if idx in used_indices:
            continue
        for token in _vtrac_display_pack(index=idx):
            if len(selected) >= b:
                break
            _add_pack(idx, token)
        used_indices.add(idx)
        if len(selected) >= b:
            break

    # Tail: touch additional ranked indices (1 evidence-backed combo per index, else display fallback).
    tail_added = 0
    for raw in indices_ranked[spine_packs_target:]:
        if len(selected) >= b:
            break
        idx = int(raw)
        if idx in used_indices:
            continue

        chosen = ""
        for row in lane_rows.get(idx, []):
            c = _normalize_pick3_literal(row.get("combo") or "")
            if c and c not in selected_set:
                chosen = c
                break
        if not chosen:
            for token in _vtrac_display_pack(index=idx):
                c = _normalize_pick3_literal(token)
                if c and c not in selected_set:
                    chosen = c
                    break
        if not chosen:
            continue

        if _add_pack(idx, chosen):
            used_indices.add(idx)
            tail_added += 1

    # Safety top-up: if we couldn't fill due to duplicates/empty packs, fill remaining from convergence.
    for row in ranked_conv:
        if len(selected) >= b:
            break
        combo = _normalize_pick3_literal(row.get("combo") or "")
        if not combo or combo in selected_set:
            continue
        selected.append(combo)
        selected_set.add(combo)

    selected = selected[:b]
    boxed = _boxed_canonicals(selected)
    used_indices_list = list(pack_combos_by_index.keys())
    return {
        "budget": int(b),
        "combos": selected,
        "combos_count": len(selected),
        "cost_units": len(selected),
        "boxed_canonicals": boxed,
        "boxed_canonicals_count": len(boxed),
        "vtrac_pack": {
            "index": int(used_indices_list[0]) if used_indices_list else None,
            "indices": list(used_indices_list),
            "packs_target": int(spine_packs_target),
            "pack_combos": list(pack_combos),
            "pack_combos_by_index": {int(k): list(v) for k, v in pack_combos_by_index.items()},
            "chooser": {
                "ranked_indices": chooser_ranked,
                "spine_packs_target": int(spine_packs_target),
                "rank_count": int(rank_count),
            },
            "filler_policy": "spine4_index_tail",
            "allocation": {
                "scan_limit": int(scan_limit),
                "sort_preset": str(sort_preset),
                "spine_packs_target": int(spine_packs_target),
                "tail_added": int(tail_added),
            },
        },
    }


def _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
    spine_max_lines_per_index: int,
    spine_taper_caps: Optional[Sequence[int]] = None,
    spine_pick_mode: str = "display",
    tail_pick_mode: str = "convergence",
    scan_limit: int = 350,
    sort_preset: str = "methods_first",
    spine_sort_preset: Optional[str] = None,
    tail_sort_preset: Optional[str] = None,
    indices_ranked_override: Optional[Sequence[int]] = None,
    chooser_ranked_override: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Anti-spike variant (selection-only):
    - Keep the same spine+tail geometry as `...spine4_index_tail`,
    - but cap the per-index spend in the 4-pack spine, then reallocate freed lines to tail breadth.

    Goal: reduce CU_LANE_BUT_PLAY_MISS by preventing "8-line spine spikes" from collapsing lane breadth.
    """
    import modules.vtrac_reference as vr

    b = int(budget)
    if b <= 12:
        return _card_from_ranked(ranked=ranked, budget=b)
    if b < 36:
        return _card_v0_2_default_multi_pack_packheavy_lane_diverse_filler(ranked=ranked, budget=b)

    spine_packs_target = 4
    rank_count = 35  # max known display indices is ~35; safe ceiling
    spine_sort = str(spine_sort_preset or sort_preset).strip()
    tail_sort = str(tail_sort_preset or sort_preset).strip()
    if indices_ranked_override is not None:
        indices_ranked = [int(x) for x in indices_ranked_override]
        chooser_ranked = dict(chooser_ranked_override or {})
        chooser_ranked.setdefault("scan_limit", int(scan_limit))
        chooser_ranked.setdefault("sort_preset", str(sort_preset or ""))
        chooser_ranked.setdefault("chosen_indices", indices_ranked[: int(rank_count)])
        chooser_ranked.setdefault("candidates_found", int(len(indices_ranked)))
    elif spine_sort == tail_sort:
        indices_ranked, chooser_ranked = _choose_top_vtrac_indices_full(
            ranked=ranked,
            count=rank_count,
            scan_limit=int(scan_limit),
            allowed_methods=None,
            sort_preset=spine_sort,
        )
    else:
        spine_ranked, spine_snapshot = _choose_top_vtrac_indices_full(
            ranked=ranked,
            count=rank_count,
            scan_limit=int(scan_limit),
            allowed_methods=None,
            sort_preset=spine_sort,
        )
        tail_ranked, tail_snapshot = _choose_top_vtrac_indices_full(
            ranked=ranked,
            count=rank_count,
            scan_limit=int(scan_limit),
            allowed_methods=None,
            sort_preset=tail_sort,
        )
        spine_indices: List[int] = []
        for raw in spine_ranked:
            idx = int(raw)
            if idx not in spine_indices:
                spine_indices.append(idx)
            if len(spine_indices) >= int(spine_packs_target):
                break
        used = set(spine_indices)
        tail_only: List[int] = []
        for raw in tail_ranked:
            idx = int(raw)
            if idx in used:
                continue
            tail_only.append(idx)
            used.add(idx)
        indices_ranked = list(spine_indices) + list(tail_only)

        chooser_ranked = dict(tail_snapshot)
        chooser_ranked["sort_preset"] = f"split_spine_{spine_sort}__tail_{tail_sort}"
        chooser_ranked["spine_sort_preset"] = spine_sort
        chooser_ranked["tail_sort_preset"] = tail_sort
        chooser_ranked["spine_chosen_indices"] = list(spine_indices)
        chooser_ranked["chosen_indices"] = indices_ranked[: int(rank_count)]
        chooser_ranked["topN_spine"] = spine_snapshot.get("topN") if isinstance(spine_snapshot, dict) else []
    if not indices_ranked:
        return _card_v0_2_default_multi_pack_packheavy_lane_diverse_filler(ranked=ranked, budget=b)

    ranked_conv = sorted(list(ranked), key=_convergence_sort_key)
    lane_rows: Dict[int, List[Dict[str, Any]]] = {}
    for row in ranked_conv:
        if not isinstance(row, dict):
            continue
        combo = _normalize_pick3_literal(row.get("combo") or "")
        if not combo:
            continue
        idx = vr.get_vtrac_index(combo)
        if not isinstance(idx, int):
            continue
        lane_rows.setdefault(int(idx), []).append(row)

    spine_mode = str(spine_pick_mode or "display").strip().lower()
    if spine_mode.startswith("hybrid"):
        pass
    elif spine_mode not in {"display", "evidence", "display_ranked", "display_canon_ranked"}:
        spine_mode = "display"

    tail_mode = str(tail_pick_mode or "convergence").strip().lower()
    if tail_mode not in {"convergence", "score_first"}:
        tail_mode = "convergence"

    selected: List[str] = []
    selected_set: set[str] = set()
    pack_combos: List[str] = []
    pack_combos_by_index: Dict[int, List[str]] = {}

    def _add_pack(idx: int, combo: str) -> bool:
        c = _normalize_pick3_literal(combo)
        if not c or c in selected_set:
            return False
        if len(selected) >= b:
            return False
        selected.append(c)
        selected_set.add(c)
        pack_combos.append(c)
        pack_combos_by_index.setdefault(int(idx), []).append(c)
        return True

    used_indices: set[int] = set()
    spine_max = max(0, int(spine_max_lines_per_index))
    taper_raw = [int(x) for x in spine_taper_caps] if spine_taper_caps else []
    taper_caps = [max(0, min(int(x), int(spine_max))) for x in taper_raw]

    # Spine: insert capped boxed-member packs for the top-N ranked indices.
    for i, raw in enumerate(indices_ranked[:spine_packs_target]):
        idx = int(raw)
        if idx in used_indices:
            continue
        idx_cap = int(spine_max)
        if taper_caps and i < len(taper_caps):
            idx_cap = int(taper_caps[i])
        added = 0
        if spine_mode == "evidence":
            # Prefer evidence-backed combos inside the lane, then fall back to display members.
            lane_list = list(lane_rows.get(idx, []))
            lane_list.sort(key=_convergence_sort_key)
            for row in lane_list:
                if len(selected) >= b:
                    break
                if idx_cap and added >= idx_cap:
                    break
                token = _normalize_pick3_literal(row.get("combo") or "")
                if _add_pack(idx, token):
                    added += 1
            if not idx_cap or added < idx_cap:
                for token in _vtrac_display_pack(index=idx):
                    if len(selected) >= b:
                        break
                    if idx_cap and added >= idx_cap:
                        break
                    if _add_pack(idx, token):
                        added += 1
        elif spine_mode == "display_ranked":
            # Still use the display pack, but take the members with strongest evidence first.
            row_by_combo: Dict[str, Dict[str, Any]] = {}
            for row in ranked_conv:
                c = _normalize_pick3_literal(row.get("combo") or "")
                if c and c not in row_by_combo:
                    row_by_combo[c] = row

            scored: List[Tuple[Tuple[int, int, int, int, float, str], str]] = []
            for token in _vtrac_display_pack(index=idx):
                c = _normalize_pick3_literal(token)
                if not c:
                    continue
                row = row_by_combo.get(c)
                if row:
                    key = _convergence_sort_key(row)
                else:
                    key = (999, 999, 999, 999, 999.0, c)
                scored.append((key, c))
            scored.sort(key=lambda t: t[0])
            for _, token in scored:
                if len(selected) >= b:
                    break
                if idx_cap and added >= idx_cap:
                    break
                if _add_pack(idx, token):
                    added += 1
        elif spine_mode == "display_canon_ranked":
            # Still use the display pack, but rank members by canonical/permutation evidence:
            # if any permutation of a display member's canonical appears in lane evidence, prefer
            # that canonical's strongest-evidence row.
            display_tokens = list(_vtrac_display_pack(index=idx))
            base_pos = {c: i for i, c in enumerate(display_tokens)}

            best_key_by_canon: Dict[str, Tuple[int, int, int, int, float]] = {}
            for row in lane_rows.get(idx, []):
                c = _normalize_pick3_literal(row.get("combo") or "")
                if not c:
                    continue
                canon = _canon(c)
                if not canon:
                    continue
                key5 = _convergence_sort_key(row)[:-1]
                prev = best_key_by_canon.get(canon)
                if prev is None or key5 < prev:
                    best_key_by_canon[canon] = key5

            scored2: List[Tuple[Tuple[int, int, int, int, float, int], str]] = []
            for token in display_tokens:
                c = _normalize_pick3_literal(token)
                if not c:
                    continue
                canon = _canon(c)
                key5 = best_key_by_canon.get(canon) or (999, 999, 999, 999, 999.0)
                scored2.append(((*key5, int(base_pos.get(c, 999))), c))
            scored2.sort(key=lambda t: t[0])
            for _, token in scored2:
                if len(selected) >= b:
                    break
                if idx_cap and added >= idx_cap:
                    break
                if _add_pack(idx, token):
                    added += 1
        elif spine_mode.startswith("hybrid"):
            # Hybrid: preserve bounded display coverage first, then add a small number of evidence
            # rows, then fill remaining capacity with display.
            #
            # Mode format: `hybrid_d<min_display>_e<max_evidence>` (e.g., `hybrid_d4_e2`).
            display_min = 4
            evidence_max = 2
            m = re.match(r"^hybrid(?:_d(?P<d>\\d+))?(?:_e(?P<e>\\d+))?$", spine_mode)
            if m:
                if m.group("d"):
                    display_min = int(m.group("d"))
                if m.group("e"):
                    evidence_max = int(m.group("e"))

            if idx_cap > 0:
                display_min = max(0, min(int(display_min), int(idx_cap)))
                evidence_max = max(0, min(int(evidence_max), int(idx_cap) - int(display_min)))
            else:
                display_min = max(0, int(display_min))
                evidence_max = max(0, int(evidence_max))

            display_tokens = list(_vtrac_display_pack(index=idx))

            # 1) Display anchor (baseline order).
            added_display = 0
            for token in display_tokens:
                if len(selected) >= b:
                    break
                if idx_cap and added >= idx_cap:
                    break
                if added_display >= display_min:
                    break
                if _add_pack(idx, token):
                    added += 1
                    added_display += 1

            # 2) Evidence add-ons (highest convergence first; may include non-display).
            added_evidence = 0
            lane_list = list(lane_rows.get(idx, []))
            lane_list.sort(key=_convergence_sort_key)
            for row in lane_list:
                if len(selected) >= b:
                    break
                if idx_cap and added >= idx_cap:
                    break
                if added_evidence >= evidence_max:
                    break
                token = _normalize_pick3_literal(row.get("combo") or "")
                if _add_pack(idx, token):
                    added += 1
                    added_evidence += 1

            # 3) Fill remaining capacity with display.
            for token in display_tokens:
                if len(selected) >= b:
                    break
                if idx_cap and added >= idx_cap:
                    break
                if _add_pack(idx, token):
                    added += 1
        else:
            # Baseline behavior: fixed display order.
            for token in _vtrac_display_pack(index=idx):
                if len(selected) >= b:
                    break
                if idx_cap and added >= idx_cap:
                    break
                if _add_pack(idx, token):
                    added += 1
        used_indices.add(idx)
        if len(selected) >= b:
            break

    # Tail: touch additional ranked indices (1 evidence-backed combo per index, else display fallback).
    tail_added = 0
    for raw in indices_ranked[spine_packs_target:]:
        if len(selected) >= b:
            break
        idx = int(raw)
        if idx in used_indices:
            continue

        chosen = ""
        lane_list = list(lane_rows.get(idx, []))
        if tail_mode == "score_first":
            lane_list.sort(key=_score_first_sort_key)
        # else: lane_rows are already populated in `_convergence_sort_key` order via ranked_conv
        for row in lane_list:
            c = _normalize_pick3_literal(row.get("combo") or "")
            if c and c not in selected_set:
                chosen = c
                break
        if not chosen:
            for token in _vtrac_display_pack(index=idx):
                c = _normalize_pick3_literal(token)
                if c and c not in selected_set:
                    chosen = c
                    break
        if not chosen:
            continue

        if _add_pack(idx, chosen):
            used_indices.add(idx)
            tail_added += 1

    # Safety top-up: if we couldn't fill due to duplicates/empty packs, fill remaining from convergence.
    for row in ranked_conv:
        if len(selected) >= b:
            break
        combo = _normalize_pick3_literal(row.get("combo") or "")
        if not combo or combo in selected_set:
            continue
        selected.append(combo)
        selected_set.add(combo)

    selected = selected[:b]
    boxed = _boxed_canonicals(selected)
    used_indices_list = list(pack_combos_by_index.keys())
    taper_label = "_taper" + "".join(str(x) for x in taper_caps[:spine_packs_target]) if taper_caps else ""
    return {
        "budget": int(b),
        "combos": selected,
        "combos_count": len(selected),
        "cost_units": len(selected),
        "boxed_canonicals": boxed,
        "boxed_canonicals_count": len(boxed),
        "vtrac_pack": {
            "index": int(used_indices_list[0]) if used_indices_list else None,
            "indices": list(used_indices_list),
            "packs_target": int(spine_packs_target),
            "pack_combos": list(pack_combos),
            "pack_combos_by_index": {int(k): list(v) for k, v in pack_combos_by_index.items()},
            "chooser": {
                "ranked_indices": chooser_ranked,
                "spine_packs_target": int(spine_packs_target),
                "rank_count": int(rank_count),
            },
            "filler_policy": f"spine4_index_tail_spinecap{spine_max or '0'}{taper_label}",
            "allocation": {
                "scan_limit": int(scan_limit),
                "sort_preset": str(sort_preset),
                "spine_sort_preset": str(spine_sort_preset or ""),
                "tail_sort_preset": str(tail_sort_preset or ""),
                "spine_packs_target": int(spine_packs_target),
                "spine_max_lines_per_index": int(spine_max),
                "spine_taper_caps": ",".join(str(x) for x in taper_caps) if taper_caps else "",
                "spine_pick_mode": str(spine_mode),
                "tail_pick_mode": str(tail_mode),
                "tail_added": int(tail_added),
            },
        },
    }


def _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
    scan_limit: int = 350,
    sort_preset: str = "methods_first",
) -> Dict[str, Any]:
    return _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap(
        ranked=ranked,
        budget=budget,
        spine_max_lines_per_index=6,
        spine_pick_mode="display",
        scan_limit=scan_limit,
        sort_preset=sort_preset,
    )


def _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap7(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
    scan_limit: int = 350,
    sort_preset: str = "methods_first",
) -> Dict[str, Any]:
    return _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap(
        ranked=ranked,
        budget=budget,
        spine_max_lines_per_index=7,
        spine_pick_mode="display",
        scan_limit=scan_limit,
        sort_preset=sort_preset,
    )


def _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_evidence(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
    scan_limit: int = 350,
    sort_preset: str = "methods_first",
) -> Dict[str, Any]:
    return _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap(
        ranked=ranked,
        budget=budget,
        spine_max_lines_per_index=6,
        spine_pick_mode="evidence",
        scan_limit=scan_limit,
        sort_preset=sort_preset,
    )


def _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_display_ranked(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
    scan_limit: int = 350,
    sort_preset: str = "methods_first",
) -> Dict[str, Any]:
    return _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap(
        ranked=ranked,
        budget=budget,
        spine_max_lines_per_index=6,
        spine_pick_mode="display_ranked",
        scan_limit=scan_limit,
        sort_preset=sort_preset,
    )


def _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_display_canon_ranked(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
    scan_limit: int = 350,
    sort_preset: str = "methods_first",
) -> Dict[str, Any]:
    return _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap(
        ranked=ranked,
        budget=budget,
        spine_max_lines_per_index=6,
        spine_pick_mode="display_canon_ranked",
        scan_limit=scan_limit,
        sort_preset=sort_preset,
    )


def _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
    scan_limit: int = 350,
    sort_preset: str = "methods_first",
) -> Dict[str, Any]:
    """
    Allocation-level lever (selection-only): keep `spinecap6` semantics, but taper the 4 spine
    indices as:
      - rank 1: 6 lines
      - rank 2: 6 lines
      - rank 3: 4 lines
      - rank 4: 4 lines

    Frees 4 lines to extend tail breadth under the same B36 budget.
    """
    return _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap(
        ranked=ranked,
        budget=budget,
        spine_max_lines_per_index=6,
        spine_taper_caps=(6, 6, 4, 4),
        spine_pick_mode="display",
        scan_limit=scan_limit,
        sort_preset=sort_preset,
    )


def _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_spine_display_ranked(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
    scan_limit: int = 350,
    sort_preset: str = "methods_first",
) -> Dict[str, Any]:
    """
    Within-spine conversion lever (selection-only): keep taper6644 geometry, but choose the spine
    display members in evidence-ranked order (important when the taper drops spine ranks 3–4 to 4
    lines).
    """
    return _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap(
        ranked=ranked,
        budget=budget,
        spine_max_lines_per_index=6,
        spine_taper_caps=(6, 6, 4, 4),
        spine_pick_mode="display_ranked",
        scan_limit=scan_limit,
        sort_preset=sort_preset,
    )


def _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_spine_display_canon_ranked(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
    scan_limit: int = 350,
    sort_preset: str = "methods_first",
) -> Dict[str, Any]:
    """
    Within-spine conversion lever (selection-only): keep taper6644 geometry, but choose the spine
    display members using canonical/permutation evidence ranking (a more stable variant of
    display_ranked).
    """
    return _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap(
        ranked=ranked,
        budget=budget,
        spine_max_lines_per_index=6,
        spine_taper_caps=(6, 6, 4, 4),
        spine_pick_mode="display_canon_ranked",
        scan_limit=scan_limit,
        sort_preset=sort_preset,
    )


def _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_sort_packs_first(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
    scan_limit: int = 350,
) -> Dict[str, Any]:
    """
    Index-chooser lever (selection-only): keep taper6644 allocation geometry and display-only spine
    membership, but choose ranked indices using `sort_preset="packs_first"`.
    """
    return _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap(
        ranked=ranked,
        budget=budget,
        spine_max_lines_per_index=6,
        spine_taper_caps=(6, 6, 4, 4),
        spine_pick_mode="display",
        scan_limit=scan_limit,
        sort_preset="packs_first",
    )


def _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_sort_score_total_first(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
    scan_limit: int = 350,
) -> Dict[str, Any]:
    """
    Index-chooser lever (selection-only): keep taper6644 allocation geometry and display-only spine
    membership, but choose ranked indices using `sort_preset="score_total_first"`.
    """
    return _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap(
        ranked=ranked,
        budget=budget,
        spine_max_lines_per_index=6,
        spine_taper_caps=(6, 6, 4, 4),
        spine_pick_mode="display",
        scan_limit=scan_limit,
        sort_preset="score_total_first",
    )


def _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
    scan_limit: int = 350,
) -> Dict[str, Any]:
    """
    Index-chooser lever (selection-only): keep taper6644 allocation geometry and display-only spine membership,
    but choose the top-4 spine indices by `methods_first` ordering and the remaining tail indices by
    `score_total_first` ordering.
    """
    return _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap(
        ranked=ranked,
        budget=budget,
        spine_max_lines_per_index=6,
        spine_taper_caps=(6, 6, 4, 4),
        spine_pick_mode="display",
        scan_limit=scan_limit,
        sort_preset="score_total_first",
        spine_sort_preset="methods_first",
        tail_sort_preset="score_total_first",
    )


def _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_spine_display_canon_ranked(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
    scan_limit: int = 350,
) -> Dict[str, Any]:
    """
    Within-spine conversion lever (selection-only): keep the promoted split chooser index ordering
    and taper6644 geometry, but choose spine display members using canonical/permutation evidence
    ranking (instead of fixed display order).
    """
    return _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap(
        ranked=ranked,
        budget=budget,
        spine_max_lines_per_index=6,
        spine_taper_caps=(6, 6, 4, 4),
        spine_pick_mode="display_canon_ranked",
        scan_limit=scan_limit,
        sort_preset="score_total_first",
        spine_sort_preset="methods_first",
        tail_sort_preset="score_total_first",
    )


def _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6643_split_spine_methods_tail_score_total_first(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
    scan_limit: int = 350,
) -> Dict[str, Any]:
    """
    Allocation-level lever (selection-only): keep the promoted split chooser semantics
    (spine by `methods_first`, tail by `score_total_first`), but taper the 4 spine indices as
    6643 (6/6/4/3) to free 1 additional tail line under B36.
    """
    return _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap(
        ranked=ranked,
        budget=budget,
        spine_max_lines_per_index=6,
        spine_taper_caps=(6, 6, 4, 3),
        spine_pick_mode="display",
        scan_limit=scan_limit,
        sort_preset="score_total_first",
        spine_sort_preset="methods_first",
        tail_sort_preset="score_total_first",
    )


def _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_packs_tail_score_total_first(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
    scan_limit: int = 350,
) -> Dict[str, Any]:
    """
    Index-chooser lever (selection-only): keep taper6644 allocation geometry and display-only spine
    membership, but choose the top-4 spine indices by `packs_first` ordering and the remaining tail
    indices by `score_total_first` ordering.
    """
    return _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap(
        ranked=ranked,
        budget=budget,
        spine_max_lines_per_index=6,
        spine_taper_caps=(6, 6, 4, 4),
        spine_pick_mode="display",
        scan_limit=scan_limit,
        sort_preset="score_total_first",
        spine_sort_preset="packs_first",
        tail_sort_preset="score_total_first",
    )


def _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_packs_first(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
    scan_limit: int = 350,
) -> Dict[str, Any]:
    """
    Index-chooser lever (selection-only): keep taper6644 allocation geometry and display-only spine
    membership, choose the top-4 spine indices by `methods_first`, but choose the remaining tail
    indices by `packs_first` ordering.
    """
    return _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap(
        ranked=ranked,
        budget=budget,
        spine_max_lines_per_index=6,
        spine_taper_caps=(6, 6, 4, 4),
        spine_pick_mode="display",
        scan_limit=scan_limit,
        sort_preset="score_total_first",
        spine_sort_preset="methods_first",
        tail_sort_preset="packs_first",
    )


def _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_rrmix_methods_packs_score_total(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
    scan_limit: int = 350,
) -> Dict[str, Any]:
    """
    Index-chooser lever (selection-only): keep taper6644 allocation geometry and display-only spine
    membership, but choose ranked indices by a deterministic round-robin mix of multiple lenses
    (methods_first / packs_first / score_total_first).

    Goal: materially change the touched index set (reduce CU_LANE_BUT_PLAY_MISS) without altering
    analyzers, CU posture, or within-lane selection.
    """
    b = int(budget)
    if b <= 12:
        return _card_from_ranked(ranked=ranked, budget=b)
    if b < 36:
        return _card_v0_2_default_multi_pack_packheavy(ranked=ranked, budget=b)

    spine_packs_target = 4
    rank_count = 35  # max known display indices is ~35; safe ceiling
    indices_ranked, chooser_ranked = _choose_top_vtrac_indices_round_robin_mix(
        ranked=ranked,
        count=rank_count,
        scan_limit=int(scan_limit),
        allowed_methods=None,
        snapshot_top_k=12,
    )
    if not indices_ranked:
        return _card_v0_2_default_multi_pack_packheavy_lane_diverse_filler(ranked=ranked, budget=b)

    chooser_override = dict(chooser_ranked)
    chooser_override["spine_packs_target"] = int(spine_packs_target)
    chooser_override["rank_count"] = int(rank_count)
    chooser_override["spine_chosen_indices"] = [int(x) for x in indices_ranked[: int(spine_packs_target)]]
    chooser_override["chosen_indices"] = [int(x) for x in indices_ranked[: int(rank_count)]]

    return _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap(
        ranked=ranked,
        budget=b,
        spine_max_lines_per_index=6,
        spine_taper_caps=(6, 6, 4, 4),
        spine_pick_mode="display",
        scan_limit=int(scan_limit),
        sort_preset="score_total_first",
        indices_ranked_override=indices_ranked,
        chooser_ranked_override=chooser_override,
    )


def _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_rrmix_methods_packs_score_total(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
    scan_limit: int = 350,
) -> Dict[str, Any]:
    """
    Tail-only index ordering lever (selection-only):
    - Freeze the top-4 spine indices to `methods_first` (same as the promoted split chooser).
    - Re-rank only the tail indices using the deterministic round-robin mix chooser
      (methods_first / packs_first / score_total_first).

    Goal: improve shoulder lane retention without destabilizing strict conversion via spine churn.
    """
    b = int(budget)
    if b <= 12:
        return _card_from_ranked(ranked=ranked, budget=b)
    if b < 36:
        return _card_v0_2_default_multi_pack_packheavy_lane_diverse_filler(ranked=ranked, budget=b)

    spine_packs_target = 4
    rank_count = 35  # max known display indices is ~35; safe ceiling

    spine_ranked, spine_snapshot = _choose_top_vtrac_indices_full(
        ranked=ranked,
        count=rank_count,
        scan_limit=int(scan_limit),
        allowed_methods=None,
        sort_preset="methods_first",
    )
    tail_ranked, tail_snapshot = _choose_top_vtrac_indices_round_robin_mix(
        ranked=ranked,
        count=rank_count,
        scan_limit=int(scan_limit),
        allowed_methods=None,
        snapshot_top_k=12,
    )
    if not spine_ranked or not tail_ranked:
        return _card_v0_2_default_multi_pack_packheavy_lane_diverse_filler(ranked=ranked, budget=b)

    spine_indices: List[int] = []
    for raw in spine_ranked:
        idx = int(raw)
        if idx not in spine_indices:
            spine_indices.append(idx)
        if len(spine_indices) >= int(spine_packs_target):
            break

    used = set(spine_indices)
    merged: List[int] = list(spine_indices)
    for raw in tail_ranked:
        idx = int(raw)
        if idx in used:
            continue
        merged.append(idx)
        used.add(idx)
        if len(merged) >= int(rank_count):
            break

    if len(merged) < int(rank_count):
        for raw in spine_ranked:
            idx = int(raw)
            if idx in used:
                continue
            merged.append(idx)
            used.add(idx)
            if len(merged) >= int(rank_count):
                break

    chooser_override: Dict[str, Any] = {
        "scan_limit": int(scan_limit),
        "sort_preset": "split_spine_methods_first__tail_round_robin_mix_methods_packs_score_total",
        "spine_sort_preset": "methods_first",
        "tail_sort_preset": "round_robin_mix_methods_packs_score_total",
        "spine_packs_target": int(spine_packs_target),
        "rank_count": int(rank_count),
        "spine_chosen_indices": list(spine_indices),
        "topN_spine": spine_snapshot.get("topN") if isinstance(spine_snapshot, dict) else [],
        "mix": (tail_snapshot.get("mix") if isinstance(tail_snapshot, dict) else {}) or {},
        "chosen_indices": [int(x) for x in merged[: int(rank_count)]],
        "candidates_found": int(
            max(
                int(spine_snapshot.get("candidates_found") or 0) if isinstance(spine_snapshot, dict) else 0,
                int(tail_snapshot.get("candidates_found") or 0) if isinstance(tail_snapshot, dict) else 0,
            )
        ),
    }

    return _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap(
        ranked=ranked,
        budget=b,
        spine_max_lines_per_index=6,
        spine_taper_caps=(6, 6, 4, 4),
        spine_pick_mode="display",
        scan_limit=int(scan_limit),
        sort_preset="score_total_first",
        spine_sort_preset="methods_first",
        tail_sort_preset="round_robin_mix_methods_packs_score_total",
        indices_ranked_override=merged,
        chooser_ranked_override=chooser_override,
    )


def _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_constraint_spine_methods2_or_var1_sort_score_total_first(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
    scan_limit: int = 350,
) -> Dict[str, Any]:
    """
    Index-chooser lever (selection-only): keep taper6644 allocation geometry and display-only spine membership,
    but constrain the top-4 spine indices to "corroborated" lanes:
      - `methods_count >= 2` OR `variants_non_unknown >= 1`

    Tail ordering remains `score_total_first`.
    """
    spine_packs_target = 4
    rank_count = 35  # max known display indices is ~35; safe ceiling
    indices_ranked, chooser_ranked = _choose_top_vtrac_indices_full(
        ranked=ranked,
        count=rank_count,
        scan_limit=int(scan_limit),
        allowed_methods=None,
        sort_preset="score_total_first",
    )
    if not indices_ranked:
        return _card_v0_2_default_multi_pack_packheavy_lane_diverse_filler(ranked=ranked, budget=int(budget))

    top_rows = chooser_ranked.get("topN")
    ranked_rows = top_rows if isinstance(top_rows, list) else []

    constrained_spine: List[int] = []
    seen: set[int] = set()
    for row in ranked_rows:
        if not isinstance(row, dict):
            continue
        raw_idx = row.get("index")
        try:
            idx = int(raw_idx)  # type: ignore[arg-type]
        except Exception:
            continue
        if idx in seen:
            continue
        seen.add(idx)

        methods_count = int(row.get("methods_count") or 0)
        variants_non_unknown = int(row.get("variants_non_unknown") or 0)
        if methods_count >= 2 or variants_non_unknown >= 1:
            constrained_spine.append(idx)
        if len(constrained_spine) >= int(spine_packs_target):
            break

    # Fallback: if corroboration is too sparse, fill remaining spine slots from the unconstrained ranking.
    for idx in indices_ranked:
        if len(constrained_spine) >= int(spine_packs_target):
            break
        if idx in constrained_spine:
            continue
        constrained_spine.append(int(idx))

    used = set(constrained_spine[: int(spine_packs_target)])
    tail_only = [int(idx) for idx in indices_ranked if int(idx) not in used]
    indices_ranked_constrained = list(constrained_spine[: int(spine_packs_target)]) + tail_only

    chooser_override = dict(chooser_ranked)
    chooser_override["sort_preset"] = "score_total_first__constraint_spine_methods2_or_var1"
    chooser_override["spine_constraint"] = "methods_count>=2 OR variants_non_unknown>=1"
    chooser_override["spine_unconstrained_top4"] = [int(x) for x in indices_ranked[: int(spine_packs_target)]]
    chooser_override["spine_chosen_indices"] = list(indices_ranked_constrained[: int(spine_packs_target)])
    chooser_override["chosen_indices"] = list(indices_ranked_constrained[: int(rank_count)])

    return _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap(
        ranked=ranked,
        budget=budget,
        spine_max_lines_per_index=6,
        spine_taper_caps=(6, 6, 4, 4),
        spine_pick_mode="display",
        scan_limit=scan_limit,
        sort_preset="score_total_first",
        indices_ranked_override=indices_ranked_constrained,
        chooser_ranked_override=chooser_override,
    )


def _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_sort_score_total_first_tail_score_first(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
    scan_limit: int = 350,
) -> Dict[str, Any]:
    """
    Tail representative quality lever (selection-only): keep taper6644 allocation geometry and
    `score_total_first` index ordering, but choose the *tail* 1-line/index representative by
    highest score first (instead of pure convergence counts).
    """
    return _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap(
        ranked=ranked,
        budget=budget,
        spine_max_lines_per_index=6,
        spine_taper_caps=(6, 6, 4, 4),
        spine_pick_mode="display",
        tail_pick_mode="score_first",
        scan_limit=scan_limit,
        sort_preset="score_total_first",
    )


def _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6633(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
    scan_limit: int = 350,
    sort_preset: str = "methods_first",
) -> Dict[str, Any]:
    """
    Allocation-level lever (selection-only): keep `spinecap6` semantics, but taper the 4 spine
    indices as:
      - rank 1: 6 lines
      - rank 2: 6 lines
      - rank 3: 3 lines
      - rank 4: 3 lines

    Frees 2 additional lines to extend tail breadth under the same B36 budget.
    """
    return _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap(
        ranked=ranked,
        budget=budget,
        spine_max_lines_per_index=6,
        spine_taper_caps=(6, 6, 3, 3),
        spine_pick_mode="display",
        scan_limit=scan_limit,
        sort_preset=sort_preset,
    )


def _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6643(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
    scan_limit: int = 350,
    sort_preset: str = "methods_first",
) -> Dict[str, Any]:
    """
    Allocation-level lever (selection-only): keep `spinecap6` semantics, but taper the 4 spine
    indices as:
      - rank 1: 6 lines
      - rank 2: 6 lines
      - rank 3: 4 lines
      - rank 4: 3 lines

    Frees 1 additional line to extend tail breadth under the same B36 budget.
    """
    return _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap(
        ranked=ranked,
        budget=budget,
        spine_max_lines_per_index=6,
        spine_taper_caps=(6, 6, 4, 3),
        spine_pick_mode="display",
        scan_limit=scan_limit,
        sort_preset=sort_preset,
    )


def _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_hybrid_d4_e2(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
    scan_limit: int = 350,
    sort_preset: str = "methods_first",
) -> Dict[str, Any]:
    return _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap(
        ranked=ranked,
        budget=budget,
        spine_max_lines_per_index=6,
        spine_pick_mode="hybrid_d4_e2",
        scan_limit=scan_limit,
        sort_preset=sort_preset,
    )


def _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_shoulder_depth(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
    scan_limit: int = 350,
    sort_preset: str = "methods_first",
) -> Dict[str, Any]:
    """
    Shoulder-depth conversion (selection-only):
    - Keep the deep packheavy spine (full boxed-member packs) for the top 4 ranked indices.
    - Reallocate tail budget with depth on the next-ranked "shoulder" indices:
        - ranks 5–8: 2 canonical-diverse lines per index (when possible)
        - ranks 9–16: 1 line per index (when possible)
      Any shortage is absorbed by dropping the lowest tail ranks first.

    Goal: lift within-lane conversion (pack_box_hit / strict hits) without collapsing the lane
    retention gains from the spine+tail geometry.
    """
    import modules.vtrac_reference as vr

    b = int(budget)
    if b <= 12:
        return _card_from_ranked(ranked=ranked, budget=b)
    if b < 36:
        return _card_v0_2_default_multi_pack_packheavy_lane_diverse_filler(ranked=ranked, budget=b)

    spine_packs_target = 4
    rank_count = 35  # max known display indices is ~35; safe ceiling
    indices_ranked, chooser_ranked = _choose_top_vtrac_indices_full(
        ranked=ranked,
        count=rank_count,
        scan_limit=int(scan_limit),
        allowed_methods=None,
        sort_preset=sort_preset,
    )
    if not indices_ranked:
        return _card_v0_2_default_multi_pack_packheavy_lane_diverse_filler(ranked=ranked, budget=b)

    ranked_conv = sorted(list(ranked), key=_convergence_sort_key)
    lane_rows: Dict[int, List[Dict[str, Any]]] = {}
    for row in ranked_conv:
        if not isinstance(row, dict):
            continue
        combo = _normalize_pick3_literal(row.get("combo") or "")
        if not combo:
            continue
        idx = vr.get_vtrac_index(combo)
        if not isinstance(idx, int):
            continue
        lane_rows.setdefault(int(idx), []).append(row)

    selected: List[str] = []
    selected_set: set[str] = set()
    pack_combos: List[str] = []
    pack_combos_by_index: Dict[int, List[str]] = {}
    canons_by_index: Dict[int, set[str]] = {}

    def _add_pack(idx: int, combo: str) -> bool:
        c = _normalize_pick3_literal(combo)
        if not c or c in selected_set:
            return False
        if len(selected) >= b:
            return False
        selected.append(c)
        selected_set.add(c)
        pack_combos.append(c)
        pack_combos_by_index.setdefault(int(idx), []).append(c)
        canon = _canon(c)
        if canon:
            canons_by_index.setdefault(int(idx), set()).add(canon)
        return True

    def _pick_canon_diverse(*, idx: int, want: int, avoid_canons: set[str]) -> List[str]:
        """
        Pick up to `want` combos within `idx`, preferring CU lane rows (best evidence), and
        maintaining canonical diversity against `avoid_canons`.
        """
        chosen: List[str] = []
        chosen_canons: set[str] = set(avoid_canons or set())

        for row in lane_rows.get(int(idx), []):
            if len(chosen) >= want:
                break
            c = _normalize_pick3_literal(row.get("combo") or "")
            if not c or c in selected_set:
                continue
            canon = _canon(c)
            if canon and canon in chosen_canons:
                continue
            chosen.append(c)
            if canon:
                chosen_canons.add(canon)

        if len(chosen) < want:
            for token in _vtrac_display_pack(index=int(idx)):
                if len(chosen) >= want:
                    break
                c = _normalize_pick3_literal(token)
                if not c or c in selected_set or c in chosen:
                    continue
                canon = _canon(c)
                if canon and canon in chosen_canons:
                    continue
                chosen.append(c)
                if canon:
                    chosen_canons.add(canon)

        return chosen

    spine_used: set[int] = set()

    # Spine: insert full boxed-member packs for the top-N ranked indices.
    for raw in indices_ranked[:spine_packs_target]:
        idx = int(raw)
        if idx in spine_used:
            continue
        for token in _vtrac_display_pack(index=idx):
            if len(selected) >= b:
                break
            _add_pack(idx, token)
        spine_used.add(idx)
        if len(selected) >= b:
            break

    # Tail: shoulder depth.
    tail_ranked: List[int] = []
    for raw in indices_ranked[spine_packs_target:]:
        idx = int(raw)
        if idx in spine_used:
            continue
        tail_ranked.append(idx)

    shoulder_count = 4  # ranks 5–8
    mid_count = 8  # ranks 9–16
    shoulder = tail_ranked[:shoulder_count]
    mid = tail_ranked[shoulder_count : shoulder_count + mid_count]
    rest = tail_ranked[shoulder_count + mid_count :]

    tail_touched: set[int] = set()
    shoulder_first_lines = 0
    shoulder_second_lines = 0
    mid_lines = 0
    rest_lines = 0

    # Pass 1: ensure we touch shoulder indices at least once when possible.
    for idx in shoulder:
        if len(selected) >= b:
            break
        picks = _pick_canon_diverse(idx=idx, want=1, avoid_canons=set())
        for c in picks:
            if _add_pack(idx, c):
                tail_touched.add(int(idx))
                shoulder_first_lines += 1

    # Pass 2: allocate a second canonical-diverse line to shoulder indices (when possible).
    for idx in shoulder:
        if len(selected) >= b:
            break
        picks = _pick_canon_diverse(idx=idx, want=1, avoid_canons=canons_by_index.get(int(idx), set()))
        for c in picks:
            if _add_pack(idx, c):
                tail_touched.add(int(idx))
                shoulder_second_lines += 1

    # Pass 3: allocate 1 line for mid tail indices (ranks 9–16).
    for idx in mid:
        if len(selected) >= b:
            break
        picks = _pick_canon_diverse(idx=idx, want=1, avoid_canons=set())
        for c in picks:
            if _add_pack(idx, c):
                tail_touched.add(int(idx))
                mid_lines += 1

    # Pass 4: if budget remains, continue touching ranked indices (baseline-style) 1-per-index.
    for idx in rest:
        if len(selected) >= b:
            break
        picks = _pick_canon_diverse(idx=idx, want=1, avoid_canons=set())
        for c in picks:
            if _add_pack(idx, c):
                tail_touched.add(int(idx))
                rest_lines += 1

    # Safety top-up: if we couldn't fill due to duplicates/empty packs, fill remaining from convergence.
    for row in ranked_conv:
        if len(selected) >= b:
            break
        combo = _normalize_pick3_literal(row.get("combo") or "")
        if not combo or combo in selected_set:
            continue
        selected.append(combo)
        selected_set.add(combo)

    selected = selected[:b]
    boxed = _boxed_canonicals(selected)
    used_indices_list = list(pack_combos_by_index.keys())
    return {
        "budget": int(b),
        "combos": selected,
        "combos_count": len(selected),
        "cost_units": len(selected),
        "boxed_canonicals": boxed,
        "boxed_canonicals_count": len(boxed),
        "vtrac_pack": {
            "index": int(used_indices_list[0]) if used_indices_list else None,
            "indices": list(used_indices_list),
            "packs_target": int(spine_packs_target),
            "pack_combos": list(pack_combos),
            "pack_combos_by_index": {int(k): list(v) for k, v in pack_combos_by_index.items()},
            "chooser": {
                "ranked_indices": chooser_ranked,
                "spine_packs_target": int(spine_packs_target),
                "rank_count": int(rank_count),
                "shoulder_count": int(shoulder_count),
                "mid_count": int(mid_count),
            },
            "filler_policy": "spine4_index_tail_shoulder_depth",
            "allocation": {
                "scan_limit": int(scan_limit),
                "sort_preset": str(sort_preset),
                "spine_packs_target": int(spine_packs_target),
                "tail_touched_indices": int(len(tail_touched)),
                "shoulder_first_lines": int(shoulder_first_lines),
                "shoulder_second_lines": int(shoulder_second_lines),
                "mid_lines": int(mid_lines),
                "rest_lines": int(rest_lines),
            },
        },
    }


def _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_canon2(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
    scan_limit: int = 350,
    sort_preset: str = "methods_first",
) -> Dict[str, Any]:
    """
    Hybrid conversion (selection-only): preserve the deep packheavy spine (full boxed-member packs),
    but allocate *two canonical-diverse lines per tail index* (when possible).

    Goal: improve within-lane tail conversion (perm/canonical coverage) while still touching
    multiple ranked indices under fixed budget.
    """
    import modules.vtrac_reference as vr

    b = int(budget)
    if b <= 12:
        return _card_from_ranked(ranked=ranked, budget=b)
    if b < 36:
        return _card_v0_2_default_multi_pack_packheavy_lane_diverse_filler(ranked=ranked, budget=b)

    spine_packs_target = 4
    tail_per_index = 2
    rank_count = 35  # max known display indices is ~35; safe ceiling
    indices_ranked, chooser_ranked = _choose_top_vtrac_indices_full(
        ranked=ranked,
        count=rank_count,
        scan_limit=int(scan_limit),
        allowed_methods=None,
        sort_preset=sort_preset,
    )
    if not indices_ranked:
        return _card_v0_2_default_multi_pack_packheavy_lane_diverse_filler(ranked=ranked, budget=b)

    ranked_conv = sorted(list(ranked), key=_convergence_sort_key)
    lane_rows: Dict[int, List[Dict[str, Any]]] = {}
    for row in ranked_conv:
        if not isinstance(row, dict):
            continue
        combo = _normalize_pick3_literal(row.get("combo") or "")
        if not combo:
            continue
        idx = vr.get_vtrac_index(combo)
        if not isinstance(idx, int):
            continue
        lane_rows.setdefault(int(idx), []).append(row)

    selected: List[str] = []
    selected_set: set[str] = set()
    pack_combos: List[str] = []
    pack_combos_by_index: Dict[int, List[str]] = {}

    def _add_pack(idx: int, combo: str) -> bool:
        c = _normalize_pick3_literal(combo)
        if not c or c in selected_set:
            return False
        if len(selected) >= b:
            return False
        selected.append(c)
        selected_set.add(c)
        pack_combos.append(c)
        pack_combos_by_index.setdefault(int(idx), []).append(c)
        return True

    used_indices: set[int] = set()

    # Spine: insert full boxed-member packs for the top-N ranked indices.
    for raw in indices_ranked[:spine_packs_target]:
        idx = int(raw)
        if idx in used_indices:
            continue
        for token in _vtrac_display_pack(index=idx):
            if len(selected) >= b:
                break
            _add_pack(idx, token)
        used_indices.add(idx)
        if len(selected) >= b:
            break

    # Tail: allocate up to `tail_per_index` canonical-diverse lines per ranked index.
    tail_indices_added = 0
    tail_lines_added = 0
    for raw in indices_ranked[spine_packs_target:]:
        if len(selected) >= b:
            break
        idx = int(raw)
        if idx in used_indices:
            continue

        chosen: List[str] = []
        chosen_canons: set[str] = set()

        # Prefer evidence rows, 1-per-canonical (best-evidence permutation per canonical).
        for row in lane_rows.get(idx, []):
            if len(chosen) >= tail_per_index:
                break
            c = _normalize_pick3_literal(row.get("combo") or "")
            if not c or c in selected_set:
                continue
            canon = _canon(c)
            if canon and canon in chosen_canons:
                continue
            chosen.append(c)
            if canon:
                chosen_canons.add(canon)

        # Fallback: use display pack members, maintaining canonical diversity if possible.
        if len(chosen) < tail_per_index:
            for token in _vtrac_display_pack(index=idx):
                if len(chosen) >= tail_per_index:
                    break
                c = _normalize_pick3_literal(token)
                if not c or c in selected_set or c in chosen:
                    continue
                canon = _canon(c)
                if canon and canon in chosen_canons:
                    continue
                chosen.append(c)
                if canon:
                    chosen_canons.add(canon)

        added_any = False
        for c in chosen:
            if len(selected) >= b:
                break
            if _add_pack(idx, c):
                added_any = True
                tail_lines_added += 1

        if added_any:
            used_indices.add(idx)
            tail_indices_added += 1

    # Safety top-up: if we couldn't fill due to duplicates/empty packs, fill remaining from convergence.
    for row in ranked_conv:
        if len(selected) >= b:
            break
        combo = _normalize_pick3_literal(row.get("combo") or "")
        if not combo or combo in selected_set:
            continue
        selected.append(combo)
        selected_set.add(combo)

    selected = selected[:b]
    boxed = _boxed_canonicals(selected)
    used_indices_list = list(pack_combos_by_index.keys())
    return {
        "budget": int(b),
        "combos": selected,
        "combos_count": len(selected),
        "cost_units": len(selected),
        "boxed_canonicals": boxed,
        "boxed_canonicals_count": len(boxed),
        "vtrac_pack": {
            "index": int(used_indices_list[0]) if used_indices_list else None,
            "indices": list(used_indices_list),
            "packs_target": int(spine_packs_target),
            "pack_combos": list(pack_combos),
            "pack_combos_by_index": {int(k): list(v) for k, v in pack_combos_by_index.items()},
            "chooser": {
                "ranked_indices": chooser_ranked,
                "spine_packs_target": int(spine_packs_target),
                "rank_count": int(rank_count),
            },
            "filler_policy": "spine4_index_tail_canon2",
            "allocation": {
                "scan_limit": int(scan_limit),
                "sort_preset": str(sort_preset),
                "spine_packs_target": int(spine_packs_target),
                "tail_per_index": int(tail_per_index),
                "tail_indices_added": int(tail_indices_added),
                "tail_lines_added": int(tail_lines_added),
            },
        },
    }


def _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_canonvote(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
    scan_limit: int = 350,
    sort_preset: str = "methods_first",
) -> Dict[str, Any]:
    """
    Hybrid conversion (selection-only): same allocation geometry as `spine4_index_tail` (deep spine
    + 1-line tail across many indices), but tail selection is canonical-aware.

    For each tail index, pick the canonical with the *strongest union support* (methods/variants)
    across its CU evidence rows, then select that canonical's best-evidence permutation.

    Goal: improve tail "1-line" quality without collapsing lane retention.
    """
    import modules.vtrac_reference as vr

    b = int(budget)
    if b <= 12:
        return _card_from_ranked(ranked=ranked, budget=b)
    if b < 36:
        return _card_v0_2_default_multi_pack_packheavy_lane_diverse_filler(ranked=ranked, budget=b)

    spine_packs_target = 4
    rank_count = 35  # max known display indices is ~35; safe ceiling
    indices_ranked, chooser_ranked = _choose_top_vtrac_indices_full(
        ranked=ranked,
        count=rank_count,
        scan_limit=int(scan_limit),
        allowed_methods=None,
        sort_preset=sort_preset,
    )
    if not indices_ranked:
        return _card_v0_2_default_multi_pack_packheavy_lane_diverse_filler(ranked=ranked, budget=b)

    ranked_conv = sorted(list(ranked), key=_convergence_sort_key)
    lane_rows: Dict[int, List[Dict[str, Any]]] = {}
    for row in ranked_conv:
        if not isinstance(row, dict):
            continue
        combo = _normalize_pick3_literal(row.get("combo") or "")
        if not combo:
            continue
        idx = vr.get_vtrac_index(combo)
        if not isinstance(idx, int):
            continue
        lane_rows.setdefault(int(idx), []).append(row)

    selected: List[str] = []
    selected_set: set[str] = set()
    pack_combos: List[str] = []
    pack_combos_by_index: Dict[int, List[str]] = {}

    def _add_pack(idx: int, combo: str) -> bool:
        c = _normalize_pick3_literal(combo)
        if not c or c in selected_set:
            return False
        if len(selected) >= b:
            return False
        selected.append(c)
        selected_set.add(c)
        pack_combos.append(c)
        pack_combos_by_index.setdefault(int(idx), []).append(c)
        return True

    used_indices: set[int] = set()

    # Spine: insert full boxed-member packs for the top-N ranked indices.
    for raw in indices_ranked[:spine_packs_target]:
        idx = int(raw)
        if idx in used_indices:
            continue
        for token in _vtrac_display_pack(index=idx):
            if len(selected) >= b:
                break
            _add_pack(idx, token)
        used_indices.add(idx)
        if len(selected) >= b:
            break

    # Tail: touch additional ranked indices, but pick a canonical by "union support" first.
    tail_added = 0
    scan_rows_per_index = 80
    for raw in indices_ranked[spine_packs_target:]:
        if len(selected) >= b:
            break
        idx = int(raw)
        if idx in used_indices:
            continue

        canon_stats: Dict[str, Dict[str, Any]] = {}
        for i, row in enumerate(lane_rows.get(idx, [])[:scan_rows_per_index]):
            combo = _normalize_pick3_literal(row.get("combo") or "")
            if not combo or combo in selected_set:
                continue
            canon = _canon(combo)
            if not canon:
                continue
            st = canon_stats.get(canon)
            if st is None:
                st = {"best_rank": int(i), "best_combo": combo, "methods": set(), "variants": set()}
                canon_stats[canon] = st
            methods = row.get("support_methods")
            if isinstance(methods, list):
                st["methods"].update(str(x) for x in methods if str(x))
            variants = row.get("support_variants")
            if isinstance(variants, list):
                st["variants"].update(str(x) for x in variants if str(x))

        chosen = ""
        if canon_stats:
            # Deterministic: maximize method-union, then variant-union, then best_rank, then canon label.
            best_canon, st = sorted(
                canon_stats.items(),
                key=lambda kv: (
                    -len(kv[1].get("methods") or set()),
                    -len(kv[1].get("variants") or set()),
                    int(kv[1].get("best_rank") or 0),
                    str(kv[0]),
                ),
            )[0]
            _ = best_canon
            chosen = str(st.get("best_combo") or "")

        if not chosen:
            for token in _vtrac_display_pack(index=idx):
                c = _normalize_pick3_literal(token)
                if c and c not in selected_set:
                    chosen = c
                    break
        if not chosen:
            continue

        if _add_pack(idx, chosen):
            used_indices.add(idx)
            tail_added += 1

    # Safety top-up: if we couldn't fill due to duplicates/empty packs, fill remaining from convergence.
    for row in ranked_conv:
        if len(selected) >= b:
            break
        combo = _normalize_pick3_literal(row.get("combo") or "")
        if not combo or combo in selected_set:
            continue
        selected.append(combo)
        selected_set.add(combo)

    selected = selected[:b]
    boxed = _boxed_canonicals(selected)
    used_indices_list = list(pack_combos_by_index.keys())
    return {
        "budget": int(b),
        "combos": selected,
        "combos_count": len(selected),
        "cost_units": len(selected),
        "boxed_canonicals": boxed,
        "boxed_canonicals_count": len(boxed),
        "vtrac_pack": {
            "index": int(used_indices_list[0]) if used_indices_list else None,
            "indices": list(used_indices_list),
            "packs_target": int(spine_packs_target),
            "pack_combos": list(pack_combos),
            "pack_combos_by_index": {int(k): list(v) for k, v in pack_combos_by_index.items()},
            "chooser": {
                "ranked_indices": chooser_ranked,
                "spine_packs_target": int(spine_packs_target),
                "rank_count": int(rank_count),
                "tail_scan_rows_per_index": int(scan_rows_per_index),
            },
            "filler_policy": "spine4_index_tail_canonvote",
            "allocation": {
                "scan_limit": int(scan_limit),
                "sort_preset": str(sort_preset),
                "spine_packs_target": int(spine_packs_target),
                "tail_added": int(tail_added),
                "tail_scan_rows_per_index": int(scan_rows_per_index),
            },
        },
    }

def _card_v0_2_default_multi_pack_packheavy_diverse(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
) -> Dict[str, Any]:
    """
    Conversion experiment (selection-only): B36-only variant that diversifies lane selection.

    Goal: reduce CU_LANE_BUT_PLAY_MISS without touching analyzers by avoiding "single-lens"
    over-commitment when choosing VTRAC indices.
    """
    b = int(budget)
    if b <= 12:
        return _card_from_ranked(ranked=ranked, budget=b)
    if b < 36:
        return _card_v0_2_default_multi_pack_packheavy(ranked=ranked, budget=b)

    packs_target = 4
    indices, chooser = _choose_top_vtrac_indices_diverse(ranked=ranked, count=packs_target)
    return _card_vtrac_packs_boxed_first_from_indices(
        ranked=ranked,
        budget=b,
        packs_target=packs_target,
        indices=indices,
        chooser=chooser,
    )


def _card_v0_2_default_multi_pack_stablepluslane_packheavy(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
) -> Dict[str, Any]:
    """
    Conversion experiment (selection-only): packheavy, but allow stable-family evidence to participate
    in lane choice (stable_top + presetB lane methods).
    """
    b = int(budget)
    if b <= 12:
        return _card_from_ranked(ranked=ranked, budget=b)
    packs_target = 4 if b >= 36 else max(1, min(5, b // 12))
    allowed = set(_lane_methods_for_preset(preset="presetB"))
    allowed.add("stable_top")
    return _card_vtrac_packs_boxed_first(ranked=ranked, budget=b, packs_target=packs_target, allowed_methods=allowed)


def _card_v0_2_default_stable_lane(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
) -> Dict[str, Any]:
    """
    v0.2 posture variant: choose the B24/B36 VTRAC lane using only stable-family evidence.

    Goal: increase `pack_correct` without collapsing overall card diversity (keeps the original
    v0.2 fill behavior after inserting the chosen boxed-member pack).
    """
    b = int(budget)
    if b <= 12:
        return _card_from_ranked(ranked=ranked, budget=b)
    return _card_vtrac_pack_boxed_first(ranked=ranked, budget=b, allowed_methods={"stable_top"})


def _card_v0_2_default_hybrid_box_lane(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
) -> Dict[str, Any]:
    """
    v0.2 posture hybrid:
    - B12: analysis_prefix
    - B24/B36: start from v0.2 pack posture, reserve a few slots to *complete* full BOX closures cheaply,
      then fill remaining with convergence ranking.
    """
    b = int(budget)
    if b <= 12:
        return _card_from_ranked(ranked=ranked, budget=b)

    reserved = 2 if b <= 24 else 3
    base_budget = max(0, int(b) - int(reserved))

    base: Dict[str, Any]
    if b <= 24:
        base = _card_vtrac_pack_boxed_first(ranked=ranked, budget=base_budget)
    else:
        packs_target = max(1, min(5, base_budget // 12))
        base = _card_vtrac_packs_boxed_first(ranked=ranked, budget=base_budget, packs_target=packs_target)

    selected: List[str] = [_normalize_pick3_literal(x) for x in (base.get("combos") or [])]
    selected = [x for x in selected if x]
    selected_set: set[str] = set(selected)
    slots_left = int(b) - len(selected)

    # Identify closures we can complete cheaply (missing few perms) within reserved slots.
    canon_to_combos: Dict[str, set[str]] = {}
    canon_score: Dict[str, float] = {}
    for row in ranked:
        combo = _normalize_pick3_literal(row.get("combo") or "")
        canon = _canon(combo)
        if not canon:
            continue
        canon_to_combos.setdefault(canon, set()).add(combo)
        canon_score[canon] = max(canon_score.get(canon, float("-inf")), float(row.get("score") or 0.0))

    candidates: List[Tuple[int, int, float, str, List[str]]] = []
    for canon, seen_combos in canon_to_combos.items():
        perms = sorted(set(_unique_perms(canon)))
        if not perms or not set(perms).issubset(seen_combos):
            continue
        missing = [p for p in perms if p not in selected_set]
        have_count = len(perms) - len(missing)
        if not missing:
            continue
        candidates.append((len(missing), -have_count, -float(canon_score.get(canon, 0.0)), canon, missing))

    candidates.sort(key=lambda t: (t[0], t[1], t[2], t[3]))
    used_canons: set[str] = set()
    while slots_left > 0:
        picked: Optional[Tuple[int, int, float, str, List[str]]] = None
        for cand in candidates:
            miss_n, _have_neg, _score_neg, canon, missing = cand
            if canon in used_canons:
                continue
            if miss_n <= slots_left:
                picked = cand
                break
        if picked is None:
            break
        miss_n, _have_neg, _score_neg, canon, missing = picked
        for combo in missing:
            if slots_left <= 0:
                break
            c = _normalize_pick3_literal(combo)
            if not c or c in selected_set:
                continue
            selected.append(c)
            selected_set.add(c)
            slots_left -= 1
        used_canons.add(canon)

    # Fill remaining with convergence-ranked candidates.
    ranked_conv = sorted(list(ranked), key=_convergence_sort_key)
    for row in ranked_conv:
        if len(selected) >= int(b):
            break
        combo = _normalize_pick3_literal(row.get("combo") or "")
        if not combo or combo in selected_set:
            continue
        selected.append(combo)
        selected_set.add(combo)

    selected = selected[: int(b)]
    boxed = _boxed_canonicals(selected)

    out = dict(base)
    out["budget"] = int(b)
    out["combos"] = selected
    out["combos_count"] = len(selected)
    out["cost_units"] = len(selected)
    out["boxed_canonicals"] = boxed
    out["boxed_canonicals_count"] = len(boxed)
    return out


def _card_v0_2_default_recency_tiebreak(
    *,
    ranked: Sequence[Dict[str, Any]],
    budget: int,
    state_dir: Path,
    state_key: str,
    tie_preset: str,
) -> Dict[str, Any]:
    """
    v0.2 posture (budget-split) + recency tie-break for B24/B36 lane choice.

    - B12: analysis_prefix
    - B24/B36: vtrac_pack_boxed_first + recency tie-break (default-off experiment)
    """
    b = int(budget)
    if b <= 12:
        return _card_from_ranked(ranked=ranked, budget=b)
    return _card_vtrac_pack_boxed_first_recency_tiebreak(
        ranked=ranked, budget=b, state_dir=state_dir, state_key=state_key, tie_preset=tie_preset
    )

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
            "v0_2_default_multi_pack": {},
            "v0_2_default_multi_pack_laneonly_presetB": {},
            "v0_2_default_multi_pack_laneonly_presetB_packheavy": {},
            "v0_2_default_multi_pack_laneonly_presetB_packheavy_scan2000": {},
            "v0_2_default_multi_pack_laneonly_presetB_packheavy_scorefirst_scan2000": {},
            "v0_2_default_multi_pack_packheavy": {},
            "v0_2_default_multi_pack_packheavy_lane_diverse_filler": {},
            "v0_2_default_multi_pack_packheavy_diverse": {},
            "v0_2_default_multi_pack_mop_24_12": {},
            "v0_2_default_multi_pack_index_alloc_top12_4_3_2": {},
            "v0_2_default_multi_pack_packheavy_spine4_index_tail": {},
            "v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6": {},
            "v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap7": {},
            "v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_evidence": {},
            "v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_display_ranked": {},
            "v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_display_canon_ranked": {},
            "v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644": {},
            "v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_spine_display_ranked": {},
            "v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_spine_display_canon_ranked": {},
            "v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_sort_packs_first": {},
            "v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_sort_score_total_first": {},
            "v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first": {},
            "v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_spine_display_canon_ranked": {},
            "v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6643_split_spine_methods_tail_score_total_first": {},
            "v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_packs_tail_score_total_first": {},
            "v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_packs_first": {},
            "v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_rrmix_methods_packs_score_total": {},
            "v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_rrmix_methods_packs_score_total": {},
            "v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_constraint_spine_methods2_or_var1_sort_score_total_first": {},
            "v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_sort_score_total_first_tail_score_first": {},
            "v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6633": {},
            "v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6643": {},
            "v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_hybrid_d4_e2": {},
            "v0_2_default_multi_pack_packheavy_spine4_index_tail_shoulder_depth": {},
            "v0_2_default_multi_pack_packheavy_spine4_index_tail_canon2": {},
            "v0_2_default_multi_pack_packheavy_spine4_index_tail_canonvote": {},
            "v0_2_default_multi_pack_stablepluslane_packheavy": {},
            "v0_2_default_stable_lane": {},
            "v0_2_default_hybrid_box_lane": {},
            "v0_2_default_recency_lenient": {},
            "v0_2_default_recency_strict": {},
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
            strategy_cards["v0_2_default_multi_pack"][f"B{b}"] = _card_v0_2_default_multi_pack(ranked=ranked, budget=b)
            strategy_cards["v0_2_default_multi_pack_laneonly_presetB"][f"B{b}"] = _card_v0_2_default_multi_pack_laneonly_presetB(
                ranked=ranked, budget=b
            )
            strategy_cards["v0_2_default_multi_pack_laneonly_presetB_packheavy"][f"B{b}"] = (
                _card_v0_2_default_multi_pack_laneonly_presetB_packheavy(ranked=ranked, budget=b)
            )
            strategy_cards["v0_2_default_multi_pack_laneonly_presetB_packheavy_scan2000"][f"B{b}"] = (
                _card_v0_2_default_multi_pack_laneonly_presetB_packheavy_scan2000(ranked=ranked, budget=b)
            )
            strategy_cards["v0_2_default_multi_pack_laneonly_presetB_packheavy_scorefirst_scan2000"][f"B{b}"] = (
                _card_v0_2_default_multi_pack_laneonly_presetB_packheavy_scorefirst_scan2000(ranked=ranked, budget=b)
            )
            strategy_cards["v0_2_default_multi_pack_packheavy"][f"B{b}"] = _card_v0_2_default_multi_pack_packheavy(
                ranked=ranked, budget=b
            )
            strategy_cards["v0_2_default_multi_pack_packheavy_lane_diverse_filler"][f"B{b}"] = _card_v0_2_default_multi_pack_packheavy_lane_diverse_filler(
                ranked=ranked, budget=b
            )
            strategy_cards["v0_2_default_multi_pack_packheavy_diverse"][f"B{b}"] = _card_v0_2_default_multi_pack_packheavy_diverse(
                ranked=ranked, budget=b
            )
            strategy_cards["v0_2_default_multi_pack_mop_24_12"][f"B{b}"] = _card_v0_2_default_multi_pack_mop_24_12(
                ranked=ranked, budget=b
            )
            strategy_cards["v0_2_default_multi_pack_index_alloc_top12_4_3_2"][f"B{b}"] = (
                _card_v0_2_default_multi_pack_index_alloc_top12_4_3_2(ranked=ranked, budget=b)
            )
            strategy_cards["v0_2_default_multi_pack_packheavy_spine4_index_tail"][f"B{b}"] = (
                _card_v0_2_default_multi_pack_packheavy_spine4_index_tail(ranked=ranked, budget=b)
            )
            strategy_cards["v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6"][f"B{b}"] = (
                _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6(ranked=ranked, budget=b)
            )
            strategy_cards["v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap7"][f"B{b}"] = (
                _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap7(ranked=ranked, budget=b)
            )
            strategy_cards["v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_evidence"][f"B{b}"] = (
                _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_evidence(ranked=ranked, budget=b)
            )
            strategy_cards["v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_display_ranked"][f"B{b}"] = (
                _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_display_ranked(
                    ranked=ranked, budget=b
                )
            )
            strategy_cards["v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_display_canon_ranked"][f"B{b}"] = (
                _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_display_canon_ranked(
                    ranked=ranked, budget=b
                )
            )
            strategy_cards["v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644"][f"B{b}"] = (
                _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644(
                    ranked=ranked, budget=b
                )
            )
            strategy_cards["v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_spine_display_ranked"][f"B{b}"] = (
                _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_spine_display_ranked(
                    ranked=ranked, budget=b
                )
            )
            strategy_cards["v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_spine_display_canon_ranked"][f"B{b}"] = (
                _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_spine_display_canon_ranked(
                    ranked=ranked, budget=b
                )
            )
            strategy_cards["v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_sort_packs_first"][f"B{b}"] = (
                _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_sort_packs_first(
                    ranked=ranked, budget=b
                )
            )
            strategy_cards["v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_sort_score_total_first"][f"B{b}"] = (
                _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_sort_score_total_first(
                    ranked=ranked, budget=b
                )
            )
            strategy_cards[
                "v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first"
            ][f"B{b}"] = (
                _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first(
                    ranked=ranked, budget=b
                )
            )
            strategy_cards[
                "v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_spine_display_canon_ranked"
            ][f"B{b}"] = (
                _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_spine_display_canon_ranked(
                    ranked=ranked, budget=b
                )
            )
            strategy_cards[
                "v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6643_split_spine_methods_tail_score_total_first"
            ][f"B{b}"] = (
                _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6643_split_spine_methods_tail_score_total_first(
                    ranked=ranked, budget=b
                )
            )
            strategy_cards[
                "v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_packs_tail_score_total_first"
            ][f"B{b}"] = (
                _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_packs_tail_score_total_first(
                    ranked=ranked, budget=b
                )
            )
            strategy_cards[
                "v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_packs_first"
            ][f"B{b}"] = (
                _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_packs_first(
                    ranked=ranked, budget=b
                )
            )
            strategy_cards[
                "v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_rrmix_methods_packs_score_total"
            ][f"B{b}"] = (
                _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_rrmix_methods_packs_score_total(
                    ranked=ranked, budget=b
                )
            )
            strategy_cards[
                "v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_rrmix_methods_packs_score_total"
            ][f"B{b}"] = (
                _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_rrmix_methods_packs_score_total(
                    ranked=ranked, budget=b
                )
            )
            strategy_cards[
                "v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_constraint_spine_methods2_or_var1_sort_score_total_first"
            ][f"B{b}"] = (
                _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_constraint_spine_methods2_or_var1_sort_score_total_first(
                    ranked=ranked, budget=b
                )
            )
            strategy_cards["v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_sort_score_total_first_tail_score_first"][f"B{b}"] = (
                _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_sort_score_total_first_tail_score_first(
                    ranked=ranked, budget=b
                )
            )
            strategy_cards["v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6633"][f"B{b}"] = (
                _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6633(
                    ranked=ranked, budget=b
                )
            )
            strategy_cards["v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6643"][f"B{b}"] = (
                _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6643(
                    ranked=ranked, budget=b
                )
            )
            strategy_cards["v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_hybrid_d4_e2"][f"B{b}"] = (
                _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_hybrid_d4_e2(
                    ranked=ranked, budget=b
                )
            )
            strategy_cards["v0_2_default_multi_pack_packheavy_spine4_index_tail_shoulder_depth"][f"B{b}"] = (
                _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_shoulder_depth(ranked=ranked, budget=b)
            )
            strategy_cards["v0_2_default_multi_pack_packheavy_spine4_index_tail_canon2"][f"B{b}"] = (
                _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_canon2(ranked=ranked, budget=b)
            )
            strategy_cards["v0_2_default_multi_pack_packheavy_spine4_index_tail_canonvote"][f"B{b}"] = (
                _card_v0_2_default_multi_pack_packheavy_spine4_index_tail_canonvote(ranked=ranked, budget=b)
            )
            strategy_cards["v0_2_default_multi_pack_stablepluslane_packheavy"][f"B{b}"] = (
                _card_v0_2_default_multi_pack_stablepluslane_packheavy(ranked=ranked, budget=b)
            )
            strategy_cards["v0_2_default_stable_lane"][f"B{b}"] = _card_v0_2_default_stable_lane(ranked=ranked, budget=b)
            strategy_cards["v0_2_default_hybrid_box_lane"][f"B{b}"] = _card_v0_2_default_hybrid_box_lane(
                ranked=ranked, budget=b
            )
            strategy_cards["v0_2_default_recency_lenient"][f"B{b}"] = _card_v0_2_default_recency_tiebreak(
                ranked=ranked, budget=b, state_dir=state_dir, state_key=state_key, tie_preset="lenient"
            )
            strategy_cards["v0_2_default_recency_strict"][f"B{b}"] = _card_v0_2_default_recency_tiebreak(
                ranked=ranked, budget=b, state_dir=state_dir, state_key=state_key, tie_preset="strict"
            )
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
