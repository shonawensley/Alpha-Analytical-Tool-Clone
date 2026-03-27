#!/usr/bin/env python3
"""
Create an arena-native per-day synthesis report.

This report is the day-level post-results synthesis shell for the Analysis
Arena branch. It uses:

- frozen results truth
- per-state predictive arena receipts
- Brain 2 carry-through recovered from translation sandbox seeds
- existing generated validation artifacts when present

It does NOT depend on the old RUNS corpus export.
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import date as _date
from datetime import timedelta
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


REPO_ROOT = Path(__file__).resolve().parents[2]
RUNS2_VALIDATION_DIR = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS_2" / "VALIDATION"
FINAL_DOCS_DIR = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "final docs"

SYSTEM_MAP_PATH = FINAL_DOCS_DIR / "AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md"
OPERATING_FLOW_PATH = FINAL_DOCS_DIR / "AAT9_ANALYSIS_ARENA_OPERATING_FLOW__FRESH_RUNS.md"
STATE_TEMPLATE_PATH = FINAL_DOCS_DIR / "AAT9_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md"
BRAIN2_MV_TEMPLATE_PATH = FINAL_DOCS_DIR / "AAT9_BRAIN2_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md"


def parse_iso_date(value: str) -> _date:
    try:
        return _date.fromisoformat(value)
    except ValueError as exc:
        raise SystemExit(f"Invalid --date (expected YYYY-MM-DD): {value}") from exc


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def read_json(path: Path) -> Any:
    return json.loads(read_text(path))


def try_read_json(path: Path) -> Any | None:
    if not path.exists():
        return None
    return read_json(path)


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


def _profile_suffix(profile: str) -> str:
    p = str(profile or "mixed").strip()
    return "" if p == "mixed" else f"__{p}"


def _tag_suffix(experiment_tag: str) -> str:
    return f"__{experiment_tag}" if experiment_tag else ""


def _preferred_path(base_dir: Path, stem: str, ext: str, *, profile: str, experiment_tag: str) -> Path:
    tagged = base_dir / f"{stem}{_profile_suffix(profile)}{_tag_suffix(experiment_tag)}.{ext}"
    if tagged.exists():
        return tagged
    return base_dir / f"{stem}{_profile_suffix(profile)}.{ext}"


def _fmt_path(path: Path) -> str:
    suffix = "" if path.exists() else " (missing)"
    return f"`{safe_rel(path)}`{suffix}"


def _ordered_unique(values: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for value in values:
        value = str(value or "").strip()
        if not value or value in seen:
            continue
        seen.add(value)
        out.append(value)
    return out


def _fmt_items(values: Sequence[str], *, empty: str = "_none_") -> str:
    items = _ordered_unique(values)
    if not items:
        return empty
    return ", ".join(f"`{item}`" for item in items)


def _parse_results_map(results_date: str) -> dict[str, dict[str, str]]:
    out: dict[str, dict[str, str]] = {}
    path = REPO_ROOT / "data" / "results" / f"{results_date}.txt"
    if not path.exists():
        return out
    specials = {
        "New York": "NewYork4",
        "New Jersey": "NewJersey4",
        "North Carolina": "NorthCarolina4",
        "South Carolina": "SouthCarolina4",
        "Puerto Rico": "PuertoRico4",
        "Ontario": "OntarioCanada4",
        "Washington, D.C.": "WashingtonDC4",
    }
    for raw_line in read_text(path).splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if "\t" in line:
            parts = [part.strip() for part in line.split("\t")]
            label = parts[0]
            midday = "".join(ch for ch in (parts[1] if len(parts) > 1 else "") if ch.isdigit())
            evening = "".join(ch for ch in (parts[2] if len(parts) > 2 else "") if ch.isdigit())
        else:
            tokens = line.split()
            if len(tokens) < 2:
                continue
            label = []
            nums = []
            for token in tokens:
                digits = "".join(ch for ch in token if ch.isdigit())
                if len(digits) == 3:
                    nums.append(digits)
                else:
                    label.append(token)
            label = " ".join(label)
            midday = nums[0] if len(nums) >= 1 else ""
            evening = nums[1] if len(nums) >= 2 else ""
        state_key = specials.get(label, f"{label.replace(' ', '')}4")
        out[state_key] = {"midday": midday.zfill(3) if midday else "", "evening": evening.zfill(3) if evening else ""}
    return out


def _board_rows_from_sandbox(day_dir: Path, *, profile: str, experiment_tag: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for state_dir in sorted([p for p in day_dir.iterdir() if p.is_dir() and p.name != "control_center"], key=lambda p: p.name):
        sandbox_path = _preferred_path(
            state_dir / "analysis",
            "translation_sandbox_seed",
            "json",
            profile=profile,
            experiment_tag=experiment_tag,
        )
        seed = try_read_json(sandbox_path)
        if not isinstance(seed, Mapping):
            continue
        brain2 = seed.get("brain2_context") or {}
        if not isinstance(brain2, Mapping):
            continue
        scoreboard = brain2.get("scoreboard_row") or {}
        if not isinstance(scoreboard, Mapping):
            continue
        rows.append(
            {
                "state_key": state_dir.name,
                "score_rank": int(scoreboard.get("score_rank") or 9999),
                "role": str(scoreboard.get("role") or "").strip(),
                "bucket": str(scoreboard.get("targeting_bucket") or "").strip(),
                "tracker": str(scoreboard.get("tracker_posture") or "").strip(),
                "top_canonicals": [str(x) for x in (scoreboard.get("top_canonicals") or []) if str(x).strip()],
                "top_vtrac": [str(x) for x in (scoreboard.get("top_vtrac_indices") or []) if str(x).strip()],
                "profit_hint": str(scoreboard.get("profit_alert_hint") or "").strip(),
                "due_hint": str(scoreboard.get("due_double_hint") or "").strip(),
                "blackapple_hint": str(scoreboard.get("blackapple_reco_hint") or "").strip(),
                "survivor_hint": str(scoreboard.get("survivor_hint") or "").strip(),
                "consensus_hint": str(scoreboard.get("r_consensus_hint") or "").strip(),
            }
        )
    rows.sort(key=lambda row: (row["score_rank"], row["state_key"]))
    return rows


def _history_date(day_dir: Path, *, results_date: str) -> str:
    meta_path = day_dir / "control_center" / "meta.json"
    raw = try_read_json(meta_path)
    if isinstance(raw, Mapping):
        history_date = str(raw.get("history_date") or "").strip()
        if history_date:
            return history_date
    return (parse_iso_date(results_date) - timedelta(days=1)).isoformat()


def build_day_synthesis_report(
    *,
    results_date: str,
    profile: str,
    experiment_tag: str,
    predictive_sharepacks_root: Path,
    validation_dir: Path,
) -> str:
    day_dir = predictive_sharepacks_root / results_date
    history_date = _history_date(day_dir, results_date=results_date)
    board_rows = _board_rows_from_sandbox(day_dir, profile=profile, experiment_tag=experiment_tag)
    results_map = _parse_results_map(results_date)
    state_reports = sorted(validation_dir.glob(f"{results_date}__*.md"))
    state_reports = [path for path in state_reports if "__BRAIN2_MASTER_VALIDATION" not in path.name and "__DAY_SYNTHESIS" not in path.name and "__CONTROL_CENTER" not in path.name]
    brain2_mv = validation_dir / f"{results_date}__BRAIN2_MASTER_VALIDATION.md"
    control_center_md = validation_dir / f"{results_date}__CONTROL_CENTER.md"

    lines: list[str] = []
    lines.append(f"# Analysis Arena Day Synthesis — D={results_date} (H={history_date})")
    lines.append("")
    lines.append("Purpose")
    lines.append("- Provide the day-level synthesis shell for the Analysis Arena branch without depending on the old corpus-export workflow.")
    lines.append("- Tie results truth, Brain 2 carry-through, and generated validation artifacts together in one board-scope handoff.")
    lines.append("")
    lines.append("Template / SSOT anchors")
    lines.append(f"- Arena system map: {_fmt_path(SYSTEM_MAP_PATH)}")
    lines.append(f"- Arena operating flow: {_fmt_path(OPERATING_FLOW_PATH)}")
    lines.append(f"- Per-state Master Validation template: {_fmt_path(STATE_TEMPLATE_PATH)}")
    lines.append(f"- Brain 2 Master Validation template: {_fmt_path(BRAIN2_MV_TEMPLATE_PATH)}")
    lines.append("")
    lines.append("## 0) Provenance")
    lines.append(f"- Results date `D`: `{results_date}`")
    lines.append(f"- History date `H`: `{history_date}`")
    lines.append(f"- Predictive sharepacks root: `{safe_rel(predictive_sharepacks_root)}`")
    lines.append(f"- Predictive day dir: `{safe_rel(day_dir)}`")
    lines.append(f"- Validation dir: `{safe_rel(validation_dir)}`")
    lines.append(f"- Profile: `{profile}`")
    lines.append(f"- Experiment tag: `{experiment_tag or 'untagged'}`")
    lines.append(f"- Results file: {_fmt_path(REPO_ROOT / 'data' / 'results' / f'{results_date}.txt')}")
    lines.append("")
    lines.append("## 1) Board Carry-Through Snapshot")
    lines.append("")
    if board_rows:
        for row in board_rows[:8]:
            hints = " | ".join(
                part
                for part in [
                    row["profit_hint"],
                    row["due_hint"],
                    row["blackapple_hint"],
                    row["survivor_hint"],
                    row["consensus_hint"],
                ]
                if part
            )
            lines.append(
                f"- **{row['state_key']}**: `#{row['score_rank']}` role=`{row['role'] or '-'}` bucket=`{row['bucket'] or '-'}` tracker=`{row['tracker'] or '-'}` canonicals=`{','.join(row['top_canonicals'][:3]) or '-'}` vtrac=`{','.join(row['top_vtrac'][:3]) or '-'}` hints=`{hints or '-'}`"
            )
    else:
        lines.append("- No Brain 2 carry-through rows found.")
    lines.append("")
    lines.append("## 2) Results Truth Map")
    lines.append("")
    for row in board_rows[:8]:
        truth = results_map.get(row["state_key"], {})
        lines.append(
            f"- **{row['state_key']}**: Midday=`{truth.get('midday') or '-'}` Evening=`{truth.get('evening') or '-'}`"
        )
    lines.append("")
    lines.append("## 3) Validation Artifact Lock")
    lines.append("")
    lines.append(f"- Per-state validation reports generated: `{len(state_reports)}`")
    lines.append(f"- Brain 2 Master Validation: {_fmt_path(brain2_mv)}")
    lines.append(f"- Control Center daily report: {_fmt_path(control_center_md)}")
    lines.append(f"- State reports (sample): {_fmt_items([safe_rel(path) for path in state_reports[:10]], empty='_(none found)_')}")
    lines.append("")
    lines.append("## 4) Synthesis Prompts")
    lines.append("")
    lines.append("- Which states were true hosts vs echoes today?: `...`")
    lines.append("- Did the board scoreboard describe the day well as a board?: `...`")
    lines.append("- What shared complex / carryover pattern most defined the day?: `...`")
    lines.append("- Which tracker families most shaped the day across states?: `...`")
    lines.append("- What should be handed into the Brain 2 Master Validation report?: `...`")
    lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    ap = argparse.ArgumentParser(description="Create an arena-native per-day synthesis report.")
    ap.add_argument("--date", required=True, help="Results/sharepack date D (YYYY-MM-DD)")
    ap.add_argument("--profile", default="tool_only")
    ap.add_argument("--experiment-tag", default="arena_v0")
    ap.add_argument("--predictive-sharepacks-root", default="sharepacks/_predictive")
    ap.add_argument(
        "--validation-dir",
        default=None,
        help="Validation output dir to scan for per-state reports (default: RUNS_2/VALIDATION)",
    )
    ap.add_argument(
        "--out",
        help="Output Markdown path (default: RUNS_2/VALIDATION/<D>__DAY_SYNTHESIS.md)",
    )
    ap.add_argument("--force", action="store_true", help="Overwrite an existing synthesis file.")
    args = ap.parse_args()

    results_date = parse_iso_date(args.date).isoformat()
    predictive_sharepacks_root = Path(args.predictive_sharepacks_root)
    if not predictive_sharepacks_root.is_absolute():
        predictive_sharepacks_root = (REPO_ROOT / predictive_sharepacks_root).resolve()
    validation_dir = Path(args.validation_dir) if args.validation_dir else RUNS2_VALIDATION_DIR
    if not validation_dir.is_absolute():
        validation_dir = (REPO_ROOT / validation_dir).resolve()

    validation_dir.mkdir(parents=True, exist_ok=True)
    out_path = Path(args.out) if args.out else (validation_dir / f"{results_date}__DAY_SYNTHESIS.md")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if out_path.exists() and not args.force:
        raise SystemExit(f"Day synthesis already exists: {safe_rel(out_path)} (use --force to overwrite).")

    report = build_day_synthesis_report(
        results_date=results_date,
        profile=str(args.profile or "tool_only").strip(),
        experiment_tag=normalize_tag(args.experiment_tag),
        predictive_sharepacks_root=predictive_sharepacks_root,
        validation_dir=validation_dir,
    )
    out_path.write_text(report, encoding="utf-8")
    print(f"Wrote: {safe_rel(out_path)}")


if __name__ == "__main__":
    main()
