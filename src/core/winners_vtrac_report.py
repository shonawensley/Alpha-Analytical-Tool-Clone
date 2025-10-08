from __future__ import annotations

import os
from datetime import datetime
from typing import List, Dict

from utils import path_handler as ph
from modules.vtrac_matchers import build_winner_targets, digits_only


def build_vtrac_winner_report(state: str, winner: str, tables_dir: str | None = None, out_dir: str | None = None) -> str:
    """
    Build a V‑Trac winner HTML report (3 sections side‑by‑side) highlighting:
    - Purple: all combos for the winner's index
    - Green: straight permutations of the winner

    Writes HTML under data/outputs/winners/<YYYY‑MM‑DD>/vtrac_reports/<STATE>/ and returns the path.
    """
    from modules.vtrac_reference import VTRAC_DISPLAY, get_vtrac_index  # lazy import

    idx = get_vtrac_index(winner)
    # Find the display entry for this index
    entry = next((e for e in VTRAC_DISPLAY if e.get("Index") == idx), None)
    if not entry:
        raise ValueError(f"V‑Trac index {idx} not found for winner {winner}")

    singles = entry.get("Singles", "").split()
    doubles = entry.get("Doubles", "").split()
    targets = build_winner_targets(winner, singles + doubles)
    straights = targets.straights

    # Minimal CSS for purple/green overlays
    css = """
    <style>
      .panel { width: 32%; display: inline-block; vertical-align: top; }
      .box   { border: 1px solid #ddd; padding: 8px; margin: 6px; border-radius: 4px; }
      .title { font-weight: 600; margin-bottom: 6px; }
      .combo { display: inline-block; margin: 2px 6px; font-family: monospace; }
      .hit-winner { background-color:#e1f7d5; color:#0b6b00; border:1px solid #74c476; border-radius:3px; padding:0 4px; font-weight:700; }
      .hit-family { background-color:#ede3ff; color:#4b0082; border:1px solid #b39ddb; border-radius:3px; padding:0 4px; font-weight:700; }
      .muted { opacity: .6; }
    </style>
    """

    def render_panel(section_name: str) -> str:
        items = []
        items.append(f'<div class="title">{section_name}</div>')
        # Singles row
        row_s = []
        for c in singles:
            token = digits_only(c)
            if token in targets.straights:
                cls = "hit-winner"
            elif token in targets.family:
                cls = "hit-family"
            else:
                cls = "muted"
            row_s.append(f'<span class="combo {cls}">{c}</span>')
        items.append('<div class="box">' + ''.join(row_s) + '</div>')
        # Doubles row
        row_d = []
        for c in doubles:
            token = digits_only(c)
            if token in targets.straights:
                cls = "hit-winner"
            elif token in targets.family:
                cls = "hit-family"
            else:
                cls = "muted"
            row_d.append(f'<span class="combo {cls}">{c}</span>')
        items.append('<div class="box">' + ''.join(row_d) + '</div>')
        return '<div class="panel">' + ''.join(items) + '</div>'

    header = f"<h3>V‑Trac Winner Report — {state} — Winner {winner} — Index {idx}</h3>"
    layout = render_panel("Midday") + render_panel("Evening") + render_panel("Combined")
    html = "<html><head><meta charset='utf-8'>" + css + "</head><body>" + header + layout + "</body></html>"

    # Resolve output directory (winners date bucket)
    base = out_dir or ph.get_winners_output_dir()
    target = os.path.join(base, "vtrac_reports", state)
    os.makedirs(target, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_path = os.path.join(target, f"{state}_vtrac{idx}_winner_{ts}.html")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(html)
    return out_path

