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
- Reads ONLY: `sharepacks/<root>/<D>/<STATE>/candidate_universe.json`
- Writes ONLY (predictive-safe): `sharepacks/<root>/<D>/<STATE>/play_card.json`

Notes
-----
- Budget units are "combo lines" (length of the final combos list).
- Two built-in strategy variants:
  - play_box_first: prefers full canonical closures (all perms) when available.
  - analysis_prefix: strict prefix cut of the ranked combo list (for comparability).
  - convergence_box_first: prefers full canonical closures, but ranks candidates by
    cross-method + cross-variant convergence (support-count first).
"""

from __future__ import annotations

import argparse
import json
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
    if m == "due_doubles":
        return 85.0
    if m in {"due_doubles_mirror_single", "due_doubles_mirror_double"}:
        return 70.0
    if m == "consensus_double_9":
        return 60.0
    if m == "stable_top":
        return 55.0
    if m == "aux_positional":
        return 45.0
    if m == "digit_reduction_analyzer_v2":
        return 40.0
    if m in {"vtrac_enhanced_top", "vtrac_top"}:
        return 35.0
    if m == "hot_zones_top":
        return 30.0
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


def _convergence_stats(row: Dict[str, Any]) -> Tuple[int, int, int, int, float]:
    """
    Convergence priority for discovery mode (support-count based).

    Returns: (methods_count, variants_non_unknown_count, variants_total_count, pack_refs_count, base_score)
    """
    methods = row.get("support_methods") or []
    if not isinstance(methods, list):
        methods = []
    methods_count = len({str(m) for m in methods})

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

    for state_key in states:
        state_dir = day_dir / state_key
        cu_path = state_dir / "candidate_universe.json"
        if not cu_path.exists():
            raise SystemExit(f"Missing candidate universe: {_safe_rel(cu_path)}")

        out_path = state_dir / "play_card.json"
        if out_path.exists() and not args.force:
            raise SystemExit(f"Refusing to overwrite existing play card (use --force): {_safe_rel(out_path)}")

        md_path = state_dir / "play_card.md"
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
            "convergence_box_first": {},
        }
        for b in budgets:
            strategy_cards["play_box_first"][f"B{b}"] = _card_box_first(ranked=ranked, budget=b)
            strategy_cards["analysis_prefix"][f"B{b}"] = _card_from_ranked(ranked=ranked, budget=b)
            strategy_cards["convergence_box_first"][f"B{b}"] = _card_convergence_box_first(ranked=ranked, budget=b)

        payload = {
            "schema_version": SCHEMA_VERSION,
            "generated_at": _now_iso(),
            "results_date": args.date,
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
