#!/usr/bin/env python
"""
Stable-Pattern Extractor (Final Version)
========================================
Loads combined-table CSV(s) and finds "stable 3-value" substrings.
Scores them with a sophisticated, configurable weighting system from feature_config.yml.
This version includes all features discussed:
 - Vertical & Horizontal coverage
 - Mirror, Straight, Boxed, and length bonuses
 - Single Left Survivor (strict definition)
 - Dominant Last Survivor (unique with tie-breaker)
 - Consensus Tail Stubs & Bonuses
 - Hot Zone level tagging
 - Detailed 'why' string for score traceability
"""
import os, sys, re, argparse, yaml, csv, itertools
from datetime import datetime
from collections import defaultdict, Counter
import pandas as pd
from pathlib import Path

try:
    import streamlit as st
except ImportError:
    st = None

# --- Config & Constants ---
# Load weights from YAML file located next to the script
try:
    SCRIPT_DIR_PATH = Path(__file__).resolve().parent
    CFG_PATH = SCRIPT_DIR_PATH / "feature_config.yml"
    with open(CFG_PATH, "r", encoding="utf-8") as _cf:
        CFG = yaml.safe_load(_cf) or {}
except FileNotFoundError:
    print(f"FATAL ERROR: feature_config.yml not found at {CFG_PATH}")
    print("Please ensure the config file is in the same directory as this script.")
    sys.exit(1)

COLS = ['7','6','5','4','3','2','1']
digit2v = {'0':1,'5':1,'1':2,'6':2,'2':3,'7':3,'3':4,'8':4,'4':5,'9':5}
mirror_pairs = {'0':'5','5':'0','1':'6','6':'1','2':'7','7':'2',
                '3':'8','8':'3','4':'9','9':'4'}

_strip_non = re.compile(r'[^0-9]').sub
def digits_only(s:str)->str: return _strip_non('', s or '')

def is_3value(sub:str)->bool:
    d=set(sub)
    if not d: return False
    return len(d)<=3 and len({digit2v.get(x) for x in d if x in digit2v})<=3

def canon(sub:str)->str: return ''.join(sorted(sub))

def find_subs(cell:str,min_len=3,max_len=8):
    d=digits_only(cell)
    out=set(); L=len(d)
    for i in range(L):
        for j in range(i+min_len, min(i+max_len+1,L+1)):
            ss=d[i:j]
            if is_3value(ss): out.add(ss)
    return out

