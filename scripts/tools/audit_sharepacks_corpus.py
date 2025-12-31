#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence


class Status:
    PASS = "PASS"
    WARN = "WARN"
    FAIL = "FAIL"
    SKIP = "SKIP"


@dataclass(frozen=True)
class Check:
    name: str
    status: str
    details: str


@dataclass(frozen=True)
class CommandResult:
    cmd: list[str]
    returncode: int
    stdout: str
    stderr: str


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _parse_readme_inputs(readme_text: str) -> tuple[str | None, str | None]:
    history_excel = None
    results_file = None
    history_match = re.search(r"-\\s*History workbook\\s*\\(H\\):\\s*`([^`]+)`", readme_text)
    if history_match:
        history_excel = history_match.group(1).strip()
    results_match = re.search(r"-\\s*Results file\\s*\\(D\\):\\s*`([^`]+)`", readme_text)
    if results_match:
        results_file = results_match.group(1).strip()
    return history_excel, results_file


def _run_cmd(cmd: Sequence[str], env: dict[str, str] | None = None, timeout_s: int = 120) -> CommandResult:
    merged_env = os.environ.copy()
    if env:
        merged_env.update(env)
    proc = subprocess.run(
        list(cmd),
        capture_output=True,
        text=True,
        env=merged_env,
        timeout=timeout_s,
    )
    return CommandResult(cmd=list(cmd), returncode=proc.returncode, stdout=proc.stdout, stderr=proc.stderr)


def _cmd_to_str(cmd: Sequence[str]) -> str:
    return " ".join([subprocess.list2cmdline([c]) if " " in c else c for c in cmd])


def _read_draws_csv(path: Path, max_rows: int | None = None) -> list[str]:
    draws: list[str] = []
    with path.open("r", encoding="utf-8", errors="replace", newline="") as f:
        reader = csv.reader(f)
        header = next(reader, None)
        if not header or header[0].strip().lower() != "draw":
            raise ValueError(f"Unexpected CSV header in {path} (expected first column 'Draw')")
        for row in reader:
            if not row:
                continue
            val = row[0].strip()
            if not val:
                continue
            draws.append(val)
            if max_rows is not None and len(draws) >= max_rows:
                break
    return draws


def _safe_head(values: Sequence[str], n: int = 5) -> str:
    return ", ".join(values[:n])


def _compare_prefix(curr: Sequence[str], prev: Sequence[str], shift: int, k: int) -> bool:
    if shift < 0:
        return False
    if len(curr) < shift + k or len(prev) < k:
        return False
    return list(curr[shift : shift + k]) == list(prev[:k])


def _check_shift(
    *,
    label: str,
    prev: list[str],
    curr: list[str],
    expected_new: list[str] | None,
    preferred_shift: int,
    shift_candidates: Sequence[int],
    prefix_k: int,
) -> Check:
    if not prev or not curr:
        return Check(label, Status.FAIL, "Missing draws data (empty list)")

    if expected_new is None:
        for shift in shift_candidates:
            if _compare_prefix(curr, prev, shift=shift, k=prefix_k):
                if shift == preferred_shift:
                    return Check(
                        label,
                        Status.PASS,
                        f"Refresh shift inferred={shift} (no expected winners available). head={_safe_head(curr)}",
                    )
                # shift=0 usually means “no new draw”; it can be expected on some days (missing results / no draw),
                # but we still surface it as WARN so you notice it.
                return Check(
                    label,
                    Status.WARN,
                    f"Refresh shift inferred={shift} (no expected winners available). head={_safe_head(curr)}",
                )
        return Check(
            label,
            Status.FAIL,
            f"No expected winners available and no plausible shift matched. prev_head={_safe_head(prev)} curr_head={_safe_head(curr)}",
        )

    if expected_new and curr[: len(expected_new)] != expected_new:
        return Check(
            label,
            Status.FAIL,
            f"Head mismatch vs expected winners. expected={expected_new} got={curr[:len(expected_new)]} (head={_safe_head(curr)})",
        )

    if not _compare_prefix(curr, prev, shift=preferred_shift, k=prefix_k):
        return Check(
            label,
            Status.FAIL,
            f"Prefix mismatch after shift={preferred_shift}. prev_head={_safe_head(prev)} curr_head={_safe_head(curr)}",
        )

    return Check(label, Status.PASS, f"Shift OK. expected={expected_new} head={_safe_head(curr)}")


