#!/usr/bin/env python3
"""
Digit Reduction envelope/persistence harness (reporting-only).

Purpose
-------
Digit Reduction (DR) frequently "sees" the winner in its traces/overlays, but the current
caller surface (analyzer_v2 `best_pattern` top candidates) performs poorly as a predictive
top-N list (see `docs/.../RUNS/DR_V0__AUDIT__QUANT.md` and `DR_V0__AUDIT__CASES.md`).

This harness evaluates an alternative *selection-layer* view of DR using only the
sharepack-local DR trace evidence:

  - `sharepacks/<D>/<STATE>/digit_reduction/<STATE>/training/<STATE>_digit_reduction_steps.csv`

It builds a score for candidate canonicals by aggregating "digit pool" evidence across
early steps (weighted by step) and smaller pools (weighted by unique digit count), then
grades vs official results.

Key properties
--------------
- Reads frozen sharepacks + results (post-results evaluation only).
- Writes CSV + Markdown into RUNS; does not write into sharepacks.
- Does not touch analyzers; this is measurement to decide v0.2 consumption vs v0.3 tuning.
"""

from __future__ import annotations

import argparse
import csv
import sys
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
if SRC_ROOT.exists() and str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))


from alpha_analytical.control_center.batch_runner import parse_winner_sheet  # noqa: E402

import modules.vtrac_reference as vr  # noqa: E402


DEFAULT_STATES: List[str] = [
    "Connecticut4",
    "Delaware4",
    "Florida4",
    "Indiana4",
    "Michigan4",
    "NewJersey4",
    "NewYork4",
    "NorthCarolina4",
    "Ohio4",
    "OntarioCanada4",
    "Pennsylvania4",
    "PuertoRico4",
    "SouthCarolina4",
    "Virginia4",
]


def _runs_dir() -> Path:
    return REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"


def _safe_rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _canon(draw: str) -> str:
    digits = "".join(ch for ch in str(draw or "") if ch.isdigit())
    if not digits:
        return ""
    digits = digits.zfill(3) if len(digits) <= 3 else digits
    if len(digits) != 3:
        return ""
    return "".join(sorted(digits))


def _winner_digits_count(winner: str) -> int:
    canon = _canon(winner)
    return len(set(canon)) if canon else 0


def _boxed_cost_units(canon: str) -> int:
    """
    Box closure cost proxy: number of unique permutations.
    - triple: 1
    - double: 3
    - all distinct: 6
    """
    if not canon or len(canon) != 3:
        return 0
    a, b, c = canon
    if a == b == c:
        return 1
    if a == b or b == c:
        return 3
    return 6


def _iter_dates(start: str, end: str) -> List[str]:
    a = datetime.strptime(start, "%Y-%m-%d")
    b = datetime.strptime(end, "%Y-%m-%d")
    if b < a:
        a, b = b, a
    out: List[str] = []
    cur = a
    while cur <= b:
        out.append(cur.strftime("%Y-%m-%d"))
        cur += timedelta(days=1)
    return out


def _read_results_winners(results_date: str) -> Dict[str, Dict[str, str]]:
    """
    Return: project_state -> {"Midday": "123", "Evening": "456"} (as available).
    """
    results_path = REPO_ROOT / "data" / "results" / f"{results_date}.txt"
    if not results_path.exists():
        return {}
    entries = parse_winner_sheet(results_path.read_text(encoding="utf-8", errors="replace"))
    out: Dict[str, Dict[str, str]] = {}
    for e in entries:
        if not e.project_state:
            continue
        m: Dict[str, str] = {}
        if e.midday:
            m["Midday"] = e.midday
        if e.evening:
            m["Evening"] = e.evening
        if m:
            out[e.project_state] = m
    return out


def _steps_csv_path(day_dir: Path, state: str) -> Path:
    return day_dir / state / "digit_reduction" / state / "training" / f"{state}_digit_reduction_steps.csv"


