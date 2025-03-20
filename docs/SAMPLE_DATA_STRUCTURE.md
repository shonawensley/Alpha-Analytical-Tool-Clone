# Lottery Data Structure Sample

## 1. Raw Data Structure

```python
# Sample of how the data is structured internally
sample_data = {
    "Midday": {  # Can be Midday/Evening/Combined
        "Set3": {
            "Draw1": {
                "draw_data": ["934", "916", "319", "917", "723", "753", "832"],
                "R2": ["55924001877", "552400877", "552400877", "55240087", "554008", "54008", "5400"],
                "R4": ["25590084771", "255008477", "255008477", "25500847", "550084", "50084", "5004"],
                "R6": ["81770055924", "877005524", "877005524", "87005524", "800554", "80054", "0054"],
                "R8": ["77001982455", "770082455", "770082455", "70082455", "008455", "00845", "0045"]
            }
        },
        "Set2": {
            "Draw1": {
                "draw_data": ["827", "705", "130", "246", "640", "008", "390"],
                "R2": ["992440013866", "99244013866", "99244866", "99486", "998", "99", "9"],
                "R4": ["299006683441", "29906683441", "29966844", "99684", "998", "99", "9"],
                "R6": ["668100993244", "66810993244", "66899244", "68994", "899", "99", "9"],
                "R8": ["001998366244", "01998366244", "99866244", "99864", "998", "99", "9"]
            }
        },
        "Set1": {
            "Draw1": {
                "draw_data": ["705", "130", "246", "640", "008", "390", "408"],
                "R2": ["992440133866", "992443866", "994386", "9938", "993", "9", "9"],
                "R4": ["299066833441", "299668344", "996834", "9983", "993", "9", "9"],
                "R6": ["668109933244", "668993244", "689934", "8993", "993", "9", "9"],
                "R8": ["019983366244", "998366244", "998364", "9983", "993", "9", "9"]
            },
            "Draw2": {
                "R2": ["59924413866", "59941386", "599138", "59913", "591", "591"],
                "R4": ["25996683441", "59968341", "599831", "59931", "591", "591"],
                "R6": ["66815993244", "68159934", "815993", "15993", "159", "159"],
                "R8": ["19983662445", "19983645", "199835", "19935", "195", "195"]
            }
            # ... Draw3 through Draw7 follow similar pattern
        }
    }
}
```

## 2. Generated Table Formats

### 2.1 Combined Table Format
This table shows all data types (DRAW_DATA, R2, R4, R6, R8) with right-aligned values:

| Set  | Draw  | RowType   | 7   | 6   | 5   | 4   | 3   | 2   | 1   |
|------|-------|-----------|-----|-----|-----|-----|-----|-----|-----|
| Set3 | Draw1 | DRAW_DATA | 934 | 916 | 319 | 917 | 723 | 753 | 832 |
| Set3 | Draw1 | R2        | N/A | 552 | 400 | 877 | 554 | 008 | 5400* |
| Set3 | Draw1 | R4        | N/A | 255 | 008 | 477 | 550 | 084 | 5004* |
| Set3 | Draw1 | R6        | N/A | 877 | 005 | 524 | 800 | 554 | 0054* |
| Set3 | Draw1 | R8        | N/A | 770 | 082 | 455 | 008 | 455 | 0045* |

### 2.2 R2-only Table Format
This table shows only R2 rows with custom slicing rules:

| Set  | Draw  | 7   | 6   | 5   | 4   | 3   | 2   | 1   |
|------|-------|-----|-----|-----|-----|-----|-----|-----|
| Set3 | Draw1 | N/A | N/A | N/A | N/A | 554 | 008 | 5400 |
| Set2 | Draw1 | N/A | N/A | N/A | N/A | 998 | 99  | 9    |
| Set1 | Draw1 | N/A | N/A | N/A | N/A | 993 | 9   | 9*   |
| Set1 | Draw2 | N/A | N/A | N/A | N/A | N/A | 591 | 591* |

## 3. Key Rules and Patterns

### 3.1 Hot Zone Rules (Set1 only)
- Draw1: Last 5 items marked with *
- Draw2: Last 5 items marked with *
- Draw3: Last 5 items marked with *
- Draw4: Last 4 items marked with *
- Draw5: Last 2 items marked with *
- Draw6-7: No hot zones

### 3.2 R2 Slicing Rules
- Set3/Set2 Draw1: First 3 items
- Set1 Draw1: First 3 items
- Set1 Draw2: First 2 items
- Set1 Draw3-7: First 1 item

### 3.3 Data Alignment Rules
- All numeric data is right-aligned
- Empty spaces are filled with "N/A"
- Maximum 7 columns of data (7,6,5,4,3,2,1)
- Hot zones are marked with * suffix

## 4. Sample Code to Generate Tables

```python
from scripts.utils.table_generator import build_section_table, build_r2_only_table

# Load your data
section_data = sample_data["Midday"]

# Generate tables
combined_table = build_section_table(section_data)
r2_table = build_r2_only_table(section_data)

# Print or export tables
print(combined_table.to_markdown(tablefmt="grid", index=False))
print(r2_table.to_markdown(tablefmt="grid", index=False)) 

