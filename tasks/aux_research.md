I'll also explore optimal ways to:

Rank compound signals across variants (Combined/Midday/Evening),

Set meaningful scoring weights (e.g., red > blue),

Enable automated scoring and future learning,

Keep the code modular and scalable,

Fit seamlessly into your winners logging, training, and Control Center workflows.

This will be delivered as a well-structured, multi-part plan (with code where needed) for turning auxiliary features into powerful scoring units and composing them analytically across the system. I’ll begin now and notify you as soon as it’s ready.

Research completed in 10m · 12 sources · 9 searches

Auxiliary Features as Scoring Units for Winners Logging and Compounding

Features as Individually Scorable Units

To maximize analytical value, each signal from the integrated app and auxiliary tools should be treated as a discrete feature with its own score/tag. Below we enumerate all such features, grouped by module, and outline how to score them individually. This provides a foundation for combining signals, logging winning combos, and future ML integration.

Blackapple Module – Standalone Features

Blackapple produces several trigger signals
GitHub
 that can be isolated as individual scoring factors:

Mirror Pair (MIR) – Indicates if the latest draw contained a mirror pair (digit pairs 0↔5, 1↔6, 2↔7, 3↔8, 4↔9)
GitHub
. As a feature, this would score 1 for any combo that itself contains at least one mirror pair on days when the mirror trigger is active. In practice, Blackapple sets a boolean triggers["mirror"] based on the last draw
GitHub
. We can expose this as a feature flag and tag combos that have any mirror digit pair if the context trigger is true. For example:

if analysis.blackapple.triggers['mirror'] and has_mirror_pair(combo):
    features.add('MIRROR')


The has_mirror_pair utility uses the standard mirror mapping
GitHub
 to detect any mirror digit pair inside the combo.

Floating Digit (FLT) – Flags combos containing “floating” digits that have been completely absent in the recent N draws window (e.g. last 5 draws by default)
GitHub
GitHub
. Blackapple computes a list of absent digits (triggers["floating"]) and gives any combo containing at least one such digit a weight (FLT tag)
GitHub
. As an independent feature, FLOATING would be a boolean indicating the combo includes any digit from the current float list. This feature’s score could be 1 point per floating digit match (or a fixed 1 if any match). For standalone tagging:

float_digits = analysis.blackapple.triggers['floating']  # list of digits absent in last N draws
if any(d in combo for d in float_digits):
    features.add('FLOATING')


Root Sum Due (RS) – Signals that a particular digital root is “overdue” (longest-out) in recent draws
GitHub
. Blackapple finds the longest-out root and if its gap ≥ threshold (25 draws) it marks triggers["root_due"] with the due root(s)
GitHub
. We treat this as a feature by checking if the combo’s digital root matches one of the due values. If so, assign the ROOT_DUE feature. For example:

due_roots = analysis.blackapple.triggers['root_due']  # e.g. [7] if root 7 is longest-out
if digital_root(combo) in due_roots:
    features.add('ROOT_DUE')


This allows combos matching an overdue root sum to be scored (Blackapple gives such combos a tag RS and extra weight
GitHub
).

Pattern Due (PAT) – Flags that a certain digit pattern by size is due. Blackapple looks at the last draws’ “S/T pattern” (Small 0-4 vs Tall 5-9)
GitHub
 and triggers if either an extreme pattern (all Small “SSS” or all Tall “TTT”) hasn’t appeared in ≥25 draws, or if any mixed pattern (e.g. “SST”, “STS”, “TSS”) is missing for ≥12 draws
GitHub
GitHub
. There are two sub-features:

Extreme Pattern Due – True if an all-small or all-large combo pattern is overdue. Any combo of pattern SSS or TTT would get a PATTERN_EXTREME tag when this trigger is on.

Mixed Pattern Due – True if any mixed pattern is overdue; combos of type SST/STS/TSS get the feature when active.

In Blackapple, both are consolidated under a single PAT tag (weight 1) when the respective condition is met
GitHub
. For clarity, we can keep one feature PATTERN_DUE (or split into PAT_EXTREME/PAT_MIXED if we want finer granularity). Example standalone check:

pat_flags = analysis.blackapple.triggers['pattern']  # e.g. {"extreme_due": True, "mixed_due": False}
pattern = get_st_pattern(combo)  # e.g. "SST"
if pat_flags['extreme_due'] and pattern in ("SSS","TTT"):
    features.add('PATTERN_EXTREME')