# --- Main Analysis Function ---
def analyse(df:pd.DataFrame, section:str):
    """
    Main analysis function, combining all logic for pattern extraction, scoring, and flagging.
    """
    # --- STEP 1: Find all potential patterns and group them ---
    df=df.fillna('').reset_index(drop=True)
    occurrences = []
    for r_i, row in df.iterrows():
        rt=row.get('RowType','')
        if rt not in ('R2','R4','R6','R8'): continue
        setv=row.get('Set',''); draw=row.get('Draw','')
        for col in COLS:
            cell_raw = str(row.get(col,''))
            hot_level = 2 if '**' in cell_raw else 1 if '*' in cell_raw else 0
            if not cell_raw.strip() or cell_raw.strip().lower()=='nan': continue
            
            subs = find_subs(cell_raw)
            # Inject 1-2 digit cells for consensus logic
            if not subs and 1 <= len(digits_only(cell_raw)) <= 2:
                subs.add(digits_only(cell_raw))
            if not subs: continue

            for subval in subs:
                occurrences.append({
                    'section': section, 'Set': setv, 'Draw': draw, 'Col': col,
                    'RowType': rt, 'Pattern': subval, 'row_i': r_i, 'hot': hot_level
                })
    
    grouping = defaultdict(lambda: {'rows': set(), 'patterns': set(), 'hot': []})
    for occ in occurrences:
        cform = canon(occ['Pattern'])
        key_g = (occ['section'], occ['Set'], occ['Draw'], occ['Col'], cform)
        grouping[key_g]['rows'].add(occ['RowType'])
        grouping[key_g]['patterns'].add(occ['Pattern'])
        grouping[key_g]['hot'].append(occ['hot'])

    # --- STEP 2: Pre-calculate box-level summaries ---
    tail_box = defaultdict(lambda: { 'rows_present_in_box': set(), 'distinct_tails_in_box': set(), 'is_cons': False, 'stub_done': False })
    for (sec_tb, setv_tb, draw_tb, col_tb, cpat_tb), info_tb in grouping.items():
        if col_tb not in ('1','2'): continue
        rows_ = {r for r in info_tb['rows'] if r != 'CONS_STUB'}
        tail_of_cpat = cpat_tb[-2:]
        box_key = (sec_tb, setv_tb, draw_tb, col_tb)
        tb = tail_box[box_key]
        tb['rows_present_in_box'].update(rows_)
        tb['distinct_tails_in_box'].add(tail_of_cpat)
    
    for box_k, box_summary in tail_box.items():
        if len(box_summary['rows_present_in_box']) == 4:
            valid_tails = {t for t in box_summary['distinct_tails_in_box'] if 1 <= len(t) <= 2}
            if len(valid_tails) == 1:
                box_summary['is_cons'] = True
                box_summary['tail'] = next(iter(valid_tails))
    
    front_cache = {}
    for (sec,setv,draw,col,cpat),info in grouping.items():
        front_key = (sec, setv, draw, col)
        front_entry = { 'cpat': cpat, 'rowcov': len([r for r in info['rows'] if r != 'CONS_STUB']), 'perm': len(info['patterns']) }
        prev = front_cache.get(front_key)
        if (prev is None or front_entry['rowcov'] > prev['rowcov'] or
            (front_entry['rowcov'] == prev['rowcov'] and len(cpat) > len(prev['cpat']))):
            front_cache[front_key] = front_entry
            
    horiz_map = defaultdict(list)
    for (sec_g, setv_g, draw_g, col_g, cpat_g), info_g in grouping.items():
        horiz_map[(sec_g, setv_g, draw_g, cpat_g)].append(int(col_g))
        
    # --- STEP 3: Build final results by iterating through groups ---
    results = []
    for (sec, setv, draw, col, cpat), info in grouping.items():
        rowset = {r for r in info['rows'] if r != 'CONS_STUB'}
        rowcov = len(rowset); perm = len(info['patterns']); hot = max(info['hot']) if info['hot'] else 0

        # Inject stub row for tail consensus boxes (once per box)
        box_key = (sec, setv, draw, col)
        box_info = tail_box.get(box_key, {})
        is_cons_box = box_info.get('is_cons', False)
        if is_cons_box and not box_info.get('stub_done', False):
            tail_cpat = box_info.get('tail', '')
            if tail_cpat:
                results.append(dict(section=sec, Set=setv, Draw=draw, Column=col, Canonical=tail_cpat, type='consensus_stub', score=CFG.get('stub_consensus_score',3), rows='', mirror=False, straight2=False, straight3=False, single_left=False, cons_full=True, cons_3v=False, cons_stub=True, dom_last=False, dom_pair=(len(tail_cpat)==2), hot=hot, why='consensus_stub'))
                box_info['stub_done'] = True

        # --- Flag Calculation ---
        straight = (perm == 1); straight2 = (straight and rowcov >= 2); straight3 = (straight and rowcov >= 3)
        mirror = any(mirror_pairs.get(d) in cpat for d in cpat if d in mirror_pairs)
        acols = sorted(horiz_map[(sec, setv, draw, cpat)]); span = 1
        if acols: 
            tmp_run = 1
            for i2 in range(1, len(acols)):
                if acols[i2] == acols[i2-1] + 1:
                    tmp_run += 1
                else:
                    span = max(span, tmp_run)
                    tmp_run = 1
            span = max(span, tmp_run)

        single_left = (straight and rowcov >= 3 and span == 1)
        
        cons_full = is_cons_box or (rowcov==4 and perm==1 and len(cpat) == 3)
        cons_3v = (cons_full and len(cpat) == 3)

        # ----------  DOMINANT LAST SURVIVOR (unique) ----------------
        dom_last = False
        dom_pair = False
        if rowcov >= 3:                                   # current pattern must be stable
            # walk right→left once per Set-Draw
            for c_check in reversed(COLS):                # ['1','2', … ,'7']
                key_check = (sec, setv, draw, c_check)
                best = front_cache.get(key_check)
                if best and best['rowcov'] >= 3:          # first (right-most) stable column
                    if c_check == col:                    # ← we're in that column
                        # longest canonical among all stable patterns in this box
                        stable_cpats_in_box = [kk[4] for kk,vv in grouping.items() if kk[0:4]==key_check and len(vv['rows'])>=3]
                        if stable_cpats_in_box:
                            max_len = max(len(p) for p in stable_cpats_in_box)
                            # find lexicographically largest canonical of that max_len in the box
                            longest_cpats = [p for p in stable_cpats_in_box if len(p) == max_len]
                            leximax = max(longest_cpats) if longest_cpats else ""
                            
                            is_double3_tie = (len(cpat) == 3 and len(set(cpat)) == 2 and len(cpat)==max_len)
                            
                            # The current pattern is dominant if it's the longest and lexicographically largest, OR it's a double-3 tieing for longest
                            if (len(cpat) == max_len and cpat == leximax) or is_double3_tie:
                                dom_last = (len(cpat) >= 3)
                                dom_pair = (len(cpat) == 2)
                    break                                 # stop after front-line column
        # ------------------------------------------------------------
        
        # Gate short canonicals (using flags calculated above)
        if len(cpat) <= 2:
            keep_short = (cons_full or dom_pair) # dom_last implies len >= 3
            if not keep_short:
                continue

        # --- Scoring ---
        base = (rowcov * CFG['vertical_coverage_per_row'] +
                span * CFG['horizontal_span_per_col'] +
                (CFG['baseline_straight_bonus'] if straight else CFG['baseline_boxed_bonus']) +
                (CFG['mirror_bonus'] if mirror else 0) +
                (CFG['straight_2rows_bonus'] if straight2 else 0) +
                (CFG['straight_3rows_bonus'] if straight3 else 0) +
                ((max(len(p) for p in info['patterns']) - 3) * CFG['extra_digit_per_char'] if info['patterns'] else 0) +
                (CFG['single_left_bonus'] if single_left else 0) +
                (CFG['consensus_full_bonus'] if cons_full else 0) +
                (CFG['hot_level_1_bonus'] if hot == 1 else 0) +
                (CFG['hot_level_2_bonus'] if hot == 2 else 0) +
                (CFG.get('dominant_last_bonus', 0) if dom_last else 0) +
                (CFG.get('dominant_pair_bonus', 0) if dom_pair else 0) +
                (CFG.get('dominant_double3_bonus', 0) if (dom_last and len(cpat)==3 and len(set(cpat))==2) else 0)
        )
        
        # --- Build Final Record ---
        why = ['straight' if straight else 'boxed', f'cov{rowcov}']
        if span > 1: why.append(f'span{span}')
        if straight2: why.append('vstr2')
        if straight3: why.append('vstr3')
        if mirror: why.append('mirror')
        if single_left: why.append('single_left')
        if cons_full: why.append('cons_full')
        if hot > 0: why.append(f'hot{hot}')
        if dom_last: why.append('dom_last')
        if dom_pair: why.append('dom_pair')
        if cons_3v: why.append('cons_3v')
        
        results.append(dict(
            section=sec, Set=setv, Draw=draw, Column=col, Canonical=cpat,
            type='straight' if straight else 'boxed', score=base, rows=",".join(sorted(rowset)),
            mirror=mirror, straight2=straight2, straight3=straight3, single_left=single_left,
            cons_full=cons_full, cons_3v=cons_3v, cons_stub=False, dom_last=dom_last,
            dom_pair=dom_pair, hot=hot, why='|'.join(why)
        ))
        
    # --- STEP 4: highlight filter ---
    cutoff_score = CFG['min_score_to_highlight']
    keepers = { (r['section'], r['Set'], r['Draw'], r['Column'], r['Canonical']) for r in results if r['score'] >= cutoff_score }

    for (r_i, col), mask_val in list(mask_map.items()):
        rawval = df.at[r_i,col]; newmask = [False]*len(rawval)
        setv_i = df.at[r_i,'Set']; draw_i = df.at[r_i,'Draw']
        
        digit_positions = [idx for idx,ch in enumerate(rawval) if ch.isdigit()]
        digit_str = ''.join(rawval[idx] for idx in digit_positions)
        
        for sub in find_subs(rawval):
            csub = canon(sub)
            if (section, setv_i, draw_i, col, csub) not in keepers: continue
            pos_idx = digit_str.find(sub)
            while pos_idx != -1:
                for kk in range(pos_idx, pos_idx + len(sub)):
                    if kk < len(digit_positions): newmask[digit_positions[kk]] = True
                pos_idx = digit_str.find(sub, pos_idx+1)
        
        raw_digits = digits_only(rawval)
        if 1 <= len(raw_digits) <= 2:
            key_full = (section, setv_i, draw_i, col, canon(raw_digits))
            if key_full in keepers:
                for k in digit_positions: newmask[k] = True
        mask_map[(r_i,col)] = newmask
        
    results.sort(key=lambda x: x.get('score', 0), reverse=True)
    return mask_map, results

