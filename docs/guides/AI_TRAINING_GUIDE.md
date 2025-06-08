# AI Training Guide for V-TRAC Analyzer

This guide explains how to use the enhanced V-TRAC Analyzer to save predictions and winners as JSON files for AI training.

## Overview

The enhanced system now includes:
1. **Automatic JSON export** of V-TRAC predictions when you run analysis
2. **Enhanced Log Winners tab** with JSON export and bulk paste support
3. **Analysis script** to compare predictions vs actual winners
4. **Training data generation** for AI/ML optimization

## Directory Structure

```
data/
├── outputs/
│   ├── predictions/          # V-TRAC predictions (JSON)
│   ├── winners_json/         # Actual winning numbers (JSON)
│   ├── winners/              # Highlighted CSV tables
│   └── analysis/             # HTML analysis reports
```

## Step 1: Generate and Save Predictions

### Using run_with_analyzer.bat

1. Launch the app: `run_with_analyzer.bat`
2. Go to the **V-TRAC Analyzer** tab
3. Select states to analyze
4. Click **Run V-TRAC Analysis**
5. Predictions are automatically saved to `data/outputs/predictions/`

### JSON Format for Predictions

```json
{
  "date": "2025-01-24",
  "timestamp": "20250124_143022",
  "state": "Florida4",
  "predictions": [
    {
      "rank": 1,
      "index": 23,
      "score": 156.78,
      "patterns": ["123", "456", "789"],
      "pattern_count": 3
    },
    {
      "rank": 2,
      "index": 15,
      "score": 142.34,
      "patterns": ["012", "345", "678"],
      "pattern_count": 3
    }
  ]
}
```

## Step 2: Log Winners

### Method 1: Individual Entry

1. Go to the **Log Winners** tab
2. Select **Individual Entry**
3. Enter midday and/or evening winners
4. Select states (or leave empty for all)
5. Choose the date
6. Click **Log Winners & Highlight**

### Method 2: Bulk Paste (Recommended)

1. Go to the **Log Winners** tab
2. Select **Bulk Paste (Multiple States)**
3. Paste winners in this format:

```
Connecticut    042    838
Delaware       058    478
Florida        610    975
Georgia        322    332
Michigan       340    168
```

4. Choose the date
5. Click **Process Bulk Winners**

### JSON Format for Winners

```json
{
  "date": "2025-01-24",
  "timestamp": "20250124_150000",
  "state": "Florida4",
  "winners": {
    "midday": "610",
    "evening": "975"
  }
}
```

## Step 3: Analyze Predictions vs Winners

### Run Analysis

1. After collecting predictions and winners for several days
2. Run: `analyze_predictions.bat`
3. The script will:
   - Load all prediction JSON files
   - Load all winner JSON files
   - Match them by state and date
   - Generate analysis reports

### Output Files

- `analysis_results_YYYYMMDD_HHMMSS.csv` - Detailed comparison
- `training_data_YYYYMMDD_HHMMSS.json` - Ready for AI training

## Step 4: Use Training Data

### With ChatGPT/Claude

1. Zip the training data JSON file
2. Upload to ChatGPT or Claude
3. Ask: "Analyze this V-TRAC prediction data and suggest improvements to the scoring algorithm"

### With Python Scripts

```python
import json

# Load training data
with open('training_data_20250124_150000.json', 'r') as f:
    data = json.load(f)

# Analyze patterns
for sample in data:
    features = sample['features']
    labels = sample['labels']
    # Your analysis code here
```

## Best Practices

1. **Daily Routine**:
   - Run V-TRAC analysis each morning
   - Log winners each evening
   - Run analysis weekly

2. **Data Collection**:
   - Collect at least 30 days of data before major analysis
   - Include all states for better pattern recognition

3. **Pattern Analysis**:
   - Focus on top 3 predictions (rank 1-3)
   - Look for patterns that appear before wins
   - Track which V-TRAC indexes perform best

## Troubleshooting

### No JSON files created?
- Check that `data/outputs/predictions/` directory exists
- Ensure you're using the enhanced version with JSON export
- Look for error messages in the console

### Winners not matching states?
- Use exact state names from the STATES list
- The bulk paste feature tries to match partial names
- Check the warning messages for unmatched states

### Analysis finds no matches?
- Ensure predictions and winners have the same date
- Check that state names match exactly
- Verify JSON files are in correct directories

## Next Steps

1. Collect data for at least 2-4 weeks
2. Run analysis to identify patterns
3. Use insights to adjust V-TRAC scoring weights
4. Test improved algorithm on new data
5. Iterate and refine

The goal is to identify which V-TRAC patterns and indexes are most predictive of actual winners, then adjust the analyzer to prioritize those patterns. 