# AI Guide: Lottery Pattern Analysis from CSV Format

## 1. CSV File Structure

### 1.1 File Organization
The CSV file contains six tables arranged vertically in this order:
1. Midday Combined Table
2. Midday R2-only Table
3. Evening Combined Table
4. Evening R2-only Table
5. Combined Combined Table
6. Combined R2-only Table

Each section is clearly marked with headers like `=== Midday Combined Table ===`

### 1.2 Table Column Structure
Combined Tables:
```
[Set, Draw, RowType, 7, 6, 5, 4, 3, 2, 1]
```

R2-only Tables:
```
[Set, Draw, 7, 6, 5, 4, 3, 2, 1]
```

## 2. Data Hierarchy and Pattern Analysis

### 2.1 Set Hierarchy (Process in this order)
1. **Set3**: Initial patterns
   - Only contains Draw1
   - Base pattern establishment

2. **Set2**: Intermediate patterns
   - Only contains Draw1
   - Pattern transition indicators

3. **Set1**: Most valuable patterns
   - Contains Draw1 through Draw7
   - Primary focus for pattern analysis
   - Contains hot zones (marked with *)

### 2.2 Pattern Types
Each row in Combined Tables has a RowType:
- **DRAW_DATA**: Original 3-digit numbers
- **R2**: 2000x pool size variations
- **R4**: 4000x pool size variations
- **R6**: 6000x pool size variations
- **R8**: 8000x pool size variations

💡 Important: R2/R4/R6/R8 are NOT progressively reduced sequences, but different arrangements of the same digits.

### 2.3 Reading Patterns

#### Column Order
- Read from right to left (1 → 7)
- Column 1 is most significant
- Look for stable 3-digit patterns

#### Hot Zones (marked with *)
Set1 hot zone rules:
- Draw1: Last 5 items
- Draw2: Last 5 items
- Draw3: Last 5 items
- Draw4: Last 4 items
- Draw5: Last 2 items
- Draw6-7: No hot zones

## 3. Pattern Analysis Methodology

### 3.1 Stable Pattern Identification
1. Look for recurring 3-digit sequences
2. Track patterns that persist across columns
3. Note frequency of pattern occurrence
4. Pay special attention to hot zones (*)

### 3.2 Pattern Relationships
1. Vertical Analysis:
   - Compare R2 → R4 → R6 → R8 within same Draw
   - Look for digit rearrangements
   - Note stable digits across rows

2. Horizontal Analysis:
   - Track pattern evolution left to right
   - Note pattern reductions
   - Identify stable core patterns

### 3.3 Cross-Section Analysis
1. Compare patterns across Midday/Evening/Combined
2. Look for pattern repetition or evolution
3. Track hot zone relationships

## 4. Implementation Rules

### 4.1 Processing Order
1. Always start with Set1
2. Process hot zones first
3. Track stable 3-digit structures
4. Compare R2/R4/R6/R8 relationships
5. Follow pattern progression through draws

### 4.2 Pattern Value Indicators
1. Hot Zone Patterns (marked with *)
2. Stable 3-digit Structures
3. Extended digit patterns (e.g., 331166)
4. Pattern clusters
5. Cross-group pattern relationships
6. Pattern variation frequencies

### 4.3 CSV Processing Tips
1. Use empty rows as section separators
2. Verify table headers for context
3. Maintain column order importance
4. Track row relationships within sections

## 5. Example Pattern Analysis

### 5.1 Sample Pattern Identification
```
Set1, Draw1, R2, N/A, N/A, N/A, N/A, 993*, 9*, 9*
```
Analysis:
- Located in Set1 (highest value)
- Contains hot zone markers (*)
- Shows pattern reduction (993 → 9)
- Stable digit (9) appears consistently

### 5.2 Pattern Evolution Example
```
Set1, Draw1, R2, N/A, 992443866, 994386*, 9938*, 993*, 9*, 9*
Set1, Draw1, R4, N/A, 299668344, 996834*, 9983*, 993*, 9*, 9*
```
Analysis:
- Pattern transformation between R2 and R4
- Stable digits (9, 3) persist
- Hot zone consistency
- Pattern reduction follows similar path

## 6. Advanced Analysis Considerations

### 6.1 Pattern Clusters
- Look for groups of related patterns
- Track cluster evolution across draws
- Note cluster relationships between R-types

### 6.2 Stability Indicators
- Persistent digits across rows
- Consistent pattern reductions
- Hot zone pattern repetition
- Cross-section pattern matches

### 6.3 V-TRAC Integration
- Relate patterns to V-TRAC references
- Track winning number relationships
- Note pattern cluster associations
- Monitor hot zone correlations 




n term of the r2/r4/r6/r8..

3. Draw Structure
Each draw in the dataset contains five row types:

