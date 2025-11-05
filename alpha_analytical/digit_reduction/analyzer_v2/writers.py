from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Iterable, List

from .features import ItemFeature
from .io import write_csv, write_json
from .stacked import write_stacked_html


def write_artifacts(
    out_dir: Path,
    state: str,
    per_item: List[Dict[str, Any]],
    top_rows: List[Dict[str, Any]],
    meta: Dict[str, Any],
    diagnostics_config: Dict[str, Any],
    feature_entries: Iterable[ItemFeature],
    cfg: Dict[str, Any],
) -> None:
    per_item_path = out_dir / f"{state}_analyzer_v2_per_item.csv"
    top_path = out_dir / f"{state}_analyzer_v2_top_candidates.csv"
    meta_path = out_dir / f"{state}_analyzer_v2_meta.json"

    write_csv(per_item_path, per_item)
    write_csv(top_path, top_rows)
    write_json(meta_path, meta)

    if diagnostics_config.get("write_feature_distributions"):
        dist_path = out_dir / f"{state}_analyzer_v2_feature_detail.json"
        write_json(dist_path, [entry.detail for entry in feature_entries])

    if cfg.get("outputs", {}).get("write_stacked_html", True):
        variants = sorted({row.get("section") for row in per_item if row.get("section")})
        for variant in variants:
            write_stacked_html(out_dir, state, per_item, variant, top_rows)