# --- HTML & CLI / Streamlit Wrappers (assumed correct and complete) ---
def build_html(df, mask_map, section, results_chunk):
    lines = [f"<h2>{section}</h2>", "<table border='1' cellspacing='0' cellpadding='3' style='border-collapse:collapse;'>"]
    lines.append("<tr><th>Set</th><th>Draw</th><th>RowType</th>" + "".join(f"<th>{c}</th>" for c in COLS) + "</tr>")
    for i, row in df.iterrows():
        lines.append(f"<tr><td>{row.get('Set','')}</td><td>{row.get('Draw','')}</td><td>{row.get('RowType','')}</td>")
        for col_name in COLS:
            raw = str(row.get(col_name, ''))
            mask = mask_map.get((i,col_name), [False]*len(raw))
            cell_out = ""
            for j,ch_val in enumerate(raw):
                if mask[j] and (j==0 or not mask[j-1]): cell_out += "<span style='background:yellow;font-weight:bold;'>"
                cell_out += ch_val
                if mask[j] and (j==len(raw)-1 or not mask[j+1]): cell_out += "</span>"
            lines.append(f"<td>{cell_out}</td>")
        lines.append("</tr>")
    lines.append("</table>")
    lines.append("<h3>Detected Patterns (Top 30)</h3>")
    lines.append("<table border='1' cellpadding='3' cellspacing='0'><thead><tr>" +
                 "<th>Set</th><th>Draw</th><th>Col</th><th>Canonical</th><th>Type</th><th>Score</th>" +
                 "<th>Rows</th><th>Mirror?</th><th>V-Trac</th><th>Stub?</th><th>Hot</th><th>Single?</th>" +
                 "<th>Cons?</th><th>3vCons?</th><th>DomLast?</th><th>DomPair?</th><th>Why</th></tr></thead><tbody>")
    for r in results_chunk[:30]:
        vtrac_str = ''.join(str(digit2v.get(d,'')) for d in r.get('Canonical',''))
        lines.append(
            f"<tr><td>{r.get('Set','')}</td><td>{r.get('Draw','')}</td><td>{r.get('Column','')}</td>"
            f"<td>{r.get('Canonical','')}</td><td>{r.get('type','')}</td><td>{r.get('score','')}</td>"
            f"<td>{r.get('rows','')}</td><td>{'Y' if r.get('mirror',False) else ''}</td>"
            f"<td>{vtrac_str}</td>"
            f"<td>{'Y' if r.get('cons_stub',False) else ''}</td><td>{r.get('hot','')}</td>"
            f"<td>{'Y' if r.get('single_left',False) else ''}</td>"
            f"<td>{'Y' if r.get('cons_full',False) else ''}</td>"
            f"<td>{'Y' if r.get('cons_3v',False) else ''}</td>"
            f"<td>{'Y' if r.get('dom_last',False) else ''}</td>"
            f"<td>{'Y' if r.get('dom_pair',False) else ''}</td>"
            f"<td>{r.get('why','')}</td></tr>"
        )
    lines.append("</tbody></table><hr/>")
    return "\n".join(lines)