def _state_dirs_for_day(day_dir: Path) -> list[str]:
    out: list[str] = []
    for child in sorted(day_dir.iterdir()):
        if not child.is_dir():
            continue
        if child.name.startswith(("_", "DR_", "HotZones_")):
            continue
        if child.name == "control_center":
            continue
        out.append(child.name)
    return out


def _audit_day(day: str, report_lines: list[str]) -> tuple[list[Check], dict]:
    root = _repo_root()
    day_dir = root / "sharepacks" / day

    checks: list[Check] = []
    report_lines.append(f"## Day `{day}`")

    if not day_dir.exists():
        checks.append(Check("sharepack_dir_exists", Status.FAIL, f"Missing {day_dir}"))
        report_lines.append(f"- FAIL: missing `{day_dir}`")
        return checks, {}

    readme_path = day_dir / "README.md"
    if not readme_path.exists():
        checks.append(Check("readme_exists", Status.WARN, f"Missing {readme_path}"))
        report_lines.append(f"- WARN: missing `{readme_path}`")
        readme_history = None
        readme_results = None
    else:
        readme_history, readme_results = _parse_readme_inputs(_read_text(readme_path))
        checks.append(Check("readme_exists", Status.PASS, f"Found {readme_path}"))

    meta_path = day_dir / "control_center" / "meta.json"
    if not meta_path.exists():
        checks.append(Check("cc_meta_exists", Status.FAIL, f"Missing {meta_path}"))
        report_lines.append(f"- FAIL: missing `{meta_path}`")
        return checks, {}

    meta = json.loads(_read_text(meta_path))
    history_excel_path = meta.get("history_excel_path")
    results_file = meta.get("results_file")
    history_date = meta.get("history_date")

    report_lines.append(f"- History workbook: `{history_excel_path}` (H={history_date})")
    report_lines.append(f"- Results file: `{results_file}`")

    if isinstance(history_excel_path, str) and (root / history_excel_path).exists():
        checks.append(Check("history_excel_exists", Status.PASS, history_excel_path))
    else:
        checks.append(Check("history_excel_exists", Status.FAIL, f"Missing history workbook: {history_excel_path}"))

    if isinstance(results_file, str) and (root / results_file).exists():
        checks.append(Check("results_file_exists", Status.PASS, results_file))
    else:
        checks.append(Check("results_file_exists", Status.FAIL, f"Missing results file: {results_file}"))

    if readme_history and history_excel_path and readme_history != history_excel_path:
        checks.append(
            Check(
                "readme_vs_meta_history",
                Status.WARN,
                f"README history `{readme_history}` != meta `{history_excel_path}`",
            )
        )
    if readme_results and results_file and readme_results != results_file:
        checks.append(
            Check(
                "readme_vs_meta_results",
                Status.WARN,
                f"README results `{readme_results}` != meta `{results_file}`",
            )
        )

    # State list sanity
    meta_states = meta.get("states") or []
    meta_state_keys = [s.get("state_key") for s in meta_states if isinstance(s, dict)]
    disk_state_keys = _state_dirs_for_day(day_dir)
    report_lines.append(f"- States (meta): {len(meta_state_keys)}")
    report_lines.append(f"- States (disk): {len(disk_state_keys)}")

    missing_on_disk = [k for k in meta_state_keys if k and k not in disk_state_keys]
    extra_on_disk = [k for k in disk_state_keys if k not in set(meta_state_keys)]
    if missing_on_disk:
        checks.append(Check("states_missing_on_disk", Status.FAIL, f"{missing_on_disk}"))
    else:
        checks.append(Check("states_missing_on_disk", Status.PASS, ""))
    if extra_on_disk:
        checks.append(Check("states_extra_on_disk", Status.WARN, f"{extra_on_disk}"))
    else:
        checks.append(Check("states_extra_on_disk", Status.PASS, ""))

    # Per-state provenance checks + required core files (do not run heavy validators here; separate section below)
    for state in meta_states:
        if not isinstance(state, dict):
            continue
        state_key = state.get("state_key")
        if not isinstance(state_key, str):
            continue

        aux_summary_rel = state.get("aux_summary")
        aux_draws_dir_rel = state.get("aux_draws_dir")

        state_dir = day_dir / state_key
        if not state_dir.exists():
            checks.append(Check(f"{state_key}:state_dir_exists", Status.FAIL, f"Missing {state_dir}"))
            continue

        # Core inputs
        required = [
            state_dir / "tables" / "Combined_Combined.csv",
            state_dir / "tables" / "Midday_Combined.csv",
            state_dir / "tables" / "Evening_Combined.csv",
            state_dir / "json" / f"{state_key}_tables.json",
        ]
        missing_required = [str(p.relative_to(root)) for p in required if not p.exists()]
        if missing_required:
            checks.append(Check(f"{state_key}:core_files", Status.FAIL, f"Missing {missing_required}"))
        else:
            checks.append(Check(f"{state_key}:core_files", Status.PASS, ""))

        # Aux summary / snapshot meta validation
        if not isinstance(aux_summary_rel, str):
            checks.append(Check(f"{state_key}:aux_summary_path", Status.FAIL, "meta aux_summary missing"))
            continue
        aux_summary_path = root / aux_summary_rel
        if not aux_summary_path.exists():
            checks.append(Check(f"{state_key}:aux_summary_exists", Status.FAIL, f"Missing {aux_summary_rel}"))
            continue

        aux_summary = json.loads(_read_text(aux_summary_path))
        snapshot_meta = (
            aux_summary.get("draw_sources", {})
            .get("snapshot_meta", {})
        )
        excel_path = snapshot_meta.get("excel_path")
        if history_excel_path and excel_path and excel_path != history_excel_path:
            checks.append(
                Check(
                    f"{state_key}:aux_excel_match",
                    Status.FAIL,
                    f"Aux snapshot excel `{excel_path}` != day history `{history_excel_path}`",
                )
            )
        else:
            checks.append(Check(f"{state_key}:aux_excel_match", Status.PASS, f"{excel_path}"))

        if not isinstance(aux_draws_dir_rel, str):
            checks.append(Check(f"{state_key}:aux_draws_dir", Status.FAIL, "meta aux_draws_dir missing"))
            continue
        aux_draws_dir = root / aux_draws_dir_rel
        if not aux_draws_dir.exists():
            checks.append(Check(f"{state_key}:aux_draws_dir_exists", Status.FAIL, f"Missing {aux_draws_dir_rel}"))
            continue

        # Ensure snapshot draws exist (combined/midday/evening)
        expected_draws = [
            aux_draws_dir / f"{snapshot_meta.get('aux_state_label', state_key).replace(' ', '_')}_draws.csv",
        ]
        # But state labels differ by state; trust the resolved paths in summary.json instead:
        snapshot = aux_summary.get("draw_sources", {}).get("snapshot", {})
        resolved = [snapshot.get(k, {}).get("resolved_path") for k in ("combined", "midday", "evening")]
        missing_resolved = [p for p in resolved if not isinstance(p, str) or not (Path(p).exists())]
        if missing_resolved:
            checks.append(Check(f"{state_key}:aux_snapshot_draws", Status.FAIL, f"Missing resolved draws: {missing_resolved}"))
        else:
            checks.append(Check(f"{state_key}:aux_snapshot_draws", Status.PASS, "combined/midday/evening"))

    report_lines.append("")
    return checks, meta


