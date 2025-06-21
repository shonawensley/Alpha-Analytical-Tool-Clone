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
from .long_string_reducer_part1 import (
    load_csv_directory,
    extract_r2_strings_area1,
    extract_r2_strings_area2,
    get_draw_lists_for_section,
    MIRROR_MAP,
    method_a,
    method_b,
    method_c,
    method_d,
    method_e,
    method_t,
    SECTION_NAMES,
)
from .long_string_reducer_part1 import run_reduction_progression  # exposed by part‑1

METHOD_FUNCS = {
    "A": method_a,
    "B": method_b,
    "C": method_c,
    "D": method_d,
    "E": method_e,
    "T": method_t,
}

COLUMNS_ORDER: List[Tuple[str, str]] = [
    ("A", "own"), ("B", "own"), ("C", "own"), ("D", "own"), ("E", "own"), ("T", "own"),
    ("A", "combined"), ("B", "combined"), ("C", "combined"), ("D", "combined"), ("E", "combined"), ("T", "combined"),
]

STEP_LABEL = {0: "Orig"}  # row-header text; 0 = original string

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
        label = STEP_LABEL.get(idx, idx)          # 0 → "Orig", else number
        row_cells = [f"<td class='step'>{label}</td>"]
        for key in COLUMNS_ORDER:
            step_log = variation_logs.get(key, [])
            val = step_log[idx] if idx < len(step_log) else ""
            row_cells.append(f"<td>{_html_escape(val)}</td>")
        lines.append("<tr>" + "".join(row_cells) + "</tr>")

    lines.append("</table>")
    return "\n".join(lines)


def build_latest_draw_table(draw_heads):
    rows = []
    for sec in ["Midday","Evening","Combined"]:
        latest = draw_heads.get(sec, "")
        rows.append(f'<tr><td>{sec}</td><td>{_html_escape(str(latest))}</td></tr>')
    return '<table><tr><th>Section</th><th>Latest draw</th></tr>' + ''.join(rows) + '</table>'


def side_by_side(cells, sec_id):
    # Render three tables (Midday, Evening, Combined) for the given method/mode
    out = []
    for sec in ("Midday","Evening","Combined"):
        for col in (7,6,5):
            for cell in cells:
                if cell["location_id"].startswith(f"{sec}") and f"col{col}" in cell["location_id"]:
                    # Only show the table for the current method/mode
                    table = build_html_for_cell_single(cell["location_id"], cell["variation_logs"], sec_id)
                    out.append(f'<div class="lsBox">{table}</div>')
    return out

def side_by_side_area2(cells, sec_id):
    # For area2, only two tables per section: Draw4|col3, Draw6|col1
    out = []
    for sec in ("Midday","Evening","Combined"):
        draw_order = ("Draw4|col3", "Draw6|col1")
        for frag in draw_order:
            for cell in cells:
                if cell["location_id"].startswith(f"{sec}") and frag in cell["location_id"]:
                    table = build_html_for_cell_single(cell["location_id"], cell["variation_logs"], sec_id)
                    out.append(f'<div class="lsBox">{table}</div>')
    return out

def build_html_for_cell_single(location_id: str, variation_logs: Dict, sec_id: str) -> str:
    # Only show the column for the current method/mode
    meth, mode = sec_id.split("-")
    key = (meth, mode)
    step_log = variation_logs.get(key, [])
    lines = [f"<h3>{_html_escape(location_id)}</h3>"]
    lines.append("<table class='cell'>")
    lines.append("<tr><th>Step</th><th>Val</th></tr>")
    for idx, val in enumerate(step_log):
        label = STEP_LABEL.get(idx, idx)
        lines.append(f"<tr><td class='step'>{label}</td><td>{_html_escape(val)}</td></tr>")
    lines.append("</table>")
    return "\n".join(lines)

def render_longstring_tables(area1_cells, area2_cells, sec_id):
    out = []
    out.append('<h3>Long-String 1 (columns 7/6/5)</h3>')
    out.extend(side_by_side(area1_cells, sec_id))
    out.append('<h3>Long-String 2 (Set1 Draw4 col3 & Draw6 col1)</h3>')
    out.extend(side_by_side_area2(area2_cells, sec_id))
    return "\n".join(out)

def minitable(cell, sec_id):
    meta = cell["metadata"]
    nice_lbl = f'{meta["section"][0]}-{meta["set"][-1]}.{meta["draw"][-1]}'
    key = tuple(sec_id.split("-"))  # ('A','own')
    log = cell["variation_logs"][key]
    rows = ['<caption class="miniCap">'+nice_lbl+'</caption>',
            '<tr><th class="step">#</th><th>Val</th></tr>']
    for i,v in enumerate(log):
        label = STEP_LABEL.get(i, i)
        rows.append(f'<tr><td class="step">{label}</td><td>{v}</td></tr>')
        if i>=7: break
    return '<table class="miniTbl">' + ''.join(rows) + '</table>'

