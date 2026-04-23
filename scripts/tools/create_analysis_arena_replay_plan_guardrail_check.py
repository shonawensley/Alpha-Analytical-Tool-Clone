#!/usr/bin/env python3
"""Validate Analysis Arena replay-plan guardrails.

This check exists to prevent a same-window replay from being compared as a
one-window Stage 6B/7B cycle against a multi-window baseline cycle. That shape
can create false promotion-guardrail blocks and false degraded/contradicted
comparison rows.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Sequence


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.tools.analysis_arena_window_utils import safe_rel


DEFAULT_FINAL_DOCS = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "final docs"
DEFAULT_CANONICAL_MIX = (
    REPO_ROOT
    / "docs"
    / "AAT9_KIT"
    / "FINAL VALIDATION"
    / "RUNS_2"
    / "REPLAY"
    / "march_2026_15day_replay_v2_canonical_mix"
)
DEFAULT_STAGE7B = DEFAULT_CANONICAL_MIX / "ANALYSIS_ARENA__CYCLE__STAGE7B_FIXTURE_REPLAY_HARNESS.json"
DEFAULT_STEM = "AAT9_ANALYSIS_ARENA__REPLAY_PLAN_GUARDRAIL_CHECK"

EXPECTED_REPLACEMENT_WINDOWS = [
    "WINDOW_2025-12-30_to_2026-01-04",
    "WINDOW_2026-01-05_to_2026-01-09",
    "WINDOW_2026-01-15_to_2026-01-22",
    "WINDOW_2026-03-09_to_2026-03-23",
]
FORBIDDEN_REPLACEMENT_WINDOWS = {
    "WINDOW_2026-01-05_to_2026-01-09__PREALIGN_SNAPSHOT",
    "WINDOW_2026-01-15_to_2026-01-18",
}
EXPECTED_EXISTING_NAMESPACE_BLOCKERS = {
    "candidate window root already exists; archive or choose a new run label before execution",
    "candidate sharepacks root already exists; archive or choose a new run label before execution",
    "candidate replacement-cycle root already exists; archive or choose a new run label before execution",
}


def _parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--execution-prep-json",
        default=str(DEFAULT_FINAL_DOCS / "AAT9_ANALYSIS_ARENA__MARCH_RUN2_EXECUTION_PREP.json"),
    )
    ap.add_argument(
        "--execution-prep-csv",
        default=str(DEFAULT_FINAL_DOCS / "AAT9_ANALYSIS_ARENA__MARCH_RUN2_EXECUTION_PREP.csv"),
    )
    ap.add_argument(
        "--comparison-json",
        default=str(DEFAULT_FINAL_DOCS / "AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_COMPARISON_REPORT.json"),
    )
    ap.add_argument(
        "--fresh-readiness-json",
        default=str(DEFAULT_FINAL_DOCS / "AAT9_ANALYSIS_ARENA__FRESH_WINDOW_READINESS.json"),
    )
    ap.add_argument("--stage7b-json", default=str(DEFAULT_STAGE7B))
    ap.add_argument("--out-md", default="")
    ap.add_argument("--out-json", default="")
    ap.add_argument("--out-csv", default="")
    ap.add_argument("--force", action="store_true")
    return ap.parse_args()


def _resolve_path(value: str | Path) -> Path:
    path = Path(value).expanduser()
    if not path.is_absolute():
        path = (REPO_ROOT / path).resolve()
    return path


def _read_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise SystemExit(f"Missing JSON input: {path}")
    return json.loads(path.read_text(encoding="utf-8", errors="replace"))


def _read_csv(path: Path) -> List[Dict[str, str]]:
    if not path.exists():
        raise SystemExit(f"Missing CSV input: {path}")
    with path.open("r", encoding="utf-8", errors="replace", newline="") as fh:
        return [{k: (v or "") for k, v in row.items()} for row in csv.DictReader(fh)]


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
    fields = ["check_id", "status", "severity", "observed", "expected", "detail"]
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def _default_paths() -> Dict[str, Path]:
    return {
        "md": DEFAULT_FINAL_DOCS / f"{DEFAULT_STEM}.md",
        "json": DEFAULT_FINAL_DOCS / f"{DEFAULT_STEM}.json",
        "csv": DEFAULT_FINAL_DOCS / f"{DEFAULT_STEM}.csv",
    }


def _command_rows(rows: Sequence[Dict[str, str]], *, phase: str, needle: str = "") -> List[Dict[str, str]]:
    out = [row for row in rows if row.get("phase") == phase]
    if needle:
        out = [row for row in out if needle in row.get("command", "")]
    return out


def _contains_all_windows(command: str, expected_names: Sequence[str]) -> bool:
    return all(name in command for name in expected_names)


def _add_check(
    checks: List[Dict[str, Any]],
    *,
    check_id: str,
    passed: bool,
    observed: Any,
    expected: Any,
    detail: str,
    severity: str = "error",
) -> None:
    checks.append(
        {
            "check_id": check_id,
            "status": "pass" if passed else "fail",
            "severity": severity,
            "observed": observed,
            "expected": expected,
            "detail": detail,
        }
    )


def _category_counts_ok(category_counts: Dict[str, Any]) -> bool:
    disallowed = {"degraded", "contradicted", "blocked_by_missing_data", "improved_traceability"}
    return all(int(category_counts.get(key) or 0) == 0 for key in disallowed)


def build_payload(
    *,
    execution_prep_json: Path,
    execution_prep_csv: Path,
    comparison_json: Path,
    fresh_readiness_json: Path,
    stage7b_json: Path,
) -> Dict[str, Any]:
    prep = _read_json(execution_prep_json)
    commands = _read_csv(execution_prep_csv)
    comparison = _read_json(comparison_json)
    readiness = _read_json(fresh_readiness_json)
    stage7b = _read_json(stage7b_json)

    checks: List[Dict[str, Any]] = []

    replacement_names = [Path(str(path)).name for path in (prep.get("replacement_cycle") or {}).get("candidate_cycle_windows", [])]
    _add_check(
        checks,
        check_id="G01_replacement_windows_exact",
        passed=replacement_names == EXPECTED_REPLACEMENT_WINDOWS,
        observed=replacement_names,
        expected=EXPECTED_REPLACEMENT_WINDOWS,
        detail="Candidate replacement cycle must use the canonical non-overlap evidence set.",
    )
    forbidden_present = sorted(set(replacement_names) & FORBIDDEN_REPLACEMENT_WINDOWS)
    _add_check(
        checks,
        check_id="G02_no_superseded_or_snapshot_windows",
        passed=not forbidden_present,
        observed=forbidden_present or "none",
        expected="none",
        detail="Snapshots and superseded overlapping windows must not enter replacement-cycle promotion evidence.",
    )

    namespace_status = prep.get("namespace_status") or {}
    _add_check(
        checks,
        check_id="G03_baseline_window_replaced",
        passed=bool(namespace_status.get("baseline_window_replaced_in_candidate_cycle")),
        observed=namespace_status.get("baseline_window_replaced_in_candidate_cycle"),
        expected=True,
        detail="The candidate cycle must replace the replayed baseline window rather than appending duplicate March evidence.",
    )
    blockers = set(str(item) for item in prep.get("blockers") or [])
    unexpected_blockers = sorted(blockers - EXPECTED_EXISTING_NAMESPACE_BLOCKERS)
    _add_check(
        checks,
        check_id="G04_no_unexpected_execution_prep_blockers",
        passed=not unexpected_blockers,
        observed=unexpected_blockers or "none",
        expected="none besides existing replay namespace blockers",
        detail="Completed Run2 artifacts may block rerun-in-place; other blockers indicate prep drift.",
    )
    _add_check(
        checks,
        check_id="G05_stage8_blocked_in_prep",
        passed=prep.get("stage8_permission") == "blocked",
        observed=prep.get("stage8_permission"),
        expected="blocked",
        detail="Same-window replay planning must never grant Stage8/live downstream permission.",
    )

    stage2b_rows = _command_rows(commands, phase="canonical_replacement_cycle")
    stage2b_command = stage2b_rows[0].get("command", "") if stage2b_rows else ""
    _add_check(
        checks,
        check_id="G06_stage2b_canonical_replacement_command",
        passed=len(stage2b_rows) == 1 and _contains_all_windows(stage2b_command, EXPECTED_REPLACEMENT_WINDOWS),
        observed={"rows": len(stage2b_rows), "window_root_count": stage2b_command.count("--window-root")},
        expected={"rows": 1, "window_root_count": 4},
        detail="Stage2B must build the candidate cycle from explicit canonical windows.",
    )
    for check_id, command_name in [
        ("G07_stage3_explicit_window_roots", "stage3-decision-workbench"),
        ("G08_stage4_explicit_window_roots", "stage4-fixture-replay"),
        ("G09_stage5_explicit_window_roots", "stage5-shadow-evaluator"),
    ]:
        rows = _command_rows(commands, phase="stage3_to_7b_canonical_cycle", needle=command_name)
        command = rows[0].get("command", "") if rows else ""
        _add_check(
            checks,
            check_id=check_id,
            passed=len(rows) == 1 and _contains_all_windows(command, EXPECTED_REPLACEMENT_WINDOWS),
            observed={"rows": len(rows), "window_root_count": command.count("--window-root")},
            expected={"rows": 1, "window_root_count": 4},
            detail=f"{command_name} must receive explicit replacement-cycle window roots.",
        )

    comparison_rows = _command_rows(commands, phase="comparison", needle="window-replay-compare")
    comparison_command = comparison_rows[-1].get("command", "") if comparison_rows else ""
    _add_check(
        checks,
        check_id="G10_comparison_uses_canonical_mix",
        passed=(
            len(comparison_rows) == 1
            and "march_2026_15day_replay_v2_canonical_mix" in comparison_command
            and "--require-candidate-complete" in comparison_command
        ),
        observed={"rows": len(comparison_rows), "uses_canonical_mix": "march_2026_15day_replay_v2_canonical_mix" in comparison_command},
        expected={"rows": 1, "uses_canonical_mix": True, "require_candidate_complete": True},
        detail="Final comparison must point at the canonical mix candidate cycle and require candidate completeness.",
    )

    comp_summary = comparison.get("summary") or {}
    comp_meta = comparison.get("metadata") or {}
    _add_check(
        checks,
        check_id="G11_comparison_complete_clean",
        passed=(
            comp_summary.get("candidate_completeness_status") == "candidate_complete"
            and int(comp_summary.get("missing_required_candidate_target_count") or 0) == 0
            and _category_counts_ok(comp_summary.get("category_counts") or {})
        ),
        observed=comp_summary,
        expected="candidate_complete, 0 missing targets, no degraded/contradicted/improved rows",
        detail="March Run2 should remain deterministic replay confirmation, not a changed-evidence signal.",
    )
    _add_check(
        checks,
        check_id="G12_comparison_no_fresh_unlock",
        passed=(
            comp_meta.get("evidence_tier") == "same_window_replay"
            and comp_summary.get("stage8_permission") == "blocked"
            and comp_summary.get("comparison_status") == "replay_or_replication_comparison_complete_no_fresh_unlock"
        ),
        observed={"evidence_tier": comp_meta.get("evidence_tier"), "stage8_permission": comp_summary.get("stage8_permission"), "comparison_status": comp_summary.get("comparison_status")},
        expected={"evidence_tier": "same_window_replay", "stage8_permission": "blocked", "comparison_status": "replay_or_replication_comparison_complete_no_fresh_unlock"},
        detail="Same-window replay can support regression confidence only, not fresh confirmation or Stage8 unlock.",
    )

    readiness_meta = readiness.get("metadata") or {}
    _add_check(
        checks,
        check_id="G13_fresh_window_readiness_boundary",
        passed=bool(readiness_meta.get("ready_for_fresh_windows")) and int(readiness_meta.get("window_count") or 0) >= 4,
        observed=readiness_meta,
        expected={"ready_for_fresh_windows": True, "window_count_min": 4},
        detail="System may proceed to fresh-window evidence collection while keeping Stage8 blocked.",
    )
    _add_check(
        checks,
        check_id="G14_stage7b_read_only_ready",
        passed=(
            stage7b.get("fresh_window_replay_status") == "ready_for_read_only_confirmation_replay"
            and stage7b.get("scoring_rewrite_status") == "blocked_until_future_confirmation"
            and stage7b.get("guardrail") == "read_only_fixture_replay_readiness_no_live_permission"
        ),
        observed={
            "fresh_window_replay_status": stage7b.get("fresh_window_replay_status"),
            "scoring_rewrite_status": stage7b.get("scoring_rewrite_status"),
            "guardrail": stage7b.get("guardrail"),
        },
        expected={
            "fresh_window_replay_status": "ready_for_read_only_confirmation_replay",
            "scoring_rewrite_status": "blocked_until_future_confirmation",
            "guardrail": "read_only_fixture_replay_readiness_no_live_permission",
        },
        detail="Stage7B can guide confirmation replay but cannot authorize scoring rewrite.",
    )

    failed = [row for row in checks if row["status"] != "pass" and row.get("severity") == "error"]
    return {
        "schema_version": "analysis_arena_replay_plan_guardrail_check/v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "status": "pass" if not failed else "fail",
        "stage8_permission": "blocked",
        "inputs": {
            "execution_prep_json": safe_rel(execution_prep_json),
            "execution_prep_csv": safe_rel(execution_prep_csv),
            "comparison_json": safe_rel(comparison_json),
            "fresh_readiness_json": safe_rel(fresh_readiness_json),
            "stage7b_json": safe_rel(stage7b_json),
        },
        "summary": {
            "check_count": len(checks),
            "passed": sum(1 for row in checks if row["status"] == "pass"),
            "failed": len(failed),
            "expected_replacement_windows": EXPECTED_REPLACEMENT_WINDOWS,
            "observed_replacement_windows": replacement_names,
            "evidence_boundary": "same-window replay is regression evidence only; fresh-window confirmation is still required before Stage8",
        },
        "checks": checks,
    }


def _render_markdown(payload: Dict[str, Any], *, csv_path: Path) -> str:
    summary = payload["summary"]
    lines = [
        "# AAT9 Analysis Arena - Replay Plan Guardrail Check",
        "",
        "## Verdict",
        "",
        f"- status: `{payload['status']}`",
        f"- stage8_permission: `{payload['stage8_permission']}`",
        f"- checks: `{summary['passed']}/{summary['check_count']}` passed",
        f"- failed: `{summary['failed']}`",
        f"- csv: `{safe_rel(csv_path)}`",
        "",
        "## Evidence Boundary",
        "",
        "- Same-window replay remains regression/reproducibility evidence only.",
        "- Canonical replacement-cycle comparison is mandatory for same-window replay.",
        "- Fresh-window confirmation is still required before Stage8 or downstream scoring/candidate/budget rewrite work.",
        "",
        "## Replacement Cycle",
        "",
    ]
    for name in summary["observed_replacement_windows"]:
        lines.append(f"- `{name}`")
    lines += [
        "",
        "## Checks",
        "",
        "| Check | Status | Detail |",
        "|---|---:|---|",
    ]
    for row in payload["checks"]:
        lines.append(f"| `{row['check_id']}` | `{row['status']}` | {row['detail']} |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    args = _parse_args()
    defaults = _default_paths()
    out_md = _resolve_path(args.out_md) if args.out_md else defaults["md"]
    out_json = _resolve_path(args.out_json) if args.out_json else defaults["json"]
    out_csv = _resolve_path(args.out_csv) if args.out_csv else defaults["csv"]

    payload = build_payload(
        execution_prep_json=_resolve_path(args.execution_prep_json),
        execution_prep_csv=_resolve_path(args.execution_prep_csv),
        comparison_json=_resolve_path(args.comparison_json),
        fresh_readiness_json=_resolve_path(args.fresh_readiness_json),
        stage7b_json=_resolve_path(args.stage7b_json),
    )
    _write_csv(out_csv, payload["checks"], force=bool(args.force))
    payload["check_csv_path"] = safe_rel(out_csv)
    _write_json(out_json, payload, force=bool(args.force))
    _write_text(out_md, _render_markdown(payload, csv_path=out_csv), force=bool(args.force))
    print(f"[OK] Wrote replay-plan guardrail markdown: {safe_rel(out_md)}")
    print(f"[OK] Wrote replay-plan guardrail JSON: {safe_rel(out_json)}")
    print(f"[OK] Wrote replay-plan guardrail CSV: {safe_rel(out_csv)}")
    if payload["status"] != "pass":
        raise SystemExit("Replay-plan guardrail check failed.")


if __name__ == "__main__":
    main()