@dataclass(frozen=True)
class StepRow:
    step: int
    unique_digits: int
    digits: Tuple[str, ...]


@dataclass(frozen=True)
class CandidateSets:
    singles: Tuple[str, ...]
    doubles: Tuple[str, ...]
    triples: Tuple[str, ...]


def _candidate_sets_for_digits(digits: Tuple[str, ...]) -> CandidateSets:
    if not digits:
        return CandidateSets((), (), ())
    if len(digits) == 1:
        d = digits[0]
        return CandidateSets((), (), (d + d + d,))

    doubles: List[str] = []
    for i in range(len(digits)):
        for j in range(i + 1, len(digits)):
            a, b = digits[i], digits[j]
            doubles.append("".join(sorted(a + a + b)))
            doubles.append("".join(sorted(a + b + b)))

    singles: List[str] = []
    if len(digits) >= 3:
        for i in range(len(digits)):
            for j in range(i + 1, len(digits)):
                for k in range(j + 1, len(digits)):
                    singles.append(digits[i] + digits[j] + digits[k])

    return CandidateSets(tuple(sorted(set(singles))), tuple(sorted(set(doubles))), ())


@dataclass(frozen=True)
class VariantConfig:
    label: str
    max_unique_digits: int
    step_power: float
    unique_power: float
    double_weight: float
    split_weight: bool


@dataclass
class MetricsRow:
    results_date: str
    sharepacks_root: str
    variant_label: str
    state: str
    outcome: str
    winner: str
    winner_canon: str
    winner_distinct_digits: int
    winner_vtrac_index: str
    candidates_total: int
    winner_rank: str
    canon_hit_top8: str
    canon_hit_top12: str
    canon_hit_top20: str
    index_hit_top8: str
    index_hit_top12: str
    index_hit_top20: str
    index_hit_only_top8: str
    index_hit_only_top12: str
    index_hit_only_top20: str
    box_cost_top8: str
    box_cost_top12: str
    box_cost_top20: str
    evidence_steps_csv: str


def _fmt_bool(value: bool) -> str:
    return "1" if value else "0"


def _fmt_int(value: Optional[int]) -> str:
    return "" if value is None else str(int(value))


def _fmt_float(value: Optional[float]) -> str:
    return "" if value is None else f"{value:.6f}"


def _build_ranked_candidates(
    *,
    rows: Sequence[StepRow],
    candidate_cache: Dict[Tuple[str, ...], CandidateSets],
    cfg: VariantConfig,
) -> List[Tuple[str, float]]:
    scores: Dict[str, float] = {}
    for r in rows:
        if r.unique_digits <= 0 or r.unique_digits > cfg.max_unique_digits:
            continue
        if cfg.step_power:
            step_w = 1.0 / ((1 + r.step) ** cfg.step_power)
        else:
            step_w = 1.0
        if cfg.unique_power:
            uniq_w = 1.0 / (r.unique_digits**cfg.unique_power)
        else:
            uniq_w = 1.0
        base = step_w * uniq_w

        sets = candidate_cache.get(r.digits)
        if sets is None:
            sets = _candidate_sets_for_digits(r.digits)
            candidate_cache[r.digits] = sets

        if sets.singles:
            w = base
            if cfg.split_weight:
                w /= len(sets.singles)
            for c in sets.singles:
                scores[c] = scores.get(c, 0.0) + w

        if cfg.double_weight > 0 and sets.doubles:
            w = base * cfg.double_weight
            if cfg.split_weight:
                w /= len(sets.doubles)
            for c in sets.doubles:
                scores[c] = scores.get(c, 0.0) + w

        if sets.triples:
            w = base
            if cfg.split_weight:
                w /= len(sets.triples)
            for c in sets.triples:
                scores[c] = scores.get(c, 0.0) + w

    return sorted(scores.items(), key=lambda kv: (-kv[1], kv[0]))