def main_cli():
    ap = argparse.ArgumentParser(description="Stable-Pattern Extractor FULL")
    ap.add_argument("--files", nargs="+", required=True, help="One or more combined-table CSVs.")
    ap.add_argument("--html", default="stable_patterns_report.html")
    ap.add_argument("--csv",  default="stable_patterns_scores.csv")
    args = ap.parse_args()

    html_parts=[]; all_rows=[]
    for f in args.files:
        if not os.path.exists(f): continue
        df = pd.read_csv(f, dtype=str).fillna('')
        fname = os.path.basename(f)
        m = re.search(r'_(Midday|Evening|Combined)_', fname, re.I)
        section = m.group(1) if m else fname
        mask,res=analyse(df,section)
        html_parts.append(build_html(df,mask,section,res))
        all_rows.extend(res)
        print(f"✓ {section}: {len(res)} patterns")

    if not all_rows: print("No patterns found."); return
    all_rows.sort(key=lambda r:r.get('score',0), reverse=True)

    with open(args.html,'w',encoding='utf-8') as fh:
        fh.write("<html><head><meta charset='utf-8'></head><body>" + "\n".join(html_parts) + "</body></html>")
    print(f"HTML  → {os.path.abspath(args.html)}")

    out_cols = [
      "section","Set","Draw","Column","Canonical","type","score","rows",
      "mirror","straight2","straight3","single_left",
      "cons_full","cons_3v","cons_stub",
      "dom_last","dom_pair", "hot","why"
    ]
    with open(args.csv,'w',newline='',encoding='utf-8') as fc:
        w=csv.DictWriter(fc,fieldnames=out_cols); w.writeheader()
        for r in all_rows: w.writerow({k:r.get(k,'') for k in out_cols})
    print(f"CSV   → {os.path.abspath(args.csv)}")


if __name__ == "__main__":
    if st and getattr(st, '_is_running_with_streamlit', False):
        st.error("Streamlit UI for this version is not implemented yet.")
    else:
        main_cli()
