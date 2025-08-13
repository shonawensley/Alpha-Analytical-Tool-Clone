"""
Quick verification harness for Aux vs. legacy parity (Connecticut example).

Run:  python scripts/verify_ct_aux_vs_legacy.py
Outputs three checks:
- newest 5 and oldest 5 draws
- Top 5 overdue repeating pairs snapshot from last 100 draws
- V-TRAC table row count
"""

from modules.module_d_auxiliary_tools.integration import run_aux_tools
from modules.module_d_auxiliary_tools.refactored.extractor import extract_draw_list, validate_draw_data


def main():
    state = "Connecticut4"
    draws = validate_draw_data(extract_draw_list(state))
    print(f"[VERIFY] {state} first5(newest): {draws[:5]}")
    print(f"[VERIFY] {state} last5(oldest): {draws[-5:]}")

    # Run aux and read the derived overdue pairs
    res = run_aux_tools(state)
    overdue = res.get("overdue_pairs")
    if overdue is not None and not overdue.empty:
        rep = overdue[overdue.get("Type") == "Repeating"].sort_values("Draws_Overdue", ascending=False)
        top5 = rep.head(5)[["Pair", "Draws_Overdue"]].values.tolist()
        print("[VERIFY] Top5 repeating pairs snapshot:", top5)
    else:
        print("[VERIFY] Overdue pairs empty")

    boxed = res.get("boxed_vtrac")
    print("[VERIFY] VTRAC_DISPLAY rows:", (len(boxed) if boxed is not None else 0))


if __name__ == "__main__":
    main()


