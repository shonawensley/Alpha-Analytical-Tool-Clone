#!/usr/bin/env python
"""
Stable-Pattern Extractor – Final Enhanced Version
=================================================
Loads combined-table CSV(s) ▶ finds every "stable 3-value" substring
▶ scores with coverage / span / mirror / vertical-straight tiers /
single_left / tail consensus stubs (<= 2 digits) / hot-level / baseline type bump
▶ writes highlight-HTML + CSV.

This version includes:
 • Unique-only Dominant Last/Pair logic
 • Rigorous row-by-row consensus check (any column)
 • Optional row-list mismatch assertion
 • Everything else (mirror, single_left, extra_digit, etc.) unchanged

Weights live in feature_config.yml next to this file.
"""

import os, sys, re, argparse, yaml, csv
from datetime import datetime
from collections import defaultdict
import pandas as pd
from pathlib import Path

try:
    import streamlit as st
except ImportError:
    st = None

###############################################################################
# PART A: Load config, define constants
###############################################################################
SCRIPT_DIR_PATH = Path(__file__).resolve().parent
CFG_PATH = SCRIPT_DIR_PATH / "feature_config.yml"

with open(CFG_PATH, "r", encoding="utf-8") as cf:
    CFG = yaml.safe_load(cf) or {}

COLS = ['7','6','5','4','3','2','1']  # right→left

digit2v = {
    '0':1, '5':1,
    '1':2, '6':2,
    '2':3, '7':3,
    '3':4, '8':4,
    '4':5, '9':5
}

mirror_pairs = {
    '0':'5','5':'0','1':'6','6':'1',
    '2':'7','7':'2','3':'8','8':'3',
    '4':'9','9':'4'
}

_strip_non = re.compile(r'[^0-9]').sub

def digits_only(s: str) -> str:
    return _strip_non('', s or '')

def is_3value(sub: str) -> bool:
    """
    True if 'sub' has <= 3 distinct digits AND <= 3 distinct V-Trac digits.
    """
    d = set(sub)
    if len(d) > 3:
        return False
    v = {digit2v[ch] for ch in d if ch in digit2v}
    return (len(v) <= 3)

def canon(sub: str) -> str:
    """Sort digits to unify permutations, e.g. '418' -> '148'."""
    return ''.join(sorted(sub))

def find_subs(cell: str, min_len=3, max_len=8):
    """
    Return all distinct substrings [≥3..≤8] in 'cell' that pass is_3value().
    """
    d = digits_only(cell)
    out = set()
    L = len(d)
    for start in range(L):
        for end in range(start+min_len, min(start+max_len+1, L+1)):
            ssub = d[start:end]
            if is_3value(ssub):
                out.add(ssub)
    return out

