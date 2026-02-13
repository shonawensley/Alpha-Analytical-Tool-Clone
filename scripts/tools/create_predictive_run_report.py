#!/usr/bin/env python3
"""
Create a per-date/per-state Predictive Run Report Markdown file.

This is a workflow bridge between:
- frozen predictive sharepacks (pre-results): sharepacks/_predictive/<D>/...
- gradeable predictions: sharepacks/_predictive/<D>/<STATE>/candidate_universe*.json

It does NOT run analyzers, rebuild tables, or generate winners. It only reads
sharepack artifacts and writes a Markdown scaffold into RUNS.

Usage
-----
python3 scripts/tools/create_predictive_run_report.py --date 2026-01-07 --state NewJersey4
python3 scripts/tools/create_predictive_run_report.py --date 2026-01-07 --state NewJersey4 --sharepacks-root sharepacks/_predictive
python3 scripts/tools/create_predictive_run_report.py --date 2026-01-07 --state NewJersey4 --profile mixed
python3 scripts/tools/create_predictive_run_report.py --date 2026-01-07 --state NewJersey4 --experiment-tag stable10
python3 scripts/tools/create_predictive_run_report.py --date 2026-01-07 --state NewJersey4 --experiment-tag none
"""

from __future__ import annotations

import argparse
import json
from datetime import date as _date
from datetime import timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional


REPO_ROOT = Path(__file__).resolve().parents[2]


def _runs_dir() -> Path:
    return REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"


def parse_iso_date(value: str) -> _date:
    try:
        return _date.fromisoformat(value)
    except ValueError as exc:
        raise SystemExit(f"Invalid --date (expected YYYY-MM-DD): {value}") from exc


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def read_json(path: Path) -> object:
    return json.loads(read_text(path))


def safe_rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def normalize_tag(value: str) -> str:
    raw = str(value or "").strip()
    if raw.lower() in {"", "-", "none", "null"}:
        return ""
    return raw.replace(" ", "_")


def load_history_date(day_dir: Path, *, results_date: str) -> str:
    meta_path = day_dir / "control_center" / "meta.json"
    if meta_path.exists():
        raw = read_json(meta_path)
        if isinstance(raw, dict):
            h = str(raw.get("history_date") or "")
            if h:
                return h
    d = parse_iso_date(results_date)
    return (d - timedelta(days=1)).isoformat()


def summarize_candidate_universe(path: Path) -> List[str]:
    if not path.exists():
        return [
            f"- (missing) `{path.name}`",
            f"  - Generate: `python3 scripts/tools/create_candidate_universe.py --date <D> --sharepacks-root sharepacks/_predictive --profile <PROFILE> --states <STATE>`",
        ]

    raw = read_json(path)
    if not isinstance(raw, dict):
        return [f"- (unreadable) `{path.name}`"]

    packs = raw.get("packs")
    packs_list = packs if isinstance(packs, list) else []
    union_count = raw.get("union_combos_count")
    try:
        union_count_int = int(union_count)
    except Exception:
        union_count_int = len(raw.get("union_combos") or []) if isinstance(raw.get("union_combos"), list) else 0

    lines: List[str] = []
    lines.append(f"- Candidate Universe: `{safe_rel(path)}`")
    lines.append(f"- Packs: `{len(packs_list)}`; union combos: `{union_count_int}`")
    if isinstance(raw.get("contains_winners_artifacts"), bool):
        lines.append(f"- contains_winners_artifacts: `{raw.get('contains_winners_artifacts')}`")
    if packs_list:
        lines.append("- Pack list (id → mode → cost):")
        for pack in packs_list[:20]:
            if not isinstance(pack, dict):
                continue
            pack_id = str(pack.get("pack_id") or "?")
            play_mode = str(pack.get("play_mode") or "?")
            cost = pack.get("cost_units")
            try:
                cost_s = str(int(cost))
            except Exception:
                cost_s = "?"
            lines.append(f"  - `{pack_id}` → `{play_mode}` → `{cost_s}`")
        if len(packs_list) > 20:
            lines.append(f"  - … ({len(packs_list) - 20} more)")
    return lines


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Create a predictive run report scaffold (no winners).")
    ap.add_argument("--date", required=True, help="Predictive sharepack results date D (YYYY-MM-DD)")
    ap.add_argument("--state", required=True, help="State key (e.g., NewJersey4)")
    ap.add_argument(
        "--profile",
        default="tool_only",
        help="Ablation profile to reference (default: tool_only). Determines candidate_universe/play_card filenames.",
    )
    ap.add_argument(
        "--experiment-tag",
        default="stable10",
        help="Experiment tag suffix used in sharepack filenames (default: stable10). Use 'none' for untagged artifacts.",
    )
    ap.add_argument(
        "--sharepacks-root",
        default="sharepacks/_predictive",
        help="Sharepacks root directory (default: sharepacks/_predictive)",
    )
    ap.add_argument(
        "--out",
        default=None,
        help="Override output path (default: RUNS/<D>__<STATE>__PREDICTIVE{__profile}.md; mixed is unsuffixed)",
    )
    ap.add_argument("--force", action="store_true", help="Overwrite an existing file (default: refuse).")
    return ap.parse_args()


