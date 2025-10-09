from pathlib import Path

from alpha_analytical.control_center.draws_refresh import purge_draw_csvs


def test_purge_draw_csvs(tmp_path):
    out_dir = tmp_path / "draws"
    out_dir.mkdir()

    # Create dummy files for Connecticut (combined, midday, evening)
    state_stem = "Connecticut"
    files = [
        out_dir / f"{state_stem}_draws.csv",
        out_dir / f"{state_stem}_Midday_draws.csv",
        out_dir / f"{state_stem}_Evening_draws.csv",
    ]
    for file in files:
        file.write_text("dummy", encoding="utf-8")

    removed = purge_draw_csvs(["Connecticut4"], out_dir)
    assert set(removed) == set(files)
    assert all(not f.exists() for f in files)


def test_purge_respects_missing(tmp_path):
    out_dir = tmp_path / "draws"
    out_dir.mkdir()

    removed = purge_draw_csvs(["Connecticut4"], out_dir)
    assert removed == []


def test_purge_includes_specials(tmp_path):
    out_dir = tmp_path / "draws"
    out_dir.mkdir()

    stem = "Texas"
    target = out_dir / f"{stem}_Morning_draws.csv"
    target.write_text("dummy", encoding="utf-8")

    removed = purge_draw_csvs(["Texas4"], out_dir, include_specials=True)
    assert removed == [target]
    assert not target.exists()
