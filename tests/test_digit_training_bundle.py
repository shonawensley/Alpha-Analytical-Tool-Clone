from pathlib import Path
import json
import pytest
from alpha_analytical.digit_reduction.analyzer_v2.training_bundle import (
    TrainingBundleError,
    package_training_bundle,
)
VARIANTS = ("Combined", "Midday", "Evening")

@pytest.fixture()
def fake_structure(tmp_path: Path) -> Path:
    root = tmp_path / "data" / "outputs" / "analysis" / "digit_reduction" / "TestState"
    (root / "training").mkdir(parents=True)
    (root / "analyzer_v2" / "winners").mkdir(parents=True)
    # Training log and analyzer outputs
    (root / "training" / "TestState_digit_reduction_log.json").write_text("{}", encoding="utf-8")
    (root / "analyzer_v2" / "TestState_analyzer_v2_per_item.csv").write_text("id,score\n", encoding="utf-8")
    (root / "analyzer_v2" / "TestState_analyzer_v2_top_candidates.csv").write_text("id,score\n", encoding="utf-8")
    (root / "analyzer_v2" / "TestState_analyzer_v2_meta.json").write_text("{}", encoding="utf-8")
    winners = root / "analyzer_v2" / "winners"
    for variant in VARIANTS:
        stem = f"20251006_{variant}"
        (winners / f"{stem}_winner_map.json").write_text("{}", encoding="utf-8")
        (winners / f"{stem}_winner_flags.csv").write_text("col\n", encoding="utf-8")
        (winners / f"{stem}_winner_stamp.json").write_text("{}", encoding="utf-8")
        (winners / f"{stem}_winner_hits.csv").write_text("col\n", encoding="utf-8")
        (winners / f"{stem}_winner_overlay.html").write_text("<html></html>", encoding="utf-8")
    return tmp_path / "data" / "outputs" / "analysis"

def test_package_training_bundle_defaults(fake_structure: Path) -> None:
    result = package_training_bundle(
        "TestState",
        analysis_root=fake_structure,
        stamp="20251006",
        include_overlay=True,
        include_hits=True,
    )
    manifest_path = Path(result["bundle_dir"]) / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert sorted(manifest["packaged_variants"]) == sorted(["Midday", "Evening"])
    names = {entry["name"] for entry in manifest["files"]}
    expected = {
        "TestState_digit_reduction_log.json",
        "TestState_analyzer_v2_per_item.csv",
        "TestState_analyzer_v2_top_candidates.csv",
        "TestState_analyzer_v2_meta.json",
        "20251006_Midday_winner_map.json",
        "20251006_Midday_winner_flags.csv",
        "20251006_Midday_winner_stamp.json",
        "20251006_Midday_winner_hits.csv",
        "20251006_Midday_winner_overlay.html",
        "20251006_Evening_winner_map.json",
        "20251006_Evening_winner_flags.csv",
        "20251006_Evening_winner_stamp.json",
        "20251006_Evening_winner_hits.csv",
        "20251006_Evening_winner_overlay.html",
    }
    assert expected.issubset(names)
    combined_files = {f"20251006_Combined_{suffix}" for suffix in [
        "winner_map.json",
        "winner_flags.csv",
        "winner_stamp.json",
        "winner_hits.csv",
        "winner_overlay.html",
    ]}
    assert names.isdisjoint(combined_files)

def test_package_training_bundle_include_combined(fake_structure: Path) -> None:
    result = package_training_bundle(
        "TestState",
        analysis_root=fake_structure,
        stamp="20251006",
        include_overlay=True,
        include_hits=True,
        include_combined=True,
    )
    manifest = json.loads((Path(result["bundle_dir"]) / "manifest.json").read_text(encoding="utf-8"))
    assert sorted(manifest["packaged_variants"]) == sorted(["Combined", "Midday", "Evening"])
    names = {entry["name"] for entry in manifest["files"]}
    for variant in VARIANTS:
        stem = f"20251006_{variant}"
        for suffix in [
            "winner_map.json",
            "winner_flags.csv",
            "winner_stamp.json",
            "winner_hits.csv",
            "winner_overlay.html",
        ]:
            assert f"{stem}_{suffix}" in names

def test_package_training_bundle_missing_files_raises(fake_structure: Path) -> None:
    missing = fake_structure / "digit_reduction" / "TestState" / "analyzer_v2" / "TestState_analyzer_v2_meta.json"
    missing.unlink()
    with pytest.raises(TrainingBundleError):
        package_training_bundle("TestState", analysis_root=fake_structure, stamp="20251006")
