# Session 4 — City Encounters (DM quick index)

**Campaign:** No Cause for Alarm, v4.52. **Party:** four level-4 characters. These are optional public situations, not prescribed battles or a quest chain. Chapter 6 of `No_Cause_for_Alarm_5etools_CURRENT.json` contains complete read-aloud cues, NPC motives, disclosures, choices, and consequences.

| Situation | Where | If violence begins | File |
|---|---|---|---|
| The Sign Makers | Civic square | 1 Guard + 1 Commoner clerk | [Encounter 1](session4-city-01-sign-makers.json) |
| The Evicted Guests | Hotel frontage | 2 Guards | [Encounter 2](session4-city-02-evicted-guests.json) |
| The Permit Dispute | Market | 1 Guard + 1 Commoner clerk | [Encounter 3](session4-city-03-permit-dispute.json) |
| The King's Generosity | South Ward bread queue | 2 Guards + 1 Commoner herald | [Encounter 4](session4-city-04-kings-generosity.json) |
| The Unpaid Workers | Restored city-wall frontage | 2 Angry Laborers + 1 Guard | [Encounter 5](session4-city-05-unpaid-workers.json) |

Two additional optional encounter presets: [Evicted Guests with an already-present Warrior Veteran](session4-city-02-OPTIONAL-veteran.json) and [a separate street brawl with two Hired Muscle](session4-city-OPTIONAL-street-toughs.json). Neither group is an automatic reinforcement wave. A complaint, insult, rejected permit or citizen disagreement does not trigger initiative.

**Rules and 5etools:** The import files use the repository's established 5etools `fileType: encounter` format with `siteVersion: 2.36.1` and a party of four level 4 PCs. They reference Guard, Commoner, and Warrior Veteran from XMM. Angry Laborer and Hired Muscle are **custom NCFA stat blocks**, added to the live campaign JSON's `monster` array; import/load NCFA homebrew before opening encounters that use them. These imports load possible combatants, not everyone standing in the scene.

**Quick stats:** Guard AC 16, HP 11, Spear +3, 1d6+1 piercing. Warrior Veteran AC 17, HP 65, two Greatsword attacks +5 (2d6+3 each), Parry reaction +2 AC. Commoner AC 10, HP 4, improvised +2 / 1d4 as simplified table reference. Angry Laborer AC 11, HP 9, hammer +3 / 1d6+1. Hired Muscle AC 13, HP 22, weighted club +4 / 1d6+2, dagger +4 / 1d4+2.

## Playtest report — October 25, 2026

These are **DM scenario simulations and estimated pacing**, not observed play with your actual four players. No one can honestly guarantee a three-hour runtime when all five situations can be bypassed.

| Test route | Simulated choices | Approximate length | What it reveals |
|---|---|---|---|
| Fast | Resolve Noren quickly; bypass city disputes; buy one item; brief Brakkus dinner; Tulcornix | **53 min** | The adventure can still be short. Do not force encounters. |
| Curious | Question two city groups; spend time in shops; meaningful discussion at Ledger House | **147 min (2h27)** | The new encounters support more playable exploration without mandatory combat. |
| Deep exploration | Engage four scenes, investigate trade and bread distribution, shop at length, have a long dinner | **234 min (3h54)** | Three hours is possible when players actually invest, not guaranteed. One or more Ledger House arrivals may happen while they are elsewhere. |
| Hostile | Attack during a permit dispute; briefly fight a Guard; face witnesses, then return to Ledger House | **121 min (2h01)** | Street guards are too weak to consume much play; consequences involve real witnesses and travel, not arbitrary reinforcement waves. Arrest or imprisonment can prevent Tulcornix's planned appearance; respect that. |

**Tactical stress test (approximate, not exact character builds):** Using a conservative four-PC level-4 attack-only model, median resolution was ~1 round against a single Guard, ~2 rounds against 2 Guards, ~2 rounds against 2 Laborers + a Guard, ~2 rounds against two Hired Muscle, and ~6 rounds against 2 Guards + a Veteran. This ignores spell resources, crowd positions, negotiations, incapacitation, guard flight and actual initiative; its purpose is only to flag that most patrol fights will be very short while the OPTIONAL veteran encounter could be genuinely dangerous. Do not enlarge patrols after a party wins quickly.

