# modules/winner_report_full.py
from __future__ import annotations
from pathlib import Path
import re
import pandas as pd

from modules.vtrac_straight_map import VSTRAIGHTS

# ---- Paths
def winners_vtrac_dir(date_str: str, state_name: str) -> Path:
    return Path("data") / "outputs" / "winners" / date_str / "vtrac_reports" / state_name

def state_tables_dir(state_name: str) -> Path:
    # If you already have utils.path_handler.get_state_tables_dir, prefer it.
    try:
        from utils.path_handler import get_state_tables_dir
        return Path(get_state_tables_dir(state_name))
    except Exception:
        return Path("data") / "outputs" / "tables" / state_name

# ---- Load combined tables (Midday / Evening / Combined)
def load_combined_tables(state_name: str) -> dict[str, pd.DataFrame]:
    base = state_tables_dir(state_name)
    files = {
        "Midday":   base / f"{state_name}_Midday_combined.csv",
        "Evening":  base / f"{state_name}_Evening_combined.csv",
        "Combined": base / f"{state_name}_Combined_combined.csv",
    }
    tables: dict[str, pd.DataFrame] = {}
    for k, p in files.items():
        if p.exists():
            tables[k] = pd.read_csv(p, dtype=str).fillna("")
    return tables

# ---- V‑Trac mapping helpers
def get_index_and_patterns(winner: str) -> tuple[int, dict]:
    w = str(winner).strip().zfill(3)
    # Preferred: same reference the analyzer uses
    try:
        from modules.vtrac_reference import get_vtrac_index, VTRAC_DISPLAY
        idx = int(get_vtrac_index(w))
        singles, doubles = [], []
        for row in VTRAC_DISPLAY:
            if int(row.get("Index", -1)) == idx:
                singles = row.get("Singles", []) or []
                doubles = row.get("Doubles", []) or []
                break
        return idx, {"Singles": singles, "Doubles": doubles}
    except Exception:
        # Fallback if names differ
        from src.core.module_c_vtrac import find_vtrac_index_and_combos
        idx, combos = find_vtrac_index_and_combos(w)
        return int(idx), combos

def vtrac_straights_for(winner: str) -> list[str]:
    w = str(winner).strip().zfill(3)
    for code, combos in VSTRAIGHTS.items():
        if w in combos:
            return combos[:]
    return []

# ---- Overlay green straights in the analyzer HTML
def _inject_straight_highlight(html: str, straights: list[str]) -> str:
    if not straights:
        return html
    css = (
        "<style>"
        ".straight{background:#d8f5d6;color:#0b7a0b;font-weight:600;"
        "border-radius:3px;padding:0 2px}"
        "</style>"
    )
    if "</head>" in html:
        html = html.replace("</head>", css + "</head>")
    else:
        html = css + html

    # replace bare 3‑digit tokens with <span class="straight">...</span>
    for s in sorted(set(straights), reverse=True):
        patt = rf'(?<!\d){re.escape(s)}(?!\d)'
        html = re.sub(patt, f'<span class="straight">{s}</span>', html)
    return html

# ---- Public entry: full analyzer‑style report for a winner
def write_winner_full_report(state_name: str, date_str: str, winner: str) -> str:
    tables = load_combined_tables(state_name)
    idx, patterns = get_index_and_patterns(winner)
    straights = vtrac_straights_for(winner)

    # Prefer the analyzer's renderer so layout matches exactly
    try:
        from src.core.module_c_vtrac import generate_index_html_report
        html = generate_index_html_report(
            state_name=state_name,
            index=idx,
            patterns=patterns,    # {"Singles":[...], "Doubles":[...]}
            tables=tables,        # dict with "Midday"/"Evening"/"Combined" -> DataFrame
            score=0,
            rank=0,
        )
    except Exception:
        # Minimal fallback (never used if analyzer generator is present)
        singles = " ".join(patterns.get("Singles", []))
        doubles = " ".join(patterns.get("Doubles", []))
        html = f"""<!doctype html><html><head><meta charset="utf-8"><title>{state_name} WIN index {idx}</title></head>
<body><h1>{state_name} — WIN index {idx}</h1>
<p><strong>Winning:</strong> {str(winner).zfill(3)}</p>
<h2>Singles</h2><p>{singles}</p><h2>Doubles</h2><p>{doubles}</p></body></html>"""

    html = _inject_straight_highlight(html, straights)

    out_dir = winners_vtrac_dir(date_str, state_name)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{state_name}_vtrac_WIN_index_{idx}_{date_str.replace('-','')}.html"
    out_path.write_text(html, encoding="utf-8")
    return str(out_path)