if pat_flags['mixed_due'] and pattern in ("SST","STS","TSS"):
    features.add('PATTERN_MIXED')


Remaining Pairs Foundation (PAIR) – A specialized filter that builds a base pool of combos from “remaining” digit-pairs that haven’t appeared recently
GitHub
GitHub
. Blackapple’s “27-29 method” computes the set of ~27–29 pairs not seen in the last X draws and tags combos composed entirely of those pairs
GitHub
. As a feature, PAIR_FOUNDATION would mark any combo whose every internal pair is in the remaining set, provided the remaining-pairs trigger is active (i.e., 27–29 pairs remain)
GitHub
. In code:

if analysis.blackapple.triggers['pairs']['remaining_count'] in range(27, 30):
    foundation_pairs = analysis.blackapple.foundation_set
    if all(pair in foundation_pairs for pair in combo_pairs(combo)):
        features.add('PAIR_FOUNDATION')


This standalone feature identifies combos aligned with the overdue-pair foundation principle (Blackapple gives them a “PAIR” tag and extra weight
GitHub
).

Each of these Blackapple-derived features contributes a small weight to a combo’s total score (per Blackapple’s default weights: MIR=1, FLT=1, PAT=1, RS=2, PAIR=2
GitHub
). By isolating them, we can score combos more flexibly – for example, a combo might get +2 for matching an overdue root and +1 for containing a floating digit, etc., instead of one opaque BA score. This granularity also lets us log exactly which Blackapple signals were hit by a winning combo.

Positional Pressure – Standalone Features

The Positional Pressure tool surfaces features per digit position and across draw variants
GitHub
. We identify the following scorable units:

Overdue Position Digit (Hard-Due) – Indicates a digit that has not appeared in a given position for longer than a threshold (≥55 draws for combined, ≥40 for midday/eve)
GitHub
. These “hard-due” digits are highlighted in red in the UI
GitHub
. As a feature, for each position P1, P2, P3 we can mark if the combo’s digit in that position was a hard-due digit. For example, if digit 7 in P3 was beyond the threshold in Combined, any combo with 7 in the third position gets POS3_OVERDUE. This can be generalized as POS_OVERDUE with position as an attribute. Implementation-wise, after computing positional gaps:

# pseudo-code: determine hard-due digits per position for each variant
hard_due_digits = {variant: {pos: [d for d,gap in gaps[pos] if gap >= HARD_DUE_THRESH[variant]]} }
# Later, for a combo:
for pos, digit in enumerate(combo):
    if digit in hard_due_digits['combined'][pos]:
        features.add(f'P{pos+1}_OVERDUE')


This feature lets us track if a winning number included any position that was under pressure. (It’s essentially the top-ranked gap digit, since the top of each PositionTop list will usually be the hard-due one if one exists.)

Cross-Variant Consensus (XVAR-Cons) – Marks when the same digit in the same position is simultaneously a top pick in multiple draw variants (e.g. a digit is overdue in P1 for both Combined and Midday)
GitHub
GitHub
. The positional engine assigns a tag like XVAR-Cons(CM) to such digits (for Combined+Midday consensus, for example)
GitHub
. To use this as a feature, we identify all position/digit pairs that appear across ≥2 variants’ top lists. Any combo containing that digit in that position gets the CONSENSUS feature. We can derive this from the analysis notes or directly from the data:

# given positional variant results for Combined, Midday, Evening:
consensus_positions = {}  # {(pos, digit): set of variants where it’s top}
for variant, pres in analysis.positional.variant_results.items():
    for pos, summ in pres.position_summaries.items():
        for top_digit in summ.top_digits:
            key = (pos, top_digit.digit)
            consensus_positions.setdefault(key, set()).add(variant)

for (pos,digit), vars in consensus_positions.items():
    if len(vars) > 1:
        # mark feature for combos having this digit in that pos
        consensus_tag = f'XVAR_CONSENSUS'
        features_for_position[pos][digit].add(consensus_tag)


Then when evaluating a specific combo: if its P2 digit is, say, 1 and (P2,1) had cross-variant alignment, we add XVAR_CONSENSUS to that combo’s features. This formalizes the XVAR-Cons tag (which appears as XVAR-Cons(...) in the UI
GitHub
) as a scoring factor.

