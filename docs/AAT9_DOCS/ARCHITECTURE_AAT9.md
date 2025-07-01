# AAT9 Architecture Overview

This doc provides a bird's-eye flow of how **Alpha Analytical Tool 9** moves data from raw Excel → stable CSV → each module → aggregator.

```mermaid
flowchart LR
    A[Raw Excel (.xlsm)] --> B[generate_tables_pipeline];
    B --> C((Combined CSV Tables)):::data
    C --> D[Module A:<br>Stable Pattern Extractor];
    C --> E[Module B:<br>Digit Reduction];
    C --> F[Module C:<br>Hot Zones];
    D --> G[Aggregator];
    E --> G[Aggregator];
    F --> G[Aggregator];
    G --> H[[Final Synergy Scores]]
    
    classDef data fill:#fffae6,stroke:#666
```

## Key Subsystems

1. **Table Generation**  
   - Steps that parse raw Excel data, create standard CSV for each state.
   - Source: `scripts/core/generate_tables_pipeline.py`.

2. **Stable Extractor**  
   - Finds stable 3–6 digit patterns in R2/R4/R6/R8 columns, awarding "vertical/horizontal/mirror" points.

3. **Digit Reduction**  
   - Targets big columns (7..5) to reveal hidden combos after partial digit elimination.

4. **Hot Zones**  
   - Focuses on star-labeled ( * / ** ) cells, quickly scanning for short repeating combos.  
   - Some single-transit or minimal reduction used.

5. **Aggregator**  
   - Reads each module's JSON output, merges patterns, calculates synergy scores.

## Additional Notes

- We keep older architecture references in `docs/old_archives/`. 
- This doc is strictly about **AAT9** flow. 