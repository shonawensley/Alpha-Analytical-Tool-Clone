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
import os, sys, re, argparse, csv, itertools
from datetime import datetime
from collections import defaultdict, Counter
import pandas as pd
from pathlib import Path

try:
    import streamlit as st
except ImportError:
    st = None

from alpha_analytical.stable.feature_config import CFG, CONFIG_PATH as _CONFIG_PATH
from alpha_analytical.stable.post_pass_families import derive_vtrac_index_for_canonical
from alpha_analytical.vtrac import get_vtrac_index

# --- Config & Constants ---
# Retain legacy attributes for downstream callers (e.g., Streamlit Dev Health)
SCRIPT_DIR_PATH = Path(__file__).resolve().parent
CFG_PATH = _CONFIG_PATH
if not CFG_PATH.exists():
    raise FileNotFoundError(f"feature_config.yml not found at {CFG_PATH}")

COLS = ['7','6','5','4','3','2','1']
digit2v = {'0':1,'5':1,'1':2,'6':2,'2':3,'7':3,'3':4,'8':4,'4':5,'9':5}
mirror_pairs = {'0':'5','5':'0','1':'6','6':'1','2':'7','7':'2',
                '3':'8','8':'3','4':'9','9':'4'}

_strip_non = re.compile(r'[^0-9]').sub
def digits_only(s:str)->str: return _strip_non('', s or '')

def is_3value(sub:str)->bool:
    """Return True if the substring spans three or fewer V-Trac classes (regardless of raw digit count)."""
    vset = {digit2v.get(ch) for ch in sub if ch in digit2v}
    return bool(vset) and len(vset) <= 3

def canon(sub:str)->str: return ''.join(sorted(sub))

def find_subs(cell:str,min_len=3,max_len=8):
    d=digits_only(cell)
    out=set(); L=len(d)
    for i in range(L):
        for j in range(i+min_len, min(i+max_len+1,L+1)):
            ss=d[i:j]
            if is_3value(ss): out.add(ss)
    return out

def find_subs_with_counts(cell: str, min_len: int = 3, max_len: int = 8):
    raw = digits_only(cell)
    hits = Counter()
    L = len(raw)
    for start in range(L):
        for end in range(start + min_len, min(start + max_len + 1, L + 1)):
            sub = raw[start:end]
            if is_3value(sub):
                hits[sub] += 1
    return hits


def _has_hidden_three_value(raw_digits: str, family_id: int | None) -> bool:
    """Detect a 3-value pattern hidden inside a 4-digit window that maps to the same family."""
    if family_id is None or len(raw_digits) < 4:
        return False
    window = raw_digits
    for start in range(len(window) - 3):
        segment = window[start:start + 4]
        if not is_3value(segment):
            continue
        indices = ((0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3))
        for idx_tuple in indices:
            candidate = ''.join(segment[i] for i in idx_tuple)
            if not is_3value(candidate):
                continue
            candidate_family = derive_vtrac_index_for_canonical(canon(candidate), get_vtrac_index)
            if candidate_family == family_id:
                return True
    return False


# --- Main Analysis Function ---


