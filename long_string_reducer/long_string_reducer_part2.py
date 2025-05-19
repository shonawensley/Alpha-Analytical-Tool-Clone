# long_string_reducer_part2.py
"""Run‑time orchestrator + HTML writer for the Digit‑Reduction / Long‑String module.

USAGE (from project root):
    python long_string_reducer_part2.py --json data/big_table.json
    # OR
    python long_string_reducer_part2.py --csv_dir tables/

It will read the required R2 strings (Area 1 & Area 2),
run the four reduction methods (A–D) in both draw modes (own / combined),
generate a full HTML report under outputs/ and optionally a JSON dump.

Part 1 (long_string_reducer_part1.py) must be importable.
"""

from __future__ import annotations
import argparse
import datetime
import json
import os
from pathlib import Path
from typing import List, Dict, Tuple

# --- local imports ---------------------------------------------------------
from long_string_reducer_part1 import (
    load_csv_directory,
    extract_r2_strings_area1,
    extract_r2_strings_area2,
    get_draw_lists_for_section,
    MIRROR_MAP,
    method_a,
    method_b,
    method_c,
    method_d,
    SECTION_NAMES,
)
from long_string_reducer_part1 import run_reduction_progression  # exposed by part‑1

METHOD_FUNCS = {
    "A": method_a,
    "B": method_b,
    "C": method_c,
    "D": method_d,
}

COLUMNS_ORDER: List[Tuple[str, str]] = [
    ("A", "own"), ("B", "own"), ("C", "own"), ("D", "own"),
    ("A", "combined"), ("B", "combined"), ("C", "combined"), ("D", "combined"),
]

# ---------------------------------------------------------------------------
# HTML helpers
# ---------------------------------------------------------------------------

def _html_escape(txt: str) -> str:
    return (txt.replace("&", "&amp;")
               .replace("<", "&lt;")
               .replace(">", "&gt;"))


def build_html_for_cell(location_id: str, variation_logs: Dict[Tuple[str, str], List[str]]) -> str:
    """Single table per R2 string (location)."""
    max_rows = max(len(v) for v in variation_logs.values())
    lines: List[str] = []
    lines.append(f"<h3>{_html_escape(location_id)}</h3>")
    lines.append("<table class='cell'>")
    # header ------------------------------------------------
    lines.append("<tr><th>Step</th>" + "".join(f"<th>{m}-{md}</th>" for m, md in COLUMNS_ORDER) + "</tr>")

    # rows --------------------------------------------------
    for idx in range(max_rows):
        row_cells = [f"<td class='step'>{idx}</td>"]
        for key in COLUMNS_ORDER:
            step_log = variation_logs.get(key, [])
            val = step_log[idx] if idx < len(step_log) else ""
            row_cells.append(f"<td>{_html_escape(val)}</td>")
        lines.append("<tr>" + "".join(row_cells) + "</tr>")

    lines.append("</table>")
    return "\n".join(lines)


def build_full_html(results_area1: List[Dict], results_area2: List[Dict], draw_heads: Dict[str, str] = None) -> str:
    """Pretty 3-column layout:
         ┌────────────── Long-String 1 ───────────────┐
         │ Midday │ Evening │ Combined (each a column)│
         └─────────────────────────────────────────────┘
       Same again for Long-String 2.
       Optionally a small DRAW_DATA summary on top.
    """
    css = """
    body{font-family:Arial,Helvetica,sans-serif}
    table{border-collapse:collapse;font-size:12px;margin:6px 0}
    th,td{border:1px solid #bbb;padding:3px 4px}
    td.step{font-weight:bold;background:#f7f7f7}
    .grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
    h3{margin:4px 0 6px}
    """
    parts = ["<html><head><meta charset='utf-8'><style>", css, "</style></head><body>",
             "<h1>Digit-Reduction / Long-String Report</h1>"]

    # ---- optional DRAW_DATA header ---------------------------------
    if draw_heads:
        parts.append("<h2>Latest draw triples (validation)</h2>")
        parts.append("<table><tr><th>Section</th><th>Latest draw</th></tr>")
        for sec, trip in draw_heads.items():
            parts.append(f"<tr><td>{sec}</td><td>{trip}</td></tr>")
        parts.append("</table>")

    # ---- Long-String 1 (Area-1) ------------------------------------
    parts.append("<h2>Long-String 1  •  columns 7 / 6 / 5</h2>")
    parts.append('<div class="grid">')
    for sec in ("Midday","Evening","Combined"):
        parts.append(f"<div><h3>{sec}</h3>")
        # pick the three tables that belong to this section & keep order col7 -> col6 -> col5
        for col in (7,6,5):
            for cell in results_area1:
                if cell["location_id"].startswith(f"{sec}") and f"col{col}" in cell["location_id"]:
                    parts.append(build_html_for_cell(cell["location_id"], cell["variation_logs"]))
        parts.append("</div>")
    parts.append("</div>")   # /grid

    # ---- Long-String 2 (Area-2) ------------------------------------
    parts.append("<h2>Long-String 2  •  Set 1 [Draw-4 col 3, Draw-6 col 1]</h2>")
    parts.append('<div class="grid">')
    for sec in ("Midday","Evening","Combined"):
        parts.append(f"<div><h3>{sec}</h3>")
        # only two cells per section → Draw4-col3 first, then Draw6-col1
        draw_order = ("Draw4|col3", "Draw6|col1")
        for frag in draw_order:
            for cell in results_area2:
                if cell["location_id"].startswith(f"{sec}") and frag in cell["location_id"]:
                    parts.append(build_html_for_cell(cell["location_id"], cell["variation_logs"]))
        parts.append("</div>")
    parts.append("</div>")   # /grid

    parts.append("</body></html>")
    return "\n".join(parts)

