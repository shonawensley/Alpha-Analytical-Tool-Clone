#!/usr/bin/env python3
"""
Create a multi-state "glass box" trace bundle from an existing conversion casebook.

Why:
- Casebooks already curate representative outcomes by failure bucket.
- This tool turns those entries into clickable, per-outcome trace reports + an index
  so you can review multiple states without manually hunting artifacts.

Inputs:
- A casebook like:
  docs/AAT9_KIT/FINAL VALIDATION/RUNS/<A>_to_<B>__CONVERSION_CASEBOOK__tool_only__<strategy>__stable10__B36.md

Outputs:
- Many per-outcome trace files (via create_glass_box_trace_report.py default naming)
- One index markdown linking them:
  docs/AAT9_KIT/FINAL VALIDATION/RUNS/<A>_to_<B>__GLASS_BOX_TRACE_BUNDLE__tool_only__<strategy>__stable10__B36.md
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple


REPO_ROOT = Path(__file__).resolve().parents[2]
RUNS_DIR = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"
TRACE_SCRIPT = REPO_ROOT / "scripts" / "tools" / "create_glass_box_trace_report.py"


BUCKETS_ORDER = ["CU_MISS", "CU_LANE_BUT_PLAY_MISS", "CU_EXACT_BUT_PLAY_MISS", "HIT_INCLUSIVE"]


@dataclass(frozen=True)
class Case:
    bucket: str
    date: str
    state: str
    winner_label: str
    winner: str
    idx: str
    play_inclusive: str
    play_hit_any: str


def _parse_casebook_filename(path: Path) -> Dict[str, str]:
    """
    Best-effort parse of:
      <A>_to_<B>__CONVERSION_CASEBOOK__<profile>__<strategy>__<tag>__<budget>.md
    """
    stem = path.name
    if stem.endswith(".md"):
        stem = stem[: -len(".md")]
    parts = stem.split("__")
    if len(parts) < 6:
        return {}
    date_range, kind, profile, *rest = parts
    if kind != "CONVERSION_CASEBOOK":
        return {}
    m_range = re.match(r"^(?P<a>\d{4}-\d{2}-\d{2})_to_(?P<b>\d{4}-\d{2}-\d{2})$", date_range)
    if not m_range:
        return {}
    if len(rest) < 3:
        return {}
    strategy = rest[0]
    tag = rest[1]
    budget = rest[2]
    if not re.match(r"^B\d+$", budget):
        return {}
    return {"a": m_range.group("a"), "b": m_range.group("b"), "profile": profile, "strategy": strategy, "tag": tag, "budget": budget}


def _bucket_from_header(line: str) -> Optional[str]:
    m = re.match(r"^##\s+([A-Z0-9_]+)\s+\(\d+\)\s*$", line.strip())
    if not m:
        return None
    return m.group(1)


def _parse_case_line(bucket: str, line: str) -> Optional[Case]:
    # Example:
    # - `2026-01-15 OntarioCanada4 Midday` winner=`598` idx=`14` CU(...) Play(inclusive=1, hit_any=0) ...
    m = re.match(r"^- `([^`]+)`\s+winner=`([^`]+)`\s+idx=`([^`]+)`.*?Play\(inclusive=([01]),\s*hit_any=([01])\)", line.strip())
    if not m:
        return None
    header, winner, idx, play_inclusive, play_hit_any = m.groups()
    parts = header.strip().split()
    if len(parts) < 3:
        return None
    date = parts[0]
    state = parts[1]
    winner_label = parts[2]
    return Case(
        bucket=bucket,
        date=date,
        state=state,
        winner_label=winner_label,
        winner=winner,
        idx=idx,
        play_inclusive=play_inclusive,
        play_hit_any=play_hit_any,
    )


def load_cases(casebook: Path) -> List[Case]:
    cases: List[Case] = []
    current_bucket: Optional[str] = None
    for raw in casebook.read_text(encoding="utf-8", errors="replace").splitlines():
        b = _bucket_from_header(raw)
        if b:
            current_bucket = b
            continue
        if not current_bucket:
            continue
        if not raw.lstrip().startswith("- `"):
            continue
        c = _parse_case_line(current_bucket, raw)
        if c:
            cases.append(c)
    return cases


def _select_cases(cases: List[Case], *, max_per_bucket: int) -> List[Case]:
    by_bucket: Dict[str, List[Case]] = {b: [] for b in BUCKETS_ORDER}
    for c in cases:
        if c.bucket in by_bucket:
            by_bucket[c.bucket].append(c)

    selected: List[Case] = []

    for bucket in BUCKETS_ORDER:
        bucket_cases = by_bucket.get(bucket) or []
        if not bucket_cases:
            continue

        if bucket == "HIT_INCLUSIVE":
            strict = [c for c in bucket_cases if c.play_hit_any == "1"]
            lane_only = [c for c in bucket_cases if c.play_hit_any == "0"]
            ordered = (strict[:1] + lane_only[:1] + [c for c in bucket_cases if c not in strict[:1] and c not in lane_only[:1]])
        else:
            ordered = bucket_cases

        selected.extend(ordered[: max_per_bucket if max_per_bucket > 0 else len(ordered)])

    # Stable ordering for readability: bucket order then date/state/label.
    order_idx = {b: i for i, b in enumerate(BUCKETS_ORDER)}
    selected.sort(key=lambda c: (order_idx.get(c.bucket, 99), c.date, c.state, c.winner_label))
    return selected


def _run_trace(*, date: str, state: str, winner_label: str, profile: str, experiment_tag: str, strategy: str, budget: str) -> Path:
    cmd = [
        sys.executable,
        str(TRACE_SCRIPT),
        "--date",
        date,
        "--state",
        state,
        "--winner-label",
        winner_label,
        "--strategy",
        strategy,
        "--budget",
        budget,
        "--profile",
        profile,
        "--experiment-tag",
        experiment_tag,
    ]
    res = subprocess.run(cmd, cwd=str(REPO_ROOT), check=True, capture_output=True, text=True)
    out = (res.stdout or "").strip().splitlines()[-1].strip()
    if not out:
        raise RuntimeError("trace script produced no output path")
    p = Path(out)
    if not p.is_absolute():
        p = (REPO_ROOT / p).resolve()
    return p


def _bundle_out_path(*, date_from: str, date_to: str, profile: str, strategy: str, experiment_tag: str, budget: str) -> Path:
    return RUNS_DIR / f"{date_from}_to_{date_to}__GLASS_BOX_TRACE_BUNDLE__{profile}__{strategy}__{experiment_tag}__{budget}.md"


def main() -> None:
    ap = argparse.ArgumentParser(description="Create a glass-box trace bundle from an existing conversion casebook.")
    ap.add_argument("--casebook", required=True, help="Path to conversion casebook md.")
    ap.add_argument("--max-per-bucket", type=int, default=3, help="How many cases per bucket (default: 3).")
    ap.add_argument("--out", default=None, help="Override bundle index output path.")
    args = ap.parse_args()

    casebook = (REPO_ROOT / args.casebook).resolve() if not Path(args.casebook).is_absolute() else Path(args.casebook).resolve()
    if not casebook.exists():
        raise SystemExit(f"Missing casebook: {casebook}")

    meta = _parse_casebook_filename(casebook)
    if not meta:
        raise SystemExit(
            "Casebook filename did not match expected pattern. "
            "Expected: <A>_to_<B>__CONVERSION_CASEBOOK__<profile>__<strategy>__<tag>__<budget>.md"
        )

    date_from = meta["a"]
    date_to = meta["b"]
    profile = meta["profile"]
    strategy = meta["strategy"]
    experiment_tag = meta["tag"]
    budget = meta["budget"]

    all_cases = load_cases(casebook)
    if not all_cases:
        raise SystemExit(f"No cases parsed from: {casebook}")

    selected = _select_cases(all_cases, max_per_bucket=int(args.max_per_bucket))

    traces: List[Tuple[Case, Path]] = []
    for c in selected:
        trace_path = _run_trace(
            date=c.date,
            state=c.state,
            winner_label=c.winner_label,
            profile=profile,
            experiment_tag=experiment_tag,
            strategy=strategy,
            budget=budget,
        )
        traces.append((c, trace_path))

    out_path = Path(args.out) if args.out else _bundle_out_path(
        date_from=date_from,
        date_to=date_to,
        profile=profile,
        strategy=strategy,
        experiment_tag=experiment_tag,
        budget=budget,
    )
    if not out_path.is_absolute():
        out_path = (REPO_ROOT / out_path).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)

    # Build index markdown.
    rel_casebook = casebook.relative_to(REPO_ROOT) if casebook.is_relative_to(REPO_ROOT) else casebook
    lines: List[str] = []
    lines.append(f"# Glass‑Box Trace Bundle — {date_from}..{date_to}")
    lines.append("")
    lines.append("Purpose: a clickable multi-state review set (pulled from the conversion casebook buckets).")
    lines.append("")
    lines.append("Context:")
    lines.append(f"- Casebook: `{rel_casebook}`")
    lines.append(f"- Strategy: `{strategy}` @ `{budget}`")
    lines.append(f"- profile/tag: `{profile}` / `{experiment_tag}`")
    lines.append("")
    lines.append("How to use:")
    lines.append("- Read 1 bucket at a time (don’t mix failure modes).")
    lines.append("- For each trace, answer the 5 questions in `V0_3__PIPELINE_FLOW__GLASS_BOX.md`.")
    lines.append("")

    traces_by_bucket: Dict[str, List[Tuple[Case, Path]]] = {b: [] for b in BUCKETS_ORDER}
    for c, p in traces:
        traces_by_bucket.setdefault(c.bucket, []).append((c, p))

    for bucket in BUCKETS_ORDER:
        items = traces_by_bucket.get(bucket) or []
        if not items:
            continue
        lines.append(f"## {bucket} ({len(items)})")
        for c, p in items:
            rel = p.relative_to(REPO_ROOT) if p.is_relative_to(REPO_ROOT) else p
            extra = f"winner=`{c.winner}` idx=`{c.idx}` Play(inclusive={c.play_inclusive}, hit_any={c.play_hit_any})"
            lines.append(f"- `{c.date} {c.state} {c.winner_label}` → `{rel}` ({extra})")
        lines.append("")

    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", errors="replace")

    rel_out = out_path.relative_to(REPO_ROOT) if out_path.is_relative_to(REPO_ROOT) else out_path
    print(str(rel_out))


if __name__ == "__main__":
    main()