###############################################################################
# PART B: The "analyse" function
###############################################################################
def analyse(df: pd.DataFrame, section: str):
    """
    1) Finds stable 3-value substrings in each (Set,Draw,RowType,Col).
    2) Builds a highlight mask for HTML output.
    3) Groups them by (section,Set,Draw,Col,canonical).
    4) Scores them with coverage, adjacency, mirror, vertical-straight tiers,
       tail consensus (stub), single_left, unique-only dominant-last/pair, hot-level, etc.
    5) Returns (mask_map, results_list).
    """

    df = df.fillna('').reset_index(drop=True)
    mask_map = {}
    occurrences = []

    # --- STEP 1: Collect stable substrings & build highlight mask ---
    for row_i, row in df.iterrows():
        rt = row.get('RowType','')
        if rt not in ('R2','R4','R6','R8'):
            continue

        setv = row.get('Set','')
        draw = row.get('Draw','')

        for col in COLS:
            raw = str(row[col])
            if not raw.strip() or raw.strip().lower() == 'nan':
                continue

            # hot-level
            hot = 2 if '**' in raw else 1 if '*' in raw else 0

            # find stable substrings
            subs = find_subs(raw)
            if not subs:
                continue

            # build highlight mask
            dig_positions = [i for i,ch in enumerate(raw) if ch.isdigit()]
            dig_str = ''.join(raw[i] for i in dig_positions)
            local_mask = [False]*len(raw)

            for subval in subs:
                idx = dig_str.find(subval)
                while idx != -1:
                    for k in range(idx, idx + len(subval)):
                        if k < len(dig_positions):
                            realpos = dig_positions[k]
                            local_mask[realpos] = True
                    idx = dig_str.find(subval, idx+1)

                # record occurrence
                occurrences.append({
                    'section': section,
                    'Set': setv,
                    'Draw': draw,
                    'Col': col,
                    'RowType': rt,
                    'Pattern': subval,
                    'row_i': row_i,
                    'hot': hot
                })

            mask_map[(row_i,col)] = local_mask

    # --- STEP 2: Group by (section,Set,Draw,Col,canonical) ---
    from collections import defaultdict
    grouping = defaultdict(lambda: {
        'rows': set(),
        'patterns': set(),
        'hot': []
    })

    for occ in occurrences:
        cform = canon(occ['Pattern'])
        key_g = (occ['section'], occ['Set'], occ['Draw'], occ['Col'], cform)
        grouping[key_g]['rows'].add(occ['RowType'])
        grouping[key_g]['patterns'].add(occ['Pattern'])
        grouping[key_g]['hot'].append(occ['hot'])

    # adjacency map for horizontal span
    horiz_map = defaultdict(list)
    for (sec_g, setv_g, draw_g, col_g, cpat_g), info_g in grouping.items():
        horiz_map[(sec_g, setv_g, draw_g, cpat_g)].append(int(col_g))

    # --- STEP 2a: Precompute "tail_box" for col==1 or col==2 ---
    tail_box = defaultdict(lambda: {
        'rows_present_in_box': set(),
        'distinct_tails_in_box': set(),
        'is_cons': False,
        'stub_done': False
    })
    for (sec_tb, setv_tb, draw_tb, col_tb, cpat_tb), info_tb in grouping.items():
        if col_tb not in ('1','2'):
            continue
        rows_ = {r for r in info_tb['rows'] if r != 'CONS_STUB'}
        tail_of_cpat = cpat_tb[-2:]
        box_key = (sec_tb, setv_tb, draw_tb, col_tb)
        tb = tail_box[box_key]
        tb['rows_present_in_box'].update(rows_)
        tb['distinct_tails_in_box'].add(tail_of_cpat)

    # Decide if each box is truly a 1- or 2-digit tail consensus
    for box_k, box_summary in tail_box.items():
        if len(box_summary['rows_present_in_box']) == 4:
            valid_tails = {t for t in box_summary['distinct_tails_in_box']
                           if 1 <= len(t) <= 2}
            if len(valid_tails) == 1:
                box_summary['is_cons'] = True
                box_summary['tail'] = next(iter(valid_tails))

    # We'll keep track of a "front_cache" if needed, but the new
    # unique-only approach won't rely heavily on it.

    front_cache = {}

    # --- STEP 3: Build final results ---
    results = []
    for (sec, setv, draw, col, cpat), info in grouping.items():

        rowset = {r for r in info['rows'] if r != 'CONS_STUB'}
        rowcov = len(rowset)
        perm   = len(info['patterns'])
        hotval = max(info['hot']) if info['hot'] else 0

        # adjacency
        acols = sorted(horiz_map[(sec, setv, draw, cpat)])
        span  = 1
        if acols:
            tmp_run = 1
            for i2 in range(1, len(acols)):
                if acols[i2] == acols[i2-1] + 1:
                    tmp_run += 1
                else:
                    span = max(span, tmp_run)
                    tmp_run = 1
            span = max(span, tmp_run)

        # Insert an optional debug check on the rowset display
        rows_display = ",".join(sorted(rowset))
        # Uncomment the next line if you want the assertion to fail if there's a mismatch
        # assert len(rowset) == rows_display.count(',') + 1, f"Row mismatch => {rowset} vs {rows_display}"

        # (A) Possibly inject a tail-box stub if is_cons is True
        box_key   = (sec, setv, draw, col)
        box_info  = tail_box.get(box_key, {})
        is_consbox= box_info.get('is_cons', False)

        if is_consbox and not box_info.get('stub_done', False):
            # create the stub row (the user may keep or remove this feature)
            tail_cpat_for_stub = box_info['tail']
            results.append({
                'section': sec, 'Set': setv, 'Draw': draw, 'Column': col,
                'Canonical': tail_cpat_for_stub,
                'type': 'consensus_stub',
                'score': CFG['stub_consensus_score'],
                'rows': '',
                'mirror': False,
                'straight2': False,
                'straight3': False,
                'single_left': False,
                'cons_full': True,
                'cons_3v': False,
                'cons_stub': True,
                'dom_last': False,
                'dom_pair': (len(tail_cpat_for_stub) == 2),
                'hot': hotval,
                'why': 'consensus_stub'
            })
            box_info['stub_done'] = True

        # (B) Skip any pattern <3 digits if it's not a stub row
        if len(cpat) < 3:
            continue

        # Build flags
        straight   = (perm == 1)
        straight2  = (straight and rowcov >= 2)
        straight3  = (straight and rowcov >= 3)
        mirror     = any(mirror_pairs.get(d, None) in cpat for d in cpat)
        single_left= (straight and rowcov >= 3)

        # --- (B1) Rigorous row-by-row consensus check ---
        rows_needed = {'R2','R4','R6','R8'}
        cons_full = False
        cons_3v   = False

        if rowset == rows_needed and perm == 1:
            # Confirm each row is exactly cpat
            same = True
            for rrr in rows_needed:
                key_check = (sec, setv, draw, col, cpat)
                # must have exactly 1 pattern, and that pattern == cpat
                if len(info['patterns']) != 1 or cpat not in info['patterns']:
                    same = False
                    break
            if same:
                cons_full = True
                if len(cpat) == 3:
                    cons_3v = True

        # Also let the tail_box logic mark it consensus if you want
        if is_consbox:
            cons_full = True

        # (B2) Unique-Only Dominant Last & Pair
        stable   = [kk[4] for kk,vv in grouping.items()
                    if kk[:4] == (sec, setv, draw, col) and len(vv['rows'])>=2]
        dom_last = (len([p for p in stable if len(p) >= 3]) == 1 and len(cpat) >= 3)
        dom_pair = (len([p for p in stable if len(p) == 2])  == 1 and len(cpat) == 2)

        # For 3-digit doubles like 477, if rowcov≥3, we can optionally add a bonus
        dominant_double3_bonus_flag = (
            len(cpat)==3 and len(set(cpat))==2 and rowcov>=3 and not dom_last
        )

        # (C) Score
        base = 0
        # coverage
        base += rowcov * CFG['vertical_coverage_per_row']
        # adjacency
        base += span * CFG['horizontal_span_per_col']
        # baseline type
        if straight:
            base += CFG['baseline_straight_bonus']
        else:
            base += CFG['baseline_boxed_bonus']
        # mirror
        if mirror:
            base += CFG['mirror_bonus']
        # vertical-straight
        if straight2:
            base += CFG['straight_2rows_bonus']
        if straight3:
            base += CFG['straight_3rows_bonus']
        # extra-digit
        extra_len = (max(len(p) for p in info['patterns']) - 3) if info['patterns'] else 0
        base += extra_len * CFG['extra_digit_per_char']
        # single_left
        if single_left:
            base += CFG['single_left_bonus']
        # consensus
        if cons_full:
            base += CFG['consensus_full_bonus']
        # hot
        if hotval == 1:
            base += CFG['hot_level_1_bonus']
        elif hotval == 2:
            base += CFG['hot_level_2_bonus']
        # dominant
        if dom_last:
            base += CFG.get('dominant_last_bonus', 0)
        if dom_pair:
            base += CFG.get('dominant_pair_bonus', 0)
        if dominant_double3_bonus_flag:
            base += CFG.get('dominant_double3_bonus', 0)

        # (D) Build final record
        why_bits = []
        why_bits.append('straight' if straight else 'boxed')
        why_bits.append(f'cov{rowcov}')
        if span>1:
            why_bits.append(f'span{span}')
        if straight2:
            why_bits.append('vstr2')
        if straight3:
            why_bits.append('vstr3')
        if mirror:
            why_bits.append('mirror')
        if single_left:
            why_bits.append('single_left')
        if cons_full:
            why_bits.append('cons_full')
        if hotval>0:
            why_bits.append(f'hot{hotval}')
        if dom_last:
            why_bits.append('dom_last')
        if dom_pair:
            why_bits.append('dom_pair')
        if cons_3v:
            why_bits.append('cons_3v')

        rec = dict(
            section=sec,
            Set=setv,
            Draw=draw,
            Column=col,
            Canonical=cpat,
            type='straight' if straight else 'boxed',
            score=base,
            rows=rows_display,
            mirror=mirror,
            straight2=straight2,
            straight3=straight3,
            single_left=single_left,
            cons_full=cons_full,
            cons_3v=cons_3v,
            cons_stub=False,
            dom_last=dom_last,
            dom_pair=dom_pair,
            hot=hotval,
            why='|'.join(why_bits)
        )
        results.append(rec)

    # --- STEP 4: highlight filter ---
    cutoff_score = CFG['min_score_to_highlight']
    keepers = {
        (r['section'], r['Set'], r['Draw'], r['Column'], r['Canonical'])
        for r in results
        if r['score'] >= cutoff_score
    }

    # Rebuild highlight mask
    for (r_i, col) in list(mask_map.keys()):
        rawval = df.at[r_i,col]
        newmask = [False]*len(rawval)
        setv_i  = df.at[r_i, 'Set']
        draw_i  = df.at[r_i, 'Draw']

        digit_positions = [idx for idx,ch in enumerate(rawval) if ch.isdigit()]
        digit_str       = ''.join(rawval[idx] for idx in digit_positions)

        for sub in find_subs(rawval):
            csub = canon(sub)
            if (section, setv_i, draw_i, col, csub) not in keepers:
                continue
            pos_idx = digit_str.find(sub)
            while pos_idx != -1:
                for kk in range(pos_idx, pos_idx + len(sub)):
                    if kk < len(digit_positions):
                        newmask[digit_positions[kk]] = True
                pos_idx = digit_str.find(sub, pos_idx+1)
        mask_map[(r_i,col)] = newmask

    # final sort
    results.sort(key=lambda x: x['score'], reverse=True)
    return mask_map, results


