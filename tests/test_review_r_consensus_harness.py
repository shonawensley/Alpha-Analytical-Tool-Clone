import json
from pathlib import Path

from scripts.tools.review_r_consensus_harness import (
    build_r_consensus_harness,
    write_r_consensus_harness_outputs,
)


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _aux_summary() -> str:
    payload = {
        "state": "TestState",
        "date": "2025-01-01",
        "draw_sources": {},
        "config": {},
        "repeat_watch": {},
        "positional": {
            "shortlist_report": {
                "variant_top_digits": {},
                "aggregated_digits": {},
                "candidates": [],
                "consensus_notes": ["P1 digit 7 aligns across Combined, Midday (XVAR-Cons(CM))"],
                "double_pressure_notes": ["Digit 7 pressing two positions (Double-Pressure)"],
            }
        },
        "doubles": {
            "by_variant": {"midday": []},
            "multi_variant_alerts": [],
            "top_by_variant": {"midday": [{"combo": "177", "draws_since": 50, "severity": "B"}]},
        },
        "pairs": {
            "by_variant": {"midday": {}},
            "multi_variant_alerts": [],
            "top_by_variant": {"midday": {"repeating": [{"pair": "17", "draws_since": 20}], "non_repeating": []}},
        },
        "vtrac": {"overlay_by_variant": {}, "heatboard_by_variant": {}, "overlay_top": {"midday": [{"index": 20, "draws_since": 30}]}, "heatboard_top": {}},
        "sums": {"by_variant": {}, "top_by_variant": {"midday": [{"sum": 15, "flags": {"red": True}}]}},
        "blackapple": {"by_variant": {}, "top_by_variant": {"midday": [{"combo": "177", "score": 2, "tags": ["RS"]}]}}
    }
    return json.dumps(payload)


def test_r_consensus_harness_builds_event_and_outputs(tmp_path: Path) -> None:
    repo_root = tmp_path
    sharepacks_root = repo_root / "sharepacks"

    date_dir = sharepacks_root / "2025-01-01" / "TestState"
    next_date_dir = sharepacks_root / "2025-01-02" / "TestState"

    _write(date_dir / "aux" / "draws" / "TestState_Midday_draws.csv", "Draw\n771\n")
    _write(date_dir / "aux" / "draws" / "TestState_Evening_draws.csv", "Draw\n345\n")
    _write(next_date_dir / "aux" / "draws" / "TestState_Midday_draws.csv", "Draw\n999\n")
    _write(next_date_dir / "aux" / "draws" / "TestState_Evening_draws.csv", "Draw\n123\n")

    _write(date_dir / "aux" / "TestState" / "summary.json", _aux_summary())
    _write(
        date_dir / "json" / "TestState_tables.json",
        json.dumps(
            {
                "state_name": "TestState",
                "sections": {
                    "Midday": {
                        "sets": {
                            "Set1": {
                                "Draw1": {
                                    "draw_data": [],
                                        "metadata": {"hot_zone_count": 12, "is_hot_zone": True},
                                        "pattern_variations": {
                                            "R2": ["", "", "", "", "1234", "5612", "1377"],
                                            "R4": ["", "", "", "", "2234", "1513", "1777"],
                                            "R6": ["", "", "", "", "3234", "3514", "3077"],
                                            "R8": ["", "", "", "", "4234", "1515", "1177"],
                                        },
                                    }
                                }
                            }
                    }
                },
            }
        ),
    )
    _write(
        date_dir / "stable" / "TestState" / "TestState_stable_patterns_scores.csv",
        "\n".join(
            [
                "section,Set,Draw,Column,Canonical,type,score,rows,mirror,straight2,straight3,single_left,cons_full,cons_3v,cons_stub,dom_last,dom_pair,hot,perm_count_in_box,repeat_extras_in_box,horizontal_persistence_repeat,orders_modal_value,orders_modal_rows,family_id,hidden3v,score_cov,score_hpr,score_perm,score_repeat,score_straight,score_single,score_cons,score_hot,score_mirror,score_dom,score_len,score_hidden,score_vtrac_straight,score_persistence_set,score_persistence_draw,persistence_set_count,persistence_draw_run,score_double_mirror,double_mirror,why",
                "Midday,Set1,Draw1,1,77,consensus_stub,4.0,,False,False,False,False,True,False,True,False,True,1,1,0,1,,0,,False,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,False,consensus_stub",
                "Midday,Set1,Draw1,1,177,straight,24.0,\"R2,R4,R6,R8\",False,True,True,False,True,True,False,False,False,1,1,0,4,771,4,20,False,8,2,1,0,4,0,2,1,0,0,0,0,1,1,2,2,3,0,False,straight|cons_full|cons_3v|hp_repeat6|set_chain3",
                "Midday,Set1,Draw1,2,157,straight,19.0,\"R2,R4,R6,R8\",False,True,False,False,False,False,False,False,False,1,1,0,3,517,3,20,False,8,2,1,0,4,0,0,1,0,0,0,0,1,1,1,1,2,0,False,straight|hp_repeat4",
                "Midday,Set1,Draw1,3,137,straight,17.0,\"R2,R4,R6,R8\",False,True,False,False,False,False,False,False,False,1,1,0,3,731,3,21,False,8,2,1,0,4,0,0,1,0,0,0,0,1,1,1,1,2,0,False,straight|hp_repeat4"
            ]
        )
        + "\n",
    )
    _write(
        date_dir / "winners" / "TestState" / "TestState_vtrac20_winner_771_20250101_010101.json",
        json.dumps({"winner_combo": "771", "index": 20, "patterns": ["177", "717", "771"]}),
    )
    _write(
        date_dir / "winners" / "TestState" / "TestState_vtrac20_winner_771_20250101_010101.html",
        "<html><body>winner 771</body></html>\n",
    )

    payload = build_r_consensus_harness(repo_root=repo_root, sharepacks_root=sharepacks_root)

    assert payload["event_count"] == 1
    event = payload["events"][0]
    assert event["tail_value"] == "77"
    assert event["event_class"] == "two-digit"
    assert event["stable_flags"]["cons_stub"] is True
    assert event["same_day_any"] is True
    assert event["classic_same_day"]["exact_straight"]["combo"] == "771"
    assert event["primary_function"] in {"doubles trigger", "mixed", "VTRAC-index amplifier"}

    output_dir = repo_root / "docs" / "RUNS"
    paths = write_r_consensus_harness_outputs(payload, output_dir=output_dir, prefix_date="2026-03-24")
    assert Path(paths["roster_csv"]).exists()
    assert Path(paths["rollup_md"]).exists()
    assert Path(paths["rollup_json"]).exists()
    events_dir = Path(paths["events_dir"])
    assert (events_dir / f"{event['event_id']}.md").exists()
    assert (events_dir / f"{event['event_id']}.json").exists()
