# Competition 8 Evening Rerank After Midday

Date target: `2026-03-21 Evening`  
Midday truth file: `.codex/competition8_midday_results_2026-03-21.txt`

Midday results used:

- `Connecticut4 -> 954`
- `NewJersey4 -> 992`
- `Virginia4 -> 940`
- `NorthCarolina4 -> 550`
- `OntarioCanada4 -> 148`

## Method

This rerank keeps the original pre-day predictive pack intact and uses Midday only as a truth/update layer.

What changed from the original Competition 8 pass:

- Control Center sharepack was refreshed against the Midday results file
- winners-side VTRAC HTML/JSON was generated for the five Midday winners
- evening ranking was adjusted by:
  - what actually fired at Midday
  - what core state lanes appear untouched
  - what families look cross-state spent versus still locally live

## Most Important Midday Lessons

### 1. No NJ/NC state-label mix-up happened

The rebuilt predictive packs were correct.

What happened instead:

- `New Jersey Midday 992`
  - sat inside `NorthCarolina4` watchlist lane `31 => 299 / 992 / 924 / 249`
- `North Carolina Midday 550`
  - sat inside `NewJersey4` watchlist lane `1 => 005 / 055 / 550 / 500`
  - and also inside `OntarioCanada4` watchlist lane `1 => 055 / 550 / 005`
- `Virginia Midday 940`
  - sat inside `NewJersey4` evening alert family `049 / 094 / 409 / 490 / 904 / 940`

So the board behaved like a cross-state spillover board:

- live family complexes were trapped
- but multiple complexes landed in neighboring strong states instead of their home state

### 2. Midday did not consume every state equally

The rerank is not simply:

- “a state hit midday so lower it”

Instead the right question is:

- did Midday consume that state’s own core evening structure?

That answer differed a lot by state.

## Updated Evening Ranking

1. `Virginia4`
2. `NewJersey4`
3. `NorthCarolina4`
4. `Connecticut4`
5. `OntarioCanada4`

## Why The Ranking Changed

### 1. Virginia4 moves to the top

Why:

- the original Virginia core was:
  - `225`
  - `022`
  - `255`
  - `259`
  - `224`
  - `229`
- `940` Midday did **not** come from that core
- the winner-side VTRAC-15 review for `940` was mostly off-core relative to Virginia’s main predictive lane
- Virginia’s strongest evening story therefore remains largely unspent
- due-double posture is still favorable
- Control Center `022` signals still stand and were not consumed by the Midday result

Best read:

- Virginia is now the cleanest untouched evening lane among the top three

Updated evening core:

- `225`
- `022`
- `255`
- `259`
- `224`
- `229`

Secondary:

- `257`
- `268`

### 2. NewJersey4 stays very strong, but narrower

Why it drops from first to second:

- New Jersey still has the best raw compression
- but Midday showed that some NJ-adjacent family energy already fired elsewhere:
  - `550` landed in NC from the NJ/ON `055/005` family complex
  - `940` landed in VA from NJ’s `049` alert family
- that makes the evening version of NJ less about broad family coverage and more about the untouched center

What remains strongest for evening:

- `455`
- `559`
- `445`
- `499`
- `344`
- `003`

What gets de-emphasized after Midday:

- `005`
- `055`
- `049`

Best read:

- still a strong boxed-hit state
- but now the most profitable NJ evening pack is tighter than the original one

### 3. NorthCarolina4 remains dangerous, but more crossover-prone

Why it drops to third:

- NC still has major structural strength
- but it was the most crossover-heavy state on the board
- `992` landed in NJ but belonged to NC’s `31 / 299` watchlist lane
- `550` landed in NC from the NJ/ON `055 / 005` complex, not from NC’s own strongest primary lane

That means:

- NC was globally “in the mix”
- but it was not the cleanest state-local extractor at Midday

For evening, I would keep NC but shift emphasis away from the lane that already cross-fired.

Primary evening core:

- `499`
- `117`
- `599`
- `449`
- `122`
- `177`

Reduced emphasis:

- `299`
- `249`
- `992`

Best read:

- still very playable
- but more plural and spillover-prone than Virginia or tight NJ

### 4. Connecticut4 stays low

Why:

- Midday `954` was a true miss relative to the main CT pre-day story
- the original CT thesis was VTRAC `18` with:
  - `113`
  - `136`
  - `366`
  - `668`
- Midday instead landed on index `15` / canonical family `459`
- winner-side review shows more `445/440` style family texture than the original CT core

This does suggest one useful thing:

- if CT is played at all for evening, add only a very small defensive shoulder around the `459/445` family

