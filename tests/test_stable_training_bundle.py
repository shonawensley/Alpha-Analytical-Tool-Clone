import json
from pathlib import Path

import pandas as pd

from alpha_analytical.stable.training_bundle import write_training_bundle

def test_write_training_bundle(tmp_path):
    state = "TestState"
    analysis_root = tmp_path / "patterns"
    state_dir = analysis_root / state
    state_dir.mkdir(parents=True)

    scores_path = state_dir / f"{state}_stable_patterns_scores.csv"
    pd.DataFrame(
        {
            "section": ["Combined", "Midday"],
            "Canonical": ["123", "456"],
            "family_id": [5, 34],
        }
    ).to_csv(scores_path, index=False)

    html_path = state_dir / f"{state}_stable_patterns_report.html"
    html_path.write_text("<html></html>", encoding="utf-8")

    families_path = state_dir / f"{state}_stable_patterns_families.csv"
    pd.DataFrame({"family_id": [5], "family_score": [10]}).to_csv(families_path, index=False)

    spotlight_raw_path = state_dir / f"{state}_winner_family_spotlight_raw.csv"
    pd.DataFrame(
        {
            "family_id": [5, 34],
            "section": ["Combined", "Midday"],
        }
    ).to_csv(spotlight_raw_path, index=False)

    spotlight_fam_path = state_dir / f"{state}_winner_family_spotlight_families.csv"
    pd.DataFrame({"family_id": [5], "family_score": [8]}).to_csv(spotlight_fam_path, index=False)

    info = write_training_bundle(
        state=state,
        stamp="20250621",
        analysis_root=analysis_root,
        scores_path=scores_path,
        html_path=html_path,
        families_path=families_path,
        spotlight_raw_path=spotlight_raw_path,
        spotlight_family_path=spotlight_fam_path,
        winners=["059"],
    )

    bundle_dir = Path(info["bundle_dir"])
    manifest_path = Path(info["manifest"])

    assert bundle_dir.exists()
    assert manifest_path.exists()

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert manifest["state"] == state
    assert manifest["stamp"] == "20250621"
    assert manifest["winners"] == ["059"]
    assert manifest["stats"]["total_patterns"] == 2
    assert manifest["stats"]["section_counts"] == {"Combined": 1, "Midday": 1}
    assert set(manifest["stats"]["family_ids"]) == {5, 34}

    artifacts_dir = bundle_dir / "artifacts"
    copied_files = {p.name for p in artifacts_dir.iterdir()}
    expected = {
        scores_path.name,
        html_path.name,
        families_path.name,
        spotlight_raw_path.name,
        spotlight_fam_path.name,
    }
    assert expected.issubset(copied_files)
