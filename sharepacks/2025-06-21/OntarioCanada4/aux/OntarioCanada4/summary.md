# Aux Summary — OntarioCanada4 — 2025-06-21

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-21/OntarioCanada4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_06_20.xlsm` | aux_state_label: Ontario
- combined: live=`data/cleaned/draws/Ontario_draws.csv` snap=`sharepacks/2025-06-21/OntarioCanada4/aux/draws/Ontario_draws.csv` n=1000 head=343, 211, 367, 221, 875
- midday: live=`data/cleaned/draws/Ontario_Midday_draws.csv` snap=`sharepacks/2025-06-21/OntarioCanada4/aux/draws/Ontario_Midday_draws.csv` n=1000 head=211, 221, 847, 805, 890
- evening: live=`data/cleaned/draws/Ontario_Evening_draws.csv` snap=`sharepacks/2025-06-21/OntarioCanada4/aux/draws/Ontario_Evening_draws.csv` n=1000 head=343, 367, 875, 896, 807

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=33 streak=1 max=3 last_repeat_gap=37 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:9 (gap=23), P2:8 (gap=28), P3:2 (gap=34)
- consensus_notes: P1 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 4 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 952: score=48.025181428571436 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 959: score=44.92263035714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 982: score=43.93134821428572 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 989: score=40.82879714285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 932: score=40.82176428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 752: score=40.396792857142856 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 954: score=39.21474535714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 939: score=38.29869 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 782: score=36.641285714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 732: score=36.13144285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 044: ds=998 sev=B
- 004: ds=833 sev=B
- 288: ds=826 sev=B
- 778: ds=807 sev=B
- 115: ds=800 sev=B
- 144: ds=791 sev=B
- 055: ds=769 sev=B
- 346: ds=743 sev=B
- 255: ds=726 sev=B
- 111: ds=716 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=119 sev=red
  - 00: ds=91 sev=blue
  - 55: ds=72 sev=blue
  - 66: ds=56 sev=purple
  - 77: ds=42 sev=purple
  - 99: ds=23 sev=-
  - 44: ds=17 sev=-
  - 22: ds=3 sev=-
  - 11: ds=1 sev=-
  - 33: ds=0 sev=-
- non_repeating:
  - 35: ds=63 sev=red
  - 59: ds=54 sev=blue
  - 26: ds=45 sev=blue
  - 24: ds=44 sev=blue
  - 25: ds=41 sev=blue
  - 79: ds=35 sev=purple
  - 27: ds=30 sev=purple
  - 39: ds=25 sev=purple
  - 02: ds=24 sev=-
  - 29: ds=23 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:687, 1:283, 6:115, 26:114, 13:108, 5:80, 16:64, 34:58, 28:57, 3:41

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=687 fs=0 fl=0 hz=0.0, 1:ds=283 fs=1 fl=1 hz=0.006172839506172839, 6:ds=115 fs=10 fl=4 hz=0.016726403823178016, 26:ds=114 fs=3 fl=2 hz=0.008174386920980927, 13:ds=108 fs=22 fl=0 hz=0.02631578947368421, 5:ds=80 fs=28 fl=0 hz=0.03571428571428571, 16:ds=64 fs=2 fl=0 hz=0.005605381165919282, 34:ds=58 fs=12 fl=4 hz=0.017185821697099892, 28:ds=57 fs=17 fl=2 hz=0.020255863539445626, 3:ds=41 fs=20 fl=1 hz=0.022629310344827586

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S21: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S1: ds=94 flags=blue+purple
- S22: ds=54 flags=purple
- S6: ds=50 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '9'], 'pairs': {'remaining_count': 0}}
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
- current_index=17 streak=1 max=2 last_repeat_gap=19 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:6 (gap=22), P2:7 (gap=28), P3:6 (gap=24)
- consensus_notes: P1 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 4 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 952: score=48.025181428571436 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 959: score=44.92263035714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 982: score=43.93134821428572 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 989: score=40.82879714285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 932: score=40.82176428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 752: score=40.396792857142856 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 954: score=39.21474535714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 939: score=38.29869 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 782: score=36.641285714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 732: score=36.13144285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 288: ds=953 sev=B
- 099: ds=903 sev=B
- 228: ds=800 sev=B
- 333: ds=783 sev=B
- 255: ds=750 sev=B
- 566: ds=726 sev=B
- 338: ds=720 sev=B
- 355: ds=715 sev=B
- 011: ds=693 sev=B
- 368: ds=681 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=107 sev=red
  - 88: ds=59 sev=purple
  - 66: ds=57 sev=purple
  - 00: ds=45 sev=purple
  - 55: ds=41 sev=purple
  - 77: ds=28 sev=purple
  - 99: ds=11 sev=-
  - 44: ds=8 sev=-
  - 22: ds=1 sev=-
  - 11: ds=0 sev=-
- non_repeating:
  - 17: ds=46 sev=blue
  - 57: ds=44 sev=blue
  - 67: ds=44 sev=blue
  - 59: ds=41 sev=blue
  - 37: ds=38 sev=blue
  - 16: ds=34 sev=purple
  - 34: ds=32 sev=purple
  - 23: ds=31 sev=purple
  - 35: ds=31 sev=purple
  - 27: ds=30 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:343, 21:189, 16:185, 1:141, 34:126, 27:102, 26:89, 10:71, 33:62, 13:59

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=343 fs=1 fl=2 hz=0.006097560975609756, 21:ds=189 fs=42 fl=0 hz=0.05296343001261034, 16:ds=185 fs=4 fl=0 hz=0.008450704225352114, 1:ds=141 fs=4 fl=2 hz=0.011976047904191617, 34:ds=126 fs=13 fl=3 hz=0.01909307875894988, 27:ds=102 fs=16 fl=2 hz=0.020202020202020204, 26:ds=89 fs=0 fl=4 hz=0.006150061500615006, 10:ds=71 fs=22 fl=1 hz=0.02561247216035635, 33:ds=62 fs=22 fl=1 hz=0.026047565118912798, 13:ds=59 fs=21 fl=3 hz=0.026402640264026403

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S21: ds=100 flags=red+purple
- S22: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S1: ds=94 flags=blue+purple
- S3: ds=86 flags=purple
- S6: ds=73 flags=purple
- S2: ds=69 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [6], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['3', '6'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 069: score=3 tags=FLT,RS
  - 123: score=3 tags=FLT,RS
  - 168: score=3 tags=FLT,RS
  - 267: score=3 tags=FLT,RS
  - 348: score=3 tags=FLT,RS
  - 357: score=3 tags=FLT,RS
  - 456: score=3 tags=FLT,RS
  - 015: score=2 tags=RS
  - 024: score=2 tags=RS
  - 078: score=2 tags=RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=33 streak=1 max=3 last_repeat_gap=23 last_repeat_index=31

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=27), P2:3 (gap=28), P3:9 (gap=23)
- consensus_notes: P1 digit 9 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 4 (Mirror-Echo(CEM)), P1 mirror cluster around digit 2 (Mirror-Echo(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CE)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 952: score=48.025181428571436 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 959: score=44.92263035714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 982: score=43.93134821428572 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 989: score=40.82879714285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 932: score=40.82176428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 752: score=40.396792857142856 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian
- 954: score=39.21474535714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 939: score=38.29869 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 782: score=36.641285714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 732: score=36.13144285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 778: ds=984 sev=B
- 228: ds=930 sev=B
- 337: ds=897 sev=B
- 145: ds=852 sev=B
- 016: ds=833 sev=B
- 066: ds=830 sev=B
- 777: ds=818 sev=B
- 388: ds=804 sev=B
- 588: ds=771 sev=B
- 227: ds=719 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=88 sev=blue
  - 11: ds=49 sev=purple
  - 00: ds=47 sev=purple
  - 55: ds=36 sev=purple
  - 66: ds=28 sev=purple
  - 22: ds=26 sev=purple
  - 99: ds=23 sev=-
  - 77: ds=21 sev=-
  - 44: ds=13 sev=-
  - 33: ds=0 sev=-
- non_repeating:
  - 12: ds=106 sev=red
  - 26: ds=66 sev=red
  - 35: ds=36 sev=purple
  - 06: ds=33 sev=purple
  - 03: ds=31 sev=purple
  - 39: ds=29 sev=purple
  - 59: ds=27 sev=purple
  - 25: ds=26 sev=purple
  - 05: ds=25 sev=purple
  - 15: ds=25 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:674, 35:232, 6:195, 28:167, 1:147, 20:117, 3:114, 17:100, 26:57, 13:54

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=674 fs=1 fl=2 hz=0.009433962264150943, 35:ds=232 fs=0 fl=3 hz=0.005657708628005658, 6:ds=195 fs=14 fl=2 hz=0.02077922077922078, 28:ds=167 fs=7 fl=0 hz=0.011335012594458438, 1:ds=147 fs=0 fl=0 hz=0.0, 20:ds=117 fs=18 fl=1 hz=0.02280912364945978, 3:ds=114 fs=16 fl=3 hz=0.023199023199023196, 17:ds=100 fs=17 fl=3 hz=0.022753128555176336, 26:ds=57 fs=3 fl=2 hz=0.007552870090634441, 13:ds=54 fs=23 fl=2 hz=0.02969121140142518

### Sums (source: aux_validation.sums_stats_by_variant)
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S4: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S21: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S25: ds=88 flags=purple
- S27: ds=78 flags=blue+purple
- S19: ds=76 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '2'], 'pairs': {'remaining_count': 1}}
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
- 228 -> evening:930(B); midday:800(B)
- 255 -> combined:726(B); midday:750(B)
- 288 -> combined:826(B); midday:953(B)
- 338 -> evening:674(B); midday:720(B)
- 388 -> combined:687(B); evening:804(B)
- 778 -> combined:807(B); evening:984(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:91(blue); evening:47(purple); midday:45(purple)
- 24 -> combined:44(blue); midday:29(purple)
- 25 -> combined:41(blue); evening:26(purple)
- 26 -> combined:45(blue); evening:66(red)
- 27 -> combined:30(purple); midday:30(purple)
- 35 -> combined:63(red); evening:36(purple); midday:31(purple)
- 39 -> combined:25(purple); evening:29(purple)
- 55 -> combined:72(blue); evening:36(purple); midday:41(purple)
- 59 -> combined:54(blue); evening:27(purple); midday:41(blue)
- 66 -> combined:56(purple); evening:28(purple); midday:57(purple)
- 77 -> combined:42(purple); midday:28(purple)
- 88 -> combined:119(red); evening:88(blue); midday:59(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 9(5.585621428571429)[R1,XVAR-Cons(CEM)], 7(3.3952999999999998)[R2,XVAR-Cons(CM)], 1(2.7912142857142856)[R3,XVAR-Cons(CE)], 5(1.5061428571428572)[R1,Double-Pressure], 6(1.3268571428571427)[R1,Double-Pressure]
- P2: 5(6.256921428571429)[R2,XVAR-Cons(CEM)], 8(4.001414285714286)[R1,Mirror-Echo], 3(3.4915714285714285)[R3,Mirror-Echo], 7(1.536)[R1,Double-Pressure], 1(0.3552785714285714)[R3,Swap]
- P3: 2(7.7445714285714295)[R1,XVAR-Cons(CEM)], 9(3.881392857142857)[R2,Mirror-Echo], 4(2.2572357142857147)[R3,Mirror-Echo], 6(1.3865714285714286)[R1,Double-Pressure], 3(0.2612285714285714)[R3,Swap]
