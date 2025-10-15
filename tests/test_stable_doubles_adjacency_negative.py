import pandas as pd

from alpha_analytical import stable
from alpha_analytical.stable.post_pass_families import build_family_summary


def _make_row(column: str, canonical: str, *, cons_full: bool) -> dict:
    return {
        "section": "Combined",
        "Set": "Set1",
        "Draw": "Draw1",
        "Column": column,
        "Canonical": canonical,
        "rows": "R2,R4,R6",
        "perm_count_in_box": 1,
        "repeat_extras_in_box": 0.0,
        "horizontal_persistence_repeat": 1,
        "hot": 0,
        "straight2": False,
        "straight3": False,
        "cons_full": cons_full,
        "dom_last": False,
        "dom_pair": False,
        "orders_modal_value": canonical,
        "orders_modal_rows": 3,
        "type": "straight",
    }


def test_doubles_support_requires_adjacent_column():
    """Stable doubles support should only trigger when consensus digits share adjacent columns (A ±1)."""
    rows = pd.DataFrame(
        [
            _make_row("1", "227", cons_full=True),
            _make_row("3", "277", cons_full=False),
        ]
    )

    summary = build_family_summary(rows, stable.CFG)

    consensus_row = summary[(summary["section"] == "Combined") & (summary["Column"] == "1")].iloc[0]

    assert bool(consensus_row["any_consensus"]) is True
    assert bool(consensus_row["any_doubles_support"]) is False
