from pathlib import Path
from typing import Any, Dict, List

from .io import write_csv, write_json


def write_artifacts(
    outdir: Path,
    state: str,
    per_item: List[Dict[str, Any]],
    delta_rows: List[Dict[str, Any]],
    top_rows: List[Dict[str, Any]],
    meta: Dict[str, Any],
) -> None:
    write_csv(outdir / f"{state}_analyzer_v2_per_item.csv", per_item)
    write_csv(outdir / f"{state}_analyzer_v2_own_vs_combined_delta.csv", delta_rows)
    write_csv(outdir / f"{state}_analyzer_v2_top_candidates.csv", top_rows)
    write_json(outdir / f"{state}_analyzer_v2_meta.json", meta)