# ---------------------------------------------------------------------------
# Analysis driver
# ---------------------------------------------------------------------------

def analyse_area(cells: List[Dict], big_data: dict) -> List[Dict]:
    """Run 8 variations for every R2 string cell."""
    analysed: List[Dict] = []
    for cell in cells:
        loc_id = cell["location_id"]
        original = cell["original_string"] or ""
        section = cell["metadata"].get("section", "Midday")

        draw_lists = get_draw_lists_for_section(big_data, section)
        variation_logs: Dict[Tuple[str, str], List[str]] = {}
        for meth_label, func in METHOD_FUNCS.items():
            for mode in ("own", "combined"):
                draws = draw_lists[mode]
                variation_logs[(meth_label, mode)] = run_reduction_progression(original, draws, func)

        analysed.append({
            "location_id": loc_id,
            "variation_logs": variation_logs,
        })
    return analysed

# ---------------------------------------------------------------------------
# Command‑line interface
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Run Digit‑Reduction module and build HTML report.")
    g = parser.add_mutually_exclusive_group(required=True)
    g.add_argument("--json", type=Path, help="Path to the big lottery JSON file")
    g.add_argument("--csv_dir", type=Path, help="Path to the directory containing CSV tables")
    parser.add_argument("--out", type=Path, default=Path("outputs"), help="Output directory for reports")
    args = parser.parse_args()

    # --- load data ---------------------------------------------------------
    if args.json:
        print("[ERROR] --json option is not supported as load_big_lottery_json is not implemented in long_string_reducer_part1.py")
        return
    elif args.csv_dir:
        big_data = load_csv_directory(args.csv_dir)
    else:
        print("[ERROR] Either --json or --csv_dir must be provided.")
        parser.print_help()
        return

    # --- gather R2 strings -------------------------------------------------
    area1_cells, area2_cells = [], []

    for sec in SECTION_NAMES:                      # Midday / Evening / Combined
        # Ensure the big_data structure has the section before trying to iterate
        if "sections" in big_data and sec in big_data["sections"]:
            # Call the extraction functions for each section
            for loc_id, s in extract_r2_strings_area1(big_data, sec).items():
                area1_cells.append({
                    "location_id": loc_id,
                    "original_string": s,
                    "metadata": {"section": sec} # Include section metadata
                })
            for loc_id, s in extract_r2_strings_area2(big_data, sec).items():
                area2_cells.append({
                    "location_id": loc_id,
                    "original_string": s,
                    "metadata": {"section": sec} # Include section metadata
                })

    # --- run analyses ------------------------------------------------------
    analysed_area1 = analyse_area(area1_cells, big_data)
    analysed_area2 = analyse_area(area2_cells, big_data)

    # --- collect latest draw triples for validation header -----------------
    draw_heads = {}
    for sec in SECTION_NAMES:
        if (sec in big_data["sections"] and 
            "Set1" in big_data["sections"][sec]["sets"] and 
            "Draw1" in big_data["sections"][sec]["sets"]["Set1"]["draws"]):
            dd = big_data["sections"][sec]["sets"]["Set1"]["draws"]["Draw1"].get("draw_data", {})
            # col1 is newest → if it exists grab it, else first non-empty col
            latest = next((dd.get(str(c)) for c in ("1","2","3","4","5","6","7") if dd.get(str(c))), "")
            draw_heads[sec] = latest

    # --- build and dump HTML ---------------------------------------------
    html = build_full_html(analysed_area1, analysed_area2, draw_heads)
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    args.out.mkdir(parents=True, exist_ok=True)
    html_path = args.out / f"digit_reduction_{ts}.html"
    html_path.write_text(html, encoding="utf-8")
    print(f"[✓] HTML report written to {html_path}")

    # Optional JSON snapshot (comment‑in if desired)
    # json_path = args.out / f"digit_reduction_{ts}.json"
    # json_path.write_text(json.dumps({"area1": analysed_area1, "area2": analysed_area2}, indent=2))


if __name__ == "__main__":
    main() 