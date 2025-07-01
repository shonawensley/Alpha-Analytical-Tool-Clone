# Module D: Final Aggregator & Synergy # AAT9

**Purpose**  
Combines the outputs of Modules A (Stable), B (Digit Reduction), and C (Hot Zones), awarding synergy points for:

- Cross-module presence: same pattern found in stable + digit reduction, etc.
- Cross-set repetition (Set3 → Set2 → Set1).
- Cross-midday/evening synergy.
- V-Trac alignment or cluster grouping.
- "Pending" logic if not seen in last X draws.
- Hot-level synergy or 3-value synergy.

## Input Format

Aggregator typically expects JSON/dict outputs from each module:

- `stable_patterns.json` (e.g. a dict keyed by pattern).
- `digitreduce_patterns.json` (an array or nested dict).
- `hotzone_patterns.json` (an array of discovered patterns).

**It's best** if each module is stored in a consistent structure: 
```json
{
  "module_source": "StableExtractor",
  "patterns": [
    { "pattern_str":"695", "score_in_module":8, "hot_level":0, "..."},
    "..."
  ]
}
```
But you can adapt.

## Output
A synergy report, e.g.:

```json
{
  "aggregator_module": "Advanced Synergy Aggregator",
  "timestamp": "...",
  "pattern_count": 12,
  "patterns": [
    {
      "canonical_form":"569",
      "pattern_variants":["695","956"],
      "modules_found":["StableExtractor","HotZones"],
      "sections_found":["Midday"],
      "sets_found":["Set2","Set1"],
      "final_synergy_score": 25,
      "synergy_breakdown": {
        "sum_module_scores":12,
        "cross_module_bonus":3,
        "pending_bonus":3,
        "hot_super_bonus":4,
        "..."
      }
    }
  ]
}
```

## Steps

### Load Each Module's Output

- `stable_out = parse stable_patterns.json`
- `long_out = parse digitreduce_patterns.json`
- `hotz_out = parse hotzone_patterns.json`

### Unify / Normalize

Convert each discovered pattern to a standard form with:
- `pattern_str`, `module_score`, `hot_level`, `stable_after_reduction`, etc.

### Group & Score

- Possibly unify permutations (if you do that advanced approach).
- Award synergy for cross-module repeats, hot zone, stable-lingering, cross-set, 3-value, "pending in last X draws," etc.
- Output final synergy in sorted order (descending score).
- Write Out e.g. `data/outputs/analysis/aggregator/final_synergy.json`.

## Example CLI

```bash
python aggregator.py \
  --stable stable_patterns.json \
  --digit digitreduce_patterns.json \
  --hot hotzone_patterns.json \
  --recent_draws last6_draws.json \
  --output aggregator_synergy.json
```

## Configuration

Synergy weights in a config or dictionary, e.g.:

```json
{
  "cross_module_bonus": 3,
  "hot_star_bonus": 2,
  "hot_super_bonus": 4,
  "pending_bonus": 3,
  "three_value_bonus": 2
}
```
Aggregator merges them, can be tuned without rewriting modules.

## Next Steps

- Possibly feed aggregator results into an ML pipeline (see `docs/ML_NOTES.md`).
- Or pass synergy results to a "Combination Builder" for final pick-3 combos. 