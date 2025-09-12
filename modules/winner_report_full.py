from __future__ import annotations

import os
import re
from datetime import datetime
from typing import Dict

from utils import path_handler as ph


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

    # Load tables via analyzer helper
    tables: Dict[str, object] | None = vtrac.load_state_data(state_name)
    if not tables:
        raise RuntimeError(f"No combined tables available for {state_name}")

    # Compute patterns for the index
    idx = vtrac.find_vtrac_index_and_combos(win)["index"] if hasattr(vtrac, "find_vtrac_index_and_combos") else None
    if idx is None:
        # Fallback: use helper that derives all combos for a numeric index
        from modules.vtrac_reference import get_vtrac_index
        idx = get_vtrac_index(win)
        get_all = getattr(vtrac, "get_all_combinations_for_index", None)
        patterns = set(get_all(idx)) if callable(get_all) else set()
    else:
        # Prefer analyzer helper that also supplies patterns
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

    # Resolve output path
    base = out_dir or ph.get_winners_output_dir()
    target = os.path.join(base, "vtrac_reports", state_name)
    os.makedirs(target, exist_ok=True)
    out_path = os.path.join(target, f"{state_name}_vtrac{idx}_winner_{win}_{ts}.html")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(html2)
    return out_path