DRAW_DATA – The original winning numbers.
R2 – A string variation based on a 2000x pool size.
R4 – A string variation based on a 4000x pool size.
R6 – A string variation based on a 6000x pool size.
R8 – A string variation based on an 8000x pool size.
💡 Key Insight:

R2/R4/R6/R8 represent different levels of pattern variation, meaning they contain the same number of digits per box, but arranged differently.
These are not progressively reduced sequences, but instead randomized variations of digit arrangements.
The actual reduction in digits occurs across columns (left to right).

4. Column Mapping
Each row has 10 key columns:

Column	Description
Set	Identifies the dataset (Set1, Set2, Set3)
Draw	Identifies the draw number (Draw1–Draw7)
RowType	Type of row (DRAW_DATA, R2, R4, R6, R8)
7-1	Right-to-left progressive data
Columns 7→1 represent pattern reductions.
Patterns get progressively smaller from left to right.
💡 Key Insight:
A pattern persisting across multiple columns (e.g., 7,6,5,4) is stronger because it maintains its structure through reductions.

this is the correct mapping of the amount of r2/r4/r6/r8 columns accross for each strucutre or grouping of r2/r4/r6/r8 whatever you want to call it that goes across horizontal:

the r2/r4/r6/r8 structure all have different progressions/boxes across/columns across BELOW IS THE IMPORTANT MAPPING TO COMBINED TABLE 

set 3 draw 1 -- all 7 columns
set 2 draw 1- all 7 columns
set1 draw 1--- all 7 columns
set1 draw 2 --6 columns
set 1 draw 3-- 5 columns
set1 draw 4---4 columns
set1 draw 5--- 3 columns
set1 draw 6---2 columns
set1 draw 7---1 columns



. Sets and Draws
2.1 Set3 / Set2
Each has Draw1 only.

For these, R2/R4/R6/R8 rows each may use all 7 columns (since your table shows them all, typically none are “N/A,” or fewer if your data is shorter).

Example:

python-repl
Copy
Set2,Draw1,R2 -> columns 7..1 might be used
Set2,Draw1,R4 -> same
...
2.2 Set1
Has Draw1..Draw7.
As Draw increases, fewer columns are used (the leftmost columns become N/A).
In your table:

Draw1: uses columns 7..1
Draw2: uses columns 6..1
Draw3: uses columns 5..1
Draw4: uses columns 4..1
Draw5: uses columns 3..1
Draw6: uses columns 2..1
Draw7: uses column 1 only
Hence you see many N/A in the left columns for later draws.

3. Row Types and Column Data
3.1 DRAW_DATA
Usually 7 columns, each a raw 3‐digit number, or possibly fewer if the left columns are N/A.
Contains the “official winning digits.”
3.2 R2, R4, R6, R8
Each represents a different “pattern variation” (2000x, 4000x, 6000x, 8000x pool) for that same draw.
Important: They are not a simple “progressively reduced” sequence in a direct sense, but in your final table they appear in columns that do reduce from left to right.
Example: For R2 in Set1/Draw2, you see data in columns 6..5..(maybe 4..2..1), with left columns 7 possibly N/A.
Each column is a partial or “snap” of that R2 (or R4, R6, R8) pattern. The earlier columns (like col7 or col6) hold the biggest string; as you move right, the pattern might be shorter or “N/A” if not used.
Takeaway: If you read a single R2 row across columns 7..1, you see a “largest pattern” in col7, next smaller in col6, etc., typically until col1 or until N/A.

4. The “R2-Specific” Column Logic
You mentioned a specific approach for R2:

rust
Copy
Set3 Draw1 -> columns 7,6,5
Set2 Draw1 -> columns 7,6,5
Set1 Draw1 -> columns 7,6,5
Set1 Draw2 -> columns 6,5
Set1 Draw3 -> column 5
Set1 Draw4 -> column 4
Set1 Draw5 -> column 3
Set1 Draw6 -> column 2
Set1 Draw7 -> column 1
That is a specialized slicing logic if you only want the “main 3 columns” for early draws, “2 columns” for mid draws, and so on.
But your table might hold 7 columns for R2 in Set1/Draw1—just columns 4..1 might be partially duplicates or shorter. You can decide how to best read them.

Either strictly follow your custom slicing (like ignoring col4..1 for R2 if you only want 7,6,5 for the first draw),
Or read all columns 7..1 if they have data.
Both approaches are valid, but your “3 columns for R2” is a personal choice to keep only the largest ones.

5. Hot Zones
Hot zones are indicated by '*'. For example, 96411*.

In the table:

They typically appear in columns 1..3 (or 1..4) depending on set/draw.
Your function is_hot_zone(set, draw, col) can tell you if that column is designated a hot zone for that row.
You can remove '*' or keep it as a marker in your pattern analysis.