def _audit_validators(day: str, meta: dict, report_lines: list[str]) -> list[Check]:
    root = _repo_root()
    checks: list[Check] = []
    day_dir = root / "sharepacks" / day
    report_lines.append("### Validators")

    # Day-level VTRAC compact report validator
    cmd = ["python3", "scripts/tools/validate_vtrac_compact_report.py", "--date", day, "--warn-only"]
    res = _run_cmd(cmd, timeout_s=120)
    if res.returncode == 0:
        checks.append(Check("validate_vtrac_compact_report", Status.PASS, ""))
    else:
        checks.append(Check("validate_vtrac_compact_report", Status.FAIL, f"exit={res.returncode}"))
        report_lines.append(f"- FAIL: `{_cmd_to_str(cmd)}`")

    meta_states = meta.get("states") or []
    for state in meta_states:
        if not isinstance(state, dict):
            continue
        state_key = state.get("state_key")
        if not isinstance(state_key, str):
            continue

        # Tables ↔ Aux alignment (sharepack mode)
        env = {"PYTHONPATH": ".:src"}
        cmd = [
            "python3",
            "scripts/tools/validate_tables_aux_alignment.py",
            "--date",
            day,
            "--state",
            state_key,
            "--strict",
        ]
        res = _run_cmd(cmd, env=env, timeout_s=120)
        if res.returncode == 0:
            checks.append(Check(f"{day}:{state_key}:tables_aux_alignment", Status.PASS, ""))
        else:
            checks.append(Check(f"{day}:{state_key}:tables_aux_alignment", Status.FAIL, f"exit={res.returncode}"))

        # Tool winners validators (workflow sanity, not “must hit”)
        stable_dir = day_dir / state_key / "stable" / state_key
        dr_dir = day_dir / state_key / "digit_reduction" / state_key
        hz_dir = day_dir / state_key / "hot_zones" / state_key
        winners = state.get("winners") or {}
        winners_empty = isinstance(winners, dict) and not winners

        if winners_empty:
            checks.append(Check(f"{day}:{state_key}:validate_stable_winners", Status.SKIP, "No winners in results file (expected for some states/days)"))
            checks.append(Check(f"{day}:{state_key}:validate_dr_winners", Status.SKIP, "No winners in results file (expected for some states/days)"))
            checks.append(Check(f"{day}:{state_key}:validate_hot_zones_winners", Status.SKIP, "No winners in results file (expected for some states/days)"))
            continue

        if stable_dir.exists():
            cmd = ["python3", "scripts/tools/validate_stable_winners.py", "--sharepack", str(stable_dir)]
            res = _run_cmd(cmd, env=env, timeout_s=120)
            checks.append(
                Check(
                    f"{day}:{state_key}:validate_stable_winners",
                    Status.PASS if res.returncode == 0 else Status.FAIL,
                    "" if res.returncode == 0 else f"exit={res.returncode}",
                )
            )
        else:
            checks.append(Check(f"{day}:{state_key}:validate_stable_winners", Status.WARN, "Missing stable dir"))

        if dr_dir.exists():
            cmd = ["python3", "scripts/tools/validate_dr_winners.py", "--sharepack", str(dr_dir)]
            res = _run_cmd(cmd, env=env, timeout_s=120)
            checks.append(
                Check(
                    f"{day}:{state_key}:validate_dr_winners",
                    Status.PASS if res.returncode == 0 else Status.FAIL,
                    "" if res.returncode == 0 else f"exit={res.returncode}",
                )
            )
        else:
            checks.append(Check(f"{day}:{state_key}:validate_dr_winners", Status.WARN, "Missing DR dir"))

        if hz_dir.exists():
            cmd = ["python3", "scripts/tools/validate_hot_zones_winners.py", "--sharepack", str(hz_dir)]
            res = _run_cmd(cmd, env=env, timeout_s=120)
            checks.append(
                Check(
                    f"{day}:{state_key}:validate_hot_zones_winners",
                    Status.PASS if res.returncode == 0 else Status.FAIL,
                    "" if res.returncode == 0 else f"exit={res.returncode}",
                )
            )
        else:
            checks.append(Check(f"{day}:{state_key}:validate_hot_zones_winners", Status.WARN, "Missing Hot Zones dir"))

    report_lines.append("")
    return checks