Mirror Consensus (Mirror-Echo) – Similar to above, but for mirror digit alignment across variants. If digit D in position X is top in one variant and its mirror (e.g., D=1, mirror=6) is top in the same position in another variant, the tool tags those with Mirror-Echo
GitHub
. We treat this as a feature MIRROR_CONSENSUS: for a given position, if a digit and its mirror collectively appear in ≥2 variant top lists, then any combo containing either of those digits in that position can be tagged. For example, if P1 had 4 in Combined and 9 (mirror of 4) in Evening as top due, a combo with 4 or 9 in P1 would get the MIRROR_CONSENSUS feature. This is detected by the positional analysis (Mirror-Echo(C/E) tag)
GitHub
. Implementation can reuse the consensus mapping above by grouping by mirror pairs:

# Build mirror-consensus groups
mirror_consensus_positions = {}
for (pos, digit), vars in consensus_positions.items():
    mir = MIRROR_MAP.get(digit)
    if mir is None: 
        continue
    key = (pos, tuple(sorted([digit, mir])))
    mirror_consensus_positions.setdefault(key, set()).update(vars)
# If a mirror pair appears across multiple variants in same pos:
for (pos, pair), vars in mirror_consensus_positions.items():
    if len(vars) > 1:
        for digit in pair:
            features_for_position[pos][digit].add('MIRROR_CONSENSUS')


This ensures combos get a Mirror-Echo feature if they contain one of a mirror pair that had cross-variant presence.

Double-Pressure – Indicates a digit (or its mirror) is simultaneously pressuring two different positions (usually across variants)
GitHub
GitHub
. The positional engine tags such cases as Double-Pressure when a digit appears in the top 2 ranks of one position and also in another position’s top ranks (or its mirror does)
GitHub
GitHub
. We can treat DOUBLE_PRESSURE as a feature marking any combo digit that was part of a multi-position pressure cluster. Practically, if analysis notes say “Digit 7 (mirror 2) pressuring two positions across Combined, Midday”
GitHub
, then any combo containing 7 or 2 in either of those positions could be considered influenced by double-pressure. To implement, we gather all digits flagged by the analysis:

pressured_digits = set()
for note in analysis.positional.double_pressure_notes: 
    # e.g. "Digit 7 (mirror 2) pressuring two positions across Combined, Midday"
    m = re.match(r"Digit (\d+).*mirror (\d+).*Double-Pressure", note)
    if m:
        d, dm = int(m.group(1)), int(m.group(2))
        pressured_digits.update([d, dm])
# Feature assignment:
if any(int(digit) in pressured_digits for digit in combo):
    features.add('DOUBLE_PRESSURE')


This simplifies to: if a combo contains any digit that was under double-pressure, mark it. (For more precision, one could require the combo to have that digit specifically in the pressured positions, but since a combo can’t occupy two positions with one digit unless it’s a double combo, we use a simpler inclusion check.)

Adjacent Position Swap (Swap/Echo) – Flags a scenario where a top digit in one variant’s position swaps into an adjacent position in another variant. For example, if the top due for Combined P1 is 8 and the top due for Evening P2 is also 8, that “swap” is tagged as Swap
GitHub
GitHub
. Likewise if one is the mirror of the other, a Swap tag is still applied. As a feature, SWAP_ALIGN can be marked if a combo’s adjacent positions contain a pair of digits that correspond to an observed cross-variant swap. In practice, since swap signals involve two positions across two variants, a specific combo would have to have those two digits in those two positions (which could happen if the combo is a double or has the exact pair). We can identify swaps from the analysis (the engine adds a Swap tag to the PositionTopDigit entries involved
GitHub
) and then mark combos that realize that pairing. For simplicity, this feature might be less critical (swap signals are rarer), but we can include it for completeness. For example, if we detected P1:digit 3 (Combined) swapping with P2:digit 3 (Midday), then any combo like 3-3-x (with 3 in P1 and P2) gets SWAP_ECHO.

Top Rank Overlap (TOP1x) – Not a separate “user input” feature per se, but the positional candidate generation flags combos that include multiple #1 ranked digits. For instance, if a combo contains 2 of the 3 top-1 digits, it gets a “TOP1x2” tag and a small bonus score
GitHub
. We can treat the count of top-ranked digits in a combo as a derived feature (e.g., TOP1_COUNT). It’s an additive factor used internally (0.5 bonus for 2 or more top-ranked digits
GitHub
), and we can carry it forward for ML (a numeric feature or a categorical flag for “2 or 3 top picks in one combo”).

