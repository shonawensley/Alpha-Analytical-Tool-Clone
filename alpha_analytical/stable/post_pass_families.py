# alpha_analytical/stable/post_pass_families.py
from collections import defaultdict, Counter
from itertools import combinations, permutations
from typing import Optional
import numpy as np
import pandas as pd

# must stay aligned with stable extractor
DIGIT2V = {'0':1,'5':1,'1':2,'6':2,'2':3,'7':3,'3':4,'8':4,'4':5,'9':5}


# import your V-TRAC lookup (centralize it under alpha_analytical/vtrac.py)
from alpha_analytical.vtrac import get_vtrac_index



def _rep3_from_classes(canon: str) -> str | None:
    if not canon or len(canon) < 3 or not canon.isdigit():
        return None
    by_class: dict[int, list[str]] = defaultdict(list)
    for ch in canon:
        v = DIGIT2V.get(ch)
        if v is None:
            return None
        by_class[v].append(ch)
    classes = sorted(by_class.keys())
    smallest = {c: sorted(by_class[c])[0] for c in classes}
    k = len(classes)
    if k == 3:
        return ''.join(sorted(smallest[c] for c in classes))
    if k == 2:
        c0, c1 = classes
        seeds = [smallest[c0], smallest[c1]]
        cnt0, cnt1 = len(by_class[c0]), len(by_class[c1])
        if cnt0 > cnt1:
            dup = smallest[c0]
        elif cnt1 > cnt0:
            dup = smallest[c1]
        else:
            dup = min(smallest[c0], smallest[c1])
        return ''.join(sorted(seeds + [dup]))
    if k == 1:
        d = smallest[classes[0]]
        return d * 3
    return None

def derive_vtrac_index_for_canonical(canon: str, get_vtrac_index) -> int | None:
    if not canon or len(canon) < 3:
        return None
    rep3 = _rep3_from_classes(canon)
    if rep3:
        vti = get_vtrac_index(rep3)
        if vti is not None:
            return vti
    digits = list(canon)
    seen = set()
    for combo in combinations(digits, 3):
        for perm in permutations(combo, 3):
            s = ''.join(perm)
            if s in seen:
                continue
            seen.add(s)
            vti = get_vtrac_index(s)
            if vti is not None:
                return vti
    return None
