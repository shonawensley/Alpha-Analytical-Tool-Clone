from __future__ import annotations

import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict
import json

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def _ensure_canonical_utils() -> None:
    root = str(PROJECT_ROOT)
    if root in sys.path:
        try:
            sys.path.remove(root)
        except ValueError:
            pass
    sys.path.insert(0, root)
    src = str(PROJECT_ROOT / 'src')
    if src in sys.path:
        try:
            sys.path.remove(src)
        except ValueError:
            pass
    sys.path.insert(1, src)
    mod = sys.modules.get('utils')
    if not mod:
        return
    mod_path = str(getattr(mod, '__file__', '')).replace('\\', '/').lower()
    if '/src/utils/' not in mod_path:
        return
    targets = [name for name in list(sys.modules) if name == 'utils' or name.startswith('utils.')]
    for name in targets:
        sys.modules.pop(name, None)


_ensure_canonical_utils()

from utils import path_handler as ph
from utils.table_io import read_csv_strsafe


def write_winner_full_report(state: str, winner: str, out_dir: str | None = None) -> str:
    """
    Generate analyzer-style 3-pane string-tables HTML for the given winner.
    The renderer applies winner (green) and index-family (purple) highlights.

    Returns the output file path.
    """
    from core import module_c_vtrac as vtrac

    state_name = str(state or "").strip()
    win = (winner or "").strip()
    if len(win) != 3 or (not win.isdigit()):
        raise ValueError("Winning number must be a 3-digit string")

    # Load tables (string-safe) directly from tables dir
    tables_dir = os.path.join("data", "outputs", "tables", state_name)
    def _resolve_table(section: str) -> str | None:
        candidates = [
            os.path.join(tables_dir, f"{state_name}_{section}_combined.csv"),
            os.path.join(tables_dir, f"{section}_Combined.csv"),
            os.path.join(tables_dir, f"{section}_combined.csv"),
        ]
        for candidate in candidates:
            if os.path.exists(candidate):
                return candidate
        return None
    paths = {s: _resolve_table(s) for s in ("Midday", "Evening", "Combined")}
    missing = [k for k, p in paths.items() if not p]
    if missing:
        raise RuntimeError(f"Missing combined tables for {state_name}: {', '.join(missing)}")
    tables: Dict[str, object] = {
        "Midday_combined": read_csv_strsafe(paths["Midday"]),
        "Evening_combined": read_csv_strsafe(paths["Evening"]),
        "Combined_combined": read_csv_strsafe(paths["Combined"]),
    }

    # Compute patterns for the index via canonical reference
    from modules.vtrac_reference import get_vtrac_index
    idx = get_vtrac_index(win)
    get_all = getattr(vtrac, "get_all_combinations_for_index", None)
    patterns = set(get_all(idx)) if callable(get_all) else set()

    # Generate analyzer-style HTML
    gen = getattr(vtrac, "generate_index_html_report", None)
    gen_json = getattr(vtrac, "generate_index_json_report", None)
    if not callable(gen):
        raise RuntimeError("Analyzer HTML generator not available")
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    html = gen(state_name, idx, patterns, tables, score=0, rank=0, timestamp=ts, winner_combo=win)
    json_payload = gen_json(state_name, idx, patterns, tables, score=0, rank=0, timestamp=ts, winner_combo=win) if callable(gen_json) else None

    # Resolve output path under analysis/winners/<STATE>
    target = out_dir or ph.get_analysis_dir("winners", state_name)
    os.makedirs(target, exist_ok=True)
    out_path = os.path.join(target, f"{state_name}_vtrac{idx}_winner_{win}_{ts}.html")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(html)
    if json_payload is not None:
        json_path = os.path.join(target, f"{state_name}_vtrac{idx}_winner_{win}_{ts}.json")
        with open(json_path, "w", encoding="utf-8") as jh:
            json.dump(json_payload, jh, indent=2)
    return out_path