def analyse(df: pd.DataFrame, section: str):
    """Return highlight mask and scored stable-pattern rows for a section."""
    df = df.fillna('').reset_index(drop=True)

    grouping = defaultdict(
        lambda: {
            "rows": set(),
            "patterns": set(),
            "hot": [],
            "orders_by_row": defaultdict(set),
            "repeat_extras": 0,
        }
    )
    tail_box = defaultdict(lambda: {"rows": set(), "tails": set(), "is_cons": False, "stub_done": False, "tail": ""})

    for r_i, row in df.iterrows():
        rowtype = row.get('RowType', '')
        if rowtype not in ('R2', 'R4', 'R6', 'R8'):
            continue
        setv = row.get('Set', '')
        draw = row.get('Draw', '')
        for col in COLS:
            cell_raw = str(row.get(col, ''))
            hot_level = 2 if '**' in cell_raw else 1 if '*' in cell_raw else 0
            raw_digits = digits_only(cell_raw)
            if not cell_raw.strip() and not raw_digits:
                continue

            orders_counts = find_subs_with_counts(cell_raw)
            if not orders_counts and 1 <= len(raw_digits) <= 2:
                orders_counts[raw_digits] += 1
            if not orders_counts:
                continue

            box_key = (section, setv, draw, col)
            box_entry = tail_box[box_key]
            box_entry['rows'].add(rowtype)
            tail = raw_digits[-2:] if raw_digits else ''
            if 1 <= len(tail) <= 2:
                box_entry['tails'].add(tail)

            for subval, count in orders_counts.items():
                cform = canon(subval)
                key_g = (section, setv, draw, col, cform)
                info = grouping[key_g]
                info['rows'].add(rowtype)
                info['patterns'].add(subval)
                info['hot'].append(hot_level)
                info['orders_by_row'][rowtype].add(subval)
                if count > 1:
                    info['repeat_extras'] += count - 1

    for box_key, box in tail_box.items():
        rows_present = {r for r in box['rows'] if r != 'CONS_STUB'}
        if len(rows_present) == 4:
            tails = {t for t in box['tails'] if t}
            if len(tails) == 1:
                box['is_cons'] = True
                box['tail'] = next(iter(tails))

    front_cache = {}
    for (sec, setv, draw, col, cpat), info in grouping.items():
        front_key = (sec, setv, draw, col)
        entry = {
            'cpat': cpat,
            'rowcov': len([r for r in info['rows'] if r != 'CONS_STUB']),
            'perm': len(info['patterns']),
        }
        prev = front_cache.get(front_key)
        if (
            prev is None
            or entry['rowcov'] > prev['rowcov']
            or (entry['rowcov'] == prev['rowcov'] and len(cpat) > len(prev['cpat']))
        ):
            front_cache[front_key] = entry

    horiz_map = defaultdict(list)
    for (sec_g, setv_g, draw_g, col_g, cpat_g), _info in grouping.items():
        try:
            col_int = int(col_g)
        except ValueError:
            col_int = 0
        horiz_map[(sec_g, setv_g, draw_g, cpat_g)].append(col_int)

    results = []
    for (sec, setv, draw, col, cpat), info in grouping.items():
        rowset = {r for r in info['rows'] if r != 'CONS_STUB'}
        rowcov = len(rowset)
        perm_count_in_box = len(info['patterns'])
        repeat_extras_in_box = info.get('repeat_extras', 0)
        hot = max(info['hot']) if info['hot'] else 0

        orders_by_row = info['orders_by_row']
        modal_counter = Counter()
        for orders in orders_by_row.values():
            for order in orders:
                modal_counter[order] += 1
        orders_modal_value = ''
        orders_modal_rows = 0
        if modal_counter:
            orders_modal_value, orders_modal_rows = modal_counter.most_common(1)[0]

        straight = perm_count_in_box == 1
        straight2 = orders_modal_rows >= 2
        straight3 = orders_modal_rows >= 3

        mirror = any(mirror_pairs.get(d) in cpat for d in cpat if d in mirror_pairs)

        acols = sorted(horiz_map[(sec, setv, draw, cpat)])
        span = 1
        if acols:
            tmp_run = 1
            for idx in range(1, len(acols)):
                if acols[idx] == acols[idx - 1] + 1:
                    tmp_run += 1
                else:
                    span = max(span, tmp_run)
                    tmp_run = 1
            span = max(span, tmp_run)

        single_left = _eval_single_left(rowcov=rowcov, span=span, straight=straight)

        box_info = tail_box.get((sec, setv, draw, col), {})
        is_cons_box = box_info.get('is_cons', False)
        if is_cons_box and not box_info.get('stub_done', False):
            tail_cpat = box_info.get('tail', '')
            if tail_cpat:
                stub_family = derive_vtrac_index_for_canonical(canon(tail_cpat), get_vtrac_index)
                results.append(dict(
                    section=sec,
                    Set=setv,
                    Draw=draw,
                    Column=col,
                    Canonical=tail_cpat,
                    type='consensus_stub',
                    score=CFG.get('stub_consensus_score', 3),
                    rows='',
                    mirror=False,
                    straight2=False,
                    straight3=False,
                    single_left=False,
                    cons_full=True,
                    cons_3v=False,
                    cons_stub=True,
                    dom_last=False,
                    dom_pair=(len(tail_cpat) == 2),
                    hot=hot,
                    family_id=stub_family,
                    hidden3v=False,
                    perm_count_in_box=1,
                    repeat_extras_in_box=0,
                    horizontal_persistence_repeat=1,
                    orders_modal_value='',
                    orders_modal_rows=0,
                    score_cov=0,
                    score_hpr=0,
                    score_perm=0,
                    score_repeat=0,
                    score_straight=0,
                    score_single=0,
                    score_cons=0,
                    score_hot=0,
                    score_mirror=0,
                    score_dom=0,
                    score_len=0,
                    score_hidden=0,
                    why='consensus_stub'
                ))
                box_info['stub_done'] = True

        perm = perm_count_in_box
        cons_full = is_cons_box or (rowcov == 4 and straight and len(cpat) == 3)
        cons_3v = cons_full and len(cpat) == 3

        dom_last = False
        dom_pair = False
        if rowcov >= 3:
            for c_check in reversed(COLS):
                key_check = (sec, setv, draw, c_check)
                best = front_cache.get(key_check)
                if best and best['rowcov'] >= 3:
                    if c_check == col:
                        stable_cpats_in_box = [kk[4] for kk, vv in grouping.items() if kk[0:4] == key_check and len(vv['rows']) >= 3]
                        if stable_cpats_in_box:
                            max_len = max(len(p) for p in stable_cpats_in_box)
                            longest_cpats = [p for p in stable_cpats_in_box if len(p) == max_len]
                            leximax = max(longest_cpats) if longest_cpats else ''
                            is_double3_tie = (len(cpat) == 3 and len(set(cpat)) == 2 and len(cpat) == max_len)
                            if (len(cpat) == max_len and cpat == leximax) or is_double3_tie:
                                dom_last = len(cpat) >= 3
                                dom_pair = len(cpat) == 2
                    break

        if len(cpat) <= 2 and not (cons_full or dom_pair):
            continue

        family_id = derive_vtrac_index_for_canonical(cpat, get_vtrac_index)
        hidden3v_flag = _has_hidden_three_value(raw_digits, family_id)

        col_factor = 2 if col == '1' else 1
        extra_len_bonus = ((max(len(p) for p in info['patterns']) - 3) * CFG['extra_digit_per_char']) if info['patterns'] else 0

        # === AAT9-SCORE-CONTRACT: BEGIN (ROW) ===
        score_cov = rowcov * CFG['vertical_coverage_per_row']
        score_hpr = span * CFG['horizontal_persistence_repeat_bonus']
        score_perm = max(0, perm_count_in_box - 1) * CFG.get('perm_density_per_extra', 0)
        score_repeat = repeat_extras_in_box * CFG.get('repeat_count_per_extra', 0)
        score_straight = (CFG['baseline_straight_bonus'] if straight else CFG['baseline_boxed_bonus']) \
            + (CFG['straight_2rows_bonus'] if straight2 else 0) \
            + (CFG['straight_3rows_bonus'] if straight3 else 0)
        score_single = CFG['single_left_bonus'] if single_left else 0
        score_cons = CFG['consensus_full_bonus'] if cons_full else 0
        score_hot = _hot_bonus(col, hot)
        score_mirror = CFG['mirror_bonus'] if mirror else 0
        score_len = extra_len_bonus
        score_hidden = CFG.get('hidden3v_bonus', 0) if hidden3v_flag else 0
        score_dom = 0.0
        if dom_last:
            score_dom += CFG.get('dominant_last_bonus', 0)
            if len(cpat) == 3 and len(set(cpat)) == 2:
                score_dom += CFG.get('dominant_double3_bonus', 0)
            if straight:
                score_dom += 0.5
        if dom_pair:
            score_dom += CFG.get('dominant_pair_bonus', 0)

        base = (
            score_cov
            + score_hpr
            + score_perm
            + score_repeat
            + score_straight
            + score_single
            + score_cons
            + score_hot
            + score_mirror
            + score_dom
            + score_len
            + score_hidden
        )
        # === AAT9-SCORE-CONTRACT: END (ROW) ===

        why = ['straight' if straight else 'boxed', f'cov{rowcov}']
        if span > 1:
            why.append(f'hp_repeat{span}')
        if straight2:
            why.append('vstr2')
        if straight3:
            why.append('vstr3')
        if mirror:
            why.append('mirror')
        if single_left:
            why.append('single_left')
        if cons_full:
            why.append('cons_full')
        if hot > 0:
            why.append(f'hot{hot}')
        if dom_last:
            why.append('dom_last')
        if dom_pair:
            why.append('dom_pair')
        if cons_3v:
            why.append('cons_3v')
        if perm_count_in_box > 1:
            why.append(f'perm{perm_count_in_box}')
        if repeat_extras_in_box > 0:
            why.append('repeat_extra')
        if hidden3v_flag:
            why.append('hidden3v')

        results.append(dict(
            section=sec,
            Set=setv,
            Draw=draw,
            Column=col,
            Canonical=cpat,
            type='straight' if straight else 'boxed',
            score=base,
            rows=",".join(sorted(rowset)),
            mirror=mirror,
            straight2=straight2,
            straight3=straight3,
            single_left=single_left,
            cons_full=cons_full,
            cons_3v=cons_3v,
            cons_stub=False,
            dom_last=dom_last,
            dom_pair=dom_pair,
            hot=hot,
            perm_count_in_box=perm_count_in_box,
            repeat_extras_in_box=repeat_extras_in_box,
            horizontal_persistence_repeat=span,
            orders_modal_value=orders_modal_value,
            orders_modal_rows=orders_modal_rows,
            family_id=family_id,
            hidden3v=hidden3v_flag,
            score_cov=score_cov,
            score_hpr=score_hpr,
            score_perm=score_perm,
            score_repeat=score_repeat,
            score_straight=score_straight,
            score_single=score_single,
            score_cons=score_cons,
            score_hot=score_hot,
            score_mirror=score_mirror,
            score_dom=score_dom,
            score_len=score_len,
            score_hidden=score_hidden,
            why='|'.join(why)
        ))

    cutoff_score = CFG['min_score_to_highlight']
    keepers = {(r['section'], r['Set'], r['Draw'], r['Column'], r['Canonical']) for r in results if r['score'] >= cutoff_score}

    mask_map = {}
    for r_i, row in df.iterrows():
        setv_i = row.get('Set', '')
        draw_i = row.get('Draw', '')
        for col in COLS:
            rawval = str(row.get(col, ''))
            newmask = [False] * len(rawval)
            if rawval:
                digit_positions = [idx for idx, ch in enumerate(rawval) if ch.isdigit()]
                digit_str = ''.join(rawval[idx] for idx in digit_positions)
                for sub in find_subs(rawval):
                    csub = canon(sub)
                    if (section, setv_i, draw_i, col, csub) not in keepers:
                        continue
                    pos_idx = digit_str.find(sub)
                    while pos_idx != -1:
                        for kk in range(pos_idx, pos_idx + len(sub)):
                            if kk < len(digit_positions):
                                newmask[digit_positions[kk]] = True
                        pos_idx = digit_str.find(sub, pos_idx + 1)
                raw_digits = digits_only(rawval)
                if 1 <= len(raw_digits) <= 2:
                    key_full = (section, setv_i, draw_i, col, canon(raw_digits))
                    if key_full in keepers:
                        for kk in digit_positions:
                            newmask[kk] = True
            mask_map[(r_i, col)] = newmask

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
      "dom_last","dom_pair","family_id","hidden3v",
      "perm_count_in_box","repeat_extras_in_box",
      "horizontal_persistence_repeat","orders_modal_value","orders_modal_rows","hot",
      "score_cov","score_hpr","score_perm","score_repeat","score_straight",
      "score_single","score_cons","score_hot","score_mirror","score_dom",
      "score_len","score_hidden",
      "why"
    ]
    with open(args.csv,'w',newline='',encoding='utf-8') as fc:
        w=csv.DictWriter(fc,fieldnames=out_cols); w.writeheader()
        for r in all_rows: w.writerow({k:r.get(k,'') for k in out_cols})
    print(f"CSV   → {os.path.abspath(args.csv)}")

def _eval_single_left(*, rowcov:int, span:int, straight:bool)->bool:
    """Return True if pattern qualifies as 'single_left' according to v1.0.0 rule."""
    return straight and rowcov == 3 and span == 1

def _hot_bonus(col:str, hot:int)->int:
    """Compute hot-zone bonus with column-age weighting used in scoring."""
    col_factor = 2 if col == '1' else 1
    if hot == 2:
        return CFG['hot_level_2_bonus'] * col_factor
    if hot == 1:
        return CFG['hot_level_1_bonus'] * col_factor
    return 0

__all__ = [
    # existing exports
    'analyse','build_html','main_cli','is_3value','_eval_single_left','_hot_bonus'
]

if __name__ == "__main__":
    if st and getattr(st, '_is_running_with_streamlit', False):
        st.error("Streamlit UI for this version is not implemented yet.")
    else:
        main_cli()
