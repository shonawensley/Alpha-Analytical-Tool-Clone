# Aux Summary — Indiana4 — 2025-06-21

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-21/Indiana4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_06_20.xlsm` | aux_state_label: Indiana
- combined: live=`data/cleaned/draws/Indiana_draws.csv` snap=`sharepacks/2025-06-21/Indiana4/aux/draws/Indiana_draws.csv` n=1000 head=059, 923, 378, 377, 641
- midday: live=`data/cleaned/draws/Indiana_Midday_draws.csv` snap=`sharepacks/2025-06-21/Indiana4/aux/draws/Indiana_Midday_draws.csv` n=1000 head=923, 377, 689, 940, 237
- evening: live=`data/cleaned/draws/Indiana_Evening_draws.csv` snap=`sharepacks/2025-06-21/Indiana4/aux/draws/Indiana_Evening_draws.csv` n=1000 head=059, 378, 641, 188, 550

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=5 streak=1 max=3 last_repeat_gap=17 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:4 (gap=42), P2:9 (gap=14), P3:5 (gap=36)
- consensus_notes: P1 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 9 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 6 (Mirror-Echo(CM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 464: score=46.53685071428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 414: score=45.02832214285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 465: score=44.533792857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 494: score=44.16275785714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 415: score=43.025264285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 495: score=42.1597 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 454: score=40.14670785714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 434: score=40.05400785714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 424: score=38.31367928571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 455: score=38.143649999999994 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 337: ds=988 sev=B
- 277: ds=949 sev=B
- 556: ds=923 sev=B
- 224: ds=915 sev=B
- 177: ds=898 sev=B
- 899: ds=858 sev=B
- 122: ds=818 sev=B
- 002: ds=779 sev=B
- 699: ds=741 sev=B
- 448: ds=738 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=70 sev=purple
  - 22: ds=40 sev=purple
  - 66: ds=32 sev=purple
  - 44: ds=30 sev=purple
  - 99: ds=27 sev=purple
  - 00: ds=19 sev=-
  - 11: ds=12 sev=-
  - 55: ds=8 sev=-
  - 88: ds=6 sev=-
  - 77: ds=3 sev=-
- non_repeating:
  - 28: ds=58 sev=red
  - 79: ds=52 sev=blue
  - 12: ds=46 sev=blue
  - 47: ds=37 sev=blue
  - 48: ds=37 sev=blue
  - 06: ds=35 sev=purple
  - 26: ds=32 sev=purple
  - 45: ds=30 sev=purple
  - 56: ds=29 sev=purple
  - 03: ds=26 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:361, 26:214, 18:199, 6:127, 32:93, 31:92, 2:77, 25:48, 34:45, 20:44

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=361 fs=1 fl=1 hz=0.010869565217391304, 26:ds=214 fs=1 fl=0 hz=0.004081632653061225, 18:ds=199 fs=27 fl=1 hz=0.03598971722365039, 6:ds=127 fs=23 fl=0 hz=0.027777777777777776, 32:ds=93 fs=1 fl=2 hz=0.009009009009009009, 31:ds=92 fs=22 fl=1 hz=0.027315914489311165, 2:ds=77 fs=24 fl=2 hz=0.02869757174392936, 25:ds=48 fs=22 fl=0 hz=0.023429179978700747, 34:ds=45 fs=18 fl=2 hz=0.02188183807439825, 20:ds=44 fs=23 fl=1 hz=0.0255863539445629

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S5: ds=99 flags=purple
- S24: ds=69 flags=purple
- S21: ds=51 flags=purple
- S3: ds=46 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 015: score=1 tags=MIR
  - 016: score=1 tags=MIR
  - 025: score=1 tags=MIR
  - 027: score=1 tags=MIR
  - 035: score=1 tags=MIR
  - 038: score=1 tags=MIR
  - 045: score=1 tags=MIR
  - 049: score=1 tags=MIR
  - 056: score=1 tags=MIR
  - 057: score=1 tags=MIR

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=30 streak=1 max=2 last_repeat_gap=73 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=29), P2:5 (gap=14), P3:8 (gap=25)
- consensus_notes: P1 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 9 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 6 (Mirror-Echo(CM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 464: score=46.53685071428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 414: score=45.02832214285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 465: score=44.533792857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 494: score=44.16275785714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 415: score=43.025264285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 495: score=42.1597 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 454: score=40.14670785714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 434: score=40.05400785714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 424: score=38.31367928571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 455: score=38.143649999999994 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 222: ds=985 sev=B
- 088: ds=935 sev=B
- 038: ds=869 sev=B
- 111: ds=827 sev=B
- 559: ds=826 sev=B
- 466: ds=809 sev=B
- 669: ds=804 sev=B
- 035: ds=802 sev=B
- 288: ds=799 sev=B
- 334: ds=759 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=80 sev=blue
  - 22: ds=48 sev=purple
  - 33: ds=39 sev=purple
  - 44: ds=35 sev=purple
  - 88: ds=25 sev=purple
  - 66: ds=16 sev=-
  - 99: ds=13 sev=-
  - 11: ds=11 sev=-
  - 00: ds=9 sev=-
  - 77: ds=1 sev=-
- non_repeating:
  - 79: ds=160 sev=red
  - 18: ds=66 sev=red
  - 28: ds=47 sev=blue
  - 38: ds=37 sev=blue
  - 12: ds=32 sev=purple
  - 15: ds=32 sev=purple
  - 03: ds=27 sev=purple
  - 58: ds=25 sev=purple
  - 59: ds=21 sev=-
  - 24: ds=20 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:474, 31:184, 35:180, 28:165, 25:112, 18:99, 5:65, 6:63, 21:53, 19:51

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=474 fs=0 fl=0 hz=0.0020920502092050207, 31:ds=184 fs=20 fl=1 hz=0.025766871165644172, 35:ds=180 fs=3 fl=0 hz=0.00823045267489712, 28:ds=165 fs=17 fl=2 hz=0.02464332036316472, 25:ds=112 fs=28 fl=0 hz=0.03248259860788863, 18:ds=99 fs=31 fl=0 hz=0.03629976580796253, 5:ds=65 fs=16 fl=1 hz=0.018867924528301886, 6:ds=63 fs=20 fl=3 hz=0.025302530253025302, 21:ds=53 fs=45 fl=1 hz=0.052873563218390804, 19:ds=51 fs=25 fl=1 hz=0.028540065861690448

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S20: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S5: ds=49 flags=purple
- S25: ds=41 flags=purple
- S6: ds=38 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '5'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 012: score=1 tags=FLT
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 035: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=5 streak=1 max=3 last_repeat_gap=9 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:9 (gap=42), P2:6 (gap=54), P3:7 (gap=22)
- consensus_notes: P1 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 mirror cluster around digit 9 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CM)), P1 mirror cluster around digit 2 (Mirror-Echo(CE)), P2 mirror cluster around digit 4 (Mirror-Echo(CM)), P2 mirror cluster around digit 1 (Mirror-Echo(CE)), P2 mirror cluster around digit 6 (Mirror-Echo(CM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:9 (ds=42), P2:6 (ds=54)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 464: score=46.53685071428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 414: score=45.02832214285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 465: score=44.533792857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 494: score=44.16275785714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 415: score=43.025264285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 495: score=42.1597 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 454: score=40.14670785714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 434: score=40.05400785714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 424: score=38.31367928571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 455: score=38.143649999999994 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 356: ds=969 sev=B
- 068: ds=952 sev=B
- 111: ds=892 sev=B
- 022: ds=872 sev=B
- 444: ds=838 sev=B
- 118: ds=764 sev=B
- 556: ds=757 sev=B
- 088: ds=704 sev=B
- 166: ds=701 sev=B
- 555: ds=686 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 99: ds=64 sev=purple
  - 00: ds=55 sev=purple
  - 33: ds=35 sev=purple
  - 77: ds=22 sev=-
  - 22: ds=20 sev=-
  - 66: ds=16 sev=-
  - 44: ds=15 sev=-
  - 11: ds=6 sev=-
  - 55: ds=4 sev=-
  - 88: ds=3 sev=-
- non_repeating:
  - 06: ds=59 sev=red
  - 13: ds=58 sev=red
  - 68: ds=52 sev=blue
  - 47: ds=46 sev=blue
  - 27: ds=45 sev=blue
  - 07: ds=44 sev=blue
  - 17: ds=42 sev=blue
  - 23: ds=35 sev=purple
  - 49: ds=33 sev=purple
  - 34: ds=32 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:249, 18:134, 11:127, 6:119, 32:118, 26:107, 34:84, 4:56, 24:51, 31:46

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=249 fs=2 fl=0 hz=0.006633499170812604, 18:ds=134 fs=21 fl=1 hz=0.025912838633686687, 11:ds=127 fs=34 fl=0 hz=0.040229885057471264, 6:ds=119 fs=26 fl=2 hz=0.0319634703196347, 32:ds=118 fs=2 fl=1 hz=0.006097560975609756, 26:ds=107 fs=1 fl=1 hz=0.0036855036855036856, 34:ds=84 fs=14 fl=4 hz=0.02127659574468085, 4:ds=56 fs=23 fl=3 hz=0.029246344206974126, 24:ds=51 fs=44 fl=0 hz=0.046858359957401494, 31:ds=46 fs=28 fl=1 hz=0.0306553911205074

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S5: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S4: ds=55 flags=blue+purple
- S19: ds=31 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 025: score=2 tags=FLT,MIR
  - 027: score=2 tags=FLT,MIR
  - 126: score=2 tags=FLT,MIR
  - 127: score=2 tags=FLT,MIR
  - 237: score=2 tags=FLT,MIR
  - 238: score=2 tags=FLT,MIR
  - 247: score=2 tags=FLT,MIR
  - 249: score=2 tags=FLT,MIR
  - 257: score=2 tags=FLT,MIR
  - 267: score=2 tags=FLT,MIR

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 088 -> evening:704(B); midday:935(B)
- 111 -> evening:892(B); midday:827(B)
- 337 -> combined:988(B); midday:751(B)
- 339 -> evening:678(B); midday:720(B)
- 556 -> combined:923(B); evening:757(B)
- 559 -> evening:673(B); midday:826(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 03 -> combined:26(purple); midday:27(purple)
- 06 -> combined:35(purple); evening:59(red)
- 12 -> combined:46(blue); midday:32(purple)
- 22 -> combined:40(purple); midday:48(purple)
- 28 -> combined:58(red); evening:29(purple); midday:47(blue)
- 33 -> combined:70(purple); evening:35(purple); midday:39(purple)
- 44 -> combined:30(purple); midday:35(purple)
- 47 -> combined:37(blue); evening:46(blue)
- 48 -> combined:37(blue); evening:32(purple)
- 57 -> combined:25(purple); evening:26(purple)
- 79 -> combined:52(blue); evening:26(purple); midday:160(red)
- 99 -> combined:27(purple); evening:64(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 4(7.71055)[R1,XVAR-Cons(CEM)], 8(4.077857142857143)[R2,XVAR-Cons(CM)], 7(2.6689714285714286)[R3,XVAR-Cons(CE)], 9(1.8732499999999999)[R1,Mirror-Echo], 5(0.16122857142857144)[R3]
- P2: 6(4.0081428571428575)[R2,Mirror-Echo], 9(2.6340500000000002)[R1,XVAR-Cons(CM)], 1(2.499614285714286)[R3,Mirror-Echo], 5(1.1179999999999999)[R1,Double-Pressure], 3(1.0252999999999999)[R2,Double-Pressure]
- P3: 5(7.8151)[R1,XVAR-Cons(CEM)], 4(5.773071428571428)[R2,XVAR-Cons(CEM)], 8(1.4164285714285714)[R1,Double-Pressure], 7(1.2568571428571427)[R1,Double-Pressure], 6(0.26971428571428574)[R3,Swap]
