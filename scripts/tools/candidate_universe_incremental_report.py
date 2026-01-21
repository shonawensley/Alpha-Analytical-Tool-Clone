#!/usr/bin/env python3
"""
Candidate Universe incremental report (baseline vs experiment-tag).

Reporting-only:
- Reads: RUNS/*__CANDIDATE_UNIVERSE_GRADE*.csv
- Writes: RUNS/candidate_universe_incremental__<profile>__<tag>.{csv,md}

Goal: quantify incremental lift (and regressions) when adding an experiment-tagged
Candidate Universe build (e.g., DR-004) versus baseline.
"""

from __future__ import annotations

import argparse
import csv
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


REPO_ROOT = Path(__file__).resolve().parents[2]


def _runs_dir() -> Path:
    return REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"


def _safe_rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _truthy(value: str) -> bool:
    return str(value).strip() == "1"


def _safe_int(value: str) -> Optional[int]:
    v = (value or "").strip()
    if not v:
        return None
    try:
        return int(float(v))
    except Exception:
        return None


def _normalize_experiment_tag(value: str) -> str:
    raw = str(value or "").strip()
    if not raw:
        return ""
    raw = raw.replace(" ", "_")
    cleaned = re.sub(r"[^A-Za-z0-9_-]+", "", raw)
    cleaned = cleaned.strip("_-")
    if not cleaned:
        raise SystemExit(f"Invalid experiment tag: {value!r} (must contain A-Z/a-z/0-9/_/-)")
    return cleaned[:60]


def _extract_date_from_filename(path: Path) -> Optional[str]:
    m = re.match(r"^(\d{4}-\d{2}-\d{2})__", path.name)
    return m.group(1) if m else None


def _rate(n: int, d: int) -> str:
    return "" if d == 0 else f"{(n / d):.4f}"


def _winner_type(winner: str) -> str:
    w = str(winner or "").strip()
    if len(w) != 3 or not w.isdigit():
        return "unknown"
    a, b, c = w[0], w[1], w[2]
    if a == b == c:
        return "triple"
    if a == b or a == c or b == c:
        return "double"
    return "unique"


def _load_csv_rows(path: Path) -> List[Dict[str, str]]:
    with path.open("r", encoding="utf-8", errors="replace", newline="") as f:
        return list(csv.DictReader(f))


