#!/usr/bin/env python3
"""
Create a per-date Brain 2 Master Validation run report for the analysis-arena branch.

This is a reporting/helper utility only:
- Reads frozen sharepack tracker artifacts for the results date.
- Reads derived Brain 2 runtime receipts (board bundle / scoreboard / shadow DPL /
  translation sandbox manifest).
- Produces a board-level post-results validation shell with useful auto-captured anchors.

It does NOT rerun analyzers, rebuild tables, or claim final analytical verdicts.
The output is intentionally a hybrid:
- locked artifact references and bounded summaries are auto-filled
- section conclusions remain for analyst review
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import date as _date
from datetime import timedelta
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Sequence


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.tools.brain2_rank_contract import (
    RANK_INTEGRITY_INVALID_STATIC_ORDER,
    analytical_rank,
    input_order_key,
    rank_evaluation_status,
    unavailable_rank_contract,
)

RUNS_DIR = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"
RUNS2_DIR = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS_2"
TEMPLATE_PATH = (
    REPO_ROOT
    / "docs"
    / "AAT9_KIT"
    / "FINAL VALIDATION"
    / "final docs"
    / "AAT9_BRAIN2_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md"
)

MIRROR_MAP: Dict[str, str] = {
    "0": "5",
    "1": "6",
    "2": "7",
    "3": "8",
    "4": "9",
    "5": "0",
    "6": "1",
    "7": "2",
    "8": "3",
    "9": "4",
}

PREDICTIVE_TRACKER_FILES: dict[str, str] = {
    "profit_alerts": "profit_alerts.csv",
    "compound_events": "profit_compound_events.csv",
    "blackapple": "blackapple_alerts.csv",
    "due_doubles": "due_doubles.csv",
    "repeat_watch": "vtrac_repeat_watch.csv",
}

TRUTH_EVALUATION_FILES: dict[str, str] = {
    "profit_alerts_graded": "profit_alerts.csv",
    "profit_alerts_eval": "profit_alerts_eval.csv",
    "profit_alerts_eval_merged": "profit_alerts_eval_merged.csv",
    "compound_events_graded": "profit_compound_events.csv",
    "blackapple_graded": "blackapple_alerts.csv",
    "due_doubles_graded": "due_doubles.csv",
    "repeat_watch_graded": "vtrac_repeat_watch.csv",
}

# Frozen tables retain result-shaped columns for schema compatibility. They must
# contain placeholders only; populated values indicate predictive/truth mixing.
PREDICTIVE_RESULT_FIELD_RULES: dict[str, dict[str, tuple[str, ...]]] = {
    "profit_alerts": {
        "literal": ("Winner Midday", "Winner Evening"),
        "collection": ("Midday Hits", "Evening Hits"),
    },
    "compound_events": {
        "count": ("merged_rows_total", "merged_hits"),
        "boolean": ("merged_any_hit_within_decay",),
        "collection": ("merged_hit_types", "merged_any_hit_types"),
    },
    "blackapple": {
        "literal": ("Winner Midday", "Winner Evening"),
        "collection": ("Midday Hits", "Evening Hits"),
    },
    "due_doubles": {
        "literal": ("Winner Midday", "Winner Evening"),
        "boolean": ("Midday Winner In Family", "Evening Winner In Family"),
    },
    "repeat_watch": {
        "literal": ("Winner", "Winner VTRAC"),
        "boolean": ("Current==WinnerVTRAC",),
    },
}


@dataclass(frozen=True)
class DayArtifacts:
    bundle_md: Path
    bundle_json: Path
    scoreboard_md: Path
    scoreboard_json: Path
    overlay_md: Path
    overlay_json: Path
    shadow_md: Path
    shadow_json: Path
    sandbox_md: Path
    sandbox_json: Path


def parse_iso_date(value: str) -> _date:
    try:
        return _date.fromisoformat(value)
    except ValueError as exc:
        raise SystemExit(f"Invalid --date (expected YYYY-MM-DD): {value}") from exc


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def read_json(path: Path) -> Any:
    return json.loads(read_text(path))


def load_csv_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", errors="replace", newline="") as f:
        return [{k: (v or "") for k, v in row.items()} for row in csv.DictReader(f)]


def safe_int(value: Any) -> int | None:
    try:
        return int(str(value).strip())
    except Exception:
        return None


def safe_float(value: Any) -> float | None:
    try:
        return float(str(value).strip())
    except Exception:
        return None


def resolve_repo_path(value: str | Path) -> Path:
    path = Path(value)
    return path.resolve() if path.is_absolute() else (REPO_ROOT / path).resolve()


def _safe_rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _file_sha256(path: Path) -> str:
    if not path.is_file():
        return ""
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _source_receipt(
    *,
    path: Path,
    rows: Sequence[Mapping[str, Any]],
    claim_class: str,
    required: bool,
) -> dict[str, Any]:
    exists = path.is_file()
    return {
        "path": _safe_rel(path),
        "claim_class": claim_class,
        "required": required,
        "available": exists,
        "row_count": len(rows) if exists else 0,
        "sha256": _file_sha256(path),
        "status": "available" if exists else "missing",
    }


def _result_value_is_populated(value: Any, *, field_kind: str) -> bool:
    text = str(value or "").strip()
    lowered = text.lower()
    if field_kind == "literal":
        return lowered not in {"", "-", "none", "n/a", "?"}
    if field_kind == "boolean":
        return lowered not in {"", "-", "0", "false", "no", "n", "none", "n/a", "?"}
    if field_kind == "count":
        if lowered in {"", "-", "none", "n/a", "?"}:
            return False
        number = safe_float(text)
        return number is None or number != 0
    if field_kind == "collection":
        return lowered not in {"", "-", "[]", "{}", "none", "n/a", "?"}
    raise ValueError(f"Unsupported result field kind: {field_kind}")


def find_predictive_result_leakage(
    rows_by_source: Mapping[str, Sequence[Mapping[str, Any]]],
) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    for source_name, field_rules in PREDICTIVE_RESULT_FIELD_RULES.items():
        rows = rows_by_source.get(source_name) or []
        for row_number, row in enumerate(rows, start=2):
            for field_kind, field_names in field_rules.items():
                for field_name in field_names:
                    value = row.get(field_name, "")
                    if not _result_value_is_populated(value, field_kind=field_kind):
                        continue
                    findings.append(
                        {
                            "source": source_name,
                            "row_number": row_number,
                            "state_key": str(row.get("StateKey") or row.get("state_key") or ""),
                            "variant": str(row.get("Variant") or row.get("variant") or ""),
                            "field": field_name,
                            "value": str(value)[:120],
                        }
                    )
    return findings


def _profit_alert_identity(row: Mapping[str, Any]) -> str:
    state_key = str(row.get("StateKey") or row.get("state_key") or "").strip()
    variant = str(row.get("Variant") or row.get("variant") or "").strip()
    alert_id = str(row.get("AlertId") or row.get("alert_id") or "").strip()
    canonical = str(
        row.get("Canonical")
        or row.get("canonical")
        or row.get("canonical_raw")
        or ""
    ).strip()
    if not all((state_key, variant, alert_id, canonical)):
        return ""
    return "|".join((state_key, variant, alert_id, canonical))


def build_control_center_source_registry(
    *,
    results_date: str,
    predictive_control_center_dir: Path,
    truth_control_center_dir: Path,
    predictive_rows_by_source: Mapping[str, Sequence[Mapping[str, Any]]],
    truth_rows_by_source: Mapping[str, Sequence[Mapping[str, Any]]],
    predictive_meta: Mapping[str, Any] | None,
) -> dict[str, Any]:
    predictive_meta = predictive_meta or {}
    predictive_artifacts = {
        source_name: _source_receipt(
            path=predictive_control_center_dir / file_name,
            rows=predictive_rows_by_source.get(source_name) or [],
            claim_class="frozen_pre_result_definition",
            required=True,
        )
        for source_name, file_name in PREDICTIVE_TRACKER_FILES.items()
    }
    truth_artifacts = {
        source_name: _source_receipt(
            path=truth_control_center_dir / file_name,
            rows=truth_rows_by_source.get(source_name) or [],
            claim_class="post_result_evaluation",
            required=False,
        )
        for source_name, file_name in TRUTH_EVALUATION_FILES.items()
    }
    meta_path = predictive_control_center_dir / "meta.json"
    predictive_meta_receipt = _source_receipt(
        path=meta_path,
        rows=[predictive_meta] if meta_path.is_file() else [],
        claim_class="frozen_pre_result_provenance",
        required=True,
    )

    missing_predictive_sources = [
        name for name, receipt in predictive_artifacts.items() if not receipt["available"]
    ]
    if not predictive_meta_receipt["available"]:
        missing_predictive_sources.append("meta")

    leakage = find_predictive_result_leakage(predictive_rows_by_source)
    results_file = str(predictive_meta.get("results_file") or "")
    results_placeholder = "placeholder" in results_file.lower()
    state_entries = predictive_meta.get("states") if isinstance(predictive_meta.get("states"), list) else []
    metadata_winners_empty = all(
        not (row.get("winners") if isinstance(row, dict) else None)
        for row in state_entries
    )

    warnings: list[str] = []
    warnings.extend(f"MISSING_PREDICTIVE_SOURCE:{name}" for name in missing_predictive_sources)
    if predictive_meta_receipt["available"] and not results_placeholder:
        warnings.append("PREDICTIVE_RESULTS_FILE_NOT_PLACEHOLDER")
    if predictive_meta_receipt["available"] and not metadata_winners_empty:
        warnings.append("PREDICTIVE_META_WINNERS_PRESENT")
    if leakage:
        warnings.append("PREDICTIVE_RESULT_FIELDS_POPULATED")

    predictive_profit_ids = {
        identity
        for row in predictive_rows_by_source.get("profit_alerts") or []
        if (identity := _profit_alert_identity(row))
    }
    truth_profit_ids = {
        identity
        for row in truth_rows_by_source.get("profit_alerts_eval") or []
        if (identity := _profit_alert_identity(row))
    }
    matched_profit_ids = predictive_profit_ids & truth_profit_ids
    truth_join_status = "not_available"
    if truth_artifacts["profit_alerts_eval"]["available"]:
        truth_join_status = "complete" if truth_profit_ids <= predictive_profit_ids else "partial"

    hard_failure_codes: list[str] = []
    if leakage:
        hard_failure_codes.append("PREDICTIVE_RESULT_FIELDS_POPULATED")
    if predictive_meta_receipt["available"] and not results_placeholder:
        hard_failure_codes.append("PREDICTIVE_RESULTS_FILE_NOT_PLACEHOLDER")
    if predictive_meta_receipt["available"] and not metadata_winners_empty:
        hard_failure_codes.append("PREDICTIVE_META_WINNERS_PRESENT")
    status = "fail" if hard_failure_codes else ("warn" if warnings else "pass")
    return {
        "schema_version": "brain2_control_center_source_registry_v1",
        "results_date": results_date,
        "predictive": {
            "root": _safe_rel(predictive_control_center_dir.parent.parent),
            "control_center_dir": _safe_rel(predictive_control_center_dir),
            "claim_class": "frozen_pre_result_definition",
            "meta": {
                **predictive_meta_receipt,
                "generated_at_utc": str(predictive_meta.get("generated_at_utc") or ""),
                "history_date": str(predictive_meta.get("history_date") or ""),
                "results_file": results_file,
                "producer_script": str(predictive_meta.get("script") or ""),
            },
            "artifacts": predictive_artifacts,
        },
        "truth": {
            "root": _safe_rel(truth_control_center_dir.parent.parent),
            "control_center_dir": _safe_rel(truth_control_center_dir),
            "claim_class": "post_result_evaluation",
            "artifacts": truth_artifacts,
        },
        "truth_join": {
            "profit_alert_identity_fields": ["state_key", "variant", "alert_id", "canonical"],
            "status": truth_join_status,
            "predictive_identity_count": len(predictive_profit_ids),
            "truth_identity_count": len(truth_profit_ids),
            "matched_identity_count": len(matched_profit_ids),
            "unmatched_truth_identity_count": len(truth_profit_ids - predictive_profit_ids),
        },
        "integrity": {
            "status": status,
            "missing_predictive_sources": missing_predictive_sources,
            "predictive_result_fields_inert": not leakage,
            "predictive_results_file_is_placeholder": results_placeholder,
            "predictive_meta_winners_empty": metadata_winners_empty,
            "result_leakage_findings": leakage,
            "hard_failure_codes": hard_failure_codes,
            "warnings": warnings,
        },
    }


def _normalize_pick3_literal(value: Any) -> str:
    digits = "".join(ch for ch in str(value) if ch.isdigit())
    if not digits:
        return ""
    return digits.zfill(3) if len(digits) <= 3 else digits


def _is_double(triad: str) -> bool:
    triad = _normalize_pick3_literal(triad)
    return bool(triad) and len(set(triad)) == 2


def _is_triple(triad: str) -> bool:
    triad = _normalize_pick3_literal(triad)
    return bool(triad) and len(set(triad)) == 1


def _mirror_pairs_present(triad: str) -> list[str]:
    triad = _normalize_pick3_literal(triad)
    if not triad:
        return []
    digits = set(triad)
    out: list[str] = []
    for d, m in MIRROR_MAP.items():
        if d < m and d in digits and m in digits:
            out.append(f"{d}/{m}")
    return sorted(set(out))


def _ordered_unique(values: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for value in values:
        value = str(value).strip()
        if not value or value in seen:
            continue
        seen.add(value)
        out.append(value)
    return out


def _analysis_artifacts(analysis_arena_dir: Path, *, results_date: str, board_name: str) -> DayArtifacts:
    stem = board_name
    return DayArtifacts(
        bundle_md=analysis_arena_dir / f"{results_date}__BOARD_REVIEW_BUNDLE__{stem}.md",
        bundle_json=analysis_arena_dir / f"{results_date}__BOARD_REVIEW_BUNDLE__{stem}.json",
        scoreboard_md=analysis_arena_dir / f"{results_date}__BOARD_SCOREBOARD__{stem}.md",
        scoreboard_json=analysis_arena_dir / f"{results_date}__BOARD_SCOREBOARD__{stem}.json",
        overlay_md=analysis_arena_dir / f"{results_date}__BOARD_SPILLOVER_OVERLAY__{stem}.md",
        overlay_json=analysis_arena_dir / f"{results_date}__BOARD_SPILLOVER_OVERLAY__{stem}.json",
        shadow_md=analysis_arena_dir / f"{results_date}__SHADOW_DECISION_POLICY__{stem}.md",
        shadow_json=analysis_arena_dir / f"{results_date}__SHADOW_DECISION_POLICY__{stem}.json",
        sandbox_md=analysis_arena_dir / f"{results_date}__TRANSLATION_SANDBOX_SEED__{stem}.md",
        sandbox_json=analysis_arena_dir / f"{results_date}__TRANSLATION_SANDBOX_SEED__{stem}.json",
    )


def _fmt_path(path: Path) -> str:
    return f"`{_safe_rel(path)}`" if path.exists() else f"`{_safe_rel(path)}` (missing)"


def _fmt_list(items: Sequence[str], *, empty: str = "_none_") -> str:
    ordered = _ordered_unique(items)
    if not ordered:
        return empty
    return ", ".join(f"`{item}`" for item in ordered)


def _top_scoreboard_rows(rows: Sequence[dict[str, Any]], *, limit: int = 5) -> list[str]:
    out: list[str] = []
    for row in sorted(rows, key=input_order_key)[:limit]:
        canon = ", ".join((row.get("top_canonicals") or [])[:3]) or "-"
        out.append(
            f"`input={row.get('input_order') or row.get('input_rank') or '-'} {row.get('state_key')}` "
            f"legacy_rank=`{row.get('legacy_static_rank') or row.get('score_rank') or '-'}` "
            f"analytical_rank=`{analytical_rank(row) or '-'}` role=`{row.get('role')}` "
            f"bucket=`{row.get('targeting_bucket')}` tracker=`{row.get('tracker_posture')}` "
            f"canonicals=`{canon}`"
        )
    return out


def _scoreboard_state_rank_map(rows: Sequence[dict[str, Any]]) -> dict[str, int]:
    out: dict[str, int] = {}
    for row in rows:
        state_key = str(row.get("state_key") or "").strip()
        rank = analytical_rank(row)
        if state_key and rank is not None:
            out[state_key] = rank
    return out


def _group_profit_alerts(rows: Sequence[dict[str, str]]) -> list[str]:
    by_state: dict[str, dict[str, Any]] = {}
    for row in rows:
        state_key = (row.get("StateKey") or "").strip()
        if not state_key:
            continue
        slot = by_state.setdefault(state_key, {"count": 0, "strength": 0.0, "alerts": set(), "suggested": set()})
        slot["count"] += 1
        slot["strength"] += safe_float(row.get("Strength")) or 0.0
        if row.get("AlertId"):
            slot["alerts"].add(row["AlertId"].strip())
        if row.get("Suggested"):
            slot["suggested"].add(row["Suggested"].strip())
    ranked = sorted(
        by_state.items(),
        key=lambda item: (-item[1]["strength"], -item[1]["count"], item[0].lower()),
    )
    out: list[str] = []
    for state_key, info in ranked[:5]:
        out.append(
            f"`{state_key}` alerts=`{info['count']}` strength_sum=`{info['strength']:.1f}` "
            f"ids=`{','.join(sorted(info['alerts'])) or '-'}` suggested=`{','.join(sorted(info['suggested'])) or '-'}`"
        )
    return out


def _group_compound_events(rows: Sequence[dict[str, str]]) -> list[str]:
    ranked = sorted(
        rows,
        key=lambda row: (-(safe_int(row.get("priority")) or -1), row.get("state_key", ""), row.get("variant", "")),
    )
    out: list[str] = []
    for row in ranked[:6]:
        out.append(
            f"`{row.get('state_key','')}` `{row.get('variant','')}` top_event=`{row.get('top_event','')}` "
            f"priority=`{row.get('priority','')}` candidates=`{row.get('candidate_alert_ids','') or '-'}`"
        )
    return out


def _group_blackapple(rows: Sequence[dict[str, str]], *, status: str) -> list[str]:
    ranked = [
        row
        for row in rows
        if (row.get("Status") or "").strip().upper() == status.upper()
    ]
    ranked.sort(key=lambda row: (-(safe_int(row.get("BA-Score")) or -1), row.get("StateKey", ""), row.get("Variant", "")))
    out: list[str] = []
    for row in ranked[:8]:
        out.append(
            f"`{row.get('StateKey','')}` `{row.get('Variant','')}` BA=`{row.get('BA-Score','')}` "
            f"examples=`{row.get('Examples','') or '-'}`"
        )
    return out


def _top_profit_alert_states(rows: Sequence[dict[str, str]], *, rank_by_state: dict[str, int], limit: int = 8) -> list[dict[str, Any]]:
    by_state: dict[str, dict[str, Any]] = {}
    for row in rows:
        state_key = (row.get("StateKey") or "").strip()
        if not state_key:
            continue
        slot = by_state.setdefault(
            state_key,
            {
                "state_key": state_key,
                "board_rank": rank_by_state.get(state_key),
                "alert_count": 0,
                "strength_sum": 0.0,
                "alert_ids": set(),
                "suggested": set(),
            },
        )
        slot["alert_count"] += 1
        slot["strength_sum"] += safe_float(row.get("Strength")) or 0.0
        if row.get("AlertId"):
            slot["alert_ids"].add((row.get("AlertId") or "").strip())
        if row.get("Suggested"):
            slot["suggested"].add((row.get("Suggested") or "").strip())
    ranked = sorted(
        by_state.values(),
        key=lambda item: (-(item["strength_sum"]), -(item["alert_count"]), item["state_key"].lower()),
    )
    out: list[dict[str, Any]] = []
    for item in ranked[:limit]:
        out.append(
            {
                "state_key": item["state_key"],
                "board_rank": item["board_rank"],
                "alert_count": item["alert_count"],
                "strength_sum": round(float(item["strength_sum"]), 3),
                "alert_ids": sorted(item["alert_ids"]),
                "suggested": sorted(item["suggested"]),
            }
        )
    return out


def _top_compound_events(rows: Sequence[dict[str, str]], *, rank_by_state: dict[str, int], limit: int = 8) -> list[dict[str, Any]]:
    ranked = sorted(
        rows,
        key=lambda row: (-(safe_int(row.get("priority")) or -1), row.get("state_key", ""), row.get("variant", "")),
    )
    out: list[dict[str, Any]] = []
    for row in ranked[:limit]:
        state_key = (row.get("state_key") or row.get("StateKey") or "").strip()
        out.append(
            {
                "state_key": state_key,
                "board_rank": rank_by_state.get(state_key),
                "variant": (row.get("variant") or row.get("Variant") or "").strip(),
                "top_event": (row.get("top_event") or row.get("TopEvent") or "").strip(),
                "priority": safe_int(row.get("priority")) or safe_int(row.get("Priority")),
                "candidate_alert_ids": (row.get("candidate_alert_ids") or "").strip(),
            }
        )
    return out


def _top_blackapple_rows(
    rows: Sequence[dict[str, str]],
    *,
    rank_by_state: dict[str, int],
    status: str,
    limit: int = 8,
) -> list[dict[str, Any]]:
    ranked = [
        row
        for row in rows
        if (row.get("Status") or "").strip().upper() == status.upper()
    ]
    ranked.sort(key=lambda row: (-(safe_int(row.get("BA-Score")) or -1), row.get("StateKey", ""), row.get("Variant", "")))
    out: list[dict[str, Any]] = []
    for row in ranked[:limit]:
        state_key = (row.get("StateKey") or "").strip()
        out.append(
            {
                "state_key": state_key,
                "board_rank": rank_by_state.get(state_key),
                "variant": (row.get("Variant") or "").strip(),
                "ba_score": safe_int(row.get("BA-Score")),
                "status": (row.get("Status") or "").strip(),
                "examples": (row.get("Examples") or "").strip(),
                "triggers": (row.get("Triggers") or "").strip(),
            }
        )
    return out


def _top_repeat_watch_rows(
    rows: Sequence[dict[str, str]],
    *,
    rank_by_state: dict[str, int],
    limit: int = 8,
) -> list[dict[str, Any]]:
    ranked = sorted(
        rows,
        key=lambda row: (
            -(safe_float(row.get("Heat Hazard")) or -1.0),
            -(safe_int(row.get("Current Streak")) or -1),
            row.get("StateKey", ""),
            row.get("Variant", ""),
        ),
    )
    out: list[dict[str, Any]] = []
    for row in ranked[:limit]:
        state_key = (row.get("StateKey") or "").strip()
        out.append(
            {
                "state_key": state_key,
                "board_rank": rank_by_state.get(state_key),
                "variant": (row.get("Variant") or "").strip(),
                "current_index": (row.get("Current Index") or "").strip(),
                "winner_vtrac": (row.get("Winner VTRAC") or "").strip(),
                "heat_hazard": safe_float(row.get("Heat Hazard")),
                "current_streak": safe_int(row.get("Current Streak")),
                "current_equals_winner_vtrac": (row.get("Current==WinnerVTRAC") or "").strip() == "True",
            }
        )
    return out


def _scoreboard_hint_rows(
    scoreboard_rows: Sequence[dict[str, Any]],
    *,
    hint_key: str,
    limit: int = 8,
) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for row in sorted(scoreboard_rows, key=input_order_key):
        value = str(row.get(hint_key) or "").strip()
        if not value:
            continue
        out.append(
            {
                "state_key": str(row.get("state_key") or "").strip(),
                "board_rank": analytical_rank(row),
                "legacy_static_rank": safe_int(row.get("legacy_static_rank") or row.get("score_rank")),
                "input_order": safe_int(row.get("input_order") or row.get("input_rank")),
                "role": str(row.get("role") or "").strip(),
                "targeting_bucket": str(row.get("targeting_bucket") or "").strip(),
                "hint": value,
            }
        )
    return out[:limit]


def _combined_due_rows(rows: Sequence[dict[str, str]]) -> list[dict[str, str]]:
    out = [row for row in rows if (row.get("Variant") or "").strip() == "Combined"]
    out.sort(key=lambda row: (-(safe_int(row.get("Draws Since Double")) or -1), row.get("StateKey", "")))
    return out


def _due_threshold_rows(rows: Sequence[dict[str, str]], *, minimum: int = 3) -> list[dict[str, str]]:
    return [row for row in _combined_due_rows(rows) if (safe_int(row.get("Draws Since Double")) or -1) >= minimum]


def _due_converting_rows(rows: Sequence[dict[str, str]]) -> list[str]:
    out: list[str] = []
    for row in _due_threshold_rows(rows):
        if (row.get("Midday Winner In Family") or "").strip() == "True" or (row.get("Evening Winner In Family") or "").strip() == "True":
            out.append(
                f"`{row.get('StateKey','')}` DS=`{row.get('Draws Since Double','')}` "
                f"midday_in_family=`{row.get('Midday Winner In Family','')}` "
                f"evening_in_family=`{row.get('Evening Winner In Family','')}`"
            )
    return out


def _daily_double_events(
    rows: Sequence[dict[str, str]],
    *,
    rank_by_state: dict[str, int],
) -> list[str]:
    out: list[str] = []
    for row in _combined_due_rows(rows):
        state_key = (row.get("StateKey") or "").strip()
        ds = row.get("Draws Since Double", "")
        for period_key, winner_key in (("Midday", "Winner Midday"), ("Evening", "Winner Evening")):
            winner = _normalize_pick3_literal(row.get(winner_key, ""))
            if not winner:
                continue
            mirror_pairs = _mirror_pairs_present(winner)
            if _is_triple(winner):
                kind = "triple"
            elif _is_double(winner):
                kind = "double"
            elif mirror_pairs:
                kind = "mirror_double"
            else:
                continue
            out.append(
                f"`{state_key}` `{period_key}` winner=`{winner}` type=`{kind}` "
                f"analytical_rank=`{rank_by_state.get(state_key, '-')}` DS=`{ds}` mirror_pairs=`{','.join(mirror_pairs) or '-'}`"
            )
    return out


def _daily_double_events_from_inventory(
    path: Path | None,
    *,
    results_date: str,
    rank_by_state: Mapping[str, int],
) -> list[str]:
    if path is None or not path.is_file():
        return []
    out: list[str] = []
    for row in load_csv_rows(path):
        if str(row.get("date") or "").strip() != results_date:
            continue
        state_key = str(row.get("state") or "").strip()
        period = str(row.get("period") or "").strip()
        winner = _normalize_pick3_literal(row.get("winner") or "")
        event_type = str(row.get("type") or "").strip()
        if not all((state_key, period, winner, event_type)):
            continue
        out.append(
            f"`{state_key}` `{period}` winner=`{winner}` type=`{event_type}` "
            f"analytical_rank=`{rank_by_state.get(state_key, '-')}` mirror_pairs=`{row.get('mirror_pairs') or '-'}`"
        )
    return out


def _top_reason_codes(state_decisions: Sequence[dict[str, Any]], *, limit: int = 8) -> list[str]:
    counts: Counter[str] = Counter()
    for row in state_decisions:
        for code in row.get("reason_codes") or []:
            code = str(code).strip()
            if code:
                counts[code] += 1
    return [f"`{code}` x{count}" for code, count in counts.most_common(limit)]


def _load_translation_learning(translation_manifest_json: Path) -> dict[str, list[str]]:
    if not translation_manifest_json.exists():
        return {
            "boxed": [],
            "straight": [],
            "vt_box": [],
            "positional": [],
            "blackapple": [],
            "profit": [],
            "due": [],
            "preserved": [],
        }

    manifest = read_json(translation_manifest_json)
    receipts = manifest.get("state_receipts") if isinstance(manifest, dict) else []
    boxed: Counter[str] = Counter()
    straight: Counter[str] = Counter()
    vt_box: Counter[str] = Counter()
    positional: Counter[str] = Counter()
    blackapple: Counter[str] = Counter()
    profit: Counter[str] = Counter()
    due: Counter[str] = Counter()
    preserved: Counter[str] = Counter()

    for receipt in receipts if isinstance(receipts, list) else []:
        seed_path_raw = str(receipt.get("seed_json") or "").strip()
        if not seed_path_raw:
            continue
        seed_path = REPO_ROOT / seed_path_raw
        if not seed_path.exists():
            continue
        try:
            seed = read_json(seed_path)
        except Exception:
            continue
        sand = seed.get("sandbox_hypotheses") if isinstance(seed.get("sandbox_hypotheses"), dict) else {}
        brain2 = seed.get("brain2_context") if isinstance(seed.get("brain2_context"), dict) else {}
        control_arm = seed.get("control_arm") if isinstance(seed.get("control_arm"), dict) else {}

        for item in sand.get("diagnostic_boxed_seed") or []:
            value = str(item.get("value") or "").strip()
            if value:
                boxed[value] += 1
        for item in sand.get("diagnostic_straight_seed") or []:
            value = str(item.get("value") or "").strip()
            if value:
                straight[value] += 1
        for item in sand.get("diagnostic_vt_box_seed") or []:
            value = str(item.get("value") or "").strip()
            if value:
                vt_box[value] += 1

        for item in brain2.get("positional_shortlist_top") or []:
            value = str(item.get("canonical") or item.get("combo") or "").strip()
            if value:
                positional[value] += 1
        for value in brain2.get("blackapple_recommended_canonicals") or []:
            value = str(value).strip()
            if value:
                blackapple[value] += 1
        for value in brain2.get("profit_alert_implied_canonicals") or []:
            value = str(value).strip()
            if value:
                profit[value] += 1
        for value in brain2.get("due_double_example_canonicals") or []:
            value = str(value).strip()
            if value:
                due[value] += 1
        for value in control_arm.get("preserved_not_budgeted_canonicals_top") or []:
            value = str(value).strip()
            if value:
                preserved[value] += 1

    def pack(counter: Counter[str]) -> list[str]:
        return [f"`{value}` x{count}" for value, count in counter.most_common(6)]

    return {
        "boxed": pack(boxed),
        "straight": pack(straight),
        "vt_box": pack(vt_box),
        "positional": pack(positional),
        "blackapple": pack(blackapple),
        "profit": pack(profit),
        "due": pack(due),
        "preserved": pack(preserved),
    }


def build_brain2_tracker_ledger(
    *,
    results_date: str,
    history_date: str,
    artifacts: DayArtifacts,
    board_scope_states: Sequence[str],
    scoreboard_rows: Sequence[dict[str, Any]],
    board_verdict: dict[str, Any],
    shadow_verdict: dict[str, Any],
    profit_alert_rows: Sequence[dict[str, str]],
    compound_rows: Sequence[dict[str, str]],
    blackapple_rows: Sequence[dict[str, str]],
    due_rows: Sequence[dict[str, str]],
    tracker_rows: Sequence[dict[str, str]],
    truth_profit_alert_rows: Sequence[dict[str, str]],
    truth_compound_rows: Sequence[dict[str, str]],
    truth_blackapple_rows: Sequence[dict[str, str]],
    truth_due_rows: Sequence[dict[str, str]],
    truth_tracker_rows: Sequence[dict[str, str]],
    translation_learning: dict[str, list[str]],
    predictive_control_center_dir: Path,
    truth_control_center_dir: Path,
    tracker_source_registry: Mapping[str, Any],
    doubles_inventory_md: Path | None = None,
    doubles_inventory_csv: Path | None = None,
) -> dict[str, Any]:
    rank_by_state = _scoreboard_state_rank_map(scoreboard_rows)
    due_threshold_rows = _due_threshold_rows(due_rows)
    daily_double_events = _daily_double_events(truth_due_rows, rank_by_state=rank_by_state)
    if not daily_double_events:
        daily_double_events = _daily_double_events_from_inventory(
            doubles_inventory_csv,
            results_date=results_date,
            rank_by_state=rank_by_state,
        )
    repeat_watch_top = _top_repeat_watch_rows(tracker_rows, rank_by_state=rank_by_state)
    truth_repeat_watch_top = _top_repeat_watch_rows(truth_tracker_rows, rank_by_state=rank_by_state)
    repeat_watch_hits = [
        row for row in truth_repeat_watch_top if bool(row.get("current_equals_winner_vtrac"))
    ]
    predictive_sources = tracker_source_registry.get("predictive", {}).get("artifacts", {})
    return {
        "schema_version": "brain2_tracker_ledger_v2",
        "metadata": {
            "results_date": results_date,
            "history_date": history_date,
            "board_scope_states": list(board_scope_states),
            "analysis_artifacts": {
                "scoreboard_json": _safe_rel(artifacts.scoreboard_json),
                "shadow_json": _safe_rel(artifacts.shadow_json),
                "translation_manifest_json": _safe_rel(artifacts.sandbox_json),
            },
            "control_center_dir": _safe_rel(predictive_control_center_dir),
            "predictive_control_center_dir": _safe_rel(predictive_control_center_dir),
            "truth_control_center_dir": _safe_rel(truth_control_center_dir),
            "doubles_inventory_md": _safe_rel(doubles_inventory_md) if doubles_inventory_md else "",
            "doubles_inventory_csv": _safe_rel(doubles_inventory_csv) if doubles_inventory_csv else "",
            "rank_integrity_status": RANK_INTEGRITY_INVALID_STATIC_ORDER,
        },
        "rank_contract": unavailable_rank_contract(),
        "rank_evaluation": rank_evaluation_status(scoreboard_rows),
        "source_registry": dict(tracker_source_registry),
        "truth_evaluation": {
            "claim_class": "post_result_evaluation",
            "profit_alerts_row_count": len(truth_profit_alert_rows),
            "compound_events_row_count": len(truth_compound_rows),
            "blackapple_row_count": len(truth_blackapple_rows),
            "due_doubles_row_count": len(truth_due_rows),
            "repeat_watch_row_count": len(truth_tracker_rows),
            "due_doubles_converting_rows": _due_converting_rows(truth_due_rows),
            "daily_double_events": daily_double_events[:16],
            "repeat_watch_exact_hits": repeat_watch_hits,
        },
        "board_context": {
            "top_primary_target": board_verdict.get("top_primary_target") or "",
            "secondary_target": board_verdict.get("secondary_target") or "",
            "best_clean_host": board_verdict.get("best_clean_host") or "",
            "highest_context_support_state": board_verdict.get("highest_context_support_state") or "",
            "play_states": list(shadow_verdict.get("play_states") or []),
            "watch_states": list(shadow_verdict.get("watch_states") or []),
            "skip_states": list(shadow_verdict.get("skip_states") or []),
            "unresolved_states": list(shadow_verdict.get("unresolved_states") or []),
        },
        "profit_alerts": {
            "available": bool(predictive_sources.get("profit_alerts", {}).get("available")),
            "row_count": len(profit_alert_rows),
            "source": predictive_sources.get("profit_alerts", {}),
            "top_states": _top_profit_alert_states(profit_alert_rows, rank_by_state=rank_by_state),
            "scoreboard_carries": _scoreboard_hint_rows(scoreboard_rows, hint_key="profit_alert_hint"),
        },
        "compound_events": {
            "available": bool(predictive_sources.get("compound_events", {}).get("available")),
            "row_count": len(compound_rows),
            "source": predictive_sources.get("compound_events", {}),
            "top_rows": _top_compound_events(compound_rows, rank_by_state=rank_by_state),
            "scoreboard_carries": _scoreboard_hint_rows(scoreboard_rows, hint_key="compound_event_hint"),
        },
        "blackapple": {
            "available": bool(predictive_sources.get("blackapple", {}).get("available")),
            "row_count": len(blackapple_rows),
            "source": predictive_sources.get("blackapple", {}),
            "alert_states": _top_blackapple_rows(blackapple_rows, rank_by_state=rank_by_state, status="ALERT"),
            "watch_states": _top_blackapple_rows(blackapple_rows, rank_by_state=rank_by_state, status="WATCH"),
            "scoreboard_carries": _scoreboard_hint_rows(scoreboard_rows, hint_key="blackapple_reco_hint"),
        },
        "due_doubles": {
            "available": bool(predictive_sources.get("due_doubles", {}).get("available")),
            "row_count": len(due_rows),
            "source": predictive_sources.get("due_doubles", {}),
            "threshold_states": [
                {
                    "state_key": (row.get("StateKey") or "").strip(),
                    "board_rank": rank_by_state.get((row.get("StateKey") or "").strip()),
                    "draws_since_double": safe_int(row.get("Draws Since Double")),
                }
                for row in due_threshold_rows[:12]
            ],
            "converting_rows": _due_converting_rows(truth_due_rows),
            "daily_double_events": daily_double_events[:16],
            "scoreboard_carries": _scoreboard_hint_rows(scoreboard_rows, hint_key="due_double_hint"),
        },
        "repeat_watch": {
            "available": bool(predictive_sources.get("repeat_watch", {}).get("available")),
            "row_count": len(tracker_rows),
            "source": predictive_sources.get("repeat_watch", {}),
            "top_rows": repeat_watch_top,
            "exact_hits": repeat_watch_hits,
        },
        "consensus": {
            "scoreboard_carries": _scoreboard_hint_rows(scoreboard_rows, hint_key="r_consensus_hint"),
        },
        "survivor": {
            "scoreboard_carries": _scoreboard_hint_rows(scoreboard_rows, hint_key="survivor_hint"),
        },
        "translation_learning": translation_learning,
    }


def build_brain2_master_validation_report(
    *,
    results_date: str,
    history_date: str,
    artifacts: DayArtifacts,
    template_path: Path,
    board_scope_states: Sequence[str],
    scoreboard_rows: Sequence[dict[str, Any]],
    board_verdict: dict[str, Any],
    duplicate_pairs: Sequence[dict[str, Any]],
    shadow_verdict: dict[str, Any],
    state_decisions: Sequence[dict[str, Any]],
    profit_alert_rows: Sequence[dict[str, str]],
    compound_rows: Sequence[dict[str, str]],
    blackapple_rows: Sequence[dict[str, str]],
    due_rows: Sequence[dict[str, str]],
    tracker_rows: Sequence[dict[str, str]],
    truth_profit_alert_rows: Sequence[dict[str, str]],
    truth_compound_rows: Sequence[dict[str, str]],
    truth_blackapple_rows: Sequence[dict[str, str]],
    truth_due_rows: Sequence[dict[str, str]],
    truth_tracker_rows: Sequence[dict[str, str]],
    translation_learning: dict[str, list[str]],
    predictive_control_center_dir: Path,
    truth_control_center_dir: Path,
    tracker_source_registry: Mapping[str, Any],
    control_arm_runs_dir: Path,
    doubles_inventory_md: Path | None = None,
    doubles_inventory_csv: Path | None = None,
) -> str:
    source_integrity = tracker_source_registry.get("integrity", {})
    truth_sources = tracker_source_registry.get("truth", {}).get("artifacts", {})
    rank_by_state = _scoreboard_state_rank_map(scoreboard_rows)
    rank_evaluation = rank_evaluation_status(scoreboard_rows)
    top_rows = _top_scoreboard_rows(scoreboard_rows)
    direct_receipts = board_verdict.get("direct_cross_state_receipts") or []
    strongest_pairs = []
    for pair in list(duplicate_pairs)[:5]:
        strongest_pairs.append(
            f"`{pair.get('state_a')}` + `{pair.get('state_b')}` score=`{pair.get('pair_score')}` "
            f"types=`{','.join(pair.get('relationship_types') or []) or '-'}`"
        )

    due_threshold = [
        f"`{row.get('StateKey','')}` DS=`{row.get('Draws Since Double','')}`"
        for row in _due_threshold_rows(due_rows)
    ]
    daily_double_events = _daily_double_events(truth_due_rows, rank_by_state=rank_by_state)
    if not daily_double_events:
        daily_double_events = _daily_double_events_from_inventory(
            doubles_inventory_csv,
            results_date=results_date,
            rank_by_state=rank_by_state,
        )
    repeat_hits = [
        f"`{row.get('StateKey','')}` `{row.get('Variant','')}` idx=`{row.get('Current Index','')}`"
        for row in truth_tracker_rows
        if (row.get("Current==WinnerVTRAC") or "").strip() == "True"
    ]

    play_states = shadow_verdict.get("play_states") or []
    watch_states = shadow_verdict.get("watch_states") or []
    skip_states = shadow_verdict.get("skip_states") or []
    unresolved_states = shadow_verdict.get("unresolved_states") or []

    lines: list[str] = []
    lines.append(f"# Brain 2 Master Validation Run Report — D={results_date} (H={history_date})")
    lines.append("")
    lines.append("Reference template:")
    lines.append(f"- `{_safe_rel(template_path)}`")
    lines.append("")
    lines.append("Relationship to the arena-era workflow:")
    lines.append(f"- Board runtime template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_BRAIN2_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`")
    lines.append(f"- Per-state Master Validation template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_MASTER_VALIDATION_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`")
    lines.append(f"- Translation sandbox template: `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_TRANSLATION_SANDBOX_TEMPLATE__ANALYSIS_ARENA_BRANCH.md`")
    lines.append("")
    lines.append("## Rank Integrity Warning")
    lines.append("")
    lines.append("**RANK INTEGRITY STATUS: `INVALID_STATIC_ORDER`**")
    lines.append("")
    lines.append(
        "Current board rank fields are legacy, state-order-dominated priority receipts. "
        "They must not be interpreted as an evidence-derived analytical ranking."
    )
    lines.append("")
    lines.append(
        "Capture@K, top-ranked-state, and rank-performance conclusions are `NOT_EVALUABLE` "
        "until Phase 2 supplies an explicit valid analytical-rank contract."
    )
    lines.append("")
    lines.append("## Scope")
    lines.append(f"- Results date (D): `{results_date}`")
    lines.append(f"- History workbook date (H): `{history_date}`")
    lines.append(f"- Board scope states ({len(board_scope_states)}): {_fmt_list(board_scope_states)}")
    lines.append("- Full-day tracker scope: `all states represented in the frozen control_center sharepack tables`")
    lines.append("")
    lines.append("## Locked Artifacts")
    lines.append(f"- Board review bundle: {_fmt_path(artifacts.bundle_md)} / {_fmt_path(artifacts.bundle_json)}")
    lines.append(f"- Board scoreboard: {_fmt_path(artifacts.scoreboard_md)} / {_fmt_path(artifacts.scoreboard_json)}")
    lines.append(f"- Board spillover overlay: {_fmt_path(artifacts.overlay_md)} / {_fmt_path(artifacts.overlay_json)}")
    lines.append(f"- Shadow DPL: {_fmt_path(artifacts.shadow_md)} / {_fmt_path(artifacts.shadow_json)}")
    lines.append(f"- Translation sandbox day manifest: {_fmt_path(artifacts.sandbox_md)} / {_fmt_path(artifacts.sandbox_json)}")
    lines.append(f"- Predictive Control Center root: `{_safe_rel(predictive_control_center_dir)}`")
    lines.append(f"- Truth/evaluation Control Center root: `{_safe_rel(truth_control_center_dir)}`")
    lines.append(
        f"- Predictive source integrity: `{str(source_integrity.get('status') or 'unknown').upper()}` "
        f"result_fields_inert=`{bool(source_integrity.get('predictive_result_fields_inert'))}`"
    )
    lines.append(
        "- Truth/evaluation receipts available: "
        + _fmt_list(
            [name for name, receipt in truth_sources.items() if receipt.get("available")],
            empty="_none available_",
        )
    )
    lines.append(f"- Control-arm grade directory: `{_safe_rel(control_arm_runs_dir)}`")
    if doubles_inventory_md or doubles_inventory_csv:
        lines.append(
            "- Window doubles inventory: "
            + " / ".join(
                item
                for item in (
                    _fmt_path(doubles_inventory_md) if doubles_inventory_md else "",
                    _fmt_path(doubles_inventory_csv) if doubles_inventory_csv else "",
                )
                if item
            )
        )
    lines.append("")
    lines.append("## Quick Auto-Captured Anchors")
    lines.append(f"- Board evidence rows (input order; legacy rank diagnostic-only): {'; '.join(top_rows) if top_rows else '_none_'}")
    lines.append(f"- Board verdict top_primary_target: `{board_verdict.get('top_primary_target') or '-'}`")
    lines.append(f"- Board verdict secondary_target: `{board_verdict.get('secondary_target') or '-'}`")
    lines.append(f"- Board verdict best_clean_host: `{board_verdict.get('best_clean_host') or '-'}`")
    lines.append(f"- Board verdict highest_context_support_state: `{board_verdict.get('highest_context_support_state') or '-'}`")
    lines.append(f"- Shadow DPL play states: {_fmt_list(play_states)}")
    lines.append(f"- Shadow DPL watch states: {_fmt_list(watch_states)}")
    lines.append(f"- Shadow DPL unresolved states: {_fmt_list(unresolved_states)}")
    lines.append(f"- Daily doubles / mirror doubles detected: {_fmt_list(daily_double_events, empty='_none detected_')}")
    lines.append("")
    lines.append("---")
    lines.append("")

    def add_section(title: str, bullets: Sequence[str], prompts: Sequence[str]) -> None:
        lines.append(f"## {title}")
        lines.append("")
        lines.append("Auto-captured anchors:")
        for bullet in bullets or ["- _none_"]:
            lines.append(f"- {bullet}" if not bullet.startswith("- ") else bullet)
        lines.append("")
        lines.append("Analyst conclusion:")
        for prompt in prompts:
            lines.append(f"- {prompt}")
        lines.append("")

    add_section(
        "Part A — File Lock And Scope",
        [
            f"board scope states: {_fmt_list(board_scope_states)}",
            f"frozen predictive tracker artifacts: `{_safe_rel(predictive_control_center_dir / 'profit_alerts.csv')}`, `{_safe_rel(predictive_control_center_dir / 'profit_compound_events.csv')}`, `{_safe_rel(predictive_control_center_dir / 'blackapple_alerts.csv')}`, `{_safe_rel(predictive_control_center_dir / 'due_doubles.csv')}`, `{_safe_rel(predictive_control_center_dir / 'vtrac_repeat_watch.csv')}`",
            f"post-result evaluation root (kept separate): `{_safe_rel(truth_control_center_dir)}`",
            "sharepack remains the frozen raw day snapshot; board artifacts are derived arena-era receipts on top of it",
        ],
        [
            "board scope notes: `...`",
            "full-day tracker scope notes: `...`",
            "missing artifact notes: `...`",
        ],
    )

    add_section(
        "Part B — Board Outcome Map",
        [
            f"board evidence anchors (input order): {'; '.join(top_rows[:3]) if top_rows else '_none_'}",
            f"daily doubles / mirror doubles on the day: {_fmt_list(daily_double_events, empty='_none_')}",
            f"direct cross-state receipts surfaced by board verdict: {_fmt_list([str(x) for x in direct_receipts], empty='_none_')}",
        ],
        [
            "actual strongest day states: `...`",
            "states that converted meaningful structure: `...`",
            "states that were mostly echo / ambient only: `...`",
            "day-level structural class: `...`",
            "most important truth-side board insight: `...`",
        ],
    )

    add_section(
        "Part C — Board Evidence And Rank Integrity Evaluation",
        [
            f"rank evaluation status: `{rank_evaluation.get('status')}` reason=`{rank_evaluation.get('reason') or '-'}`",
            f"board evidence rows (not analytically ranked): {'; '.join(top_rows) if top_rows else '_none_'}",
            f"top_primary_target=`{board_verdict.get('top_primary_target') or '-'}` secondary_target=`{board_verdict.get('secondary_target') or '-'}`",
            f"best_clean_host=`{board_verdict.get('best_clean_host') or '-'}` highest_context_support_state=`{board_verdict.get('highest_context_support_state') or '-'}`",
            f"tight_core_states={_fmt_list(board_verdict.get('tight_core_states') or [], empty='-')}",
            f"watch_only_states={_fmt_list(board_verdict.get('watch_only_states') or [], empty='-')}",
            f"small_shoulder_states={_fmt_list(board_verdict.get('small_shoulder_states') or [], empty='-')}",
        ],
        [
            "analytical rank conclusion: `NOT_EVALUABLE — INVALID_STATIC_ORDER`",
            "rank-independent bucket and structural-evidence notes: `...`",
            "legacy ordering distortion notes (diagnostic only): `...`",
            "requirements for a future evidence-derived shadow ranker: `...`",
        ],
    )

    add_section(
        "Part D — Shared Complexes, Carryover, And Spillover",
        [
            f"strongest overlap pairs: {'; '.join(strongest_pairs) if strongest_pairs else '_none_'}",
            f"direct cross-state receipts: {_fmt_list([str(x) for x in direct_receipts], empty='_none_')}",
            f"best relationship source: `{board_verdict.get('best_relationship_source') or '-'}`",
        ],
        [
            "most important shared complexes: `...`",
            "most important host state: `...`",
            "most important echo state: `...`",
            "most important cross-state carryover receipt: `...`",
            "did the board correctly treat the day as a shared pending complex?: `...`",
            "most important spillover lesson: `...`",
        ],
    )

    add_section(
        "Part E — Aggregate Tracker Inventory",
        [
            f"highest-value alert states: {'; '.join(_group_profit_alerts(profit_alert_rows)) or '_none_'}",
            f"compound-event leaders: {'; '.join(_group_compound_events(compound_rows)) or '_none_'}",
            f"Blackapple ALERT states: {'; '.join(_group_blackapple(blackapple_rows, status='ALERT')) or '_none_'}",
            f"due-double threshold states (DS>=3): {'; '.join(due_threshold[:8]) if due_threshold else '_none_'}",
            f"repeat-watch exact hits: {'; '.join(repeat_hits) if repeat_hits else '_none_'}",
            f"separate truth/evaluation rows: alerts=`{len(truth_profit_alert_rows)}` compounds=`{len(truth_compound_rows)}` BA=`{len(truth_blackapple_rows)}` due=`{len(truth_due_rows)}` repeat=`{len(truth_tracker_rows)}`",
        ],
        [
            "most important board-scope tracker states: `...`",
            "most important full-day tracker states outside the board: `...`",
            "did tracker posture materially explain the day?: `...`",
            "most important aggregate-tracker insight: `...`",
        ],
    )

    add_section(
        "Part F — Profit Alerts And Special Compound Events",
        [
            f"highest-value alert states: {'; '.join(_group_profit_alerts(profit_alert_rows)) or '_none_'}",
            f"top compound-event rows: {'; '.join(_group_compound_events(compound_rows)) or '_none_'}",
            f"profit alerts source: `{_safe_rel(predictive_control_center_dir / 'profit_alerts.csv')}`",
            f"compound events source: `{_safe_rel(predictive_control_center_dir / 'profit_compound_events.csv')}`",
        ],
        [
            "most important alert IDs: `...`",
            "implied-set conversions: `...`",
            "most important special compound events: `...`",
            "alert-rich but structurally weak states: `...`",
            "did profit alerts / compound events materially improve Brain 2?: `...`",
            "most important alert-layer lesson: `...`",
        ],
    )

    add_section(
        "Part G — Blackapple Board Review",
        [
            f"BA ALERT states: {'; '.join(_group_blackapple(blackapple_rows, status='ALERT')) or '_none_'}",
            f"BA WATCH states: {'; '.join(_group_blackapple(blackapple_rows, status='WATCH')) or '_none_'}",
            f"Blackapple source: `{_safe_rel(predictive_control_center_dir / 'blackapple_alerts.csv')}`",
        ],
        [
            "important BA recommendation carries: `...`",
            "states where BA looked stronger than the board gave credit for: `...`",
            "did BA function mainly as host indicator / echo amplifier / shortlist helper / noise / mixed?: `...`",
            "most important BA lesson: `...`",
        ],
    )

    add_section(
        "Part H — Due Doubles Mechanism-Specific State Evaluation",
        [
            f"due-mechanism states reviewed by Draws Since Double (DS>=3): {'; '.join(due_threshold) if due_threshold else '_none_'}",
            f"top due states that converted in-family: {'; '.join(_due_converting_rows(truth_due_rows)) or '_none / truth receipt unavailable_'}",
            f"due doubles source: `{_safe_rel(predictive_control_center_dir / 'due_doubles.csv')}`",
        ],
        [
            "top due states that failed: `...`",
            "threshold states (3 draws missing) that converted: `...`",
            "important due families / examples that converted: `...`",
            "conversion class notes: `...`",
            "most important due-doubles mechanism-order lesson: `...`",
        ],
    )

    add_section(
        "Part I — All Daily Doubles And Mirror Doubles Evidence Audit",
        [
            f"daily doubles / mirror doubles reviewed: {'; '.join(daily_double_events) if daily_double_events else '_none_'}",
            f"support sources: due-doubles=`{_safe_rel(predictive_control_center_dir / 'due_doubles.csv')}` BA=`{_safe_rel(predictive_control_center_dir / 'blackapple_alerts.csv')}` alerts=`{_safe_rel(predictive_control_center_dir / 'profit_alerts.csv')}`",
            f"window doubles inventory: {(' / '.join(x for x in (_fmt_path(doubles_inventory_md) if doubles_inventory_md else '', _fmt_path(doubles_inventory_csv) if doubles_inventory_csv else '') if x)) if (doubles_inventory_md or doubles_inventory_csv) else '_not provided_'}",
        ],
        [
            "most important strong-evidence double: `...`",
            "most important weak-evidence double: `...`",
            "most important doubles / mirror-doubles lesson: `...`",
        ],
    )

    add_section(
        "Part J — Shadow DPL And Board Posture Evaluation",
        [
            f"play states: {_fmt_list(play_states)}",
            f"watch states: {_fmt_list(watch_states)}",
            f"skip states: {_fmt_list(skip_states)}",
            f"unresolved states: {_fmt_list(unresolved_states)}",
            f"top useful reason codes: {'; '.join(_top_reason_codes(state_decisions)) or '_none_'}",
            f"top_play_state=`{shadow_verdict.get('top_play_state') or '-'}` top_watch_state=`{shadow_verdict.get('top_watch_state') or '-'}`",
        ],
        [
            "rank-dependent DPL conclusion: `NOT_EVALUABLE — decisions remain UNRESOLVED`",
            "rank-independent structural modes worth preserving: `...`",
            "independent hard blockers (for example locally spent) observed: `...`",
            "most important DPL quarantine lesson: `...`",
        ],
    )

    add_section(
        "Part K — Translation Sandbox / Combination Learning Capture",
        [
            f"strongest boxed themes: {'; '.join(translation_learning.get('boxed') or []) or '_none_'}",
            f"strongest straight themes: {'; '.join(translation_learning.get('straight') or []) or '_none_'}",
            f"strongest VT-box themes: {'; '.join(translation_learning.get('vt_box') or []) or '_none_'}",
            f"repeated positional shortlist carries: {'; '.join(translation_learning.get('positional') or []) or '_none_'}",
            f"repeated Blackapple carries: {'; '.join(translation_learning.get('blackapple') or []) or '_none_'}",
            f"profit-alert implied carries: {'; '.join(translation_learning.get('profit') or []) or '_none_'}",
            f"due-double carries: {'; '.join(translation_learning.get('due') or []) or '_none_'}",
            f"preserved-not-budgeted canonicals: {'; '.join(translation_learning.get('preserved') or []) or '_none_'}",
        ],
        [
            "most important preserved-not-budgeted cluster: `...`",
            "strongest translator-learning note: `...`",
        ],
    )

    add_section(
        "Part L — Control-Arm Comparison",
        [
            f"candidate-universe grade: `{_safe_rel(control_arm_runs_dir / f'{results_date}__CANDIDATE_UNIVERSE_GRADE__tool_only__arena_v0.md')}`",
            f"play-card grade: `{_safe_rel(control_arm_runs_dir / f'{results_date}__PLAY_CARD_GRADE__tool_only__arena_v0.md')}`",
            "B12/B24/B36 remain the baseline/control-arm comparison surface, not the arena branch truth",
        ],
        [
            "most important control-arm success: `...`",
            "most important control-arm suppression: `...`",
            "did the control arm outperform, underperform, or mostly lag Brain 2 truth?: `...`",
            "most important control-arm lesson: `...`",
        ],
    )

    add_section(
        "Part M — Final Board Lessons And Promotions",
        [
            f"top board runtime artifacts locked above; use this section to end with board-level lessons rather than state-by-state repetition",
        ],
        [
            "strongest board-level insight: `...`",
            "strongest tracker insight: `...`",
            "strongest cross-state carryover insight: `...`",
            "strongest doubles / mirror-doubles insight: `...`",
            "strongest translation-learning insight: `...`",
            "one thing that deserves later promotion: `...`",
            "one thing that should remain research-only for now: `...`",
            "one structural follow-up target: `...`",
            "one thing to watch on the next fresh runs: `...`",
        ],
    )

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", required=True, help="Results date D (YYYY-MM-DD)")
    ap.add_argument(
        "--analysis-arena-dir",
        required=True,
        help="Directory containing the Brain 2 runtime artifacts for the day",
    )
    ap.add_argument(
        "--board-name",
        default="analysis_arena_day_review",
        help="Board artifact suffix/name (default: analysis_arena_day_review)",
    )
    ap.add_argument(
        "--predictive-sharepacks-root",
        default="sharepacks/_predictive",
        help="Root containing frozen pre-result sharepacks (default: sharepacks/_predictive)",
    )
    ap.add_argument(
        "--truth-sharepacks-root",
        default="sharepacks",
        help="Root containing optional post-result evaluation sharepacks (default: sharepacks)",
    )
    ap.add_argument(
        "--strict-predictive-sources",
        action="store_true",
        help="Fail when any required frozen tracker source or its meta.json is missing.",
    )
    ap.add_argument(
        "--out",
        help="Output Markdown path (default: docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/<D>__BRAIN2_MASTER_VALIDATION.md)",
    )
    ap.add_argument(
        "--out-json",
        help="Optional structured tracker-ledger JSON path (default: alongside the markdown output).",
    )
    ap.add_argument(
        "--control-arm-runs-dir",
        default=str(RUNS_DIR),
        help="Directory holding Candidate Universe / Play Card grades (default legacy RUNS dir)",
    )
    ap.add_argument("--doubles-inventory-md", help="Optional doubles inventory Markdown path")
    ap.add_argument("--doubles-inventory-csv", help="Optional doubles inventory CSV path")
    ap.add_argument("--force", action="store_true", help="Overwrite output if it already exists")
    args = ap.parse_args()

    results_date = parse_iso_date(args.date).isoformat()
    analysis_arena_dir = Path(args.analysis_arena_dir)
    predictive_sharepacks_root = resolve_repo_path(args.predictive_sharepacks_root)
    truth_sharepacks_root = resolve_repo_path(args.truth_sharepacks_root)
    out_path = Path(args.out) if args.out else (RUNS2_DIR / f"{results_date}__BRAIN2_MASTER_VALIDATION.md")
    default_json_name = (
        out_path.name.replace("__BRAIN2_MASTER_VALIDATION.md", "__BRAIN2_TRACKER_LEDGER.json")
        if "__BRAIN2_MASTER_VALIDATION.md" in out_path.name
        else f"{out_path.stem}__TRACKER_LEDGER.json"
    )
    out_json_path = (
        Path(args.out_json)
        if args.out_json
        else out_path.with_name(default_json_name)
    )
    control_arm_runs_dir = resolve_repo_path(args.control_arm_runs_dir)
    doubles_inventory_md = resolve_repo_path(args.doubles_inventory_md) if args.doubles_inventory_md else None
    doubles_inventory_csv = resolve_repo_path(args.doubles_inventory_csv) if args.doubles_inventory_csv else None

    if out_path.exists() and not args.force:
        raise SystemExit(f"Output already exists: {out_path}. Use --force to overwrite.")

    artifacts = _analysis_artifacts(analysis_arena_dir, results_date=results_date, board_name=args.board_name)
    predictive_control_center_dir = predictive_sharepacks_root / results_date / "control_center"
    truth_control_center_dir = truth_sharepacks_root / results_date / "control_center"
    meta_path = predictive_control_center_dir / "meta.json"
    history_date = (parse_iso_date(results_date) - timedelta(days=1)).isoformat()
    meta: dict[str, Any] = {}
    if meta_path.exists():
        loaded_meta = read_json(meta_path)
        if isinstance(loaded_meta, dict):
            meta = loaded_meta
            history_date = str(meta.get("history_date") or history_date)

    scoreboard = read_json(artifacts.scoreboard_json) if artifacts.scoreboard_json.exists() else {}
    bundle = read_json(artifacts.bundle_json) if artifacts.bundle_json.exists() else {}
    shadow = read_json(artifacts.shadow_json) if artifacts.shadow_json.exists() else {}

    scoreboard_rows = scoreboard.get("scoreboard_rows") if isinstance(scoreboard, dict) else []
    scoreboard_rows = scoreboard_rows if isinstance(scoreboard_rows, list) else []
    board_verdict = scoreboard.get("board_verdict") if isinstance(scoreboard, dict) else {}
    if not isinstance(board_verdict, dict):
        board_verdict = {}
    duplicate_pairs = scoreboard.get("duplicate_pairs") if isinstance(scoreboard, dict) else []
    duplicate_pairs = duplicate_pairs if isinstance(duplicate_pairs, list) else []
    shadow_verdict = shadow.get("shadow_verdict") if isinstance(shadow, dict) else {}
    if not isinstance(shadow_verdict, dict):
        shadow_verdict = {}
    state_decisions = shadow.get("state_decisions") if isinstance(shadow, dict) else []
    state_decisions = state_decisions if isinstance(state_decisions, list) else []

    predictive_rows_by_source = {
        source_name: load_csv_rows(predictive_control_center_dir / file_name)
        for source_name, file_name in PREDICTIVE_TRACKER_FILES.items()
    }
    truth_rows_by_source = {
        source_name: load_csv_rows(truth_control_center_dir / file_name)
        for source_name, file_name in TRUTH_EVALUATION_FILES.items()
    }
    tracker_source_registry = build_control_center_source_registry(
        results_date=results_date,
        predictive_control_center_dir=predictive_control_center_dir,
        truth_control_center_dir=truth_control_center_dir,
        predictive_rows_by_source=predictive_rows_by_source,
        truth_rows_by_source=truth_rows_by_source,
        predictive_meta=meta,
    )
    source_integrity = tracker_source_registry["integrity"]
    if source_integrity["hard_failure_codes"]:
        raise SystemExit(
            "Predictive tracker source failed result-leakage safeguards: "
            + ", ".join(source_integrity["hard_failure_codes"])
            + "; findings="
            + json.dumps(source_integrity["result_leakage_findings"][:5], sort_keys=True)
        )
    if args.strict_predictive_sources and source_integrity["missing_predictive_sources"]:
        raise SystemExit(
            "Missing required predictive tracker sources: "
            + ", ".join(source_integrity["missing_predictive_sources"])
        )
    for warning in source_integrity["warnings"]:
        print(f"WARNING: {warning}", file=sys.stderr)

    profit_alert_rows = predictive_rows_by_source["profit_alerts"]
    compound_rows = predictive_rows_by_source["compound_events"]
    blackapple_rows = predictive_rows_by_source["blackapple"]
    due_rows = predictive_rows_by_source["due_doubles"]
    tracker_rows = predictive_rows_by_source["repeat_watch"]
    truth_profit_alert_rows = truth_rows_by_source["profit_alerts_graded"]
    truth_compound_rows = truth_rows_by_source["compound_events_graded"]
    truth_blackapple_rows = truth_rows_by_source["blackapple_graded"]
    truth_due_rows = truth_rows_by_source["due_doubles_graded"]
    truth_tracker_rows = truth_rows_by_source["repeat_watch_graded"]
    translation_learning = _load_translation_learning(artifacts.sandbox_json)

    report = build_brain2_master_validation_report(
        results_date=results_date,
        history_date=history_date,
        artifacts=artifacts,
        template_path=TEMPLATE_PATH,
        board_scope_states=[str(row.get("state_key") or "") for row in scoreboard_rows],
        scoreboard_rows=scoreboard_rows,
        board_verdict=board_verdict,
        duplicate_pairs=duplicate_pairs,
        shadow_verdict=shadow_verdict,
        state_decisions=state_decisions,
        profit_alert_rows=profit_alert_rows,
        compound_rows=compound_rows,
        blackapple_rows=blackapple_rows,
        due_rows=due_rows,
        tracker_rows=tracker_rows,
        truth_profit_alert_rows=truth_profit_alert_rows,
        truth_compound_rows=truth_compound_rows,
        truth_blackapple_rows=truth_blackapple_rows,
        truth_due_rows=truth_due_rows,
        truth_tracker_rows=truth_tracker_rows,
        translation_learning=translation_learning,
        predictive_control_center_dir=predictive_control_center_dir,
        truth_control_center_dir=truth_control_center_dir,
        tracker_source_registry=tracker_source_registry,
        control_arm_runs_dir=control_arm_runs_dir,
        doubles_inventory_md=doubles_inventory_md,
        doubles_inventory_csv=doubles_inventory_csv,
    )
    tracker_ledger = build_brain2_tracker_ledger(
        results_date=results_date,
        history_date=history_date,
        artifacts=artifacts,
        board_scope_states=[str(row.get("state_key") or "") for row in scoreboard_rows],
        scoreboard_rows=scoreboard_rows,
        board_verdict=board_verdict,
        shadow_verdict=shadow_verdict,
        profit_alert_rows=profit_alert_rows,
        compound_rows=compound_rows,
        blackapple_rows=blackapple_rows,
        due_rows=due_rows,
        tracker_rows=tracker_rows,
        truth_profit_alert_rows=truth_profit_alert_rows,
        truth_compound_rows=truth_compound_rows,
        truth_blackapple_rows=truth_blackapple_rows,
        truth_due_rows=truth_due_rows,
        truth_tracker_rows=truth_tracker_rows,
        translation_learning=translation_learning,
        predictive_control_center_dir=predictive_control_center_dir,
        truth_control_center_dir=truth_control_center_dir,
        tracker_source_registry=tracker_source_registry,
        doubles_inventory_md=doubles_inventory_md,
        doubles_inventory_csv=doubles_inventory_csv,
    )

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(report, encoding="utf-8")
    out_json_path.write_text(json.dumps(tracker_ledger, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Wrote: {out_path}")
    print(f"Wrote: {out_json_path}")


if __name__ == "__main__":
    main()
