# Module C: Hot Zones Analysis

**Purpose**  
Detect patterns in the "star" columns or any `*`/`**` cells in R2/R4/R6/R8. Typically focuses on 3-value or short final columns. Often uses single-digit transit or a small method (like removing 1–2 digits) to see if a 3-digit repeat emerges.

## Input

- The combined CSV tables or a derived JSON that includes star-labeled cells. E.g. `6688*`, `****`.
- Possibly you track `Set1->Draw7` or final columns with star indicators.

## Output

- A list of discovered "hot zone patterns." Example:

  ```json
  {
    "hotzone_patterns":[
      {
        "pattern": "695",
        "local_hotzone_score": 4,
        "hot_level": 2,
        "stable_after_reduction": false,
        "lingers_across_boxes": false,
        "locations": [
          ["Midday","Set1","Draw3","R2",5]
        ]
      },
      {
        "pattern": "267",
        "local_hotzone_score": 3,
        "hot_level": 1,
        "stable_after_reduction": true,
        "lingers_across_boxes": false,
        "locations": [
          ["Midday","Set1","Draw1","R2",7]
        ]
      }
    ]
  }
  ```

## Process

### Locate Starred Cells

- Check each row's `hot_zone_indicators` or parse the text (`*` or `**` at the end).
- If `**`, treat as super-hot => `hot_level=2`; if `*`, then `hot_level=1`.

### Extract 3–digit or 3-value combos

- Possibly do single-digit removal if your config says so.
- Score them with `local_hotzone_score`.

### Tag Output
Each pattern includes:
- `hot_level` (0/1/2),
- `stable_after_reduction` (if we used digit removal),
- optional synergy with midday/evening if you want to check cross-sections.

## CLI Example

```bash
python hot_zones.py --state=Florida4 --output=hotzone_patterns.json
```

## Scoring

- Minor base: found in a hot zone => +5
- If `hot_level = 1` => +2 more
- If `hot_level = 2` => +4 more
- If stable after single-digit transit => +2

Summation is your `local_hotzone_score`.

## Typical Usage

- Run after you generate tables (and optionally after stable/digit_reduction).
- Then aggregator merges your "hotzone_patterns" with the other module outputs. 