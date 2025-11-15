# long_string_reducer_part2.py
"""Run-time orchestrator + HTML writer for the Digit-Reduction / Long-String module.

USAGE (from project root):
    python long_string_reducer_part2.py --json data/big_table.json
    # OR
    python long_string_reducer_part2.py --csv_dir tables/

It will read the required R2 strings (Area 1 & Area 2),
run the four reduction methods (A-D) in both draw modes (own / combined),
generate a full HTML report under outputs/ and optionally a JSON dump.

Part 1 (long_string_reducer_part1.py) must be importable.
"""

from __future__ import annotations
import argparse
import datetime
import json
import os
from pathlib import Path
from typing import List, Dict, Tuple, Optional

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
from .long_string_reducer_part1 import run_reduction_progression  # exposed by part-1

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

AREA1_DISPLAY_COLS = ("col7", "col6", "col5", "col4", "col2")
AREA1_DISPLAY_LABEL = " / ".join(col.replace("col", "") for col in AREA1_DISPLAY_COLS)
AREA1_DISPLAY_COLS_NUM = tuple(int(col.replace("col", "")) for col in AREA1_DISPLAY_COLS)

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
        label = STEP_LABEL.get(idx, idx)          # 0 -> "Orig", else number
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
        for col in AREA1_DISPLAY_COLS_NUM:
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
    out.append(f'<h3>Long-String 1 (columns {AREA1_DISPLAY_LABEL})</h3>')
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

def build_full_html(
    results_area1: List[Dict],
    results_area2: List[Dict],
    draw_heads: Dict[str, str] = None,
    view_mode: str = "tabbed",
) -> str:
    """Render the reductions report.

    view_mode:
      - "tabbed"  (default) shows a navbar to toggle method/mode sections
      - "stacked" shows all sections one after another for easy scrolling
    """
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
    # Override CSS for stacked mode (no tabs, show all sections)
    if str(view_mode).lower() == "stacked":
        css += "\n#methodNav{display:none}\nsection.method{display:block}\n"

    parts = ["<html><head><meta charset='utf-8'><style>", css, "</style></head><body>"]
    # Navbar only for tabbed mode
    if str(view_mode).lower() == "tabbed":
        parts.append('<nav id="methodNav">')
        for meth, md in COLUMNS_ORDER:
            sec_id = f"{meth}-{md}"
            label = f"{meth}-{md}"
            active = ' class="active"' if sec_id == "A-own" else ''
            parts.append(f'<button data-target="{sec_id}"{active}>{label}</button>')
        parts.append('</nav>')
        # Tab JS to toggle sections
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
    for meth, md in COLUMNS_ORDER:
        sec_id = f"{meth}-{md}"
        parts.append(f'<section class="method" id="{sec_id}">')
        parts.append(f'<h2>Method {meth} - {md}</h2>')
        # LONG-STRING 1  (col7/6/5/4/2)
        ls1 = [
            c
            for c in results_area1
            if any(c["location_id"].endswith(col) for col in AREA1_DISPLAY_COLS)
        ]
        parts.append(f'<h3>Long-String 1  (columns {AREA1_DISPLAY_LABEL})</h3>')
        parts.append(grid_block(ls1, list(AREA1_DISPLAY_COLS), sec_id))
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
# Public wrapper for Streamlit / external usage
# ---------------------------------------------------------------------------

# Helper to build the nested big_data structure from any *combined.csv files, even if prefixed with state name

def _load_big_data_from_tables(csv_dir: Path) -> dict:
    """Flexibly load *_combined.csv tables inside `csv_dir` into the nested dict structure
    expected by the reduction algorithms. Handles filenames that include the state prefix
    (e.g. `Connecticut4_Midday_combined.csv`)."""
    import pandas as pd  # local import to avoid top-level dependency if unused

    big: dict = {"sections": {}}

    for fp in csv_dir.glob("*_combined.csv"):
        try:
            df = pd.read_csv(fp, dtype=str).fillna("")
        except Exception:
            continue  # skip unreadable file

        fname_lower = fp.name.lower()
        if "midday" in fname_lower:
            section = "Midday"
        elif "evening" in fname_lower:
            section = "Evening"
        else:
            section = "Combined"

        sect_node = big["sections"].setdefault(section, {"sets": {}})

        for _, row in df.iterrows():
            # -------- normalise & sanity-clean -------------------------
            set_name  = str(row.get("Set",  "") or "").strip()
            draw_name = str(row.get("Draw", "") or "").strip()
            row_type  = str(row.get("RowType", "") or "").strip().upper()
            if not (set_name and draw_name and row_type):
                continue

            # Accept mixed-case / dashes
            if row_type in {"DRAW_DATA", "DRAW"}:
                row_type = "DRAW_DATA"
            elif row_type.replace("-", "") == "R2":
                row_type = "R2"

            col_values = {str(c): str(row.get(str(c), "")).strip()
                          for c in ["7","6","5","4","3","2","1"]}
            # -----------------------------------------------------------

            draw_node = (
                sect_node["sets"]
                .setdefault(set_name, {})
                .setdefault("draws", {})
                .setdefault(draw_name, {"pattern_variations": {}, "draw_data": {}})
            )

            if row_type == "DRAW_DATA":
                draw_node["draw_data"] = col_values
            else:            # R2, R3, ...
                draw_node["pattern_variations"].setdefault(row_type, col_values)

    return big