Each positional feature above can be given a weight or simply tracked as a boolean. In the current engine, these manifest as tags in the positional shortlist (e.g., tags like Mirror-Echo(CM), XVAR-Cons(ME), Double-Pressure)
GitHub
. By formalizing them, we enable compounding and logging. For example, if a winning number had a red-highlighted overdue digit in P3 and also was the consensus pick across combined/midday in P1, we’d log both P3_OVERDUE and XVAR_CONSENSUS as true for that draw.

Pairs Overdue Analysis – Standalone Features

The Pairs analysis tool flags overdue pair combinations using color codes. We can convert these into features:

Red Pair – Indicates the combo contains at least one digit-pair that is extremely overdue. In the overdue pairs logic, “RED” corresponds to pairs exceeding the higher threshold (e.g., ≥107 draws out for a double pair, ≥56 out for a non-repeating pair)
GitHub
. If any of the three internal pairs of the combo is tagged Red, we assign a RED_PAIR feature. This aligns with the “RED” category in the pair status output (often used to highlight very late pairs)
GitHub
GitHub
.

Blue Pair – Indicates the combo has an overdue pair (moderately late). “BLUE” is the next threshold (e.g., ≥71 for doubles, ≥37 for non-repeating)
GitHub
GitHub
. Any combo with a pair in the Blue category gets feature BLUE_PAIR. (If a pair qualifies as Red, we count it as Red rather than Blue since Red is higher priority.)

Purple Pair (Pending) – (Optional) a third tier for pairs that are somewhat overdue (>=25 draws out, used as “pending late”)
GitHub
. We might include a PURPLE_PAIR or PENDING_PAIR feature for completeness, though in many contexts Red and Blue are the primary flags of interest
GitHub
.

These pair features can be determined by computing the pair status for the current history and using the helper that maps a combo to the highest-priority color of its pairs
GitHub
GitHub
. For example:

color = get_combo_color(combo, pair_status)  # returns 'red', 'blue', 'purple', or ''
if color == 'red':
    features.add('RED_PAIR')
elif color == 'blue':
    features.add('BLUE_PAIR')
elif color == 'purple':
    features.add('PURPLE_PAIR')


This way, if the day’s winning combo contained an overdue pair (say one pair was last seen 120 draws ago), we’d log that it had a Red Pair feature. The control center could also display counts of how many Red/Blue pairs each state has pending
GitHub
, and we can tie that into scoring (e.g. combos with red pairs might get a higher priority in predictions).

V-Trac Index – (Not exactly a binary feature but a categorical attribute) Each combo corresponds to a V-Trac index (1–35) based on a transformation of its digits. The system tracks which V-Trac indices have appeared recently and highlights the top 5 “overdue” indices as well as recent hits
GitHub
GitHub
. We can treat a combo’s V-Trac index as a feature for compounding: e.g., a combo might get a boost if its index is among the top overdue indices or if it’s among recent hits. For instance, define VTRAC_OVERDUE feature if the combo’s index is in the overdue top-5. Likewise an index that just hit could have a marker (though likely we focus on overdue for prediction). This can compound with other features (e.g., “boxed V-Trac index 17 has multiple overdue signals”).

Digit Pattern Type – Another auxiliary attribute: whether the combo is a “Triple” (all digits same), “Double” (two same, one different), or “Single” (all distinct). And within singles, its S/T pattern (covered by Pattern Due above) or other patterns (like High/Low count, Even/Odd count) could be features. The current Blackapple covers only S/T pattern signals, but one could imagine separate features like ALL_LOW, ALL_HIGH, ALL_ODD, etc., if needed for ML. These are straightforward to derive from the combo but were not explicitly in the question; we note them as possible future features.

Each of these features is treated independently, meaning we calculate a boolean or score contribution for each, rather than just a combined score. The next step is to leverage these individual pieces in combination analytics.

Designing for Compounding Analytics

With distinct feature flags in place, we can design a system to compound them – i.e. analyze intersections of multiple signals for stronger predictions. There are two aspects to this:

 

1. Additive Scoring: By assigning each feature a weight and summing, we naturally compound signals – a combo that hits multiple features will score higher. This is essentially what Blackapple and the positional tool already do internally (summing weights of active tags)
GitHub
GitHub
. We can extend this to all features. For example, we might start with equal weights (1 point each) or use tuned weights (perhaps mirror, pattern, etc., are weaker signals so 0.5 each, whereas cross-variant consensus or an overdue pair might be stronger, say 1.5 each). A combo’s compound score would be:

