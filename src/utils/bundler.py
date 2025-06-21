"""
Light-weight helper that glues one day's predictions + winners into a single
JSON bundle an ML script can read later.
"""

import json
from pathlib import Path

def bundle_day(state: str,
               date_str: str,
               pred_path: Path,
               winners_path: Path,
               out_dir: Path | str = "data/outputs/bundles") -> Path:
    """
    Combine the two existing JSON files into
    data/outputs/bundles/<state>_<date>_bundle.json

    Returns the bundle Path (so callers can show a link in the UI).
    """
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    bundle = {
        "date": date_str,
        "state": state,
        "predictions": json.load(open(pred_path, "r")),
        "winners":     json.load(open(winners_path, "r"))
    }

    bundle_path = out_dir / f"{state}_{date_str}_bundle.json"
    with open(bundle_path, "w") as f:
        json.dump(bundle, f, indent=2)

    return bundle_path 