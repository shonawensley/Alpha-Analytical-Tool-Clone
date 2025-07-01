# AAT9 ▸ Module D — V-TRAC Analyzer
**Checkpoint v0.3 – 2025-06-06**

### Why it matters
This upgrade turns the demo V-TRAC script into a production module that:
1. ranks the **top N (3)** V-TRAC indices for tomorrow,
2. logs today's winners & colours the tables,
3. writes a **bundle JSON** → fuel for ML.

### New / changed files at v0.3
| File | Purpose |
|---|---|
| `scripts/streamlit_app_with_analyzer.py` | fixed `script_dir` bug, now calls `bundle_day()` |
| `utils/bundler.py` | **NEW** → merges predictions + winners into `data/outputs/bundles/STATE_DATE_bundle.json` |
| `docs/modules/AAT9_Module_VTRAC_Enhancement.md` | this spec |

### Data-flow
```
tables ─┐
├─► vtrac_analyzer ──► predictions.json
│ └─► analysis/*.html
log winners ─┘
└─► winners.json ──► bundle_day() ──► bundles/
```

### Bundle JSON schema (`v0.3`)
```jsonc
{
  "date": "2025-06-06",
  "state": "Florida4",
  "predictions": [
    {"index": 28, "score": 153},
    {"index": 12, "score": 148},
    {"index": 3,  "score": 131}
  ],
  "winners": { "midday": "456", "evening": "123" }
}
```
**Deferred (logged in CHANGELOG)**
- integrate mirror bonuses into Module A,
- replace top-N ranking with Aggregator synergy score,
- CSV colour-tags remain off (raw numbers easier for ML).