score = 0
for feature in features_of_combo:
    score += FEATURE_WEIGHTS.get(feature, 1.0)


By adjusting FEATURE_WEIGHTS (similar to Blackapple’s WEIGHTS dict
GitHub
 or Positional WeightsConfig
GitHub
), the operator can calibrate how much each factor contributes. For instance, we could give a higher weight to RED_PAIR (very overdue pair) and ROOT_DUE since those signify long absences, while FLOATING or SWAP might be smaller bonuses. This additive model is transparent and easy to tweak, and it lays the groundwork for machine learning to potentially learn better weightings.

 

2. Multi-Feature Alignment Queries: Sometimes we want to identify when specific combinations of features coincide (not just additive, but logical AND). For example, the prompt mentioned “a boxed V-TRAC index with RED + PATTERN + FLOATING alignment across Combined/Midday.” This could be interpreted as looking for a scenario where:

A particular V-Trac index (say index 17’s set of combos) has multiple signals aligning,

Specifically, a Red pair overdue, a pattern-due trigger, and floating digits, and perhaps this is observed in both Combined and Midday analyses.

To support such compounding analytics, we can design our feature evaluation to not only output individual flags but also allow filtered views. Some approaches:

Tagged Combo Lists: Generate lists of candidate combos tagged with all their active features (as we do in Blackapple’s expander, which lists tags
GitHub
). Then use simple queries or filters on that list. For example, filter the list to combos where tags include all of {'RED_PAIR','PATTERN_DUE','FLOATING'} and see which V-Trac indices those belong to. If many combos from index 17 show all three tags, that index is a hot target.

Feature Set Intersection Logic: Programmatically, we could loop through all combos (or all V-Trac indices) and count how many signals each has. For instance:

for v_index, combos in combos_by_vtrac.items():
    for combo in combos:
        feats = features_of_combo(combo)
        if feats.issuperset({'RED_PAIR','PATTERN_DUE','FLOATING'}):
            vtrac_hits[v_index] += 1


If vtrac_hits[17] is notably high, index 17 has a compounding alignment of those features across many combos, which might warrant an “alert”. This can be extended to cross-variant: e.g., ensure the feature appears in both Combined and Midday variant data. Cross-variant alignment is already partly handled by the XVAR and Mirror-Echo features, but we can explicitly require that a feature is true in two contexts. For example, “PATTERN_DUE across Combined and Midday” means both variants flagged a pattern gap – we can check both variant outputs for pattern triggers and then consider it a stronger signal.

Composite Feature Definitions: We may even define new meta-features that represent common combinations. For example, define FLOATING_AND_RED that is true if both FLOATING and RED_PAIR features are true for a combo. This could get combinatorially large, so better is to handle via queries or on-the-fly compounding as above. However, for known strategic combos like the example, one could create a special case: e.g., if a certain V-Trac index hasn’t hit (index overdue) and now also one of its combos has a Red pair and a due pattern, that index could be given an “Index Alert” score.

In practice, a user-friendly way to do compounding is via the Control Center or Aux page: provide interactive filters or pre-defined compound criteria. E.g., a section “Compound Alerts” could list things like “Index 17 (boxed) – RED pair + Pattern due + Floating digit (Combined & Midday alignment)” if such a scenario arises, essentially automating what an expert might look for manually.

 

Under the hood, this requires our code to easily cross-reference features. Because we’ve modularized feature computation, it’s straightforward to combine results. We might implement a helper like:

def combos_with_features(all_combos, required_feats):
    return [c for c in all_combos if features_of_combo(c).issuperset(required_feats)]


Using this, any compound query is one line. This is powerful for advanced analysis and also for feeding into correlation testing (we can examine how often certain feature combos lead to hits).

Winners Logging Integration

To close the loop, we integrate these features into the automated winners logging. The goal is that whenever a winning draw is recorded, the system automatically checks which features were aligned for that winning combo on that day.

 

Approach: After each draw, run the analysis for that state/variant (Blackapple, Positional, Pairs) for the recent history up to just before the win. Then evaluate the winning combo against all features.

 

We can build a WinnerFeatureReport data structure to hold this info, and log it (as a row in a CSV or database, and/or display in the UI).

 

For example, a simplified code flow for logging a winner’s features:

