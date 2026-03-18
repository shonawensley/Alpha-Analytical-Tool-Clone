# Aggregated Analysis Arena Pilot Review

Date: 2026-03-18

Purpose: review the first real aggregated analysis-arena runtime artifact after implementation, using one frozen day with winners present plus one predictive-side smoke day.

Primary build artifacts:
- `docs/AAT9_KIT/FINAL VALIDATION/final docs/AAT9_AGGREGATED_ANALYSIS_ARENA_CONTRACT_v0.md`
- `scripts/tools/build_aggregated_analysis_arena.py`

Pilot outputs:
- frozen review set:
  - `sharepacks/2025-12-31/Virginia4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
  - `sharepacks/2025-12-31/Florida4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
  - `sharepacks/2025-12-31/NewJersey4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
  - `sharepacks/2025-12-31/NorthCarolina4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
- predictive smoke:
  - `sharepacks/_predictive/2026-03-15/NorthCarolina4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`
  - `sharepacks/_predictive/2026-03-15/NewJersey4/analysis/aggregated_analysis_arena__tool_only__arena_v0.json`

---

## Topline

The first aggregated arena object is successful as a runtime artifact.

It now gives a single per-state snapshot that:
- preserves Stable, DR, VTRAC, Hot Zones, and Aux / Control Center together
- exposes cross-tool canonical / family / VTRAC-lane agreement
- keeps downstream Candidate Universe / Play Card artifacts explicitly separate
- makes arena-vs-downstream comparison operational

The first frozen review also showed the expected current limitation:
- the arena is already better at preserving winner-related VTRAC lane truth than literal winner canonicals
- it is not yet a literal-conversion engine

That is a good result for v0.

---

## Pilot Set

Chosen frozen review states on `2025-12-31`:
- `Virginia4`
- `Florida4`
- `NewJersey4`
- `NorthCarolina4`

These gave:
- a same-index swarm / lane-heavy case (`Virginia4`)
- a hot-zones / context-heavy split case (`Florida4`)
- a strong VTRAC-family environment (`NewJersey4`)
- a doubles-heavy noisy environment (`NorthCarolina4`)

---

## What Worked

### 1) The artifact is real and reviewable

Each pilot state now has one object with the same stable top-level namespaces:
- `metadata`
- `provenance`
- `string_tools`
- `context_tools`
- `cross_tool_relations`
- `arena_synthesis`
- `downstream_handoff`
- `review_links`

That is the first time the analysis-arena branch has had a real per-state runtime SSOT object instead of scattered tool folders plus prose.

### 2) Cross-tool VTRAC agreement is visible immediately

Across the four frozen pilot states, the arena surfaced strong dominant VTRAC indices even when literal winners were not dominant canonicals.

Winner VTRAC index rank in the arena:

| State | Winners | Winner VTRAC index | Arena index rank |
|---|---|---:|---:|
| `Virginia4` | `686 / 636` | `18` | `3` |
| `Florida4` | `407 / 211` | `12 / 17` | `7 / not ranked` |
| `NewJersey4` | `366 / 418` | `18 / 24` | `2 / not ranked` |
| `NorthCarolina4` | `867 / 057` | `21 / 3` | `not ranked / 7` |

This is exactly the kind of signal the new layer was supposed to expose:
- the arena can preserve winner-lane truth even when literal conversion is still weak

### 3) Context is now visible as reinforcement, not hidden promotion

All four frozen pilot states showed `context_reinforced` regimes in the arena.

That means the new object is doing something the old narrow consumers could not do cleanly:
- it shows where Aux / Control Center is supporting the same corridors the string tools are already surfacing
- without collapsing those context surfaces into final play-card logic

### 4) Downstream baselines are now easy to compare against the arena

In the same arena object, the current downstream baselines were easy to compare:

| State | Arena dominant canonical | Current play-card top |
|---|---|---|
| `Virginia4` | `177` | `004` |
| `Florida4` | `677` | `003` |
| `NewJersey4` | `299` | `022` |
| `NorthCarolina4` | `003` | `001` |

That is useful even when both miss.

It means the system can now separate:
- what the arena preserved
- what the current downstream consumer did with it

instead of treating them as one blurred miss.

---

## What The Pilot Shows About Current Limits

### 1) Canonical consensus is still too literal / clutter-heavy

In all four pilot states, the dominant arena canonicals were not the literal winners.

That is not a failure of the arena object itself.
It is evidence that:
- the current synthesis layer is still descriptive and broad
- it is not yet applying the next generation of conversion scoring

This is acceptable for v0.

### 2) The current contradiction layer is too permissive

All four frozen pilot states ended with:
- `context_reinforced = true`
- no contradiction flags

That is probably too soft.

The arena is already preserving rich context, but the next review/calibration pass should likely add sharper flags for:
- split literal regimes
- context pressure with weak literal closure
- strong VTRAC agreement but poor canonical concentration

### 3) Winner canonicals are often present somewhere, but not yet dominant

Text inspection of the resulting arena payloads showed the winner canonicals / winner indices were often still present somewhere in the preserved tool evidence, even when they were not in the top canonical consensus surface.

That is an important distinction:
- the arena is preserving more truth than the current top synthesis table alone suggests

---

## State Notes

### Virginia4

Winner:
- `686 / 636`
- both map to `VTRAC index 18`

Arena:
- dominant canonical: `177`
- dominant VTRAC indices: `20`, `23`, `18`
- winner lane `18` reached rank `3`

Read:
- the object preserved the correct winner-lane corridor strongly enough to review
- literal canonical concentration is still pointing elsewhere

### Florida4

Winner:
- `407` (`idx 12`)
- `211` (`idx 17`)

Arena:
- dominant canonical: `677`
- dominant VTRAC indices: `10`, `23`, `21`, then `12`
- `idx 12` only reached rank `7`; `idx 17` did not rank

Read:
- this remains a split / cluttered state
- the arena is useful because it makes the miss visibly lane-level rather than hiding it behind downstream boards

### NewJersey4

Winner:
- `366` (`idx 18`)
- `418` (`idx 24`)

Arena:
- dominant canonical: `299`
- dominant VTRAC indices: `31`, `18`, `28`
- winner lane `18` reached rank `2`

Read:
- this is one of the clearest “winner lane preserved, literal winner not promoted” pilot cases

### NorthCarolina4

Winner:
- `867` (`idx 21`)
- `057` (`idx 3`)

Arena:
- dominant canonical: `003`
- dominant VTRAC indices: `4`, `28`, `1`, then `3`
- evening winner lane `3` reached rank `7`; midday winner lane `21` did not rank

Read:
- this is the noisiest / most doubles-heavy pilot state
- the arena still improved interpretability because the environment is visibly double-heavy and context-reinforced

---

## Predictive Smoke

The same builder also wrote predictive-side artifacts for:
- `2026-03-15 / NorthCarolina4`
- `2026-03-15 / NewJersey4`

That confirms the runtime object works in both modes:
- predictive root: no winners artifacts required
- frozen/results root: winners links available for review

---

## Recommendation

Do not redesign combination-forming yet.

The next optimal move is:
1. use this new arena artifact as the main review object for a small frozen gold-day window
2. add one arena-native review scoreboard around it
3. classify gaps as:
   - arena missing
   - arena present but underweighted
   - conversion gap
   - budget / packaging gap

The important conclusion from the pilot is:

The analysis-arena branch now has a real runtime object, and it is already exposing lane/corridor truth more cleanly than the older downstream-only path. The next work should happen around arena review and synthesis calibration, not another return to broad tool-local tuning.
