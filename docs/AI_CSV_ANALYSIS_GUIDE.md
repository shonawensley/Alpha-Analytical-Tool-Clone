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