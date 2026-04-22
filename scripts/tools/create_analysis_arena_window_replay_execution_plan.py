#!/usr/bin/env python3
"""Create a read-only execution plan for an Analysis Arena window replay.

The plan stops before running the replay. Its job is to freeze the namespace,
source coverage, command order, and guardrails so a same-window replay can be
approved and executed without overwriting the preserved baseline.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.tools.analysis_arena_window_utils import safe_rel


DEFAULT_RUNS2_ROOT = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS_2"
DEFAULT_FINAL_DOCS = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "final docs"
DEFAULT_BASELINE_WINDOW = DEFAULT_RUNS2_ROOT / "WINDOW_2026-03-09_to_2026-03-23"
DEFAULT_HISTORY_ROOT = REPO_ROOT / "data" / "history"
DEFAULT_RESULTS_ROOT = REPO_ROOT / "data" / "results"
DEFAULT_BONUS_ROOT = REPO_ROOT / "data" / "results_bonus"
DEFAULT_PREDICTIVE_SHAREPACKS_ROOT = REPO_ROOT / "sharepacks" / "_predictive"
DEFAULT_TRUTH_SHAREPACKS_ROOT = REPO_ROOT / "sharepacks"
DEFAULT_LABEL = "march_2026_15day_replay_v2"
DEFAULT_WINDOW_NAME = "WINDOW_2026-03-09_to_2026-03-23"
DEFAULT_CANDIDATE_SHAREPACKS = REPO_ROOT / "sharepacks" / "_predictive_replay" / DEFAULT_LABEL
DEFAULT_STEM = "AAT9_ANALYSIS_ARENA__MARCH_RUN2_EXECUTION_PREP"
DEFAULT_BASELINE_MANIFEST_STEM = "AAT9_ANALYSIS_ARENA__MARCH_RUN2_BASELINE_MANIFEST"


def _parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--run-label", default=DEFAULT_LABEL)
    ap.add_argument("--start-date", default="2026-03-09", help="Replay results/window start date.")
    ap.add_argument("--end-date", default="2026-03-23", help="Replay results/window end date.")
    ap.add_argument("--history-start-date", default="2026-03-08", help="Replay history start date H.")
    ap.add_argument("--history-end-date", default="2026-03-22", help="Replay history end date H.")
    ap.add_argument("--baseline-window-root", default=str(DEFAULT_BASELINE_WINDOW))
    ap.add_argument("--baseline-cycle-root", default=str(DEFAULT_RUNS2_ROOT))
    ap.add_argument("--runs2-root", default=str(DEFAULT_RUNS2_ROOT))
    ap.add_argument("--history-root", default=str(DEFAULT_HISTORY_ROOT))
    ap.add_argument("--results-root", default=str(DEFAULT_RESULTS_ROOT))
    ap.add_argument("--bonus-results-root", default=str(DEFAULT_BONUS_ROOT))
    ap.add_argument("--candidate-sharepacks-root", default=str(DEFAULT_CANDIDATE_SHAREPACKS))
    ap.add_argument("--truth-sharepacks-root", default=str(DEFAULT_TRUTH_SHAREPACKS_ROOT))
    ap.add_argument("--profile", default="tool_only")
    ap.add_argument("--experiment-tag", default="arena_v0")
    ap.add_argument("--board-name", default="analysis_arena_day_review")
    ap.add_argument("--top-n-stable", type=int, default=10)
    ap.add_argument("--decay-upload-days-total", type=int, default=5)
    ap.add_argument("--windowed-draws", type=int, default=5)
    ap.add_argument("--out-md", default="")
    ap.add_argument("--out-json", default="")
    ap.add_argument("--out-csv", default="")
    ap.add_argument("--force", action="store_true", help="Overwrite existing outputs.")
    return ap.parse_args()


def _resolve_path(value: str | Path) -> Path:
    path = Path(value).expanduser()
    if not path.is_absolute():
        path = (REPO_ROOT / path).resolve()
    return path


def _parse_date(value: str) -> date:
    try:
        return datetime.strptime(str(value), "%Y-%m-%d").date()
    except Exception as exc:
        raise SystemExit(f"Invalid date {value!r}; expected YYYY-MM-DD") from exc


def _date_range(start: date, end: date) -> List[date]:
    if end < start:
        raise SystemExit(f"Invalid range: {start.isoformat()}..{end.isoformat()}")
    out: List[date] = []
    current = start
    while current <= end:
        out.append(current)
        current += timedelta(days=1)
    return out


def _shell_join(parts: Sequence[str | Path]) -> str:
    out: List[str] = []
    for part in parts:
        text = str(part)
        if not text:
            continue
        if any(ch.isspace() for ch in text) or any(ch in text for ch in ("'", '"', "(", ")", "&", ";")):
            out.append("'" + text.replace("'", "'\"'\"'") + "'")
        else:
            out.append(text)
    return " ".join(out)


def _default_paths() -> Dict[str, Path]:
    return {
        "md": DEFAULT_FINAL_DOCS / f"{DEFAULT_STEM}.md",
        "json": DEFAULT_FINAL_DOCS / f"{DEFAULT_STEM}.json",
        "csv": DEFAULT_FINAL_DOCS / f"{DEFAULT_STEM}.csv",
    }


def _write_text(path: Path, text: str, *, force: bool) -> None:
    if path.exists() and not force:
        raise SystemExit(f"Refusing to overwrite existing file without --force: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _write_json(path: Path, payload: Any, *, force: bool) -> None:
    _write_text(path, json.dumps(payload, indent=2, sort_keys=True) + "\n", force=force)


def _write_csv(path: Path, rows: Sequence[Dict[str, Any]], *, force: bool) -> None:
    if path.exists() and not force:
        raise SystemExit(f"Refusing to overwrite existing file without --force: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = ["sequence", "phase", "purpose", "writes_to", "command", "dry_run_command"]
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def _history_file_exists(history_root: Path, item: date) -> bool:
    candidates = [
        history_root / f"Pick3StatsC4_{item.isoformat()}.xlsm",
        history_root / f"Pick3StatsC4_{item.isoformat().replace('-', '_')}.xlsm",
    ]
    return any(path.exists() for path in candidates)


def _dated_txt_exists(root: Path, item: date) -> bool:
    return (root / f"{item.isoformat()}.txt").exists()


def _missing_dates(dates: Iterable[date], exists_fn) -> List[str]:
    return [item.isoformat() for item in dates if not exists_fn(item)]


def _is_relative_to(child: Path, parent: Path) -> bool:
    try:
        child.resolve().relative_to(parent.resolve())
        return True
    except ValueError:
        return False


def _path_equal(left: Path, right: Path) -> bool:
    return left.resolve() == right.resolve()


def _has_path_part(path: Path, part: str) -> bool:
    return part in path.resolve().parts


def _plan_write_paths(commands: Sequence[Dict[str, Any]]) -> List[Path]:
    paths: List[Path] = []
    for row in commands:
        text = str(row.get("writes_to") or "").strip()
        if not text:
            continue
        paths.append(_resolve_path(text))
    return paths


def _add_command(
    rows: List[Dict[str, Any]],
    *,
    phase: str,
    purpose: str,
    writes_to: Path | str,
    parts: Sequence[str | Path],
    dry_run: bool = False,
) -> None:
    command = _shell_join(parts)
    dry_parts = list(parts)
    if dry_run and "--dry-run" not in [str(item) for item in dry_parts]:
        dry_parts.append("--dry-run")
    rows.append(
        {
            "sequence": len(rows) + 1,
            "phase": phase,
            "purpose": purpose,
            "writes_to": safe_rel(_resolve_path(writes_to)) if isinstance(writes_to, (Path, str)) and str(writes_to) else "",
            "command": command,
            "dry_run_command": _shell_join(dry_parts) if dry_run else command,
        }
    )


def _grade_commands(
    *,
    rows: List[Dict[str, Any]],
    dates: Sequence[date],
    candidate_sharepacks: Path,
    control_arm_dir: Path,
    profile: str,
    experiment_tag: str,
    force: bool,
) -> None:
    force_parts = ["--force"] if force else []
    out_suffix = f"__{profile}" if profile != "mixed" else ""
    tag_suffix = f"__{experiment_tag}" if experiment_tag else ""
    for item in dates:
        d = item.isoformat()
        _add_command(
            rows,
            phase="control_arm_grading",
            purpose=f"grade candidate universe for {d} into isolated Run 2 control-arm dir",
            writes_to=control_arm_dir,
            parts=[
                "python3",
                "scripts/tools/grade_candidate_universe.py",
                "--date",
                d,
                "--sharepacks-root",
                candidate_sharepacks,
                "--profile",
                profile,
                "--experiment-tag",
                experiment_tag,
                "--out-csv",
                control_arm_dir / f"{d}__CANDIDATE_UNIVERSE_GRADE{out_suffix}{tag_suffix}.csv",
                "--out-md",
                control_arm_dir / f"{d}__CANDIDATE_UNIVERSE_GRADE{out_suffix}{tag_suffix}.md",
                *force_parts,
            ],
            dry_run=False,
        )
        _add_command(
            rows,
            phase="control_arm_grading",
            purpose=f"grade play card for {d} into isolated Run 2 control-arm dir",
            writes_to=control_arm_dir,
            parts=[
                "python3",
                "scripts/tools/grade_play_card.py",
                "--date",
                d,
                "--sharepacks-root",
                candidate_sharepacks,
                "--profile",
                profile,
                "--experiment-tag",
                experiment_tag,
                "--out-csv",
                control_arm_dir / f"{d}__PLAY_CARD_GRADE{out_suffix}{tag_suffix}.csv",
                "--out-md",
                control_arm_dir / f"{d}__PLAY_CARD_GRADE{out_suffix}{tag_suffix}.md",
                *force_parts,
            ],
            dry_run=False,
        )


def build_payload(
    *,
    run_label: str,
    start_date: date,
    end_date: date,
    history_start: date,
    history_end: date,
    baseline_window_root: Path,
    baseline_cycle_root: Path,
    runs2_root: Path,
    history_root: Path,
    results_root: Path,
    bonus_results_root: Path,
    candidate_sharepacks_root: Path,
    truth_sharepacks_root: Path,
    profile: str,
    experiment_tag: str,
    board_name: str,
    top_n_stable: int,
    decay_upload_days_total: int,
    windowed_draws: int,
) -> Dict[str, Any]:
    window_dates = _date_range(start_date, end_date)
    history_dates = _date_range(history_start, history_end)
    tail_dates = _date_range(start_date, end_date + timedelta(days=max(0, decay_upload_days_total - 1)))
    window_name = f"WINDOW_{start_date.isoformat()}_to_{end_date.isoformat()}"

    replay_root = runs2_root / "REPLAY" / run_label
    candidate_window_root = replay_root / window_name
    candidate_analysis_subdir = Path("REPLAY") / run_label / window_name / "ANALYSIS_ARENA"
    candidate_validation_subdir = Path("REPLAY") / run_label / window_name / "VALIDATION"
    candidate_control_arm_dir = candidate_window_root / "CONTROL_ARM"

    source_coverage = {
        "history_missing": _missing_dates(history_dates, lambda item: _history_file_exists(history_root, item)),
        "results_missing": _missing_dates(window_dates, lambda item: _dated_txt_exists(results_root, item)),
        "tail_results_missing": _missing_dates(tail_dates, lambda item: _dated_txt_exists(results_root, item)),
        "bonus_results_missing": _missing_dates(tail_dates, lambda item: _dated_txt_exists(bonus_results_root, item)),
    }
    source_coverage["ready"] = not any(source_coverage.values())

    namespace_status = {
        "baseline_window_exists": baseline_window_root.exists(),
        "baseline_cycle_exists": baseline_cycle_root.exists(),
        "candidate_replay_root_exists": replay_root.exists(),
        "candidate_window_root_exists": candidate_window_root.exists(),
        "candidate_sharepacks_root_exists": candidate_sharepacks_root.exists(),
        "candidate_control_arm_exists": candidate_control_arm_dir.exists(),
        "candidate_window_equals_baseline_window": _path_equal(candidate_window_root, baseline_window_root),
        "candidate_window_inside_baseline_window": _is_relative_to(candidate_window_root, baseline_window_root),
        "baseline_window_inside_candidate_window": _is_relative_to(baseline_window_root, candidate_window_root),
        "candidate_replay_path_has_run_label": _has_path_part(replay_root, run_label),
        "candidate_window_path_has_run_label": _has_path_part(candidate_window_root, run_label),
        "candidate_sharepacks_path_has_run_label": _has_path_part(candidate_sharepacks_root, run_label),
        "candidate_sharepacks_is_production_predictive": _path_equal(candidate_sharepacks_root, DEFAULT_PREDICTIVE_SHAREPACKS_ROOT)
        or _is_relative_to(candidate_sharepacks_root, DEFAULT_PREDICTIVE_SHAREPACKS_ROOT),
        "safe_to_create_candidate_namespace": not candidate_window_root.exists() and not candidate_sharepacks_root.exists(),
    }

    commands: List[Dict[str, Any]] = []
    _add_command(
        commands,
        phase="preflight",
        purpose="freeze March baseline manifest immediately before Run 2 execution",
        writes_to=DEFAULT_FINAL_DOCS,
        parts=[
            "python3",
            "scripts/tools/run_analysis_arena_cycle.py",
            "window-replay-baseline-manifest",
            "--baseline-window-root",
            baseline_window_root,
            "--baseline-cycle-root",
            baseline_cycle_root,
            "--evidence-tier",
            "same_window_replay",
            "--run-label",
            run_label,
            "--no-receipt",
            "--force",
        ],
    )
    _add_command(
        commands,
        phase="preflight",
        purpose="regenerate read-only replay readiness before executing Run 2",
        writes_to=DEFAULT_FINAL_DOCS,
        parts=[
            "python3",
            "scripts/tools/run_analysis_arena_cycle.py",
            "window-replay-readiness",
            "--runs2-root",
            runs2_root,
            "--no-receipt",
            "--force",
        ],
    )
    _add_command(
        commands,
        phase="preflight",
        purpose="preserve pending baseline-vs-candidate comparison state",
        writes_to=DEFAULT_FINAL_DOCS,
        parts=[
            "python3",
            "scripts/tools/run_analysis_arena_cycle.py",
            "window-replay-compare",
            "--run-label",
            f"{run_label}_pending",
            "--no-receipt",
            "--force",
        ],
    )
    _add_command(
        commands,
        phase="namespace_setup",
        purpose="create isolated Run 2 control-arm output directory before direct grade commands",
        writes_to=candidate_control_arm_dir,
        parts=["mkdir", "-p", candidate_control_arm_dir],
    )
    _add_command(
        commands,
        phase="pre",
        purpose="build Run 2 predictive sharepacks and Analysis Arena pre artifacts in isolated namespace",
        writes_to=candidate_window_root / "ANALYSIS_ARENA",
        parts=[
            "python3",
            "scripts/tools/run_analysis_arena_cycle.py",
            "pre-range",
            "--start-history-date",
            history_start.isoformat(),
            "--end-history-date",
            history_end.isoformat(),
            "--sharepacks-root",
            candidate_sharepacks_root,
            "--profile",
            profile,
            "--experiment-tag",
            experiment_tag,
            "--board-name",
            board_name,
            "--runs-subdir",
            candidate_analysis_subdir,
            "--top-n-stable",
            str(top_n_stable),
            "--write-audit-evidence",
            "--play-card-write-md",
            "--force",
        ],
        dry_run=True,
    )

    _grade_commands(
        rows=commands,
        dates=window_dates,
        candidate_sharepacks=candidate_sharepacks_root,
        control_arm_dir=candidate_control_arm_dir,
        profile=profile,
        experiment_tag=experiment_tag,
        force=True,
    )
    windowed_prefix = f"{start_date.isoformat()}_to_{end_date.isoformat()}__PLAY_CARD_WINDOWED_GRADE__{profile}__{experiment_tag}__N{windowed_draws}"
    _add_command(
        commands,
        phase="control_arm_grading",
        purpose="grade candidate play cards across the replay window with isolated windowed outputs",
        writes_to=candidate_control_arm_dir,
        parts=[
            "python3",
            "scripts/tools/grade_play_card_windowed.py",
            "--start-date",
            start_date.isoformat(),
            "--end-date",
            end_date.isoformat(),
            "--window-draws",
            str(windowed_draws),
            "--sharepacks-root",
            candidate_sharepacks_root,
            "--profile",
            profile,
            "--experiment-tag",
            experiment_tag,
            "--out-csv",
            candidate_control_arm_dir / f"{windowed_prefix}.csv",
            "--out-md",
            candidate_control_arm_dir / f"{windowed_prefix}.md",
            "--out-rollup-csv",
            candidate_control_arm_dir / f"play_card_windowed_rollup__{profile}__{experiment_tag}__N{windowed_draws}__{start_date.isoformat()}_to_{end_date.isoformat()}.csv",
            "--out-rollup-md",
            candidate_control_arm_dir / f"play_card_windowed_rollup__{profile}__{experiment_tag}__N{windowed_draws}__{start_date.isoformat()}_to_{end_date.isoformat()}.md",
            "--force",
        ],
    )
    _add_command(
        commands,
        phase="post",
        purpose="build Run 2 validation reports while reading Run 2 Analysis Arena artifacts and isolated control-arm grades",
        writes_to=candidate_window_root / "VALIDATION",
        parts=[
            "python3",
            "scripts/tools/run_analysis_arena_cycle.py",
            "post-range",
            "--start-date",
            start_date.isoformat(),
            "--end-date",
            end_date.isoformat(),
            "--sharepacks-root",
            candidate_sharepacks_root,
            "--truth-sharepacks-root",
            truth_sharepacks_root,
            "--profile",
            profile,
            "--experiment-tag",
            experiment_tag,
            "--board-name",
            board_name,
            "--runs-subdir",
            candidate_validation_subdir,
            "--analysis-runs-subdir",
            candidate_analysis_subdir,
            "--control-arm-runs-dir",
            candidate_control_arm_dir,
            "--skip-candidate-universe-grade",
            "--skip-play-card-grade",
            "--skip-windowed",
            "--force",
        ],
        dry_run=True,
    )
    _add_command(
        commands,
        phase="window_close",
        purpose="close Run 2 window with standard window reports and decay carryover",
        writes_to=candidate_window_root,
        parts=[
            "python3",
            "scripts/tools/run_analysis_arena_cycle.py",
            "window-close",
            "--window-root",
            candidate_window_root,
            "--runs-root",
            candidate_control_arm_dir,
            "--sharepacks-root",
            candidate_sharepacks_root,
            "--profile",
            profile,
            "--experiment-tag",
            experiment_tag,
            "--include-decay",
            "--results-root",
            results_root,
            "--decay-upload-days-total",
            str(decay_upload_days_total),
            "--force",
        ],
        dry_run=True,
    )
    for phase, script in [
        ("post_run_audit", "scripts/tools/create_window_evidence_utilization_audit.py"),
        ("post_run_audit", "scripts/tools/create_window_audit_interpretation_report.py"),
        ("post_run_audit", "scripts/tools/create_window_stage2_signal_exposure_audit.py"),
        ("post_run_audit", "scripts/tools/create_window_stage2b_signal_stack_analysis.py"),
    ]:
        parts: List[str | Path] = ["python3", script, "--window-root", candidate_window_root]
        if script.endswith("create_window_stage2b_signal_stack_analysis.py"):
            parts += ["--runs2-dir", replay_root]
        parts.append("--force")
        _add_command(
            commands,
            phase=phase,
            purpose=f"generate {Path(script).stem} for Run 2",
            writes_to=candidate_window_root,
            parts=parts,
            dry_run=False,
        )
    _add_command(
        commands,
        phase="post_run_audit",
        purpose="generate Stage 2B cross-window rollup inside candidate replay root",
        writes_to=replay_root,
        parts=[
            "python3",
            "scripts/tools/create_stage2b_cross_window_stack_rollup.py",
            "--runs2-dir",
            replay_root,
            "--output-dir",
            replay_root,
            "--force",
        ],
    )

    for cmd_name, purpose in [
        ("stage3-decision-workbench", "regenerate Stage 3 decision workbench from Run 2 window evidence"),
        ("stage4-fixture-replay", "regenerate Stage 4 fixture replay from Run 2 Stage 3 queue"),
        ("stage4b-replay-readback", "regenerate Stage 4B readback from Run 2 fixture evidence"),
        ("stage4c-shadow-translator", "regenerate Stage 4C shadow translator prototype from Run 2 evidence"),
        ("stage5-shadow-evaluator", "regenerate Stage 5 shadow translator evaluator from Run 2 prototype outputs"),
        ("stage5-readback", "regenerate Stage 5 readback from Run 2 evaluator outputs"),
        ("stage6a-shadow-spec", "regenerate Stage 6A shadow translator spec from Run 2 readback"),
        ("stage6b-shadow-replay", "regenerate Stage 6B shadow replay from Run 2 Stage 6A/5 evidence"),
        ("stage6b-readback", "regenerate Stage 6B readback from Run 2 replay outputs"),
        ("stage6c-confirmation-protocol", "regenerate Stage 6C confirmation protocol from Run 2 readback"),
        ("stage6d-restraint-calibration", "regenerate Stage 6D restraint calibration from Run 2 evidence"),
        ("stage6e-support-narrowing", "regenerate Stage 6E support narrowing from Run 2 evidence"),
        ("stage6f-decision-atlas", "regenerate Stage 6F decision atlas from Run 2 evidence"),
        ("stage7a-fresh-confirmation-scaffold", "regenerate Stage 7A scaffold from Run 2 evidence"),
        ("stage7b-fixture-replay-harness", "regenerate Stage 7B fixture replay harness from Run 2 evidence"),
    ]:
        _add_command(
            commands,
            phase="stage3_to_7b",
            purpose=purpose,
            writes_to=replay_root,
            parts=[
                "python3",
                "scripts/tools/run_analysis_arena_cycle.py",
                cmd_name,
                "--runs2-root",
                replay_root,
                "--output-dir",
                replay_root,
                "--force",
            ],
            dry_run=True,
        )
    _add_command(
        commands,
        phase="comparison",
        purpose="compare preserved March baseline against Run 2 candidate after the replay exists",
        writes_to=DEFAULT_FINAL_DOCS,
        parts=[
            "python3",
            "scripts/tools/run_analysis_arena_cycle.py",
            "window-replay-compare",
            "--baseline-window-root",
            baseline_window_root,
            "--candidate-window-root",
            candidate_window_root,
            "--baseline-cycle-root",
            baseline_cycle_root,
            "--candidate-cycle-root",
            replay_root,
            "--evidence-tier",
            "same_window_replay",
            "--run-label",
            run_label,
            "--require-candidate-complete",
            "--force",
        ],
    )

    blocked: List[str] = []
    plan_write_paths = _plan_write_paths(commands)
    writes_inside_baseline = sorted(
        safe_rel(path) for path in plan_write_paths if _path_equal(path, baseline_window_root) or _is_relative_to(path, baseline_window_root)
    )
    namespace_status["planned_write_paths_inside_baseline_window"] = writes_inside_baseline
    if not baseline_window_root.exists():
        blocked.append("baseline window root is missing")
    if not baseline_cycle_root.exists():
        blocked.append("baseline cycle root is missing")
    if namespace_status["candidate_window_equals_baseline_window"]:
        blocked.append("candidate window root equals preserved baseline window root")
    if namespace_status["candidate_window_inside_baseline_window"] and not namespace_status["candidate_window_equals_baseline_window"]:
        blocked.append("candidate window root is inside preserved baseline window root")
    if namespace_status["baseline_window_inside_candidate_window"] and not namespace_status["candidate_window_equals_baseline_window"]:
        blocked.append("preserved baseline window root is inside candidate window root")
    if not namespace_status["candidate_replay_path_has_run_label"]:
        blocked.append("candidate replay root does not include the Run 2 run label")
    if not namespace_status["candidate_window_path_has_run_label"]:
        blocked.append("candidate window root does not include the Run 2 run label")
    if not namespace_status["candidate_sharepacks_path_has_run_label"]:
        blocked.append("candidate sharepacks root does not include the Run 2 run label")
    if namespace_status["candidate_sharepacks_is_production_predictive"]:
        blocked.append("candidate sharepacks root points at or inside production predictive sharepacks")
    if writes_inside_baseline:
        blocked.append("planned command writes inside preserved baseline window root: " + ", ".join(writes_inside_baseline))
    for key, values in source_coverage.items():
        if key != "ready" and values:
            blocked.append(f"{key}: {', '.join(values)}")
    if candidate_window_root.exists():
        blocked.append("candidate window root already exists; archive or choose a new run label before execution")
    if candidate_sharepacks_root.exists():
        blocked.append("candidate sharepacks root already exists; archive or choose a new run label before execution")

    return {
        "schema_version": "analysis_arena_window_replay_execution_plan/v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "run_label": run_label,
        "evidence_tier": "same_window_replay",
        "status": "ready_for_approval_to_run" if not blocked else "blocked_until_prep_items_resolved",
        "stage8_permission": "blocked",
        "window": {
            "name": window_name,
            "start_date": start_date.isoformat(),
            "end_date": end_date.isoformat(),
            "history_start_date": history_start.isoformat(),
            "history_end_date": history_end.isoformat(),
            "decay_upload_days_total": decay_upload_days_total,
            "tail_results_end_date": tail_dates[-1].isoformat(),
        },
        "namespaces": {
            "baseline_window_root": safe_rel(baseline_window_root),
            "baseline_cycle_root": safe_rel(baseline_cycle_root),
            "candidate_replay_root": safe_rel(replay_root),
            "candidate_window_root": safe_rel(candidate_window_root),
            "candidate_analysis_subdir": str(candidate_analysis_subdir),
            "candidate_validation_subdir": str(candidate_validation_subdir),
            "candidate_control_arm_dir": safe_rel(candidate_control_arm_dir),
            "candidate_sharepacks_root": safe_rel(candidate_sharepacks_root),
            "truth_sharepacks_root": safe_rel(truth_sharepacks_root),
        },
        "source_coverage": source_coverage,
        "namespace_status": namespace_status,
        "baseline_manifest": {
            "md": safe_rel(DEFAULT_FINAL_DOCS / f"{DEFAULT_BASELINE_MANIFEST_STEM}.md"),
            "json": safe_rel(DEFAULT_FINAL_DOCS / f"{DEFAULT_BASELINE_MANIFEST_STEM}.json"),
            "csv": safe_rel(DEFAULT_FINAL_DOCS / f"{DEFAULT_BASELINE_MANIFEST_STEM}.csv"),
            "created_by_first_preflight_command": True,
        },
        "blockers": blocked,
        "commands": commands,
        "guardrails": [
            "Do not write into the preserved baseline window root.",
            "Do not write Run 2 predictive sharepacks into sharepacks/_predictive.",
            "Run 2 is same-window replay evidence only.",
            "Same-window replay cannot unlock Stage 8A or live scoring/candidate/budget changes.",
            "Review degraded or contradicted comparison rows before using Run 2 as development evidence.",
        ],
    }


def _render_markdown(payload: Dict[str, Any], *, csv_path: Path) -> str:
    namespaces = payload["namespaces"]
    coverage = payload["source_coverage"]
    ns = payload["namespace_status"]
    manifest = payload.get("baseline_manifest") or {}
    commands = payload["commands"]
    blockers = payload["blockers"]
    window_name = str((payload.get("window") or {}).get("name") or DEFAULT_WINDOW_NAME)
    phase_counts: Dict[str, int] = {}
    for row in commands:
        phase = str(row.get("phase") or "")
        phase_counts[phase] = phase_counts.get(phase, 0) + 1

    lines: List[str] = [
        "# AAT9 Analysis Arena - March Run 2 Execution Prep",
        "",
        "## 1. Verdict",
        "",
        f"- run_label: `{payload['run_label']}`",
        f"- evidence_tier: `{payload['evidence_tier']}`",
        f"- status: `{payload['status']}`",
        f"- stage8_permission: `{payload['stage8_permission']}`",
        f"- command_count: `{len(commands)}`",
        f"- command_csv: `{safe_rel(csv_path)}`",
        "",
        "Operational read:",
        "",
        "- March 09-23 is approved here only as a controlled same-window Run 2 replay target.",
        "- This prep does not execute the replay.",
        "- The actual run should be executed only after reviewing this plan and approving the command sequence.",
        "",
        "## 2. Namespaces",
        "",
        f"- baseline_window_root: `{namespaces['baseline_window_root']}`",
        f"- candidate_replay_root: `{namespaces['candidate_replay_root']}`",
        f"- candidate_window_root: `{namespaces['candidate_window_root']}`",
        f"- candidate_sharepacks_root: `{namespaces['candidate_sharepacks_root']}`",
        f"- candidate_control_arm_dir: `{namespaces['candidate_control_arm_dir']}`",
        "",
        "Important routing choice:",
        "",
        f"- The Run 2 window keeps the exact folder name `{window_name}` inside a nested replay root.",
        "- This is intentional because Stage 3/4 fixture tools discover exact `WINDOW_<start>_to_<end>` names and would ignore a suffixed `__RUN2` folder.",
        "",
        "## 3. Source Coverage",
        "",
        f"- history_missing: `{', '.join(coverage['history_missing']) or 'none'}`",
        f"- results_missing: `{', '.join(coverage['results_missing']) or 'none'}`",
        f"- tail_results_missing: `{', '.join(coverage['tail_results_missing']) or 'none'}`",
        f"- bonus_results_missing: `{', '.join(coverage['bonus_results_missing']) or 'none'}`",
        f"- source_ready: `{str(coverage['ready']).lower()}`",
        "",
        "## 4. Namespace Safety",
        "",
    ]
    for key, value in ns.items():
        lines.append(f"- {key}: `{str(value).lower()}`")

    lines += [
        "",
        "## 5. Baseline Manifest",
        "",
        f"- markdown: `{manifest.get('md', '')}`",
        f"- json: `{manifest.get('json', '')}`",
        f"- csv: `{manifest.get('csv', '')}`",
        "- created_by_first_preflight_command: `true`",
        "",
        "## 6. Command Phases",
        "",
    ]
    for phase, count in phase_counts.items():
        lines.append(f"- `{phase}`: `{count}` commands")

    lines += [
        "",
        "The full executable command list is in the CSV. The major order is:",
        "",
        "1. baseline manifest freeze, replay readiness, and pending comparison preflight",
        "2. isolated pre-range into Run 2 sharepacks and Run 2 Analysis Arena folder",
        "3. isolated control-arm grading into Run 2 `CONTROL_ARM`",
        "4. isolated post-range into Run 2 `VALIDATION`",
        "5. window close plus decay",
        "6. post-run audit and Stage 2B",
        "7. Stage 3 through Stage 7B regeneration",
        "8. candidate-complete baseline-vs-Run-2 comparison",
        "",
        "## 7. Blockers",
        "",
    ]
    if blockers:
        for item in blockers:
            lines.append(f"- {item}")
    else:
        lines.append("- none")

    lines += [
        "",
        "## 8. Guardrails",
        "",
    ]
    for item in payload["guardrails"]:
        lines.append(f"- {item}")

    lines += [
        "",
        "## 9. Run-Ready Meaning",
        "",
        "If blockers are `none`, the system is ready for a separately approved March Run 2 execution.",
        "That still means same-window replay only. It can measure regression, reproducibility, traceability improvements, and changed Stage 6B-7B posture, but it cannot substitute for true fresh-window confirmation.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    args = _parse_args()
    defaults = _default_paths()
    out_md = _resolve_path(args.out_md) if args.out_md else defaults["md"]
    out_json = _resolve_path(args.out_json) if args.out_json else defaults["json"]
    out_csv = _resolve_path(args.out_csv) if args.out_csv else defaults["csv"]
    payload = build_payload(
        run_label=str(args.run_label),
        start_date=_parse_date(args.start_date),
        end_date=_parse_date(args.end_date),
        history_start=_parse_date(args.history_start_date),
        history_end=_parse_date(args.history_end_date),
        baseline_window_root=_resolve_path(args.baseline_window_root),
        baseline_cycle_root=_resolve_path(args.baseline_cycle_root),
        runs2_root=_resolve_path(args.runs2_root),
        history_root=_resolve_path(args.history_root),
        results_root=_resolve_path(args.results_root),
        bonus_results_root=_resolve_path(args.bonus_results_root),
        candidate_sharepacks_root=_resolve_path(args.candidate_sharepacks_root),
        truth_sharepacks_root=_resolve_path(args.truth_sharepacks_root),
        profile=str(args.profile),
        experiment_tag=str(args.experiment_tag),
        board_name=str(args.board_name),
        top_n_stable=int(args.top_n_stable),
        decay_upload_days_total=int(args.decay_upload_days_total),
        windowed_draws=int(args.windowed_draws),
    )

    _write_csv(out_csv, payload["commands"], force=bool(args.force))
    payload["command_csv_path"] = safe_rel(out_csv)
    _write_json(out_json, payload, force=bool(args.force))
    _write_text(out_md, _render_markdown(payload, csv_path=out_csv), force=bool(args.force))
    print(f"Wrote: {safe_rel(out_md)}")
    print(f"Wrote: {safe_rel(out_json)}")
    print(f"Wrote: {safe_rel(out_csv)}")


if __name__ == "__main__":
    main()
