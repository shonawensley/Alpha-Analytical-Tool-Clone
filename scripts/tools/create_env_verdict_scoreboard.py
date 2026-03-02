#!/usr/bin/env python3
"""
Create an env-verdict (post-results) scoreboard by joining:
- RUNS/corpus_summary.csv (human MV synthesis label: env_verdict)
- __PORTFOLIO_VS_RESULTS__*.csv (objective hit/near-miss metrics)

Primary use: quantify posture/regime behavior (tight vs noisy vs split) and compare
baseline vs dc1 conversion variants without drowning in per-day artifacts.

Important: `env_verdict` is *post-hoc* and is NOT a predictive claim.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


RowKey = Tuple[str, str, str]  # (date, state_key, period)


def _pct(numer: int, denom: int) -> float:
    return 0.0 if denom <= 0 else 100.0 * (numer / denom)


def _as_int(value: str) -> int:
    try:
        return int(value)
    except Exception:
        return 0


def _bucket_env_verdict(verdict: str) -> str:
    """
    Collapse many human labels into a small set.
    """
    v = (verdict or "").strip().lower()
    if not v:
        return "UNLABELED"

    if "split" in v or ("midday" in v and "evening" in v):
        return "SPLIT"

    if "unknown" in v:
        return "UNKNOWN"

    if (
        "weak" in v
        or "noisy" in v
        or "cautious" in v
        or "pass" in v
        or "low-confidence" in v
        or "mixed" in v
    ):
        return "WEAK_NOISY"

    if v.startswith("strong") or v == "playable" or v.startswith("playable"):
        return "STRONG"

    if v.startswith("support") or "support" in v:
        return "SUPPORT"

    return "OTHER"


@dataclass(frozen=True)
class Metrics:
    rows: int = 0
    straight: int = 0
    boxed_any: int = 0
    vtrac_index: int = 0
    cover_all_no_box: int = 0
    in_winner_index_sum: int = 0
    winner_is_double: int = 0

    def add_row(
        self,
        *,
        straight_hit: int,
        boxed_any_perm_hit: int,
        vtrac_index_hit: int,
        digit_cover_all_unique: int,
        in_winner_index: int,
        winner_is_double: int,
    ) -> "Metrics":
        cover_all_no_box = 1 if (digit_cover_all_unique == 1 and boxed_any_perm_hit == 0) else 0
        return Metrics(
            rows=self.rows + 1,
            straight=self.straight + (1 if straight_hit else 0),
            boxed_any=self.boxed_any + (1 if boxed_any_perm_hit else 0),
            vtrac_index=self.vtrac_index + (1 if vtrac_index_hit else 0),
            cover_all_no_box=self.cover_all_no_box + cover_all_no_box,
            in_winner_index_sum=self.in_winner_index_sum + in_winner_index,
            winner_is_double=self.winner_is_double + (1 if winner_is_double else 0),
        )

    def rate(self, numer: int) -> float:
        return _pct(numer, self.rows)

    def rate_str(self, numer: int) -> str:
        return f"{self.rate(numer):.1f}% ({numer}/{self.rows})"

    def avg_in_winner_index(self) -> float:
        return 0.0 if self.rows <= 0 else self.in_winner_index_sum / self.rows


def _load_env_map(corpus_summary_csv: Path) -> Dict[RowKey, str]:
    env: Dict[RowKey, str] = {}
    with corpus_summary_csv.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            key: RowKey = (row["date"], row["state"], row["period"])
            env[key] = (row.get("env_verdict") or "").strip()
    return env


def _iter_window_rows(window_csv: Path, *, budget_label: str) -> Iterable[dict]:
    with window_csv.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("winner_missing", "0") == "1":
                continue
            if row.get("budget_label") != budget_label:
                continue
            yield row


def _collect_metrics(
    window_csv: Path,
    *,
    env_map: Dict[RowKey, str],
    budget_label: str,
) -> Tuple[Dict[str, Metrics], int, int]:
    """
    Returns (metrics_by_bucket, rows_total, rows_labeled_nonempty).
    """
    by_bucket: Dict[str, Metrics] = {}
    total = 0
    labeled = 0

    for row in _iter_window_rows(window_csv, budget_label=budget_label):
        total += 1
        key: RowKey = (row["results_date"], row["state_key"], row["winner_label"])
        verdict = env_map.get(key, "")
        if verdict.strip():
            labeled += 1
        bucket = _bucket_env_verdict(verdict)

        prev = by_bucket.get(bucket, Metrics())
        by_bucket[bucket] = prev.add_row(
            straight_hit=_as_int(row.get("straight_hit", "0")),
            boxed_any_perm_hit=_as_int(row.get("boxed_any_perm_hit", "0")),
            vtrac_index_hit=_as_int(row.get("vtrac_index_hit", "0")),
            digit_cover_all_unique=_as_int(row.get("digit_cover_all_unique", "0")),
            in_winner_index=_as_int(row.get("in_winner_index", "0")),
            winner_is_double=_as_int(row.get("winner_is_double", "0")),
        )

    return by_bucket, total, labeled


def _ordered_buckets(keys: Sequence[str]) -> List[str]:
    preferred = ["STRONG", "SUPPORT", "WEAK_NOISY", "SPLIT", "UNKNOWN", "OTHER", "UNLABELED"]
    keyset = set(keys)
    ordered = [k for k in preferred if k in keyset] + sorted(k for k in keyset if k not in preferred)
    return ordered


def _merge_metrics(by_bucket: Dict[str, Metrics], buckets: Sequence[str]) -> Metrics:
    merged = Metrics()
    for b in buckets:
        m = by_bucket.get(b, Metrics())
        merged = Metrics(
            rows=merged.rows + m.rows,
            straight=merged.straight + m.straight,
            boxed_any=merged.boxed_any + m.boxed_any,
            vtrac_index=merged.vtrac_index + m.vtrac_index,
            cover_all_no_box=merged.cover_all_no_box + m.cover_all_no_box,
            in_winner_index_sum=merged.in_winner_index_sum + m.in_winner_index_sum,
            winner_is_double=merged.winner_is_double + m.winner_is_double,
        )
    return merged


def _delta_pp(base_rate: float, var_rate: float) -> float:
    return var_rate - base_rate


def _fmt_pp(x: float) -> str:
    return f"{x:+.1f}pp"


def _write_md(
    out_md: Path,
    *,
    budget_label: str,
    corpus_summary_csv: Path,
    windows: Sequence[Tuple[str, Path, Path]],
    env_map: Dict[RowKey, str],
) -> None:
    lines: List[str] = []
    lines.append(f"# Env Verdict Scoreboard — {budget_label} (baseline vs dc1)")
    lines.append("")
    lines.append("Purpose")
    lines.append("- Quantify outcomes by **post-hoc environment verdict** buckets (tight vs noisy vs split).")
    lines.append("- Compare baseline (`stable10`) vs `dc1` closure on the same rows (B36).")
    lines.append("")
    lines.append("Important")
    lines.append("- `env_verdict` comes from MV synthesis (`corpus_summary.csv`). It is **not a predictive claim**.")
    lines.append("- Use this to validate posture/regime claims (`E021/E009`): when conversion changes help and when they don’t.")
    lines.append("- `CoverAll+NoBoxPerm` is a **bad** metric (we had all 3 digits but picked no winning permutation). Lower is better.")
    lines.append("- `UNLABELED` means the MV `env_verdict` label is missing for that row (not “unknown regime”).")
    lines.append("")
    lines.append("Evidence inputs")
    lines.append(f"- Env labels: `{corpus_summary_csv.as_posix()}`")
    for label, base_csv, dc1_csv in windows:
        lines.append(f"- Window `{label}` baseline: `{base_csv.as_posix()}`")
        lines.append(f"- Window `{label}` dc1: `{dc1_csv.as_posix()}`")
    lines.append("")
    lines.append("Bucket mapping (collapsed)")
    lines.append("- `STRONG`: strong/playable days (often Stable exact boxed hits present)")
    lines.append("- `SUPPORT`: partial structure/support days")
    lines.append("- `WEAK_NOISY`: weak/noisy/cautious/mixed/pass/low-confidence days")
    lines.append("- `SPLIT`: explicitly split (Midday vs Evening differs)")
    lines.append("- `UNKNOWN` / `OTHER`: misc buckets")
    lines.append("- `UNLABELED`: missing MV label in `corpus_summary.csv` for that row")
    lines.append("")

    for label, base_csv, dc1_csv in windows:
        base_by_bucket, base_rows, base_labeled = _collect_metrics(
            base_csv, env_map=env_map, budget_label=budget_label
        )
        dc1_by_bucket, dc1_rows, dc1_labeled = _collect_metrics(
            dc1_csv, env_map=env_map, budget_label=budget_label
        )

        lines.append(f"## Window — {label}")
        lines.append("")
        lines.append(f"- Rows (winner-present, {budget_label}): baseline `{base_rows}`, dc1 `{dc1_rows}`")
        lines.append(
            f"- Rows with non-empty `env_verdict`: baseline `{base_labeled}` ({_pct(base_labeled, base_rows):.1f}%), dc1 `{dc1_labeled}` ({_pct(dc1_labeled, dc1_rows):.1f}%)"
        )
        if base_rows != dc1_rows:
            lines.append(
                f"- Warning: row count mismatch (baseline {base_rows} vs dc1 {dc1_rows}). Deltas may be misleading."
            )
        lines.append("")

        lines.append(
            "| Bucket | Rows | Straight (base→dc1) | Boxed(any perm) (base→dc1) | VTRAC idx hit (base→dc1) | CoverAll+NoBoxPerm (base→dc1) | Avg in-winner-index (base→dc1) | WinnerIsDouble% |"
        )
        lines.append("|---|---:|---|---|---|---|---|---:|")

        buckets = _ordered_buckets(list(set(base_by_bucket.keys()) | set(dc1_by_bucket.keys())))
        for bucket in buckets:
            b = base_by_bucket.get(bucket, Metrics())
            d = dc1_by_bucket.get(bucket, Metrics())
            if b.rows <= 0:
                continue

            straight = (
                f"{b.rate_str(b.straight)} → {d.rate_str(d.straight)} "
                f"({_fmt_pp(_delta_pp(b.rate(b.straight), d.rate(d.straight)))})"
            )
            boxed_any = (
                f"{b.rate_str(b.boxed_any)} → {d.rate_str(d.boxed_any)} "
                f"({_fmt_pp(_delta_pp(b.rate(b.boxed_any), d.rate(d.boxed_any)))})"
            )
            idx_hit = (
                f"{b.rate_str(b.vtrac_index)} → {d.rate_str(d.vtrac_index)} "
                f"({_fmt_pp(_delta_pp(b.rate(b.vtrac_index), d.rate(d.vtrac_index)))})"
            )
            cover_no_box = (
                f"{b.rate_str(b.cover_all_no_box)} → {d.rate_str(d.cover_all_no_box)} "
                f"({_fmt_pp(_delta_pp(b.rate(b.cover_all_no_box), d.rate(d.cover_all_no_box)))})"
            )
            avg_in_idx = (
                f"{b.avg_in_winner_index():.2f} → {d.avg_in_winner_index():.2f} "
                f"({(d.avg_in_winner_index() - b.avg_in_winner_index()):+.2f})"
            )
            winner_double_pct = f"{_pct(b.winner_is_double, b.rows):.1f}%"

            lines.append(
                f"| {bucket} | {b.rows} | {straight} | {boxed_any} | {idx_hit} | {cover_no_box} | {avg_in_idx} | {winner_double_pct} |"
            )

        # Collapsed totals
        strong_support = _merge_metrics(base_by_bucket, ["STRONG", "SUPPORT"])
        weakish = _merge_metrics(base_by_bucket, ["WEAK_NOISY", "OTHER", "UNKNOWN", "UNLABELED"])
        split = _merge_metrics(base_by_bucket, ["SPLIT"])
        all_total = _merge_metrics(base_by_bucket, buckets)

        def _collapse_row(name: str, base: Metrics, var: Metrics) -> str:
            if base.rows <= 0:
                return f"| {name} | 0 | - | - | - | - | - | - |"
            return (
                f"| {name} | {base.rows} | "
                f"{base.rate(base.straight):.1f}% → {var.rate(var.straight):.1f}% ({_fmt_pp(_delta_pp(base.rate(base.straight), var.rate(var.straight)))}) | "
                f"{base.rate(base.boxed_any):.1f}% → {var.rate(var.boxed_any):.1f}% ({_fmt_pp(_delta_pp(base.rate(base.boxed_any), var.rate(var.boxed_any)))}) | "
                f"{base.rate(base.vtrac_index):.1f}% → {var.rate(var.vtrac_index):.1f}% ({_fmt_pp(_delta_pp(base.rate(base.vtrac_index), var.rate(var.vtrac_index)))}) | "
                f"{base.rate(base.cover_all_no_box):.1f}% → {var.rate(var.cover_all_no_box):.1f}% ({_fmt_pp(_delta_pp(base.rate(base.cover_all_no_box), var.rate(var.cover_all_no_box)))}) | "
                f"{base.avg_in_winner_index():.2f} → {var.avg_in_winner_index():.2f} ({(var.avg_in_winner_index() - base.avg_in_winner_index()):+.2f}) | "
                f"{_pct(base.winner_is_double, base.rows):.1f}% |"
            )

        lines.append("")
        lines.append("### Collapsed totals (operator view)")
        lines.append("")
        lines.append(
            "| Collapsed bucket | Rows | Straight (base→dc1) | Boxed(any perm) (base→dc1) | VTRAC idx hit (base→dc1) | CoverAll+NoBoxPerm (base→dc1) | Avg in-winner-index (base→dc1) | WinnerIsDouble% |"
        )
        lines.append("|---|---:|---|---|---|---|---|---:|")

        # For collapse rows, we need dc1 metrics merged on the same bucket sets.
        dc1_strong_support = _merge_metrics(dc1_by_bucket, ["STRONG", "SUPPORT"])
        dc1_weakish = _merge_metrics(dc1_by_bucket, ["WEAK_NOISY", "OTHER", "UNKNOWN", "UNLABELED"])
        dc1_split = _merge_metrics(dc1_by_bucket, ["SPLIT"])
        dc1_all_total = _merge_metrics(dc1_by_bucket, buckets)

        lines.append(_collapse_row("TIGHT_TOTAL (STRONG+SUPPORT)", strong_support, dc1_strong_support))
        lines.append(_collapse_row("NOISY_TOTAL (WEAK+OTHER+…)", weakish, dc1_weakish))
        lines.append(_collapse_row("SPLIT_TOTAL", split, dc1_split))
        lines.append(_collapse_row("ALL_TOTAL", all_total, dc1_all_total))
        lines.append("")

    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _write_csv(
    out_csv: Path,
    *,
    budget_label: str,
    windows: Sequence[Tuple[str, Path, Path]],
    env_map: Dict[RowKey, str],
) -> None:
    out_csv.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "window",
        "bucket",
        "rows",
        "base_straight_pct",
        "dc1_straight_pct",
        "delta_straight_pp",
        "base_boxed_any_pct",
        "dc1_boxed_any_pct",
        "delta_boxed_any_pp",
        "base_vtrac_idx_pct",
        "dc1_vtrac_idx_pct",
        "delta_vtrac_idx_pp",
        "base_cover_all_no_box_pct",
        "dc1_cover_all_no_box_pct",
        "delta_cover_all_no_box_pp",
        "base_avg_in_winner_index",
        "dc1_avg_in_winner_index",
        "delta_avg_in_winner_index",
        "winner_is_double_pct",
    ]

    with out_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for label, base_csv, dc1_csv in windows:
            base_by_bucket, _, _ = _collect_metrics(base_csv, env_map=env_map, budget_label=budget_label)
            dc1_by_bucket, _, _ = _collect_metrics(dc1_csv, env_map=env_map, budget_label=budget_label)
            buckets = _ordered_buckets(list(set(base_by_bucket.keys()) | set(dc1_by_bucket.keys())))

            for bucket in buckets:
                b = base_by_bucket.get(bucket, Metrics())
                d = dc1_by_bucket.get(bucket, Metrics())
                if b.rows <= 0:
                    continue

                base_straight = b.rate(b.straight)
                dc1_straight = d.rate(d.straight)
                base_boxed_any = b.rate(b.boxed_any)
                dc1_boxed_any = d.rate(d.boxed_any)
                base_idx = b.rate(b.vtrac_index)
                dc1_idx = d.rate(d.vtrac_index)
                base_cover = b.rate(b.cover_all_no_box)
                dc1_cover = d.rate(d.cover_all_no_box)

                writer.writerow(
                    {
                        "window": label,
                        "bucket": bucket,
                        "rows": b.rows,
                        "base_straight_pct": f"{base_straight:.3f}",
                        "dc1_straight_pct": f"{dc1_straight:.3f}",
                        "delta_straight_pp": f"{(dc1_straight - base_straight):+.3f}",
                        "base_boxed_any_pct": f"{base_boxed_any:.3f}",
                        "dc1_boxed_any_pct": f"{dc1_boxed_any:.3f}",
                        "delta_boxed_any_pp": f"{(dc1_boxed_any - base_boxed_any):+.3f}",
                        "base_vtrac_idx_pct": f"{base_idx:.3f}",
                        "dc1_vtrac_idx_pct": f"{dc1_idx:.3f}",
                        "delta_vtrac_idx_pp": f"{(dc1_idx - base_idx):+.3f}",
                        "base_cover_all_no_box_pct": f"{base_cover:.3f}",
                        "dc1_cover_all_no_box_pct": f"{dc1_cover:.3f}",
                        "delta_cover_all_no_box_pp": f"{(dc1_cover - base_cover):+.3f}",
                        "base_avg_in_winner_index": f"{b.avg_in_winner_index():.3f}",
                        "dc1_avg_in_winner_index": f"{d.avg_in_winner_index():.3f}",
                        "delta_avg_in_winner_index": f"{(d.avg_in_winner_index() - b.avg_in_winner_index()):+.3f}",
                        "winner_is_double_pct": f"{_pct(b.winner_is_double, b.rows):.3f}",
                    }
                )


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out-md", required=True, help="Output markdown path.")
    parser.add_argument("--out-csv", default="", help="Optional output CSV path.")
    parser.add_argument(
        "--corpus-summary",
        default="docs/AAT9_KIT/FINAL VALIDATION/RUNS/corpus_summary.csv",
        help="Path to corpus_summary.csv (env_verdict labels).",
    )
    parser.add_argument("--budget", default="B36", help="Budget label to score (default: B36).")
    parser.add_argument(
        "--window",
        action="append",
        required=True,
        help="Window triple: LABEL:BASE_CSV:DC1_CSV",
    )
    args = parser.parse_args(argv)

    corpus_summary_csv = Path(args.corpus_summary)
    out_md = Path(args.out_md)
    out_csv = Path(args.out_csv) if args.out_csv else None
    budget_label = args.budget

    env_map = _load_env_map(corpus_summary_csv)

    windows: List[Tuple[str, Path, Path]] = []
    for spec in args.window:
        parts = spec.split(":")
        if len(parts) != 3:
            raise SystemExit(f"Invalid --window spec: {spec} (expected LABEL:BASE:DC1)")
        label, base_csv, dc1_csv = parts
        windows.append((label, Path(base_csv), Path(dc1_csv)))

    _write_md(
        out_md,
        budget_label=budget_label,
        corpus_summary_csv=corpus_summary_csv,
        windows=windows,
        env_map=env_map,
    )

    if out_csv is not None:
        _write_csv(out_csv, budget_label=budget_label, windows=windows, env_map=env_map)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
