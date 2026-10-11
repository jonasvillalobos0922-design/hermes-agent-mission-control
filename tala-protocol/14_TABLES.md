# 14 — TABLES

**TIER:** REF | **DEPENDS:** 01, 02, 04, 08 | Tables are *inputs to rules*. Draw rows from the tape: **d20** and **d6** use their columns directly; **d12** = ((d100 − 1) mod 12) + 1 (≈1% bias accepted); **d10** = last digit of the d100 (0 = 10).

---

## T1 — Scavenge flavor (d10 by resource; flavor only, never quantity)

Quantity comes from the yield table (file 02 §7). T1 says what the units look like. A Bonus find result of 5 uses the flavor row's item.

**FOOD (Rations):** 1 canned sardines · 2 instant noodles · 3 sack of rice · 4 dried fish packets · 5 biscuits and condensed milk · 6 canned corned beef · 7 ripe bananas (fresh, spoil in 3 Days) · 8 peanut butter jar · 9 boil-in-bag meals · 10 mixed leftovers (fresh, spoil in 1 Day; need a fire)

**WATER (L, packaged):** 1 5-gallon dispenser jug · 2 bottled water case · 3 sealed rain barrel (needs boiling) · 4 cistern tap jug (needs boiling) · 5 sodas (+1 LOB, sugary) · 6 coconut water cartons · 7 hotel minibar · 8 ice melt · 9 filter bottle · 10 fire-hose reserve (needs boiling)

**MEDICAL:** 1 gauze and tape · 2 antiseptic wash · 3 paracetamol strip · 4 antibiotic courses · 5 saline bags · 6 suture kit · 7 glucose tablets · 8 box of face masks · 9 ORS packets · 10 compression bandages. **Remisol never appears here** (file 04 §5).

**PARTS:** 1 wire coil · 2 batteries (AA ×8) · 3 duct tape · 4 fasteners and hinges · 5 steel pipe · 6 solar panel fragment · 7 handset charger and cable · 8 bike chain · 9 padlocks · 10 hand drill

**FUEL:** 1 jerrycan (gasoline) · 2 diesel from a generator · 3 LPG cylinder (cooking only) · 4 kerosene · 5 boat outboard fuel · 6 generator petrol · 7 isopropyl alcohol · 8 siphon from a wreck · 9 motorbike tank · 10 truck diesel

---

## T2 — Encounters (d12, by Heat tier)

**QUIET (Heat 0–2):** 1 lone Lakad in a doorway · 2 two Lakad asleep standing · 3 stray dog (friend or alarm) · 4 survivor scavenging, wary · 5 scream far away (Heat +1 elsewhere) · 6 nothing but a sound behind a wall · 7 Sariwa (D1–D7 only; else Lakad) · 8 sealed door knocking from inside · 9 a handwritten note on a gate · 10 a body with a keepsake · 11 a locked pantry · 12 a drifting cluster (2 Lakad)

**STIRRING (Heat 3–5):** 1 Pack of 3 Lakad · 2 Lakad with a Sariwa · 3 a Hiyaw at distance (D14+) · 4 Tulisan scouts · 5 a wounded survivor asking for help · 6 two Lakad in a stairwell · 7 Lakad crowd in an open yard · 8 mesh ping from an unknown handset · 9 a barricaded family refusing entry · 10 a collapsed floor with a Gutom below · 11 FBC drone overhead (leash check-in) · 12 Pack of (Density+2)

**DRAWN/SWARM (Convergence):** use file 02 §5 (Pack or Horde). Add one complication: 1–4 a second group from another direction · 5–8 an exit blocked · 9–10 a Hiyaw screams (+3 Heat) · 11–12 a survivor group runs into you.

---

## T3 — Costs (d12)

1 +30 min lost · 2 N+1 spike · 3 Graze (−1 Vit) · 4 tool Durability −1 · 5 yield reduced by 1 · 6 someone sees you · 7 S+1 for a Watch · 8 door/loot stuck (Task to open) · 9 contaminated (d100 ≤ 30 → Gut-Sick) · 10 forced to drop an item · 11 handset knocked: battery −5% · 12 a rival scavenger notices your route

---

## T4 — Weather (d20)

1 Storm (Heat −1/Watch outdoors; boats unusable; travel DC +2) · 2–4 Heavy rain (Stealth DC −2; +1 L collectible/Watch) · 5–8 Showers (Stealth DC −1) · 9–14 Overcast, humid · 15–18 Clear, hot (WTR −1 extra per Watch) · 19–20 Amihan breeze (D45+ only; else Clear) — cooler, drier, noise carries (+1 N in open).
**Scheduled:** D9–D10 = Typhoon Dindo (override; Storm). Weather rolls once per Day at DWN.

---

## T5 — Mesh chatter (one per Day boundary, d20 column)

1 Ang Tinig: "Water at the Capitol cistern. Bring your own jug." · 2 Bayanihan relay: "Node 4 is dark. Bring parts." · 3 Command: "Perimeter holds. Remain indoors." · 4 Carbon: "Tribute is due at dusk." · 5 a child's voice: "Is anyone near Lahug?" · 6 FBC: "Registration of handsets continues at Pier 1." · 7 Lumina: "Medical access is by invitation." · 8 Fisher: "Tide favours a short crossing tonight." · 9 Static, then a hum · 10 Ang Tinig: "Three barangays share a stove tonight." · 11 Command: "Drone sweep scheduled for dusk." · 12 unknown: "Do not answer the radio at night." · 13 Mering: "We will not close the gate on anyone with a bag of rice." · 14 Tulisan: "Colon is ours. Walk around." · 15 Command: "Selection will be announced soon." (D20+) · 16 Lumina: "Beacon tests continue." (D40+) · 17 Ang Tinig: "Who has a doctor?" · 18 Fisher: "Fuel for a seat." · 19 Pagsibol: "The harvest is coming." (D40+) · 20 Static only.

---

## T6 — NPC reaction (d100)

**Roll d100 + (Standing × 5) + (Tiwala × 5).** Bands: ≤20 **Hostile** · 21–40 **Wary** · 41–60 **Neutral** · 61–80 **Friendly** · 81+ **Eager**.
Modifiers: offering a costed gift +10 · armed/aggressive −10 · visible bite/Fever −20 · known TALA user in Command zone −5.

---

## T7 — Loob events (d6)

**Breaking (LOB 0):** 1 **Freeze** (lose next 2 rounds) · 2 **Flee** (bolt to nearest exit, drop an item) · 3 **Lash out** (Resolve DC 12 or strike nearest person) · 4 **Collapse** (RST −2) · 5 **Silence** (VOICE −2 for a Watch) · 6 **Panic hoard** (take food you don't need; ally Tiwala −1)
**Bright moment (d6):** 1 a song on the radio (+1 LOB) · 2 a stray cat shares a ledge (+1) · 3 clear night, stars through a broken roof (+2, Anchor refresh) · 4 rain collected cleanly (WTR +2) · 5 an old photo found (+1; may sting) · 6 a stranger shares a meal (+1, Standing +1 with their group)

---

## T8 — Location events (d12, inside buildings)

1 collapsed stairs · 2 a shrine of family photos · 3 a locked pantry (needs Tools) · 4 a Lakad trapped in a closet · 5 a handwritten note ("We went to the Capitol") · 6 a flickering outlet (generator hum nearby) · 7 a radio crackle with a voice · 8 a bloodstained mattress · 9 a child's drawing on a wall · 10 a sealed rice bag · 11 a dead person clutching a Bantay handset (full of Ledger entries) · 12 a clean bed and a window with a view of the stars
