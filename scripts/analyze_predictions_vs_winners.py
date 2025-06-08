#!/usr/bin/env python
"""
Analyze V-TRAC predictions vs actual winners
This script reads the JSON files and provides insights for AI training
"""

import os
import json
import pandas as pd
from datetime import datetime
from pathlib import Path
import sys

# Add the project root to the Python path
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(script_dir))

def load_json_files(directory):
    """Load all JSON files from a directory"""
    files = []
    if os.path.exists(directory):
        for filename in os.listdir(directory):
            if filename.endswith('.json'):
                filepath = os.path.join(directory, filename)
                with open(filepath, 'r') as f:
                    data = json.load(f)
                    files.append(data)
    return files

def analyze_predictions_vs_winners():
    """Analyze predictions against actual winners"""
    predictions_dir = os.path.join("data", "outputs", "predictions")
    winners_dir = os.path.join("data", "outputs", "winners_json")
    
    predictions = load_json_files(predictions_dir)
    winners = load_json_files(winners_dir)
    
    print(f"Found {len(predictions)} prediction files")
    print(f"Found {len(winners)} winner files")
    
    # Create lookup for winners by state and date
    winners_lookup = {}
    for w in winners:
        key = f"{w['state']}_{w['date']}"
        winners_lookup[key] = w['winners']
    
    # Analyze predictions
    results = []
    for pred in predictions:
        state = pred['state']
        date = pred['date']
        key = f"{state}_{date}"
        
        if key in winners_lookup:
            winner_data = winners_lookup[key]
            
            # Check if any prediction patterns might relate to winners
            for p in pred['predictions']:
                result = {
                    'state': state,
                    'date': date,
                    'rank': p['rank'],
                    'index': p['index'],
                    'score': p['score'],
                    'pattern_count': p['pattern_count'],
                    'midday_winner': winner_data.get('midday', ''),
                    'evening_winner': winner_data.get('evening', ''),
                    'patterns': p['patterns']
                }
                results.append(result)
    
    # Convert to DataFrame for analysis
    df = pd.DataFrame(results)
    
    if not df.empty:
        print("\n=== Analysis Summary ===")
        print(f"Total predictions analyzed: {len(df)}")
        print(f"States covered: {df['state'].nunique()}")
        print(f"Date range: {df['date'].min()} to {df['date'].max()}")
        
        # Top performing indexes
        print("\n=== Top V-TRAC Indexes by Average Score ===")
        index_scores = df.groupby('index')['score'].agg(['mean', 'count']).sort_values('mean', ascending=False).head(10)
        print(index_scores)
        
        # Save detailed results
        output_file = f"analysis_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(output_file, index=False)
        print(f"\nDetailed results saved to: {output_file}")
        
        return df
    else:
        print("No matching predictions and winners found for analysis")
        return None

def generate_training_data():
    """Generate training data in a format suitable for AI/ML"""
    df = analyze_predictions_vs_winners()
    
    if df is not None:
        # Create training data structure
        training_data = []
        
        for _, row in df.iterrows():
            # Create feature vector
            features = {
                'state': row['state'],
                'date': row['date'],
                'vtrac_index': row['index'],
                'prediction_rank': row['rank'],
                'score': row['score'],
                'pattern_count': row['pattern_count'],
                'patterns': row['patterns']
            }
            
            # Labels (what we're trying to predict)
            labels = {
                'midday_winner': row['midday_winner'],
                'evening_winner': row['evening_winner']
            }
            
            training_data.append({
                'features': features,
                'labels': labels
            })
        
        # Save training data
        output_file = f"training_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(output_file, 'w') as f:
            json.dump(training_data, f, indent=2)
        
        print(f"\nTraining data saved to: {output_file}")
        print(f"Total training samples: {len(training_data)}")
        
        return training_data

if __name__ == "__main__":
    print("V-TRAC Prediction Analysis Tool")
    print("=" * 50)
    
    # Run analysis
    generate_training_data()
    
    print("\nAnalysis complete!")
    print("\nNext steps:")
    print("1. Continue collecting predictions and winners daily")
    print("2. Run this analysis periodically to update training data")
    print("3. Use the training data to optimize V-TRAC parameters") 