def _box_cost_for_top(ranked: Sequence[Tuple[str, float]], k: int) -> int:
    total = 0
    for canon, _ in ranked[:k]:
        total += _boxed_cost_units(canon)
    return total


def _index_hit_for_top(*, ranked: Sequence[Tuple[str, float]], k: int, winner_index: Optional[int]) -> bool:
    if winner_index is None:
        return False
    for canon, _ in ranked[:k]:
        idx = vr.get_vtrac_index(canon)
        if idx == winner_index:
            return True
    return False


def _label_from_cfg(cfg: VariantConfig) -> str:
    parts = [
        f"u{cfg.max_unique_digits}",
        f"sp{cfg.step_power:g}",
        f"up{cfg.unique_power:g}",
        f"dw{cfg.double_weight:g}",
        "split" if cfg.split_weight else "nosplit",
    ]
    return "_".join(parts)


def _default_cfgs(args: argparse.Namespace) -> List[VariantConfig]:
    cfgs: List[VariantConfig] = []
    for max_u in args.max_unique_digits:
        for step_pow in args.step_powers:
            for uniq_pow in args.unique_powers:
                for dbl_w in args.double_weights:
                    cfg = VariantConfig(
                        label=f"dr_env_{max_u}_{step_pow:g}_{uniq_pow:g}_dw{dbl_w:g}{'_split' if args.split_weight else ''}",
                        max_unique_digits=int(max_u),
                        step_power=float(step_pow),
                        unique_power=float(uniq_pow),
                        double_weight=float(dbl_w),
                        split_weight=bool(args.split_weight),
                    )
                    cfgs.append(cfg)
    # stable ordering
    cfgs.sort(key=lambda c: _label_from_cfg(c))
    return cfgs


def _load_step_rows(*, steps_csv: Path, outcome: str) -> List[StepRow]:
    rows: List[StepRow] = []
    with steps_csv.open(newline="", encoding="utf-8", errors="replace") as f:
        r = csv.DictReader(f)
        for row in r:
            if (row.get("section") or "").strip() != outcome:
                continue
            val = "".join(ch for ch in (row.get("value") or "") if ch.isdigit())
            if not val:
                continue
            digits = tuple(sorted(set(val)))
            try:
                step = int((row.get("step") or "0").strip() or 0)
            except Exception:
                step = 0
            try:
                unique_digits = int((row.get("unique_digits") or "0").strip() or 0)
            except Exception:
                unique_digits = 0
            rows.append(StepRow(step=step, unique_digits=unique_digits, digits=digits))
    return rows