But the state is still not trustworthy enough to move up.

Primary evening core:

- `113`
- `136`
- `366`
- `668`
- `224`
- `355`

Tiny defensive shoulder only:

- `459`
- `445`

### 5. OntarioCanada4 stays last

Why:

- Midday `148` was not trapped by the main ON pre-day structure
- winner-side review shows a broad VTRAC-24 family field rather than a clean pre-day extraction
- ON already had a split state profile before Midday
- then the `055/005` family complex also cross-fired into NC, weakening one of Ontario’s best evening pathways

Best read:

- keep as lowest-priority coverage only

If played at all, I would center Ontario more on:

- `368`
- `259`
- `568`

and de-emphasize:

- `055`
- `559`

## Updated Evening Packs

### Virginia4

Primary:

- `225`
- `022`
- `255`
- `259`
- `224`
- `229`

Secondary:

- `257`
- `268`

### NewJersey4

Primary:

- `455`
- `559`
- `445`
- `499`
- `344`
- `003`

Secondary:

- `001`

## Evening Result Addendum

Evening truth later came back as:

- `Connecticut4 -> 394`
- `NewJersey4 -> 950`

These do not change the earlier rerank history, but they do add two important relationship-study cases.

### Connecticut4 -> `394`

This is the clearest example on the board of a result that was not directly called, but still looks structurally related to the final findings environment.

Important local ingredients were:

- `A10 099 DBL/RANK1`
  - implied set: `099 / 909 / 990`
- `A12 355 PERM/CLAMP`
  - implied set: `503 / 508 / 553 / 558`
- arena VTRAC watchlist `15`
  - `440 / 044 / 099`
- arena VTRAC watchlist `4`
  - `355 / 003`

Why this matters:

- the evening winner `394` was not a direct literal catch
- but the board did preserve:
  - a doubled `99` anchor
  - a doubled `55` anchor
  - a live `3` key through `355`
  - the same-index / same-neighborhood shoulder behavior around the missed Midday `954` case

Current judgment:

- this should still be treated as `composite`, not direct
- but it is exactly the kind of result that argues for a later final-findings relationship layer instead of literal-only grading

### NewJersey4 -> `950`

This also reads as a relationship-driven result rather than a clean direct literal call.

The strongest pre-result New Jersey structures were:

- `455`
- `559`
- `445`
- `499`
- `344`
- `003`

And the live supporting neighborhoods included:

- VTRAC `15`
  - `049 / 459 / 445 / 044 / 599`
- VTRAC `5`
  - `559 / 004 / 455 / 554 / 009`
- VTRAC `4`
  - `003 / 355 / 053 / 508 / 805 / 035 / 558`

Why this matters:

- `950` again looks closer to a mirror-double / lane-shoulder conversion than to a literal top-list hit
- it sits nearer the active `049 / 459 / 599` and `455 / 559 / 009` family environment than a plain miss label would suggest

Current judgment:

- not direct
- stronger than a random miss
- best preserved as a `lane/family-to-composite` evening case for later relationship study

## Resulting Lesson

Competition 8 is now even clearer:

- the current arena branch is already good at trapping live family environments
- it is not yet fully operationalizing the final relation work between:
  - doubled anchors
  - mirror doubles
  - same-index shoulders
  - key-digit carry
  - and cross-state spillover

That is exactly why the next layer should sit:

- above per-state arena analysis
- and below advanced combination forming

Reduced after Midday:

- `005`
- `055`
- `049`

### NorthCarolina4

Primary:

- `499`
- `117`
- `599`
- `449`
- `122`
- `177`

Secondary:

- `889`
- `348`

Reduced after Midday crossover:

- `299`
- `249`

### Connecticut4

Primary:

- `113`
- `136`
- `366`
- `668`
- `224`
- `355`

Defensive shoulder only:

- `459`
- `445`

### OntarioCanada4

Primary:

- `368`
- `259`
- `568`

Secondary:

- `355`
- `599`

Reduced after Midday:

- `055`
- `559`

## Best Practical Read

If reduced to three evening states after Midday:

1. `Virginia4`
2. `NewJersey4`
3. `NorthCarolina4`

If reduced to two:

- `Virginia4`
- `NewJersey4`

If reduced to one:

- `Virginia4`

## Final Judgment

The original pre-day analysis was directionally strong, but Midday exposed a real board behavior:

- strong double/mirror family complexes were live
- they spilled across the strongest states instead of resolving locally

For evening, the safest response is not to chase the already-fired spillovers.

The better response is:

- move up the cleanest untouched core
- tighten NJ to its still-unspent center
- keep NC but reduce the lane that already cross-fired
