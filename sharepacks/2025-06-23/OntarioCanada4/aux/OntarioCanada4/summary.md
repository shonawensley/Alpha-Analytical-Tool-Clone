# Aux Summary — OntarioCanada4 — 2025-06-23

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-23/OntarioCanada4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-06-22.xlsm` | aux_state_label: Ontario
- combined: live=`data/cleaned/draws/Ontario_draws.csv` snap=`sharepacks/2025-06-23/OntarioCanada4/aux/draws/Ontario_draws.csv` n=1000 head=616, 918, 517, 678, 343
- midday: live=`data/cleaned/draws/Ontario_Midday_draws.csv` snap=`sharepacks/2025-06-23/OntarioCanada4/aux/draws/Ontario_Midday_draws.csv` n=1000 head=918, 678, 211, 221, 847
- evening: live=`data/cleaned/draws/Ontario_Evening_draws.csv` snap=`sharepacks/2025-06-23/OntarioCanada4/aux/draws/Ontario_Evening_draws.csv` n=1000 head=616, 517, 343, 367, 875

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=16 streak=1 max=3 last_repeat_gap=41 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=24), P2:8 (gap=32), P3:2 (gap=38)
- consensus_notes: P1 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 2 (Mirror-Echo(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 152: score=50.79694428571428 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 182: score=50.35417785714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 159: score=45.09649535714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 452: score=44.81919285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 189: score=44.653728928571425 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 482: score=44.434178571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 132: score=44.00401071428571 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 154: score=42.18839892857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 184: score=41.7456325 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 752: score=41.43687142857143 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 004: ds=837 sev=B
- 288: ds=830 sev=B
- 778: ds=811 sev=B
- 115: ds=804 sev=B
- 144: ds=795 sev=B
- 055: ds=773 sev=B
- 346: ds=747 sev=B
- 255: ds=730 sev=B
- 111: ds=720 sev=B
- 116: ds=700 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=123 sev=red
  - 00: ds=95 sev=blue
  - 55: ds=76 sev=blue
  - 77: ds=46 sev=purple
  - 99: ds=27 sev=purple
  - 44: ds=21 sev=-
  - 22: ds=7 sev=-
  - 11: ds=5 sev=-
  - 33: ds=4 sev=-
  - 66: ds=0 sev=-
- non_repeating:
  - 35: ds=67 sev=red
  - 59: ds=58 sev=red
  - 26: ds=49 sev=blue
  - 24: ds=48 sev=blue
  - 25: ds=45 sev=blue
  - 79: ds=39 sev=blue
  - 27: ds=34 sev=purple
  - 39: ds=29 sev=purple
  - 02: ds=28 sev=purple
  - 29: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:691, 1:287, 6:119, 26:118, 13:112, 5:84, 34:62, 28:61, 3:45, 10:38

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=691 fs=0 fl=0 hz=0.0, 1:ds=287 fs=1 fl=1 hz=0.006172839506172839, 6:ds=119 fs=10 fl=4 hz=0.016726403823178016, 26:ds=118 fs=3 fl=2 hz=0.008174386920980927, 13:ds=112 fs=22 fl=0 hz=0.02631578947368421, 5:ds=84 fs=28 fl=0 hz=0.03571428571428571, 34:ds=62 fs=12 fl=4 hz=0.017185821697099892, 28:ds=61 fs=17 fl=2 hz=0.020255863539445626, 3:ds=45 fs=20 fl=1 hz=0.022629310344827586, 10:ds=38 fs=24 fl=2 hz=0.02774813233724653

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S1: ds=98 flags=blue+purple
- S22: ds=58 flags=purple
- S6: ds=54 flags=red+purple
- S7: ds=45 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=3 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': True}, 'floating': ['0', '2'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 015: score=3 tags=FLT,MIR,PAT
  - 016: score=3 tags=FLT,MIR,PAT
  - 025: score=3 tags=FLT,MIR,PAT
  - 027: score=3 tags=FLT,MIR,PAT
  - 035: score=3 tags=FLT,MIR,PAT
  - 038: score=3 tags=FLT,MIR,PAT
  - 045: score=3 tags=FLT,MIR,PAT
  - 049: score=3 tags=FLT,MIR,PAT
  - 126: score=3 tags=FLT,MIR,PAT
  - 127: score=3 tags=FLT,MIR,PAT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=24 streak=1 max=2 last_repeat_gap=21 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=19), P2:8 (gap=25), P3:6 (gap=26)
- consensus_notes: P1 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 2 (Mirror-Echo(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 152: score=50.79694428571428 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 182: score=50.35417785714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 159: score=45.09649535714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 452: score=44.81919285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 189: score=44.653728928571425 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 482: score=44.434178571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 132: score=44.00401071428571 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 154: score=42.18839892857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 184: score=41.7456325 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 752: score=41.43687142857143 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 288: ds=955 sev=B
- 099: ds=905 sev=B
- 228: ds=802 sev=B
- 333: ds=785 sev=B
- 255: ds=752 sev=B
- 566: ds=728 sev=B
- 338: ds=722 sev=B
- 355: ds=717 sev=B
- 011: ds=695 sev=B
- 368: ds=683 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=109 sev=red
  - 88: ds=61 sev=purple
  - 66: ds=59 sev=purple
  - 00: ds=47 sev=purple
  - 55: ds=43 sev=purple
  - 77: ds=30 sev=purple
  - 99: ds=13 sev=-
  - 44: ds=10 sev=-
  - 22: ds=3 sev=-
  - 11: ds=2 sev=-
- non_repeating:
  - 17: ds=48 sev=blue
  - 57: ds=46 sev=blue
  - 59: ds=43 sev=blue
  - 37: ds=40 sev=blue
  - 16: ds=36 sev=purple
  - 34: ds=34 sev=purple
  - 23: ds=33 sev=purple
  - 35: ds=33 sev=purple
  - 27: ds=32 sev=purple
  - 24: ds=31 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:345, 16:187, 1:143, 34:128, 27:104, 26:91, 10:73, 33:64, 13:61, 6:59

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=345 fs=1 fl=1 hz=0.0056603773584905665, 16:ds=187 fs=4 fl=0 hz=0.008450704225352114, 1:ds=143 fs=4 fl=2 hz=0.011976047904191617, 34:ds=128 fs=13 fl=3 hz=0.01909307875894988, 27:ds=104 fs=16 fl=2 hz=0.020202020202020204, 26:ds=91 fs=0 fl=4 hz=0.006150061500615006, 10:ds=73 fs=22 fl=1 hz=0.02561247216035635, 33:ds=64 fs=22 fl=1 hz=0.026047565118912798, 13:ds=61 fs=21 fl=3 hz=0.026402640264026403, 6:ds=59 fs=18 fl=1 hz=0.02065217391304348

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S22: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S1: ds=96 flags=blue+purple
- S3: ds=88 flags=purple
- S6: ds=75 flags=red+purple
- S2: ds=71 flags=purple
- S9: ds=47 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [6], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '3', '5'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 015: score=3 tags=FLT,RS
  - 024: score=3 tags=FLT,RS
  - 069: score=3 tags=FLT,RS
  - 078: score=3 tags=FLT,RS
  - 123: score=3 tags=FLT,RS
  - 159: score=3 tags=FLT,RS
  - 258: score=3 tags=FLT,RS
  - 348: score=3 tags=FLT,RS
  - 357: score=3 tags=FLT,RS
  - 456: score=3 tags=FLT,RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=16 streak=1 max=3 last_repeat_gap=25 last_repeat_index=31

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=27), P2:3 (gap=30), P3:9 (gap=25)
- consensus_notes: P1 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 8 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 2 (Mirror-Echo(CM)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 3 (Mirror-Echo(CEM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CEM)), P3 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 152: score=50.79694428571428 tags=Double-Pressure,Lane-C,Mirror-Echo(CEM),R1,R2 src=lane
- 182: score=50.35417785714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 159: score=45.09649535714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 452: score=44.81919285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 189: score=44.653728928571425 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 482: score=44.434178571428575 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 132: score=44.00401071428571 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 154: score=42.18839892857143 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 184: score=41.7456325 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 752: score=41.43687142857143 tags=Double-Pressure,Mirror-Echo(CEM),Mirror-Echo(CM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 778: ds=986 sev=B
- 228: ds=932 sev=B
- 337: ds=899 sev=B
- 145: ds=854 sev=B
- 016: ds=835 sev=B
- 066: ds=832 sev=B
- 777: ds=820 sev=B
- 388: ds=806 sev=B
- 588: ds=773 sev=B
- 227: ds=721 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=90 sev=blue
  - 11: ds=51 sev=purple
  - 00: ds=49 sev=purple
  - 55: ds=38 sev=purple
  - 22: ds=28 sev=purple
  - 99: ds=25 sev=purple
  - 77: ds=23 sev=-
  - 44: ds=15 sev=-
  - 33: ds=2 sev=-
  - 66: ds=0 sev=-
- non_repeating:
  - 12: ds=108 sev=red
  - 26: ds=68 sev=red
  - 35: ds=38 sev=blue
  - 06: ds=35 sev=purple
  - 03: ds=33 sev=purple
  - 39: ds=31 sev=purple
  - 59: ds=29 sev=purple
  - 25: ds=28 sev=purple
  - 05: ds=27 sev=purple
  - 79: ds=26 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:676, 35:234, 6:197, 28:169, 1:149, 20:119, 3:116, 17:102, 26:59, 13:56

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=676 fs=1 fl=2 hz=0.009433962264150943, 35:ds=234 fs=0 fl=3 hz=0.005657708628005658, 6:ds=197 fs=14 fl=2 hz=0.02077922077922078, 28:ds=169 fs=7 fl=0 hz=0.011335012594458438, 1:ds=149 fs=0 fl=0 hz=0.0, 20:ds=119 fs=18 fl=1 hz=0.02280912364945978, 3:ds=116 fs=16 fl=3 hz=0.023199023199023196, 17:ds=102 fs=17 fl=3 hz=0.022753128555176336, 26:ds=59 fs=3 fl=2 hz=0.007552870090634441, 13:ds=56 fs=23 fl=2 hz=0.02969121140142518

### Sums (source: aux_validation.sums_stats_by_variant)
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S4: ds=100 flags=red+purple
- S5: ds=100 flags=red+purple
- S21: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S25: ds=90 flags=purple
- S27: ds=80 flags=blue+purple
- S19: ds=78 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '2', '9'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 015: score=2 tags=FLT,MIR
  - 016: score=2 tags=FLT,MIR
  - 025: score=2 tags=FLT,MIR
  - 027: score=2 tags=FLT,MIR
  - 035: score=2 tags=FLT,MIR
  - 038: score=2 tags=FLT,MIR
  - 045: score=2 tags=FLT,MIR
  - 049: score=2 tags=FLT,MIR
  - 056: score=2 tags=FLT,MIR
  - 057: score=2 tags=FLT,MIR

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 228 -> evening:932(B); midday:802(B)
- 255 -> combined:730(B); midday:752(B)
- 288 -> combined:830(B); midday:955(B)
- 338 -> evening:676(B); midday:722(B)
- 388 -> combined:691(B); evening:806(B)
- 778 -> combined:811(B); evening:986(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:95(blue); evening:49(purple); midday:47(purple)
- 24 -> combined:48(blue); midday:31(purple)
- 25 -> combined:45(blue); evening:28(purple)
- 26 -> combined:49(blue); evening:68(red)
- 27 -> combined:34(purple); midday:32(purple)
- 35 -> combined:67(red); evening:38(blue); midday:33(purple)
- 39 -> combined:29(purple); evening:31(purple)
- 55 -> combined:76(blue); evening:38(purple); midday:43(purple)
- 59 -> combined:58(red); evening:29(purple); midday:43(blue)
- 77 -> combined:46(purple); midday:30(purple)
- 79 -> combined:39(blue); evening:26(purple)
- 88 -> combined:123(red); evening:90(blue); midday:61(purple)
- 99 -> combined:27(purple); evening:25(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 1(7.382042857142857)[R2,XVAR-Cons(CEM)], 4(4.703892857142857)[R3,XVAR-Cons(CEM)], 7(3.8215714285714286)[R1,XVAR-Cons(CM)], 9(1.0678071428571427)[R2,Mirror-Echo]
- P2: 5(6.8957)[R2,XVAR-Cons(CEM)], 8(6.510685714285715)[R1,Mirror-Echo], 3(3.1627142857142854)[R3,Mirror-Echo], 6(0.19092142857142858)[R3,Swap]
- P3: 2(7.7196)[R1,XVAR-Cons(CEM)], 9(4.067035714285714)[R2,Mirror-Echo], 4(2.4078214285714283)[R3,Mirror-Echo], 6(1.3762857142857143)[R1,Double-Pressure], 3(0.2881)[R3,Swap]
