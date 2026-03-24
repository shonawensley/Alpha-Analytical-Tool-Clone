import json
from pathlib import Path

from scripts.tools.review_stable_survivor_capture import build_survivor_capture_audit


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def test_survivor_capture_audit_flags_progression_and_arena_compression(tmp_path: Path) -> None:
    repo_root = tmp_path
    sharepacks_root = repo_root / "sharepacks"
    state_dir = sharepacks_root / "2025-01-01" / "TestState"
    stable_dir = state_dir / "stable" / "TestState"
    winners_dir = state_dir / "winners" / "TestState"

    _write(
        stable_dir / "TestState_stable_patterns_scores.csv",
        "\n".join(
            [
                "section,Set,Draw,Column,Canonical,type,score,rows,mirror,straight2,straight3,single_left,cons_full,cons_3v,cons_stub,dom_last,dom_pair,hot,perm_count_in_box,repeat_extras_in_box,horizontal_persistence_repeat,orders_modal_value,orders_modal_rows,family_id,hidden3v,score_cov,score_hpr,score_perm,score_repeat,score_straight,score_single,score_cons,score_hot,score_mirror,score_dom,score_len,score_hidden,score_vtrac_straight,score_persistence_set,score_persistence_draw,persistence_set_count,persistence_draw_run,score_double_mirror,double_mirror,why",
                "Combined,Set1,Draw1,1,756,straight,21.0,\"R2,R4,R6,R8\",False,True,False,False,False,False,False,False,False,1,1,0,3,756,4,7.0,False,8,3,1,0,4,0,0,2,0,0,0,0.5,1,2,2,3,0,False,frontier",
                "Combined,Set1,Draw1,2,756,straight,25.0,\"R2,R4,R6,R8\",False,True,False,False,False,False,False,False,False,1,1,0,4,756,4,7.0,False,8,4,1,0,4,0,0,2,0,0,0,0.5,1,2,3,3,0,False,frontier",
                "Combined,Set1,Draw1,2,765,straight,24.0,\"R2,R4,R6,R8\",False,True,False,False,False,False,False,False,False,1,1,0,4,765,4,7.0,False,8,4,1,0,4,0,0,2,0,0,0,0.5,1,2,3,3,0,False,frontier",
            ]
        )
        + "\n",
    )
    _write(
        stable_dir / "TestState_stable_patterns_families.csv",
        "\n".join(
                [
                    "section,Set,Draw,Column,family_id,rows_cov,perm_count_in_box,repeat_extras_in_box,horizontal_persistence_repeat,hot_density,any_straight2,any_straight3,any_consensus,any_dom_last,any_doubles_support,any_vtrac_straight,any_hidden3v,max_persistence_set,max_persistence_draw,persistence_set_count,persistence_draw_run,hidden3v_hits,hot1_count,hot2_count,consensus_hits,top_canonicals,top_modal_orders,fam_cov,fam_hpr,fam_perm,fam_repeat,fam_cons,fam_hot,fam_straight2,fam_straight3,fam_doubles,fam_vtrac,fam_hidden,fam_double_mirror,fam_persistence,fam_section_bonus,fam_progression_bonus,fam_last_remaining_bonus,family_score,best_compound_score,section_count,progression_flag,last_remaining_3v",
                    "Combined,Set1,Draw1,1,12,4,1,0,3,1.0,True,False,False,False,False,False,False,2,2,2,2,0,0,1,0,756:1;7567:1;765:1,756:1,8,3,1,0,0,1,2,0,0,0,0,0,2,0,1,0,28.0,51.0,1,True,False",
                    "Combined,Set1,Draw1,2,12,4,1,0,4,1.0,True,False,False,False,False,False,False,2,3,2,3,0,0,1,0,756:1;7567:1;765:1,756:1,8,4,1,0,0,1,2,0,0,0,0,0,3,0,1,3,33.0,55.0,1,True,True",
                ]
            )
            + "\n",
        )
    _write(
        stable_dir / "TestState_stable_patterns_compound.csv",
        "section,Canonical,compound_score,base_max_score,why,why_tags,col1_hits,consensus_hits,double_mirror_hits,set_chain_depth,draw_chain_depth,examples\n"
        "Combined,756,55.0,25.0,frontier,frontier,1,0,0,1,1,Set1/Draw1/Col2\n",
    )
    _write(
        stable_dir / "TestState_metrics.json",
        json.dumps(
            {
                "generated_at": "2026-03-23T00:00:00+00:00",
                "state": "TestState",
                "total_patterns": 3,
                "total_families": 1,
                "compression_ratio": 0.1,
                "avg_top_hot_density": 1.0,
                "health": {"compound_rows": 1, "funnel_precol1": 0, "vt_only_lane": 0},
                "signals": {"consensus_of_consensus": False, "hot2_bias": False},
                "evidence_schema_version": 1,
                "stable_contract_version": 1,
                "compound_schema_version": 1,
            }
        )
        + "\n",
    )
    _write(
        winners_dir / "TestState_vtrac7_winner_756_20260101_010101.html",
        """
<html><body>
<h2>TestState Combined Combined Table</h2>
<table>
  <tr><th>Set</th><th>Draw</th><th>RowType</th><th>7</th><th>6</th><th>5</th><th>4</th><th>3</th><th>2</th><th>1</th></tr>
  <tr><td>Set1</td><td>Draw1</td><td>R2</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td class="ls-box ls-box-edge"><span class="hit-winner">756</span></td><td>NA</td></tr>
</table>
</body></html>
""".strip()
        + "\n",
    )

    payload = build_survivor_capture_audit(
        repo_root=repo_root,
        sharepacks_root=sharepacks_root,
        case_specs=["2025-01-01:TestState"],
        min_rows_cov=3,
    )

    case = payload["cases"][0]
    summary = case["summary"]

    assert summary["raw_frontier_boxes"] == 1
    assert summary["raw_progression_chain_boxes"] == 2
    assert summary["html_ls_boxes"] == 1
    assert summary["raw_frontier_overlapping_html_ls"] == 1
    assert summary["raw_frontier_overlapping_html_winner"] == 1
    assert summary["arena_frontier_boxes"] == 1
    assert summary["arena_pattern_compression_boxes"] == 0
    assert summary["arena_progression_preserved_sequences"] == 1
    assert summary["arena_progression_snapshot_sequences"] == 0
    assert summary["last_remaining_profile_counts"] == {"multi_literal_single_vtrac_family_with_hidden_support": 1}
    assert summary["last_remaining_support_counts"] == {"winner_hidden": 1}
    assert summary["last_remaining_enriched_profile_counts"] == {
        "multi_literal_single_vtrac_family_with_hidden_support__winner_hidden": 1
    }

    frontier_box = next(item for item in case["ledger"] if item["raw_frontier"])
    assert frontier_box["box_key"] == "Combined:Set1:Draw1:Col2"
    assert frontier_box["raw_exact3digit_patterns"] == "756,765"
    assert frontier_box["raw_hidden_terminal_patterns"] == "7567"
    assert frontier_box["arena_exact3digit_patterns"] == "756,765"
    assert frontier_box["raw_exact3digit_missing_from_arena"] == ""
    assert frontier_box["last_remaining_profile"] == "multi_literal_single_vtrac_family_with_hidden_support"
    assert frontier_box["last_remaining_support_class"] == "winner_hidden"
    assert frontier_box["last_remaining_enriched_profile"] == (
        "multi_literal_single_vtrac_family_with_hidden_support__winner_hidden"
    )
    assert "arena_progression_preserved" in frontier_box["gap_tags"]
    assert "html_ls_box_on_raw_frontier" in frontier_box["gap_tags"]
