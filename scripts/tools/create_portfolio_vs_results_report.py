#!/usr/bin/env python3
"""
Create a windowed "Portfolio vs Results" report for predictive sharepacks.

What this solves (plain English)
--------------------------------
You want a broad-first scoreboard so you can stop manually eyeballing portfolios:
- For each day/state: what are the Play Cards (B12/B24/B36)?
- Do they hit the posted Midday/Evening results?
- If they miss: how close were they (VTRAC lane hit, digit coverage, 2-of-3 overlaps, etc.)?

This is analysis-only:
- Reads ONLY existing artifacts:
  - sharepacks/<root>/<D>/<STATE>/candidate_universe*.json
  - sharepacks/<root>/<D>/<STATE>/play_card*.json
  - data/results/<D>.txt
- Writes ONLY into docs/AAT9_KIT/FINAL VALIDATION/RUNS
  (never into predictive sharepacks).

Hit definitions (the 4 core surfaces)
-------------------------------------
- straight_hit:
    Exact winner combo appears in the list.
- boxed_any_perm_hit:
    Winner canonical appears as *any* permutation in the list.
    (Example: winner 942 → canon 249; list contains 294 → boxed_any_perm_hit=1.)
- boxed_full_hit:
    All unique permutations of the winner canonical appear in the list.
    (This is the strict "we effectively played the full box via explicit lines" lens.)
- vtrac_index_hit:
    At least one listed combo is in the same boxed-family VTRAC index as the winner.
    This is "lane/neighborhood" isolation, not digit containment.

Extra closeness signals (advanced)
----------------------------------
- digit_cover_all_unique:
    The union of digits across the list covers all unique winner digits
    (e.g., list has ...044 and ...677, winner is 647 → digit_cover_all_unique=1).
- best_overlap:
    Best multiset digit-overlap between any listed combo and the winner (0..3).
    Doubles matter (e.g., overlap(377,737)=3).
- in_winner_index:
    How many listed combos fall inside the winner's VTRAC index.

Usage
-----
python3 scripts/tools/create_portfolio_vs_results_report.py \\
  --start-date 2026-01-01 --end-date 2026-01-09 \\
  --sharepacks-root sharepacks/_predictive --profile tool_only
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))


def _runs_dir() -> Path:
    return REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"


def _safe_rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _read_json(path: Path) -> object:
    return json.loads(_read_text(path))


def _profile_suffix(profile: str) -> str:
    p = (profile or "mixed").strip()
    return "" if p == "mixed" else f"__{p}"


def _normalize_experiment_tag(value: str) -> str:
    raw = str(value or "").strip()
    if not raw:
        return ""
    raw = raw.replace(" ", "_")
    cleaned = re.sub(r"[^A-Za-z0-9_-]+", "", raw).strip("_-")
    if not cleaned:
        raise SystemExit(f"Invalid experiment tag: {value!r} (must contain A-Z/a-z/0-9/_/-)")
    return cleaned[:60]


def _normalize_pick3(value: str) -> str:
    digits = "".join(ch for ch in str(value) if ch.isdigit())
    if not digits:
        return ""
    digits = digits.zfill(3) if len(digits) <= 3 else digits
    return digits if len(digits) == 3 else ""


def _canon(value: str) -> str:
    v = _normalize_pick3(value)
    return "".join(sorted(v)) if v else ""


def _unique_perms(triad: str) -> set[str]:
    from itertools import permutations

    triad = _normalize_pick3(triad)
    if not triad:
        return set()
    return {"".join(p) for p in permutations(triad, 3)}


def _boxed_canonicals(combos: Sequence[str]) -> set[str]:
    by_canon: Dict[str, set[str]] = {}
    for c in combos:
        c = _normalize_pick3(c)
        if not c:
            continue
        by_canon.setdefault(_canon(c), set()).add(c)
    boxed: set[str] = set()
    for canon, members in by_canon.items():
        perms = _unique_perms(canon)
        if perms and perms.issubset(members):
            boxed.add(canon)
    return boxed


def _winner_vtrac_index(winner: str) -> Optional[int]:
    import modules.vtrac_reference as vr

    w = _normalize_pick3(winner)
    if not w:
        return None
    idx = vr.get_vtrac_index(w)
    return idx if isinstance(idx, int) else None


def _combo_vtrac_index(combo: str) -> Optional[int]:
    import modules.vtrac_reference as vr

    c = _normalize_pick3(combo)
    if not c:
        return None
    idx = vr.get_vtrac_index(c)
    return idx if isinstance(idx, int) else None


def _digits_unique(value: str) -> set[str]:
    v = _normalize_pick3(value)
    return set(v) if v else set()


def _multiset_digit_overlap(a: str, b: str) -> int:
    aa = _normalize_pick3(a)
    bb = _normalize_pick3(b)
    if not aa or not bb:
        return 0
    ca = Counter(aa)
    cb = Counter(bb)
    return sum(min(ca[d], cb[d]) for d in set(ca) | set(cb))


def _is_double_like(value: str) -> bool:
    v = _normalize_pick3(value)
    return bool(v) and len(set(v)) <= 2


@dataclass(frozen=True)
class Winner:
    midday: Optional[str]
    evening: Optional[str]


def _load_results_winners(results_file: Path) -> Dict[str, Winner]:
    """
    Parse data/results/<D>.txt into {StateKey: Winner(midday, evening)}.
    Uses the project's canonical mapping to StateKey(s) for each row.
    """
    if not results_file.exists():
        return {}
    from alpha_analytical.control_center.batch_runner import (  # type: ignore
        parse_winner_sheet,
        _PROJECT_STATE_CANDIDATES,
    )

    entries = parse_winner_sheet(_read_text(results_file))
    winners: Dict[str, Winner] = {}
    for entry in entries:
        canonical = getattr(entry, "canonical", None)
        midday = getattr(entry, "midday", None)
        evening = getattr(entry, "evening", None)
        if not canonical:
            continue
        candidates = _PROJECT_STATE_CANDIDATES.get(canonical)
        if not candidates:
            project_state = getattr(entry, "project_state", None)
            candidates = (project_state,) if project_state else ()
        for state_key in candidates:
            if not state_key:
                continue
            winners[state_key] = Winner(
                midday=_normalize_pick3(midday or ""),
                evening=_normalize_pick3(evening or ""),
            )
    return winners


def _candidate_universe_path(state_dir: Path, *, profile: str, experiment_tag: str) -> Path:
    out_suffix = _profile_suffix(profile)
    tag_suffix = f"__{experiment_tag.strip()}" if (experiment_tag or "").strip() else ""
    return state_dir / f"candidate_universe{out_suffix}{tag_suffix}.json"


def _load_candidate_universe_summary_tagged(
    state_dir: Path,
    *,
    profile: str,
    prefer_experiment_tags: Sequence[str],
) -> Tuple[int, int, List[str], int, List[str]]:
    """
    Returns:
      packs_count, union_count, due_doubles_canonicals_union, top_support_count, top_support_canonicals(up to 3)
    """
    cu: Optional[Path] = None
    for tag in prefer_experiment_tags:
        cand = _candidate_universe_path(state_dir, profile=profile, experiment_tag=tag)
        if cand.exists():
            cu = cand
            break
    if cu is None:
        return 0, 0, [], 0, []
    raw = _read_json(cu)
    if not isinstance(raw, dict):
        return 0, 0, [], 0, []
    packs = raw.get("packs")
    packs_list = packs if isinstance(packs, list) else []

    union_count = raw.get("union_combos_count")
    try:
        union_count_int = int(union_count)
    except Exception:
        union = raw.get("union_combos")
        union_count_int = len(union) if isinstance(union, list) else 0

    due_doubles: set[str] = set()
    support: Dict[str, int] = {}
    for p in packs_list:
        if not isinstance(p, dict):
            continue
        method_id = str(p.get("method_id") or "")
        canonicals = p.get("canonicals") or []

        if isinstance(canonicals, list):
            uniq: set[str] = set()
            for c in canonicals:
                cc = _canon(str(c))
                if cc:
                    uniq.add(cc)
            for cc in uniq:
                support[cc] = support.get(cc, 0) + 1

        if method_id == "due_doubles" and isinstance(canonicals, list):
            for c in canonicals:
                cc = _canon(str(c))
                if cc:
                    due_doubles.add(cc)

    top_support_count = max(support.values(), default=0)
    top_support = [c for c, n in sorted(support.items(), key=lambda x: (-x[1], x[0])) if n == top_support_count][:3]
    return len(packs_list), union_count_int, sorted(due_doubles), top_support_count, top_support


def _play_card_path(state_dir: Path, *, profile: str, experiment_tag: str) -> Path:
    out_suffix = _profile_suffix(profile)
    tag_suffix = f"__{experiment_tag.strip()}" if (experiment_tag or "").strip() else ""
    return state_dir / f"play_card{out_suffix}{tag_suffix}.json"


def _load_play_card_cut(
    state_dir: Path,
    *,
    profile: str,
    strategy: str,
    budget: int,
    prefer_experiment_tags: Sequence[str],
) -> Tuple[set[str], List[str], Optional[Path]]:
    """
    Returns (boxed_full_canonicals, combos, source_path).
    """
    bkey = f"B{int(budget)}"
    for tag in prefer_experiment_tags:
        pc = _play_card_path(state_dir, profile=profile, experiment_tag=tag)
        if not pc.exists():
            continue
        raw = _read_json(pc)
        if not isinstance(raw, dict):
            continue
        strategies = raw.get("strategies")
        if not isinstance(strategies, dict):
            continue
        strat = strategies.get(strategy)
        if not isinstance(strat, dict):
            continue
        card = strat.get(bkey)
        if not isinstance(card, dict):
            continue
        combos = [_normalize_pick3(x) for x in (card.get("combos") or [])]
        combos_list = [c for c in combos if c]
        return _boxed_canonicals(combos_list), combos_list, pc
    return set(), [], None


def _parse_date(s: str) -> date:
    parts = (s or "").strip().split("-")
    if len(parts) != 3:
        raise ValueError(f"Invalid date: {s!r} (expected YYYY-MM-DD)")
    return date(int(parts[0]), int(parts[1]), int(parts[2]))


def _iter_dates_between(sharepacks_root: Path, start: date, end: date) -> List[str]:
    out: List[str] = []
    for p in sorted(sharepacks_root.iterdir(), key=lambda q: q.name):
        if not p.is_dir():
            continue
        try:
            d = _parse_date(p.name)
        except Exception:
            continue
        if start <= d <= end:
            out.append(p.name)
    return out


@dataclass(frozen=True)
class BudgetSpec:
    label: str
    budget: int
    strategy: str


def _rank_key(r: Dict[str, Any]) -> Tuple[int, int, int, int, str]:
    """
    Matches create_predictive_portfolio_report.py tool_first ordering:
      1) candidate_top_support desc
      2) candidate_union asc
      3) due_doubles_count desc
      4) candidate_packs desc
      5) state_key
    """
    return (
        -int(r.get("candidate_top_support") or 0),
        int(r.get("candidate_union") or 0),
        -int(r.get("due_doubles_count") or 0),
        -int(r.get("candidate_packs") or 0),
        str(r.get("state_key") or ""),
    )


def _summarize_against_winner(
    *,
    winner: str,
    combos: Sequence[str],
    boxed_full: set[str],
) -> Dict[str, Any]:
    winner = _normalize_pick3(winner)
    if not winner:
        return {"winner_missing": 1}

    winner_canon = _canon(winner)
    winner_idx = _winner_vtrac_index(winner)

    combos_norm = [_normalize_pick3(c) for c in combos if _normalize_pick3(c)]
    combos_set = set(combos_norm)
    canon_set = {c for c in (_canon(x) for x in combos_norm) if c}

    # Core hit flags.
    straight_hit = 1 if winner in combos_set else 0
    boxed_any_perm_hit = 1 if (winner_canon and winner_canon in canon_set) else 0
    boxed_full_hit = 1 if (winner_canon and winner_canon in boxed_full) else 0

    # Lane/index stats.
    idxs: List[int] = []
    in_winner_index = 0
    if isinstance(winner_idx, int):
        for c in combos_norm:
            idx = _combo_vtrac_index(c)
            if isinstance(idx, int):
                idxs.append(idx)
                if idx == winner_idx:
                    in_winner_index += 1
    idx_counts = Counter(idxs) if idxs else Counter()
    unique_indices = len(idx_counts)
    top_index_count = max(idx_counts.values(), default=0)
    winner_index_is_top = 0
    if isinstance(winner_idx, int) and idx_counts:
        winner_index_is_top = 1 if idx_counts.get(winner_idx, 0) == top_index_count and top_index_count > 0 else 0
    vtrac_index_hit = 1 if in_winner_index > 0 else 0

    # Advanced closeness.
    winner_digits_u = _digits_unique(winner)
    digit_union: set[str] = set()
    best_overlap = 0
    overlap2plus = 0
    doubles_count = 0
    for c in combos_norm:
        digit_union |= _digits_unique(c)
        ov = _multiset_digit_overlap(c, winner)
        best_overlap = max(best_overlap, ov)
        if ov >= 2:
            overlap2plus += 1
        if _is_double_like(c):
            doubles_count += 1
    digit_cover_all_unique = 1 if winner_digits_u and winner_digits_u.issubset(digit_union) else 0
    digit_cover_unique = len(winner_digits_u & digit_union) if winner_digits_u else 0

    return {
        "winner_missing": 0,
        "winner": winner,
        "winner_canonical": winner_canon,
        "winner_vtrac_index": winner_idx if isinstance(winner_idx, int) else "",
        "straight_hit": straight_hit,
        "boxed_any_perm_hit": boxed_any_perm_hit,
        "boxed_full_hit": boxed_full_hit,
        "vtrac_index_hit": vtrac_index_hit,
        "in_winner_index": in_winner_index,
        "unique_indices": unique_indices,
        "top_index_count": top_index_count,
        "winner_index_is_top": winner_index_is_top,
        "digit_cover_unique": digit_cover_unique,
        "digit_cover_all_unique": digit_cover_all_unique,
        "best_overlap": best_overlap,
        "overlap2plus_count": overlap2plus,
        "winner_is_double": 1 if _is_double_like(winner) else 0,
        "combos_with_double_count": doubles_count,
    }


def main() -> None:
    ap = argparse.ArgumentParser(description="Create a windowed Portfolio vs Results report (predictive sharepacks).")
    ap.add_argument("--start-date", required=True, help="Start date (YYYY-MM-DD)")
    ap.add_argument("--end-date", required=True, help="End date (YYYY-MM-DD)")
    ap.add_argument(
        "--sharepacks-root",
        default="sharepacks/_predictive",
        help="Sharepacks root directory (default: sharepacks/_predictive)",
    )
    ap.add_argument(
        "--profile",
        choices=["mixed", "tool_only", "profit_only"],
        default="tool_only",
        help="Ablation profile (default: tool_only). Selects candidate_universe/play_card suffix.",
    )
    ap.add_argument(
        "--prefer-experiment-tags",
        default=None,
        help=(
            "Optional comma-separated experiment tags to prefer when selecting candidate_universe/play_card files. "
            "Default: stable10,,vtracpack_v1."
        ),
    )
    ap.add_argument("--play-strategy-b12", default="analysis_prefix", help="B12 play strategy key.")
    ap.add_argument(
        "--play-strategy-b24",
        default="vtrac_pack_boxed_first_laneonly_presetB",
        help="B24 play strategy key.",
    )
    ap.add_argument(
        "--play-strategy-b36",
        default="v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22",
        help="B36 play strategy key.",
    )
    ap.add_argument("--out-md", default=None, help="Override Markdown output path.")
    ap.add_argument("--out-csv", default=None, help="Override CSV output path.")
    ap.add_argument("--force", action="store_true", help="Overwrite existing outputs (default: refuse).")
    ap.add_argument(
        "--skip-missing-results",
        action="store_true",
        help="Skip dates without data/results/<D>.txt (default: fail).",
    )
    args = ap.parse_args()

    start = _parse_date(args.start_date)
    end = _parse_date(args.end_date)
    if end < start:
        raise SystemExit("--end-date must be >= --start-date")

    sharepacks_root = Path(args.sharepacks_root)
    if not sharepacks_root.is_absolute():
        sharepacks_root = (REPO_ROOT / sharepacks_root).resolve()

    prefer_tags: Sequence[str] = ("stable10", "", "vtracpack_v1")
    raw_prefer = str(args.prefer_experiment_tags or "").strip()
    if raw_prefer:
        tags: List[str] = []
        for part in raw_prefer.split(","):
            part = part.strip()
            if not part or part.lower() in {"-", "none", "null"}:
                tag = ""
            else:
                tag = _normalize_experiment_tag(part)
            if tag not in tags:
                tags.append(tag)
        if "" not in tags:
            tags.append("")
        if "vtracpack_v1" not in tags:
            tags.append("vtracpack_v1")
        prefer_tags = tags

    dates = _iter_dates_between(sharepacks_root, start, end)
    if not dates:
        raise SystemExit(f"No sharepack days found under {_safe_rel(sharepacks_root)} between {start} and {end}")

    profile = str(args.profile or "mixed").strip()
    out_suffix = "" if profile == "mixed" else f"__{profile}"

    runs_dir = _runs_dir()
    runs_dir.mkdir(parents=True, exist_ok=True)
    out_md = (
        Path(args.out_md)
        if args.out_md
        else runs_dir / f"{start.isoformat()}_to_{end.isoformat()}__PORTFOLIO_VS_RESULTS{out_suffix}.md"
    )
    out_csv = (
        Path(args.out_csv)
        if args.out_csv
        else runs_dir / f"{start.isoformat()}_to_{end.isoformat()}__PORTFOLIO_VS_RESULTS{out_suffix}.csv"
    )
    if (out_md.exists() or out_csv.exists()) and not args.force:
        raise SystemExit(f"Refusing to overwrite existing outputs (use --force): {_safe_rel(out_md)} / {_safe_rel(out_csv)}")

    budgets = [
        BudgetSpec("B12", 12, str(args.play_strategy_b12).strip()),
        BudgetSpec("B24", 24, str(args.play_strategy_b24).strip()),
        BudgetSpec("B36", 36, str(args.play_strategy_b36).strip()),
    ]

    rows_out: List[Dict[str, Any]] = []
    skipped_missing_results: List[str] = []

    for dstr in dates:
        day_dir = sharepacks_root / dstr
        if not day_dir.exists():
            continue

        results_file = REPO_ROOT / "data" / "results" / f"{dstr}.txt"
        if not results_file.exists():
            if args.skip_missing_results:
                skipped_missing_results.append(dstr)
                continue
            raise SystemExit(f"Missing results file: {_safe_rel(results_file)} (use --skip-missing-results to ignore)")

        winners_by_state = _load_results_winners(results_file)

        # Build state list + rank (same ordering as the predictive portfolio tool-first triage).
        state_rows: List[Dict[str, Any]] = []
        for p in sorted(day_dir.iterdir(), key=lambda q: q.name):
            if not p.is_dir() or p.name == "control_center":
                continue
            state_key = p.name
            packs_count, union_count, due_doubles, top_support_count, top_support = _load_candidate_universe_summary_tagged(
                p, profile=profile, prefer_experiment_tags=prefer_tags
            )
            state_rows.append(
                {
                    "results_date": dstr,
                    "state_key": state_key,
                    "candidate_packs": packs_count,
                    "candidate_union": union_count,
                    "due_doubles": due_doubles,
                    "due_doubles_count": len(due_doubles),
                    "candidate_top_support": int(top_support_count),
                    "candidate_top_support_canon": top_support,
                }
            )
        state_rows.sort(key=_rank_key)
        rank_by_state = {r["state_key"]: i + 1 for i, r in enumerate(state_rows)}

        for r in state_rows:
            state_key = str(r["state_key"])
            state_dir = day_dir / state_key

            # Load the actual play-card lists for each budget.
            combos_by_budget: Dict[str, List[str]] = {}
            boxed_by_budget: Dict[str, set[str]] = {}
            src_by_budget: Dict[str, str] = {}
            for b in budgets:
                boxed_full, combos, src = _load_play_card_cut(
                    state_dir,
                    profile=profile,
                    strategy=b.strategy,
                    budget=b.budget,
                    prefer_experiment_tags=prefer_tags,
                )
                combos_by_budget[b.label] = combos
                boxed_by_budget[b.label] = boxed_full
                src_by_budget[b.label] = _safe_rel(src) if src else ""

            w = winners_by_state.get(state_key, Winner(midday=None, evening=None))
            for winner_label, winner_value in (("Midday", w.midday or ""), ("Evening", w.evening or "")):
                for b in budgets:
                    combos = combos_by_budget.get(b.label, [])
                    boxed_full = boxed_by_budget.get(b.label, set())
                    metrics = _summarize_against_winner(winner=winner_value, combos=combos, boxed_full=boxed_full)

                    winner_canon = str(metrics.get("winner_canonical") or "")
                    due_doubles: List[str] = [str(x) for x in (r.get("due_doubles") or [])]
                    top_support: List[str] = [str(x) for x in (r.get("candidate_top_support_canon") or [])]
                    rows_out.append(
                        {
                            "results_date": dstr,
                            "state_key": state_key,
                            "rank": rank_by_state.get(state_key, ""),
                            "winner_label": winner_label,
                            "budget_label": b.label,
                            "strategy": b.strategy,
                            "combos_count": len(combos),
                            "play_card_path": src_by_budget.get(b.label, ""),
                            "candidate_packs": r.get("candidate_packs", 0),
                            "candidate_union": r.get("candidate_union", 0),
                            "candidate_top_support": r.get("candidate_top_support", 0),
                            "candidate_top_support_canon": " ".join(top_support) if top_support else "",
                            "due_doubles_count": r.get("due_doubles_count", 0),
                            "due_doubles_canon": " ".join(due_doubles) if due_doubles else "",
                            "due_doubles_contains_winner_canon": 1 if (winner_canon and winner_canon in set(due_doubles)) else 0,
                            "top_support_contains_winner_canon": 1 if (winner_canon and winner_canon in set(top_support)) else 0,
                            **metrics,
                        }
                    )

    # Write CSV (row-level; markdown will summarize).
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    fieldnames: List[str] = []
    for r in rows_out:
        for k in r.keys():
            if k not in fieldnames:
                fieldnames.append(k)
    with out_csv.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows_out:
            w.writerow({k: r.get(k, "") for k in fieldnames})

    # Build markdown summary.
    def _prob_at_least_one_hit(*, pop_size: int, draw_n: int, good_k: int) -> float:
        """
        Random-baseline helper.

        Probability of drawing >=1 "good" item when drawing draw_n items uniformly
        without replacement from a population of pop_size that contains good_k "good"
        items.
        """
        if pop_size <= 0:
            return 0.0
        if good_k <= 0 or draw_n <= 0:
            return 0.0
        if good_k >= pop_size or draw_n >= pop_size:
            return 1.0
        if draw_n > (pop_size - good_k):
            return 1.0
        no_hit = 1.0
        for i in range(draw_n):
            no_hit *= (pop_size - good_k - i) / (pop_size - i)
        return 1.0 - no_hit

    def _vtrac_index_sizes() -> Dict[int, int]:
        import modules.vtrac_reference as vr

        counts: Dict[int, int] = {}
        for n in range(1000):
            s = f"{n:03d}"
            idx = vr.get_vtrac_index(s)
            if isinstance(idx, int):
                counts[idx] = counts.get(idx, 0) + 1
        return counts

    def _rate(n: int, d: int) -> str:
        return "—" if d <= 0 else f"{(100.0 * n / d):.1f}% ({n}/{d})"

    def _pct(n: int, d: int) -> str:
        return "—" if d <= 0 else f"{(100.0 * n / d):.1f}%"

    def _rank_int(row: Dict[str, Any]) -> int:
        try:
            return int(row.get("rank") or 0) or 9999
        except Exception:
            return 9999

    def _count_metric(rows: Sequence[Dict[str, Any]], key: str) -> int:
        return sum(1 for r in rows if int(r.get(key) or 0) == 1)

    eligible = [r for r in rows_out if int(r.get("winner_missing") or 0) == 0]
    by_budget: Dict[str, List[Dict[str, Any]]] = {}
    for r in eligible:
        by_budget.setdefault(str(r.get("budget_label") or "?"), []).append(r)

    # Random baselines (for context only): compare observed hit rates vs random picks.
    # These are *not* claims of significance; they help you calibrate intuition quickly.
    vtrac_sizes = _vtrac_index_sizes()

    lines: List[str] = []
    lines.append(f"# Portfolio vs Results (Windowed) — {start.isoformat()} → {end.isoformat()}{out_suffix}")
    lines.append("")
    lines.append("Broad-first evaluation of B12/B24/B36 Play Cards vs posted Midday/Evening results, plus near-miss signals.")
    lines.append("")
    lines.append("## Inputs (SSOT)")
    lines.append(f"- Predictive sharepacks root: `{_safe_rel(sharepacks_root)}`")
    lines.append("- Results root: `data/results/` (graded against same-date `data/results/<D>.txt`)")
    lines.append("")
    lines.append("## Outputs")
    lines.append(f"- Row-level CSV (sortable): `{_safe_rel(out_csv)}`")
    lines.append("")
    lines.append("## Window coverage")
    lines.append(f"- Sharepack days in window: **{len(dates)}** (`{dates[0]}` → `{dates[-1]}`)")
    lines.append(f"- Outcome rows produced: **{len(rows_out)}** (Midday+Evening × B12/B24/B36)")
    lines.append(f"- Rows with a winner present: **{len(eligible)}**")
    if skipped_missing_results:
        lines.append(f"- Skipped missing results dates: `{', '.join(skipped_missing_results)}`")
    lines.append("")
    lines.append("## Hit-rate summary (all states + both outcomes)")
    lines.append("| Budget | Straight | Boxed(any perm) | Boxed(full) | VTRAC idx hit | Digit-cover(all unique) | Avg in-winner-index |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|")
    for b in ("B12", "B24", "B36"):
        rows = by_budget.get(b, [])
        dcount = len(rows)
        straight = sum(int(r.get("straight_hit") or 0) for r in rows)
        boxed_any = sum(int(r.get("boxed_any_perm_hit") or 0) for r in rows)
        boxed_full = sum(int(r.get("boxed_full_hit") or 0) for r in rows)
        lane = sum(int(r.get("vtrac_index_hit") or 0) for r in rows)
        digit_cover = sum(int(r.get("digit_cover_all_unique") or 0) for r in rows)
        avg_in_lane = (sum(int(r.get("in_winner_index") or 0) for r in rows) / dcount) if dcount else 0.0
        lines.append(
            f"| {b} | {_rate(straight, dcount)} | {_rate(boxed_any, dcount)} | {_rate(boxed_full, dcount)} | {_rate(lane, dcount)} | {_rate(digit_cover, dcount)} | {avg_in_lane:.2f} |"
        )

    lines.append("")
    lines.append("## Random baseline context (calibration, not a performance claim)")
    lines.append(
        "These are the expected hit rates if you picked the same number of lines uniformly at random from 000–999. "
        "Use this to calibrate which metrics are genuinely “hard” vs “easy” at each budget."
    )
    lines.append("| Budget | Expected Straight | Observed Straight | Expected Boxed(any perm) | Observed Boxed(any perm) | Expected VTRAC idx hit | Observed VTRAC idx hit |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|")
    for b in ("B12", "B24", "B36"):
        rows = by_budget.get(b, [])
        if not rows:
            continue
        dcount = len(rows)
        obs_straight = _count_metric(rows, "straight_hit")
        obs_box = _count_metric(rows, "boxed_any_perm_hit")
        obs_lane = _count_metric(rows, "vtrac_index_hit")

        exp_straight = sum(
            _prob_at_least_one_hit(pop_size=1000, draw_n=int(r.get("combos_count") or 0), good_k=1) for r in rows
        ) / dcount

        exp_box = 0.0
        exp_lane = 0.0
        for r in rows:
            winner = _normalize_pick3(r.get("winner") or "")
            n_lines = int(r.get("combos_count") or 0)
            if winner:
                exp_box += _prob_at_least_one_hit(pop_size=1000, draw_n=n_lines, good_k=len(_unique_perms(winner)))
                winner_idx = r.get("winner_vtrac_index")
                try:
                    idx_int = int(winner_idx)
                except Exception:
                    idx_int = -1
                idx_size = vtrac_sizes.get(idx_int, 0)
                exp_lane += _prob_at_least_one_hit(pop_size=1000, draw_n=n_lines, good_k=idx_size)
        exp_box = exp_box / dcount
        exp_lane = exp_lane / dcount

        lines.append(
            "| "
            + " | ".join(
                [
                    b,
                    f"{exp_straight*100.0:.1f}%",
                    _pct(obs_straight, dcount),
                    f"{exp_box*100.0:.1f}%",
                    _pct(obs_box, dcount),
                    f"{exp_lane*100.0:.1f}%",
                    _pct(obs_lane, dcount),
                ]
            )
            + " |"
        )

    # Rank vs hits (does the portfolio ranking concentrate hits?).
    lines.append("")
    lines.append("## Rank vs hits (is the daily state ranking actually concentrating hits?)")
    lines.append(
        "Bands are per-day rank bands (same rank definition as the predictive portfolio tool-first triage). "
        "Lift>1 means hits are more concentrated than random-by-rank."
    )

    metrics = [
        ("straight_hit", "Straight"),
        ("boxed_any_perm_hit", "Boxed(any perm)"),
        ("boxed_full_hit", "Boxed(full)"),
        ("vtrac_index_hit", "VTRAC idx hit"),
    ]
    for budget in ("B12", "B24", "B36"):
        rows = by_budget.get(budget, [])
        if not rows:
            continue
        rows_top3 = [r for r in rows if _rank_int(r) <= 3]
        rows_4_7 = [r for r in rows if 4 <= _rank_int(r) <= 7]
        rows_8p = [r for r in rows if _rank_int(r) >= 8]
        total_rows = len(rows)
        share_top3 = len(rows_top3) / total_rows if total_rows else 0.0

        lines.append("")
        lines.append(f"### {budget}")
        lines.append("| Metric | Hits | Top3 capture | Lift(top3) | HitRate Top3 | HitRate 4-7 | HitRate 8+ |")
        lines.append("|---|---:|---:|---:|---:|---:|---:|")
        for key, label in metrics:
            total_hits = _count_metric(rows, key)
            if total_hits <= 0:
                lines.append(f"| {label} | 0 | — | — | — | — | — |")
                continue
            hits_top3 = _count_metric(rows_top3, key)
            capture_top3 = hits_top3 / total_hits
            lift_top3 = (capture_top3 / share_top3) if share_top3 > 0 else 0.0
            lines.append(
                "| "
                + " | ".join(
                    [
                        label,
                        str(total_hits),
                        f"{capture_top3*100.0:.1f}% (exp {share_top3*100.0:.1f}%)",
                        f"{lift_top3:.2f}x",
                        _pct(_count_metric(rows_top3, key), len(rows_top3)),
                        _pct(_count_metric(rows_4_7, key), len(rows_4_7)),
                        _pct(_count_metric(rows_8p, key), len(rows_8p)),
                    ]
                )
                + " |"
            )

    # Doubles lens (your "system likes doubles" hypothesis).
    lines.append("")
    lines.append("## Doubles lens (does performance change when the winner is a double/triple?)")
    lines.append("| Budget | WinnerType | Rows | Straight | Boxed(any perm) | VTRAC idx hit |")
    lines.append("|---|---|---:|---:|---:|---:|")
    for budget in ("B12", "B24", "B36"):
        rows = by_budget.get(budget, [])
        if not rows:
            continue
        dbl = [r for r in rows if int(r.get("winner_is_double") or 0) == 1]
        sgl = [r for r in rows if int(r.get("winner_is_double") or 0) == 0]
        for label, subset in (("double", dbl), ("single", sgl)):
            lines.append(
                "| "
                + " | ".join(
                    [
                        budget,
                        label,
                        str(len(subset)),
                        _pct(_count_metric(subset, "straight_hit"), len(subset)),
                        _pct(_count_metric(subset, "boxed_any_perm_hit"), len(subset)),
                        _pct(_count_metric(subset, "vtrac_index_hit"), len(subset)),
                    ]
                )
                + " |"
            )

    # Digit-assembly misses (digits present somewhere, but never assembled as a winner-perm).
    lines.append("")
    lines.append("## Digit-assembly misses (all winner digits are present somewhere in the list, but no winner-perm exists)")
    lines.append("| Budget | Rows | DigitCoverAll | CoverAll+NoBoxPerm | OfThose: best_overlap>=2 |")
    lines.append("|---|---:|---:|---:|---:|")
    for budget in ("B12", "B24", "B36"):
        rows = by_budget.get(budget, [])
        if not rows:
            continue
        cover_all = [r for r in rows if int(r.get("digit_cover_all_unique") or 0) == 1]
        cover_all_no_perm = [r for r in cover_all if int(r.get("boxed_any_perm_hit") or 0) == 0]
        overlap2plus = [r for r in cover_all_no_perm if int(r.get("best_overlap") or 0) >= 2]
        lines.append(
            "| "
            + " | ".join(
                [
                    budget,
                    str(len(rows)),
                    _rate(len(cover_all), len(rows)),
                    _rate(len(cover_all_no_perm), len(rows)),
                    _rate(len(overlap2plus), len(cover_all_no_perm)),
                ]
            )
            + " |"
        )

    # Winner-lane depth (within-index count) — direct response to your “4–5 combos in the winner index” question.
    lines.append("")
    lines.append("## Winner-lane depth (how many listed combos landed inside the winner’s VTRAC index?)")
    lines.append("| Budget | LaneHit rows | Avg in_winner_index | pct(in>=2) | pct(in>=4) | pct(in>=6) |")
    lines.append("|---|---:|---:|---:|---:|---:|")
    for budget in ("B12", "B24", "B36"):
        rows = by_budget.get(budget, [])
        lane_rows = [r for r in rows if int(r.get("vtrac_index_hit") or 0) == 1]
        if not lane_rows:
            lines.append(f"| {budget} | 0 | — | — | — | — |")
            continue
        avg_in = sum(int(r.get("in_winner_index") or 0) for r in lane_rows) / len(lane_rows)
        ge2 = sum(1 for r in lane_rows if int(r.get("in_winner_index") or 0) >= 2)
        ge4 = sum(1 for r in lane_rows if int(r.get("in_winner_index") or 0) >= 4)
        ge6 = sum(1 for r in lane_rows if int(r.get("in_winner_index") or 0) >= 6)
        lines.append(
            "| "
            + " | ".join(
                [
                    budget,
                    str(len(lane_rows)),
                    f"{avg_in:.2f}",
                    _pct(ge2, len(lane_rows)),
                    _pct(ge4, len(lane_rows)),
                    _pct(ge6, len(lane_rows)),
                ]
            )
            + " |"
        )

    # State leaderboard (broad orientation): which states in this window had more hits/near-hits.
    lines.append("")
    lines.append("## State leaderboard (window totals; use this to pick which states to deep-dive first)")
    lines.append("Counts are across Midday+Evening outcomes in this window (winner-present rows only).")
    for budget in ("B12", "B24", "B36"):
        rows = by_budget.get(budget, [])
        if not rows:
            continue
        by_state: Dict[str, List[Dict[str, Any]]] = {}
        for r in rows:
            by_state.setdefault(str(r.get("state_key") or "?"), []).append(r)
        lines.append("")
        lines.append(f"### {budget}")
        lines.append("| State | Rows | Straight | Boxed(any perm) | VTRAC idx hit | DigitCoverAll |")
        lines.append("|---|---:|---:|---:|---:|---:|")
        for state_key in sorted(by_state.keys()):
            srows = by_state[state_key]
            lines.append(
                "| "
                + " | ".join(
                    [
                        state_key,
                        str(len(srows)),
                        _rate(_count_metric(srows, "straight_hit"), len(srows)),
                        _rate(_count_metric(srows, "boxed_any_perm_hit"), len(srows)),
                        _rate(_count_metric(srows, "vtrac_index_hit"), len(srows)),
                        _rate(_count_metric(srows, "digit_cover_all_unique"), len(srows)),
                    ]
                )
                + " |"
            )

    # Context columns from the portfolio table (due doubles / CU top support).
    # These are outcome-level context signals, so we summarize them once using the B36 rows (winner-present).
    ctx_rows = [r for r in eligible if str(r.get("budget_label") or "") == "B36"]
    if ctx_rows:
        lines.append("")
        lines.append("## Portfolio context signals (due doubles + CU top support)")
        lines.append("These come from Candidate Universe (not from the Play Card itself).")

        def _ctx_rate(rows: Sequence[Dict[str, Any]], key: str) -> str:
            return _rate(sum(1 for r in rows if int(r.get(key) or 0) == 1), len(rows))

        lines.append("| Context signal | Overall | Among B36 straight hits | Among B36 boxed(any perm) hits | Among B36 VTRAC idx hits |")
        lines.append("|---|---:|---:|---:|---:|")
        for ctx_key, label in (
            ("due_doubles_contains_winner_canon", "DueDoubles contains winner canonical"),
            ("top_support_contains_winner_canon", "CU top-support contains winner canonical"),
        ):
            straight_rows = [r for r in ctx_rows if int(r.get("straight_hit") or 0) == 1]
            boxed_rows = [r for r in ctx_rows if int(r.get("boxed_any_perm_hit") or 0) == 1]
            lane_rows = [r for r in ctx_rows if int(r.get("vtrac_index_hit") or 0) == 1]
            lines.append(
                "| "
                + " | ".join(
                    [
                        label,
                        _ctx_rate(ctx_rows, ctx_key),
                        _ctx_rate(straight_rows, ctx_key),
                        _ctx_rate(boxed_rows, ctx_key),
                        _ctx_rate(lane_rows, ctx_key),
                    ]
                )
                + " |"
            )

    # "Near miss" shortlist: lane hit but no boxed-any-perm.
    def _ival(v: Any) -> int:
        try:
            return int(v)
        except Exception:
            return 0

    near_misses = [
        r
        for r in eligible
        if _ival(r.get("vtrac_index_hit")) == 1 and _ival(r.get("boxed_any_perm_hit")) == 0
    ]
    near_misses.sort(
        key=lambda r: (
            -_ival(r.get("digit_cover_all_unique")),
            -_ival(r.get("best_overlap")),
            -_ival(r.get("in_winner_index")),
            int(r.get("rank") or 9999),
            str(r.get("results_date") or ""),
            str(r.get("state_key") or ""),
            str(r.get("winner_label") or ""),
            str(r.get("budget_label") or ""),
        )
    )

    lines.append("")
    lines.append("## Top ‘near miss’ cases (lane hit but digits not hit)")
    lines.append("| D | Rank | State | Winner | Budget | in_winner_index | digit_cover_all | best_overlap | play_card |")
    lines.append("|---|---:|---|---:|---:|---:|---:|---:|---|")
    for r in near_misses[:30]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(r.get("results_date") or ""),
                    str(r.get("rank") or ""),
                    str(r.get("state_key") or ""),
                    str(r.get("winner") or ""),
                    str(r.get("budget_label") or ""),
                    str(r.get("in_winner_index") or 0),
                    str(r.get("digit_cover_all_unique") or 0),
                    str(r.get("best_overlap") or 0),
                    str(r.get("play_card_path") or ""),
                ]
            )
            + " |"
        )

    # Digit-assembly roster: winner digits present but not assembled into any winner permutation.
    digit_assembly = [
        r
        for r in eligible
        if int(r.get("digit_cover_all_unique") or 0) == 1 and int(r.get("boxed_any_perm_hit") or 0) == 0
    ]
    digit_assembly.sort(
        key=lambda r: (
            -_ival(r.get("best_overlap")),
            -_ival(r.get("overlap2plus_count")),
            int(r.get("rank") or 9999),
            str(r.get("results_date") or ""),
            str(r.get("state_key") or ""),
            str(r.get("winner_label") or ""),
            str(r.get("budget_label") or ""),
        )
    )
    lines.append("")
    lines.append("## Top ‘digit assembly’ cases (all digits present, but no winner permutation was selected)")
    lines.append("| D | Rank | State | Winner | Budget | best_overlap | overlap2plus_count | play_card |")
    lines.append("|---|---:|---|---:|---:|---:|---:|---|")
    for r in digit_assembly[:30]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(r.get("results_date") or ""),
                    str(r.get("rank") or ""),
                    str(r.get("state_key") or ""),
                    str(r.get("winner") or ""),
                    str(r.get("budget_label") or ""),
                    str(r.get("best_overlap") or 0),
                    str(r.get("overlap2plus_count") or 0),
                    str(r.get("play_card_path") or ""),
                ]
            )
            + " |"
        )

    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

    print(f"[OK] Wrote: {_safe_rel(out_md)}")
    print(f"[OK] Wrote: {_safe_rel(out_csv)}")


if __name__ == "__main__":
    main()
