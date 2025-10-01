from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import yaml

from .features import compute_features_union
from .io import analyzer_out_dir, load_training_json, training_dir_for_state
from .pivot import cross_section_pivot, cross_col_agree, methods_consensus, own_vs_combined, set_memory
from .score import score_row
from .types import Item
from .vtrac_index import VHotSpec, derive_hot_families_from_dr, try_load_hot_families_from_predictions, vtrac_set
from .writers import write_artifacts

SectionKey = Tuple[str, str, str, str, str, int, str, str]
MethodKey = Tuple[str, str, str, str, str, int, str]


def _as_int(value: Any) -> int:
    try:
        if isinstance(value, str):
            value = value.strip()
            if not value:
                return 0
        return int(value)
    except (TypeError, ValueError):
        try:
            return int(float(value))
        except (TypeError, ValueError):
            return 0


def _section_key_from_item(item: Item) -> SectionKey:
    return (
        item.key.state,
        item.key.area,
        item.key.section,
        item.key.set,
        item.key.draw,
        item.key.col,
        item.key.method,
        item.key.mode,
    )


def _section_key_from_row(row: Dict[str, Any]) -> SectionKey:
    return (
        str(row.get("state", "")),
        str(row.get("area", "")),
        str(row.get("section", "")),
        str(row.get("set", "")),
        str(row.get("draw", "")),
        _as_int(row.get("col", 0)),
        str(row.get("method", "")),
        str(row.get("mode", "")),
    )


def _cross_section_key(row: Dict[str, Any]) -> Tuple[str, str, str, str, int, str, str]:
    return (
        str(row.get("state", "")),
        str(row.get("area", "")),
        str(row.get("set", "")),
        str(row.get("draw", "")),
        _as_int(row.get("col", 0)),
        str(row.get("method", "")),
        str(row.get("mode", "")),
    )


def _method_key(row: Dict[str, Any]) -> MethodKey:
    return (
        str(row.get("state", "")),
        str(row.get("area", "")),
        str(row.get("section", "")),
        str(row.get("set", "")),
        str(row.get("draw", "")),
        _as_int(row.get("col", 0)),
        str(row.get("mode", "")),
    )


def _top_candidates(per_item_rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    aggregator: Dict[str, Dict[str, Any]] = {}
    for row in per_item_rows:
        canon = str(row.get("final.canon3", ""))
        if not canon:
            continue
        entry = aggregator.setdefault(
            canon,
            {
                "final.canon3": canon,
                "score_sum": 0.0,
                "hits": 0,
                "sections": set(),
                "methods": set(),
            },
        )
        entry["score_sum"] += float(row.get("score", 0.0))
        entry["hits"] += 1
        entry["sections"].add(row.get("section"))
        entry["methods"].add(row.get("method"))
    board: List[Dict[str, Any]] = []
    for entry in aggregator.values():
        board.append(
            {
                "final.canon3": entry["final.canon3"],
                "score_sum": round(entry["score_sum"], 2),
                "hits": entry["hits"],
                "sections": len(entry["sections"]),
                "methods": len(entry["methods"]),
            }
        )
    board.sort(key=lambda r: (-float(r["score_sum"]), -r["hits"]))
    return board[:200]


def _prepare_vhot(state: str, cfg_paths: Dict[str, Any], per_item_rows: List[Dict[str, Any]]) -> VHotSpec:
    predictions_dir = Path(cfg_paths.get("vtrac_predictions_dir", "data/outputs/predictions"))
    spec = try_load_hot_families_from_predictions(state, predictions_dir)
    if spec is not None:
        return spec
    return derive_hot_families_from_dr(per_item_rows, min_methods=2, prefer_section="Combined", top_k=5)


def run(state: str, analysis_root: Optional[Path | str] = None) -> Dict[str, Any]:
    cfg_path = Path(__file__).parent / "config.yml"
    cfg = yaml.safe_load(cfg_path.read_text(encoding="utf-8"))
    thresholds = cfg.get("thresholds", {})
    weights = cfg.get("weights", {})
    penalties = cfg.get("penalties", {})
    caps = cfg.get("caps", {})
    paths_cfg = cfg.get("paths", {})

    root_path: Optional[Path] = Path(analysis_root) if analysis_root is not None else None
    training_dir_for_state(state, root_path)  # raises if missing
    items, source_path = load_training_json(state, root_path)
    if not items:
        raise ValueError(f"No training items available for state {state}")

    per_item_rows: List[Dict[str, Any]] = []
    for item in items:
        row: Dict[str, Any] = {
            "state": item.key.state,
            "area": item.key.area,
            "section": item.key.section,
            "set": item.key.set,
            "draw": item.key.draw,
            "col": item.key.col,
            "method": item.key.method,
            "mode": item.key.mode,
        }
        row.update(compute_features_union(item, thresholds))
        per_item_rows.append(row)

    cross_section = cross_section_pivot(items)
    own_features, delta_rows = own_vs_combined(items)
    set_features = set_memory(items)
    xcol_features = cross_col_agree(items)
    method_features = methods_consensus(items, int(thresholds.get("early_step_k", 3)))

    for row in per_item_rows:
        key = _section_key_from_row(row)
        row.update(cross_section.get(_cross_section_key(row), {}))
        row.update(own_features.get(key, {}))
        row.update(set_features.get(key, {}))
        row.update(xcol_features.get(key, {}))
        row.update(method_features.get(_method_key(row), {}))
        row.setdefault("mode.only_one", 0)
        row.setdefault("mode.agree_core", 0)
        row.setdefault("mode.time_to3_delta_abs", 0)
        row.setdefault("mode.len_delta_abs", 0)
        row.setdefault("set.memory_strength", 0)
        row.setdefault("set.repeat_new_box", 0)
        row.setdefault("set.linger", 0)
        row.setdefault("xcol.agree_count", 0)
        row.setdefault("methods.core_agreement", 0)
        row.setdefault("methods.early_fraction", 0.0)
        row.setdefault("method.agree_count", 0)

    hot_spec = _prepare_vhot(state, paths_cfg, per_item_rows)
    fam_strength = hot_spec.detail or {}
    for row in per_item_rows:
        canon = str(row.get("final.canon3", ""))
        vset = vtrac_set(canon) if canon else ""
        row["vtrac.set"] = vset
        row["vtrac.v_hot"] = float(fam_strength.get(vset, 0.0))
        row["vtrac.hot_source"] = hot_spec.source

    for row in per_item_rows:
        row["score"] = score_row(row, weights, penalties, caps, thresholds)

    top_rows = _top_candidates(per_item_rows)
    out_dir = analyzer_out_dir(state, root_path)
    meta = {
        "state": state,
        "config_version": cfg.get("version", 0),
        "items": len(per_item_rows),
        "source": str(source_path),
        "thresholds": thresholds,
        "weights": weights,
        "penalties": penalties,
        "vtrac_hot_source": hot_spec.source,
        "vtrac_hot_families": sorted(hot_spec.families),
    }

    write_artifacts(out_dir, state, per_item_rows, delta_rows, top_rows, meta)

    return {
        "state": state,
        "rows": len(per_item_rows),
        "out_dir": str(out_dir),
        "artifacts": [
            f"{state}_analyzer_v2_per_item.csv",
            f"{state}_analyzer_v2_own_vs_combined_delta.csv",
            f"{state}_analyzer_v2_top_candidates.csv",
            f"{state}_analyzer_v2_meta.json",
        ],
        "config_version": cfg.get("version", 0),
    }