# scripts/checks/smoke_positional.py
import csv
import glob
import os
import sys
import importlib.util

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MOD = os.path.join(
    REPO,
    "modules",
    "module_d_auxiliary_tools",
    "refactored",
    "positional_tool.py",
)


def load_module(path):
    spec = importlib.util.spec_from_file_location("aux_positional_tool", path)
    module = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
    assert spec and spec.loader
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)  # type: ignore[union-attr]
    return module


def load_draws(sample_csv):
    with open(sample_csv, newline="", encoding="utf-8") as handle:
        reader = csv.reader(handle)
        draws = []
        for row in reader:
            if not row:
                continue
            cell = row[0].strip()
            if len(cell) == 3 and cell.isdigit():
                draws.append(cell)
    return list(reversed(draws))  # newest-first


if __name__ == "__main__":
    module = load_module(MOD)
    candidates = glob.glob(os.path.join(REPO, "data", "cleaned", "*_draws.csv"))
    if not candidates:
        print("No draws CSV found under data/cleaned/")
        sys.exit(1)

    csv_path = candidates[0]
    draws = load_draws(csv_path)
    if not draws:
        print(f"No draws in {csv_path}")
        sys.exit(1)

    report = module.analyze_state_variants({"combined": draws}, window=150, topk=3)
    variant_result = report.variant_results.get("combined")
    if not variant_result or not variant_result.draws_used:
        print("Variant analysis returned no data")
        sys.exit(1)

    print(f"Variant=combined Window={variant_result.window} Total={variant_result.draws_used}")
    for pos_idx in (0, 1, 2):
        summary = variant_result.position_summaries.get(pos_idx)
        if not summary:
            continue
        row = ", ".join(
            f"#{entry.rank} d{entry.digit} gap={entry.gap} score={entry.score:.2f}"
            for entry in summary.top_digits
        )
        print(f"P{pos_idx + 1}: {row}")

    if report.candidates:
        print("Top positional candidates:")
        for cand in report.candidates[:5]:
            print(f"  {cand.combo} score={cand.score:.2f} tags={' '.join(cand.tags)}")
