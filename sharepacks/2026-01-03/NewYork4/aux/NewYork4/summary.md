# Aux Summary — NewYork4 — 2026-01-03

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-03/NewYork4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-02.xlsm` | aux_state_label: New York
- combined: live=`data/cleaned/draws/New_York_draws.csv` snap=`sharepacks/2026-01-03/NewYork4/aux/draws/New_York_draws.csv` n=1000 head=256, 998, 174, 117, 116
- midday: live=`data/cleaned/draws/New_York_Midday_draws.csv` snap=`sharepacks/2026-01-03/NewYork4/aux/draws/New_York_Midday_draws.csv` n=1000 head=998, 117, 419, 051, 321
- evening: live=`data/cleaned/draws/New_York_Evening_draws.csv` snap=`sharepacks/2026-01-03/NewYork4/aux/draws/New_York_Evening_draws.csv` n=1000 head=256, 174, 116, 132, 195

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=7 streak=1 max=2 last_repeat_gap=25 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=21), P2:4 (gap=26), P3:0 (gap=12)
- consensus_notes: P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P1 mirror cluster around digit 1 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 640: score=34.25302142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 540: score=34.065378571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 600: score=33.74032142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 500: score=33.55267857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 646: score=30.66942142857143 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R3 src=cartesian
- 747: score=30.459722142857142 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 606: score=30.15672142857143 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 707: score=29.947022142857143 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 647: score=29.735092857142856 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R3 src=cartesian
- 547: score=29.54745 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R3 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 244: ds=984 sev=B
- 699: ds=927 sev=B
- 115: ds=845 sev=B
- 222: ds=781 sev=B
- 339: ds=762 sev=B
- 136: ds=753 sev=B
- 000: ds=752 sev=B
- 177: ds=746 sev=B
- 667: ds=714 sev=B
- 777: ds=708 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=55 sev=purple
  - 77: ds=41 sev=purple
  - 55: ds=40 sev=purple
  - 22: ds=36 sev=purple
  - 66: ds=16 sev=-
  - 44: ds=15 sev=-
  - 00: ds=12 sev=-
  - 33: ds=10 sev=-
  - 11: ds=3 sev=-
  - 99: ds=1 sev=-
- non_repeating:
  - 67: ds=67 sev=red
  - 06: ds=64 sev=red
  - 69: ds=60 sev=red
  - 36: ds=56 sev=red
  - 68: ds=42 sev=blue
  - 07: ds=41 sev=blue
  - 34: ds=37 sev=blue
  - 27: ds=34 sev=purple
  - 18: ds=31 sev=purple
  - 79: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 18:214, 35:202, 26:118, 32:103, 28:72, 5:66, 23:56, 31:51, 10:41, 3:40

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 18:ds=214 fs=12 fl=3 hz=0.0199203187250996, 35:ds=202 fs=4 fl=3 hz=0.009138381201044387, 26:ds=118 fs=2 fl=1 hz=0.007173601147776184, 32:ds=103 fs=7 fl=3 hz=0.012515644555694618, 28:ds=72 fs=16 fl=3 hz=0.021788990825688075, 5:ds=66 fs=15 fl=3 hz=0.01973684210526316, 23:ds=56 fs=23 fl=2 hz=0.02910360884749709, 31:ds=51 fs=21 fl=1 hz=0.023579849946409433, 10:ds=41 fs=23 fl=1 hz=0.027809965237543453, 3:ds=40 fs=15 fl=2 hz=0.021660649819494587

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S25: ds=80 flags=purple
- S22: ds=78 flags=purple
- S7: ds=68 flags=purple
- S23: ds=55 flags=purple
- S3: ds=45 flags=purple
- S10: ds=36 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '3'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=34 streak=1 max=2 last_repeat_gap=17 last_repeat_index=14

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:6 (gap=30), P2:4 (gap=26), P3:6 (gap=23)
- consensus_notes: P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P1 mirror cluster around digit 1 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 640: score=34.25302142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 540: score=34.065378571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 600: score=33.74032142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 500: score=33.55267857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 646: score=30.66942142857143 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R3 src=cartesian
- 747: score=30.459722142857142 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 606: score=30.15672142857143 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 707: score=29.947022142857143 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 647: score=29.735092857142856 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R3 src=cartesian
- 547: score=29.54745 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R3 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 001: ds=997 sev=B
- 337: ds=830 sev=B
- 366: ds=823 sev=B
- 044: ds=801 sev=B
- 667: ds=779 sev=B
- 189: ds=765 sev=B
- 449: ds=761 sev=B
- 456: ds=732 sev=B
- 223: ds=725 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 66: ds=115 sev=red
  - 55: ds=45 sev=purple
  - 33: ds=43 sev=purple
  - 88: ds=27 sev=purple
  - 00: ds=22 sev=-
  - 22: ds=21 sev=-
  - 77: ds=20 sev=-
  - 44: ds=7 sev=-
  - 11: ds=1 sev=-
  - 99: ds=0 sev=-
- non_repeating:
  - 27: ds=69 sev=red
  - 06: ds=55 sev=blue
  - 25: ds=54 sev=blue
  - 36: ds=39 sev=blue
  - 69: ds=38 sev=blue
  - 09: ds=35 sev=purple
  - 56: ds=33 sev=purple
  - 67: ds=33 sev=purple
  - 16: ds=30 sev=purple
  - 29: ds=25 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:369, 26:341, 16:264, 18:117, 22:100, 15:89, 23:82, 27:75, 1:71, 28:68

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=369 fs=1 fl=1 hz=0.005145797598627787, 26:ds=341 fs=1 fl=0 hz=0.004081632653061225, 16:ds=264 fs=3 fl=0 hz=0.005471956224350205, 18:ds=117 fs=16 fl=2 hz=0.020524515393386546, 22:ds=100 fs=42 fl=0 hz=0.04713804713804714, 15:ds=89 fs=17 fl=2 hz=0.02134831460674157, 23:ds=82 fs=24 fl=1 hz=0.02860411899313501, 27:ds=75 fs=12 fl=2 hz=0.01728110599078341, 1:ds=71 fs=3 fl=2 hz=0.008075370121130552, 28:ds=68 fs=21 fl=2 hz=0.0257847533632287

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S8: ds=86 flags=red+purple
- S25: ds=62 flags=blue+purple
- S10: ds=54 flags=purple
- S7: ds=49 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 016: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 036: score=1 tags=FLT
  - 046: score=1 tags=FLT
  - 056: score=1 tags=FLT
  - 067: score=1 tags=FLT
  - 068: score=1 tags=FLT
  - 069: score=1 tags=FLT
  - 126: score=1 tags=FLT
  - 136: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=7 streak=1 max=2 last_repeat_gap=32 last_repeat_index=7

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:4 (gap=24), P2:8 (gap=38), P3:7 (gap=40)
- consensus_notes: P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P1 mirror cluster around digit 1 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 5 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P3:7 (ds=40)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 640: score=34.25302142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 540: score=34.065378571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 600: score=33.74032142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 500: score=33.55267857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 646: score=30.66942142857143 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R3 src=cartesian
- 747: score=30.459722142857142 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 606: score=30.15672142857143 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 707: score=29.947022142857143 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 647: score=29.735092857142856 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R3 src=cartesian
- 547: score=29.54745 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R3 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 566: ds=976 sev=B
- 668: ds=856 sev=B
- 248: ds=850 sev=B
- 014: ds=830 sev=B
- 222: ds=814 sev=B
- 001: ds=795 sev=B
- 999: ds=785 sev=B
- 444: ds=784 sev=B
- 156: ds=759 sev=B
- 133: ds=707 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 77: ds=126 sev=red
  - 44: ds=50 sev=purple
  - 99: ds=40 sev=purple
  - 88: ds=37 sev=purple
  - 55: ds=20 sev=-
  - 22: ds=18 sev=-
  - 66: ds=8 sev=-
  - 00: ds=6 sev=-
  - 33: ds=5 sev=-
  - 11: ds=2 sev=-
- non_repeating:
  - 48: ds=96 sev=red
  - 07: ds=85 sev=red
  - 03: ds=62 sev=red
  - 39: ds=43 sev=blue
  - 67: ds=39 sev=blue
  - 06: ds=32 sev=purple
  - 46: ds=30 sev=purple
  - 69: ds=30 sev=purple
  - 36: ds=28 sev=purple
  - 38: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 18:107, 34:106, 35:101, 32:84, 33:77, 10:67, 17:65, 26:59, 4:51, 2:46

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 18:ds=107 fs=14 fl=1 hz=0.01884570082449941, 34:ds=106 fs=19 fl=0 hz=0.02242152466367713, 35:ds=101 fs=5 fl=2 hz=0.00963855421686747, 32:ds=84 fs=9 fl=1 hz=0.013095238095238096, 33:ds=77 fs=16 fl=2 hz=0.022113022113022112, 10:ds=67 fs=27 fl=1 hz=0.030335861321776812, 17:ds=65 fs=31 fl=1 hz=0.034408602150537634, 26:ds=59 fs=3 fl=4 hz=0.008879023307436182, 4:ds=51 fs=23 fl=1 hz=0.026200873362445417, 2:ds=46 fs=28 fl=1 hz=0.03456495828367104

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S9: ds=67 flags=purple
- S3: ds=52 flags=purple
- S16: ds=45 flags=purple
- S25: ds=40 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [7], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 016: score=3 tags=FLT,RS
  - 025: score=3 tags=FLT,RS
  - 034: score=3 tags=FLT,RS
  - 079: score=3 tags=FLT,RS
  - 178: score=3 tags=FLT,RS
  - 268: score=3 tags=FLT,RS
  - 358: score=3 tags=FLT,RS
  - 124: score=2 tags=RS
  - 169: score=2 tags=RS
  - 259: score=2 tags=RS

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 001 -> evening:795(B); midday:997(B)
- 222 -> combined:781(B); evening:814(B)
- 667 -> combined:714(B); midday:779(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 06 -> combined:64(red); evening:32(purple); midday:55(blue)
- 07 -> combined:41(blue); evening:85(red)
- 09 -> combined:26(purple); midday:35(purple)
- 27 -> combined:34(purple); midday:69(red)
- 34 -> combined:37(blue); evening:25(purple)
- 36 -> combined:56(red); evening:28(purple); midday:39(blue)
- 55 -> combined:40(purple); midday:45(purple)
- 67 -> combined:67(red); evening:39(blue); midday:33(purple)
- 69 -> combined:60(red); evening:30(purple); midday:38(blue)
- 77 -> combined:41(purple); evening:126(red)
- 88 -> combined:55(purple); evening:37(purple); midday:27(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 6(3.022)[R3,XVAR-Cons(CM)], 5(2.834357142857143)[R1,XVAR-Cons(CM)], 7(2.502407142857143)[R2,XVAR-Cons(CE)], 4(1.4165714285714284)[R1,Double-Pressure], 8(1.0971)[R2,Double-Pressure]
- P2: 4(7.068092857142857)[R1,XVAR-Cons(CEM)], 0(6.555392857142857)[R2,XVAR-Cons(CEM)], 8(3.355428571428571)[R3,XVAR-Cons(CE)], 3(1.0971)[R2,Double-Pressure]
- P3: 0(2.662928571428571)[R1,Mirror-Echo], 7(1.645)[R1,Double-Pressure], 6(1.2867142857142857)[R1,Double-Pressure], 9(1.2134)[R2,Double-Pressure], 3(0.9199999999999999)[R2,Double-Pressure]
