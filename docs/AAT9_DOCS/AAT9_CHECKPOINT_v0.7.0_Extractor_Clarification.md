# AAT9 - Project Checkpoint v0.7.0
## Stable Pattern Extractor Clarification - June 21

### 1. The Problem: A Major Mix-Up

We have just resolved a significant point of confusion regarding the **Stable Pattern Extractor**. Previous work may have involved incorrect, older, or less comprehensive versions of the script. This caused a cascade of problems and circular debugging. The project had multiple scripts with similar names (`pattern_extractor`, `stable_pattern_analyzer_standalone`, etc.), making it difficult to identify the correct tool.

### 2. The Solution: Discovery of Authoritative Documentation

The confusion was resolved upon finding a set of highly detailed documents created by the user, which laid out the full design, features, and known bugs of the *correct* and most advanced tool.

These documents are now the **single source of truth** for this module. They are essential reading for any future work on this tool.

**Location:** `docs/stable_pattern_guide/`

The most important file is `stable_pattern_master_guide_AAT9.md`, which contains the complete blueprint.

### 3. The Correct Tool and Its Status

**The one and only correct script for this module is:**
*   `scripts/tools/stable_pattern_extractor.py`

**The correct configuration file it uses is:**
*   `scripts/tools/feature_config.yml`

**Current Status:** The script is approximately 95% complete. Recent debugging work was successful because it was aligned with fixing the known bugs listed in Part 5 and Part 9 of the `MASTER GUIDE`. All comprehensive features (Dominant Survivor, Consensus, flexible scoring, etc.) are present in the code.

### 4. Directive for Future AI Assistants & Developers

**READ THIS FIRST.** Before performing any work on the Stable Pattern Extractor, you **must** review the documentation in `docs/stable_pattern_guide/`.

*   **DO NOT** use any other script from the archive or elsewhere that claims to be a pattern extractor.
*   **DO** reference the `MASTER GUIDE` to understand the purpose of each feature and scoring weight. All scoring logic is driven by the `feature_config.yml` file.
*   **The immediate next step** is to implement the final small bug fixes listed in the `MASTER GUIDE` to get the tool to a stable "v1.0 LOCKED" state. After that, work can begin on the subsequent modules (e.g., Long-String Digit-Reduction).

This checkpoint solidifies our understanding and should prevent any future AI from repeating past mistakes. The path forward is now clear and well-documented. 