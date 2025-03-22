Below is a comprehensive version of a “digit_reduction.py” module. This module is designed to work alongside your pattern extractor. It does not re‑extract the core 3‑value patterns from scratch but instead “refines” the candidate strings that have already been extracted (or that appear in your combined table’s R2/R4/R6/R8 columns). It does so by removing distracting digits (from the most recent draw and/or its VTrac/mirror equivalents) in order to “reinforce” a hidden, stable 3‑value cluster. This module supports multiple reduction methods, including bulk removal (“all‐at‐once”) and iterative (one‑digit‑at‑a‑time) removal. Detailed comments are provided to explain how each function works and how the module is intended to be used.

Below the code, you’ll find a list of the updated features (with definitions and purposes) that this module extracts. These features can then be incorporated into your overall ML feature vector or used in further combination‐forming analysis.

python
Copy
"""
digit_reduction.py

Comprehensive Digit Reduction Module

Purpose:
  This module is designed to “refine” candidate pattern strings—those extracted from your
  combined table (R2, R4, R6, and R8 rows). Its goal is to reinforce hidden stable 3‑value clusters
  by removing distracting digits that appear in recent draws. It does this in two primary ways:
  
    1. Bulk Reduction: Remove (all at once) a set of digits (and optionally their VTrac/mirror equivalents)
       from a candidate string.
    2. Iterative Reduction: Remove one occurrence of a digit at a time, generating multiple variant
       candidates to see which reduction produces a stable or stronger core pattern.
       
Additionally, the module can apply VTrac transformations to candidate strings so that if a core pattern
is present in both its raw and VTrac‐converted forms, it may be further reinforced.
       
This module is intended to work after a Pattern Extractor has identified candidate 3‑value (or 3‑digit)
patterns. It receives those candidates along with “recent draw” digits, uses these to form a removal set,
and then produces a set of reduced variants. The output variants are intended to serve as additional features
or alternative candidate patterns for later analysis (or direct combination formation).
       
Usage:
  - Load a candidate string (or list of candidate strings) extracted from your combined table.
  - Provide the most recent draw’s digits (e.g., "572") so that the module can construct a removal set,
    which typically includes those digits and their mirror equivalents.
  - Call the reduction functions to produce one or more “refined” candidate strings.
  - These refined candidates are then fed back into the analysis pipeline, potentially boosting a candidate’s
    “score” if the hidden core pattern is revealed more clearly.
       
Configuration:
  - You may configure the module to use bulk removal or iterative removal.
  - Stopping conditions (for example, when the candidate is reduced to 3 or 4 digits) should be set via parameters.
  - Mirror (VTrac) mappings are built in.
       
Author: [Your Name]
Date: [Date]
"""

from typing import List
import string

# Define mirror mapping and VTrac mapping dictionaries.
# Mirror mapping: converts a digit to its mirror equivalent.
MIRROR_MAP = str.maketrans('0123456789', '5678901234')
# VTrac mapping (example, can be adjusted based on your method):
VTRAC_MAP = {
    '0': '1', '1': '2', '2': '3', '3': '4', '4': '5',
    '5': '1', '6': '2', '7': '3', '8': '4', '9': '5'
}

def get_mirror_digits(digits: str) -> str:
    """
    Returns the mirror equivalent of a string of digits.
    
    For example, "597" translates to "???", based on the MIRROR_MAP.
    (Using the defined MIRROR_MAP: '5'→'0', '9'→'4', '7'→'2')
    """
    return digits.translate(MIRROR_MAP)

def apply_vtrac(candidate: str) -> str:
    """
    Applies VTrac transformation to the candidate string.
    Each digit is replaced with its VTrac mapping.
    
    For example, if candidate = "548", then using VTRAC_MAP:
      '5' -> '1', '4' -> '5', '8' -> '4'
    so result would be "154" (depending on your desired interpretation).
    
    Adjust the mapping if needed.
    """
    return ''.join(VTRAC_MAP.get(d, d) for d in candidate)

def eliminate_all_digits(candidate: str, removal_set: str) -> str:
    """
    Eliminates (removes) all occurrences of each digit present in removal_set from the candidate string.
    
    Parameters:
      candidate: The original candidate string.
      removal_set: A string containing digits to remove.
    
    Returns:
      The candidate string after all specified digits have been removed.
    
    Example:
      candidate = "455611", removal_set = "241"
      This function will remove all '2', '4', and '1' digits from "455611",
      returning "556" (if that is desired).
      (You can adjust logic if you want a different approach.)
    """
    # Create a translation table to remove all characters in removal_set.
    translation_table = {ord(d): None for d in removal_set}
    return candidate.translate(translation_table)