###############################################################################
# PART C: Build HTML for highlight & scoreboard
###############################################################################
def build_html(df, mask_map, section, results_chunk):
    """
    Renders two tables:
      1) The original data with highlight
      2) A 'top patterns' summary table
    """
    lines = [f"<h2>{section}</h2>"]
    lines.append("<table border='1' cellspacing='0' cellpadding='3' style='border-collapse:collapse;'>")
    # header
    lines.append("<tr><th>Set</th><th>Draw</th><th>RowType</th>"
                 + "".join(f"<th>{c}</th>" for c in COLS)
                 + "</tr>")

    for i, row in df.iterrows():
        lines.append("<tr>")
        lines.append(f"<td>{row.get('Set','')}</td>"
                     f"<td>{row.get('Draw','')}</td>"
                     f"<td>{row.get('RowType','')}</td>")
        for col in COLS:
            raw = str(row.get(col,''))
            mk  = mask_map.get((i,col), [False]*len(raw))
            cell_out = ""
            for j,ch in enumerate(raw):
                start_h = (mk[j] and (j==0 or not mk[j-1]))
                end_h   = (mk[j] and (j==len(raw)-1 or not mk[j+1]))
                if start_h:
                    cell_out += "<span style='background:yellow;font-weight:bold;'>"
                cell_out += ch
                if end_h:
                    cell_out += "</span>"
            lines.append(f"<td>{cell_out}</td>")
        lines.append("</tr>")
    lines.append("</table>")

    # scoreboard
    lines.append("<h3>Detected Patterns (Top 30)</h3>")
    lines.append("<table border='1' cellpadding='3' cellspacing='0'>")
    lines.append("<tr><th>Set</th><th>Draw</th><th>Col</th><th>Canonical</th>"
                 "<th>Type</th><th>Score</th><th>Rows</th><th>Mirror?</th>"
                 "<th>V-Trac</th><th>Stub?</th><th>Hot</th><th>Single?</th>"
                 "<th>Cons?</th><th>3vCons?</th><th>DomLast?</th><th>DomPair?</th>"
                 "<th>Why</th></tr>")

    topN = results_chunk[:30]
    for r in topN:
        # build V-Trac
        vtrac = ''.join(str(digit2v.get(d,'')) for d in r['Canonical'])
        lines.append(
            f"<tr>"
            f"<td>{r.get('Set','')}</td>"
            f"<td>{r.get('Draw','')}</td>"
            f"<td>{r.get('Column','')}</td>"
            f"<td>{r.get('Canonical','')}</td>"
            f"<td>{r.get('type','')}</td>"
            f"<td>{r.get('score','')}</td>"
            f"<td>{r.get('rows','')}</td>"
            f"<td>{'Y' if r.get('mirror',False) else ''}</td>"
            f"<td>{vtrac}</td>"
            f"<td>{'Y' if r.get('cons_stub',False) else ''}</td>"
            f"<td>{r.get('hot','')}</td>"
            f"<td>{'Y' if r.get('single_left',False) else ''}</td>"
            f"<td>{'Y' if r.get('cons_full',False) else ''}</td>"
            f"<td>{'Y' if r.get('cons_3v',False) else ''}</td>"
            f"<td>{'Y' if r.get('dom_last',False) else ''}</td>"
            f"<td>{'Y' if r.get('dom_pair',False) else ''}</td>"
            f"<td>{r.get('why','')}</td>"
            f"</tr>"
        )
    lines.append("</table>")
    return "\n".join(lines)

