from pathlib import Path

import json

import pytest

from alpha_analytical.digit_reduction.analyzer_v2.training_bundle import (
    TrainingBundleError,
    cleanup_training_bundles,
    package_training_bundle,
)


@pytest.fixture()
def fake_structure(tmp_path: Path) -> Path:
    root = tmp_path / "data" / "outputs" / "analysis" / "digit_reduction" / "TestState"
    (root / "training").mkdir(parents=True)
    (root / "analyzer_v2" / "winners").mkdir(parents=True)

    # Training log
    (root / "training" / "TestState_digit_reduction_log.json").write_text("{}", encoding="utf-8")

    # Analyzer outputs
    (root / "analyzer_v2" / "TestState_analyzer_v2_per_item.csv").write_text("id,score\n", encoding="utf-8")
    (root / "analyzer_v2" / "TestState_analyzer_v2_top_candidates.csv").write_text("id,score\n", encoding="utf-8")
    (root / "analyzer_v2" / "TestState_analyzer_v2_meta.json").write_text("{}", encoding="utf-8")

    # Winner artifacts for stamp 20251006
    winners = root / "analyzer_v2" / "winners"
    for variant in ["Combined", "Midday"]:
        stem = f"20251006_{variant}"
        (winners / f"{stem}_winner_map.json").write_text("{}", encoding="utf-8")
        (winners / f"{stem}_winner_flags.csv").write_text("col\n", encoding="utf-8")
        (winners / f"{stem}_winner_stamp.json").write_text("{}", encoding="utf-8")
        (winners / f"{stem}_winner_hits.csv").write_text("col\n", encoding="utf-8")
        (winners / f"{stem}_winner_overlay.html").write_text("<html></html>", encoding="utf-8")

    return tmp_path / "data" / "outputs" / "analysis"


def test_package_training_bundle_creates_expected_files(fake_structure: Path):
    result = package_training_bundle(
        "TestState",
        analysis_root=fake_structure,
        stamp="20251006",
        include_overlay=True,
        include_hits=True,
        make_zip=False,
    )

    bundle_dir = Path(result["bundle_dir"])
    assert bundle_dir.exists()

    manifest = json.loads((bundle_dir / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["state"] == "TestState"
    assert manifest["stamp"] == "20251006"
    names = {entry["name"] for entry in manifest["files"]}
    expected = {
        "TestState_digit_reduction_log.json",
        "TestState_analyzer_v2_per_item.csv",
        "TestState_analyzer_v2_top_candidates.csv",
        "TestState_analyzer_v2_meta.json",
        "20251006_Combined_winner_map.json",
        "20251006_Combined_winner_flags.csv",
        "20251006_Combined_winner_stamp.json",
        "20251006_Combined_winner_hits.csv",
        "20251006_Combined_winner_overlay.html",
        "20251006_Midday_winner_map.json",
        "20251006_Midday_winner_flags.csv",
        "20251006_Midday_winner_stamp.json",
        "20251006_Midday_winner_hits.csv",
        "20251006_Midday_winner_overlay.html",
    }
    assert expected.issubset(names)


def test_package_training_bundle_missing_files_raises(fake_structure: Path):
    # Remove a required file
    missing = fake_structure / "digit_reduction" / "TestState" / "analyzer_v2" / "TestState_analyzer_v2_meta.json"
    missing.unlink()
    with pytest.raises(TrainingBundleError):
        package_training_bundle("TestState", analysis_root=fake_structure, stamp="20251006")


def test_cleanup_training_bundles_removes_directories(fake_structure: Path):
    # Produce a bundle then clean it
    package_training_bundle("TestState", analysis_root=fake_structure, stamp="20251006")
    removed = cleanup_training_bundles("TestState", analysis_root=fake_structure)
    assert removed  # non-empty
    bundles_dir = fake_structure / "digit_reduction" / "TestState" / "training_sets"
    assert not any(bundles_dir.iterdir())
