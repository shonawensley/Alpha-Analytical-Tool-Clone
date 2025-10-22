import json
from pathlib import Path

import pandas as pd

from alpha_analytical.stable.metrics import build_metrics, write_metrics
from alpha_analytical.stable.training_bundle import write_training_bundle


def test_write_training_bundle(tmp_path):
    state = "TestState"
    analysis_root = tmp_path / "patterns"
    state_dir = analysis_root / state
    state_dir.mkdir(parents=True)

    scores_path = state_dir / f"{state}_stable_patterns_scores.csv"
    scores_df = pd.DataFrame(
        {
            "section": ["Combined", "Midday"],
            "Canonical": ["123", "456"],
            "family_id": [5, 34],
            "score": [10, 5],
            "type": ["straight", "straight"],
        }
    )
    scores_df.to_csv(scores_path, index=False)

    html_path = state_dir / f"{state}_stable_patterns_report.html"
    html_path.write_text("<html></html>", encoding="utf-8")

    families_path = state_dir / f"{state}_stable_patterns_families.csv"
    families_df = pd.DataFrame(
        {
            "family_id": [5, 34],
            "family_score": [10, 7],
            "hot_density": [0.4, 0.25],
        }
    )
    families_df.to_csv(families_path, index=False)

    spotlight_raw_path = state_dir / f"{state}_winner_family_spotlight_raw.csv"
    pd.DataFrame(
        {
            "family_id": [5, 34],
            "section": ["Combined", "Midday"],
        }
    ).to_csv(spotlight_raw_path, index=False)

    spotlight_fam_path = state_dir / f"{state}_winner_family_spotlight_families.csv"
    pd.DataFrame({"family_id": [5], "family_score": [8]}).to_csv(spotlight_fam_path, index=False)

    metrics_dir = state_dir / "metrics"
    metrics_payload = build_metrics(
        state=state,
        df_scores=scores_df,
        families_df=families_df,
        winners=["059"],
    )
    metrics_path = write_metrics(metrics_dir, state, metrics_payload)

    info = write_training_bundle(
        state=state,
        stamp="20250621",
        analysis_root=analysis_root,
        scores_path=scores_path,
        html_path=html_path,
        families_path=families_path,
        spotlight_raw_path=spotlight_raw_path,
        spotlight_family_path=spotlight_fam_path,
        metrics_path=metrics_path,
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

    metrics_entry = manifest["files"]["metrics_json"]
    assert metrics_entry is not None
    metrics_entry_path = Path(metrics_entry)
    assert metrics_entry_path.parts[0] == "artifacts"
    assert metrics_entry_path.name == metrics_path.name

    versions = manifest.get("versions") or {}
    assert versions.get("evidence_schema") == metrics_payload["evidence_schema_version"]
    assert versions.get("stable_contract") == metrics_payload["stable_contract_version"]

    artifacts_dir = bundle_dir / "artifacts"
    copied_files = {p.name for p in artifacts_dir.iterdir()}
    expected = {
        scores_path.name,
        html_path.name,
        families_path.name,
        spotlight_raw_path.name,
        spotlight_fam_path.name,
        metrics_path.name,
    }
    assert expected.issubset(copied_files)
