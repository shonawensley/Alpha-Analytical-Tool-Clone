from modules.vtrac_enhanced import (
    DEFAULT_WEIGHTS,
    build_engine_input_from_tables,
    run_analysis,
    write_prediction_bundle,
)
from modules.vtrac_enhanced.types import Cell, EngineInput, PatternsGrid, SectionData


def _empty_ring() -> tuple[Cell, ...]:
    return tuple(Cell(digits="") for _ in range(7))


def _cells(*values: str) -> tuple[Cell, ...]:
    padded = list(values) + [""] * (7 - len(values))
    cells = []
    for idx, value in enumerate(padded):
        col_number = 7 - idx
        hot = col_number <= 2
        superhot = col_number == 1
        cells.append(Cell(digits=value, hot=hot, superhot=superhot))
    return tuple(cells)


def test_run_analysis_scores_index() -> None:
    r2 = _cells("", "", "", "", "", "045", "059")
    grid = PatternsGrid(
        by_r={
            "R2": r2,
            "R4": _empty_ring(),
            "R6": _empty_ring(),
            "R8": _empty_ring(),
        }
    )
    engine_input = EngineInput(
        sections=[SectionData(section="Combined", set_name="Set1", patterns=grid)],
        recent_draws=("059",),
        winner_hint=None,
    )

    output = run_analysis(engine_input, DEFAULT_WEIGHTS)
    assert output.indices_ranked, "Expected at least one scored index"
    top = output.indices_ranked[0]
    assert top.index == 5, f"Expected index 5 to be highest, got {top.index}"
    assert top.score > 0
    assert any(s.straight == "045" or s.straight == "059" for s in top.straights)


def test_write_prediction_bundle(tmp_path) -> None:
    r2 = _cells("", "", "", "", "", "045", "059")
    grid = PatternsGrid(
        by_r={"R2": r2, "R4": _empty_ring(), "R6": _empty_ring(), "R8": _empty_ring()}
    )
    engine_input = EngineInput(
        sections=[SectionData(section="Combined", set_name="Set1", patterns=grid)],
        recent_draws=("059",),
    )

    output = run_analysis(engine_input)
    out_path = write_prediction_bundle("TestState", output, analysis_root=tmp_path)
    assert out_path.exists()
    data = out_path.read_text(encoding="utf-8")
    assert '"TestState"' in data
