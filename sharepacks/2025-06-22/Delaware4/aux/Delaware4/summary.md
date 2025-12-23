# Aux Summary — Delaware4 — 2025-06-22

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-22/Delaware4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-06-21.xlsm` | aux_state_label: Delaware
- combined: live=`data/cleaned/draws/Delaware_draws.csv` snap=`sharepacks/2025-06-22/Delaware4/aux/draws/Delaware_draws.csv` n=1000 head=989, 756, 527, 772, 471
- midday: live=`data/cleaned/draws/Delaware_Midday_draws.csv` snap=`sharepacks/2025-06-22/Delaware4/aux/draws/Delaware_Midday_draws.csv` n=1000 head=756, 772, 489, 937, 010
- evening: live=`data/cleaned/draws/Delaware_Evening_draws.csv` snap=`sharepacks/2025-06-22/Delaware4/aux/draws/Delaware_Evening_draws.csv` n=1000 head=989, 527, 471, 702, 277

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=34 streak=1 max=3 last_repeat_gap=13 last_repeat_index=9

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=35), P2:4 (gap=29), P3:4 (gap=21)
- consensus_notes: P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 145: score=51.18107928571428 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 144: score=47.837514285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 845: score=43.501642857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 844: score=43.24691428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 195: score=41.48202857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R2 src=cartesian
- 194: score=41.2273 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 165: score=40.849714285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R2 src=cartesian
- 164: score=40.59498571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 148: score=39.537035714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 545: score=39.479148571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 455: ds=905 sev=B
- 228: ds=869 sev=B
- 355: ds=865 sev=B
- 144: ds=829 sev=B
- 599: ds=817 sev=B
- 009: ds=798 sev=B
- 055: ds=787 sev=B
- 668: ds=755 sev=B
- 189: ds=749 sev=B
- 368: ds=712 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=115 sev=red
  - 88: ds=54 sev=purple
  - 66: ds=40 sev=purple
  - 22: ds=25 sev=purple
  - 11: ds=22 sev=-
  - 44: ds=21 sev=-
  - 33: ds=17 sev=-
  - 00: ds=9 sev=-
  - 77: ds=3 sev=-
  - 99: ds=0 sev=-
- non_repeating:
  - 35: ds=67 sev=red
  - 04: ds=56 sev=red
  - 09: ds=56 sev=red
  - 69: ds=53 sev=blue
  - 36: ds=45 sev=blue
  - 68: ds=44 sev=blue
  - 03: ds=43 sev=blue
  - 28: ds=39 sev=blue
  - 29: ds=36 sev=purple
  - 58: ds=34 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 13:176, 35:147, 31:118, 5:98, 4:96, 21:69, 33:66, 14:58, 19:53, 20:50

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 13:ds=176 fs=11 fl=1 hz=0.016883116883116882, 35:ds=147 fs=3 fl=0 hz=0.00909090909090909, 31:ds=118 fs=15 fl=3 hz=0.023622047244094488, 5:ds=98 fs=20 fl=1 hz=0.023411371237458192, 4:ds=96 fs=19 fl=1 hz=0.02600780234070221, 21:ds=69 fs=36 fl=1 hz=0.04111111111111111, 33:ds=66 fs=14 fl=2 hz=0.0188470066518847, 14:ds=58 fs=44 fl=0 hz=0.047311827956989246, 19:ds=53 fs=35 fl=1 hz=0.03956043956043956, 20:ds=50 fs=18 fl=3 hz=0.023281596452328163

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S27: ds=100 flags=purple
- S23: ds=80 flags=purple
- S24: ds=73 flags=blue+purple
- S17: ds=67 flags=red+purple
- S20: ds=66 flags=purple
- S22: ds=54 flags=purple
- S5: ds=46 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [4], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '3'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 013: score=3 tags=FLT,RS
  - 049: score=3 tags=FLT,RS
  - 058: score=3 tags=FLT,RS
  - 067: score=3 tags=FLT,RS
  - 139: score=3 tags=FLT,RS
  - 238: score=3 tags=FLT,RS
  - 346: score=3 tags=FLT,RS
  - 148: score=2 tags=RS
  - 157: score=2 tags=RS
  - 247: score=2 tags=RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=7 streak=1 max=2 last_repeat_gap=72 last_repeat_index=21

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:5 (gap=28), P2:0 (gap=38), P3:4 (gap=10)
- consensus_notes: P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 145: score=51.18107928571428 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 144: score=47.837514285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 845: score=43.501642857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 844: score=43.24691428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 195: score=41.48202857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R2 src=cartesian
- 194: score=41.2273 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 165: score=40.849714285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R2 src=cartesian
- 164: score=40.59498571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 148: score=39.537035714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 545: score=39.479148571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 008: ds=965 sev=B
- 589: ds=898 sev=B
- 244: ds=825 sev=B
- 035: ds=775 sev=B
- 122: ds=759 sev=B
- 778: ds=755 sev=B
- 336: ds=754 sev=B
- 368: ds=744 sev=B
- 588: ds=720 sev=B
- 118: ds=693 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=58 sev=purple
  - 55: ds=57 sev=purple
  - 11: ds=28 sev=purple
  - 66: ds=26 sev=purple
  - 22: ds=12 sev=-
  - 44: ds=10 sev=-
  - 33: ds=8 sev=-
  - 99: ds=5 sev=-
  - 00: ds=4 sev=-
  - 77: ds=1 sev=-
- non_repeating:
  - 05: ds=87 sev=red
  - 06: ds=65 sev=red
  - 04: ds=46 sev=blue
  - 02: ds=42 sev=blue
  - 09: ds=42 sev=blue
  - 12: ds=41 sev=blue
  - 58: ds=37 sev=blue
  - 17: ds=34 sev=purple
  - 35: ds=33 sev=purple
  - 23: ds=32 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:393, 16:219, 5:130, 17:107, 27:106, 33:99, 13:89, 3:87, 4:84, 35:73

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=393 fs=1 fl=3 hz=0.008888888888888889, 16:ds=219 fs=2 fl=1 hz=0.00657030223390276, 5:ds=130 fs=23 fl=2 hz=0.031685678073510776, 17:ds=107 fs=16 fl=3 hz=0.021420518602029315, 27:ds=106 fs=21 fl=1 hz=0.025142857142857144, 33:ds=99 fs=15 fl=2 hz=0.01893095768374165, 13:ds=89 fs=18 fl=0 hz=0.022511848341232227, 3:ds=87 fs=26 fl=0 hz=0.03082191780821918, 4:ds=84 fs=17 fl=2 hz=0.021566401816118047, 35:ds=73 fs=2 fl=1 hz=0.013636363636363637

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S2: ds=100 flags=purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S23: ds=85 flags=purple
- S3: ds=84 flags=purple
- S22: ds=82 flags=purple
- S20: ds=63 flags=purple
- S4: ds=59 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- _no candidates_

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=34 streak=1 max=3 last_repeat_gap=19 last_repeat_index=12

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=22), P2:4 (gap=19), P3:3 (gap=24)
- consensus_notes: P1 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 9 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 3 (Mirror-Echo(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P2 mirror cluster around digit 9 (Mirror-Echo(CEM)), P2 mirror cluster around digit 1 (Mirror-Echo(CM)), P2 mirror cluster around digit 4 (Mirror-Echo(CE)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 145: score=51.18107928571428 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),R1 src=lane
- 144: score=47.837514285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 845: score=43.501642857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 844: score=43.24691428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 195: score=41.48202857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R2 src=cartesian
- 194: score=41.2273 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 165: score=40.849714285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R2 src=cartesian
- 164: score=40.59498571428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 148: score=39.537035714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 545: score=39.479148571428574 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 333: ds=976 sev=B
- 699: ds=966 sev=B
- 019: ds=951 sev=B
- 449: ds=826 sev=B
- 244: ds=781 sev=B
- 116: ds=766 sev=B
- 229: ds=756 sev=B
- 055: ds=724 sev=B
- 399: ds=682 sev=B
- 000: ds=680 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=91 sev=blue
  - 33: ds=88 sev=blue
  - 44: ds=55 sev=purple
  - 22: ds=42 sev=purple
  - 88: ds=27 sev=purple
  - 66: ds=20 sev=-
  - 11: ds=11 sev=-
  - 00: ds=9 sev=-
  - 77: ds=4 sev=-
  - 99: ds=0 sev=-
- non_repeating:
  - 36: ds=78 sev=red
  - 35: ds=65 sev=red
  - 24: ds=63 sev=red
  - 03: ds=50 sev=blue
  - 08: ds=48 sev=blue
  - 34: ds=39 sev=blue
  - 28: ds=38 sev=blue
  - 69: ds=36 sev=purple
  - 48: ds=33 sev=purple
  - 04: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:228, 32:125, 13:88, 21:84, 28:79, 31:59, 11:56, 5:49, 4:48, 19:41

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=228 fs=1 fl=2 hz=0.005270092226613966, 32:ds=125 fs=1 fl=2 hz=0.007079646017699115, 13:ds=88 fs=14 fl=1 hz=0.01839080459770115, 21:ds=84 fs=54 fl=0 hz=0.06242774566473988, 28:ds=79 fs=20 fl=2 hz=0.024043715846994534, 31:ds=59 fs=18 fl=3 hz=0.02458100558659218, 11:ds=56 fs=50 fl=0 hz=0.05405405405405406, 5:ds=49 fs=10 fl=3 hz=0.014238773274917854, 4:ds=48 fs=24 fl=0 hz=0.02575107296137339, 19:ds=41 fs=27 fl=2 hz=0.03049421661409043

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S21: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S27: ds=100 flags=purple
- S17: ds=67 flags=purple
- S4: ds=50 flags=purple
- S6: ds=46 flags=red+purple
- S10: ds=42 flags=purple
- S23: ds=40 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['3', '6'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 013: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 034: score=1 tags=FLT
  - 035: score=1 tags=FLT
  - 036: score=1 tags=FLT
  - 037: score=1 tags=FLT
  - 038: score=1 tags=FLT
  - 039: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 055 -> combined:787(B); evening:724(B)
- 244 -> evening:781(B); midday:825(B)
- 368 -> combined:712(B); midday:744(B)
- 668 -> combined:755(B); evening:667(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 03 -> combined:43(blue); evening:50(blue)
- 04 -> combined:56(red); evening:28(purple); midday:46(blue)
- 09 -> combined:56(red); evening:28(purple); midday:42(blue)
- 22 -> combined:25(purple); evening:42(purple)
- 28 -> combined:39(blue); evening:38(blue)
- 35 -> combined:67(red); evening:65(red); midday:33(purple)
- 36 -> combined:45(blue); evening:78(red)
- 55 -> combined:115(red); evening:91(blue); midday:57(purple)
- 58 -> combined:34(purple); midday:37(blue)
- 66 -> combined:40(purple); midday:26(purple)
- 68 -> combined:44(blue); midday:29(purple)
- 69 -> combined:53(blue); evening:36(purple); midday:26(purple)
- 88 -> combined:54(purple); evening:27(purple); midday:58(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 1(6.520314285714286)[R2,XVAR-Cons(CEM)], 8(4.429714285714286)[R1,Mirror-Echo], 5(1.436)[R1,Double-Pressure], 0(0.9299)[R2,Double-Pressure], 3(0.8262857142857143)[R3,Mirror-Echo]
- P2: 4(7.270528571428572)[R1,Mirror-Echo], 6(3.528)[R2,XVAR-Cons(CM)], 9(3.1603142857142856)[R3,Mirror-Echo], 0(1.7449999999999999)[R1,Double-Pressure], 3(0.2612285714285714)[R3,Swap]
- P3: 5(6.801399999999999)[R2,XVAR-Cons(CEM)], 4(6.546671428571428)[R1,XVAR-Cons(CEM)], 8(1.7461928571428573)[R3,XVAR-Cons(CM)], 3(1.3165714285714285)[R1,Double-Pressure]
