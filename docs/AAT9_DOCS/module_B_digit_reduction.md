# Module B: Digit Reduction & Hidden Patterns # AAT9

**Purpose**  
Focuses on **long-string columns** (commonly col7..col5 or any 6–8 digit strings) in R2/R4/R6/R8. Applies digit reduction (Methods A, B, C, or single-digit transit) to uncover hidden 3-value or 3-digit combos that do not appear in the raw data.

## Inputs

- The same CSV tables from `generate_tables_pipeline.bat`.  
- Typically we only read columns 7,6,5 in Set3->Draw1, Set2->Draw1, Set1->Draw1, or similar big areas.

## Outputs

- JSON or dict where each cell's "notable patterns" are discovered. Example:
  ```json
  {
    "module_name": "LongStringReduction_Area1",
    "analysis_results": [
      {
        "cell_id": "Midday|Set3|Draw1|R2|col7",
        "original_string": "6688110...",
        "initial_stable": ["6688"],
        "method_a": { "own": {"..."}, "combined": {"..."} },
        "method_b": { "..." },
        "method_d": { "transit_steps": ["..."], "all_discovered": ["695","688"] },
        "notable_patterns": [
          { "pattern": "695", "score": 8 },
          { "pattern": "688", "score": 5 }
        ],
        "final_score": 14
      }
    ]
  }
  ```

## Key Steps

### Identify Target Cells

- E.g., gather (R2, col7), (R4, col7), (R6, col7), (R8, col7) from each set/draw.
- Possibly also (Draw4 col3), (Draw6 col1) if you want "area2" reductions.

### Apply Reduction Methods

- **Method A**: remove each digit from the past draw if present.
- **Method B**: remove digit or its mirror once.
- **Method C**: remove all occurrences of each digit + mirror.
- **Method D** (single-digit transit): iteratively remove digits from the prior day.

### Discover 3-value patterns
After each reduction step, parse if a substring is 3-value (≤3 unique digits). If found, record in `found_3value_substrings`.

### Score Patterns

- Might add points for "initial_stable," "found in method A + method B," or "multi-method bonus."
- Summarize total cell-level `final_score`.
- Store in `analysis_results`.

## CLI Usage (Example)

```bash
python digit_reduction.py --state=Florida4 --output data/outputs/analysis/long_string/florida_reduced.json
```

## Configuration & Tweaks

- `past_draw_digits_own` vs. `past_draw_digits_combined`: controlling which digits you remove.
- Slicing rules for which columns are "long enough" to reduce.
- `scoring_dict` for each method's base points, multi-method synergy, single-digit transit bonus, etc.

## Future Plans

- Link with aggregator to combine stable + digit_reduction outputs.
- Possibly unify with hot zone approach if star-labeled but also big strings. 