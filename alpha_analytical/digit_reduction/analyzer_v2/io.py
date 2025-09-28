from __future__ import annotations
import json, csv
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
from .types import Item, Step, Key

def _prefer_path_handler():
    try:
        # Canonical SSOT for dirs in AAT9
        from utils import path_handler as ph  # lives inside repo
        return ph
    except Exception:
        return None

def training_dir_for_state(state: str, analysis_root: Optional[Path] = None) -> Path:
    """
    data/outputs/analysis/digit_reduction/<STATE>/training
    """
    ph = _prefer_path_handler()
    if ph and hasattr(ph, "get_analysis_dir"):
        base = Path(ph.get_analysis_dir("digit_reduction", state))
    else:
        base = (analysis_root or Path("data/outputs/analysis/digit_reduction") / state)
    return Path(base) / "training"

def analyzer_out_dir(state: str, analysis_root: Optional[Path] = None) -> Path:
    """
    data/outputs/analysis/digit_reduction/<STATE>/analyzer_v2
    """
    ph = _prefer_path_handler()
    if ph and hasattr(ph, "get_analysis_dir"):
        base = Path(ph.get_analysis_dir("digit_reduction", state))
    else:
        base = (analysis_root or Path("data/outputs/analysis/digit_reduction") / state)
    out = Path(base) / "analyzer_v2"
    out.mkdir(parents=True, exist_ok=True)
    return out

def _load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))

def load_training_json(state: str, analysis_root: Optional[Path] = None) -> List[Item]:
    tdir = training_dir_for_state(state, analysis_root)
    # canonical name like: <STATE>digit_reduction_logs.json
    f = None
    for cand in tdir.glob(f"*{state}*digit_reduction*logs*.json"):
        f = cand; break
    if f is None:
        raise FileNotFoundError(f"No training JSON under {tdir}")
    data = _load_json(f)
    items: List[Item] = []
    for it in data.get("items", []):
        key = Key(
            state=it["state"], area=it["area"], section=it["section"],
            set=it["set"], draw=it["draw"], col=int(it["col"]),
            method=it["method"], mode=it["mode"]
        )
        steps = [Step(**s) for s in it.get("steps", [])]
        items.append(Item(
            key=key,
            grid_position=it.get("grid_position", {}),
            sequence_meta=it.get("sequence_meta", {}),
            steps=steps,
            final=it.get("final", {})
        ))
    return items

def write_csv(path: Path, rows: List[Dict[str, Any]]):
    if not rows:
        path.write_text("", encoding="utf-8"); return
    cols = sorted({k for r in rows for k in r.keys()})
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in rows: w.writerow(r)

def write_json(path: Path, obj: Any):
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")
