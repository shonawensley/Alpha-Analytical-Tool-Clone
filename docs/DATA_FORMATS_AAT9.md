# AAT9 Data Formats

A quick reference for the **CSV tables** and **JSON exports** that each module uses or produces.

## CSV Tables

After running `generate_tables_pipeline.bat`, we get 6 standard files per state:

1. **Midday_combined.csv**  
2. **Evening_combined.csv**  
3. **Combined_combined.csv**  
4. **Midday_R2_only.csv**  
5. **Evening_R2_only.csv**  
6. **Combined_R2_only.csv**

Each file typically has columns:  
`Set`, `Draw`, `RowType`, `7`, `6`, `5`, `4`, `3`, `2`, `1`

**Example** (`Florida4_Midday_combined.csv`):

| Set  | Draw  | RowType | 7        | 6        | ... | 1     |
|------|-------|---------|----------|----------|-----|-------|
|Set3  |Draw1  |DRAW_DATA|6688      |668       | ... |66**   |
|Set3  |Draw1  |R2       |          |          | ... |...    |
|...   |...    |...      |...       |...       | ... |...    |

## JSON Export

1. **Stable Patterns JSON**  
   - Keyed by pattern string, storing "score, locations, stable_after_reduction."  
   - e.g. `data/outputs/analysis/stable_patterns.json`.

2. **Digit Reduction JSON**  
   - Typically an object: `"analysis_results" => array of cell objects`, each with "notable_patterns".
   - e.g. `data/outputs/analysis/longstring_patterns.json`.

3. **Hot Zones JSON**  
   - `"hotzone_patterns" => [ {pattern, local_hotzone_score, hot_level}, ... ]`.

4. **Aggregator Synergy JSON**  
   - Summarizes final synergy:  
   ```json
   {
     "aggregator_module": "AAT9 Synergy",
     "patterns":[
       {
         "canonical_form": "569",
         "modules_found":["StableExtractor","HotZones"],
         "final_synergy_score":25,
         ...
       }
     ]
   }
   ```

## When to Use Each Format

- **CSV**: For internal Python data loading (pandas).
- **JSON**: For storing module outputs, or passing data to external tools or final synergy step.

## Potential Edge Cases

- Some columns might have fewer than 7 steps (Draw4 only goes up to col4).
- Star-labeled cells ( `6688*` ) or double stars ( `66**` ), handle carefully.
- R2-only files have fewer columns, focusing on R2 substring. 