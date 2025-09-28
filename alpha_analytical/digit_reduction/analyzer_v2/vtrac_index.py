# alpha_analytical/digit_reduction/analyzer_v2/vtrac_index.py
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Set, Tuple, Iterable, Optional
import json
import re
from collections import Counter, defaultdict

# Canonical digit→V family mapping used across AAT9 (0/5→1, 1/6→2, 2/7→3, 3/8→4, 4/9→5)
# Matches Stable-Pattern and V-TRAC docs. (See AAT9 Module D: V-TRAC Analyzer + Stable Pattern HTML.) 
VTRAC_MAP = {'0':'1','5':'1','1':'2','6':'2','2':'3','7':'3','3':'4','8':'4','4':'5','9':'5'}

def to_vtrac_str(s: str) -> str:
    """Map each digit to its V family (preserve order and duplicates)."""
    if not s: return ""
    return "".join(VTRAC_MAP.get(ch, "") for ch in s if ch.isdigit())

def vtrac_set(s: str) -> str:
    """Sorted unique V families for the given digit string (e.g., '467' -> '24')."""
    vv = to_vtrac_str(s)
    return "".join(sorted(set(vv))) if vv else ""

@dataclass
class VHotSpec:
    """Hot V families used for synergy, with optional human context."""
    families: Set[str]           # e.g., {'12','24','135'} (strings of 1..5)
    source: str                  # 'predictions_json' | 'derived_from_DR' | 'none'
    detail: Dict[str, float]     # optional strength per family (0..1)

# -------- (A) Optional: load hot families from V-TRAC predictions JSON ----------
def _find_latest_json(pred_dir: Path, state: str) -> Optional[Path]:
    """Return the most recent *<STATE>* predictions JSON if present."""
    if not pred_dir.exists(): return None
    cand: List[Tuple[float, Path]] = []
    for p in pred_dir.glob(f"*{state}*.*json"):
        try:
            cand.append((p.stat().st_mtime, p))
        except Exception:
            continue
    if not cand: return None
    cand.sort(reverse=True)
    return cand[0][1]

def _extract_indices(payload: dict) -> List[int]:
    """
    Heuristically extract top V-TRAC indices from various shapes:
      - {"top_indices":[{"index":17,"score":...}, ...]}
      - {"ranked":[{"id":23}, ...]}
      - {"indices":{"17":{"score":...}, "31":{...}}}
    Returns a list of ints (may be empty).
    """
    out: List[int] = []
    if isinstance(payload.get("top_indices"), list):
        for it in payload["top_indices"]:
            idx = it.get("index") or it.get("id") or it.get("idx")
            if isinstance(idx, int): out.append(idx)
    if isinstance(payload.get("ranked"), list) and not out:
        for it in payload["ranked"]:
            idx = it.get("index") or it.get("id") or it.get("idx")
            if isinstance(idx, int): out.append(idx)
    if isinstance(payload.get("indices"), dict) and not out:
        for k in payload["indices"].keys():
            try: out.append(int(k))
            except Exception: pass
    return out

def _indices_to_families(indices: Iterable[int]) -> Set[str]:
    """
    Convert V-TRAC index numbers into boxed V families.
    If a project-wide BOXED_VTRAC_REFERENCE table is available in your V-TRAC utils,
    adapt this function to map index→family exactly.
    For now we conservatively return an empty set; synergy will fall back to DR-derived families.
    """
    # Placeholder: uncomment/replace when you wire the real table:
    # from utils.vtrac_utils import BOXED_VTRAC_REFERENCE   # per AAT9 Module D
    # fams = set()
    # for idx in indices:
    #     entry = BOXED_VTRAC_REFERENCE.get(idx)
    #     if entry:
    #         fams.add("".join(sorted(set(str(x) for x in entry["families"]))))
    # return fams
    return set()

def try_load_hot_families_from_predictions(state: str,
                                           predictions_dir: Path) -> Optional[VHotSpec]:
    """
    Try to read V‑TRAC predictions JSON and translate into hot V families.
    Gracefully returns None if not present or cannot map to families.
    """
    latest = _find_latest_json(predictions_dir, state)
    if not latest: 
        return None
    try:
        payload = json.loads(latest.read_text(encoding="utf-8"))
    except Exception:
        return None
    idx = _extract_indices(payload)
    fams = _indices_to_families(idx)
    if not fams:
        return None
    # Optionally derive a simple strength ~ rank/score here if available.
    return VHotSpec(families=fams, source="predictions_json", detail={f: 1.0 for f in fams})

# -------- (B) Fallback: derive hot families directly from the DR feature table ---
def derive_hot_families_from_dr(df_rows: Iterable[dict],
                                min_methods: int = 2,
                                prefer_section: str = "Combined",
                                top_k: int = 5) -> VHotSpec:
    """
    Compute V family prevalence using your DR features themselves.
    Signals:
      • present across ≥min_methods at the same location
      • appears in the preferred section more often (defaults to 'Combined')
      • has broad coverage across columns or sets
    Returns top_k families scaled to 0..1 strength.
    """
    bucket: Dict[str, Dict[str, int]] = defaultdict(lambda: {"count":0, "methods":0, "sections":0, "cols":0, "sets":0, "pref":0})
    seen_keys = set()
    for r in df_rows:
        sig = str(r.get("final_3canon") or "")
        if not sig: 
            continue
        fam = vtrac_set(sig)  # e.g., '24'
        if not fam:
            continue
        k = (r["area"], r["section"], r["set"], r["draw"], r["col"], r["mode"], r["method"], sig)
        if k in seen_keys: 
            continue
        seen_keys.add(k)
        node = bucket[fam]
        node["count"] += 1
        node["methods"] += 1  # approximated per unique (method,sig) above
        node["sections"] += 1
        node["cols"] += 1
        node["sets"] += 1
        if str(r.get("section")) == prefer_section:
            node["pref"] += 1

    # Score families by a simple, robust composite (normalized later)
    score: Dict[str, float] = {}
    for fam, m in bucket.items():
        s = (1.0 * m["count"] +
             0.5 * m["methods"] +
             0.5 * m["cols"] +
             0.5 * m["sets"] +
             0.6 * m["pref"])
        score[fam] = float(s)
    if not score:
        return VHotSpec(families=set(), source="none", detail={})
    # Top-K & normalize to 0..1
    ranked = sorted(score.items(), key=lambda kv: kv[1], reverse=True)[:max(1, top_k)]
    mx = max(v for _, v in ranked) or 1.0
    detail = {fam: (val / mx) for fam, val in ranked}
    return VHotSpec(families=set(detail.keys()), source="derived_from_DR", detail=detail)