def _write_csv(path: Path, fieldnames: Sequence[str], rows: Sequence[Dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(fieldnames), extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow(r)


def _write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def _iter_grade_csvs(runs_dir: Path, *, profile: str, tag_suffix: str) -> List[Path]:
    if profile == "mixed":
        return sorted(runs_dir.glob(f"*__CANDIDATE_UNIVERSE_GRADE{tag_suffix}.csv"))
    return sorted(runs_dir.glob(f"*__CANDIDATE_UNIVERSE_GRADE__{profile}{tag_suffix}.csv"))


@dataclass(frozen=True)
class CaseKey:
    results_date: str
    state_key: str
    winner_label: str


@dataclass
class FocusAgg:
    packs: int = 0
    cost_units_sum: int = 0
    combos_sum: int = 0
    hit_any: int = 0
    box_hit: int = 0
    straight_hit: int = 0
    vtrac_index_hit: int = 0
    vtrac_index_hit_only: int = 0

    def add(self, row: Dict[str, str]) -> None:
        if _truthy(row.get("winner_missing", "")):
            return
        self.packs += 1
        self.cost_units_sum += int(_safe_int(row.get("cost_units", "") or "") or 0)
        self.combos_sum += int(_safe_int(row.get("combos_count", "") or "") or 0)
        self.hit_any = max(self.hit_any, 1 if _truthy(row.get("hit_any", "")) else 0)
        self.box_hit = max(self.box_hit, 1 if _truthy(row.get("box_hit", "")) else 0)
        self.straight_hit = max(self.straight_hit, 1 if _truthy(row.get("straight_hit", "")) else 0)
        self.vtrac_index_hit = max(self.vtrac_index_hit, 1 if _truthy(row.get("vtrac_index_hit", "")) else 0)
        self.vtrac_index_hit_only = max(
            self.vtrac_index_hit_only, 1 if _truthy(row.get("vtrac_index_hit_only", "")) else 0
        )


def _collect_union_rows(rows: Iterable[Dict[str, str]]) -> Dict[CaseKey, Dict[str, str]]:
    out: Dict[CaseKey, Dict[str, str]] = {}
    for r in rows:
        if _truthy(r.get("winner_missing", "")):
            continue
        if (r.get("pack_id") or "").strip() != "__UNION__":
            continue
        if (r.get("method_id") or "").strip() != "union":
            continue
        results_date = (r.get("results_date") or "").strip()
        state_key = (r.get("state_key") or "").strip()
        winner_label = (r.get("winner_label") or "").strip()
        if not results_date or not state_key or not winner_label:
            continue
        out[CaseKey(results_date=results_date, state_key=state_key, winner_label=winner_label)] = r
    return out


def _collect_focus_aggs(
    rows: Iterable[Dict[str, str]], *, method_prefix: str
) -> Dict[CaseKey, FocusAgg]:
    out: Dict[CaseKey, FocusAgg] = {}
    pfx = (method_prefix or "").strip()
    if not pfx:
        return out
    for r in rows:
        if _truthy(r.get("winner_missing", "")):
            continue
        if (r.get("pack_id") or "").strip() == "__UNION__":
            continue
        mid = (r.get("method_id") or "").strip()
        if not mid.startswith(pfx):
            continue
        results_date = (r.get("results_date") or "").strip()
        state_key = (r.get("state_key") or "").strip()
        winner_label = (r.get("winner_label") or "").strip()
        if not results_date or not state_key or not winner_label:
            continue
        key = CaseKey(results_date=results_date, state_key=state_key, winner_label=winner_label)
        out.setdefault(key, FocusAgg()).add(r)
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description="Incremental Candidate Universe report (baseline vs experiment-tag).")
    ap.add_argument(
        "--runs-dir",
        default=str(_runs_dir()),
        help="RUNS directory (default: docs/AAT9_KIT/FINAL VALIDATION/RUNS).",
    )
    ap.add_argument(
        "--profile",
        choices=["mixed", "tool_only", "profit_only"],
        default="tool_only",
        help="Ablation profile to compare (default: tool_only).",
    )
    ap.add_argument(
        "--experiment-tag",
        required=True,
        help="Experiment tag suffix selecting the experiment grade files (required).",
    )
    ap.add_argument(
        "--baseline-experiment-tag",
        default="",
        help="Optional baseline experiment tag (default: none / baseline).",
    )
    ap.add_argument(
        "--focus-method-prefix",
        default="digit_reduction_dr004",
        help="Optional method_id prefix to report as a focused contributor (default: digit_reduction_dr004).",
    )
    ap.add_argument(
        "--dates",
        nargs="*",
        default=None,
        help="Optional explicit list of results dates to include (default: infer from matching grade file pairs).",
    )
    ap.add_argument("--date-from", default="", help="Optional inclusive start date filter (YYYY-MM-DD).")
    ap.add_argument("--date-to", default="", help="Optional inclusive end date filter (YYYY-MM-DD).")
    ap.add_argument("--out-csv", default=None, help="Override output CSV path.")
    ap.add_argument("--out-md", default=None, help="Override output Markdown path.")
    args = ap.parse_args()

    runs_dir = Path(args.runs_dir)
    if not runs_dir.is_absolute():
        runs_dir = (REPO_ROOT / runs_dir).resolve()
    runs_dir.mkdir(parents=True, exist_ok=True)

    profile = str(args.profile or "tool_only").strip()
    exp_tag = _normalize_experiment_tag(args.experiment_tag)
    base_tag = _normalize_experiment_tag(args.baseline_experiment_tag)
    exp_suffix = f"__{exp_tag}" if exp_tag else ""
    base_suffix = f"__{base_tag}" if base_tag else ""

    if not exp_tag:
        raise SystemExit("--experiment-tag is required.")

    dates_filter: Optional[List[str]] = None
    if args.dates is not None and len(args.dates) > 0:
        dates_filter = [str(d).strip() for d in args.dates if str(d).strip()]

    date_from = str(args.date_from or "").strip()
    date_to = str(args.date_to or "").strip()

    base_files = _iter_grade_csvs(runs_dir, profile=profile, tag_suffix=base_suffix)
    if not base_files:
        raise SystemExit(
            f"No baseline grade CSVs found under: {_safe_rel(runs_dir)} (profile={profile}, tag={base_tag or '—'})"
        )

    paired: List[Tuple[str, Path, Path]] = []
    for base_path in base_files:
        d = _extract_date_from_filename(base_path)
        if not d:
            continue
        if dates_filter is not None and d not in dates_filter:
            continue
        if date_from and d < date_from:
            continue
        if date_to and d > date_to:
            continue
        exp_path = (
            runs_dir / f"{d}__CANDIDATE_UNIVERSE_GRADE{'' if profile == 'mixed' else f'__{profile}'}{exp_suffix}.csv"
        )
        if not exp_path.exists():
            continue
        paired.append((d, base_path, exp_path))

    if not paired:
        raise SystemExit(
            "No matching baseline/experiment grade CSV pairs found. "
            f"(profile={profile}, baseline={base_tag or '—'}, experiment={exp_tag})"
        )

    focus_prefix = str(args.focus_method_prefix or "").strip()

    rows_out: List[Dict[str, object]] = []
    missing_pairs: List[str] = []
    for d, base_path, exp_path in paired:
        base_rows = _load_csv_rows(base_path)
        exp_rows = _load_csv_rows(exp_path)

        base_union = _collect_union_rows(base_rows)
        exp_union = _collect_union_rows(exp_rows)
        focus_aggs = _collect_focus_aggs(exp_rows, method_prefix=focus_prefix)

        # Join on union keys.
        keys = sorted(set(base_union.keys()) & set(exp_union.keys()), key=lambda k: (k.results_date, k.state_key, k.winner_label))
        if not keys:
            missing_pairs.append(d)
            continue

        for k in keys:
            b = base_union[k]
            e = exp_union[k]
            winner = (e.get("winner") or b.get("winner") or "").strip()
            winner_canon = (e.get("winner_canonical") or b.get("winner_canonical") or "").strip()
            winner_idx = (e.get("winner_vtrac_index") or b.get("winner_vtrac_index") or "").strip()
            b_hit = 1 if _truthy(b.get("hit_any", "")) else 0
            e_hit = 1 if _truthy(e.get("hit_any", "")) else 0
            b_box = 1 if _truthy(b.get("box_hit", "")) else 0
            e_box = 1 if _truthy(e.get("box_hit", "")) else 0
            b_st = 1 if _truthy(b.get("straight_hit", "")) else 0
            e_st = 1 if _truthy(e.get("straight_hit", "")) else 0
            b_idx_hit = 1 if _truthy(b.get("vtrac_index_hit", "")) else 0
            e_idx_hit = 1 if _truthy(e.get("vtrac_index_hit", "")) else 0
            b_idx_only = 1 if _truthy(b.get("vtrac_index_hit_only", "")) else 0
            e_idx_only = 1 if _truthy(e.get("vtrac_index_hit_only", "")) else 0
            b_cost = int(_safe_int(b.get("cost_units", "") or "") or 0)
            e_cost = int(_safe_int(e.get("cost_units", "") or "") or 0)

            f = focus_aggs.get(k, FocusAgg())
            inc = 1 if (b_hit == 0 and e_hit == 1) else 0
            reg = 1 if (b_hit == 1 and e_hit == 0) else 0
            focus_sanity = "" if inc == 0 else ("ok" if f.hit_any == 1 else "missing")

            rows_out.append(
                {
                    "results_date": k.results_date,
                    "state_key": k.state_key,
                    "winner_label": k.winner_label,
                    "winner": winner,
                    "winner_canonical": winner_canon,
                    "winner_type": _winner_type(winner),
                    "winner_vtrac_index": winner_idx,
                    "base_hit_any": b_hit,
                    "exp_hit_any": e_hit,
                    "delta_hit_any": e_hit - b_hit,
                    "incremental_hit": inc,
                    "regression_hit": reg,
                    "base_straight_hit": b_st,
                    "exp_straight_hit": e_st,
                    "base_box_hit": b_box,
                    "exp_box_hit": e_box,
                    "base_vtrac_index_hit": b_idx_hit,
                    "exp_vtrac_index_hit": e_idx_hit,
                    "base_vtrac_index_only": b_idx_only,
                    "exp_vtrac_index_only": e_idx_only,
                    "base_cost_units": b_cost,
                    "exp_cost_units": e_cost,
                    "delta_cost_units": e_cost - b_cost,
                    "focus_method_prefix": focus_prefix,
                    "focus_packs": f.packs,
                    "focus_cost_units_sum": f.cost_units_sum,
                    "focus_hit_any": f.hit_any,
                    "focus_box_hit": f.box_hit,
                    "focus_straight_hit": f.straight_hit,
                    "focus_vtrac_index_hit": f.vtrac_index_hit,
                    "focus_vtrac_index_only": f.vtrac_index_hit_only,
                    "focus_sanity_if_incremental": focus_sanity,
                    "baseline_grade_csv": _safe_rel(base_path),
                    "experiment_grade_csv": _safe_rel(exp_path),
                }
            )

    if not rows_out:
        raise SystemExit("No union rows compared (pairs existed, but no joinable __UNION__ rows were found).")

    # Aggregate (overall + by (winner_label, winner_type)).
    def add_bucket(agg: Dict[str, int], r: Dict[str, object]) -> None:
        agg["rows"] = agg.get("rows", 0) + 1
        agg["base_hits"] = agg.get("base_hits", 0) + int(r.get("base_hit_any") or 0)
        agg["exp_hits"] = agg.get("exp_hits", 0) + int(r.get("exp_hit_any") or 0)
        agg["inc_hits"] = agg.get("inc_hits", 0) + int(r.get("incremental_hit") or 0)
        agg["reg_hits"] = agg.get("reg_hits", 0) + int(r.get("regression_hit") or 0)
        agg["delta_cost_sum"] = agg.get("delta_cost_sum", 0) + int(r.get("delta_cost_units") or 0)
        agg["base_cost_sum"] = agg.get("base_cost_sum", 0) + int(r.get("base_cost_units") or 0)
        agg["exp_cost_sum"] = agg.get("exp_cost_sum", 0) + int(r.get("exp_cost_units") or 0)

    overall: Dict[str, int] = {}
    by_bucket: Dict[Tuple[str, str], Dict[str, int]] = {}
    for r in rows_out:
        add_bucket(overall, r)
        bkey = (str(r.get("winner_label") or "Unknown"), str(r.get("winner_type") or "unknown"))
        add_bucket(by_bucket.setdefault(bkey, {}), r)

    rows_out.sort(key=lambda r: (str(r["results_date"]), str(r["state_key"]), str(r["winner_label"])))

    out_suffix = f"__from_{base_tag}__to_{exp_tag}" if base_tag else f"__{exp_tag}"
    out_profile = "" if profile == "mixed" else f"__{profile}"
    out_csv = (
        Path(args.out_csv)
        if args.out_csv
        else runs_dir / f"candidate_universe_incremental{out_profile}{out_suffix}.csv"
    )
    out_md = (
        Path(args.out_md)
        if args.out_md
        else runs_dir / f"candidate_universe_incremental{out_profile}{out_suffix}.md"
    )

    _write_csv(
        out_csv,
        fieldnames=[
            "results_date",
            "state_key",
            "winner_label",
            "winner",
            "winner_canonical",
            "winner_type",
            "winner_vtrac_index",
            "base_hit_any",
            "exp_hit_any",
            "delta_hit_any",
            "incremental_hit",
            "regression_hit",
            "base_straight_hit",
            "exp_straight_hit",
            "base_box_hit",
            "exp_box_hit",
            "base_vtrac_index_hit",
            "exp_vtrac_index_hit",
            "base_vtrac_index_only",
            "exp_vtrac_index_only",
            "base_cost_units",
            "exp_cost_units",
            "delta_cost_units",
            "focus_method_prefix",
            "focus_packs",
            "focus_cost_units_sum",
            "focus_hit_any",
            "focus_box_hit",
            "focus_straight_hit",
            "focus_vtrac_index_hit",
            "focus_vtrac_index_only",
            "focus_sanity_if_incremental",
            "baseline_grade_csv",
            "experiment_grade_csv",
        ],
        rows=rows_out,
    )

    def fmt_cost(v: int, n: int) -> str:
        return "" if n == 0 else f"{(v / n):.2f}"

    rows_n = int(overall.get("rows", 0))
    inc = int(overall.get("inc_hits", 0))
    reg = int(overall.get("reg_hits", 0))
    delta_cost_sum = int(overall.get("delta_cost_sum", 0))
    base_cost_sum = int(overall.get("base_cost_sum", 0))
    exp_cost_sum = int(overall.get("exp_cost_sum", 0))
    cost_per_inc = "" if inc == 0 else f"{(delta_cost_sum / inc):.2f}"

    # Small “drill list” for incremental/regression cases.
    inc_cases = [r for r in rows_out if int(r.get("incremental_hit") or 0) == 1]
    reg_cases = [r for r in rows_out if int(r.get("regression_hit") or 0) == 1]

    md: List[str] = []
    md.append("# Candidate Universe — Incremental Report\n")
    md.append("Reporting-only: compares `__UNION__` rows between baseline and experiment-tag grade outputs.\n")
    md.append("## Inputs\n")
    md.append(f"- RUNS dir: `{_safe_rel(runs_dir)}`")
    md.append(f"- Profile: `{profile}`")
    md.append(f"- Baseline tag: `{base_tag or '—'}`")
    md.append(f"- Experiment tag: `{exp_tag}`")
    md.append(f"- Focus method prefix: `{focus_prefix or '—'}`\n")
    md.append("## Summary (union hit_any)\n")
    md.append("| Rows | base hit_any | exp hit_any | incremental | regressions | avg base cost | avg exp cost | avg Δcost | Δcost / incremental |")
    md.append("|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
    md.append(
        "| "
        + " | ".join(
            [
                str(rows_n),
                _rate(int(overall.get("base_hits", 0)), rows_n),
                _rate(int(overall.get("exp_hits", 0)), rows_n),
                str(inc),
                str(reg),
                fmt_cost(base_cost_sum, rows_n),
                fmt_cost(exp_cost_sum, rows_n),
                fmt_cost(delta_cost_sum, rows_n),
                cost_per_inc,
            ]
        )
        + " |"
    )

    md.append("\n## Breakdown (winner_label × winner_type)\n")
    md.append("| winner_label | winner_type | Rows | base hit_any | exp hit_any | incremental | regressions | avg Δcost | Δcost / incremental |")
    md.append("|---|---|---:|---:|---:|---:|---:|---:|---:|")
    for (wl, wt) in sorted(by_bucket.keys()):
        a = by_bucket[(wl, wt)]
        n = int(a.get("rows", 0))
        if n == 0:
            continue
        inc_b = int(a.get("inc_hits", 0))
        delta_sum = int(a.get("delta_cost_sum", 0))
        md.append(
            f"| {wl} | {wt} | {n} | {_rate(int(a.get('base_hits', 0)), n)} | {_rate(int(a.get('exp_hits', 0)), n)} | "
            f"{inc_b} | {int(a.get('reg_hits', 0))} | {fmt_cost(delta_sum, n)} | {'' if inc_b == 0 else f'{(delta_sum / inc_b):.2f}'} |"
        )

    if inc_cases:
        md.append("\n## Incremental-hit cases (baseline miss → experiment hit)\n")
        md.append("| Date | State | Outcome | Winner | Winner type | focus_hit_any | focus_sanity | Δcost |")
        md.append("|---|---|---|---:|---|---:|---|---:|")
        for r in inc_cases[:50]:
            md.append(
                f"| {r['results_date']} | {r['state_key']} | {r['winner_label']} | {r['winner']} | {r['winner_type']} | "
                f"{r['focus_hit_any']} | {r['focus_sanity_if_incremental'] or ''} | {r['delta_cost_units']} |"
            )

    if reg_cases:
        md.append("\n## Regression cases (baseline hit → experiment miss)\n")
        md.append("| Date | State | Outcome | Winner | Winner type | Δcost |")
        md.append("|---|---|---|---:|---|---:|")
        for r in reg_cases[:50]:
            md.append(
                f"| {r['results_date']} | {r['state_key']} | {r['winner_label']} | {r['winner']} | {r['winner_type']} | {r['delta_cost_units']} |"
            )

    if missing_pairs:
        md.append("\n## Notes\n")
        md.append(f"- Some matched file pairs had no joinable `__UNION__` rows: `{', '.join(sorted(set(missing_pairs)))}`")

    md.append("\n## Outputs\n")
    md.append(f"- CSV: `{_safe_rel(out_csv)}`")
    md.append(f"- MD: `{_safe_rel(out_md)}`\n")

    _write_text(out_md, "\n".join(md))


if __name__ == "__main__":
    main()

