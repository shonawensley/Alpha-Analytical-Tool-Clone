# Digit-Reduction Cheat-Sheet  🥷 *AAT9*

> *Pin this beside your keyboard.  Everything here fits on one screen.*

| ℹ️ WHAT | HOW / CODE SNIPPET | TIP |
|--------|--------------------|-----|
| **Run module** | `python long_string_reducer_part2.py --csv_dir tables/ --out outputs/` | Generates HTML in `outputs/`. |
| **Where strings come from** | Area-1 → `Set3/2/1 Draw1 col7 6 5`  <br>Area-2 → `Set1 Draw4 col3`, `Draw6 col1` | Extracted by helper fns in *part1*. |
| **Draw sequences (7×)** | `get_draw_lists_for_section(big, "Midday")["own"]` | “Combined” is interleaved Midday↔Evening. |
| **Mirror pairs** | `MIRROR_MAP = {"0":"5", … "4":"9"}` | 0↔5 1↔6 2↔7 3↔8 4↔9 |
| **Reduction methods** | | |
| A  _exact-all_ | `state.replace(d,"")` for each exact digit *d* | Wipes every copy of *d*. |
| B  _exact-else-mirror (all)_ | If *d* present ⇒ wipe *d* else wipe mirror | |
| C  _exact + mirror (all)_ | Always wipe both *d* and mirror | |
| D  _transit (single mirror)_ | Wipe all *d*, **then one mirror** | Legacy “transit digit”. |
| E  _single-hit legacy_ | Remove **one** exact, else **one** mirror | Old Method B. |
| T  _adaptive transit_ | 1) wipe all exacts <br>2) peel mirrors until len≤3 | Target length hard-coded to 3. |
| **Add new method** | 1. Define `def method_x(state, draw_digits): …` in *part1*  <br>2. Add to `METHOD_FUNCS` both files  <br>3. Append to `COLUMNS_ORDER` in *part2* | UI tab appears automatically. |
| **Quick sanity check** | In HTML → Method A-own → Midday Set1 Draw1 col7  <br>Original string :`559922086` <br>Draw-1 digits :`8 4 1` | Expect **`55992206`** after step-1 (all 8 4 1 removed). |
| **Typical investigation flow** | 1️⃣ Open HTML → pick method  <br>2️⃣ Scan mini-tables for 3-digit survivors  <br>3️⃣ Cross-reference with Stable-Pattern module | |
| **Regenerate full report** | Delete old `outputs/digit_reduction_*.html` and rerun script | Timestamped files avoid collisions. |
| **Common gotcha** | Empty strings after step-N? That’s OK – reduction stops early. | |

---

### Micro-Glossary
* **R2 string** – Raw pattern from combined table (row `R2`).  
* **Exact digit** – The literal drawn digit (e.g., 4).  
* **Mirror digit** – Its V-Trac pair (e.g., 9).  
* **Transit digit** – A mirror removed *only* when string is still “long.”

### FAQ
*“Why does Method T sometimes finish at length 2?”*  
> Because all mirrors of remaining digits may belong to the same draw digit – removal overshoots the target (acceptable).

*“Can I change the target length?”*  
> Edit `method_t(..., target_len=3)` call in *part2* if you need a 4-digit survivor list.

---

*© AAT9 Digit-Reduction module – 2025-05-25*