def _audit_cross_day_freshness(dates: Sequence[str], metas: dict[str, dict], report_lines: list[str]) -> list[Check]:
    root = _repo_root()
    checks: list[Check] = []
    report_lines.append("## Cross-day freshness checks")

    if len(dates) < 2:
        report_lines.append("- SKIP: need at least 2 dates")
        checks.append(Check("cross_day", Status.SKIP, "Need >= 2 dates"))
        report_lines.append("")
        return checks

    for prev_day, curr_day in zip(dates, dates[1:]):
        prev_meta = metas.get(prev_day) or {}
        curr_meta = metas.get(curr_day) or {}
        prev_states = {s.get("state_key"): s for s in (prev_meta.get("states") or []) if isinstance(s, dict) and isinstance(s.get("state_key"), str)}
        curr_states = {s.get("state_key"): s for s in (curr_meta.get("states") or []) if isinstance(s, dict) and isinstance(s.get("state_key"), str)}
        shared_keys = sorted(set(prev_states.keys()) & set(curr_states.keys()))

        report_lines.append(f"### `{prev_day}` → `{curr_day}`")

        for state_key in shared_keys:
            prev_state = prev_states[state_key]
            curr_state = curr_states[state_key]

            prev_winners = prev_state.get("winners") or {}
            midday_prev = prev_winners.get("Midday")
            evening_prev = prev_winners.get("Evening")

            curr_draws_dir_rel = curr_state.get("aux_draws_dir")
            prev_draws_dir_rel = prev_state.get("aux_draws_dir")
            if not isinstance(curr_draws_dir_rel, str) or not isinstance(prev_draws_dir_rel, str):
                checks.append(Check(f"{state_key}:cross_day", Status.FAIL, "Missing aux_draws_dir in meta"))
                continue

            prev_draws_dir = root / prev_draws_dir_rel
            curr_draws_dir = root / curr_draws_dir_rel

            combined_prev_path = prev_draws_dir / f"{state_key.replace('4','')}_draws.csv"
            combined_curr_path = curr_draws_dir / f"{state_key.replace('4','')}_draws.csv"

            # Prefer using the resolved snapshot paths from Aux summary (more robust across labels)
            def resolved_paths(day: str, state_key: str) -> dict[str, Path]:
                meta = metas.get(day) or {}
                for s in meta.get("states") or []:
                    if isinstance(s, dict) and s.get("state_key") == state_key:
                        aux_summary_rel = s.get("aux_summary")
                        if isinstance(aux_summary_rel, str) and (root / aux_summary_rel).exists():
                            aux = json.loads(_read_text(root / aux_summary_rel))
                            snap = aux.get("draw_sources", {}).get("snapshot", {})
                            out = {}
                            for k in ("combined", "midday", "evening"):
                                rp = snap.get(k, {}).get("resolved_path")
                                if isinstance(rp, str):
                                    out[k] = Path(rp)
                            return out
                return {}

            prev_res = resolved_paths(prev_day, state_key)
            curr_res = resolved_paths(curr_day, state_key)
            if not prev_res or not curr_res:
                checks.append(Check(f"{state_key}:cross_day_paths", Status.FAIL, "Missing resolved snapshot paths"))
                continue

            # Read draws (limit for performance; enough for shift proof)
            try:
                prev_combined = _read_draws_csv(prev_res["combined"], max_rows=50)
                curr_combined = _read_draws_csv(curr_res["combined"], max_rows=52)
                prev_midday = _read_draws_csv(prev_res["midday"], max_rows=50)
                curr_midday = _read_draws_csv(curr_res["midday"], max_rows=51)
                prev_evening = _read_draws_csv(prev_res["evening"], max_rows=50)
                curr_evening = _read_draws_csv(curr_res["evening"], max_rows=51)
            except Exception as e:
                checks.append(Check(f"{state_key}:cross_day_read", Status.FAIL, f"{e}"))
                continue

            expected_midday = [midday_prev] if isinstance(midday_prev, str) else None
            expected_evening = [evening_prev] if isinstance(evening_prev, str) else None
            if isinstance(midday_prev, str) and isinstance(evening_prev, str):
                # Combined ordering is newest-first; most states serialize Evening then Midday for the same date.
                expected_combined = [evening_prev, midday_prev]
                expected_combined_alt = [midday_prev, evening_prev]
            elif isinstance(midday_prev, str):
                expected_combined = [midday_prev]
                expected_combined_alt = None
            elif isinstance(evening_prev, str):
                expected_combined = [evening_prev]
                expected_combined_alt = None
            else:
                expected_combined = None
                expected_combined_alt = None

            # Midday/Evening should shift by 1 when that winner exists.
            checks.append(
                _check_shift(
                    label=f"{prev_day}->{curr_day}:{state_key}:midday_shift",
                    prev=prev_midday,
                    curr=curr_midday,
                    expected_new=expected_midday,
                    preferred_shift=1,
                    shift_candidates=(1, 0),
                    prefix_k=20,
                )
            )
            checks.append(
                _check_shift(
                    label=f"{prev_day}->{curr_day}:{state_key}:evening_shift",
                    prev=prev_evening,
                    curr=curr_evening,
                    expected_new=expected_evening,
                    preferred_shift=1,
                    shift_candidates=(1, 0),
                    prefix_k=20,
                )
            )

            # Combined shifts by 2 when both winners exist.
            if expected_combined is None:
                combined_check = _check_shift(
                    label=f"{prev_day}->{curr_day}:{state_key}:combined_shift",
                    prev=prev_combined,
                    curr=curr_combined,
                    expected_new=None,
                    preferred_shift=2,
                    shift_candidates=(2, 1, 0),
                    prefix_k=20,
                )
                checks.append(combined_check)
            else:
                combined_check = _check_shift(
                    label=f"{prev_day}->{curr_day}:{state_key}:combined_shift",
                    prev=prev_combined,
                    curr=curr_combined,
                    expected_new=expected_combined,
                    preferred_shift=len(expected_combined),
                    shift_candidates=(len(expected_combined),),
                    prefix_k=20,
                )
                if combined_check.status == Status.FAIL and expected_combined_alt is not None:
                    combined_check_alt = _check_shift(
                        label=f"{prev_day}->{curr_day}:{state_key}:combined_shift",
                        prev=prev_combined,
                        curr=curr_combined,
                        expected_new=expected_combined_alt,
                        preferred_shift=len(expected_combined_alt),
                        shift_candidates=(len(expected_combined_alt),),
                        prefix_k=20,
                    )
                    if combined_check_alt.status == Status.PASS:
                        checks.append(Check(f"{prev_day}->{curr_day}:{state_key}:combined_shift", Status.WARN, "Ordering is Midday→Evening (unexpected) but shift is correct"))
                    else:
                        checks.append(combined_check)
                else:
                    checks.append(combined_check)

        report_lines.append("")

    return checks


