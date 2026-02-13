#!/usr/bin/env python3
"""
Export a manageable, upload-friendly "research pack" for deep analysis (e.g. ChatGPT Pro).

Goal: include the highest-value evidence surfaces (winners lens + run reports + Aux summary
and bounded Digit Reduction overlays) without copying full sharepacks (which can be huge).

This script is reporting-only. It does not modify analyzers or sharepacks; it only copies
selected files into an export folder (recommended: under sharepacks/_scratch/).

Modes:
  - window: export all states for a date window (can be large).
  - curated: export a small set of high-signal cases (recommended).

Examples:
  # Curated pack for a window (recommended)
  python3 scripts/tools/export_chatgpt_research_pack.py \\
    --start-date 2026-01-05 --end-date 2026-01-09 --mode curated --include-predictive --zip

  # Full window pack (all states; can be big)
  python3 scripts/tools/export_chatgpt_research_pack.py \\
    --start-date 2026-01-05 --end-date 2026-01-09 --mode window --zip

Notes:
  - Some predictive artifacts are experiment-tagged (e.g. stable10):
      sharepacks/_predictive/<D>/<STATE>/candidate_universe__tool_only__stable10.json
    Use --experiment-tag stable10 to copy those files into the export.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
import sys
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Set, Tuple

REPO_ROOT = Path(__file__).resolve().parents[2]
RUNS_DIR = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"
FINAL_DOCS_DIR = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "final docs"


@dataclass(frozen=True)
class Case:
    date: str
    state: str


def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Export a bounded evidence pack for deep research (winners lens + RUNS + Aux + DR overlays)."
    )

    p.add_argument("--mode", choices=("curated", "window"), default="curated")
    p.add_argument(
        "--experiment-tag",
        default=None,
        help=(
            "Optional experiment tag for predictive artifacts (e.g. stable10). "
            "When set, the exporter will prefer candidate_universe/play_card filenames that include the tag."
        ),
    )
    p.add_argument(
        "--extra-window",
        action="append",
        default=[],
        help=(
            "Also copy window-level RUNS docs for these start:end date ranges (YYYY-MM-DD:YYYY-MM-DD). "
            "Repeatable. Useful when your pack needs an OOS guardrail window in addition to the main dates."
        ),
    )
    p.add_argument(
        "--include-path",
        action="append",
        default=[],
        help=(
            "Additional repo-relative file or directory to copy into the export (repeatable). "
            "Useful to include a PACKAGES/* prompt bundle alongside the exported RUNS/sharepacks artifacts."
        ),
    )

    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--dates", nargs="+", help="Explicit results dates D (YYYY-MM-DD)")
    g.add_argument("--start-date", help="Start results date D (YYYY-MM-DD)")
    p.add_argument("--end-date", default=None, help="End results date D (YYYY-MM-DD) (required with --start-date)")

    p.add_argument(
        "--states",
        nargs="*",
        default=None,
        help="Optional explicit state keys (default: infer from sharepacks/<D>/ directories)",
    )
    p.add_argument(
        "--out",
        default=None,
        help="Output directory (default: sharepacks/_scratch/chatgpt_research_pack_<stamp>/)",
    )
    p.add_argument("--zip", action="store_true", help="Also create a .zip archive next to the folder.")

    p.add_argument("--include-predictive", action="store_true", help="Also copy predictive artifacts (sharepacks/_predictive).")
    p.add_argument(
        "--profile",
        choices=("mixed", "tool_only", "profit_only"),
        default="mixed",
        help=(
            "Ablation profile for predictive artifacts + profile-scoped RUNS exports (default: mixed). "
            "tool_only = exclude Profit Alerts derived packs; profit_only = Profit Alerts derived packs only."
        ),
    )
    p.add_argument(
        "--include-control-center",
        action="store_true",
        help="Copy sharepacks/<D>/control_center boards (filtered; see flags).",
    )
    p.add_argument(
        "--include-profit-alerts",
        action="store_true",
        help="Include Profit Alerts files when exporting control_center (default: excluded).",
    )
    p.add_argument(
        "--include-tables",
        action="store_true",
        help="Also copy tables/ and json/*_tables.json snapshots for selected cases (default: off; can be large).",
    )
    p.add_argument(
        "--include-final-docs",
        action="store_true",
        default=True,
        help="Include key SSOT docs (final docs portal + CODEX_READ_FIRST + VTRAC reference).",
    )

    # curated selectors
    p.add_argument(
        "--max-convergence-cases",
        type=int,
        default=20,
        help="Curated mode: include up to N top convergence cases (default: 20).",
    )
    p.add_argument(
        "--max-doubles-queue",
        type=int,
        default=30,
        help="Curated mode: include up to N entries from Doubles study queue (default: 30).",
    )
    p.add_argument(
        "--max-profit-alerts-cases",
        type=int,
        default=0,
        help=(
            "Curated mode: include up to N Profit Alerts cases (HIT rows first, then higher strength). "
            "Default: 0 (disabled)."
        ),
    )
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would be copied (no filesystem writes).",
    )

    args = p.parse_args()
    if args.start_date and not args.end_date:
        p.error("--end-date is required when using --start-date")
    return args


def _date_range_inclusive(start: str, end: str) -> List[str]:
    ds = datetime.strptime(start, "%Y-%m-%d").date()
    de = datetime.strptime(end, "%Y-%m-%d").date()
    if de < ds:
        raise SystemExit(f"end-date {end} is before start-date {start}")
    dates: List[str] = []
    cur = ds
    while cur <= de:
        dates.append(cur.strftime("%Y-%m-%d"))
        cur += timedelta(days=1)
    return dates


def _infer_states_from_day(day_dir: Path) -> List[str]:
    if not day_dir.exists():
        return []
    states: List[str] = []
    for entry in day_dir.iterdir():
        if not entry.is_dir():
            continue
        name = entry.name
        if name.endswith("4"):
            states.append(name)
    return sorted(states)


def _copy_file(src: Path, dest: Path, *, dry_run: bool, manifest_rows: List[Dict[str, object]]) -> None:
    if not src.exists() or not src.is_file():
        manifest_rows.append({"status": "missing", "src": str(src), "dest": str(dest), "bytes": 0})
        return
    if dry_run:
        manifest_rows.append({"status": "would_copy", "src": str(src), "dest": str(dest), "bytes": src.stat().st_size})
        return
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)
    manifest_rows.append({"status": "copied", "src": str(src), "dest": str(dest), "bytes": src.stat().st_size})


def _copy_glob(
    src_dir: Path,
    dest_dir: Path,
    patterns: Sequence[str],
    *,
    dry_run: bool,
    manifest_rows: List[Dict[str, object]],
    allow_empty: bool = True,
) -> None:
    matched: List[Path] = []
    for pattern in patterns:
        matched.extend(sorted(src_dir.glob(pattern)))
    matched = [p for p in matched if p.is_file()]
    if not matched and not allow_empty:
        manifest_rows.append({"status": "missing_dir_or_pattern", "src": str(src_dir), "dest": str(dest_dir), "bytes": 0})
        return
    for src in matched:
        rel = src.relative_to(src_dir)
        _copy_file(src, dest_dir / rel, dry_run=dry_run, manifest_rows=manifest_rows)


def _copy_tree(src_dir: Path, dest_dir: Path, *, dry_run: bool, manifest_rows: List[Dict[str, object]]) -> None:
    if not src_dir.exists() or not src_dir.is_dir():
        manifest_rows.append({"status": "missing", "src": str(src_dir), "dest": str(dest_dir), "bytes": 0})
        return
    for src in sorted(src_dir.rglob("*")):
        if not src.is_file():
            continue
        rel = src.relative_to(src_dir)
        _copy_file(src, dest_dir / rel, dry_run=dry_run, manifest_rows=manifest_rows)


def _write_candidate_universe_md_from_payload(*, out_path: Path, payload: Dict[str, object]) -> None:
    def short_list(items: Sequence[object], limit: int = 8) -> str:
        xs = [str(x) for x in items if str(x)]
        if len(xs) <= limit:
            return ", ".join(xs)
        return ", ".join(xs[:limit]) + f", …(+{len(xs) - limit})"

    state_key = str(payload.get("state_key") or "?")
    results_date = str(payload.get("results_date") or "?")
    history_date = str(payload.get("history_date") or "-")
    generated_at = str(payload.get("generated_at") or "-")
    inputs_hash = str(payload.get("inputs_hash") or "-")
    packs = payload.get("packs") or []
    union_count = int(payload.get("union_combos_count") or 0)
    leakage = bool(payload.get("contains_winners_artifacts"))
    leakage_issues = payload.get("leakage_issues") or []

    lines: List[str] = []
    lines.append(f"# Candidate Universe — {state_key} — D={results_date}")
    lines.append("")
    lines.append("This is a **pre-results** playset artifact (gradeable later).")
    lines.append("")
    lines.append("## Meta")
    lines.append("")
    lines.append(f"- generated_at: `{generated_at}`")
    lines.append(f"- history_date (H): `{history_date}`")
    lines.append(f"- results_date (D): `{results_date}`")
    lines.append(f"- inputs_hash: `{inputs_hash}`")
    lines.append(f"- packs: `{len(packs) if isinstance(packs, list) else 0}`")
    lines.append(f"- union_combos_count: `{union_count}`")
    lines.append("")
    lines.append("## Leakage")
    lines.append("")
    lines.append(f"- contains_winners_artifacts: `{str(leakage).lower()}`")
    if leakage_issues:
        for issue in leakage_issues:
            lines.append(f"- issue: `{issue}`")
    else:
        lines.append("- issues: none")
    lines.append("")
    lines.append("## Packs")
    lines.append("")

    if isinstance(packs, list):
        for p in packs:
            if not isinstance(p, dict):
                continue
            pack_id = str(p.get("pack_id") or "?")
            method_id = str(p.get("method_id") or "?")
            variant = str(p.get("variant") or "Unknown")
            play_mode = str(p.get("play_mode") or "Unknown")
            combos = p.get("combos") or []
            canonicals = p.get("canonicals") or []
            why_tags = p.get("why_tags") or []
            evidence_paths = p.get("evidence_paths") or []
            lines.append(f"### `{pack_id}`")
            lines.append("")
            lines.append(f"- method_id: `{method_id}`")
            lines.append(f"- variant: `{variant}`")
            lines.append(f"- play_mode: `{play_mode}`")
            lines.append(f"- combos_count: `{int(p.get('combos_count') or 0)}`")
            lines.append(f"- cost_units: `{int(p.get('cost_units') or 0)}`")
            if canonicals:
                lines.append(f"- canonicals: {short_list(canonicals, limit=12)}")
            if why_tags:
                lines.append(f"- why_tags: {short_list(why_tags, limit=12)}")
            if evidence_paths:
                lines.append(f"- evidence_paths: {short_list(evidence_paths, limit=8)}")
            if combos:
                lines.append(f"- combos(sample): {short_list(combos, limit=18)}")
            lines.append("")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def _generate_candidate_universe_md(
    src_json: Path,
    dest_md: Path,
    *,
    dry_run: bool,
    manifest_rows: List[Dict[str, object]],
) -> None:
    if not src_json.exists() or not src_json.is_file():
        manifest_rows.append({"status": "missing", "src": str(src_json), "dest": str(dest_md), "bytes": 0})
        return
    if dry_run:
        manifest_rows.append({"status": "would_generate", "src": str(src_json), "dest": str(dest_md), "bytes": 0})
        return
    payload = json.loads(src_json.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise SystemExit(f"Unexpected candidate_universe payload type: {type(payload)} ({src_json})")
    _write_candidate_universe_md_from_payload(out_path=dest_md, payload=payload)
    manifest_rows.append({"status": "generated", "src": str(src_json), "dest": str(dest_md), "bytes": dest_md.stat().st_size})


def _read_convergence_cases_csv(path: Path, *, max_rows: int) -> List[Case]:
    if not path.exists():
        return []
    rows: List[Tuple[float, Case]] = []
    with path.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            try:
                score = float(row.get("convergence_score") or 0.0)
            except ValueError:
                score = 0.0
            date = (row.get("date") or "").strip()
            state = (row.get("state") or "").strip()
            if not date or not state:
                continue
            rows.append((score, Case(date=date, state=state)))
    rows.sort(key=lambda t: t[0], reverse=True)
    cases: List[Case] = []
    seen: Set[Tuple[str, str]] = set()
    for _, c in rows:
        key = (c.date, c.state)
        if key in seen:
            continue
        seen.add(key)
        cases.append(c)
        if len(cases) >= max_rows:
            break
    return cases


def _read_doubles_study_queue(path: Path, *, max_rows: int) -> List[Case]:
    if not path.exists():
        return []
    cases: List[Case] = []
    seen: Set[Tuple[str, str]] = set()
    # Table lines look like: | 1 | 2026-01-09 | Delaware4 | Evening | ...
    pat = re.compile(r"^\|\s*\d+\s*\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*([A-Za-z]+4)\s*\|")
    with path.open(encoding="utf-8") as f:
        for line in f:
            m = pat.match(line)
            if not m:
                continue
            date, state = m.group(1), m.group(2)
            key = (date, state)
            if key in seen:
                continue
            seen.add(key)
            cases.append(Case(date=date, state=state))
            if len(cases) >= max_rows:
                break
    return cases


def _profit_alerts_status_priority(status: str) -> int:
    s = (status or "").strip().upper()
    if s == "HIT":
        return 0
    if s == "EXPIRED":
        return 1
    if s == "CENSORED":
        return 2
    if s == "ACTIVE":
        return 3
    return 9


def _read_profit_alerts_cases_for_dates(*, dates: List[str], max_rows: int) -> List[Case]:
    if max_rows <= 0 or not dates:
        return []
    rows: List[Tuple[int, float, Case]] = []
    for d in dates:
        eval_path = REPO_ROOT / "sharepacks" / d / "control_center" / "profit_alerts_eval.csv"
        if not eval_path.exists():
            continue
        try:
            with eval_path.open(newline="", encoding="utf-8") as f:
                for row in csv.DictReader(f):
                    state_key = (row.get("state_key") or "").strip()
                    if not state_key:
                        continue
                    status = (row.get("status") or "").strip()
                    try:
                        strength = float(row.get("strength") or 0.0)
                    except ValueError:
                        strength = 0.0
                    rows.append(
                        (_profit_alerts_status_priority(status), -strength, Case(date=d, state=state_key))
                    )
        except Exception:
            continue

    rows.sort(key=lambda t: (t[0], t[1]))
    cases: List[Case] = []
    seen: Set[Tuple[str, str]] = set()
    for _, __, c in rows:
        key = (c.date, c.state)
        if key in seen:
            continue
        seen.add(key)
        cases.append(c)
        if len(cases) >= max_rows:
            break
    return cases


def _select_cases(args: argparse.Namespace, dates: List[str], *, states_filter: Optional[Set[str]]) -> Dict[str, Set[str]]:
    if args.mode == "window":
        mapping: Dict[str, Set[str]] = {}
        for date in dates:
            mapping[date] = set(states_filter or [])
        return mapping

    # curated
    selected: Set[Tuple[str, str]] = set()

    # Profit Alerts HIT/high-strength cases (optional; disabled by default)
    for c in _read_profit_alerts_cases_for_dates(dates=dates, max_rows=int(args.max_profit_alerts_cases or 0)):
        if c.date not in dates:
            continue
        if states_filter and c.state not in states_filter:
            continue
        selected.add((c.date, c.state))

    # Doubles/Mirror-doubles queue
    for c in _read_doubles_study_queue(
        RUNS_DIR / "DOUBLES_MIRROR_DOUBLES__STUDY_QUEUE.md", max_rows=args.max_doubles_queue
    ):
        if c.date not in dates:
            continue
        if states_filter and c.state not in states_filter:
            continue
        selected.add((c.date, c.state))

    # Convergence cases (prefer exact window filename if present)
    conv_path = None
    if dates:
        conv_candidate = RUNS_DIR / f"{dates[0]}_to_{dates[-1]}__CONVERGENCE_CASES.csv"
        if conv_candidate.exists():
            conv_path = conv_candidate
    if conv_path is None:
        # fallback: any convergence cases file for the window; take the first that matches date range naming
        for p in sorted(RUNS_DIR.glob("*__CONVERGENCE_CASES.csv")):
            conv_path = p
            break
    if conv_path:
        for c in _read_convergence_cases_csv(conv_path, max_rows=args.max_convergence_cases):
            if c.date not in dates:
                continue
            if states_filter and c.state not in states_filter:
                continue
            selected.add((c.date, c.state))

    mapping: Dict[str, Set[str]] = {}
    for date, state in sorted(selected):
        mapping.setdefault(date, set()).add(state)
    return mapping


def _copy_runs_docs(
    dates: List[str],
    export_root: Path,
    *,
    profile: str,
    extra_windows: Sequence[Tuple[str, str]],
    dry_run: bool,
    manifest_rows: List[Dict[str, object]],
) -> None:
    dest_runs = export_root / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"
    profile = str(profile or "mixed").strip()
    rollup_suffix = "" if profile == "mixed" else f"__{profile}"

    # Global navigation + synthesis docs (small, and critical for context)
    always = [
        "PORTAL.md",
        "INDEX.md",
        "FIX_LATER_INDEX.md",
        "SUPERBRAIN_ROADMAP.md",
        "SUPERBRAIN_V0_2__DEFAULTS.md",
        "V0_2__INTEGRATION_LOG.md",
        "V0_3__GLOSSARY__PREDICTIVE_SEMANTICS.md",
        "V0_3__PIPELINE_FLOW__GLASS_BOX.md",
        "V0_3__PREDICTIVE_POLICY__tool_only__stable10.md",
        "DEEP_ANALYSIS_CODEX_VALUABLE_INSIGHTS.md",
        "SUPERBRAIN_V0__SYNTHESIS_SPRINT.md",
        "SUPERBRAIN_V0__GOLD_EXTRACTION.md",
        "DOUBLES_MIRROR_DOUBLES__INVENTORY.md",
        "DOUBLES_MIRROR_DOUBLES__INVENTORY.csv",
        "DOUBLES_MIRROR_DOUBLES__DEEP_DIVE.md",
        "DOUBLES_MIRROR_DOUBLES__STUDY_QUEUE.md",
        f"candidate_universe_rollup{rollup_suffix}.md",
        f"candidate_universe_rollup{rollup_suffix}.csv",
        f"play_card_rollup{rollup_suffix}.md",
        f"play_card_rollup{rollup_suffix}.csv",
    ]
    for fname in always:
        _copy_file(RUNS_DIR / fname, dest_runs / fname, dry_run=dry_run, manifest_rows=manifest_rows)

    # Window-level corpus docs that match the requested date range(s)
    if dates:
        window_prefix = f"{dates[0]}_to_{dates[-1]}__"
        for path in sorted(RUNS_DIR.glob(f"{window_prefix}*")):
            if path.is_file():
                if profile == "tool_only" and "profit_alert" in path.name.lower():
                    continue
                _copy_file(path, dest_runs / path.name, dry_run=dry_run, manifest_rows=manifest_rows)

    # Optional extra windows (e.g., an OOS guardrail window)
    for start, end in extra_windows:
        window_prefix = f"{start}_to_{end}__"
        for path in sorted(RUNS_DIR.glob(f"{window_prefix}*")):
            if path.is_file():
                if profile == "tool_only" and "profit_alert" in path.name.lower():
                    continue
                _copy_file(path, dest_runs / path.name, dry_run=dry_run, manifest_rows=manifest_rows)

    # Per-day docs
    for date in dates:
        for path in sorted(RUNS_DIR.glob(f"{date}__*")):
            if path.is_file():
                if profile != "mixed":
                    name = path.name
                    lower = name.lower()
                    if profile == "tool_only" and "profit_alert" in lower:
                        continue
                    if name.endswith("__CONTROL_CENTER.md"):
                        continue
                    # Predictive per-state reports are profile-agnostic and often reference mixed artifacts.
                    if "__PREDICTIVE.md" in name:
                        continue
                    if "__PREDICTIVE_PORTFOLIO" in name:
                        if f"__PREDICTIVE_PORTFOLIO__{profile}.md" not in name:
                            continue
                    if "__CANDIDATE_UNIVERSE_GRADE" in name:
                        if f"__CANDIDATE_UNIVERSE_GRADE__{profile}" not in name:
                            continue
                    if "__PLAY_CARD_GRADE" in name:
                        if f"__PLAY_CARD_GRADE__{profile}" not in name:
                            continue
                _copy_file(path, dest_runs / path.name, dry_run=dry_run, manifest_rows=manifest_rows)


def _copy_context_docs(export_root: Path, *, dry_run: bool, manifest_rows: List[Dict[str, object]]) -> None:
    # Canonical read-first + final docs portal (SSOT)
    for src in [
        REPO_ROOT / "briefings" / "CODEX_READ_FIRST_AAT9_WSL_2.md",
        FINAL_DOCS_DIR / "README.md",
        FINAL_DOCS_DIR / "AAT9_Master_Validation_Predictive_Day_Quickstart.md",
        FINAL_DOCS_DIR / "AAT9_Candidate_Universe_Contract.md",
        FINAL_DOCS_DIR / "AAT9_Aux_Coverage_And_Legend.md",
        FINAL_DOCS_DIR / "SUPERBRAIN_PRIMITIVES.md",
        FINAL_DOCS_DIR / "WORKFLOW_CHANGELOG.md",
        REPO_ROOT / "TOOLS" / "VTRAC_REFERENCE_STRAIGHT.MD",
    ]:
        rel = src.relative_to(REPO_ROOT)
        _copy_file(src, export_root / rel, dry_run=dry_run, manifest_rows=manifest_rows)


def _copy_sharepack_state_evidence(
    src_state_dir: Path,
    dest_state_dir: Path,
    *,
    include_tables: bool,
    dry_run: bool,
    manifest_rows: List[Dict[str, object]],
) -> None:
    # State README is a nice portal if present.
    _copy_file(src_state_dir / "README.md", dest_state_dir / "README.md", dry_run=dry_run, manifest_rows=manifest_rows)

    state = src_state_dir.name

    # Winners lens (HTML/JSON)
    winners_dir = src_state_dir / "winners" / state
    _copy_glob(
        winners_dir,
        dest_state_dir / "winners" / state,
        patterns=("*.html", "*.json", "*.md"),
        dry_run=dry_run,
        manifest_rows=manifest_rows,
        allow_empty=True,
    )

    if include_tables:
        # Tables snapshots (CSV + JSON) (can be large; copy only when explicitly requested)
        tables_dir = src_state_dir / "tables"
        _copy_glob(
            tables_dir,
            dest_state_dir / "tables",
            patterns=("*.csv",),
            dry_run=dry_run,
            manifest_rows=manifest_rows,
            allow_empty=True,
        )
        json_dir = src_state_dir / "json"
        _copy_glob(
            json_dir,
            dest_state_dir / "json",
            patterns=(f"{state}_tables.json",),
            dry_run=dry_run,
            manifest_rows=manifest_rows,
            allow_empty=True,
        )

    # Aux (summary only; draw CSVs are intentionally excluded to keep size down)
    aux_dir = src_state_dir / "aux" / state
    _copy_glob(
        aux_dir,
        dest_state_dir / "aux" / state,
        patterns=("summary.md", "summary.json"),
        dry_run=dry_run,
        manifest_rows=manifest_rows,
        allow_empty=True,
    )

    # Tool summaries (small)
    for tool in ("stable", "vtrac", "hot_zones", "digit_reduction"):
        tdir = src_state_dir / tool / state
        _copy_glob(
            tdir,
            dest_state_dir / tool / state,
            patterns=("summary.md", "summary.json"),
            dry_run=dry_run,
            manifest_rows=manifest_rows,
            allow_empty=True,
        )

    # Digit Reduction overlay subset (this is the key “expensive” artifact; keep it bounded)
    dr_winners_dir = src_state_dir / "digit_reduction" / state / "analyzer_v2" / "winners"
    _copy_glob(
        dr_winners_dir,
        dest_state_dir / "digit_reduction" / state / "analyzer_v2" / "winners",
        patterns=(
            "*_winner_overlay.html",
            "*_winner_map.json",
            "*_winner_hits.csv",
            "*_winner_flags.csv",
            "*_winner_stamp.json",
        ),
        dry_run=dry_run,
        manifest_rows=manifest_rows,
        allow_empty=True,
    )


def _copy_predictive_state_artifacts(
    src_state_dir: Path,
    dest_state_dir: Path,
    *,
    profile: str,
    experiment_tag: Optional[str],
    dry_run: bool,
    manifest_rows: List[Dict[str, object]],
) -> None:
    profile = str(profile or "mixed").strip()
    suffix = "" if profile == "mixed" else f"__{profile}"
    tag_suffix = f"__{experiment_tag}" if experiment_tag else ""

    cu_json_name = f"candidate_universe{suffix}{tag_suffix}.json"
    cu_md_name = f"candidate_universe{suffix}{tag_suffix}.md"
    cu_evidence_csv = f"candidate_universe_evidence{suffix}{tag_suffix}.csv"
    cu_evidence_md = f"candidate_universe_evidence{suffix}{tag_suffix}.md"
    signals_name = f"signals_bundle{suffix}{tag_suffix}.json"
    play_card_json = f"play_card{suffix}{tag_suffix}.json"
    play_card_md = f"play_card{suffix}{tag_suffix}.md"

    # Always copy the gradeable JSON + evidence surfaces.
    for fname in (cu_json_name, cu_evidence_csv, cu_evidence_md, signals_name, play_card_json, play_card_md):
        _copy_file(src_state_dir / fname, dest_state_dir / fname, dry_run=dry_run, manifest_rows=manifest_rows)

    # candidate_universe.md is optional in the pipeline; generate it from the JSON if missing.
    src_md = src_state_dir / cu_md_name
    if src_md.exists() and src_md.is_file():
        _copy_file(src_md, dest_state_dir / cu_md_name, dry_run=dry_run, manifest_rows=manifest_rows)
    else:
        _generate_candidate_universe_md(
            src_state_dir / cu_json_name,
            dest_state_dir / cu_md_name,
            dry_run=dry_run,
            manifest_rows=manifest_rows,
        )

    state = src_state_dir.name
    for tool in ("stable", "vtrac", "hot_zones", "digit_reduction", "aux"):
        tdir = src_state_dir / tool / state if tool != "aux" else src_state_dir / "aux" / state
        _copy_glob(
            tdir,
            dest_state_dir / tdir.relative_to(src_state_dir),
            patterns=("summary.md", "summary.json"),
            dry_run=dry_run,
            manifest_rows=manifest_rows,
            allow_empty=True,
        )


def _copy_control_center(
    src_cc_dir: Path,
    dest_cc_dir: Path,
    *,
    dry_run: bool,
    manifest_rows: List[Dict[str, object]],
    include_profit_alerts: bool,
) -> None:
    if not src_cc_dir.exists():
        manifest_rows.append({"status": "missing", "src": str(src_cc_dir), "dest": str(dest_cc_dir), "bytes": 0})
        return
    for src in sorted(src_cc_dir.iterdir()):
        if not src.is_file():
            continue
        name = src.name
        if not include_profit_alerts:
            if name.startswith("profit_alerts") or name.startswith("profit_alerts_eval"):
                continue
        _copy_file(src, dest_cc_dir / name, dry_run=dry_run, manifest_rows=manifest_rows)


def _write_readme(
    out_dir: Path,
    *,
    args: argparse.Namespace,
    dates: List[str],
    selected_cases: Dict[str, Set[str]],
    manifest_rows: List[Dict[str, object]],
    dry_run: bool,
) -> None:
    byte_statuses = {"copied", "would_copy", "generated", "would_generate"}
    copied_statuses = {"copied", "generated"} if not dry_run else {"would_copy", "would_generate"}
    total_bytes = sum(int(r.get("bytes") or 0) for r in manifest_rows if r.get("status") in byte_statuses)
    copied = sum(1 for r in manifest_rows if r.get("status") in copied_statuses)
    missing = sum(1 for r in manifest_rows if r.get("status") == "missing")

    lines: List[str] = []
    lines.append("# ChatGPT Research Pack (Export)")
    lines.append("")
    lines.append("Purpose: a bounded, upload-friendly bundle for deep research without copying full sharepacks.")
    lines.append("")
    lines.append("## Contents (high level)")
    lines.append("")
    lines.append("- `docs/AAT9_KIT/FINAL VALIDATION/RUNS/` (navigation + state/day reports + rollups)")
    lines.append("- `sharepacks/<D>/<STATE>/winners/` (HTML+JSON environment lens)")
    if args.include_tables:
        lines.append("- `sharepacks/<D>/<STATE>/tables/*.csv` + `sharepacks/<D>/<STATE>/json/*_tables.json` (string tables snapshots)")
    lines.append("- `sharepacks/<D>/<STATE>/aux/<STATE>/summary.md` (Aux evidence dump)")
    lines.append("- `sharepacks/<D>/<STATE>/digit_reduction/<STATE>/analyzer_v2/winners/*_overlay.html` (DR overlay subset)")
    lines.append("")
    if args.include_predictive:
        suffix = "" if args.profile == "mixed" else f"__{args.profile}"
        tag_suffix = f"__{args.experiment_tag}" if args.experiment_tag else ""
        lines.append(
            f"- `sharepacks/_predictive/<D>/<STATE>/candidate_universe{suffix}{tag_suffix}.json` + `play_card{suffix}{tag_suffix}.json` (pre-results artifacts)"
        )
        lines.append("")
    lines.append("## Export parameters")
    lines.append("")
    lines.append(f"- mode: `{args.mode}`")
    lines.append(f"- experiment_tag: `{args.experiment_tag or ''}`")
    lines.append(f"- dates: `{dates[0] if dates else ''}` → `{dates[-1] if dates else ''}` ({len(dates)} days)")
    lines.append(f"- include_predictive: `{bool(args.include_predictive)}`")
    lines.append(f"- profile: `{args.profile}`")
    lines.append(f"- include_control_center: `{bool(args.include_control_center)}`")
    lines.append(f"- include_profit_alerts: `{bool(args.include_profit_alerts)}`")
    lines.append(f"- include_tables: `{bool(args.include_tables)}`")
    lines.append("")
    lines.append("## Selected cases")
    lines.append("")
    if not selected_cases:
        lines.append("- (none; export was window-only or no cases matched)")
    else:
        for date in sorted(selected_cases.keys()):
            states = ", ".join(sorted(selected_cases[date]))
            lines.append(f"- `{date}`: {states}")
    lines.append("")
    if args.include_path:
        lines.append("## Included extra paths")
        lines.append("")
        for p in args.include_path:
            s = str(p or "").strip()
            if s:
                lines.append(f"- `{s}`")
        lines.append("")
    lines.append("## How to use this pack (ChatGPT Pro Deep Research)")
    lines.append("")
    lines.append("1) Upload the `.zip` produced alongside this folder.")
    lines.append("2) In ChatGPT Pro, open this file first: `README.md` (zip root).")
    lines.append("3) If a pack prompt was included (recommended), open and follow it:")
    lines.append("   - `docs/AAT9_KIT/FINAL VALIDATION/PACKAGES/*/CHATGPT_PRO_DEEP_RESEARCH_PROMPT.md`")
    lines.append("4) Use `MANIFEST.csv` for a mechanical access check (missing rows are explicitly labeled).")
    lines.append("")
    lines.append("## Key entrypoints")
    lines.append("")
    lines.append("- RUNS portal: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/PORTAL.md`")
    lines.append("- Doubles study queue: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/DOUBLES_MIRROR_DOUBLES__STUDY_QUEUE.md`")
    lines.append("")
    lines.append("## Size summary")
    lines.append("")
    lines.append(f"- files_copied: `{copied}`")
    lines.append(f"- files_missing: `{missing}` (expected; some days/states lack certain artifacts)")
    lines.append(f"- total_bytes: `{total_bytes}`")
    lines.append("")

    if dry_run:
        return
    (out_dir / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def _write_manifest(out_dir: Path, manifest_rows: List[Dict[str, object]], *, dry_run: bool) -> None:
    if dry_run:
        return
    # Keep as CSV for easy inspection and diffing.
    path = out_dir / "MANIFEST.csv"
    cols = ["status", "src", "dest", "bytes"]
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for row in manifest_rows:
            w.writerow({k: row.get(k, "") for k in cols})


def _maybe_zip(out_dir: Path, *, dry_run: bool) -> Optional[Path]:
    if dry_run:
        return None
    base = str(out_dir)
    zip_path = shutil.make_archive(base, "zip", root_dir=out_dir)
    return Path(zip_path)


def main() -> None:
    args = _parse_args()

    if args.dates:
        dates = [d.strip() for d in args.dates]
    else:
        dates = _date_range_inclusive(args.start_date, args.end_date)

    out_dir = (
        Path(args.out)
        if args.out
        else (REPO_ROOT / "sharepacks" / "_scratch" / f"chatgpt_research_pack_{datetime.now(tz=timezone.utc).strftime('%Y%m%d_%H%M%S')}")
    )
    if not out_dir.is_absolute():
        out_dir = (REPO_ROOT / out_dir).resolve()

    states_filter = set(args.states) if args.states else None
    selected = _select_cases(args, dates, states_filter=states_filter)

    extra_windows: List[Tuple[str, str]] = []
    for raw in args.extra_window or []:
        s = str(raw or "").strip()
        if not s:
            continue
        if ":" not in s:
            raise SystemExit(f"--extra-window must be YYYY-MM-DD:YYYY-MM-DD (got {raw!r})")
        start, end = (p.strip() for p in s.split(":", 1))
        # Validate parse.
        datetime.strptime(start, "%Y-%m-%d")
        datetime.strptime(end, "%Y-%m-%d")
        extra_windows.append((start, end))

    manifest_rows: List[Dict[str, object]] = []

    if not args.dry_run:
        out_dir.mkdir(parents=True, exist_ok=True)

    if args.include_final_docs:
        _copy_context_docs(out_dir, dry_run=args.dry_run, manifest_rows=manifest_rows)

    # Optional extra files/dirs (e.g., a pointer-only PACKAGES bundle with a prompt/manifest)
    for raw in args.include_path or []:
        s = str(raw or "").strip()
        if not s:
            continue
        src = (REPO_ROOT / s).resolve()
        dest = (out_dir / s).resolve()
        if src.is_file():
            _copy_file(src, dest, dry_run=args.dry_run, manifest_rows=manifest_rows)
        elif src.is_dir():
            _copy_tree(src, dest, dry_run=args.dry_run, manifest_rows=manifest_rows)
        else:
            manifest_rows.append({"status": "missing", "src": str(src), "dest": str(dest), "bytes": 0})

    # RUNS (always copy; small, and anchors navigation)
    _copy_runs_docs(
        dates,
        out_dir,
        profile=args.profile,
        extra_windows=extra_windows,
        dry_run=args.dry_run,
        manifest_rows=manifest_rows,
    )

    # Post-results sharepacks (winners lens lives here)
    for date in dates:
        src_day = REPO_ROOT / "sharepacks" / date
        if args.mode == "window":
            states = sorted(states_filter or set(_infer_states_from_day(src_day)))
        else:
            states = sorted(selected.get(date, set()))

        if not states:
            continue

        dest_day = out_dir / "sharepacks" / date
        for state in states:
            _copy_sharepack_state_evidence(
                src_day / state,
                dest_day / state,
                include_tables=bool(args.include_tables),
                dry_run=args.dry_run,
                manifest_rows=manifest_rows,
            )

        if args.include_control_center:
            _copy_control_center(
                src_day / "control_center",
                dest_day / "control_center",
                dry_run=args.dry_run,
                manifest_rows=manifest_rows,
                include_profit_alerts=bool(args.include_profit_alerts),
            )

    # Predictive sharepacks (optional; pre-results artifacts + summaries)
    if args.include_predictive:
        for date in dates:
            src_day = REPO_ROOT / "sharepacks" / "_predictive" / date
            if args.mode == "window":
                states = sorted(states_filter or set(_infer_states_from_day(src_day)))
            else:
                states = sorted(selected.get(date, set()))
            if not states:
                continue
            dest_day = out_dir / "sharepacks" / "_predictive" / date
            for state in states:
                _copy_predictive_state_artifacts(
                    src_day / state,
                    dest_day / state,
                    profile=args.profile,
                    experiment_tag=args.experiment_tag,
                    dry_run=args.dry_run,
                    manifest_rows=manifest_rows,
                )
            if args.include_control_center:
                _copy_control_center(
                    src_day / "control_center",
                    dest_day / "control_center",
                    dry_run=args.dry_run,
                    manifest_rows=manifest_rows,
                    include_profit_alerts=bool(args.include_profit_alerts),
                )

    _write_readme(
        out_dir,
        args=args,
        dates=dates,
        selected_cases=selected,
        manifest_rows=manifest_rows,
        dry_run=args.dry_run,
    )
    _write_manifest(out_dir, manifest_rows, dry_run=args.dry_run)

    zip_path = None
    if args.zip:
        zip_path = _maybe_zip(out_dir, dry_run=args.dry_run)

    if args.dry_run:
        print(f"[DRY RUN] out_dir={out_dir}")
        return

    print(f"[OK] Export pack written: {out_dir}")
    if zip_path:
        print(f"[OK] Zip archive: {zip_path}")


if __name__ == "__main__":
    main()
