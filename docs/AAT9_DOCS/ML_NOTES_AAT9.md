# AAT9 ML Notes

**A Place to Park Future ML Ideas**  
We don't integrate ML in AAT9's core modules yet, but here's how we might add it:

1. **Feature Engineering**  
   - Let each synergy pattern produce a feature vector: 
     - stable_score, hotzone_score, cross_module_count, times_in_set1, etc.
   - Possibly one row per pattern or per day/pattern combination.

2. **Classification**  
   - Model if a pattern "will appear next draw" vs. not. 
   - Historical label: Did that pattern actually hit?

3. **Hyperparam Tuning**  
   - Weighted synergy vs. direct ML. 
   - Could unify with aggregator logic or replace aggregator synergy with an ML-based approach.

4. **Data Volume**  
   - Might gather thousands of historical draws. 
   - Each draw = a row, each pattern => a column?

5. **Integration**  
   - Keep the aggregator in place. ML becomes an optional post-step. 
   - E.g. `module_E_ml_classifier.py` or separate system.

**Resources**  
- scikit-learn for quick prototypes.  
- Maintain your aggregator JSON so new features are easy to ingest into ML.  