def build_family_summary(df_scores: pd.DataFrame, cfg: dict) -> pd.DataFrame:
    """
    Aggregates row-level stable patterns into family rows.
    family_id = vtrac_index (broad)  # fine to start broad
    Grouping keys: (section, Set, Draw, Column, family_id)
    """

    def _normalize_col_value(value: object) -> Optional[int]:
        try:
            return int(str(value))
        except (TypeError, ValueError):
            return None

    doubles_by_key: dict[tuple[object, object, object, object], set[int]] = defaultdict(set)
    consensus_by_key: dict[tuple[object, object, object, object], set[int]] = defaultdict(set)
    for _, row in df_scores.iterrows():
        fid = row.get("family_id")
        if fid is None or pd.isna(fid):
            continue
        fid = int(fid)
        key_family = (row.get("section"), row.get("Set"), row.get("Draw"), fid)
        col_int = _normalize_col_value(row.get("Column"))
        canonical = str(row.get("Canonical", ""))
        if col_int is not None and len(canonical) == 3 and len(set(canonical)) <= 2:
            doubles_by_key[key_family].add(col_int)
        if row.get("cons_full") and col_int is not None:
            consensus_by_key[key_family].add(col_int)

    rows = []

    # pre-compute front-line/rightmost stable column per (section, Set, Draw)
    # using df_scores[dom_last==True] or recompute if needed.

    g = defaultdict(lambda: {
        "rows_covered": set(),
        "perm_count_in_box": 0,
        "repeat_extras_in_box": 0,
        "horizontal_persistence_repeat": 0,
        "hot_hits": 0,
        "hot_total": 0,
        "any_straight2": False,
        "any_straight3": False,
        "any_consensus": False,
        "any_dom_last": False,
        "canonicals": Counter(),
        "modal_orders": Counter()
    })

    for _, r in df_scores.iterrows():
        canon = str(r["Canonical"])
        section, Set, Draw, Col = r["section"], r["Set"], r["Draw"], r["Column"]
        vti = derive_vtrac_index_for_canonical(canon, get_vtrac_index)
        if vti is None:
            continue
        key = (section, Set, Draw, Col, vti)
        gg = g[key]
        gg["rows_covered"].update((str(r["rows"]) or "").split(","))  # crude but workable
        gg["perm_count_in_box"] = max(gg["perm_count_in_box"], int(r.get("perm_count_in_box", 1)))
        gg["repeat_extras_in_box"] += float(r.get("repeat_extras_in_box", 0))
        gg["horizontal_persistence_repeat"] = max(
            gg["horizontal_persistence_repeat"],
            int(r.get("horizontal_persistence_repeat", 1))
        )
        hot = int(r.get("hot", 0)); gg["hot_total"] += 1; gg["hot_hits"] += (1 if hot>0 else 0)
        gg["any_straight2"] = gg["any_straight2"] or bool(r.get("straight2", False))
        gg["any_straight3"] = gg["any_straight3"] or bool(r.get("straight3", False))
        gg["any_consensus"] = gg["any_consensus"] or bool(r.get("cons_full", False))
        gg["any_dom_last"] = gg["any_dom_last"] or bool(r.get("dom_last", False))
        gg["canonicals"][canon] += 1
        mv = str(r.get("orders_modal_value", "")).strip()
        if mv:
            gg["modal_orders"][mv] += int(r.get("orders_modal_rows", 0))


    # score per family box
    out = []
    for (section, Set, Draw, Col, vti), gg in g.items():
        hot_density = (gg["hot_hits"] / gg["hot_total"]) if gg["hot_total"] else 0.0
        rows_cov = len([x for x in gg["rows_covered"] if x])
        key_family = (section, Set, Draw, int(vti))
        cons_cols = consensus_by_key.get(key_family, set())
        double_cols = doubles_by_key.get(key_family, set())
        col_int = _normalize_col_value(Col)
        any_doubles_support = False
        if gg["any_consensus"] and col_int is not None and double_cols:
            for d_col in double_cols:
                if abs(d_col - col_int) <= 1:
                    any_doubles_support = True
                    break
        # === AAT9-SCORE-CONTRACT: BEGIN (FAMILY) ===
        fam_cov = rows_cov * cfg["vertical_coverage_per_row"]
        fam_hpr = gg["horizontal_persistence_repeat"] * cfg["horizontal_persistence_repeat_bonus"]
        fam_perm = max(0, gg["perm_count_in_box"]-1) * cfg.get("perm_density_per_extra", 0)
        fam_repeat = gg["repeat_extras_in_box"] * cfg.get("repeat_count_per_extra", 0)
        fam_cons = cfg.get("consensus_family_bonus", 0) if gg["any_consensus"] else 0
        fam_hot = cfg.get("hotzone_family_bonus", 0) if hot_density >= 0.5 else 0
        fam_straight2 = cfg.get("straight_2rows_bonus", 0) if gg["any_straight2"] else 0
        fam_straight3 = cfg.get("straight_3rows_bonus", 0) if gg["any_straight3"] else 0
        fam_doubles = cfg.get("doubles_trigger_bonus", 0) if any_doubles_support else 0
        fam_score = (
            fam_cov
            + fam_hpr
            + fam_perm
            + fam_repeat
            + fam_cons
            + fam_hot
            + fam_straight2
            + fam_straight3
            + fam_doubles
        )
        # === AAT9-SCORE-CONTRACT: END (FAMILY) ===
        out.append({
            "section": section, "Set": Set, "Draw": Draw, "Column": Col,
            "family_id": vti,
            "rows_cov": rows_cov,
            "perm_count_in_box": gg["perm_count_in_box"],
            "repeat_extras_in_box": gg["repeat_extras_in_box"],
            "horizontal_persistence_repeat": gg["horizontal_persistence_repeat"],
            "hot_density": round(hot_density, 3),
            "any_straight2": gg["any_straight2"],
            "any_straight3": gg["any_straight3"],
            "any_consensus": gg["any_consensus"],
            "any_dom_last": gg["any_dom_last"],
            "any_doubles_support": any_doubles_support,
            "top_canonicals": ";".join([f"{k}:{v}" for k, v in gg["canonicals"].most_common(3)]),
            "top_modal_orders": ";".join([f"{k}:{v}" for k, v in gg["modal_orders"].most_common(3)]),
            "fam_cov": fam_cov,
            "fam_hpr": fam_hpr,
            "fam_perm": fam_perm,
            "fam_repeat": fam_repeat,
            "fam_cons": fam_cons,
            "fam_hot": fam_hot,
            "fam_straight2": fam_straight2,
            "fam_straight3": fam_straight3,
            "fam_doubles": fam_doubles,
            "fam_section_bonus": 0.0,
            "fam_progression_bonus": 0.0,
            "fam_last_remaining_bonus": 0.0,
            "family_score": fam_score,
        })

    df = pd.DataFrame(out)
    if df.empty:
        return df

    keys = ["Set", "Draw", "Column", "family_id"]
    df["section_count"] = df.groupby(keys)["section"].transform("nunique")
    df["section_count"] = df["section_count"].fillna(0).astype(int)
    section_bonus = np.maximum(0, df["section_count"] - 1) * cfg.get("vtrac_family_presence", 1)
    section_bonus += np.where(df["section_count"] == 3, cfg.get("cross_section_triple", 2), 0)
    df["fam_section_bonus"] = section_bonus
    df["family_score"] += section_bonus

    def _normalize_set_value(value: object) -> Optional[int]:
        if value is None:
            return None
        digits = "".join(ch for ch in str(value) if ch.isdigit())
        return int(digits) if digits else None

    def _has_progression(values: list[Optional[int]]) -> bool:
        seq = sorted({v for v in values if v is not None})
        if len(seq) < 2:
            return False
        run = 1
        for idx in range(1, len(seq)):
            if seq[idx] == seq[idx - 1] + 1:
                run += 1
                if run >= 2:
                    return True
            else:
                run = 1
        return False

    df["_set_num"] = df["Set"].apply(_normalize_set_value)
    df["progression_flag"] = df.groupby(["section", "Draw", "Column", "family_id"])["_set_num"].transform(
        lambda nums: _has_progression(nums.tolist())
    )
    df["progression_flag"] = df["progression_flag"].fillna(False).astype(bool)
    progression_bonus = df["progression_flag"].astype(int) * cfg.get("progression_across_sets", 1)
    df["fam_progression_bonus"] = progression_bonus
    df["family_score"] += progression_bonus

    df["last_remaining_3v"] = False
    for (sec, setv, draw), box in df.groupby(["section", "Set", "Draw"]):
        stable = box[box["rows_cov"] >= 3].copy()
        if stable.empty:
            continue
        stable["col_int"] = pd.to_numeric(stable["Column"], errors="coerce")
        stable = stable.dropna(subset=["col_int"])
        if stable.empty:
            continue
        col_max = int(stable["col_int"].max())
        survivors = stable[stable["col_int"] == col_max]
        fams = survivors["family_id"].dropna().unique()
        if len(fams) == 1:
            fid = fams[0]
            mask = (
                (df["section"] == sec)
                & (df["Set"] == setv)
                & (df["Draw"] == draw)
                & (df["Column"] == str(col_max))
                & (df["family_id"] == fid)
            )
            df.loc[mask, "last_remaining_3v"] = True
            bonus = cfg.get("last_remaining_3v_bonus", 3)
            df.loc[mask, "fam_last_remaining_bonus"] += bonus
            df.loc[mask, "family_score"] += bonus

    df["last_remaining_3v"] = df["last_remaining_3v"].fillna(False).astype(bool)
    df["fam_last_remaining_bonus"] = df["fam_last_remaining_bonus"].fillna(0.0)
    df.drop(columns=["_set_num"], inplace=True)

    df = df.sort_values(["section", "Set", "Draw", "Column", "family_score"], ascending=[True, True, True, True, False]).reset_index(drop=True)

    return df