def main() -> None:
    args = parse_args()
    results_date = parse_iso_date(args.date).isoformat()
    profile = str(args.profile or "mixed").strip()
    experiment_tag = normalize_tag(args.experiment_tag)
    out_suffix = "" if profile == "mixed" else f"__{profile}"
    tag_suffix = f"__{experiment_tag}" if experiment_tag else ""

    sharepacks_root = Path(args.sharepacks_root)
    if not sharepacks_root.is_absolute():
        sharepacks_root = (REPO_ROOT / sharepacks_root).resolve()
    day_dir = sharepacks_root / results_date
    if not day_dir.exists():
        raise SystemExit(f"Missing sharepack day dir: {safe_rel(day_dir)}")

    state_dir = day_dir / args.state
    if not state_dir.exists():
        raise SystemExit(f"Missing sharepack state dir: {safe_rel(state_dir)}")

    runs_dir = _runs_dir()
    runs_dir.mkdir(parents=True, exist_ok=True)
    default_out = runs_dir / f"{results_date}__{args.state}__PREDICTIVE{out_suffix}.md"
    out_path = Path(args.out) if args.out else default_out
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if out_path.exists() and not args.force:
        raise SystemExit(f"Predictive run report already exists: {safe_rel(out_path)} (use --force to overwrite).")

    history_date = load_history_date(day_dir, results_date=results_date)

    candidate_universe = state_dir / f"candidate_universe{out_suffix}{tag_suffix}.json"
    play_card = state_dir / f"play_card{out_suffix}{tag_suffix}.json"
    fallback_note: Optional[str] = None
    if experiment_tag and (not candidate_universe.exists() or not play_card.exists()):
        cu_fallback = state_dir / f"candidate_universe{out_suffix}.json"
        pc_fallback = state_dir / f"play_card{out_suffix}.json"
        if (not candidate_universe.exists()) and cu_fallback.exists():
            candidate_universe = cu_fallback
            fallback_note = (
                f"Experiment tag `{experiment_tag}` not found; fell back to untagged `{Path(candidate_universe).name}`."
            )
        if (not play_card.exists()) and pc_fallback.exists():
            play_card = pc_fallback
            msg = f"Experiment tag `{experiment_tag}` not found; fell back to untagged `{Path(play_card).name}`."
            fallback_note = f"{fallback_note} {msg}".strip() if fallback_note else msg
    cc_dir = day_dir / "control_center"

    # Common evidence pointers (best-effort; may be missing).
    evidence_paths: Dict[str, str] = {
        "Sharepack state README": safe_rel(state_dir / "README.md"),
        "Candidate Universe": safe_rel(candidate_universe),
        "Play Card": safe_rel(play_card),
        "Control Center portal dir": safe_rel(cc_dir),
        "Profit Alerts (optional)": safe_rel(cc_dir / "profit_alerts.csv"),
        "Due Doubles": safe_rel(cc_dir / "due_doubles.csv"),
        "VTRAC Repeat Watch": safe_rel(cc_dir / "vtrac_repeat_watch.csv"),
        "Stable scores": safe_rel(state_dir / "stable" / args.state / f"{args.state}_stable_patterns_scores.csv"),
        "Stable report": safe_rel(state_dir / "stable" / args.state / f"{args.state}_stable_patterns_report.html"),
        "Digit Reduction report": safe_rel(state_dir / "digit_reduction" / args.state / f"{args.state}_digit_reduction_report.html"),
        "DR Analyzer V2 top": safe_rel(
            state_dir
            / "digit_reduction"
            / args.state
            / "analyzer_v2"
            / f"{args.state}_analyzer_v2_top_candidates.csv"
        ),
        "Hot Zones top lanes": safe_rel(state_dir / "hot_zones" / args.state / f"{args.state}_hot_zones_top_lanes.csv"),
        "Aux summary": safe_rel(state_dir / "aux" / args.state / "summary.md"),
    }

    lines: List[str] = []
    lines.append(f"# Predictive Run Report — {args.state} — D={results_date} (H={history_date})")
    lines.append("")
    lines.append("Purpose")
    lines.append("- Capture a **pre-results** snapshot analysis for one state/day.")
    lines.append(f"- Keep predictions gradeable via `{candidate_universe.name}` (do not mix in winners artifacts).")
    lines.append("")
    lines.append("Scope")
    lines.append(f"- Results date (D): `{results_date}`")
    lines.append(f"- History workbook date (H): `{history_date}` (usually D-1)")
    lines.append(f"- Predictive sharepack root: `{safe_rel(sharepacks_root)}`")
    lines.append(f"- Sharepack state dir: `{safe_rel(state_dir)}`")
    lines.append(f"- Profile: `{profile}`")
    if experiment_tag:
        lines.append(f"- Experiment tag: `{experiment_tag}`")
    lines.append("")
    if fallback_note:
        lines.append("Note")
        lines.append(f"- {fallback_note}")
    lines.append("")
    lines.append("SSOT posture (winners‑free; read first)")
    lines.append("- Portal: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/PORTAL.md`")
    lines.append("- Roadmap (macro map): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_ROADMAP.md`")
    lines.append("- Defaults (what we run by default): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0_2__DEFAULTS.md`")
    lines.append("- v0.3 policy (coverage vs conversion): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__PREDICTIVE_POLICY__tool_only__stable10.md`")
    lines.append("- Glossary (strict vs lane vs inclusive): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__GLOSSARY__PREDICTIVE_SEMANTICS.md`")
    lines.append("- Glass‑box flow (evidence → CU → Play Card → grades): `docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_3__PIPELINE_FLOW__GLASS_BOX.md`")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Candidate Universe (gradeable predictions)")
    lines.append("")
    lines.extend(summarize_candidate_universe(candidate_universe))
    lines.append("")
    lines.append("## Evidence pointers (sharepack-local)")
    lines.append("")
    for label, path in evidence_paths.items():
        lines.append(f"- {label}: `{path}`")
    lines.append("")
    lines.append("## Analyst notes (fill in)")
    lines.append("")
    lines.append("- What is the strongest evidence cluster (Stable/DR/VTRAC/HZ/Aux/Profit Alerts)?")
    lines.append("- Which pack(s) do you actually want to play (budgeted, boxed-first)?")
    lines.append("- Any cross-variant notes (Midday vs Evening), without treating Combined as an outcome?")
    lines.append("- Any anomalies (missing artifacts, suspicious drift, etc.)?")
    lines.append("")

    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"Wrote: {out_path}")


if __name__ == "__main__":
    main()
