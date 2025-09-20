# alpha_analytical/stable/post_pass_families.py
from collections import defaultdict, Counter
import pandas as pd
from itertools import combinations, permutations

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
    rows = []

    # pre-compute front-line/rightmost stable column per (section, Set, Draw)
    # using df_scores[dom_last==True] or recompute if needed.

    g = defaultdict(lambda: {
        "rows_covered": set(),
        "perm_count_in_box": 0,
        "repeat_extras_in_box": 0,
        "hp_span": 0,
        "hot_hits": 0,
        "hot_total": 0,
        "any_straight2": False,
        "any_straight3": False,
        "any_consensus": False,
        "any_dom_last": False,
        "canonicals": Counter(),
        "modal_orders": Counter(),
    })

    for _, r in df_scores.iterrows():
        canon = str(r["Canonical"])
        section, Set, Draw, Col = r["section"], r["Set"], r["Column"], r["Draw"]
        vti = derive_vtrac_index_for_canonical(canon, get_vtrac_index)
        if vti is None:
            continue
        key = (section, Set, Draw, Col, vti)
        gg = g[key]
        gg["rows_covered"].update((str(r["rows"]) or "").split(","))  # crude but workable
        gg["perm_count_in_box"] = max(gg["perm_count_in_box"], int(r.get("perm_count_in_box", 1)))
        gg["repeat_extras_in_box"] += float(r.get("repeat_extras_in_box", 0))
        gg["hp_span"] = max(gg["hp_span"], int(r.get("hp_span", 1)))
        hot = int(r.get("hot", 0)); gg["hot_total"] += 1; gg["hot_hits"] += (1 if hot>0 else 0)
        gg["any_straight2"] = gg["any_straight2"] or bool(r.get("straight2", False))
        gg["any_straight3"] = gg["any_straight3"] or bool(r.get("straight3", False))
        gg["any_consensus"] = gg["any_consensus"] or bool(r.get("cons_full", False))
        gg["any_dom_last"] = gg["any_dom_last"] or bool(r.get("dom_last", False))
        gg["canonicals"][canon] += 1
        mv = str(r.get("orders_modal_value","")).strip()
        if mv: gg["modal_orders"][mv] += int(r.get("orders_modal_rows", 0))

    # score per family box
    out = []
    for (section, Set, Draw, Col, vti), gg in g.items():
        hot_density = (gg["hot_hits"] / gg["hot_total"]) if gg["hot_total"] else 0.0
        rows_cov = len([x for x in gg["rows_covered"] if x])
        fam_score = (
            rows_cov * cfg["vertical_coverage_per_row"]
            + gg["hp_span"] * cfg["horizontal_span_per_col"]
            + max(0, gg["perm_count_in_box"]-1) * cfg["perm_density_per_extra"]
            + gg["repeat_extras_in_box"] * cfg["repeat_count_per_extra"]
            + (cfg["consensus_family_bonus"] if gg["any_consensus"] else 0)
            + (cfg["last_remaining_3v_bonus"] if gg["any_dom_last"] else 0)
            + (cfg["hotzone_family_bonus"] if hot_density >= 0.5 else 0)
            + (cfg["straight_2rows_bonus"] if gg["any_straight2"] else 0)
            + (cfg["straight_3rows_bonus"] if gg["any_straight3"] else 0)
        )
        out.append({
            "section": section, "Set": Set, "Draw": Draw, "Column": Col,
            "family_id": vti,
            "rows_cov": rows_cov,
            "perm_count_in_box": gg["perm_count_in_box"],
            "repeat_extras_in_box": gg["repeat_extras_in_box"],
            "hp_span": gg["hp_span"],
            "hot_density": round(hot_density,3),
            "any_straight2": gg["any_straight2"],
            "any_straight3": gg["any_straight3"],
            "any_consensus": gg["any_consensus"],
            "any_dom_last": gg["any_dom_last"],
            "top_canonicals": ";".join([f"{k}:{v}" for k,v in gg["canonicals"].most_common(3)]),
            "top_modal_orders": ";".join([f"{k}:{v}" for k,v in gg["modal_orders"].most_common(3)]),
            "family_score": fam_score,
        })

    df = pd.DataFrame(out).sort_values(["section","Set","Draw","Column","family_score"], ascending=[True,True,True,True,False]).reset_index(drop=True)

    # (Optional) Cross-section & progression bonuses can be added in a second pass
    # grouping by (Set,Draw,Column,family_id) across sections, and Set progression Draw=1 across sets.

    return df
