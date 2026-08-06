#!/usr/bin/env python3
"""Build an aggregated analysis arena from frozen sharepack artifacts.

The aggregated arena is the first per-state runtime object that preserves the
string-tool and context-tool evidence in one budget-blind snapshot. It is
designed to be reviewed against winners later without forcing that evidence
through Candidate Universe or play-card geometry first.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from modules.vtrac_reference import get_index_set, get_vtrac_index
from modules.vtrac_straight_map import (
    ordered_vcode_for_combo,
    vstraight_lane_for_combo,
    vstraight_lanes_for_index,
)
from scripts.tools.aux_control_center_arena import build_aux_control_center_arena_payload
from scripts.tools.dr_arena import build_dr_arena_payload
from scripts.tools.stable_arena import build_stable_arena_payload

try:
    from scripts.tools.create_candidate_universe import _extract_aux_badge_pressure_signals
except Exception:  # pragma: no cover - optional fallback only
    _extract_aux_badge_pressure_signals = None  # type: ignore[assignment]


SECTION_ORDER: Tuple[str, ...] = ("Combined", "Midday", "Evening")


def _read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8", errors="replace"))


def _load_csv_rows(path: Path) -> List[Dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as fh:
        return [dict(row) for row in csv.DictReader(fh)]


def _safe_rel(path: Path, repo_root: Path = REPO_ROOT) -> str:
    try:
        return str(path.resolve().relative_to(repo_root.resolve()))
    except Exception:
        return str(path)


def _section_sort_key(value: str) -> Tuple[int, str]:
    title = str(value or "").strip().title()
    try:
        return (SECTION_ORDER.index(title), title)
    except ValueError:
        return (len(SECTION_ORDER), title)


def _to_int(value: object, default: int = 0) -> int:
    try:
        text = str(value or "").strip()
        if not text:
            return int(default)
        return int(float(text))
    except Exception:
        return int(default)


def _to_float(value: object, default: float = 0.0) -> float:
    try:
        text = str(value or "").strip()
        if not text:
            return float(default)
        return float(text)
    except Exception:
        return float(default)


def _normalize_pick3_literal(value: object) -> str:
    digits = "".join(ch for ch in str(value or "") if ch.isdigit())
    if not digits:
        return ""
    if len(digits) <= 3:
        digits = digits.zfill(3)
    return digits if len(digits) == 3 else ""


def _canon(value: object) -> str:
    digits = _normalize_pick3_literal(value)
    return "".join(sorted(digits)) if digits else ""


def _append_unique(values: List[str], value: object, *, limit: int = 20) -> None:
    text = str(value or "").strip()
    if not text or text in values or len(values) >= int(limit):
        return
    values.append(text)


def _sorted_counter(counter: Counter[str]) -> Dict[str, int]:
    return {key: int(counter[key]) for key in sorted(counter, key=lambda k: (-counter[k], k))}


def _is_double(canonical: str) -> bool:
    digits = _normalize_pick3_literal(canonical)
    return bool(digits) and len(set(digits)) < len(digits)


def _hash_inputs(paths: Sequence[Path]) -> str:
    digest = hashlib.sha256()
    for path in sorted({str(p.resolve()) for p in paths}):
        digest.update(path.encode("utf-8"))
        digest.update(b"\0")
        file_path = Path(path)
        if file_path.exists():
            digest.update(file_path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def _now_utc_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _flatten_path_values(value: Any) -> List[str]:
    out: List[str] = []
    if isinstance(value, str):
        if value.strip():
            out.append(value.strip())
    elif isinstance(value, list):
        for item in value:
            out.extend(_flatten_path_values(item))
    elif isinstance(value, dict):
        for item in value.values():
            out.extend(_flatten_path_values(item))
    return out


def _collect_existing_paths(repo_root: Path, payload: Dict[str, Any], *keys: str) -> List[Path]:
    out: List[Path] = []
    for key in keys:
        raw = payload.get(key)
        for rel in _flatten_path_values(raw):
            path = (repo_root / rel).resolve()
            if path.exists():
                out.append(path)
    seen: set[str] = set()
    unique: List[Path] = []
    for path in out:
        key = str(path)
        if key in seen:
            continue
        seen.add(key)
        unique.append(path)
    return unique


def _find_prebuilt_analysis_json(state_dir: Path, stem: str) -> Optional[Path]:
    analysis_dir = state_dir / "analysis"
    if not analysis_dir.exists():
        return None
    candidates = sorted(analysis_dir.glob(f"{stem}__*.json"))
    return candidates[-1] if candidates else None


def _load_day_meta(day_dir: Path) -> Dict[str, Any]:
    meta_path = day_dir / "control_center" / "meta.json"
    if meta_path.exists():
        raw = _read_json(meta_path)
        if isinstance(raw, dict):
            return raw
    return {}


def _infer_history_date(day_dir: Path, explicit: Optional[str]) -> Optional[str]:
    if explicit:
        return explicit
    meta = _load_day_meta(day_dir)
    text = str(meta.get("history_date") or "").strip()
    return text or None


def _contains_winners_for_state(day_meta: Dict[str, Any], state_key: str, sharepacks_root: Path) -> bool:
    if "_predictive" in sharepacks_root.parts:
        return False
    for row in day_meta.get("states", []) if isinstance(day_meta.get("states"), list) else []:
        if str(row.get("state_key") or "").strip() != state_key:
            continue
        winners = row.get("winners")
        return bool(winners)
    return False


def _resolve_states(day_dir: Path, state_args: Sequence[str], day_meta: Dict[str, Any]) -> List[str]:
    if state_args:
        return [str(s).strip() for s in state_args if str(s).strip()]
    meta_states = [
        str(row.get("state_key") or "").strip()
        for row in (day_meta.get("states") or [])
        if isinstance(row, dict) and str(row.get("state_key") or "").strip()
    ]
    if meta_states:
        return meta_states
    return sorted(path.name for path in day_dir.iterdir() if path.is_dir() and path.name != "control_center")


def _load_or_build_stable_payload(
    *,
    day_dir: Path,
    state_dir: Path,
    state_key: str,
    results_date: str,
    history_date: Optional[str],
    profile: str,
    experiment_tag: str,
    sharepacks_root: Path,
    contains_winners_artifacts: bool,
    repo_root: Path,
) -> Tuple[Dict[str, Any], List[Path], Dict[str, Any]]:
    payload = build_stable_arena_payload(
        state_dir=state_dir,
        state_key=state_key,
        results_date=results_date,
        history_date=str(history_date or ""),
        profile=profile,
        experiment_tag=experiment_tag,
        sharepacks_root=sharepacks_root,
        contains_winners_artifacts=contains_winners_artifacts,
        repo_root=repo_root,
    )
    if payload is not None:
        paths = _collect_existing_paths(repo_root, payload, "evidence_paths")
        normalized = {
            "available": True,
            "source_mode": "rebuilt_from_raw",
            "source_path": None,
            "schema": payload.get("schema"),
            "metrics_summary": payload.get("metrics_summary"),
            "r_consensus_context": payload.get("r_consensus_context"),
            "sections": payload.get("sections") or {},
        }
        status = {"available": True, "source_mode": "rebuilt_from_raw", "source_path": None}
        return normalized, paths, status

    prebuilt = _find_prebuilt_analysis_json(state_dir, "stable_arena")
    if prebuilt is not None:
        raw = _read_json(prebuilt)
        if isinstance(raw, dict):
            paths = [prebuilt, *_collect_existing_paths(repo_root, raw, "evidence_paths")]
            normalized = {
                "available": True,
                "source_mode": "loaded_prebuilt",
                "source_path": _safe_rel(prebuilt, repo_root),
                "schema": raw.get("schema"),
                "metrics_summary": raw.get("metrics_summary"),
                "r_consensus_context": raw.get("r_consensus_context"),
                "sections": raw.get("sections") or {},
            }
            status = {"available": True, "source_mode": "loaded_prebuilt", "source_path": _safe_rel(prebuilt, repo_root)}
            return normalized, paths, status

    return {"available": False, "sections": {}}, [], {"available": False, "source_mode": "missing", "source_path": None}


def _load_or_build_dr_payload(
    *,
    day_dir: Path,
    state_dir: Path,
    state_key: str,
    results_date: str,
    history_date: Optional[str],
    profile: str,
    experiment_tag: str,
    sharepacks_root: Path,
    contains_winners_artifacts: bool,
    repo_root: Path,
) -> Tuple[Dict[str, Any], List[Path], Dict[str, Any]]:
    payload = build_dr_arena_payload(
        state_dir=state_dir,
        state_key=state_key,
        results_date=results_date,
        history_date=history_date,
        profile=profile,
        experiment_tag=experiment_tag,
        sharepacks_root=sharepacks_root,
        contains_winners_artifacts=contains_winners_artifacts,
        repo_root=repo_root,
    )
    if payload is not None:
        paths = _collect_existing_paths(repo_root, payload.get("paths") or {}, "per_item_csv", "top_candidates_csv", "meta_json", "training_logs_json", "training_steps_csv")
        normalized = {
            "available": True,
            "source_mode": "rebuilt_from_raw",
            "source_path": None,
            "schema_revision": payload.get("schema_revision"),
            "meta": payload.get("meta") or {},
            "sections": payload.get("sections") or {},
        }
        status = {"available": True, "source_mode": "rebuilt_from_raw", "source_path": None}
        return normalized, paths, status

    prebuilt = _find_prebuilt_analysis_json(state_dir, "dr_arena")
    if prebuilt is not None:
        raw = _read_json(prebuilt)
        if isinstance(raw, dict):
            paths = [prebuilt, *_collect_existing_paths(repo_root, raw.get("paths") or {}, "per_item_csv", "top_candidates_csv", "meta_json", "training_logs_json", "training_steps_csv")]
            normalized = {
                "available": True,
                "source_mode": "loaded_prebuilt",
                "source_path": _safe_rel(prebuilt, repo_root),
                "schema_revision": raw.get("schema_revision"),
                "meta": raw.get("meta") or {},
                "sections": raw.get("sections") or {},
            }
            status = {"available": True, "source_mode": "loaded_prebuilt", "source_path": _safe_rel(prebuilt, repo_root)}
            return normalized, paths, status

    return {"available": False, "sections": {}}, [], {"available": False, "source_mode": "missing", "source_path": None}


def _load_badge_pressure(
    *,
    state_dir: Path,
    state_key: str,
    repo_root: Path,
    top_k: int,
) -> Tuple[Optional[Dict[str, Any]], List[Path]]:
    analysis_dir = state_dir / "analysis"
    signals_candidates = sorted(analysis_dir.glob("signals_bundle__*.json"))
    if signals_candidates:
        raw = _read_json(signals_candidates[-1])
        tools = raw.get("tools") if isinstance(raw, dict) else None
        badge = (tools or {}).get("aux_badge_pressure") if isinstance(tools, dict) else None
        if isinstance(badge, dict):
            return badge, _collect_existing_paths(repo_root, badge, "evidence_paths")

    if _extract_aux_badge_pressure_signals is not None:
        try:
            badge, inputs = _extract_aux_badge_pressure_signals(state_dir=state_dir, state_key=state_key, top_k=top_k)
            return badge, list(inputs)
        except Exception:
            return None, []
    return None, []


def _aux_payload_has_substance(payload: Dict[str, Any]) -> bool:
    arena_objects = payload.get("arena_objects") if isinstance(payload.get("arena_objects"), dict) else {}
    substantive_keys = [
        "aux_positional_pressure",
        "aux_vtrac_pressure",
        "aux_badge_pressure",
        "aux_pair_band_context",
        "aux_due_doubles_family_pressure",
        "aux_repeat_watch_context",
        "aux_sums_context",
        "aux_blackapple_context",
        "cc_profit_alert_context",
        "cc_compound_event_context",
    ]
    for key in substantive_keys:
        block = arena_objects.get(key)
        if not isinstance(block, dict):
            continue
        if bool(block.get("available")):
            return True
    return False


def _load_or_build_aux_payload(
    *,
    day_dir: Path,
    state_dir: Path,
    state_key: str,
    results_date: str,
    history_date: Optional[str],
    profile: str,
    experiment_tag: str,
    sharepacks_root: Path,
    contains_winners_artifacts: bool,
    repo_root: Path,
    top_items: int,
) -> Tuple[Dict[str, Any], List[Path], Dict[str, Any]]:
    badge_pressure, badge_paths = _load_badge_pressure(
        state_dir=state_dir,
        state_key=state_key,
        repo_root=repo_root,
        top_k=max(5, int(top_items)),
    )
    payload = build_aux_control_center_arena_payload(
        day_dir=day_dir,
        state_dir=state_dir,
        state_key=state_key,
        results_date=results_date,
        history_date=str(history_date or ""),
        profile=profile,
        experiment_tag=experiment_tag,
        sharepacks_root=sharepacks_root,
        contains_winners_artifacts=contains_winners_artifacts,
        repo_root=repo_root,
        badge_pressure=badge_pressure,
        top_items=top_items,
    )
    if _aux_payload_has_substance(payload):
        paths = _collect_existing_paths(repo_root, payload, "inputs") + badge_paths
        normalized = {
            "available": True,
            "source_mode": "rebuilt_from_raw",
            "source_path": None,
            "schema_version": payload.get("schema_version"),
            "arena_objects": payload.get("arena_objects") or {},
            "linked_truth_layers": payload.get("linked_truth_layers") or {},
        }
        status = {"available": True, "source_mode": "rebuilt_from_raw", "source_path": None}
        return normalized, paths, status

    prebuilt = _find_prebuilt_analysis_json(state_dir, "aux_control_center_arena")
    if prebuilt is not None:
        raw = _read_json(prebuilt)
        if isinstance(raw, dict):
            paths = [prebuilt, *_collect_existing_paths(repo_root, raw, "inputs")]
            normalized = {
                "available": bool(raw.get("available")),
                "source_mode": "loaded_prebuilt",
                "source_path": _safe_rel(prebuilt, repo_root),
                "schema_version": raw.get("schema_version"),
                "arena_objects": raw.get("arena_objects") or {},
                "linked_truth_layers": raw.get("linked_truth_layers") or {},
            }
            status = {"available": bool(raw.get("available")), "source_mode": "loaded_prebuilt", "source_path": _safe_rel(prebuilt, repo_root)}
            return normalized, paths, status

    return {"available": False, "arena_objects": {}}, badge_paths, {"available": False, "source_mode": "missing", "source_path": None}


def _build_vtrac_arena_objects(enhanced: Dict[str, Any], *, top_lanes: int = 12, top_witnesses: int = 12) -> Dict[str, Any]:
    """Build predictive-safe VTRAC lane/corridor review objects."""
    base = {
        "schema": "aat9.vtrac_analyzer.arena_objects.v1",
        "source_scope": "predictive_safe_vtrac_enhanced_only",
        "semantic_guardrails": {
            "vcode_labels_are_metadata_only": True,
            "playable_literals_only": True,
            "boxed_index_can_contain_multiple_ordered_lanes": True,
            "no_winner_artifacts_used": True,
            "no_scoring_weights_changed": True,
            "source_rows_are_not_independent_votes": True,
            "review_order": "DESCRIPTIVE_UNCALIBRATED_NATIVE_SCORE_SUM",
            "score_total_semantics": (
                "Heterogeneous source-native values plus a bounded rank hint; "
                "review ordering only, never a calibrated cross-tool score."
            ),
        },
    }
    if not isinstance(enhanced, dict) or not enhanced:
        return {**base, "available": False, "ordered_lane_corridors": [], "boxed_index_corridors": []}

    lane_map: Dict[str, Dict[str, Any]] = {}
    index_map: Dict[str, Dict[str, Any]] = {}

    def lane_record(vcode: str, straight: str) -> Dict[str, Any]:
        idx = get_vtrac_index(straight)
        record = lane_map.setdefault(
            vcode,
            {
                "ordered_vcode": vcode,
                "boxed_vtrac_index": idx,
                "ordered_lane_8": vstraight_lane_for_combo(straight),
                "score_total": 0.0,
                "witness_scores": defaultdict(float),
                "witness_sources": defaultdict(list),
                "witness_canonicals": {},
                "source_indices_seen": set(),
                "source_types": Counter(),
            },
        )
        if record.get("boxed_vtrac_index") is None:
            record["boxed_vtrac_index"] = idx
        return record

    def index_record(idx: int) -> Dict[str, Any]:
        key = str(idx)
        return index_map.setdefault(
            key,
            {
                "boxed_vtrac_index": idx,
                "score_total": 0.0,
                "ordered_vcodes_present": set(),
                "witness_scores": defaultdict(float),
                "witness_sources": defaultdict(list),
                "witness_canonicals": {},
                "source_indices_seen": set(),
                "source_types": Counter(),
            },
        )

    def register(straight_value: object, *, score: float, source: str, source_index: object = None) -> None:
        straight = _normalize_pick3_literal(straight_value)
        if not straight:
            return
        vcode = ordered_vcode_for_combo(straight)
        if not vcode:
            return
        idx = get_vtrac_index(straight)
        canonical = _canon(straight)
        lane = lane_record(vcode, straight)
        lane["score_total"] += float(score)
        lane["witness_scores"][straight] += float(score)
        _append_unique(lane["witness_sources"][straight], source, limit=12)
        lane["witness_canonicals"][straight] = canonical
        lane["source_types"][source.split(":", 1)[0]] += 1
        if source_index is not None and str(source_index).strip():
            lane["source_indices_seen"].add(str(source_index).strip())

        if idx is None:
            return
        corridor = index_record(int(idx))
        corridor["score_total"] += float(score)
        corridor["ordered_vcodes_present"].add(vcode)
        corridor["witness_scores"][straight] += float(score)
        _append_unique(corridor["witness_sources"][straight], source, limit=12)
        corridor["witness_canonicals"][straight] = canonical
        corridor["source_types"][source.split(":", 1)[0]] += 1
        if source_index is not None and str(source_index).strip():
            corridor["source_indices_seen"].add(str(source_index).strip())

    for rank, entry in enumerate(enhanced.get("straights_ranked", []) if isinstance(enhanced.get("straights_ranked"), list) else [], start=1):
        if not isinstance(entry, dict):
            continue
        score = _to_float(entry.get("score"))
        register(
            entry.get("straight"),
            score=score + max(0.0, 1.0 - (rank * 0.01)),
            source="straights_ranked",
            source_index=entry.get("index"),
        )

    for entry in enhanced.get("indices_ranked", []) if isinstance(enhanced.get("indices_ranked"), list) else []:
        if not isinstance(entry, dict):
            continue
        evidence = entry.get("evidence") if isinstance(entry.get("evidence"), dict) else {}
        raw = evidence.get("raw") if isinstance(evidence.get("raw"), dict) else {}
        order_counts = raw.get("order_counts") if isinstance(raw.get("order_counts"), dict) else {}
        for straight, value in order_counts.items():
            register(straight, score=_to_float(value), source="indices_ranked.order_counts", source_index=entry.get("index"))

    section_summaries = enhanced.get("section_summaries") if isinstance(enhanced.get("section_summaries"), dict) else {}
    for section, block in section_summaries.items():
        if not isinstance(block, dict):
            continue
        for key in ("top_straights", "top_straight_witnesses", "straights_ranked"):
            rows = block.get(key)
            if not isinstance(rows, list):
                continue
            for row in rows[:25]:
                if isinstance(row, dict):
                    straight = row.get("straight") or row.get("pattern") or row.get("value") or row.get("candidate")
                    score = _to_float(row.get("score") or row.get("count") or row.get("weight"), default=1.0)
                else:
                    straight = row
                    score = 1.0
                register(straight, score=score, source=f"section_summaries:{section}:{key}")

    def witness_rows(record: Dict[str, Any]) -> List[Dict[str, Any]]:
        scores = record.get("witness_scores") or {}
        sources = record.get("witness_sources") or {}
        canonicals = record.get("witness_canonicals") or {}
        rows = []
        for straight, score in sorted(scores.items(), key=lambda item: (-float(item[1]), item[0]))[: int(top_witnesses)]:
            rows.append(
                {
                    "straight": straight,
                    "canonical": canonicals.get(straight) or _canon(straight),
                    "score": round(float(score), 6),
                    "sources": list(sources.get(straight) or []),
                }
            )
        return rows

    ordered_rows: List[Dict[str, Any]] = []
    for record in sorted(lane_map.values(), key=lambda item: (-float(item.get("score_total") or 0.0), str(item.get("ordered_vcode") or "")))[: int(top_lanes)]:
        ordered_rows.append(
            {
                "ordered_vcode": record.get("ordered_vcode"),
                "boxed_vtrac_index": record.get("boxed_vtrac_index"),
                "ordered_lane_8": record.get("ordered_lane_8") or [],
                "score_total": round(float(record.get("score_total") or 0.0), 6),
                "witness_count": len(record.get("witness_scores") or {}),
                "source_indices_seen": sorted(record.get("source_indices_seen") or []),
                "source_index_mismatch": any(
                    str(value) != str(record.get("boxed_vtrac_index"))
                    for value in (record.get("source_indices_seen") or [])
                ),
                "top_witness_straights": witness_rows(record),
                "source_types": _sorted_counter(record.get("source_types") or Counter()),
            }
        )

    boxed_rows: List[Dict[str, Any]] = []
    for record in sorted(index_map.values(), key=lambda item: (-float(item.get("score_total") or 0.0), int(item.get("boxed_vtrac_index") or 0)))[: int(top_lanes)]:
        idx = int(record.get("boxed_vtrac_index") or 0)
        ordered_vcodes_present = sorted(record.get("ordered_vcodes_present") or [])
        lane_scores = [
            {"ordered_vcode": row.get("ordered_vcode"), "score_total": row.get("score_total")}
            for row in ordered_rows
            if row.get("ordered_vcode") in ordered_vcodes_present
        ]
        boxed_rows.append(
            {
                "boxed_vtrac_index": idx,
                "boxed_corridor_size": len(get_index_set(idx)),
                "ordered_vcodes_available_for_index": sorted(vstraight_lanes_for_index(idx)),
                "ordered_vcodes_present": ordered_vcodes_present,
                "ordered_lane_count_present": len(ordered_vcodes_present),
                "score_total": round(float(record.get("score_total") or 0.0), 6),
                "source_indices_seen": sorted(record.get("source_indices_seen") or []),
                "source_index_mismatch": any(
                    str(value) != str(record.get("boxed_vtrac_index"))
                    for value in (record.get("source_indices_seen") or [])
                ),
                "top_ordered_lanes": sorted(lane_scores, key=lambda item: (-float(item.get("score_total") or 0.0), str(item.get("ordered_vcode") or "")))[: int(top_witnesses)],
                "top_witness_straights": witness_rows(record),
                "source_types": _sorted_counter(record.get("source_types") or Counter()),
            }
        )

    return {**base, "available": bool(ordered_rows or boxed_rows), "ordered_lane_corridors": ordered_rows, "boxed_index_corridors": boxed_rows}


def _build_vtrac_tool_payload(
    *,
    day_dir: Path,
    state_dir: Path,
    state_key: str,
    repo_root: Path,
    top_indices: int,
    top_straights: int,
    top_sections: int,
) -> Tuple[Dict[str, Any], List[Path], Dict[str, Any]]:
    vtrac_dir = state_dir / "vtrac" / state_key
    candidates = sorted(vtrac_dir.glob(f"{state_key}_vtrac_enhanced_*.json")) if vtrac_dir.exists() else []
    enhanced_path = candidates[-1] if candidates else None
    enhanced = _read_json(enhanced_path) if enhanced_path is not None else {}
    if not isinstance(enhanced, dict):
        enhanced = {}

    compact_path = day_dir / "vtrac_compact_report.json"
    compact_state: Optional[Dict[str, Any]] = None
    if compact_path.exists():
        compact = _read_json(compact_path)
        if isinstance(compact, dict):
            for row in compact.get("states", []) if isinstance(compact.get("states"), list) else []:
                if not isinstance(row, dict):
                    continue
                if str(row.get("state") or "").strip() == state_key:
                    compact_state = row
                    break

    indices_ranked: List[Dict[str, Any]] = []
    for entry in enhanced.get("indices_ranked", []) if isinstance(enhanced.get("indices_ranked"), list) else []:
        if len(indices_ranked) >= int(top_indices):
            break
        if not isinstance(entry, dict):
            continue
        try:
            idx = int(entry.get("index"))
        except Exception:
            continue
        indices_ranked.append(
            {
                "index": idx,
                "score": round(_to_float(entry.get("score")), 6),
                "reasons": [str(x) for x in (entry.get("reasons") or []) if str(x)],
            }
        )

    straights_ranked: List[Dict[str, Any]] = []
    for entry in enhanced.get("straights_ranked", []) if isinstance(enhanced.get("straights_ranked"), list) else []:
        if len(straights_ranked) >= int(top_straights):
            break
        if not isinstance(entry, dict):
            continue
        straight = _normalize_pick3_literal(entry.get("straight"))
        if not straight:
            continue
        straights_ranked.append(
            {
                "straight": straight,
                "canonical": _canon(straight),
                "index": _to_int(entry.get("index"), default=-1) if str(entry.get("index") or "").strip() else None,
                "score": round(_to_float(entry.get("score")), 6),
                "reasons": [str(x) for x in (entry.get("reasons") or []) if str(x)],
            }
        )

    compact_sections: List[Dict[str, Any]] = []
    if isinstance(compact_state, dict):
        for entry in compact_state.get("sections", []) if isinstance(compact_state.get("sections"), list) else []:
            if len(compact_sections) >= int(top_sections):
                break
            if not isinstance(entry, dict):
                continue
            compact_sections.append(
                {
                    "section": str(entry.get("section") or ""),
                    "index_hint": _to_int(entry.get("index_hint"), default=-1) if str(entry.get("index_hint") or "").strip() else None,
                    "confidence_score": round(_to_float(entry.get("confidence_score")), 6),
                    "tier": str(entry.get("tier") or ""),
                    "hot_count": _to_int(entry.get("hot_count")),
                    "superhot_count": _to_int(entry.get("superhot_count")),
                    "stable_cols_count": _to_int(entry.get("stable_cols_count")),
                    "mask_drop": bool(entry.get("mask_drop")),
                    "mirror_supported": bool(entry.get("mirror_supported")),
                    "double_hits": _to_int(entry.get("double_hits")),
                    "top_tokens": [str(x) for x in (entry.get("top_tokens") or []) if str(x)],
                    "recommended_tokens": [str(x) for x in (entry.get("recommended_tokens") or []) if str(x)],
                    "why": str(entry.get("why") or ""),
                }
            )

    top_indices_by_state = []
    if isinstance(compact_state, dict):
        top_indices_by_state = [
            {
                "index": _to_int(entry.get("index"), default=-1) if str(entry.get("index") or "").strip() else None,
                "score": round(_to_float(entry.get("score")), 6),
                "why": str(entry.get("why") or ""),
            }
            for entry in (compact_state.get("top_indices_by_state") or [])[: int(top_indices)]
            if isinstance(entry, dict)
        ]

    arena_objects = _build_vtrac_arena_objects(
        enhanced,
        top_lanes=max(12, int(top_indices)),
        top_witnesses=max(12, int(top_straights)),
    )

    paths = [path for path in (enhanced_path, compact_path if compact_state is not None else None) if path is not None]
    payload = {
        "available": bool(enhanced or compact_state),
        "source_mode": "raw" if (enhanced or compact_state) else "missing",
        "source_paths": [_safe_rel(path, repo_root) for path in paths],
        "enhanced": {
            "state": enhanced.get("state"),
            "timestamp": enhanced.get("timestamp"),
            "indices_ranked": indices_ranked,
            "straights_ranked": straights_ranked,
            "section_summaries": enhanced.get("section_summaries") if isinstance(enhanced.get("section_summaries"), dict) else {},
            "telemetry": enhanced.get("telemetry") if isinstance(enhanced.get("telemetry"), dict) else {},
        },
        "arena_objects": arena_objects,
        "compact_report_day": {
            "available": compact_state is not None,
            "top_indices_by_state": top_indices_by_state,
            "sections": sorted(compact_sections, key=lambda item: _section_sort_key(str(item.get("section") or ""))),
        },
    }
    status = {
        "available": bool(enhanced or compact_state),
        "source_mode": "raw" if (enhanced or compact_state) else "missing",
        "source_path": _safe_rel(enhanced_path, repo_root) if enhanced_path is not None else (_safe_rel(compact_path, repo_root) if compact_state is not None else None),
    }
    return payload, paths, status


def _split_tags(value: object) -> List[str]:
    return [part.strip() for part in str(value or "").split("|") if part.strip()] if "|" in str(value or "") else [part.strip() for part in str(value or "").split(",") if part.strip()]


def _build_hot_zones_tool_payload(
    *,
    day_dir: Path,
    state_dir: Path,
    state_key: str,
    results_date: str,
    repo_root: Path,
    top_lanes: int,
    top_per_lane: int,
) -> Tuple[Dict[str, Any], List[Path], Dict[str, Any]]:
    hz_dir = state_dir / "hot_zones" / state_key
    meta_path = hz_dir / f"{state_key}_hot_zones_meta.json"
    top_lanes_path = hz_dir / f"{state_key}_hot_zones_top_lanes.csv"
    per_lane_path = hz_dir / f"{state_key}_hot_zones_per_lane.csv"
    winner_map_path = hz_dir / f"{results_date}_hot_zones_winner_map.json"

    meta = _read_json(meta_path) if meta_path.exists() else {}
    if not isinstance(meta, dict):
        meta = {}

    lane_rows = _load_csv_rows(top_lanes_path)
    lane_payloads: List[Dict[str, Any]] = []
    for row in lane_rows[: int(top_lanes)]:
        triad = _normalize_pick3_literal(row.get("triad") or row.get("Triad"))
        if not triad:
            continue
        lane_payloads.append(
            {
                "triad": triad,
                "canonical": _canon(triad),
                "vtrac_index": get_vtrac_index(triad),
                "vt_triad": str(row.get("vt_triad") or row.get("VT_Triad") or "").strip() or None,
                "support_count": _to_int(row.get("support_count")),
                "hot_hits": _to_int(row.get("hot_hits")),
                "superhot_hits": _to_int(row.get("superhot_hits")),
                "vertical_hits": _to_int(row.get("vertical_hits")),
                "set1_hits": _to_int(row.get("set1_hits")),
                "col1_hits": _to_int(row.get("col1_hits")),
                "precol1_hits": _to_int(row.get("precol1_hits")),
                "vt_straight_hits": _to_int(row.get("vt_straight_hits")),
                "vt_only_lane_hits": _to_int(row.get("vt_only_lane_hits")),
                "guard_hits": _to_int(row.get("guard_hits")),
                "literal_hits": _to_int(row.get("literal_hits")),
                "variant_span": _to_int(row.get("variant_span")),
                "set_span": _to_int(row.get("set_span")),
                "column_span": _to_int(row.get("column_span")),
                "score_mean": round(_to_float(row.get("score_mean")), 6),
                "score_max": round(_to_float(row.get("score_max")), 6),
                "evidence_tags": _split_tags(row.get("evidence_tags")),
            }
        )

    per_lane_rows = _load_csv_rows(per_lane_path)
    per_lane_payloads: List[Dict[str, Any]] = []
    for row in sorted(per_lane_rows, key=lambda item: (-_to_float(item.get("score")), _normalize_pick3_literal(item.get("triad"))))[: int(top_per_lane)]:
        triad = _normalize_pick3_literal(row.get("triad"))
        if not triad:
            continue
        per_lane_payloads.append(
            {
                "section": str(row.get("section") or ""),
                "set_name": str(row.get("set_name") or ""),
                "draw_name": str(row.get("draw_name") or ""),
                "column_index": _to_int(row.get("column_index"), default=-1),
                "triad": triad,
                "canonical": _canon(triad),
                "vtrac_index": get_vtrac_index(triad),
                "vt_triad": str(row.get("vt_triad") or "").strip() or None,
                "vertical_support": _to_int(row.get("vertical_support")),
                "horizontal_span": _to_int(row.get("horizontal_span")),
                "set_span": _to_int(row.get("set_span")),
                "variant_echo": _to_int(row.get("variant_echo")),
                "has_straight": bool(_to_int(row.get("has_straight"))),
                "has_vt_straight": bool(_to_int(row.get("has_vt_straight"))),
                "vt_only_lane": bool(_to_int(row.get("vt_only_lane"))),
                "col1_arrival": bool(_to_int(row.get("col1_arrival"))),
                "precol1_funnel": bool(_to_int(row.get("precol1_funnel"))),
                "is_starred": bool(_to_int(row.get("is_starred"))),
                "star_count": _to_int(row.get("star_count")),
                "is_superhot_slot": bool(_to_int(row.get("is_superhot_slot"))),
                "guard_injected": bool(_to_int(row.get("guard_injected"))),
                "score": round(_to_float(row.get("score")), 6),
                "reasons": _split_tags(row.get("reasons")),
            }
        )

    winner_map_top: List[Dict[str, Any]] = []
    if winner_map_path.exists():
        raw = _read_json(winner_map_path)
        if isinstance(raw, list):
            for row in raw[: int(top_lanes)]:
                if not isinstance(row, dict):
                    continue
                triad = _normalize_pick3_literal(row.get("triad"))
                if not triad:
                    continue
                winner_map_top.append(
                    {
                        "triad": triad,
                        "canonical": _canon(triad),
                        "vtrac_index": get_vtrac_index(triad),
                        "score_mean": round(_to_float(row.get("score_mean")), 6),
                        "support_count": _to_int(row.get("support_count")),
                        "evidence_tags": _split_tags(row.get("evidence_tags")),
                    }
                )

    paths = [path for path in (meta_path, top_lanes_path, per_lane_path, winner_map_path) if path.exists()]
    payload = {
        "available": bool(lane_payloads or per_lane_payloads or winner_map_top),
        "source_mode": "raw" if paths else "missing",
        "source_paths": [_safe_rel(path, repo_root) for path in paths],
        "meta": meta,
        "top_lanes": lane_payloads,
        "per_lane_top": per_lane_payloads,
        "winner_map_top": winner_map_top,
    }
    status = {
        "available": bool(lane_payloads or per_lane_payloads or winner_map_top),
        "source_mode": "raw" if paths else "missing",
        "source_path": _safe_rel(top_lanes_path, repo_root) if top_lanes_path.exists() else None,
    }
    return payload, paths, status


def _source_bucket(source: str) -> str:
    head = str(source or "").split(":", 1)[0]
    if head in {"stable", "dr", "vtrac", "hot"}:
        return "string"
    return "context"


def _register_vote(
    store: Dict[str, Dict[str, Any]],
    *,
    key: str,
    source: str,
    score: float,
    literal: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
) -> None:
    if not key:
        return
    bucket = _source_bucket(source)
    entry = store.setdefault(
        key,
        {
            "value": key,
            "support_count": 0,
            "score_total": 0.0,
            "string_source_count": 0,
            "context_source_count": 0,
            "sources": [],
            "example_literals": [],
            "metadata": [],
        },
    )
    entry["support_count"] += 1
    entry["score_total"] = round(float(entry.get("score_total") or 0.0) + float(score or 0.0), 6)
    if bucket == "string":
        entry["string_source_count"] += 1
    else:
        entry["context_source_count"] += 1
    entry["sources"].append({"source": source, "score": round(float(score or 0.0), 6)})
    if literal:
        normalized = _normalize_pick3_literal(literal) or str(literal)
        if normalized and normalized not in entry["example_literals"]:
            entry["example_literals"].append(normalized)
    if metadata:
        entry["metadata"].append(dict(metadata))


def _sorted_votes(store: Dict[str, Dict[str, Any]], *, numeric: bool = False) -> List[Dict[str, Any]]:
    def _key(item: Dict[str, Any]) -> Tuple[float, float, str]:
        value = item.get("value")
        label = str(value)
        if numeric:
            try:
                label = f"{int(value):03d}"
            except Exception:
                label = str(value)
        return (
            -float(item.get("support_count") or 0.0),
            -float(item.get("score_total") or 0.0),
            label,
        )

    ordered = sorted(store.values(), key=_key)
    for entry in ordered:
        entry["sources"] = sorted(
            entry.get("sources") or [],
            key=lambda item: (-float(item.get("score") or 0.0), str(item.get("source") or "")),
        )
    return ordered


def _top_weighted_keys(counter: Dict[str, float], *, limit: int, numeric: bool = False) -> List[str]:
    items = sorted(
        ((str(key), float(value)) for key, value in counter.items() if str(key).strip()),
        key=lambda kv: (
            -kv[1],
            f"{int(kv[0]):03d}" if numeric and str(kv[0]).isdigit() else str(kv[0]),
        ),
    )
    return [key for key, _ in items[: max(0, int(limit))]]


def _normalize_counter_values(values: Any, *, pick3_only: bool = False) -> List[str]:
    out: List[str] = []
    if not isinstance(values, list):
        return out
    for item in values:
        text = _normalize_pick3_literal(item) if pick3_only else str(item or "").strip()
        if text:
            out.append(text)
    return out


def _stable_survivor_profile_from_frontier(frontier: Dict[str, Any]) -> str:
    entries = frontier.get("entries") if isinstance(frontier.get("entries"), list) else []
    last_remaining_count = sum(1 for entry in entries if isinstance(entry, dict) and bool(entry.get("last_remaining_3v")))
    if last_remaining_count <= 0:
        return ""

    pattern_summary = frontier.get("frontier_pattern_summary") if isinstance(frontier.get("frontier_pattern_summary"), dict) else {}
    exact_patterns = _normalize_counter_values(pattern_summary.get("exact3digit_patterns_all"), pick3_only=True)
    three_value_patterns = _normalize_counter_values(pattern_summary.get("three_value_like_patterns_all"), pick3_only=True)
    hidden_patterns = _normalize_counter_values(pattern_summary.get("hidden_terminal_patterns_all"), pick3_only=False)
    vtrac_indices = _normalize_counter_values(pattern_summary.get("vtrac_indices_all"), pick3_only=False)

    if len(exact_patterns) == 1:
        profile = "exact_single_literal"
    elif len(exact_patterns) > 1 and len(vtrac_indices) == 1:
        profile = "multi_literal_single_vtrac_family"
    elif len(exact_patterns) > 1:
        profile = "multi_literal_mixed_family"
    elif len(vtrac_indices) == 1 and three_value_patterns:
        profile = "hidden_single_vtrac_family"
    else:
        profile = "unresolved_terminal"

    if hidden_patterns and profile in {"exact_single_literal", "multi_literal_single_vtrac_family", "hidden_single_vtrac_family"}:
        profile = f"{profile}_with_hidden_support"
    return profile


def _build_stable_survivor_context(stable_tool: Dict[str, Any]) -> Dict[str, Any]:
    sections = stable_tool.get("sections") if isinstance(stable_tool.get("sections"), dict) else {}
    if not sections:
        return {
            "available": False,
            "frontier_count": 0,
            "progression_count": 0,
            "last_remaining_rows": 0,
        }

    frontier_canonical_weights: Dict[str, float] = defaultdict(float)
    frontier_vtrac_weights: Dict[str, float] = defaultdict(float)
    three_value_weights: Dict[str, float] = defaultdict(float)
    hidden_terminal_weights: Dict[str, float] = defaultdict(float)
    last_remaining_canonical_weights: Dict[str, float] = defaultdict(float)
    last_remaining_vtrac_weights: Dict[str, float] = defaultdict(float)
    profile_counter: Dict[str, float] = defaultdict(float)

    frontier_examples: List[Dict[str, Any]] = []
    last_remaining_examples: List[Dict[str, Any]] = []
    frontier_count = 0
    frontier_single_family_count = 0
    frontier_multi_family_count = 0
    progression_count = 0
    progression_with_last_remaining_count = 0
    last_remaining_rows = 0
    hidden_terminal_frontier_count = 0

    for section, block in sections.items():
        if not isinstance(block, dict):
            continue
        summary = block.get("summary") if isinstance(block.get("summary"), dict) else {}
        section_last_remaining_rows = _to_int(summary.get("last_remaining_rows"), 0)

        frontiers = block.get("survivor_frontiers") if isinstance(block.get("survivor_frontiers"), list) else []
        progressions = block.get("survivor_progressions") if isinstance(block.get("survivor_progressions"), list) else []
        frontier_count += len(frontiers)
        progression_count += len(progressions)
        progression_with_last_remaining_count += sum(
            1 for item in progressions if isinstance(item, dict) and bool(item.get("has_last_remaining"))
        )

        for frontier in frontiers:
            if not isinstance(frontier, dict):
                continue
            if bool(frontier.get("is_single_family")):
                frontier_single_family_count += 1
            else:
                frontier_multi_family_count += 1

            pattern_summary = frontier.get("frontier_pattern_summary") if isinstance(frontier.get("frontier_pattern_summary"), dict) else {}
            exact_patterns = _normalize_counter_values(pattern_summary.get("exact3digit_patterns_all"), pick3_only=True)
            vtrac_indices = _normalize_counter_values(pattern_summary.get("vtrac_indices_all"), pick3_only=False)
            three_value_patterns = _normalize_counter_values(pattern_summary.get("three_value_like_patterns_all"), pick3_only=True)
            hidden_patterns = _normalize_counter_values(pattern_summary.get("hidden_terminal_patterns_all"), pick3_only=False)
            last_remaining_count = sum(
                1 for entry in (frontier.get("entries") or []) if isinstance(entry, dict) and bool(entry.get("last_remaining_3v"))
            )
            section_last_remaining_rows += last_remaining_count
            progression_cols = _to_int(frontier.get("progression_column_count"), 0)
            if hidden_patterns:
                hidden_terminal_frontier_count += 1

            for item in (pattern_summary.get("exact3digit_patterns_top") or [])[:6]:
                if not isinstance(item, dict):
                    continue
                value = _normalize_pick3_literal(item.get("value"))
                if not value:
                    continue
                weight = float(max(1, _to_int(item.get("count"), 1)) + min(3, progression_cols) + (2 if last_remaining_count > 0 else 0))
                frontier_canonical_weights[value] += weight
                if last_remaining_count > 0:
                    last_remaining_canonical_weights[value] += weight

            for item in (pattern_summary.get("vtrac_indices_top") or [])[:6]:
                if not isinstance(item, dict):
                    continue
                value = str(item.get("value") or "").strip()
                if not value:
                    continue
                weight = float(max(1, _to_int(item.get("count"), 1)) + min(3, progression_cols) + (2 if last_remaining_count > 0 else 0))
                frontier_vtrac_weights[value] += weight
                if last_remaining_count > 0:
                    last_remaining_vtrac_weights[value] += weight

            for value in three_value_patterns[:8]:
                three_value_weights[value] += 1.0 + (1.0 if last_remaining_count > 0 else 0.0)
            for value in hidden_patterns[:8]:
                hidden_terminal_weights[value] += 1.0 + (1.0 if last_remaining_count > 0 else 0.0)

            example = {
                "section": str(section),
                "set": str(frontier.get("set") or ""),
                "draw": str(frontier.get("draw") or ""),
                "frontier_column": _to_int(frontier.get("frontier_column"), 0),
                "progression_column_count": progression_cols,
                "is_single_family": bool(frontier.get("is_single_family")),
                "frontier_family_count": _to_int(frontier.get("frontier_family_count"), 0),
                "last_remaining_count": last_remaining_count,
                "exact3digit_patterns": exact_patterns[:8],
                "three_value_like_patterns": three_value_patterns[:8],
                "vtrac_indices": vtrac_indices[:8],
                "hidden_terminal_patterns": hidden_patterns[:6],
            }
            frontier_examples.append(example)

            profile = _stable_survivor_profile_from_frontier(frontier)
            if profile:
                profile_counter[profile] += 1.0
                last_remaining_examples.append({**example, "profile": profile})
        last_remaining_rows += section_last_remaining_rows

    frontier_examples.sort(
        key=lambda item: (
            -_to_int(item.get("last_remaining_count"), 0),
            -_to_int(item.get("progression_column_count"), 0),
            str(item.get("section") or ""),
            str(item.get("set") or ""),
            str(item.get("draw") or ""),
            _to_int(item.get("frontier_column"), 0),
        )
    )
    last_remaining_examples.sort(
        key=lambda item: (
            -_to_int(item.get("last_remaining_count"), 0),
            -_to_int(item.get("progression_column_count"), 0),
            str(item.get("profile") or ""),
            str(item.get("section") or ""),
            str(item.get("set") or ""),
            str(item.get("draw") or ""),
        )
    )

    return {
        "available": bool(frontier_count or progression_count or last_remaining_rows),
        "frontier_count": int(frontier_count),
        "frontier_single_family_count": int(frontier_single_family_count),
        "frontier_multi_family_count": int(frontier_multi_family_count),
        "progression_count": int(progression_count),
        "progression_with_last_remaining_count": int(progression_with_last_remaining_count),
        "last_remaining_rows": int(last_remaining_rows),
        "hidden_terminal_frontier_count": int(hidden_terminal_frontier_count),
        "top_frontier_canonicals": _top_weighted_keys(frontier_canonical_weights, limit=10),
        "top_frontier_vtrac_indices": _top_weighted_keys(frontier_vtrac_weights, limit=10, numeric=True),
        "top_three_value_like_patterns": _top_weighted_keys(three_value_weights, limit=10),
        "top_hidden_terminal_patterns": _top_weighted_keys(hidden_terminal_weights, limit=10),
        "top_last_remaining_canonicals": _top_weighted_keys(last_remaining_canonical_weights, limit=10),
        "top_last_remaining_vtrac_indices": _top_weighted_keys(last_remaining_vtrac_weights, limit=10, numeric=True),
        "last_remaining_profile_counts": {
            key: int(value)
            for key, value in sorted(profile_counter.items(), key=lambda kv: (-kv[1], kv[0]))
        },
        "frontier_examples": frontier_examples[:10],
        "last_remaining_examples": last_remaining_examples[:10],
    }


def _build_r_consensus_context(stable_tool: Dict[str, Any]) -> Dict[str, Any]:
    context = stable_tool.get("r_consensus_context") if isinstance(stable_tool.get("r_consensus_context"), dict) else {}
    if not context:
        return {
            "available": False,
            "event_count": 0,
            "trial_eligible": False,
            "signal_strength_class": "none",
        }
    return {
        "available": bool(context.get("available")),
        "event_count": _to_int(context.get("event_count"), 0),
        "single_digit_count": _to_int(context.get("single_digit_count"), 0),
        "two_digit_count": _to_int(context.get("two_digit_count"), 0),
        "col1_count": _to_int(context.get("col1_count"), 0),
        "col2_count": _to_int(context.get("col2_count"), 0),
        "cons_full_event_count": _to_int(context.get("cons_full_event_count"), 0),
        "cons_3v_event_count": _to_int(context.get("cons_3v_event_count"), 0),
        "cons_stub_event_count": _to_int(context.get("cons_stub_event_count"), 0),
        "section_counts": dict(context.get("section_counts") or {}) if isinstance(context.get("section_counts"), dict) else {},
        "cross_variant_tail_values": [str(value) for value in (context.get("cross_variant_tail_values") or []) if str(value).strip()],
        "top_tail_values": [str(value) for value in (context.get("top_tail_values") or []) if str(value).strip()],
        "top_support_canonicals": [_canon(value) for value in (context.get("top_support_canonicals") or []) if _canon(value)],
        "top_support_vtrac_indices": [str(value) for value in (context.get("top_support_vtrac_indices") or []) if str(value).strip()],
        "signal_strength_class": str(context.get("signal_strength_class") or "none"),
        "trial_eligible": bool(context.get("trial_eligible")),
        "events_top": [item for item in (context.get("events_top") or [])[:10] if isinstance(item, dict)],
    }


def _build_cross_tool_relations(
    *,
    stable_tool: Dict[str, Any],
    stable_survivor_context: Dict[str, Any],
    r_consensus_context: Dict[str, Any],
    dr_tool: Dict[str, Any],
    vtrac_tool: Dict[str, Any],
    hot_tool: Dict[str, Any],
    aux_tool: Dict[str, Any],
) -> Dict[str, Any]:
    canonical_votes: Dict[str, Dict[str, Any]] = {}
    vtrac_votes: Dict[str, Dict[str, Any]] = {}
    family_votes: Dict[str, Dict[str, Any]] = {}

    stable_sections = stable_tool.get("sections") if isinstance(stable_tool.get("sections"), dict) else {}
    for section, block in stable_sections.items():
        if not isinstance(block, dict):
            continue
        for row in (block.get("top_row_patterns") or [])[:12]:
            if not isinstance(row, dict):
                continue
            canonical = str(row.get("canonical") or "")
            score = _to_float(row.get("score"))
            _register_vote(canonical_votes, key=canonical, source=f"stable:{section}:row", score=score, literal=canonical)
            idx = get_vtrac_index(canonical) if canonical else None
            if idx is not None:
                _register_vote(vtrac_votes, key=str(idx), source=f"stable:{section}:row", score=score, literal=canonical)
        for row in (block.get("top_compound_patterns") or [])[:12]:
            if not isinstance(row, dict):
                continue
            canonical = str(row.get("canonical") or "")
            score = _to_float(row.get("compound_score"))
            _register_vote(canonical_votes, key=canonical, source=f"stable:{section}:compound", score=score, literal=canonical)
            idx = get_vtrac_index(canonical) if canonical else None
            if idx is not None:
                _register_vote(vtrac_votes, key=str(idx), source=f"stable:{section}:compound", score=score, literal=canonical)
        for row in (block.get("family_rollups_top") or [])[:8]:
            if not isinstance(row, dict):
                continue
            family_id = str(row.get("family_id") or "").strip()
            score = _to_float(row.get("family_score_total"))
            _register_vote(family_votes, key=family_id, source=f"stable:{section}:family", score=score, metadata={"section": section})

    for value in (stable_survivor_context.get("top_frontier_canonicals") or [])[:8]:
        canonical = _canon(value)
        if canonical:
            _register_vote(canonical_votes, key=canonical, source="stable:survivor_frontier", score=4.0, literal=canonical)
    for value in (stable_survivor_context.get("top_last_remaining_canonicals") or [])[:8]:
        canonical = _canon(value)
        if canonical:
            _register_vote(canonical_votes, key=canonical, source="stable:last_remaining", score=6.0, literal=canonical)
    for value in (stable_survivor_context.get("top_frontier_vtrac_indices") or [])[:8]:
        text = str(value or "").strip()
        if text:
            _register_vote(vtrac_votes, key=text, source="stable:survivor_frontier", score=4.0)
    for value in (stable_survivor_context.get("top_last_remaining_vtrac_indices") or [])[:8]:
        text = str(value or "").strip()
        if text:
            _register_vote(vtrac_votes, key=text, source="stable:last_remaining", score=6.0)
    consensus_strength = {
        "strong": 3.5,
        "moderate": 2.5,
        "light": 1.5,
    }.get(str(r_consensus_context.get("signal_strength_class") or ""), 1.0)
    if r_consensus_context.get("available"):
        for rank, value in enumerate((r_consensus_context.get("top_support_canonicals") or [])[:6], start=1):
            canonical = _canon(value)
            if canonical:
                _register_vote(
                    canonical_votes,
                    key=canonical,
                    source="stable:r_consensus",
                    score=max(0.75, consensus_strength - ((rank - 1) * 0.35)),
                    literal=canonical,
                )
        for rank, value in enumerate((r_consensus_context.get("top_support_vtrac_indices") or [])[:6], start=1):
            text = str(value or "").strip()
            if text:
                _register_vote(
                    vtrac_votes,
                    key=text,
                    source="stable:r_consensus",
                    score=max(0.75, consensus_strength - ((rank - 1) * 0.35)),
                )

    dr_sections = dr_tool.get("sections") if isinstance(dr_tool.get("sections"), dict) else {}
    for section, block in dr_sections.items():
        if not isinstance(block, dict):
            continue
        summary = block.get("summary") if isinstance(block.get("summary"), dict) else {}
        for row in (summary.get("top_candidate_preview") or [])[:8]:
            if not isinstance(row, dict):
                continue
            pattern = _normalize_pick3_literal(row.get("best_pattern"))
            if not pattern:
                continue
            score = _to_float(row.get("score_v2"))
            _register_vote(canonical_votes, key=_canon(pattern), source=f"dr:{section}:candidate", score=score, literal=pattern)
            idx = get_vtrac_index(pattern)
            if idx is not None:
                _register_vote(vtrac_votes, key=str(idx), source=f"dr:{section}:candidate", score=score, literal=pattern)
            family_id = str(row.get("family_id") or "").strip()
            _register_vote(family_votes, key=family_id, source=f"dr:{section}:candidate", score=score, metadata={"section": section})

    vtrac_enhanced = vtrac_tool.get("enhanced") if isinstance(vtrac_tool.get("enhanced"), dict) else {}
    for row in (vtrac_enhanced.get("straights_ranked") or [])[:15]:
        if not isinstance(row, dict):
            continue
        straight = _normalize_pick3_literal(row.get("straight"))
        if not straight:
            continue
        score = _to_float(row.get("score"))
        _register_vote(canonical_votes, key=_canon(straight), source="vtrac:straight", score=score, literal=straight)
        idx = row.get("index")
        if idx is not None:
            _register_vote(vtrac_votes, key=str(idx), source="vtrac:straight", score=score, literal=straight)
    for row in (vtrac_enhanced.get("indices_ranked") or [])[:15]:
        if not isinstance(row, dict):
            continue
        idx = row.get("index")
        if idx is not None:
            _register_vote(vtrac_votes, key=str(idx), source="vtrac:index", score=_to_float(row.get("score")))
    compact_day = vtrac_tool.get("compact_report_day") if isinstance(vtrac_tool.get("compact_report_day"), dict) else {}
    for row in (compact_day.get("top_indices_by_state") or [])[:10]:
        if not isinstance(row, dict):
            continue
        idx = row.get("index")
        if idx is not None:
            _register_vote(vtrac_votes, key=str(idx), source="vtrac:day_compact", score=_to_float(row.get("score")))

    for row in (hot_tool.get("top_lanes") or [])[:15]:
        if not isinstance(row, dict):
            continue
        canonical = str(row.get("canonical") or "")
        triad = _normalize_pick3_literal(row.get("triad"))
        score = _to_float(row.get("score_mean"))
        _register_vote(canonical_votes, key=canonical, source="hot:top_lane", score=score, literal=triad)
        idx = row.get("vtrac_index")
        if idx is not None:
            _register_vote(vtrac_votes, key=str(idx), source="hot:top_lane", score=score, literal=triad)

    arena_objects = aux_tool.get("arena_objects") if isinstance(aux_tool.get("arena_objects"), dict) else {}
    positional = arena_objects.get("aux_positional_pressure") if isinstance(arena_objects.get("aux_positional_pressure"), dict) else {}
    for row in (positional.get("shortlist_top") or [])[:10]:
        if not isinstance(row, dict):
            continue
        combo = _normalize_pick3_literal(row.get("combo"))
        canonical = str(row.get("canonical") or _canon(combo))
        score = _to_float(row.get("score"))
        _register_vote(canonical_votes, key=canonical, source="aux:positional", score=score, literal=combo)
        idx = row.get("vtrac_index")
        if idx is not None and int(idx) >= 0:
            _register_vote(vtrac_votes, key=str(idx), source="aux:positional", score=score, literal=combo)

    badge = arena_objects.get("aux_badge_pressure") if isinstance(arena_objects.get("aux_badge_pressure"), dict) else {}
    for row in (badge.get("top_combo_alerts") or [])[:10]:
        if not isinstance(row, dict):
            continue
        combo = _normalize_pick3_literal(row.get("combo"))
        canonical = str(row.get("canonical") or _canon(combo))
        score = float(_to_int(row.get("draws_since")))
        _register_vote(canonical_votes, key=canonical, source="aux:badge_combo", score=score, literal=combo)
        idx = get_vtrac_index(combo)
        if idx is not None:
            _register_vote(vtrac_votes, key=str(idx), source="aux:badge_combo", score=score, literal=combo)
    index_pressure = badge.get("index_pressure") if isinstance(badge.get("index_pressure"), dict) else {}
    by_variant = index_pressure.get("by_variant") if isinstance(index_pressure.get("by_variant"), dict) else {}
    for variant, data in by_variant.items():
        if not isinstance(data, dict):
            continue
        for row in (data.get("top_indices") or [])[:6]:
            if not isinstance(row, dict):
                continue
            idx = row.get("index")
            if idx is not None:
                _register_vote(vtrac_votes, key=str(idx), source=f"aux:badge_index:{variant}", score=_to_float(row.get("pressure_density")))

    aux_vtrac = arena_objects.get("aux_vtrac_pressure") if isinstance(arena_objects.get("aux_vtrac_pressure"), dict) else {}
    overlay_top = aux_vtrac.get("overlay_top") if isinstance(aux_vtrac.get("overlay_top"), dict) else {}
    for variant, rows in overlay_top.items():
        if not isinstance(rows, list):
            continue
        for row in rows[:6]:
            if not isinstance(row, dict):
                continue
            idx = row.get("index")
            if idx is not None:
                _register_vote(vtrac_votes, key=str(idx), source=f"aux:vtrac_overlay:{variant}", score=_to_float(row.get("draws_since")))

    blackapple = arena_objects.get("aux_blackapple_context") if isinstance(arena_objects.get("aux_blackapple_context"), dict) else {}
    for row in (blackapple.get("control_center_top") or [])[:6]:
        if not isinstance(row, dict):
            continue
        for example in row.get("examples") or []:
            combo = _normalize_pick3_literal(example)
            if not combo:
                continue
            _register_vote(canonical_votes, key=_canon(combo), source="aux:blackapple", score=_to_float(row.get("ba_score")), literal=combo)
            idx = get_vtrac_index(combo)
            if idx is not None:
                _register_vote(vtrac_votes, key=str(idx), source="aux:blackapple", score=_to_float(row.get("ba_score")), literal=combo)

    profit_alerts = arena_objects.get("cc_profit_alert_context") if isinstance(arena_objects.get("cc_profit_alert_context"), dict) else {}
    for row in (profit_alerts.get("top_alerts") or [])[:10]:
        if not isinstance(row, dict):
            continue
        canonical = str(row.get("canonical") or "")
        score = _to_float(row.get("strength"))
        _register_vote(canonical_votes, key=canonical, source="context:profit_alert", score=score, literal=canonical)
        idx = get_vtrac_index(canonical)
        if idx is not None:
            _register_vote(vtrac_votes, key=str(idx), source="context:profit_alert", score=score, literal=canonical)
        evidence_summary = row.get("evidence_summary") if isinstance(row.get("evidence_summary"), dict) else {}
        family_id = str(evidence_summary.get("stable_family_id") or "").strip()
        _register_vote(family_votes, key=family_id, source="context:profit_alert", score=score)

    canonical_consensus = _sorted_votes(canonical_votes)
    vtrac_consensus = _sorted_votes(vtrac_votes, numeric=True)
    family_consensus = _sorted_votes(family_votes)

    regime_flags: List[str] = []
    contradiction_flags: List[str] = []

    if any(_is_double(str(item.get("value") or "")) for item in canonical_consensus[:5]):
        regime_flags.append("double_heavy_canonical_surface")
    if _to_int(stable_survivor_context.get("frontier_count"), 0) > 0:
        regime_flags.append("stable_survivor_frontier_present")
    if _to_int(stable_survivor_context.get("progression_count"), 0) > 0:
        regime_flags.append("stable_survivor_progression_present")
    if _to_int(stable_survivor_context.get("last_remaining_rows"), 0) > 0:
        regime_flags.append("stable_last_remaining_present")
    if _to_int(stable_survivor_context.get("hidden_terminal_frontier_count"), 0) > 0:
        regime_flags.append("stable_hidden_terminal_present")
    if _to_int(r_consensus_context.get("event_count"), 0) > 0:
        regime_flags.append("r_consensus_present")
    if _to_int(r_consensus_context.get("event_count"), 0) > 1:
        regime_flags.append("r_consensus_multi_event")
    if r_consensus_context.get("cross_variant_tail_values"):
        regime_flags.append("r_consensus_cross_variant")
    if bool(r_consensus_context.get("trial_eligible")):
        regime_flags.append("r_consensus_trial_eligible")
    if any(item.get("string_source_count", 0) > 0 and item.get("context_source_count", 0) > 0 for item in canonical_consensus[:8]):
        regime_flags.append("context_reinforced_canonical_overlap")
    if any(item.get("string_source_count", 0) > 0 and item.get("context_source_count", 0) > 0 for item in vtrac_consensus[:8]):
        regime_flags.append("cross_tool_vtrac_alignment")
    if (canonical_consensus[:1] and canonical_consensus[0].get("support_count", 0) <= 2) and (vtrac_consensus[:1] and vtrac_consensus[0].get("support_count", 0) >= 3):
        regime_flags.append("vtrac_stronger_than_literal")
    if not canonical_consensus or canonical_consensus[0].get("support_count", 0) <= 1:
        contradiction_flags.append("no_clear_canonical_consensus")
    if any(item.get("string_source_count", 0) == 0 and item.get("context_source_count", 0) > 0 for item in canonical_consensus[:8]):
        contradiction_flags.append("context_only_canonical_pressure_present")
    if family_consensus and family_consensus[0].get("support_count", 0) <= 1:
        contradiction_flags.append("stable_dr_family_split")

    return {
        "canonical_consensus_top": canonical_consensus[:15],
        "vtrac_index_consensus_top": vtrac_consensus[:15],
        "family_consensus_top": family_consensus[:12],
        "r_consensus_context": r_consensus_context,
        "regime_flags": regime_flags,
        "contradiction_flags": contradiction_flags,
    }


def _build_arena_synthesis(
    *,
    cross_tool_relations: Dict[str, Any],
    stable_survivor_context: Dict[str, Any],
    r_consensus_context: Dict[str, Any],
) -> Dict[str, Any]:
    canonical_consensus = list(cross_tool_relations.get("canonical_consensus_top") or [])
    vtrac_consensus = list(cross_tool_relations.get("vtrac_index_consensus_top") or [])
    family_consensus = list(cross_tool_relations.get("family_consensus_top") or [])
    regime_flags = [str(x) for x in (cross_tool_relations.get("regime_flags") or []) if str(x)]
    contradiction_flags = [str(x) for x in (cross_tool_relations.get("contradiction_flags") or []) if str(x)]

    context_reinforced_canonicals = [
        item for item in canonical_consensus if int(item.get("string_source_count") or 0) > 0 and int(item.get("context_source_count") or 0) > 0
    ][:10]
    context_only_pressure = [
        item for item in canonical_consensus if int(item.get("string_source_count") or 0) == 0 and int(item.get("context_source_count") or 0) > 0
    ][:10]

    dominant_canonicals = canonical_consensus[:10]
    dominant_vtrac_indices = vtrac_consensus[:10]
    dominant_families = family_consensus[:8]
    dominant_canonical_value = str(dominant_canonicals[0]["value"]) if dominant_canonicals else ""
    dominant_canonical_index = get_vtrac_index(dominant_canonical_value) if dominant_canonical_value else None

    vtrac_literal_watchlist: List[Dict[str, Any]] = []
    for rank, item in enumerate(dominant_vtrac_indices[:6], start=1):
        if int(item.get("string_source_count") or 0) <= 0:
            continue
        literals = [str(x) for x in (item.get("example_literals") or []) if str(x).strip()]
        if not literals:
            continue
        canonicals: List[str] = []
        for literal in literals:
            canonical = _canon(literal)
            if canonical and canonical not in canonicals:
                canonicals.append(canonical)
        vtrac_literal_watchlist.append(
            {
                "vtrac_index": str(item.get("value") or ""),
                "rank": rank,
                "support_count": int(item.get("support_count") or 0),
                "score_total": round(float(item.get("score_total") or 0.0), 6),
                "string_source_count": int(item.get("string_source_count") or 0),
                "context_source_count": int(item.get("context_source_count") or 0),
                "example_literals": literals[:10],
                "candidate_canonicals": canonicals[:10],
                "is_dominant_vtrac_index": rank == 1,
                "dominant_canonical_split": (
                    dominant_canonical_index is not None and str(dominant_canonical_index) != str(item.get("value") or "")
                ),
            }
        )

    state_regime = {
        "dominant_canonical": dominant_canonical_value or None,
        "dominant_vtrac_index": dominant_vtrac_indices[0]["value"] if dominant_vtrac_indices else None,
        "dominant_family": dominant_families[0]["value"] if dominant_families else None,
        "double_heavy": "double_heavy_canonical_surface" in regime_flags,
        "context_reinforced": "context_reinforced_canonical_overlap" in regime_flags,
        "vtrac_alignment": "aligned" if "cross_tool_vtrac_alignment" in regime_flags else "mixed",
        "tail_consensus_present": "r_consensus_present" in regime_flags,
        "tail_consensus_value": (r_consensus_context.get("top_tail_values") or [None])[0],
        "tail_consensus_column": (
            "col1"
            if _to_int(r_consensus_context.get("col1_count"), 0) >= _to_int(r_consensus_context.get("col2_count"), 0)
            and _to_int(r_consensus_context.get("col1_count"), 0) > 0
            else "col2"
            if _to_int(r_consensus_context.get("col2_count"), 0) > 0
            else None
        ),
        "consensus_strength_class": str(r_consensus_context.get("signal_strength_class") or "none"),
        "consensus_trial_eligible": bool(r_consensus_context.get("trial_eligible")),
        "r_consensus_event_count": _to_int(r_consensus_context.get("event_count"), 0),
        "r_consensus_cross_variant_tail_count": len(r_consensus_context.get("cross_variant_tail_values") or []),
        "survivor_pressure": "stable_survivor_frontier_present" in regime_flags,
        "survivor_progression": "stable_survivor_progression_present" in regime_flags,
        "last_remaining": "stable_last_remaining_present" in regime_flags,
        "hidden_terminal_support": "stable_hidden_terminal_present" in regime_flags,
        "survivor_frontier_count": _to_int(stable_survivor_context.get("frontier_count"), 0),
        "survivor_progression_count": _to_int(stable_survivor_context.get("progression_count"), 0),
        "last_remaining_rows": _to_int(stable_survivor_context.get("last_remaining_rows"), 0),
        "contradiction_count": len(contradiction_flags),
    }

    review_prompts: List[str] = []
    if dominant_vtrac_indices:
        top = ", ".join(str(item["value"]) for item in dominant_vtrac_indices[:3])
        review_prompts.append(f"Check winners HTML against dominant VTRAC indices {top} before evaluating literal conversion.")
    if vtrac_literal_watchlist:
        top = ", ".join(
            f"{item['vtrac_index']}:{'/'.join(item['candidate_canonicals'][:2])}"
            for item in vtrac_literal_watchlist[:3]
        )
        review_prompts.append(f"Use VTRAC watchlist {top} to inspect lane-linked literal neighborhoods before downstream conversion decisions.")
    if context_reinforced_canonicals:
        top = ", ".join(str(item["value"]) for item in context_reinforced_canonicals[:3])
        review_prompts.append(f"Check whether context-reinforced canonicals {top} are structurally alive or only alert-driven.")
    if contradiction_flags:
        review_prompts.append(f"Inspect contradiction flags: {', '.join(contradiction_flags[:4])}.")
    if dominant_families:
        top = ", ".join(str(item["value"]) for item in dominant_families[:3])
        review_prompts.append(f"Compare family agreement {top} against actual winner family / corridor behavior.")
    if stable_survivor_context.get("available"):
        survivor_canonicals = ", ".join(str(value) for value in (stable_survivor_context.get("top_frontier_canonicals") or [])[:3])
        if survivor_canonicals:
            review_prompts.append(
                f"Inspect stable survivor frontiers around {survivor_canonicals} before compressing literal corridor truth."
            )
        last_profiles = stable_survivor_context.get("last_remaining_profile_counts") if isinstance(stable_survivor_context.get("last_remaining_profile_counts"), dict) else {}
        if last_profiles:
            top_profiles = ", ".join(list(last_profiles.keys())[:3])
            review_prompts.append(f"Review stable last-remaining terminal profiles: {top_profiles}.")
        hidden_patterns = ", ".join(str(value) for value in (stable_survivor_context.get("top_hidden_terminal_patterns") or [])[:3])
        if hidden_patterns:
            review_prompts.append(f"Check hidden survivor terminals {hidden_patterns} for family/VTRAC carryover value.")
    if r_consensus_context.get("available"):
        tail_values = ", ".join(str(value) for value in (r_consensus_context.get("top_tail_values") or [])[:3])
        support_canonicals = ", ".join(str(value) for value in (r_consensus_context.get("top_support_canonicals") or [])[:3])
        review_prompts.append(
            f"Inspect R-Consensus tails {tail_values or '-'} against local support canonicals {support_canonicals or '-'} before any translator-style interpretation."
        )
        if r_consensus_context.get("cross_variant_tail_values"):
            cross_variant_tails = ", ".join(str(value) for value in (r_consensus_context.get("cross_variant_tail_values") or [])[:3])
            review_prompts.append(f"Check whether cross-variant R-Consensus tails {cross_variant_tails} align with survivor, VTRAC, or alert corridors.")

    return {
        "dominant_canonicals": dominant_canonicals,
        "dominant_vtrac_indices": dominant_vtrac_indices,
        "dominant_families": dominant_families,
        "vtrac_literal_watchlist": vtrac_literal_watchlist,
        "context_reinforced_canonicals": context_reinforced_canonicals,
        "context_only_pressure": context_only_pressure,
        "stable_survivor_context": stable_survivor_context,
        "r_consensus_context": r_consensus_context,
        "state_regime": state_regime,
        "review_prompts": review_prompts,
    }


def _select_preferred_file(state_dir: Path, stem: str, preferred: Sequence[str]) -> Optional[Path]:
    candidates = sorted(state_dir.glob(f"{stem}*.json"))
    if not candidates:
        return None
    for suffix in preferred:
        for path in candidates:
            if path.name == suffix:
                return path
    return candidates[0]


def _build_downstream_handoff(state_dir: Path, repo_root: Path) -> Tuple[Dict[str, Any], List[Path]]:
    candidate_path = _select_preferred_file(
        state_dir,
        "candidate_universe",
        (
            "candidate_universe__tool_only.json",
            "candidate_universe__tool_only__stable10.json",
        ),
    )
    play_card_path = _select_preferred_file(
        state_dir,
        "play_card",
        (
            "play_card__tool_only.json",
            "play_card__tool_only__stable10.json",
        ),
    )

    inputs: List[Path] = []
    payload: Dict[str, Any] = {}

    if candidate_path is not None:
        raw = _read_json(candidate_path)
        if isinstance(raw, dict):
            payload["candidate_universe"] = {
                "available": True,
                "path": _safe_rel(candidate_path, repo_root),
                "schema_version": raw.get("schema_version"),
                "union_combos_count": raw.get("union_combos_count"),
                "pack_count": len(raw.get("packs") or []) if isinstance(raw.get("packs"), list) else 0,
                "digit_envelopes_count": len(raw.get("digit_envelopes") or []) if isinstance(raw.get("digit_envelopes"), list) else 0,
            }
            inputs.append(candidate_path)
    else:
        payload["candidate_universe"] = {"available": False}

    if play_card_path is not None:
        raw = _read_json(play_card_path)
        if isinstance(raw, dict):
            ranked_top = []
            for row in (raw.get("ranked_candidates") or [])[:10]:
                if not isinstance(row, dict):
                    continue
                ranked_top.append(
                    {
                        "combo": _normalize_pick3_literal(row.get("combo") or row.get("candidate")),
                        "canonical": _canon(row.get("combo") or row.get("candidate")),
                        "score": round(_to_float(row.get("score")), 6),
                    }
                )
            payload["play_card"] = {
                "available": True,
                "path": _safe_rel(play_card_path, repo_root),
                "schema_version": raw.get("schema_version"),
                "ranked_candidate_count": len(raw.get("ranked_candidates") or []) if isinstance(raw.get("ranked_candidates"), list) else 0,
                "strategy_names": sorted((raw.get("strategies") or {}).keys()) if isinstance(raw.get("strategies"), dict) else [],
                "ranked_candidates_top": ranked_top,
            }
            inputs.append(play_card_path)
    else:
        payload["play_card"] = {"available": False}

    return payload, inputs


def _build_review_links(
    *,
    day_dir: Path,
    state_dir: Path,
    state_key: str,
    repo_root: Path,
) -> Tuple[Dict[str, Any], List[Path]]:
    inputs: List[Path] = []
    winners_dir = state_dir / "winners" / state_key
    winners_files = sorted(winners_dir.glob("*")) if winners_dir.exists() else []
    inputs.extend([path for path in winners_files if path.is_file()])

    signals_candidates = sorted((state_dir / "analysis").glob("signals_bundle__*.json")) if (state_dir / "analysis").exists() else []
    signals_path = signals_candidates[-1] if signals_candidates else None
    if signals_path is not None:
        inputs.append(signals_path)

    cc_meta = day_dir / "control_center" / "meta.json"
    if cc_meta.exists():
        inputs.append(cc_meta)

    tool_dirs = {}
    for name in ("stable", "digit_reduction", "vtrac", "hot_zones", "aux", "winners"):
        path = state_dir / name
        if path.exists():
            tool_dirs[name] = _safe_rel(path, repo_root)

    return (
        {
            "signals_bundle_path": _safe_rel(signals_path, repo_root) if signals_path is not None else None,
            "control_center_meta_path": _safe_rel(cc_meta, repo_root) if cc_meta.exists() else None,
            "winners_dir": _safe_rel(winners_dir, repo_root) if winners_dir.exists() else None,
            "winners_files": [_safe_rel(path, repo_root) for path in winners_files[:20]],
            "tool_dirs": tool_dirs,
        },
        inputs,
    )


def build_aggregated_analysis_arena_payload(
    *,
    day_dir: Path,
    state_key: str,
    results_date: str,
    history_date: Optional[str],
    profile: str,
    experiment_tag: str,
    sharepacks_root: Path,
    repo_root: Path = REPO_ROOT,
    top_items: int = 12,
) -> Dict[str, Any]:
    state_dir = day_dir / state_key
    day_meta = _load_day_meta(day_dir)
    contains_winners_artifacts = _contains_winners_for_state(day_meta, state_key, sharepacks_root)

    stable_tool, stable_inputs, stable_status = _load_or_build_stable_payload(
        day_dir=day_dir,
        state_dir=state_dir,
        state_key=state_key,
        results_date=results_date,
        history_date=history_date,
        profile=profile,
        experiment_tag=experiment_tag,
        sharepacks_root=sharepacks_root,
        contains_winners_artifacts=contains_winners_artifacts,
        repo_root=repo_root,
    )
    dr_tool, dr_inputs, dr_status = _load_or_build_dr_payload(
        day_dir=day_dir,
        state_dir=state_dir,
        state_key=state_key,
        results_date=results_date,
        history_date=history_date,
        profile=profile,
        experiment_tag=experiment_tag,
        sharepacks_root=sharepacks_root,
        contains_winners_artifacts=contains_winners_artifacts,
        repo_root=repo_root,
    )
    aux_tool, aux_inputs, aux_status = _load_or_build_aux_payload(
        day_dir=day_dir,
        state_dir=state_dir,
        state_key=state_key,
        results_date=results_date,
        history_date=history_date,
        profile=profile,
        experiment_tag=experiment_tag,
        sharepacks_root=sharepacks_root,
        contains_winners_artifacts=contains_winners_artifacts,
        repo_root=repo_root,
        top_items=top_items,
    )
    vtrac_tool, vtrac_inputs, vtrac_status = _build_vtrac_tool_payload(
        day_dir=day_dir,
        state_dir=state_dir,
        state_key=state_key,
        repo_root=repo_root,
        top_indices=max(12, top_items),
        top_straights=max(12, top_items),
        top_sections=6,
    )
    hot_tool, hot_inputs, hot_status = _build_hot_zones_tool_payload(
        day_dir=day_dir,
        state_dir=state_dir,
        state_key=state_key,
        results_date=results_date,
        repo_root=repo_root,
        top_lanes=max(12, top_items),
        top_per_lane=max(12, top_items),
    )
    stable_survivor_context = _build_stable_survivor_context(stable_tool)
    r_consensus_context = _build_r_consensus_context(stable_tool)

    cross_tool_relations = _build_cross_tool_relations(
        stable_tool=stable_tool,
        stable_survivor_context=stable_survivor_context,
        r_consensus_context=r_consensus_context,
        dr_tool=dr_tool,
        vtrac_tool=vtrac_tool,
        hot_tool=hot_tool,
        aux_tool=aux_tool,
    )
    arena_synthesis = _build_arena_synthesis(
        cross_tool_relations=cross_tool_relations,
        stable_survivor_context=stable_survivor_context,
        r_consensus_context=r_consensus_context,
    )
    downstream_handoff, downstream_inputs = _build_downstream_handoff(state_dir, repo_root)
    review_links, review_inputs = _build_review_links(day_dir=day_dir, state_dir=state_dir, state_key=state_key, repo_root=repo_root)

    evidence_inputs = [
        *stable_inputs,
        *dr_inputs,
        *aux_inputs,
        *vtrac_inputs,
        *hot_inputs,
        *downstream_inputs,
        *review_inputs,
    ]
    unique_inputs: List[Path] = []
    seen = set()
    for path in evidence_inputs:
        key = str(path.resolve())
        if key in seen:
            continue
        seen.add(key)
        unique_inputs.append(path)

    metadata = {
        "generated_at": _now_utc_iso(),
        "results_date": results_date,
        "history_date": history_date,
        "profile": profile,
        "experiment_tag": experiment_tag,
        "state_key": state_key,
        "sharepack_root": _safe_rel(sharepacks_root, repo_root),
        "sharepack_state_dir": _safe_rel(state_dir, repo_root),
        "contains_winners_artifacts": contains_winners_artifacts,
    }
    provenance = {
        "inputs_hash": _hash_inputs(unique_inputs),
        "evidence_paths": [_safe_rel(path, repo_root) for path in unique_inputs],
        "source_status": {
            "stable": stable_status,
            "digit_reduction": dr_status,
            "vtrac_analyzer": vtrac_status,
            "hot_zones": hot_status,
            "aux_control_center": aux_status,
        },
        "contract_refs": [
            "docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_FINAL_STRING_TOOL_OUTPUTS__ANALYSIS_ARENA_FEED.md",
            "docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_FINAL_CONTEXT_TOOL_OUTPUTS__ANALYSIS_ARENA_FEED.md",
            "docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_Analyzer_Lean_Outputs.md",
            "docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_AGGREGATED_ANALYSIS_ARENA_CONTRACT_v0.md",
        ],
    }

    return {
        "schema_version": "aggregated_analysis_arena_v0",
        "metadata": metadata,
        "provenance": provenance,
        "string_tools": {
            "stable": stable_tool,
            "digit_reduction": dr_tool,
            "vtrac_analyzer": vtrac_tool,
            "hot_zones": hot_tool,
        },
        "context_tools": {
            "aux_control_center": aux_tool,
        },
        "cross_tool_relations": cross_tool_relations,
        "arena_synthesis": arena_synthesis,
        "downstream_handoff": downstream_handoff,
        "review_links": review_links,
    }


def build_aggregated_analysis_arena_markdown(payload: Dict[str, Any]) -> str:
    metadata = payload.get("metadata") if isinstance(payload.get("metadata"), dict) else {}
    synthesis = payload.get("arena_synthesis") if isinstance(payload.get("arena_synthesis"), dict) else {}
    relations = payload.get("cross_tool_relations") if isinstance(payload.get("cross_tool_relations"), dict) else {}
    provenance = payload.get("provenance") if isinstance(payload.get("provenance"), dict) else {}
    string_tools = payload.get("string_tools") if isinstance(payload.get("string_tools"), dict) else {}

    lines: List[str] = []
    lines.append(
        f"# Aggregated Analysis Arena — {metadata.get('state_key', '?')} — D={metadata.get('results_date', '?')} ({metadata.get('profile', '?')})"
    )
    lines.append("")
    lines.append("Purpose: preserve all major string-tool and context-tool evidence in one reviewable, budget-blind state snapshot.")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- schema_version: `{payload.get('schema_version', '')}`")
    lines.append(f"- history_date: `{metadata.get('history_date') or '-'}`")
    lines.append(f"- experiment_tag: `{metadata.get('experiment_tag') or '-'}`")
    lines.append(f"- contains_winners_artifacts: `{metadata.get('contains_winners_artifacts')}`")
    lines.append(f"- inputs_hash: `{str(provenance.get('inputs_hash') or '')[:16]}`")

    source_status = provenance.get("source_status") if isinstance(provenance.get("source_status"), dict) else {}
    if source_status:
        lines.append("")
        lines.append("## Source Status")
        lines.append("")
        lines.append("| Source | Available | Mode | Path |")
        lines.append("|---|---|---|---|")
        for key in ("stable", "digit_reduction", "vtrac_analyzer", "hot_zones", "aux_control_center"):
            row = source_status.get(key) if isinstance(source_status.get(key), dict) else {}
            lines.append(
                f"| {key} | {row.get('available', False)} | {row.get('source_mode', '-')} | {row.get('source_path') or '-'} |"
            )

    lines.append("")
    lines.append("## Dominant Canonicals")
    lines.append("")
    lines.append("| Canonical | Support | String | Context | Score Total | Examples |")
    lines.append("|---|---:|---:|---:|---:|---|")
    for item in (synthesis.get("dominant_canonicals") or [])[:12]:
        examples = ", ".join(item.get("example_literals") or []) or "-"
        lines.append(
            f"| {item.get('value')} | {item.get('support_count')} | {item.get('string_source_count')} | {item.get('context_source_count')} | {item.get('score_total')} | {examples} |"
        )

    lines.append("")
    lines.append("## Dominant VTRAC Indices")
    lines.append("")
    lines.append("| Index | Support | String | Context | Score Total | Examples |")
    lines.append("|---|---:|---:|---:|---:|---|")
    for item in (synthesis.get("dominant_vtrac_indices") or [])[:12]:
        examples = ", ".join(item.get("example_literals") or []) or "-"
        lines.append(
            f"| {item.get('value')} | {item.get('support_count')} | {item.get('string_source_count')} | {item.get('context_source_count')} | {item.get('score_total')} | {examples} |"
        )

    watchlist = synthesis.get("vtrac_literal_watchlist") if isinstance(synthesis.get("vtrac_literal_watchlist"), list) else []
    if watchlist:
        lines.append("")
        lines.append("## VTRAC Literal Watchlist")
        lines.append("")
        lines.append("| Index | Rank | Support | String | Context | Canonicals | Examples | Split |")
        lines.append("|---|---:|---:|---:|---:|---|---|---|")
        for item in watchlist[:10]:
            canonicals = ", ".join(item.get("candidate_canonicals") or []) or "-"
            examples = ", ".join(item.get("example_literals") or []) or "-"
            split = "Y" if item.get("dominant_canonical_split") else "N"
            lines.append(
                f"| {item.get('vtrac_index')} | {item.get('rank')} | {item.get('support_count')} | {item.get('string_source_count')} | {item.get('context_source_count')} | {canonicals} | {examples} | {split} |"
            )

    vtrac_tool = string_tools.get("vtrac_analyzer") if isinstance(string_tools.get("vtrac_analyzer"), dict) else {}
    vtrac_objects = vtrac_tool.get("arena_objects") if isinstance(vtrac_tool.get("arena_objects"), dict) else {}
    ordered_lanes = vtrac_objects.get("ordered_lane_corridors") if isinstance(vtrac_objects.get("ordered_lane_corridors"), list) else []
    boxed_corridors = vtrac_objects.get("boxed_index_corridors") if isinstance(vtrac_objects.get("boxed_index_corridors"), list) else []
    if vtrac_objects.get("available") and (ordered_lanes or boxed_corridors):
        lines.append("")
        lines.append("## VTRAC Corridor Objects")
        lines.append("")
        lines.append("Predictive-safe ordered-lane and boxed-corridor summaries derived from VTRAC Enhanced; these are evidence inventory objects, not final prediction weights.")
        lines.append("")
        lines.append("| Ordered VCode | Boxed Index | Score Total | Witnesses | Top Witnesses |")
        lines.append("|---|---:|---:|---:|---|")
        for item in ordered_lanes[:10]:
            witnesses = ", ".join(row.get("straight") or "" for row in (item.get("top_witness_straights") or [])[:5] if isinstance(row, dict)) or "-"
            lines.append(
                f"| {item.get('ordered_vcode')} | {item.get('boxed_vtrac_index')} | {item.get('score_total')} | {item.get('witness_count')} | {witnesses} |"
            )
        lines.append("")
        lines.append("| Boxed Index | Score Total | Lane Count Present | Present Ordered VCodes | Top Witnesses |")
        lines.append("|---|---:|---:|---|---|")
        for item in boxed_corridors[:10]:
            vcodes = ", ".join(item.get("ordered_vcodes_present") or []) or "-"
            witnesses = ", ".join(row.get("straight") or "" for row in (item.get("top_witness_straights") or [])[:5] if isinstance(row, dict)) or "-"
            lines.append(
                f"| {item.get('boxed_vtrac_index')} | {item.get('score_total')} | {item.get('ordered_lane_count_present')} | {vcodes} | {witnesses} |"
            )

    lines.append("")
    lines.append("## Dominant Families")
    lines.append("")
    lines.append("| Family | Support | Score Total |")
    lines.append("|---|---:|---:|")
    for item in (synthesis.get("dominant_families") or [])[:10]:
        lines.append(f"| {item.get('value')} | {item.get('support_count')} | {item.get('score_total')} |")

    lines.append("")
    lines.append("## Regime")
    lines.append("")
    lines.append(f"- regime_flags: `{', '.join(relations.get('regime_flags') or []) or '-'}`")
    lines.append(f"- contradiction_flags: `{', '.join(relations.get('contradiction_flags') or []) or '-'}`")
    state_regime = synthesis.get("state_regime") if isinstance(synthesis.get("state_regime"), dict) else {}
    if state_regime:
        lines.append(f"- dominant_canonical: `{state_regime.get('dominant_canonical') or '-'}`")
        lines.append(f"- dominant_vtrac_index: `{state_regime.get('dominant_vtrac_index') or '-'}`")
        lines.append(f"- dominant_family: `{state_regime.get('dominant_family') or '-'}`")
        lines.append(f"- double_heavy: `{state_regime.get('double_heavy')}`")
        lines.append(f"- context_reinforced: `{state_regime.get('context_reinforced')}`")
        lines.append(f"- vtrac_alignment: `{state_regime.get('vtrac_alignment')}`")
        lines.append(f"- tail_consensus_present: `{state_regime.get('tail_consensus_present')}`")
        lines.append(f"- tail_consensus_value: `{state_regime.get('tail_consensus_value') or '-'}`")
        lines.append(f"- tail_consensus_column: `{state_regime.get('tail_consensus_column') or '-'}`")
        lines.append(f"- consensus_strength_class: `{state_regime.get('consensus_strength_class') or '-'}`")
        lines.append(f"- consensus_trial_eligible: `{state_regime.get('consensus_trial_eligible')}`")
        lines.append(f"- survivor_pressure: `{state_regime.get('survivor_pressure')}`")
        lines.append(f"- survivor_progression: `{state_regime.get('survivor_progression')}`")
        lines.append(f"- last_remaining: `{state_regime.get('last_remaining')}`")
        lines.append(f"- hidden_terminal_support: `{state_regime.get('hidden_terminal_support')}`")

    stable_survivor_context = synthesis.get("stable_survivor_context") if isinstance(synthesis.get("stable_survivor_context"), dict) else {}
    if stable_survivor_context.get("available"):
        lines.append("")
        lines.append("## Stable Survivor Context")
        lines.append("")
        lines.append(f"- frontier_count: `{stable_survivor_context.get('frontier_count', 0)}`")
        lines.append(f"- progression_count: `{stable_survivor_context.get('progression_count', 0)}`")
        lines.append(f"- last_remaining_rows: `{stable_survivor_context.get('last_remaining_rows', 0)}`")
        lines.append(f"- hidden_terminal_frontier_count: `{stable_survivor_context.get('hidden_terminal_frontier_count', 0)}`")
        top_frontier_canonicals = ", ".join(stable_survivor_context.get("top_frontier_canonicals") or []) or "-"
        top_last_remaining_canonicals = ", ".join(stable_survivor_context.get("top_last_remaining_canonicals") or []) or "-"
        top_frontier_vtrac = ", ".join(stable_survivor_context.get("top_frontier_vtrac_indices") or []) or "-"
        lines.append(f"- top_frontier_canonicals: `{top_frontier_canonicals}`")
        lines.append(f"- top_last_remaining_canonicals: `{top_last_remaining_canonicals}`")
        lines.append(f"- top_frontier_vtrac_indices: `{top_frontier_vtrac}`")
        profile_counts = stable_survivor_context.get("last_remaining_profile_counts") if isinstance(stable_survivor_context.get("last_remaining_profile_counts"), dict) else {}
        if profile_counts:
            lines.append(f"- last_remaining_profile_counts: `{json.dumps(profile_counts, sort_keys=True)}`")

    r_consensus_context = synthesis.get("r_consensus_context") if isinstance(synthesis.get("r_consensus_context"), dict) else {}
    if r_consensus_context.get("available"):
        lines.append("")
        lines.append("## R-Consensus Context")
        lines.append("")
        lines.append(f"- event_count: `{r_consensus_context.get('event_count', 0)}`")
        lines.append(f"- single_digit_count: `{r_consensus_context.get('single_digit_count', 0)}`")
        lines.append(f"- two_digit_count: `{r_consensus_context.get('two_digit_count', 0)}`")
        lines.append(f"- col1/col2: `{r_consensus_context.get('col1_count', 0)}/{r_consensus_context.get('col2_count', 0)}`")
        lines.append(f"- signal_strength_class: `{r_consensus_context.get('signal_strength_class', '-')}`")
        lines.append(f"- trial_eligible: `{r_consensus_context.get('trial_eligible')}`")
        lines.append(f"- top_tail_values: `{', '.join(r_consensus_context.get('top_tail_values') or []) or '-'}`")
        lines.append(f"- cross_variant_tail_values: `{', '.join(r_consensus_context.get('cross_variant_tail_values') or []) or '-'}`")
        lines.append(f"- top_support_canonicals: `{', '.join(r_consensus_context.get('top_support_canonicals') or []) or '-'}`")
        lines.append(f"- top_support_vtrac_indices: `{', '.join(r_consensus_context.get('top_support_vtrac_indices') or []) or '-'}`")

    lines.append("")
    lines.append("## Review Prompts")
    lines.append("")
    for prompt in (synthesis.get("review_prompts") or [])[:10]:
        lines.append(f"- {prompt}")

    handoff = payload.get("downstream_handoff") if isinstance(payload.get("downstream_handoff"), dict) else {}
    if handoff:
        lines.append("")
        lines.append("## Downstream Handoff")
        lines.append("")
        cu = handoff.get("candidate_universe") if isinstance(handoff.get("candidate_universe"), dict) else {}
        pc = handoff.get("play_card") if isinstance(handoff.get("play_card"), dict) else {}
        lines.append(f"- candidate_universe: `{cu.get('path') or '-'}` | combos=`{cu.get('union_combos_count') or 0}` | packs=`{cu.get('pack_count') or 0}`")
        lines.append(f"- play_card: `{pc.get('path') or '-'}` | ranked=`{pc.get('ranked_candidate_count') or 0}`")
        strategy_names = pc.get("strategy_names") if isinstance(pc.get("strategy_names"), list) else []
        if strategy_names:
            lines.append(f"- play_card_strategies: `{', '.join(strategy_names[:12])}`")

    review_links = payload.get("review_links") if isinstance(payload.get("review_links"), dict) else {}
    if review_links:
        lines.append("")
        lines.append("## Review Links")
        lines.append("")
        lines.append(f"- signals_bundle: `{review_links.get('signals_bundle_path') or '-'}`")
        lines.append(f"- winners_dir: `{review_links.get('winners_dir') or '-'}`")
        winners_files = review_links.get("winners_files") if isinstance(review_links.get("winners_files"), list) else []
        if winners_files:
            for path in winners_files[:10]:
                lines.append(f"- winner_file: `{path}`")

    return "\n".join(lines).rstrip() + "\n"


def write_aggregated_analysis_arena_files(
    *,
    out_json_path: Path,
    payload: Dict[str, Any],
    write_md: bool = True,
) -> Tuple[Path, Optional[Path]]:
    out_json_path.parent.mkdir(parents=True, exist_ok=True)
    out_json_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    md_path: Optional[Path] = None
    if write_md:
        md_path = out_json_path.with_suffix(".md")
        md_path.write_text(build_aggregated_analysis_arena_markdown(payload), encoding="utf-8")
    return out_json_path, md_path


def _default_out_name(profile: str, experiment_tag: str) -> str:
    if experiment_tag:
        return f"aggregated_analysis_arena__{profile}__{experiment_tag}.json"
    return f"aggregated_analysis_arena__{profile}.json"


def main(argv: Optional[Sequence[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Build aggregated analysis arena artifacts for frozen sharepacks.")
    ap.add_argument("--sharepacks-root", default="sharepacks/_predictive")
    ap.add_argument("--date", required=True)
    ap.add_argument("--states", nargs="*", default=[])
    ap.add_argument("--profile", default="tool_only")
    ap.add_argument("--experiment-tag", default="arena_v0")
    ap.add_argument("--history-date")
    ap.add_argument("--top-items", type=int, default=12)
    ap.add_argument("--no-md", action="store_true")
    args = ap.parse_args(argv)

    sharepacks_root = Path(args.sharepacks_root)
    if not sharepacks_root.is_absolute():
        sharepacks_root = (REPO_ROOT / sharepacks_root).resolve()
    day_dir = sharepacks_root / args.date
    if not day_dir.exists():
        raise SystemExit(f"Day directory not found: {day_dir}")

    day_meta = _load_day_meta(day_dir)
    history_date = _infer_history_date(day_dir, args.history_date)
    states = _resolve_states(day_dir, args.states, day_meta)
    if not states:
        raise SystemExit(f"No states found under {day_dir}")

    for state_key in states:
        state_dir = day_dir / state_key
        if not state_dir.exists():
            print(f"[skip] missing state dir: {state_dir}")
            continue
        payload = build_aggregated_analysis_arena_payload(
            day_dir=day_dir,
            state_key=state_key,
            results_date=args.date,
            history_date=history_date,
            profile=args.profile,
            experiment_tag=args.experiment_tag,
            sharepacks_root=sharepacks_root,
            repo_root=REPO_ROOT,
            top_items=int(args.top_items),
        )
        out_json = state_dir / "analysis" / _default_out_name(args.profile, args.experiment_tag)
        arena_json, arena_md = write_aggregated_analysis_arena_files(
            out_json_path=out_json,
            payload=payload,
            write_md=not args.no_md,
        )
        print(f"[ok] {state_key} -> {_safe_rel(arena_json)}")
        if arena_md is not None:
            print(f"     md -> {_safe_rel(arena_md)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
