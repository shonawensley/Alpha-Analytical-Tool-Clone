from pathlib import Path
from typing import Dict, Any, List
from .io import write_csv, write_json

def write_artifacts(outdir: Path,
                    per_item: List[Dict[str, Any]],
                    top: List[Dict[str, Any]],
                    loc_summary: List[Dict[str, Any]],
                    meta: Dict[str, Any],
                    state: str):
    write_csv(outdir / f"{state}_analyzer_v2_features.csv", per_item)
    write_csv(outdir / f"{state}_analyzer_v2_top_candidates.csv", top)
    write_csv(outdir / f"{state}_analyzer_v2_location_summary.csv", loc_summary)
    write_json(outdir / f"{state}_analyzer_v2_meta.json", meta)