def grid_block(cells, want_cols, sec_id):
    box = {}                             # {(set, draw, section, col): cell}
    for c in cells:
        m = c["metadata"]
        box[(m["set"], m["draw"], m["section"], m["col"])] = c

    lines = []
    for set_name in ["Set3","Set2","Set1"]:
        for draw in sorted({ d for (s,d,_,_) in box }):
            lines.append(f'<div class="rowHead">{set_name} {draw}</div>')
            lines.append('<div class="grid3">')
            for sec in ("Midday", "Evening", "Combined"):
                inner = ['<div class="lsStrip">']
                for want in want_cols:                      # use the list we received
                    cell = box.get((set_name, draw, sec, want))
                    if cell:
                        inner.append(f'<div class="mini">{minitable(cell, sec_id)}</div>')
                    else:
                        inner.append('<div class="mini"></div>')
                inner.append('</div>')      # lsStrip
                lines.append('<div class="lsBox">' + ''.join(inner) + '</div>')
            lines.append('</div>')   # grid3
    return "\n".join(lines)

def build_full_html(results_area1: List[Dict], results_area2: List[Dict], draw_heads: Dict[str, str] = None) -> str:
    """Tabbed layout: navbar for A-own, ..., D-combined. Each tab shows two big tables (Long-String 1 and 2), each as Midday | Evening | Combined."""
    css = """
    body{font-family:Arial,Helvetica,sans-serif}
    table{border-collapse:collapse;font-size:12px;margin:6px 0}
    th,td{border:1px solid #bbb;padding:3px 4px}
    td.step{font-weight:bold;background:#f7f7f7}
    .lsBox      {flex:1 1 0; min-width:160px; font-size:11px}
    .grid3      {display:flex; gap:8px; margin-bottom:10px;}
    .rowHead    {font-style:italic; margin-top:6px; font-size:12px}
    #methodNav { margin-bottom:14px }
    #methodNav button.active { background:#333;color:#fff }
    section.method { display:none }
    section.method:first-of-type { display:block }
    h3{margin:4px 0 6px}
    th.step,td.step{width:24px;text-align:center}
    .lsStrip  {display:flex; gap:4px; flex-wrap:wrap}
    .lsBox:not(:last-child){border-right:2px solid #aaa; padding-right:6px}
    .miniTbl  {font-size:10px}
    .miniCap  {font-size:9px; font-style:italic; text-align:left; padding:0 0 2px}
    .mini     {flex:1 1 0; min-width:110px}
    """
    parts = ["<html><head><meta charset='utf-8'><style>", css, "</style></head><body>"]
    # Navbar
    parts.append('<nav id="methodNav">')
    for meth, mode in COLUMNS_ORDER:
        sec_id = f"{meth}-{mode}"
        label = f"{meth}-{mode}"
        active = ' class="active"' if sec_id == "A-own" else ''
        parts.append(f'<button data-target="{sec_id}"{active}>{label}</button>')
    parts.append('</nav>')
    # JS
    parts.append("""
    <script>
      const btns = [...document.querySelectorAll('#methodNav button')];
      btns.forEach(btn => btn.onclick = () => {
        const tgt = btn.dataset.target;
        document.querySelectorAll('section.method').forEach(
            sec => sec.style.display = (sec.id === tgt) ? 'block' : 'none');
        btns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
      });
    </script>
    """)
    # Latest draw triples
    if draw_heads:
        parts.append('<h2>Latest draw triples (validation)</h2>')
        parts.append(build_latest_draw_table(draw_heads))
    # Tabbed sections
    for meth, mode in COLUMNS_ORDER:
        sec_id = f"{meth}-{mode}"
        parts.append(f'<section class="method" id="{sec_id}">')
        parts.append(f'<h2>Method {meth} – {mode}</h2>')
        # LONG-STRING 1  (cols 7/6/5)
        ls1 = [c for c in results_area1 if any(c["location_id"].endswith(f"col{x}") for x in (7,6,5))]
        parts.append('<h3>Long-String 1  (columns 7 / 6 / 5)</h3>')
        parts.append(grid_block(ls1, ['col7','col6','col5'], sec_id))
        # LONG-STRING 2  (Set1 Draw-4 col3  + Draw-6 col1)
        ls2 = [c for c in results_area2]  # already just those two columns
        parts.append('<h3>Long-String 2  (Set1 Draw-4 col-3  & Draw-6 col-1)</h3>')
        parts.append(grid_block(ls2, ['col3','col1'], sec_id))
        parts.append('</section>')
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
            "metadata": cell.get("metadata", {})
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
                # Parse loc_id: e.g. 'Midday|Set3|Draw1|col7'
                parts = loc_id.split("|")
                area1_cells.append({
                    "location_id": loc_id,
                    "original_string": s,
                    "metadata": {
                        "section": parts[0],
                        "set": parts[1],
                        "draw": parts[2],
                        "col": parts[3] if len(parts) > 3 else ""
                    }
                })
            for loc_id, s in extract_r2_strings_area2(big_data, sec).items():
                parts = loc_id.split("|")
                area2_cells.append({
                    "location_id": loc_id,
                    "original_string": s,
                    "metadata": {
                        "section": parts[0],
                        "set": parts[1],
                        "draw": parts[2],
                        "col": parts[3] if len(parts) > 3 else ""
                    }
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