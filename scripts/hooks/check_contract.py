#!/usr/bin/env python
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

sys.dont_write_bytecode = True
REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))


REQUIRED_ROW_COLUMNS = {
    "section",
    "Set",
    "Draw",
    "Column",
    "Canonical",
    "type",
    "score",
    "rows",
    "mirror",
    "straight2",
    "straight3",
    "single_left",
    "cons_full",
    "cons_3v",
    "cons_stub",
    "dom_last",
    "dom_pair",
    "family_id",
    "hidden3v",
    "perm_count_in_box",
    "repeat_extras_in_box",
    "horizontal_persistence_repeat",
    "orders_modal_value",
    "orders_modal_rows",
    "hot",
    "score_cov",
    "score_hpr",
    "score_perm",
    "score_repeat",
    "score_straight",
    "score_single",
    "score_cons",
    "score_hot",
    "score_mirror",
    "score_dom",
    "score_len",
    "score_hidden",
    "why",
}

REQUIRED_FAMILY_COLUMNS = {
    "section",
    "Set",
    "Draw",
    "Column",
    "family_id",
    "rows_cov",
    "perm_count_in_box",
    "repeat_extras_in_box",
    "horizontal_persistence_repeat",
    "hot_density",
    "any_straight2",
    "any_straight3",
    "any_consensus",
    "any_dom_last",
    "any_doubles_support",
    "top_canonicals",
    "top_modal_orders",
    "fam_cov",
    "fam_hpr",
    "fam_perm",
    "fam_repeat",
    "fam_cons",
    "fam_hot",
    "fam_straight2",
    "fam_straight3",
    "fam_doubles",
    "fam_section_bonus",
    "fam_progression_bonus",
    "fam_last_remaining_bonus",
    "family_score",
    "section_count",
    "progression_flag",
    "last_remaining_3v",
}

REQUIRED_YAML_KEYS = {
    "vertical_coverage_per_row",
    "horizontal_persistence_repeat_bonus",
    "baseline_straight_bonus",
    "baseline_boxed_bonus",
    "straight_2rows_bonus",
    "straight_3rows_bonus",
    "extra_digit_per_char",
    "single_left_bonus",
    "mirror_bonus",
    "consensus_full_bonus",
    "stub_consensus_score",
    "hot_level_1_bonus",
    "hot_level_2_bonus",
    "dominant_last_bonus",
    "dominant_pair_bonus",
    "dominant_double3_bonus",
    "min_score_to_highlight",
    "perm_density_per_extra",
    "repeat_count_per_extra",
    "vtrac_family_presence",
    "cross_section_triple",
    "progression_across_sets",
    "last_remaining_3v_bonus",
    "consensus_family_bonus",
    "hotzone_family_bonus",
    "doubles_trigger_bonus",
    "hidden3v_bonus",
}


def _build_sample_scores():
    from alpha_analytical import stable

    rows = []
    for row_type in ["R2", "R4", "R6", "R8"]:
        row = {"RowType": row_type, "Set": "Set1", "Draw": "Draw1"}
        for col in stable.COLS:
            row[col] = {"1": "227", "2": "277"}.get(col, "")
        rows.append(row)
    df = pd.DataFrame(rows)
    _, results = stable.analyse(df, "Combined")
    return pd.DataFrame(results)


def main() -> int:
    try:
        from alpha_analytical import stable
        from alpha_analytical.stable.feature_config import CFG as STABLE_CFG
        from alpha_analytical.stable.post_pass_families import build_family_summary
    except Exception as exc:
        sys.stderr.write(f"[check_contract] Unable to import Stable modules: {exc}\n")
        return 1

    df_scores = _build_sample_scores()
    missing_rows = REQUIRED_ROW_COLUMNS - set(df_scores.columns)
    if missing_rows:
        sys.stderr.write(f"[check_contract] Missing row columns: {sorted(missing_rows)}\n")
        return 1

    families = build_family_summary(df_scores, STABLE_CFG)
    missing_fams = REQUIRED_FAMILY_COLUMNS - set(families.columns)
    if missing_fams:
        sys.stderr.write(f"[check_contract] Missing family columns: {sorted(missing_fams)}\n")
        return 1

    cfg_path = Path(stable.CFG_PATH)
    if not cfg_path.exists():
        sys.stderr.write(f"[check_contract] Config file not found: {cfg_path}\n")
        return 1

    cfg_keys = set(STABLE_CFG.keys())
    missing_keys = REQUIRED_YAML_KEYS - cfg_keys
    if missing_keys:
        sys.stderr.write(f"[check_contract] feature_config.yml missing keys: {sorted(missing_keys)}\n")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