def log_winner_features(state, variant, winning_combo):
    # 1. Load recent draws and run analyses
    draws = load_state_draws(state, variant)
    ba_result = blackapple.analyze_blackapple(draws)
    pos_result = positional.analyze_state_variants({ 'combined': draws, ... })  # include other variants if needed
    pair_nonrep, pair_rep, pair_status = analyze_pairs.calculate_overdue_pairs(draws)

    # 2. Evaluate features for the winning combo
    feature_set = evaluate_combo_features(winning_combo, ba_result, pos_result, pair_status)
    status = ba_result['score']  # BA status (OFF/WATCH/ALERT) if we want to log overall status too
    
    # 3. Log or output
    log_entry = {
        'date': today, 'state': state, 'variant': variant, 'winning_combo': winning_combo,
        'BA_status': ba_status_label(ba_result['score']),
        **{feat: (feat in feature_set) for feat in ALL_FEATURES}
    }
    append_to_csv('winners_log.csv', log_entry)


Here, evaluate_combo_features would implement the checks described in earlier sections, combining all modules’ signals to return a set of feature tags that apply to the given combo. The resulting log entry might look like:

Date, State, Variant, WinningCombo, BA_status, MIRROR, FLOATING, ROOT_DUE, PATTERN_DUE, PAIR_FOUNDATION, P1_OVERDUE, P2_OVERDUE, P3_OVERDUE, XVAR_CONSENSUS, MIRROR_CONSENSUS, DOUBLE_PRESSURE, SWAP_ALIGN, RED_PAIR, BLUE_PAIR, ... etc.
2025-09-29, NY, Midday, 502, ALERT, TRUE, TRUE, FALSE, TRUE, TRUE, FALSE, TRUE, FALSE, TRUE, FALSE, FALSE, FALSE, TRUE, FALSE, ...


In this hypothetical example, the winning combo “502” triggered multiple features (maybe it had a mirror pair and a floating digit, etc.) and Blackapple had an ALERT for that state. The system can automatically record this. Over time, this log provides a rich dataset of which features tend to coincide with winning numbers.

 

Automated Checks: We will implement this logging as part of the draw result entry workflow. For instance, when the operator marks a draw as completed or enters the winning number, the app can generate the feature report for that draw. This could be done server-side so it’s ready by the time the operator looks at the results.

 

Using the Logged Data: The Control Center could show a summary like “Features hit by yesterday’s winners”, or simply rely on the CSV for offline analysis. For example, we might observe that many winners had FLOATING true, suggesting floating digits are a strong signal, or that few winners had SWAP_ALIGN, suggesting that feature is less useful. This feedback can help tweak weights or feature definitions (a step toward ML model training).

Integration into Control Center and Logs

We aim for a hands-off workflow: the user shouldn’t have to manually toggle these analyses each time. Thus:

Control Center UI: We can add a section or columns to surface feature scores. The existing Control Center shows a per-state Blackapple status and examples, plus a positional heat badge
GitHub
GitHub
. We can extend this:

Add a column “Feature Count” or “Signals” that simply lists how many of the defined features are triggered for the top candidate (or for the BA examples). For instance, if the top BA candidate for a state has tags MIR, FLT, PAIR, we could show “3 signals”. This gives a quick sense of signal density.

Alternatively, use small icons or color codes in the “Examples” or a tooltip. E.g., hover over a candidate to see its feature tags.

Since there are many possible features, listing all in the table might overwhelm. Instead, the Control Center could have an expandable “Feature Matrix” per state. Clicking it would show a table of the top N combos with columns for each feature (a checkmark if present). This essentially exposes the feature vector for each candidate.

Auxiliary Tools Page: The Aux page already displays detailed Positional and (optionally) Blackapple state panels. We could integrate an “Overdue Pairs” panel that lists Red/Blue pairs counts (or top overdue pairs) for that state. We can also show a combined shortlist that merges Blackapple and Positional candidates, annotated with all features. This gives power users a one-stop view.

Exportable Logs: All the feature information should be exportable. We will maintain:

A daily Winners Log (as described) for actual outcomes.

Optionally, a Feature Predictions Log that for each state/day lists the top recommended combos and their features. For example, each morning the system could output a CSV of each state’s “predictions” with feature tags, which the user can later cross-reference with the actual draw. This is analogous to back-testing data.

Per-state variant logs: e.g., a running log for each state that records each draw’s feature triggers (even for non-winning combos, possibly just the signals that were active that day). For instance, “Day X: Mirror trigger ON, Root sum 7 due, Red pair count 2” etc. This can help spot trends like “state Y had a root sum due for 10 days and then it finally hit.”

