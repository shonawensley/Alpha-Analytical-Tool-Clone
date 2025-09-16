from __future__ import annotations

import os
import re
from datetime import datetime
from typing import Dict

from utils import path_handler as ph
from utils.table_io import read_csv_strsafe


def _unique_straights(winner: str) -> set[str]:
    w = (winner or "").strip()
    if len(w) != 3 or (not w.isdigit()):
        return set()
    a, b, c = w[0], w[1], w[2]
    return {
        a + b + c,
        a + c + b,
        b + a + c,
        b + c + a,
        c + a + b,
        c + b + a,
    }


def _inject_green_overlay(html: str, straights: set[str]) -> str:
    if not html or not straights:
        return html
    # Ensure we add a small CSS class for green overlay
    style_block = (
        "\n<style>.hit-straight{background:#d6f5d6;color:#0a7a0a;"
        "font-weight:600;border-radius:3px;padding:0 2px;}</style>\n"
    )
    try:
        html = html.replace("</head>", style_block + "</head>")
    except Exception:
        # If head not found, just prefix
        html = style_block + html

    # Replace occurrences of the straight combos as standalone 3-digit tokens
    def wrap_token(match: re.Match) -> str:
        tok = match.group(0)
        if tok in straights:
            return f'<span class="hit-straight">{tok}</span>'
        return tok

    pattern = re.compile(r"(?<!\d)(\d{3})(?!\d)")
    return pattern.sub(wrap_token, html)


def write_winner_full_report(state: str, winner: str, out_dir: str | None = None) -> str:
    """
    Generate analyzer-style 3-pane string-tables HTML for the given winner:
    - Uses the same renderer as the V-TRAC analyzer
    - Adds a green overlay for winner straight permutations

    Returns the output file path.
    """
    from core import module_c_vtrac as vtrac

    state_name = str(state or "").strip()
    win = (winner or "").strip()
    if len(win) != 3 or (not win.isdigit()):
        raise ValueError("Winning number must be a 3-digit string")

    # Load tables (string-safe) directly from tables dir
    tables_dir = os.path.join("data", "outputs", "tables", state_name)
    def _p(section: str) -> str:
        return os.path.join(tables_dir, f"{state_name}_{section}_combined.csv")
    paths = {s: _p(s) for s in ("Midday", "Evening", "Combined")}
    if not all(os.path.exists(p) for p in paths.values()):
        missing = [k for k, p in paths.items() if not os.path.exists(p)]
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
    if not callable(gen):
        raise RuntimeError("Analyzer HTML generator not available")
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    html = gen(state_name, idx, patterns, tables, score=0, rank=0, timestamp=ts)

    # Overlay winner straights in green
    html2 = _inject_green_overlay(html, _unique_straights(win))

    # Resolve output path under analysis/winners/<STATE>
    target = out_dir or ph.get_analysis_dir("winners", state_name)
    os.makedirs(target, exist_ok=True)
    out_path = os.path.join(target, f"{state_name}_vtrac{idx}_winner_{win}_{ts}.html")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(html2)
    return out_path
