# modules/sums_ui.py

from typing import Dict, Any, List
import pandas as pd

COLOR_CLASS = {
    "blue": "blue",
    "red": "red",
    "purple": "purple",
}

def _flag_to_badge(flags: Dict[str, bool]) -> str:
    badges: List[str] = []
    for key, val in flags.items():
        if val:
            css = COLOR_CLASS.get(key, "")
            badges.append(f'<span class="{css}">{key}</span>')
    return " ".join(badges) if badges else ""

def build_sums_dataframe(stats: Dict[str, Any]) -> pd.DataFrame:
    """
    Convert stats dict from calculate_sums_stats() to a compact table for UI.
    """
    rows = []
    for s, m in sorted(stats["by_sum"].items(), key=lambda kv: kv[0]):
        rows.append({
            "Type": "Sum",
            "Bucket": s,
            "Hits": m["count"],
            "Expected": round(m["expected"], 2),
            "Hit %": round(100 * m["hit_rate"], 1),
            "Exp %": round(100 * m["exp_rate"], 1),
            "Z": round(m["z"], 2),
            "Draws Since": m["draws_since"],
            "Flags": _flag_to_badge(m["flags"]),
        })
    for r, m in sorted(stats["by_root_sum"].items(), key=lambda kv: kv[0]):
        rows.append({
            "Type": "Root",
            "Bucket": r,
            "Hits": m["count"],
            "Expected": round(m["expected"], 2),
            "Hit %": round(100 * m["hit_rate"], 1),
            "Exp %": round(100 * m["exp_rate"], 1),
            "Z": round(m["z"], 2),
            "Draws Since": m["draws_since"],
            "Flags": _flag_to_badge(m["flags"]),
        })
    return pd.DataFrame(rows)