def _summarize(checks: Iterable[Check]) -> dict[str, int]:
    summary = {Status.PASS: 0, Status.WARN: 0, Status.FAIL: 0, Status.SKIP: 0}
    for c in checks:
        summary[c.status] = summary.get(c.status, 0) + 1
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit sharepacks corpus integrity (provenance, alignment, freshness).")
    parser.add_argument(
        "--dates",
        nargs="*",
        default=["2025-06-21", "2025-06-22", "2025-06-23"],
        help="Results dates D to audit (folder names under sharepacks/). Default: 2025-06-21 2025-06-22 2025-06-23",
    )
    parser.add_argument(
        "--out",
        default=None,
        help="Optional output markdown path (default: reports/audit/sharepacks_audit_<timestamp>.md).",
    )
    parser.add_argument(
        "--no-validators",
        action="store_true",
        help="Skip running validators (only provenance + cross-day freshness).",
    )
    args = parser.parse_args()

    dates = [d.strip() for d in args.dates if d.strip()]
    root = _repo_root()
    now_utc = dt.datetime.now(dt.timezone.utc)
    out_path = Path(args.out) if args.out else root / "reports" / "audit" / f"sharepacks_audit_{now_utc.strftime('%Y%m%d_%H%M%S')}.md"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    report_lines: list[str] = []
    report_lines.append(f"# Sharepacks Corpus Audit ({now_utc.isoformat()}Z)")
    report_lines.append("")
    report_lines.append("Scope:")
    report_lines.append(f"- Dates: {', '.join([f'`{d}`' for d in dates])}")
    report_lines.append("")

    all_checks: list[Check] = []
    metas: dict[str, dict] = {}

    # Per-day checks
    for day in dates:
        day_checks, meta = _audit_day(day, report_lines)
        all_checks.extend(day_checks)
        if meta:
            metas[day] = meta
        if meta and not args.no_validators:
            all_checks.extend(_audit_validators(day, meta, report_lines))

    # Cross-day freshness checks
    if metas:
        all_checks.extend(_audit_cross_day_freshness(dates, metas, report_lines))

    summary = _summarize(all_checks)
    report_lines.insert(2, f"Summary: PASS={summary[Status.PASS]} WARN={summary[Status.WARN]} FAIL={summary[Status.FAIL]} SKIP={summary[Status.SKIP]}")
    report_lines.insert(3, "")

    # Failure index
    failures = [c for c in all_checks if c.status == Status.FAIL]
    warnings = [c for c in all_checks if c.status == Status.WARN]
    skips = [c for c in all_checks if c.status == Status.SKIP]
    if failures:
        report_lines.append("## FAILURES")
        for c in failures:
            report_lines.append(f"- **{c.name}**: {c.details}")
        report_lines.append("")
    if warnings:
        report_lines.append("## WARNINGS")
        for c in warnings:
            report_lines.append(f"- **{c.name}**: {c.details}")
        report_lines.append("")
    if skips:
        report_lines.append("## SKIPS")
        for c in skips:
            report_lines.append(f"- **{c.name}**: {c.details}")
        report_lines.append("")

    out_path.write_text("\n".join(report_lines) + "\n", encoding="utf-8")
    print(f"[audit] wrote {out_path}")
    print(f"[audit] Summary: PASS={summary[Status.PASS]} WARN={summary[Status.WARN]} FAIL={summary[Status.FAIL]} SKIP={summary[Status.SKIP]}")

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
