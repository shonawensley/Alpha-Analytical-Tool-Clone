import textwrap

from alpha_analytical.control_center import batch_runner


SAMPLE = textwrap.dedent(
    """
    StatePick 3
    MiddayEvening
    Connecticut001883
    Delaware714650
    Georgia605310
    256
    Ontario829965
    Quebec285
    Texas731
    135616
    
    Virginia442893
    """
)


def test_parse_winner_sheet_basic_extraction():
    entries = batch_runner.parse_winner_sheet(SAMPLE)
    by_canonical = {entry.canonical: entry for entry in entries}

    assert by_canonical["Connecticut"].midday == "001"
    assert by_canonical["Connecticut"].evening == "883"

    assert by_canonical["Delaware"].midday == "714"
    assert by_canonical["Delaware"].evening == "650"

    georgia = by_canonical["Georgia"]
    assert georgia.midday == "605"
    assert georgia.evening == "310"
    assert georgia.raw_digits[2] == "256"  # extra token ignored for winners

    ontario = by_canonical["Ontario"]
    assert ontario.midday == "829"
    assert ontario.evening == "965"

    texas = by_canonical["Texas"]
    assert texas.midday == "731"
    assert texas.evening == "135"


def test_filter_tracked_only_returns_known_states():
    entries = batch_runner.parse_winner_sheet(SAMPLE)
    tracked = batch_runner.filter_tracked(entries)
    canons = {entry.canonical for entry in tracked}
    assert "Connecticut" in canons
    assert "Quebec" not in canons  # not part of tracked mapping