**Regression checks:** all seven imports parse, homebrew reference hashes match NCFA monsters, IDs are unique, official reference sources are XMM, party size and level are 4 × 4, the chapter has exactly five optional scenes, approved maps and original NPC sessions remain, and Tulcornix still delivers the final confrontation. The actual 5etools UI import was not tested here; only file-format and reference checks were performed.

**Use at the table:** Describe any one situation if the PCs naturally enter that district. Let them decide what matters. Display the encounter builder file **only** if something genuinely escalates to a fight. After Tulcornix confronts Pepper, **end Session 4**; do not begin Elowen's rescue tonight.


## Single physically buildable street map and numbered miniature pull — 2026-10-25

**Map / terrain:** Your ENHANCE 36 × 24-inch, 1-inch grid mat. Five storefront/frontage boxes are drawn on the mat; main street kept empty for tactical movement. Place only 6 STAHLHAMMERS standard walls, 2 door walls, 1 window wall, 4 barrels, and 2 jars. No prebuilt buildings, fountain, cart, wagon, tree, bench or extra furniture is required. The exact coordinate diagram is in the uploaded player/DM street layout on Google Drive.

**[36 × 24 build diagram on Drive](https://drive.google.com/file/d/1HHh3qZNux7C4CsV47OUQCuZ2cgcxJMcX/view?usp=drivesdk)** · **[complete mini pull and mat setup guide](https://drive.google.com/file/d/1qiVZEYuux7n7cNIqckXlj3YA3_Er4gO2/view?usp=drivesdk)**

All mini numbers below are matched to the user's authoritative 161-mini Arcknight binder, with permanent numbers and known appearances. **They are visual proxies, not assertions of species, class or equipment. Reuse between different city scenes only; never show two simultaneous NPCs with one model.**

| Location / scene | Every speaking NPC / representative civilian | Mini #s (proxies as needed) |
|---|---|---|
| Kellan's Well | Noren; captive Veteran | #025; #033 |
| Ledger House | Brakkus; Jord; Brann; Tulcornix (final beat) | **original Brakkus mini**; #043; #048; #037 |
| Shops | Tiera (Tiny Mage); Edda (Spare Button); Joren; Maten (Two Hammers); Jord (Odds & Ends) | #017; #005; #029; #042; #043 |
| 1. Sign Makers | Worker A; Worker B; Royal Clerk; Guard | #046; #062; #027; #021 |
| 2. Evicted Guests | Hotel proprietor; first and second displaced adult; child; 2 Guards | #017; #039; #041; #018; #035/#036 |
| 3. Permit Dispute | Merchant; clerk; Guard; one shopper if addressed | #040; #027; #021; #019 |
| 4. King's Generosity | Herald; baker; 2 Guards; two representative residents | #028; #029; #035/#036; #019/#017 |
| 5. Unpaid Workers | 2 primary laborers; Crown administrator; Guard; optional witness worker | #046/#062; #027; #021; #045 |
| Independent street toughs (if needed) | Hired Muscle A and B | #045/#046 |
| Koven House only if attacked | 6 guards; Veteran sergeant; 2 clerks | #026/#030/#031/#032/#034/#038; #044; #017/#039 |

Pages/pockets for the most-used street pull: #017 P03 Front TL; #018 P03 Front TR; #019 P03 Front BL; #021 P03 Back TL; #027 P04 Front BL; #028 P04 Front BR; #029 P04 Back TL; #035 P05 Front BL; #036 P05 Front BR; #039 P05 Back BL; #040 P05 Back BR; #041 P06 Front TL; #042 P06 Front TR; #045 P06 Back TL; #046 P06 Back TR; #062 P08 Back TR. (Page 08 Back Top Right for #062 is confirmed by permanent numbering.) For **all** pages/pockets consult the complete Drive mini pull guide.

Do not pull Prince Reginald, Princess Narcissa, or King Hendrix minis for Session 4: they do not physically appear. Unnamed queues and crowds are described, with one or two visual representatives, not fabricated as fixed individual NPCs. Optional Koven House figures remain in the binder unless the players decide to attack.
