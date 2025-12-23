# Aux Summary — OntarioCanada4 — 2025-06-22

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-22/OntarioCanada4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-06-21.xlsm` | aux_state_label: Ontario
- combined: live=`data/cleaned/draws/Ontario_draws.csv` snap=`sharepacks/2025-06-22/OntarioCanada4/aux/draws/Ontario_draws.csv` n=1000 head=517, 678, 343, 211, 367
- midday: live=`data/cleaned/draws/Ontario_Midday_draws.csv` snap=`sharepacks/2025-06-22/OntarioCanada4/aux/draws/Ontario_Midday_draws.csv` n=1000 head=678, 211, 221, 847, 805
- evening: live=`data/cleaned/draws/Ontario_Evening_draws.csv` snap=`sharepacks/2025-06-22/OntarioCanada4/aux/draws/Ontario_Evening_draws.csv` n=1000 head=517, 343, 367, 875, 896

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=7 streak=1 max=3 last_repeat_gap=39 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:9 (gap=25), P2:8 (gap=30), P3:2 (gap=36)
- consensus_notes: P1 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 4 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 952: score=51.414766428571426 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 982: score=50.91820464285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 959: score=49.00110142857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 989: score=48.50453964285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 152: score=45.835342857142855 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 182: score=45.40355 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 932: score=44.61375821428571 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 954: score=42.76770428571429 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 984: score=42.271142499999996 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 939: score=42.200093214285715 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane

### Doubles (source: aux_validation.collect_variant_stats)
- 004: ds=835 sev=B
- 288: ds=828 sev=B
- 778: ds=809 sev=B
- 115: ds=802 sev=B
- 144: ds=793 sev=B
- 055: ds=771 sev=B
- 346: ds=745 sev=B
- 255: ds=728 sev=B
- 111: ds=718 sev=B
- 116: ds=698 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=121 sev=red
  - 00: ds=93 sev=blue
  - 55: ds=74 sev=blue
  - 66: ds=58 sev=purple
  - 77: ds=44 sev=purple
  - 99: ds=25 sev=purple
  - 44: ds=19 sev=-
  - 22: ds=5 sev=-
  - 11: ds=3 sev=-
  - 33: ds=2 sev=-
- non_repeating:
  - 35: ds=65 sev=red
  - 59: ds=56 sev=red
  - 26: ds=47 sev=blue
  - 24: ds=46 sev=blue
  - 25: ds=43 sev=blue
  - 79: ds=37 sev=blue
  - 27: ds=32 sev=purple
  - 39: ds=27 sev=purple
  - 02: ds=26 sev=purple
  - 29: ds=25 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:689, 1:285, 6:117, 26:116, 13:110, 5:82, 16:66, 34:60, 28:59, 3:43

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=689 fs=0 fl=0 hz=0.0, 1:ds=285 fs=1 fl=1 hz=0.006172839506172839, 6:ds=117 fs=10 fl=4 hz=0.016726403823178016, 26:ds=116 fs=3 fl=2 hz=0.008174386920980927, 13:ds=110 fs=22 fl=0 hz=0.02631578947368421, 5:ds=82 fs=28 fl=0 hz=0.03571428571428571, 16:ds=66 fs=2 fl=0 hz=0.005605381165919282, 34:ds=60 fs=12 fl=4 hz=0.017185821697099892, 28:ds=59 fs=17 fl=2 hz=0.020255863539445626, 3:ds=43 fs=20 fl=1 hz=0.022629310344827586

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S1: ds=96 flags=blue+purple
- S22: ds=56 flags=purple
- S6: ds=52 flags=red+purple
- S7: ds=43 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': True}, 'floating': ['0', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 015: score=2 tags=FLT,PAT
  - 016: score=2 tags=FLT,PAT
  - 017: score=2 tags=FLT,PAT
  - 018: score=2 tags=FLT,PAT
  - 019: score=2 tags=FLT,PAT
  - 025: score=2 tags=FLT,PAT
  - 026: score=2 tags=FLT,PAT
  - 027: score=2 tags=FLT,PAT
  - 028: score=2 tags=FLT,PAT
  - 029: score=2 tags=FLT,PAT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=21 streak=1 max=2 last_repeat_gap=20 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=18), P2:8 (gap=24), P3:6 (gap=25)
- consensus_notes: P1 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 4 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 952: score=51.414766428571426 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 982: score=50.91820464285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 959: score=49.00110142857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 989: score=48.50453964285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 152: score=45.835342857142855 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 182: score=45.40355 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 932: score=44.61375821428571 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 954: score=42.76770428571429 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 984: score=42.271142499999996 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 939: score=42.200093214285715 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane

### Doubles (source: aux_validation.collect_variant_stats)
- 288: ds=954 sev=B
- 099: ds=904 sev=B
- 228: ds=801 sev=B
- 333: ds=784 sev=B
- 255: ds=751 sev=B
- 566: ds=727 sev=B
- 338: ds=721 sev=B
- 355: ds=716 sev=B
- 011: ds=694 sev=B
- 368: ds=682 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=108 sev=red
  - 88: ds=60 sev=purple
  - 66: ds=58 sev=purple
  - 00: ds=46 sev=purple
  - 55: ds=42 sev=purple
  - 77: ds=29 sev=purple
  - 99: ds=12 sev=-
  - 44: ds=9 sev=-
  - 22: ds=2 sev=-
  - 11: ds=1 sev=-
- non_repeating:
  - 17: ds=47 sev=blue
  - 57: ds=45 sev=blue
  - 59: ds=42 sev=blue
  - 37: ds=39 sev=blue
  - 16: ds=35 sev=purple
  - 34: ds=33 sev=purple
  - 23: ds=32 sev=purple
  - 35: ds=32 sev=purple
  - 27: ds=31 sev=purple
  - 24: ds=30 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:344, 16:186, 1:142, 34:127, 27:103, 26:90, 10:72, 33:63, 13:60, 6:58

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=344 fs=1 fl=1 hz=0.0056603773584905665, 16:ds=186 fs=4 fl=0 hz=0.008450704225352114, 1:ds=142 fs=4 fl=2 hz=0.011976047904191617, 34:ds=127 fs=13 fl=3 hz=0.01909307875894988, 27:ds=103 fs=16 fl=2 hz=0.020202020202020204, 26:ds=90 fs=0 fl=4 hz=0.006150061500615006, 10:ds=72 fs=22 fl=1 hz=0.02561247216035635, 33:ds=63 fs=22 fl=1 hz=0.026047565118912798, 13:ds=60 fs=21 fl=3 hz=0.026402640264026403, 6:ds=58 fs=18 fl=1 hz=0.02065217391304348

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S22: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S1: ds=95 flags=blue+purple
- S3: ds=87 flags=purple
- S6: ds=74 flags=purple
- S2: ds=70 flags=purple
- S9: ds=46 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [6], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['3', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 069: score=3 tags=FLT,RS
  - 123: score=3 tags=FLT,RS
  - 159: score=3 tags=FLT,RS
  - 249: score=3 tags=FLT,RS
  - 348: score=3 tags=FLT,RS
  - 357: score=3 tags=FLT,RS
  - 789: score=3 tags=FLT,RS
  - 015: score=2 tags=RS
  - 024: score=2 tags=RS
  - 078: score=2 tags=RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=7 streak=1 max=3 last_repeat_gap=24 last_repeat_index=31

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=26), P2:3 (gap=29), P3:9 (gap=24)
- consensus_notes: P1 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 4 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 952: score=51.414766428571426 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 982: score=50.91820464285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 959: score=49.00110142857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 989: score=48.50453964285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 152: score=45.835342857142855 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 182: score=45.40355 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 932: score=44.61375821428571 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 954: score=42.76770428571429 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 984: score=42.271142499999996 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 939: score=42.200093214285715 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane

### Doubles (source: aux_validation.collect_variant_stats)
- 778: ds=985 sev=B
- 228: ds=931 sev=B
- 337: ds=898 sev=B
- 145: ds=853 sev=B
- 016: ds=834 sev=B
- 066: ds=831 sev=B
- 777: ds=819 sev=B
- 388: ds=805 sev=B
- 588: ds=772 sev=B
- 227: ds=720 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=89 sev=blue
  - 11: ds=50 sev=purple
  - 00: ds=48 sev=purple
  - 55: ds=37 sev=purple
  - 66: ds=29 sev=purple
  - 22: ds=27 sev=purple
  - 99: ds=24 sev=-
  - 77: ds=22 sev=-
  - 44: ds=14 sev=-
  - 33: ds=1 sev=-
- non_repeating:
  - 12: ds=107 sev=red
  - 26: ds=67 sev=red
  - 35: ds=37 sev=blue
  - 06: ds=34 sev=purple
  - 03: ds=32 sev=purple
  - 39: ds=30 sev=purple
  - 59: ds=28 sev=purple
  - 25: ds=27 sev=purple
  - 05: ds=26 sev=purple
  - 79: ds=25 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:675, 35:233, 6:196, 28:168, 1:148, 20:118, 3:115, 17:101, 26:58, 13:55

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=675 fs=1 fl=2 hz=0.009433962264150943, 35:ds=233 fs=0 fl=3 hz=0.005657708628005658, 6:ds=196 fs=14 fl=2 hz=0.02077922077922078, 28:ds=168 fs=7 fl=0 hz=0.011335012594458438, 1:ds=148 fs=0 fl=0 hz=0.0, 20:ds=118 fs=18 fl=1 hz=0.02280912364945978, 3:ds=115 fs=16 fl=3 hz=0.023199023199023196, 17:ds=101 fs=17 fl=3 hz=0.022753128555176336, 26:ds=58 fs=3 fl=2 hz=0.007552870090634441, 13:ds=55 fs=23 fl=2 hz=0.02969121140142518

### Sums (source: aux_validation.sums_stats_by_variant)
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S4: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S21: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S25: ds=89 flags=purple
- S27: ds=79 flags=blue+purple
- S19: ds=77 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '2'], 'pairs': {'remaining_count': 1}}
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

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 228 -> evening:931(B); midday:801(B)
- 255 -> combined:728(B); midday:751(B)
- 288 -> combined:828(B); midday:954(B)
- 338 -> evening:675(B); midday:721(B)
- 388 -> combined:689(B); evening:805(B)
- 778 -> combined:809(B); evening:985(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:93(blue); evening:48(purple); midday:46(purple)
- 24 -> combined:46(blue); midday:30(purple)
- 25 -> combined:43(blue); evening:27(purple)
- 26 -> combined:47(blue); evening:67(red)
- 27 -> combined:32(purple); midday:31(purple)
- 35 -> combined:65(red); evening:37(blue); midday:32(purple)
- 39 -> combined:27(purple); evening:30(purple)
- 55 -> combined:74(blue); evening:37(purple); midday:42(purple)
- 59 -> combined:56(red); evening:28(purple); midday:42(blue)
- 66 -> combined:58(purple); evening:29(purple); midday:58(purple)
- 77 -> combined:44(purple); midday:29(purple)
- 79 -> combined:37(blue); evening:25(purple)
- 88 -> combined:121(red); evening:89(blue); midday:60(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 9(7.177314285714285)[R1,XVAR-Cons(CEM)], 1(5.847642857142858)[R3,XVAR-Cons(CEM)], 7(3.5214285714285714)[R2,XVAR-Cons(CM)], 4(0.34959999999999997)[R3,Mirror-Echo]
- P2: 5(6.809900000000001)[R2,XVAR-Cons(CEM)], 8(6.378107142857143)[R1,Mirror-Echo], 3(3.0698928571428574)[R3,Mirror-Echo], 6(0.1774857142857143)[R3,Swap]
- P3: 2(7.6777999999999995)[R1,XVAR-Cons(CEM)], 9(3.9742142857142855)[R2,Mirror-Echo], 4(2.3325285714285715)[R3,Mirror-Echo], 6(1.3464285714285715)[R1,Double-Pressure], 3(0.2746642857142857)[R3,Swap]