def _build_score_df(results_area1: List[Dict], results_area2: List[Dict]):
    """Flatten analysed cell logs into a tidy DataFrame."""
    import pandas as pd

    rows = []
    for cell in results_area1 + results_area2:
        loc = cell["location_id"]
        for (meth, mode), log in cell["variation_logs"].items():
            final_val = log[-1] if log else ""
            rows.append({
                "Location": loc,
                "Method": meth,
                "Mode": mode,
                "Final": final_val,
                "Steps": len(log),
            })
    return pd.DataFrame(rows)


def run_digit_reduction(
    state: str,
    tables_path: Path,
    out_path: Path | str | None = None,
    *,
    min_occ: int = 3,
) -> tuple["pd.DataFrame", str, str]:
    """Wrapper exposing the digit-reduction engine to other modules (e.g. Streamlit).

    Parameters
    ----------
    state : str
        State identifier (e.g. "Connecticut4") - only used for naming outputs.
    tables_path : Path
        Directory containing the *_combined.csv tables for that state.
    out_path : Path | str | None, optional
        Destination folder for artefacts. Defaults to
        data/outputs/analysis/digit_reduction/<STATE>/.
    min_occ : int, optional
        Reserved for future use (kept for API symmetry with stable-pattern wrapper).

    Returns
    -------
    df_scores : pandas.DataFrame
    html_path : str - absolute path to generated HTML report
    csv_path  : str - absolute path to generated CSV file ("" if no data)
    """
    import pandas as pd  # local import

    tables_path = Path(tables_path)
    if not tables_path.exists():
        return pd.DataFrame(), "", ""

    if out_path is None:
        out_path = Path("data/outputs/analysis/digit_reduction") / state
    out_path = Path(out_path)
    out_path.mkdir(parents=True, exist_ok=True)

    # --------------------------------------------------------
    # Build big_data structure the analyser expects
    # --------------------------------------------------------
    big_data = _load_big_data_from_tables(tables_path)
    if not big_data.get("sections"):
        return pd.DataFrame(), "", ""

    # --------------------------------------------------------
    # Gather R2 strings (Area-1 & Area-2) and analyse
    # --------------------------------------------------------
    area1_cells, area2_cells = [], []
    for sec in SECTION_NAMES:
        if "sections" not in big_data or sec not in big_data["sections"]:
            continue
        for loc_id, s in extract_r2_strings_area1(big_data, sec).items():
            parts = loc_id.split("|")
            area1_cells.append({
                "location_id": loc_id,
                "original_string": s,
                "metadata": {"section": parts[0], "set": parts[1], "draw": parts[2], "col": parts[3] if len(parts)>3 else ""},
            })
        for loc_id, s in extract_r2_strings_area2(big_data, sec).items():
            parts = loc_id.split("|")
            area2_cells.append({
                "location_id": loc_id,
                "original_string": s,
                "metadata": {"section": parts[0], "set": parts[1], "draw": parts[2], "col": parts[3] if len(parts)>3 else ""},
            })

    analysed_area1 = analyse_area(area1_cells, big_data)
    analysed_area2 = analyse_area(area2_cells, big_data)

    # --------------------------------------------------------
    # Build latest-draw map for header validation
    # --------------------------------------------------------
    draw_heads: Dict[str, str] = {}
    for sec in SECTION_NAMES:
        try:
            dd = big_data["sections"][sec]["sets"]["Set1"]["draws"]["Draw1"].get("draw_data", {})
            latest = next((dd.get(str(c)) for c in ("1","2","3","4","5","6","7") if dd.get(str(c))), "")
            draw_heads[sec] = latest
        except Exception:
            continue

    # --------------------------------------------------------
    # Write HTML reports (tabbed + stacked)
    # --------------------------------------------------------
    html_content = build_full_html(analysed_area1, analysed_area2, draw_heads, view_mode="tabbed")
    html_path = out_path / f"{state}_digit_reduction_report.html"
    html_path.write_text(html_content, encoding="utf-8")

    try:
        html_content_stacked = build_full_html(analysed_area1, analysed_area2, draw_heads, view_mode="stacked")
        (out_path / f"{state}_digit_reduction_report_stacked.html").write_text(html_content_stacked, encoding="utf-8")
    except Exception:
        # If for any reason the stacked build fails, continue with the tabbed report only
        pass

    # --------------------------------------------------------
    # Training-friendly exports (CSV steps + JSON logs)
    # --------------------------------------------------------
    try:
        train_dir = out_path / "training"
        train_dir.mkdir(parents=True, exist_ok=True)

        rows: List[Dict] = []
        items: List[Dict] = []

        def _to_int(s: str, default: int = 0) -> int:
            try:
                return int(s)
            except Exception:
                return default

        def _col_num_from_label(col_label: str) -> int:
            # expects formats like "col7", "col3", else returns 0
            try:
                if isinstance(col_label, str) and col_label.startswith("col"):
                    return int(col_label.replace("col", "").strip())
            except Exception:
                pass
            return 0

        SECTION_RANK = {"Midday": 1, "Evening": 2, "Combined": 3}
        SET_RANK = {"Set1": 1, "Set2": 2, "Set3": 3}

        def _add_area(area_label: str, analysed_cells: List[Dict]) -> None:
            for cell in analysed_cells:
                meta = cell.get("metadata", {})
                loc = cell.get("location_id", "")
                vlogs = cell.get("variation_logs", {}) or {}
                for (meth, md), log in vlogs.items():
                    # Build raw steps with features
                    raw_steps: List[Dict] = []
                    for idx, val in enumerate(log):
                        sval = str(val or "")
                        length = len(sval)
                        unique_digits = len(set(sval)) if sval else 0
                        is_3value = (unique_digits <= 3 and sval != "")
                        raw_steps.append({
                            "step": idx,
                            "value": sval,
                            "length": length,
                            "unique_digits": unique_digits,
                            "is_3value": bool(is_3value),
                        })

                    # Determine last change step (trim terminal repeats only)
                    last_change_step = 0
                    for i in range(1, len(raw_steps)):
                        if raw_steps[i]["value"] != raw_steps[i-1]["value"]:
                            last_change_step = i

                    first_3value_step = -1
                    for s in raw_steps:
                        if s["is_3value"]:
                            first_3value_step = s["step"]
                            break

                    # Determine terminal start: first step reaching small/low-variance state
                    # Terminal is defined as length <= 3 OR unique_digits <= 2 (includes empty string)
                    first_terminal_idx = -1
                    for s in raw_steps:
                        if s["length"] <= 3 or s["unique_digits"] <= 2:
                            first_terminal_idx = s["step"]
                            break

                    steps_total_before_compaction = len(raw_steps)
                    kept: List[Dict] = []
                    if not raw_steps:
                        kept = []
                    else:
                        if first_terminal_idx == -1:
                            # No terminal; keep up to last change
                            kept = raw_steps[: last_change_step + 1]
                        else:
                            # Keep everything up to the first terminal step (inclusive)
                            kept = raw_steps[: first_terminal_idx + 1]
                            # After terminal: allow at most one exact duplicate per distinct value
                            # and keep later change steps (also allowing one duplicate for each new value)
                            allowed_dups_per_value = 1
                            dup_count_for_current = 0
                            for j in range(first_terminal_idx + 1, last_change_step + 1):
                                s = raw_steps[j]
                                if kept and s["value"] == kept[-1]["value"]:
                                    if dup_count_for_current < allowed_dups_per_value:
                                        kept.append(s)
                                        dup_count_for_current += 1
                                    else:
                                        # skip further identical terminal repeats
                                        continue
                                else:
                                    kept.append(s)
                                    dup_count_for_current = 0
                    steps_kept_after_compaction = len(kept)

                    # Structural anchors / ranks for AI mapping
                    section = str(meta.get("section", ""))
                    set_name = str(meta.get("set", ""))
                    draw_name = str(meta.get("draw", ""))
                    col_label = str(meta.get("col", ""))
                    col_num = _col_num_from_label(col_label)

                    grid_position = {
                        "area_rank": 1 if area_label == "LS1" else 2,
                        "section_rank": SECTION_RANK.get(section, 0),
                        "set_rank": SET_RANK.get(set_name, 0),
                        "draw_rank": _to_int(draw_name.replace("Draw", ""), 0) if draw_name else 0,
                        "col_rank": col_num,
                    }

                    # Emit CSV rows for kept steps only
                    for s in kept:
                        rows.append({
                            "state": state,
                            "area": area_label,
                            "section": section,
                            "set": set_name,
                            "draw": draw_name,
                            "col": col_num,
                            "col_label": col_label,
                            "location": loc,
                            "method": meth,
                            "mode": md,
                            "area_rank": grid_position["area_rank"],
                            "section_rank": grid_position["section_rank"],
                            "set_rank": grid_position["set_rank"],
                            "draw_rank": grid_position["draw_rank"],
                            "col_rank": grid_position["col_rank"],
                            "step": s["step"],
                            "value": s["value"],
                            "length": s["length"],
                            "unique_digits": s["unique_digits"],
                            "is_3value": s["is_3value"],
                            "first_3value_step": first_3value_step,
                            "last_change_step": last_change_step,
                            "steps_total_before_compaction": steps_total_before_compaction,
                            "steps_kept_after_compaction": steps_kept_after_compaction,
                        })

                    final_obj = kept[-1] if kept else {"value": "", "length": 0, "unique_digits": 0, "is_3value": False}

                    items.append({
                        "state": state,
                        "area": area_label,
                        "section": section,
                        "set": set_name,
                        "draw": draw_name,
                        "col": col_num,
                        "col_label": col_label,
                        "location": loc,
                        "method": meth,
                        "mode": md,
                        "grid_position": grid_position,
                        "sequence_meta": {
                            "first_3value_step": first_3value_step,
                            "last_change_step": last_change_step,
                            "steps_total_before_compaction": steps_total_before_compaction,
                            "steps_kept_after_compaction": steps_kept_after_compaction,
                        },
                        "steps": kept,
                        "final": {
                            "value": final_obj.get("value", ""),
                            "length": final_obj.get("length", 0),
                            "unique_digits": final_obj.get("unique_digits", 0),
                            "is_3value": final_obj.get("is_3value", False),
                        },
                    })

        _add_area("LS1", analysed_area1)
        _add_area("LS2", analysed_area2)

        # CSV (steps)
        try:
            import pandas as pd  # type: ignore
            steps_csv_path = train_dir / f"{state}_digit_reduction_steps.csv"
            df_steps = pd.DataFrame(rows)
            if not df_steps.empty:
                df_steps.to_csv(steps_csv_path, index=False)
        except Exception:
            pass

        # JSON (logs) with guidance (JSON has no native comments, so we embed guidance fields)
    except Exception:
        # Training exports are optional; failures must not block the main report
        pass

    # --------------------------------------------------------
    # Build & persist score DataFrame
    # --------------------------------------------------------
    df_scores = _build_score_df(analysed_area1, analysed_area2)
    csv_path = out_path / f"{state}_digit_reduction_scores.csv"
    if not df_scores.empty:
        df_scores.to_csv(csv_path, index=False)
        csv_path_str: str = str(csv_path)
    else:
        csv_path_str = ""

    return df_scores, str(html_path), csv_path_str

# Re-export for convenience
try:
    import pandas as pd  # noqa: F401 - re-export check
except ModuleNotFoundError:
    pass

__all__ = [
    # existing exports ... (implicitly) add new symbol
    "run_digit_reduction",
]

# ---------------------------------------------------------------------------
# Command-line interface
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Run Digit-Reduction module and build HTML report.")
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
            # col1 is newest -> if it exists grab it, else first non-empty col
            latest = next((dd.get(str(c)) for c in ("1","2","3","4","5","6","7") if dd.get(str(c))), "")
            draw_heads[sec] = latest

    # --- build and dump HTML ---------------------------------------------
    html = build_full_html(analysed_area1, analysed_area2, draw_heads)
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    args.out.mkdir(parents=True, exist_ok=True)
    html_path = args.out / f"digit_reduction_{ts}.html"
    html_path.write_text(html, encoding="utf-8")
    print(f"[OK] HTML report written to {html_path}")

    # Optional JSON snapshot (comment-in if desired)
    # json_path = args.out / f"digit_reduction_{ts}.json"
    # json_path.write_text(json.dumps({"area1": analysed_area1, "area2": analysed_area2}, indent=2))


if __name__ == "__main__":
    main() 
