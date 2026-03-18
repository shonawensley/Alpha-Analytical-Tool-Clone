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
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from modules.vtrac_reference import get_vtrac_index
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


def _build_cross_tool_relations(
    *,
    stable_tool: Dict[str, Any],
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
        "regime_flags": regime_flags,
        "contradiction_flags": contradiction_flags,
    }


def _build_arena_synthesis(
    *,
    cross_tool_relations: Dict[str, Any],
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
        "vtrac_alignment": "cross_tool_vtrac_alignment" in regime_flags,
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

    return {
        "dominant_canonicals": dominant_canonicals,
        "dominant_vtrac_indices": dominant_vtrac_indices,
        "dominant_families": dominant_families,
        "vtrac_literal_watchlist": vtrac_literal_watchlist,
        "context_reinforced_canonicals": context_reinforced_canonicals,
        "context_only_pressure": context_only_pressure,
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

    cross_tool_relations = _build_cross_tool_relations(
        stable_tool=stable_tool,
        dr_tool=dr_tool,
        vtrac_tool=vtrac_tool,
        hot_tool=hot_tool,
        aux_tool=aux_tool,
    )
    arena_synthesis = _build_arena_synthesis(cross_tool_relations=cross_tool_relations)
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
