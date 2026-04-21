#!/usr/bin/env python3
"""Create a read-only Analysis Arena window replay comparison report.

The report compares a preserved baseline package against an optional rerun or
replication package. If the candidate package is not provided yet, it produces a
baseline-preservation/readiness report so replay work can be planned without
overwriting the current evidence.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Dict, List, Mapping, Sequence


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.tools.analysis_arena_window_utils import safe_rel


DEFAULT_RUNS2_ROOT = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS_2"
DEFAULT_FINAL_DOCS = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "final docs"
DEFAULT_BASELINE_WINDOW_ROOT = DEFAULT_RUNS2_ROOT / "WINDOW_2026-03-09_to_2026-03-23"
DEFAULT_STEM = "AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_COMPARISON_REPORT"

EVIDENCE_TIERS = {"same_window_replay", "archived_window_replication", "true_fresh_confirmation"}

WINDOW_TARGETS: List[Dict[str, Any]] = [
    {"target_id": "window_performance_gap", "suffix": "PERFORMANCE_GAP.json", "layer": "window_close", "required": True},
    {"target_id": "window_deep_hit_analysis", "suffix": "DEEP_HIT_ANALYSIS.json", "layer": "window_close", "required": True},
    {"target_id": "window_frontier_harness", "suffix": "C1_C2_FRONTIER_ANALYSIS.json", "layer": "window_close", "required": True},
    {"target_id": "window_pure_finalist_scorecard", "suffix": "PURE_FINALIST_SCORECARD.json", "layer": "window_close", "required": True},
    {"target_id": "window_translator_ledger", "suffix": "TRANSLATOR_LEARNING_LEDGER.json", "layer": "window_close", "required": True},
    {"target_id": "window_deep_analysis", "suffix": "DEEP_ANALYSIS__CODEX.json", "layer": "window_close", "required": True},
    {"target_id": "window_decay_carryover", "suffix": "DECAY_CARRYOVER_SCORECARD.json", "layer": "window_close", "required": False},
    {"target_id": "window_stage2b_stack_scorecard", "suffix": "STAGE2B_SIGNAL_STACK_SCORECARD.json", "layer": "post_run_audit", "required": False},
    {"target_id": "window_stage3_casebook", "suffix": "STAGE3_CASEBOOK.csv", "layer": "post_run_audit", "required": False},
]

CYCLE_TARGETS: List[Dict[str, Any]] = [
    {
        "target_id": "stage6b_scenario_scorecard",
        "filename": "ANALYSIS_ARENA__CYCLE__STAGE6B_REPLAY_SCENARIO_SCORECARD.csv",
        "layer": "stage6b",
        "key_fields": ["scenario_id"],
        "material_fields": [
            "scenario_role",
            "allowed_permission",
            "live_scoring_permission",
            "candidate_generation_permission",
            "matched_value_rate",
            "false_positive_proxy_rate",
            "pool_normalized_positive_yield",
            "sample_completeness_rate",
        ],
    },
    {
        "target_id": "stage6b_lane_increment",
        "filename": "ANALYSIS_ARENA__CYCLE__STAGE6B_LANE_INCREMENT_MATRIX.csv",
        "layer": "stage6b",
        "key_fields": ["comparison_id"],
        "material_fields": ["positive_conversion_delta", "false_positive_proxy_delta", "pool_normalized_yield_delta", "readback_interpretation"],
    },
    {
        "target_id": "stage6b_guardrail_compliance",
        "filename": "ANALYSIS_ARENA__CYCLE__STAGE6B_GUARDRAIL_COMPLIANCE.csv",
        "layer": "stage6b",
        "key_fields": ["guardrail_id"],
        "material_fields": ["status", "evidence", "failure_response"],
    },
    {
        "target_id": "stage6b_readback_scenario_decisions",
        "filename": "ANALYSIS_ARENA__CYCLE__STAGE6B_READBACK_SCENARIO_DECISIONS.csv",
        "layer": "stage6b_readback",
        "key_fields": ["scenario_id"],
        "material_fields": ["readback_decision", "status", "allowed_permission", "macro_findings_posture", "live_permission"],
    },
    {
        "target_id": "stage6b_readback_requirement_results",
        "filename": "ANALYSIS_ARENA__CYCLE__STAGE6B_READBACK_REQUIREMENT_RESULTS.csv",
        "layer": "stage6b_readback",
        "key_fields": ["requirement_id", "test_target"],
        "material_fields": ["readback_result", "evidence", "next_action", "live_permission"],
    },
    {
        "target_id": "stage6c_confirmation_tests",
        "filename": "ANALYSIS_ARENA__CYCLE__STAGE6C_CONFIRMATION_TEST_MATRIX.csv",
        "layer": "stage6c",
        "key_fields": ["test_id", "confirmation_target"],
        "material_fields": ["current_march_evidence", "fresh_window_test", "pass_threshold", "live_permission"],
    },
    {
        "target_id": "stage6c_rewrite_blockers",
        "filename": "ANALYSIS_ARENA__CYCLE__STAGE6C_REWRITE_BLOCKERS.csv",
        "layer": "stage6c",
        "key_fields": ["blocker_id"],
        "material_fields": ["status", "rationale", "clearance_condition", "current_evidence", "live_permission"],
    },
    {
        "target_id": "stage6d_restraint_bucket_scorecard",
        "filename": "ANALYSIS_ARENA__CYCLE__STAGE6D_RESTRAINT_BUCKET_SCORECARD.csv",
        "layer": "stage6d",
        "key_fields": ["bucket_id"],
        "material_fields": ["bucket_type", "restraint_pressure", "matched_value_rate", "false_positive_proxy_rate", "bucket_status"],
    },
    {
        "target_id": "stage6e_support_bucket_scorecard",
        "filename": "ANALYSIS_ARENA__CYCLE__STAGE6E_SUPPORT_BUCKET_SCORECARD.csv",
        "layer": "stage6e",
        "key_fields": ["bucket_id", "peer_key"],
        "material_fields": ["bucket_type", "support_context", "matched_value_rate", "false_positive_proxy_rate", "bucket_status"],
    },
    {
        "target_id": "stage6f_lane_decision_atlas",
        "filename": "ANALYSIS_ARENA__CYCLE__STAGE6F_LANE_DECISION_ATLAS.csv",
        "layer": "stage6f",
        "key_fields": ["lane_id"],
        "material_fields": ["current_decision", "current_status", "decision_posture", "primary_blockers", "allowed_permission", "live_permission"],
    },
    {
        "target_id": "stage6f_active_blockers",
        "filename": "ANALYSIS_ARENA__CYCLE__STAGE6F_ACTIVE_BLOCKERS_AND_CLEARANCE.csv",
        "layer": "stage6f",
        "key_fields": ["blocker_id"],
        "material_fields": ["status", "blocks", "rationale", "clearance_condition", "live_permission"],
    },
    {
        "target_id": "stage6f_carry_forward_queue",
        "filename": "ANALYSIS_ARENA__CYCLE__STAGE6F_FRESH_WINDOW_CARRY_FORWARD_QUEUE.csv",
        "layer": "stage6f",
        "key_fields": ["subject", "priority"],
        "material_fields": ["carry_forward_action", "acceptance_or_review_test", "allowed_permission", "live_permission"],
    },
    {
        "target_id": "stage7a_confirmation_requirements",
        "filename": "ANALYSIS_ARENA__CYCLE__STAGE7A_CONFIRMATION_REQUIREMENTS.csv",
        "layer": "stage7a",
        "key_fields": ["requirement_id", "confirmation_target"],
        "material_fields": ["current_threshold_result", "fresh_window_test", "pass_threshold", "live_permission"],
    },
    {
        "target_id": "stage7a_march_seed_benchmarks",
        "filename": "ANALYSIS_ARENA__CYCLE__STAGE7A_MARCH_SEED_BENCHMARKS.csv",
        "layer": "stage7a",
        "key_fields": ["benchmark_id", "source_id"],
        "material_fields": ["subject", "march_metric_summary", "recommended_future_comparison"],
    },
    {
        "target_id": "stage7b_queue_replay_status",
        "filename": "ANALYSIS_ARENA__CYCLE__STAGE7B_QUEUE_REPLAY_STATUS.csv",
        "layer": "stage7b",
        "key_fields": ["subject", "related_requirement_id"],
        "material_fields": ["replay_readiness_status", "readiness_reason", "active_blockers", "allowed_permission", "live_permission"],
    },
    {
        "target_id": "stage7b_requirement_coverage",
        "filename": "ANALYSIS_ARENA__CYCLE__STAGE7B_REQUIREMENT_COVERAGE.csv",
        "layer": "stage7b",
        "key_fields": ["requirement_id", "confirmation_target"],
        "material_fields": ["coverage_status", "fresh_window_readiness_status", "missing_items", "live_permission"],
    },
    {
        "target_id": "stage7b_blocker_recheck",
        "filename": "ANALYSIS_ARENA__CYCLE__STAGE7B_BLOCKER_RECHECK.csv",
        "layer": "stage7b",
        "key_fields": ["blocker_id"],
        "material_fields": ["blocker_status", "current_evidence", "stage7b_recheck_result", "live_permission"],
    },
]


def _parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--baseline-window-root", default=str(DEFAULT_BASELINE_WINDOW_ROOT), help="Preserved baseline window root.")
    ap.add_argument("--candidate-window-root", default="", help="Optional rerun/replication window root.")
    ap.add_argument("--baseline-cycle-root", default=str(DEFAULT_RUNS2_ROOT), help="Baseline RUNS_2 cycle-level artifact root.")
    ap.add_argument("--candidate-cycle-root", default="", help="Optional rerun/replication cycle-level artifact root.")
    ap.add_argument("--evidence-tier", default="same_window_replay", choices=sorted(EVIDENCE_TIERS))
    ap.add_argument("--run-label", default="march_2026_15day_replay_v2_pending")
    ap.add_argument("--out-md", default="", help="Optional Markdown output path.")
    ap.add_argument("--out-json", default="", help="Optional JSON output path.")
    ap.add_argument("--out-csv", default="", help="Optional CSV output path.")
    ap.add_argument("--force", action="store_true", help="Overwrite existing outputs.")
    return ap.parse_args()


def _resolve_path(value: str | Path) -> Path:
    path = Path(value).expanduser()
    if not path.is_absolute():
        path = (REPO_ROOT / path).resolve()
    return path


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
    fieldnames = [
        "target_id",
        "layer",
        "artifact_kind",
        "category",
        "status",
        "baseline_path",
        "candidate_path",
        "baseline_exists",
        "candidate_exists",
        "baseline_sha256",
        "candidate_sha256",
        "baseline_row_count",
        "candidate_row_count",
        "added_key_count",
        "removed_key_count",
        "changed_key_count",
        "material_change_fields",
        "interpretation",
    ]
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row.get(key, "") for key in fieldnames})


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _read_csv_rows(path: Path) -> List[Dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", errors="replace", newline="") as fh:
        return [{k: (v or "") for k, v in row.items()} for row in csv.DictReader(fh)]


def _read_json(path: Path) -> Any:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8", errors="replace"))
    except Exception:
        return {}


def _artifact_kind(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".csv":
        return "csv"
    if suffix == ".json":
        return "json"
    if suffix == ".md":
        return "markdown"
    return suffix.lstrip(".") or "unknown"


def _find_window_artifact(window_root: Path, suffix: str) -> Path:
    if not window_root:
        return Path("")
    matches = sorted(window_root.glob(f"*__ANALYSIS_ARENA__{suffix}"))
    return matches[0] if matches else window_root / f"{window_root.name}__ANALYSIS_ARENA__{suffix}"


def _candidate_missing(candidate_root: Path | None) -> bool:
    return candidate_root is None or str(candidate_root) == "" or not candidate_root.exists()


def _display_path(path: Path, *, enabled: bool = True) -> str:
    if not enabled:
        return ""
    text = str(path)
    if text in {"", "."}:
        return ""
    return safe_rel(path)


def _row_key(row: Mapping[str, Any], preferred_fields: Sequence[str]) -> str:
    parts: List[str] = []
    for field in preferred_fields:
        value = str(row.get(field) or "").strip()
        if value:
            parts.append(value)
    if parts:
        return "::".join(parts)
    for field in ("id", "target_id", "subject", "bucket_id", "requirement_id", "scenario_id", "blocker_id", "lane_id"):
        value = str(row.get(field) or "").strip()
        if value:
            return value
    return json.dumps({key: row.get(key, "") for key in sorted(row)}, sort_keys=True)


def _row_signature(row: Mapping[str, Any], fields: Sequence[str]) -> str:
    selected = {field: str(row.get(field) or "") for field in fields if field in row}
    if not selected:
        selected = {key: str(row.get(key) or "") for key in sorted(row)}
    return json.dumps(selected, sort_keys=True)


def _csv_compare(
    baseline_path: Path,
    candidate_path: Path,
    *,
    candidate_provided: bool,
    key_fields: Sequence[str],
    material_fields: Sequence[str],
) -> Dict[str, Any]:
    if not candidate_provided:
        return {
            "category": "blocked_by_missing_data",
            "status": "candidate_not_provided",
            "baseline_row_count": len(_read_csv_rows(baseline_path)),
            "candidate_row_count": 0,
            "added_keys": [],
            "removed_keys": [],
            "changed_keys": [],
            "material_change_fields": [],
        }

    baseline_rows = _read_csv_rows(baseline_path)
    candidate_rows = _read_csv_rows(candidate_path)
    baseline_by_key = {_row_key(row, key_fields): row for row in baseline_rows}
    candidate_by_key = {_row_key(row, key_fields): row for row in candidate_rows}
    baseline_keys = set(baseline_by_key)
    candidate_keys = set(candidate_by_key)
    added = sorted(candidate_keys - baseline_keys)
    removed = sorted(baseline_keys - candidate_keys)
    changed: List[str] = []
    changed_fields: set[str] = set()

    for key in sorted(baseline_keys & candidate_keys):
        baseline_sig = _row_signature(baseline_by_key[key], material_fields)
        candidate_sig = _row_signature(candidate_by_key[key], material_fields)
        if baseline_sig != candidate_sig:
            changed.append(key)
            for field in material_fields:
                if str(baseline_by_key[key].get(field) or "") != str(candidate_by_key[key].get(field) or ""):
                    changed_fields.add(field)

    if not added and not removed and not changed:
        category = "unchanged"
        status = "row_signatures_match"
    elif removed:
        category = "degraded"
        status = "candidate_lost_baseline_rows"
    elif changed and any(field in changed_fields for field in ("status", "readback_result", "current_decision", "current_status", "replay_readiness_status", "blocker_status", "live_permission")):
        category = "contradicted"
        status = "material_status_or_decision_changed"
    elif changed:
        category = "improved_traceability"
        status = "material_metric_or_evidence_changed"
    elif added:
        category = "newly_exposed"
        status = "candidate_added_rows"
    else:
        category = "renamed_or_reclassified_only"
        status = "non_material_difference"

    return {
        "category": category,
        "status": status,
        "baseline_row_count": len(baseline_rows),
        "candidate_row_count": len(candidate_rows),
        "added_keys": added,
        "removed_keys": removed,
        "changed_keys": changed,
        "material_change_fields": sorted(changed_fields),
    }


def _json_status_summary(path: Path) -> Dict[str, Any]:
    payload = _read_json(path)
    if not isinstance(payload, dict):
        return {}
    keys = [
        "stage",
        "fresh_window_replay_status",
        "scoring_rewrite_status",
        "guardrail",
        "queue_row_count",
        "requirement_row_count",
        "blocker_row_count",
        "casebook_row_count",
    ]
    return {key: payload.get(key) for key in keys if key in payload}


def _json_compare(baseline_path: Path, candidate_path: Path, *, candidate_provided: bool) -> Dict[str, Any]:
    if not candidate_provided:
        return {"category": "blocked_by_missing_data", "status": "candidate_not_provided", "material_change_fields": []}
    baseline_summary = _json_status_summary(baseline_path)
    candidate_summary = _json_status_summary(candidate_path)
    if baseline_summary == candidate_summary:
        return {"category": "unchanged", "status": "summary_fields_match", "material_change_fields": []}
    changed_fields = sorted({key for key in set(baseline_summary) | set(candidate_summary) if baseline_summary.get(key) != candidate_summary.get(key)})
    if any(key.endswith("status") or key == "guardrail" for key in changed_fields):
        category = "contradicted"
        status = "json_status_fields_changed"
    else:
        category = "improved_traceability"
        status = "json_summary_counts_changed"
    return {"category": category, "status": status, "material_change_fields": changed_fields}


def _compare_target(
    *,
    target_id: str,
    layer: str,
    baseline_path: Path,
    candidate_path: Path,
    candidate_provided: bool,
    key_fields: Sequence[str] = (),
    material_fields: Sequence[str] = (),
    required: bool = True,
) -> Dict[str, Any]:
    baseline_exists = baseline_path.exists()
    candidate_exists = candidate_provided and candidate_path.exists()
    kind = _artifact_kind(baseline_path if baseline_exists else candidate_path)

    baseline_sha = _sha256(baseline_path) if baseline_exists else ""
    candidate_sha = _sha256(candidate_path) if candidate_exists else ""

    if not baseline_exists and not candidate_exists:
        category = "blocked_by_missing_data" if required else "unchanged"
        status = "both_missing" if required else "optional_both_missing"
        detail: Dict[str, Any] = {"material_change_fields": []}
    elif baseline_exists and not candidate_exists:
        category = "blocked_by_missing_data"
        status = "candidate_not_provided" if not candidate_provided else "candidate_missing_artifact"
        detail = {"material_change_fields": []}
    elif not baseline_exists and candidate_exists:
        category = "newly_exposed"
        status = "candidate_has_artifact_baseline_missing"
        detail = {"material_change_fields": []}
    elif baseline_sha == candidate_sha:
        category = "unchanged"
        status = "hash_match"
        detail = {
            "baseline_row_count": len(_read_csv_rows(baseline_path)) if kind == "csv" else "",
            "candidate_row_count": len(_read_csv_rows(candidate_path)) if kind == "csv" else "",
            "material_change_fields": [],
        }
    elif kind == "csv":
        detail = _csv_compare(
            baseline_path,
            candidate_path,
            candidate_provided=candidate_provided,
            key_fields=key_fields,
            material_fields=material_fields,
        )
        category = detail["category"]
        status = detail["status"]
    elif kind == "json":
        detail = _json_compare(baseline_path, candidate_path, candidate_provided=candidate_provided)
        category = detail["category"]
        status = detail["status"]
    else:
        category = "improved_traceability"
        status = "hash_changed_non_structured_artifact"
        detail = {"material_change_fields": []}

    return {
        "target_id": target_id,
        "layer": layer,
        "artifact_kind": kind,
        "category": category,
        "status": status,
        "required": bool(required),
        "baseline_path": _display_path(baseline_path, enabled=bool(baseline_exists or str(baseline_path) not in {"", "."})),
        "candidate_path": _display_path(candidate_path, enabled=bool(candidate_provided)),
        "baseline_exists": bool(baseline_exists),
        "candidate_exists": bool(candidate_exists),
        "baseline_sha256": baseline_sha,
        "candidate_sha256": candidate_sha,
        "baseline_row_count": detail.get("baseline_row_count", ""),
        "candidate_row_count": detail.get("candidate_row_count", ""),
        "added_keys": detail.get("added_keys", []),
        "removed_keys": detail.get("removed_keys", []),
        "changed_keys": detail.get("changed_keys", []),
        "added_key_count": len(detail.get("added_keys", []) or []),
        "removed_key_count": len(detail.get("removed_keys", []) or []),
        "changed_key_count": len(detail.get("changed_keys", []) or []),
        "material_change_fields": "|".join(detail.get("material_change_fields", []) or []),
        "interpretation": _interpretation_for(category),
    }


def _interpretation_for(category: str) -> str:
    if category == "unchanged":
        return "baseline and candidate target match for the selected comparison surface"
    if category == "improved_traceability":
        return "candidate changed measurable detail; review as traceability/metric behavior, not fresh confirmation"
    if category == "newly_exposed":
        return "candidate exposed target rows/artifacts absent from baseline"
    if category == "degraded":
        return "candidate lost baseline rows/artifacts; review before trusting rerun"
    if category == "contradicted":
        return "candidate changed status/decision posture; requires manual review"
    if category == "renamed_or_reclassified_only":
        return "candidate differs without selected material field movement"
    return "candidate or baseline data is missing; no comparison conclusion"


def _summary_status(evidence_tier: str, candidate_provided: bool, counts: Counter[str]) -> str:
    if not candidate_provided:
        return "baseline_preserved_candidate_pending"
    if counts.get("contradicted", 0) or counts.get("degraded", 0):
        return "review_required_before_interpretation"
    if counts.get("blocked_by_missing_data", 0):
        return "comparison_partial_missing_data"
    if evidence_tier == "true_fresh_confirmation":
        return "fresh_comparison_ready_for_manual_gate_review"
    return "replay_or_replication_comparison_complete_no_fresh_unlock"


def build_payload(
    *,
    baseline_window_root: Path,
    candidate_window_root: Path | None,
    baseline_cycle_root: Path,
    candidate_cycle_root: Path | None,
    evidence_tier: str,
    run_label: str,
) -> Dict[str, Any]:
    candidate_window_provided = candidate_window_root is not None and candidate_window_root.exists()
    candidate_cycle_provided = candidate_cycle_root is not None and candidate_cycle_root.exists()

    window_rows: List[Dict[str, Any]] = []
    for target in WINDOW_TARGETS:
        baseline_path = _find_window_artifact(baseline_window_root, str(target["suffix"]))
        candidate_path = _find_window_artifact(candidate_window_root, str(target["suffix"])) if candidate_window_root else Path("")
        window_rows.append(
            _compare_target(
                target_id=str(target["target_id"]),
                layer=str(target["layer"]),
                baseline_path=baseline_path,
                candidate_path=candidate_path,
                candidate_provided=candidate_window_provided,
                required=bool(target.get("required", True)),
            )
        )

    cycle_rows: List[Dict[str, Any]] = []
    for target in CYCLE_TARGETS:
        baseline_path = baseline_cycle_root / str(target["filename"])
        candidate_path = candidate_cycle_root / str(target["filename"]) if candidate_cycle_root else Path("")
        cycle_rows.append(
            _compare_target(
                target_id=str(target["target_id"]),
                layer=str(target["layer"]),
                baseline_path=baseline_path,
                candidate_path=candidate_path,
                candidate_provided=candidate_cycle_provided,
                key_fields=list(target.get("key_fields") or []),
                material_fields=list(target.get("material_fields") or []),
                required=True,
            )
        )

    all_rows = window_rows + cycle_rows
    counts = Counter(str(row.get("category") or "") for row in all_rows)
    candidate_provided = candidate_window_provided or candidate_cycle_provided

    return {
        "metadata": {
            "run_label": run_label,
            "evidence_tier": evidence_tier,
            "baseline_window_root": safe_rel(baseline_window_root),
            "candidate_window_root": safe_rel(candidate_window_root) if candidate_window_root else "",
            "baseline_cycle_root": safe_rel(baseline_cycle_root),
            "candidate_cycle_root": safe_rel(candidate_cycle_root) if candidate_cycle_root else "",
            "candidate_window_provided": candidate_window_provided,
            "candidate_cycle_provided": candidate_cycle_provided,
            "guardrail": "read_only_comparison_no_window_execution_no_live_permission",
        },
        "summary": {
            "comparison_status": _summary_status(evidence_tier, candidate_provided, counts),
            "total_targets": len(all_rows),
            "window_targets": len(window_rows),
            "cycle_targets": len(cycle_rows),
            "category_counts": dict(counts),
            "stage8_permission": "blocked",
            "allowed_conclusions": _allowed_conclusions(evidence_tier, candidate_provided),
            "blocked_conclusions": _blocked_conclusions(evidence_tier),
        },
        "window_comparisons": window_rows,
        "cycle_comparisons": cycle_rows,
        "diff_ledger": all_rows,
    }


def _allowed_conclusions(evidence_tier: str, candidate_provided: bool) -> str:
    if not candidate_provided:
        return "baseline preservation, target inventory, and rerun planning only"
    if evidence_tier == "same_window_replay":
        return "regression behavior, before-after differences, deterministic replay checks, traceability changes"
    if evidence_tier == "archived_window_replication":
        return "historical replication behavior, stress-test differences, blocker recheck candidates"
    return "fresh-window gate review only after manual March-vs-fresh interpretation"


def _blocked_conclusions(evidence_tier: str) -> str:
    if evidence_tier in {"same_window_replay", "archived_window_replication"}:
        return "no fresh confirmation, no Stage 8A unlock, no live scoring/candidate/budget replacement"
    return "no live scoring/candidate/budget replacement without explicit Stage 8 shadow design and approval"


def _render_markdown(payload: Dict[str, Any]) -> str:
    meta = payload.get("metadata") or {}
    summary = payload.get("summary") or {}
    counts = summary.get("category_counts") or {}
    rows = payload.get("diff_ledger") or []

    lines: List[str] = [
        "# Analysis Arena Window Replay Comparison Report",
        "",
        "## 1. Verdict",
        "",
        f"- run_label: `{meta.get('run_label', '')}`",
        f"- evidence_tier: `{meta.get('evidence_tier', '')}`",
        f"- comparison_status: `{summary.get('comparison_status', '')}`",
        f"- total_targets: `{summary.get('total_targets', 0)}`",
        f"- stage8_permission: `{summary.get('stage8_permission', 'blocked')}`",
        "",
        "Category counts:",
        "",
    ]
    for category in ("unchanged", "improved_traceability", "newly_exposed", "degraded", "contradicted", "renamed_or_reclassified_only", "blocked_by_missing_data"):
        lines.append(f"- `{category}`: `{counts.get(category, 0)}`")

    lines += [
        "",
        "## 2. Compared Roots",
        "",
        f"- baseline_window_root: `{meta.get('baseline_window_root', '')}`",
        f"- candidate_window_root: `{meta.get('candidate_window_root', '') or 'not_provided'}`",
        f"- baseline_cycle_root: `{meta.get('baseline_cycle_root', '')}`",
        f"- candidate_cycle_root: `{meta.get('candidate_cycle_root', '') or 'not_provided'}`",
        "",
        "Durable references:",
        "",
        "- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__WINDOW_REPLAY_COMPARISON_DESIGN.md`",
        "- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_ANALYSIS_ARENA__MARCH_REPLAY_RUNBOOK.md`",
        "",
        "## 3. Target Matrix",
        "",
        "| Target | Layer | Category | Status | Baseline | Candidate |",
        "|---|---|---|---|---|---|",
    ]
    for row in rows:
        lines.append(
            "| "
            f"`{row.get('target_id', '')}` | "
            f"`{row.get('layer', '')}` | "
            f"`{row.get('category', '')}` | "
            f"`{row.get('status', '')}` | "
            f"`{str(row.get('baseline_exists')).lower()}` | "
            f"`{str(row.get('candidate_exists')).lower()}` |"
        )

    lines += [
        "",
        "## 4. Allowed Conclusions",
        "",
        f"- {summary.get('allowed_conclusions', '')}",
        "",
        "## 5. Blocked Conclusions",
        "",
        f"- {summary.get('blocked_conclusions', '')}",
        "- This report does not run a window and does not grant Stage 8 permission.",
        "- Same-window replay and archived-window replication cannot replace true fresh-window confirmation.",
        "",
        "## 6. Next Use",
        "",
    ]
    if not meta.get("candidate_window_provided") and not meta.get("candidate_cycle_provided"):
        lines += [
            "- Preserve the baseline root before any rerun.",
            "- Choose a separate rerun output namespace or run label.",
            "- Re-run this comparison with candidate roots after the rerun exists.",
        ]
    else:
        lines += [
            "- Review any `contradicted` or `degraded` rows manually first.",
            "- Treat `improved_traceability` as development evidence, not fresh confirmation.",
            "- Use only true fresh confirmation for Stage 8A consideration.",
        ]
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    args = _parse_args()
    evidence_tier = str(args.evidence_tier or "").strip()
    if evidence_tier not in EVIDENCE_TIERS:
        raise SystemExit(f"Invalid --evidence-tier: {evidence_tier}")

    baseline_window_root = _resolve_path(args.baseline_window_root)
    candidate_window_root = _resolve_path(args.candidate_window_root) if str(args.candidate_window_root or "").strip() else None
    baseline_cycle_root = _resolve_path(args.baseline_cycle_root)
    candidate_cycle_root = _resolve_path(args.candidate_cycle_root) if str(args.candidate_cycle_root or "").strip() else None

    defaults = _default_paths()
    out_md = _resolve_path(args.out_md) if str(args.out_md or "").strip() else defaults["md"]
    out_json = _resolve_path(args.out_json) if str(args.out_json or "").strip() else defaults["json"]
    out_csv = _resolve_path(args.out_csv) if str(args.out_csv or "").strip() else defaults["csv"]

    payload = build_payload(
        baseline_window_root=baseline_window_root,
        candidate_window_root=candidate_window_root,
        baseline_cycle_root=baseline_cycle_root,
        candidate_cycle_root=candidate_cycle_root,
        evidence_tier=evidence_tier,
        run_label=str(args.run_label or "").strip() or "window_replay_comparison",
    )

    rows = list(payload.get("diff_ledger") or [])
    _write_json(out_json, payload, force=bool(args.force))
    _write_csv(out_csv, rows, force=bool(args.force))
    _write_text(out_md, _render_markdown(payload), force=bool(args.force))

    print(f"[OK] Wrote replay comparison markdown: {safe_rel(out_md)}")
    print(f"[OK] Wrote replay comparison JSON: {safe_rel(out_json)}")
    print(f"[OK] Wrote replay comparison CSV: {safe_rel(out_csv)}")


if __name__ == "__main__":
    main()