def _write_csv(path: Path, rows: Sequence[MetricsRow]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = list(MetricsRow.__annotations__.keys())
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({k: getattr(r, k) for k in fields})


def _summarize(rows: Sequence[MetricsRow], cfgs: Sequence[VariantConfig]) -> str:
    by_label: Dict[str, List[MetricsRow]] = {}
    for r in rows:
        by_label.setdefault(r.variant_label, []).append(r)

    lines: List[str] = []
    lines.append("# Digit Reduction — Envelope Harness (Reporting-Only)")
    lines.append("")
    lines.append("Purpose: evaluate DR as a digit-pool / early-arrival evidence source (selection-layer),")
    lines.append("using only `*_digit_reduction_steps.csv`, graded vs results.")
    lines.append("")
    lines.append("Notes:")
    lines.append("- `winner_vtrac_index` is boxed-family index (1–35) from `modules.vtrac_reference.get_vtrac_index` (triples have none).")
    lines.append("- `box_cost_topK` is a proxy if you fully BOX-close each canonical (6/3/1 lines).")
    lines.append("")
    lines.append("## Summary (all states, Midday+Evening)")
    lines.append("")
    lines.append("| variant | opps | canon@8 | canon@12 | canon@20 | idx@8 | idx@12 | idx@20 | idx_only@12 | avg_box_cost@12 |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|")

    for cfg in cfgs:
        label = _label_from_cfg(cfg)
        rs = by_label.get(label, [])
        if not rs:
            continue
        opps = len(rs)
        canon8 = sum(1 for r in rs if r.canon_hit_top8 == "1")
        canon12 = sum(1 for r in rs if r.canon_hit_top12 == "1")
        canon20 = sum(1 for r in rs if r.canon_hit_top20 == "1")
        idx8 = sum(1 for r in rs if r.index_hit_top8 == "1")
        idx12 = sum(1 for r in rs if r.index_hit_top12 == "1")
        idx20 = sum(1 for r in rs if r.index_hit_top20 == "1")
        idx_only12 = sum(1 for r in rs if r.index_hit_only_top12 == "1")
        avg_cost12 = sum(int(r.box_cost_top12 or "0") for r in rs) / max(1, opps)
        lines.append(
            f"| `{label}` | {opps} | {canon8/opps:.3f} | {canon12/opps:.3f} | {canon20/opps:.3f} | {idx8/opps:.3f} | {idx12/opps:.3f} | {idx20/opps:.3f} | {idx_only12/opps:.3f} | {avg_cost12:.1f} |"
        )

    lines.append("")
    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Digit Reduction envelope harness (reporting-only)")
    p.add_argument("--start", required=True, help="Start results date D (YYYY-MM-DD)")
    p.add_argument("--end", required=True, help="End results date D (YYYY-MM-DD)")
    p.add_argument("--states", nargs="*", help="Optional subset of states (default: tracked list)")
    p.add_argument(
        "--sharepacks-root",
        default=str(REPO_ROOT / "sharepacks"),
        help="Sharepacks root directory (default: sharepacks/)",
    )
    p.add_argument(
        "--max-unique-digits",
        nargs="*",
        type=int,
        default=[4, 5, 7, 9],
        help="Max unique digits in a DR step-value pool to include (default: 4 5 7 9)",
    )
    p.add_argument(
        "--step-powers",
        nargs="*",
        type=float,
        default=[1.0, 2.0],
        help="Step weighting power (default: 1.0 2.0); higher emphasizes early steps.",
    )
    p.add_argument(
        "--unique-powers",
        nargs="*",
        type=float,
        default=[1.0],
        help="Unique-digit weighting power (default: 1.0); higher emphasizes smaller pools.",
    )
    p.add_argument(
        "--double-weights",
        nargs="*",
        type=float,
        default=[0.0, 0.25, 1.0],
        help="Relative weight for double candidates generated from pools (default: 0,0.25,1.0)",
    )
    p.add_argument(
        "--split-weight",
        action="store_true",
        help="Distribute row weight across its candidate set (recommended; prevents 'winning by widening').",
    )
    p.add_argument(
        "--out-prefix",
        default=None,
        help="Override output basename under RUNS (default: DR_V0__ENVELOPE_HARNESS__<start>_to_<end>)",
    )
    return p.parse_args()


def main() -> None:
    args = parse_args()

    sharepacks_root = Path(args.sharepacks_root)
    if not sharepacks_root.is_absolute():
        sharepacks_root = (REPO_ROOT / sharepacks_root).resolve()

    states = list(args.states) if args.states else list(DEFAULT_STATES)
    dates = _iter_dates(args.start, args.end)
    cfgs = _default_cfgs(args)

    # Load winners for each date.
    winners_by_date: Dict[str, Dict[str, Dict[str, str]]] = {}
    for d in dates:
        winners_by_date[d] = _read_results_winners(d)

    all_rows: List[MetricsRow] = []
    candidate_cache: Dict[Tuple[str, ...], CandidateSets] = {}

    for d in dates:
        day_dir = sharepacks_root / d
        winners_for_day = winners_by_date.get(d, {})
        if not winners_for_day:
            continue

        for state in states:
            winners = winners_for_day.get(state, {})
            if not winners:
                continue
            steps_csv = _steps_csv_path(day_dir, state)
            if not steps_csv.exists():
                continue

            # Load outcome-specific rows once per (D,state).
            rows_by_outcome: Dict[str, List[StepRow]] = {}
            for outcome in ("Midday", "Evening"):
                if outcome not in winners:
                    continue
                rows_by_outcome[outcome] = _load_step_rows(steps_csv=steps_csv, outcome=outcome)

            for outcome, winner in sorted(winners.items(), key=lambda kv: kv[0]):
                if outcome not in rows_by_outcome:
                    continue
                w_canon = _canon(winner)
                if not w_canon:
                    continue
                w_dist = _winner_digits_count(winner)
                w_idx = vr.get_vtrac_index(w_canon)

                for cfg in cfgs:
                    label = _label_from_cfg(cfg)
                    ranked = _build_ranked_candidates(
                        rows=rows_by_outcome[outcome],
                        candidate_cache=candidate_cache,
                        cfg=cfg,
                    )
                    canonicals = [c for c, _ in ranked]
                    winner_rank: Optional[int] = None
                    for i, c in enumerate(canonicals, start=1):
                        if c == w_canon:
                            winner_rank = i
                            break

                    top8 = canonicals[:8]
                    top12 = canonicals[:12]
                    top20 = canonicals[:20]
                    canon_hit8 = w_canon in top8
                    canon_hit12 = w_canon in top12
                    canon_hit20 = w_canon in top20

                    idx_hit8 = _index_hit_for_top(ranked=ranked, k=8, winner_index=w_idx)
                    idx_hit12 = _index_hit_for_top(ranked=ranked, k=12, winner_index=w_idx)
                    idx_hit20 = _index_hit_for_top(ranked=ranked, k=20, winner_index=w_idx)

                    idx_only8 = bool(idx_hit8 and not canon_hit8)
                    idx_only12 = bool(idx_hit12 and not canon_hit12)
                    idx_only20 = bool(idx_hit20 and not canon_hit20)

                    row = MetricsRow(
                        results_date=d,
                        sharepacks_root=_safe_rel(sharepacks_root),
                        variant_label=label,
                        state=state,
                        outcome=outcome,
                        winner=str(winner),
                        winner_canon=w_canon,
                        winner_distinct_digits=str(w_dist),
                        winner_vtrac_index=str(w_idx) if w_idx is not None else "",
                        candidates_total=str(len(canonicals)),
                        winner_rank=_fmt_int(winner_rank),
                        canon_hit_top8=_fmt_bool(canon_hit8),
                        canon_hit_top12=_fmt_bool(canon_hit12),
                        canon_hit_top20=_fmt_bool(canon_hit20),
                        index_hit_top8=_fmt_bool(idx_hit8),
                        index_hit_top12=_fmt_bool(idx_hit12),
                        index_hit_top20=_fmt_bool(idx_hit20),
                        index_hit_only_top8=_fmt_bool(idx_only8),
                        index_hit_only_top12=_fmt_bool(idx_only12),
                        index_hit_only_top20=_fmt_bool(idx_only20),
                        box_cost_top8=str(_box_cost_for_top(ranked, 8)),
                        box_cost_top12=str(_box_cost_for_top(ranked, 12)),
                        box_cost_top20=str(_box_cost_for_top(ranked, 20)),
                        evidence_steps_csv=_safe_rel(steps_csv),
                    )
                    all_rows.append(row)

    out_prefix = args.out_prefix or f"DR_V0__ENVELOPE_HARNESS__{args.start}_to_{args.end}"
    out_csv = _runs_dir() / f"{out_prefix}.csv"
    out_md = _runs_dir() / f"{out_prefix}.md"
    _write_csv(out_csv, all_rows)
    out_md.write_text(_summarize(all_rows, cfgs), encoding="utf-8")

    print(f"Wrote: {_safe_rel(out_md)}")
    print(f"Wrote: {_safe_rel(out_csv)}")


if __name__ == "__main__":
    main()
