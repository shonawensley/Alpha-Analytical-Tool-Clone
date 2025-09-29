def score_row(row: dict, W: dict, T: dict) -> float:
    s = 0.0
    # P2 core
    s += W.get("w_time_to_3value_fast",0)   * int(row.get("time_to_3",99) <= 3)
    s += W.get("w_stabilizes_after_3",0)    * int(row.get("post3_span",0) >= 1)
    s += W.get("w_terminal_is_3value",0)    * int(row.get("terminal_unique",9) <= 3 and row.get("terminal_len",0) in (1,2,3))
    s += W.get("w_terminal_unique_1",0)     * int(row.get("terminal_unique",9) == 1)
    s += W.get("w_terminal_unique_2",0)     * int(row.get("terminal_unique",9) == 2)
    s += W.get("w_terminal_len_3",0)        * int(row.get("terminal_len",0) == 3)
    s += W.get("w_pivot_tightens",0)         * int(row.get("pivot_tightens", False))
    s += W.get("w_pivot_same_final_set",0)   * int(row.get("pivot_same_final_set", False))
    s += W.get("w_pivot_earlier_first3",0)   * int(row.get("pivot_time_delta", 0) > 0)
    s += W.get("w_set_carry",0)              * int(row.get("set_carry", False) or row.get("set.linger", False))
    s += W.get("w_box_carry",0)              * int(row.get("box_carry", False))
    s += W.get("w_method_consensus2",0)      * int(row.get("method_agree",0) >= 2 or row.get("method.agree_flag", False))
    s += W.get("w_method_consensus3",0)      * int(row.get("method_agree",0) >= 3)
    s += W.get("w_method_consensus4",0)      * int(row.get("method_agree",0) >= 4)
    s += W.get("w_prer_pure3value",0)        * int(row.get("pre.orig_unique",99) <= 3)
    s += W.get("w_permutation_density",0)    * (row.get("perm_count",0) / 6.0)

    # P1 extras
    s += W.get("tail.exact_len3",0)          * int(row.get("tail.exact_len3",0)==1)
    s += W.get("tail.unique2",0)             * int(row.get("tail.unique2",0)==1)
    s += W.get("traj.early_terminal",0)      * int(row.get("traj.early_terminal",0)==1)
    s += W.get("traj.reduction_slope",0)     * float(row.get("traj.reduction_slope",0.0))
    s += W.get("pre.mirror_pair",0)          * int(row.get("pre.mirror_pair",0)==1)
    s += W.get("stability.order_cue",0)      * float(row.get("stability.order_cue",0.0))
    s += W.get("stability.horiz_persist",0)  * float(row.get("stability.horiz_persist",0.0))
    # penalties (P1)
    s += W.get("penalties.tail.wobble",0)    * float(row.get("tail.wobble",0.0))
    s += W.get("penalties.mode.only_one",0)  * float(row.get("mode.only_one",0.0))
    s += W.get("penalties.degenerate.empty",0)* float(row.get("degenerate.empty",0.0))

    # Light V‑TRAC synergy (optional)
    s += W.get("w_vtrac_hot_index",0)        * int(row.get("v_hot", False))

    return float(s)