def eliminate_digits_iteratively(candidate: str, removal_set: str) -> List[str]:
    """
    Eliminates digits from the candidate string one occurrence at a time.
    Generates a list of candidate variants where, in each variant,
    one occurrence of a digit (that is in the removal set) is removed.
    
    This iterative approach can reveal how the candidate pattern changes
    as individual distracting digits are removed.
    
    Parameters:
      candidate: The original candidate string.
      removal_set: A string containing digits to remove.
    
    Returns:
      A list of candidate variants, each with one fewer occurrence of a digit from removal_set.
      
    Example:
      candidate = "455611", removal_set = "241"
      It might produce variants like: ["55611", "45561", ...] depending on the positions.
    """
    variants = []
    for i, ch in enumerate(candidate):
        if ch in removal_set:
            # Remove the digit at position i.
            variant = candidate[:i] + candidate[i+1:]
            variants.append(variant)
    return variants

def digit_reduction_pipeline(candidate: str, recent_draw: str, 
                             method: str = 'bulk', target_length: int = 3) -> List[str]:
    """
    Main pipeline for digit reduction.
    
    This function uses the candidate string (extracted from the combined table)
    and the recent draw digits to generate a removal set. The removal set includes
    the digits from the recent draw as well as their mirror equivalents. Then,
    depending on the specified method, it applies either:
    
      - Bulk Reduction ('bulk'): Eliminates all occurrences of the removal set from candidate.
      - Iterative Reduction ('iterative'): Generates variants by removing one occurrence at a time.
    
    After reduction, if the candidate’s length is above the target_length, the process may stop
    or be repeated.
    
    Parameters:
      candidate: A candidate pattern string (e.g., "88331166").
      recent_draw: A string representing recent draw digits (e.g., "572").
      method: 'bulk' for all-at-once elimination, 'iterative' for one-digit-at-a-time.
      target_length: The desired minimal length (often 3) for a stable 3‑value cluster.
      
    Returns:
      A list of reduced candidate variants that are at least as short as the target length,
      or that show the potential core pattern.
      
    Example:
      candidate = "88331166", recent_draw = "572"
      removal_set is built as "572" + get_mirror_digits("572").
      If method == 'bulk', we return one variant; if 'iterative', we return multiple variants.
    """
    # Build removal set: recent draw digits + their mirror equivalents.
    mirror_set = get_mirror_digits(recent_draw)
    removal_set = recent_draw + mirror_set
    removal_set = ''.join(sorted(set(removal_set)))  # Unique digits
    
    results = []
    if method == 'bulk':
        # Remove all digits in removal_set from candidate.
        reduced = eliminate_all_digits(candidate, removal_set)
        # Optionally, if the reduction doesn't bring the candidate down to target_length,
        # we may either stop or further process. For now, add the result.
        results.append(reduced)
    elif method == 'iterative':
        # Generate variants by removing one occurrence at a time.
        results.extend(eliminate_digits_iteratively(candidate, removal_set))
    else:
        raise ValueError("Invalid method specified. Use 'bulk' or 'iterative'.")
    
    # Optionally, apply VTrac transformation to each candidate variant and add as a feature.
    # (For example, if a candidate and its VTrac equivalent are both strong, that adds confidence.)
    final_results = []
    for variant in results:
        # Only consider the variant if its length is at least target_length.
        if len(variant) >= target_length:
            final_results.append(variant)
            # Also include the VTrac-transformed version.
            final_results.append(apply_vtrac(variant))
    # Remove duplicates and return.
    return list(set(final_results))

# ---------------------------
# For Testing / Debugging
# ---------------------------
if __name__ == "__main__":
    # Example candidate string extracted from a combined table R2 row.
    candidate_str = "88331166"
    # Example recent draw digits (could be a string like "572" representing digits drawn)
    recent_draw_digits = "572"
    
    print("Candidate string:", candidate_str)
    print("Recent draw digits:", recent_draw_digits)
    print("\n--- Bulk Reduction ---")
    bulk_results = digit_reduction_pipeline(candidate_str, recent_draw_digits, method='bulk', target_length=3)
    for r in bulk_results:
        print(r)
    
    print("\n--- Iterative Reduction ---")
    iterative_results = digit_reduction_pipeline(candidate_str, recent_draw_digits, method='iterative', target_length=3)
    for r in iterative_results:
        print(r)