Implementing these, in code we might extend the ControlCenter component of our Streamlit app to include new data. For example, if we have a dataframe of feature counts or a preformatted HTML with icons, we can inject it into the table or as an expander below each row.

 

For logging, the code snippet above already writes to CSV. We ensure this happens automatically (perhaps nightly or whenever new draws are ingested). The logs can be stored in logs/features/ directory or similar for easy access.

 

To maintain simplicity, these features and their logging run off the same data sources we already have (draws CSVs). We avoid introducing new data requirements. And we will guard it so that if a data file is missing, it simply skips that feature (so the app remains robust).

Future ML Integration and Extensibility

By structuring each signal as a standalone feature, we’ve essentially created a feature vector that can feed machine learning models or more sophisticated analytics:

Lightweight Scoring: The additive model with tunable weights is a form of a linear model that can be adjusted manually or via ML. In the near term, we keep it “lightweight” – simple addition of points – to retain interpretability. Each feature’s contribution is clear and we can tweak weights easily (for example, using grid search or even a genetic algorithm on historical data to find an optimal weight set that best predicts hits).

Feature Tag Output: We already produce tags for human reading; for ML we will produce numeric encodings. For example, we can one-hot encode each feature (True/False becomes 1/0). Our winners log CSV is essentially the training data: features vs outcome=win (though every logged row is a win by definition; to train a model we’d need to include non-winning combos as well). We could augment the log to include, say, the top recommended combo each day that did not win, as negative examples for ML.

Additive & Combinatorial Logic: Because our design treats features modularly, it’s easy to experiment with additional features or new combinations. If a new lottery strategy emerges (say tracking last-digit repeats, or some AI-detected pattern), we can add it as another feature function without disrupting the others. The scoring and logging automatically include any new feature added to the ALL_FEATURES list.

Correlation and Pattern Learning: With all features logged, we can compute correlations (e.g., does DOUBLE_PRESSURE correlate with wins?) and even allow an ML model to learn non-linear interactions that our manual compounding might miss. For instance, a decision tree could learn that “if ROOT_DUE and RED_PAIR are both true, probability of win doubles”, effectively learning a compound rule. Our system’s logs and feature extraction make such exploration possible.

Modular Code Design: The implementation is divided into clear modules:

blackapple_features.py – wraps Blackapple analysis and extracts the five BA features for any combo.

positional_features.py – provides functions to get the positional feature flags (overdue positions, consensus, etc.) given the positional analysis result.

pair_features.py – computes overdue pairs and provides get_combo_color and related utilities for pair-based features.

feature_scorer.py – orchestrates combining all feature computations and scoring a combo or generating a feature vector. This might include a FeatureScorer class that holds the current state’s analysis context and has methods like score_combo(combo) which returns a tuple (score, feature_tags).

winner_logger.py – handles writing the feature logs, possibly using the above classes.

By breaking it down this way, each piece is maintainable. We ensure extensibility: adding a new feature is as simple as writing a new function and adding its name to the feature list. The rest of the pipeline (scoring, logging, UI) can pick it up if designed generically (for example, using features.add(name) and iterating over FEATURE_WEIGHTS means new features automatically get a default weight and are logged).

 

In summary, we end up with a robust system where each lottery analysis signal – Mirror pairs, floating digits, overdue roots, positional gaps, pair colors, etc. – is an individually trackable and tunable unit. We can mix and match these signals for deeper analysis (compounding them), log exactly what happened when a number hits, display them in the app for transparency, and feed them into future ML models. This approach provides immediate usability and clarity, and it sets up a path for more advanced predictive analytics down the line (such as having an ML model suggest weight adjustments or discover new patterns), all while keeping the workflow largely automated and the complexity under the hood.

 

Sources:

Blackapple triggers and scoring logic
GitHub
GitHub

Explanation of remaining-pairs foundation (27–29 method)
GitHub

Positional pressure tags: mirror, consensus, double-pressure, etc.
GitHub
GitHub

Positional analysis scoring and tag injection (Mirror-Echo, XVAR-Cons, Swap)
GitHub
GitHub
GitHub

Overdue pair thresholds for Red/Blue categories
GitHub
GitHub

V-Trac index analysis snippet
GitHub
GitHub
 (demonstrating how combo statuses like color and shapes are assigned per index)