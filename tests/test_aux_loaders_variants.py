from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT / "src"
AUX_DIR = ROOT / "scripts" / "auxiliary" / "working"
for candidate in (ROOT, SRC_DIR, AUX_DIR):
    if str(candidate) not in sys.path:
        sys.path.insert(0, str(candidate))

from modules import aux_loaders


def _write_csv(path: Path, draws: list[str]) -> None:
    lines = ["Draw"] + draws
    path.write_text("\n".join(lines), encoding="utf-8")


def test_load_state_draws_variants(tmp_path):
    base = tmp_path / "draws"
    base.mkdir()

    _write_csv(base / "Connecticut_draws.csv", ["225", "445", "004"])
    _write_csv(base / "Connecticut_Midday_draws.csv", ["002", "077", "669"])
    _write_csv(base / "Connecticut_Evening_draws.csv", ["466", "255", "044"])

    draws_c, path_c = aux_loaders.load_state_draws("Connecticut", base=base)
    assert draws_c[:3] == ["225", "445", "004"]
    assert path_c and path_c.endswith("Connecticut_draws.csv")

    draws_m, path_m = aux_loaders.load_state_draws("Connecticut", variant="midday", base=base)
    assert draws_m[:3] == ["002", "077", "669"]
    assert path_m and path_m.endswith("Connecticut_Midday_draws.csv")

    draws_e, path_e = aux_loaders.load_state_draws("Connecticut4", variant="evening", base=base)
    assert draws_e[:3] == ["466", "255", "044"]
    assert path_e and path_e.endswith("Connecticut_Evening_draws.csv")

    assert all(len(value) == 3 for value in draws_c + draws_m + draws_e)


def test_missing_west_virginia_variant_does_not_borrow_virginia(tmp_path):
    base = tmp_path / "draws"
    base.mkdir()

    _write_csv(base / "Virginia_Midday_draws.csv", ["123", "456"])
    _write_csv(base / "West_Virginia_draws.csv", ["789", "012"])
    _write_csv(base / "West_Virginia_Evening_draws.csv", ["345", "678"])

    draws, resolved = aux_loaders.load_state_draws(
        "WestVirginia4",
        variant="midday",
        base=base,
    )

    assert draws == []
    assert resolved is None


def test_ontario_canada_alias_resolves_exact_ontario_files(tmp_path):
    base = tmp_path / "draws"
    base.mkdir()

    _write_csv(base / "Ontario_draws.csv", ["123", "456"])
    _write_csv(base / "Ontario_Midday_draws.csv", ["234", "567"])
    _write_csv(base / "Ontario_Evening_draws.csv", ["345", "678"])

    combined, combined_path = aux_loaders.load_state_draws(
        "OntarioCanada4",
        variant="combined",
        base=base,
    )
    midday, midday_path = aux_loaders.load_state_draws(
        "OntarioCanada4",
        variant="midday",
        base=base,
    )

    assert combined == ["123", "456"]
    assert combined_path and combined_path.endswith("Ontario_draws.csv")
    assert midday == ["234", "567"]
    assert midday_path and midday_path.endswith("Ontario_Midday_draws.csv")