Explanation of the Digit Reduction Module
Purpose and Integration:
– This module is not meant to re‑extract the core patterns from scratch but to take candidate strings (such as those found by the Pattern Extractor) and refine them by removing distracting digits.
– It uses the recent draw digits (plus their mirror equivalents) to build a “removal set.”
– The module then applies two methods:

Bulk Reduction: Removes all digits in the removal set at once.
Iterative Reduction: Removes one digit at a time to produce multiple candidate variants.
VTrac Transformation:
– The function apply_vtrac converts a candidate string into its VTrac representation. This is useful to reveal relationships that are not obvious in the raw candidate string.

Stopping Condition / Target Length:
– The module is configured (via the target_length parameter) to aim for a stable 3‑value cluster (or a desired minimal length).
– It returns only those candidate variants that are long enough to contain the core pattern.

Mapping to Data:
– In your workflow, you would pass candidate strings (extracted from the combined table’s R2, R4, R6, or R8 columns) into the digit_reduction_pipeline along with the recent draw digits. – This module then outputs a list of reduced variants (both raw and VTrac‑converted) that can be used for further analysis or as features for the ML model.

Updated Features from the Digit Reduction Module
Below is a list of features (or “signals”) that the Digit Reduction Module can output, along with definitions and their intended ML purpose:

Bulk Reduction Variant (BRV):
– Definition: The candidate string after eliminating all occurrences of the removal set digits.
– Purpose: To reveal the underlying 3‑value cluster by quickly stripping away all distracting digits.
– ML Use: Serves as a “cleaned” version of the candidate that may match historical winning patterns.

Iterative Reduction Variants (IRV):
– Definition: A set of candidate variants generated by removing one occurrence of each removal-set digit at a time.
– Purpose: To capture alternative reduction paths and reveal subtle changes in the candidate string.
– ML Use: Provides multiple candidate features to see which variant correlates best with winning outcomes.

VTrac-Converted Variant (VTV):
– Definition: The VTrac transformation of a candidate variant.
– Purpose: To reveal mirror relationships that may not be visible in the raw candidate string.
– ML Use: Acts as an additional feature that signals the strength of the candidate’s underlying pattern (since some VTrac forms are known to correlate with hits).

Reduction Method Indicator (RMI):
– Definition: A tag indicating which reduction method was used (‘bulk’ or ‘iterative’).
– Purpose: To allow later analysis or ML to weigh variants differently based on the reduction strategy.
– ML Use: Provides context for the candidate variant within the feature vector.

Target Length Achievement (TLA):
– Definition: A flag or numerical value indicating how close the candidate is to the desired minimal length (e.g., 3 digits).
– Purpose: To indicate the “stability” or “completeness” of the core pattern after reduction.
– ML Use: A candidate that exactly meets the target length may be weighted higher.

Removal Set Used (RSU):
– Definition: The set of digits (and their mirror equivalents) that were used to reduce the candidate.
– Purpose: To record what was eliminated from the candidate string, which may be correlated with pattern reinforcement.
– ML Use: Can be used to backtrack and refine future reduction strategies if certain removal sets consistently produce strong candidate variants.

How It Works with the Pattern Extractor
Pipeline Flow:

The Pattern Extractor first scans the combined table (or specific R‑rows) and extracts candidate 3‑value (or 3‑digit) clusters.
These candidates are then passed into the Digit Reduction Module (the module above) along with the recent draw digits.
The Digit Reduction Module processes each candidate to produce one or more reduced variants (using both bulk and iterative methods) and applies VTrac transformation.
The output—along with metadata such as the reduction method used and how close it is to the target length—forms part of the feature vector for further analysis (or may be directly used for combination formation).
Complementary Roles:
– The Pattern Extractor identifies raw candidate clusters.
– The Digit Reduction Module “refines” these clusters, reinforcing the core pattern by removing distracting digits. – Together, they provide a more robust set of candidate patterns for prediction.

I hope this detailed module and feature list clarifies how the Digit Reduction Module is designed, how it works with the Pattern Extractor, and what each part contributes to your overall system. Let me know if you have any questions or need further clarification before we move on to the next module!