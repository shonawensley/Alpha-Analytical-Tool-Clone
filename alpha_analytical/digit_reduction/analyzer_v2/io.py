from __future__ import annotations
import json, csv
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
from .types import Item, Step, Key

def _safe_int(value: Any, default: int = 0) -> int:
    try:
        if isinstance(value, str):
            value = value.strip()
            if not value:
                return default
        return int(value)
    except (TypeError, ValueError):
        try:
            return int(float(value))
        except (TypeError, ValueError):
            return default


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
        root = analysis_root if analysis_root is not None else Path("data/outputs/analysis/digit_reduction")
        base = Path(root) / state
    training = Path(base) / "training"
    training.mkdir(parents=True, exist_ok=True)
    return training

def analyzer_out_dir(state: str, analysis_root: Optional[Path] = None) -> Path:
    """
    data/outputs/analysis/digit_reduction/<STATE>/analyzer_v2
    """
    ph = _prefer_path_handler()
    if ph and hasattr(ph, "get_analysis_dir"):
        base = Path(ph.get_analysis_dir("digit_reduction", state))
    else:
        root = analysis_root if analysis_root is not None else Path("data/outputs/analysis/digit_reduction")
        base = Path(root) / state
    out = Path(base) / "analyzer_v2"
    out.mkdir(parents=True, exist_ok=True)
    return out

def _load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))

def load_training_json(state: str, analysis_root: Optional[Path] = None) -> Tuple[List[Item], Path]:
    tdir = training_dir_for_state(state, analysis_root)
    patterns = [
        f"{state}_digit_reduction_log*.json",
        f"*{state}*digit_reduction_log*.json",
        f"*{state}*digit_reduction_logs*.json",
    ]
    candidates = []
    for pattern in patterns:
        candidates.extend(tdir.glob(pattern))
    if not candidates:
        raise FileNotFoundError(f"No training JSON under {tdir}")
    candidates.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    unique = []
    seen = set()
    for cand in candidates:
        resolved = cand.resolve()
        if resolved in seen:
            continue
        unique.append(cand)
        seen.add(resolved)
    target = unique[0]
    data = _load_json(target)
    items: List[Item] = []
    for payload in data.get("items", []):
        key = Key(
            state=payload["state"],
            area=payload["area"],
            section=payload["section"],
            set=payload["set"],
            draw=payload["draw"],
            col=_safe_int(payload.get("col")),
            method=payload["method"],
            mode=payload["mode"],
        )
        steps = [Step(**step) for step in payload.get("steps", [])]
        items.append(
            Item(
                key=key,
                grid_position=payload.get("grid_position", {}),
                sequence_meta=payload.get("sequence_meta", {}),
                steps=steps,
                final=payload.get("final", {}),
            )
        )
    return items, target

def write_csv(path: Path, rows: List[Dict[str, Any]]):
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    columns = sorted({key for row in rows for key in row.keys()})
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

def write_json(path: Path, obj: Any):
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")