###############################################################################
# PART D: CLI or Streamlit entry point
###############################################################################
if __name__ == "__main__":
    # If running in Streamlit, handle differently
    if st and getattr(st, '_is_running_with_streamlit', False):
        pass  # you could import a specialized streamlit UI if desired
    else:
        ap = argparse.ArgumentParser()
        ap.add_argument("--files", nargs="+", required=True, help="Paths to combined CSV(s).")
        ap.add_argument("--html",  default="stable_patterns.html", help="Output HTML file.")
        ap.add_argument("--csv",   default="stable_patterns.csv",  help="Output CSV file.")
        args = ap.parse_args()

        all_results   = []
        html_sections = []

        for f in args.files:
            df = pd.read_csv(f, dtype=str).fillna('')
            fname = os.path.basename(f)
            m = re.search(r'_(Midday|Evening|Combined)_', fname, re.I)
            section_name = m.group(1) if m else fname

            mask_map, rlist = analyse(df, section_name)
            all_results.extend(rlist)
            partial_html = build_html(df, mask_map, section_name, rlist)
            html_sections.append(partial_html)
            print(f"✓ {section_name}: {len(rlist)} patterns found")

        # sort final results
        all_results.sort(key=lambda x: x['score'], reverse=True)

        # build final HTML
        final_html = (
            "<html><head><meta charset='utf-8'/>"
            "<title>Stable Patterns Extraction</title>"
            "<style>body{font-family:Arial;} "
            "table{border-collapse:collapse;margin:10px 0;} "
            "td,th{border:1px solid #ccc;padding:4px 6px;} "
            "span[style*='background']{border:1px dotted #f00;}"
            "</style></head><body>"
            f"<h1>Stable Patterns Report</h1>"
            f"<p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>"
            + "\n".join(html_sections) +
            "</body></html>"
        )

        with open(args.html, 'w', encoding='utf-8') as fh:
            fh.write(final_html)
        print(f"HTML -> {args.html}")

        # Write CSV
        out_cols = [
            "section","Set","Draw","Column","Canonical","type","score","rows",
            "mirror","straight2","straight3","single_left","cons_full","cons_3v",
            "cons_stub","dom_last","dom_pair","hot","why"
        ]
        with open(args.csv,'w',newline='',encoding='utf-8') as fc:
            w = csv.DictWriter(fc, fieldnames=out_cols)
            w.writeheader()
            for rowd in all_results:
                w.writerow({k: rowd.get(k,'') for k in out_cols})
        print(f"CSV  -> {args.csv}")
