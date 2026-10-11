# 02 — SURVIVAL & SIGNATURE

**TIER:** CORE | **DEPENDS:** 01

---

## 1. Needs (tracks 0–10, start at 8 unless Origin says otherwise)

| Need | Code | Decay (per Watch boundary) | Restore |
|------|------|---------------------------|---------|
| Water | WTR | −1 every 2 Watches (−1 every Watch if heat/exertion) | 1 L safe water = +2 |
| Food | FOD | −1 every 3 Watches | 1 **Ration** = +3 (the rules also call it a Meal): about a day and a half of food. Half-ration items = +1 or +2 |
| Rest | RST | −1 per Watch awake | Safe sleep +3/Watch · Fitful sleep +2/Watch |
| Loob (morale, "inner self") | LOB | event-driven; −1 per Day alone | see §9 |

**Thresholds (all needs):** **≤4 Strained** (−1 to all rolls) · **≤2 Failing** (−2 to all rolls, plus effect below) · **0 Crisis.**

| Need at 0 | Effect |
|-----------|--------|
| WTR | −1 Vitality per Watch until restored |
| FOD | −1 Vitality every 2 Watches until restored |
| RST | Microsleep collapse event; GM picks the worst moment within the Watch (Stealth/Athletics auto-Setback) |
| LOB | **Breaking event** (file 14 T7): freeze, flee, or lash out; player chooses one, outcome rolled |

**Untreated water:** drinking unboiled/unfiltered water triggers d100 ≤ 30 → **Gut-Sick** (−1 RST, −2 WTR next Watch, Medicine DC 12 to treat). Boiling takes 1 hr + fire (Signature S1, L4 at night) and 1 Fuel unit per 4 L.

## 2. Vitality & conditions

**Vitality** = 4 + BODY (max). Injuries: **Graze** (−1) · **Wound** (−2, gains a condition) · **Grave** (−3, condition + Bleeding). Rest recovers 1 Vitality per full Watch of safe rest with Food ≥ 3 and Water ≥ 3. Medicine DC 12 accelerates to 2 per Watch (needs supplies).

Conditions: **Bleeding** (−1 Vit per Watch; SCENT +1; Medicine DC 12 to stop) · **Fractured** (−2 Athletics, slows travel ×2) · **Exhausted** (−1 all, forced by RST ≤2 combined with exertion) · **Shaken** (−1 NERVE rolls) · **Gut-Sick** (§1) · **Fever (infection)** — see file 04.

At 0 Vitality the PC is **Down**. An ally can stabilise within 3 rounds (Medicine DC 15) or the PC faces **Final Watch** (file 04 §6).

## 3. Load (encumbrance)

**Slots = 6 + BODY.** A pack adds +2. Over capacity: −1 Athletics and −1 Stealth per slot over.

| Item | Slots |
|------|-------|
| Water, 2 L | 1 |
| Food, 3 Rations | 1 |
| One-handed weapon | 1 |
| Heavy weapon (axe, sledge) | 2 |
| Firearm + 12 rounds | 1 |
| Medical kit (basic) | 1 |
| Tool roll / Parts ×5 | 1 |
| Power bank | 1 per 2 |
| Rope, tarp, bedroll | 1 each |

## 4. Signature: Noise, Light, Scent

The player's current **Signature** has three meters (0–5). Set from what you are *currently doing or carrying*; the highest active source per meter applies, and meters reset when the activity stops.

| Meter | 0 | 1 | 2 | 3 | 4 | 5 |
|-------|---|---|---|---|---|---|
| **NOISE (N)** | sneaking, resting | normal movement indoors, quiet talk | prying a door, normal conversation, hammering | running, breaking glass, boat motor | shouting, car engine, generator | gunshot, alarm, explosion |
| **LIGHT (L)** *(counts only DSK–DEP)* | none | candle, dim phone | flashlight, headlamp | lantern, vehicle lights | open fire | searchlight, flare |
| **SCENT (S)** | none | sweat/unwashed, cooking, minor bleeding | smoke, handling corpses, butchering | heavy bleeding, rotting stores | burning bodies | deliberate chum/lure |

**Handset emission (E):** the device adds to Signature Total: **SILENT 0 · STANDARD +1 · FULL +2** (file 05 §5).

**Signature Total ST = N + L + S + E** (cap 15).

## 5. Zone Heat

Each zone has a **Heat** value 0–10 (the attention of the local Dead). Base Heat per zone is in file 08.

**Per Watch spent in a zone, Heat changes by ST:** 0–1: **−1** · 2–4: **0** · 5–8: **+1** · 9–12: **+2** · 13+: **+3**.
**Spikes (immediate):** gunshot +3 · explosion +4 · alarm +3 · vehicle engine +1 per Watch · shout +1 · generator +1 per Watch. A spike of 3+ also adds **+1 Heat to adjacent zones** (echo).
**Unoccupied zones** drift ±1 per Day toward Base Heat.

| Heat | Tier | What it means |
|------|------|---------------|
| 0–2 | **QUIET** | Singles and strays only |
| 3–5 | **STIRRING** | Patrols; groups possible |
| 6–8 | **DRAWN** | Convergence: a **Pack** (Density + 2 Gutom) arrives in 90 min |
| 9–10 | **SWARM** | Convergence: a **Horde** (Density × 4 + 10) arrives in 30 min |

**Encounter roll per Watch spent outside a secure Hold:** d100 ≤ (Heat × 6 + Density × 4 + any sealed modifiers, file 04 §3) → roll the encounter on file 14 T2 for the current Heat tier. Size by tier: QUIET 1 · STIRRING 1 to Density · DRAWN/SWARM per Convergence.

**Dead Quiet:** if ST ≤ 1 for the whole Convergence window *and* the PC is in a Hold with Concealment ≥ 3 (or hidden in a reasonable cache), the group **passes** without engaging. Otherwise they hit the Hold (see §10).

## 6. Stealth

**Stealth DC = 8 + ST** (cap 21). Add +2 for Hiyaw present, +1 per 5 Gutom beyond the first group, −2 if wind/rain masks (file 14 T4). Failure by Setback means noticed at CLOSE range; Break means noticed at ENGAGED or a Convergence trigger.

## 7. Scavenging and pools

Searchable zones hold **Pools** of five resources: **Food (Rations), Water (litres, packaged), Medical, Parts, Fuel**. Base Pools per zone are in file 08. A Pool is what a lone scavenger can realistically reach; institutional stores (the Compact's market, Command rations, the Tower) are separate and are earned through Standing, labor or trade (file 09).

**Competition tiers.** Other survivors strip the city. The *effective* Pool is:

`Effective Pool = floor(Base × Tier multiplier) − units the PC has already taken there`

| Tier | Days | Multiplier | Zone feel | Scavenge DC modifier |
|------|------|-----------|-----------|----------------------|
| **Rich** | 0–14 | ×1.0 | Untouched shelves, locked rooms | +0 |
| **Picked** | 15–45 | ×0.6 | Cleaned-out lobbies; the good rooms are gone | +1 |
| **Scraped** | 46+ | ×0.35 | Bare shelves, scavenger marks on doors | +2 |

When the multiplier drops, a Pool the PC already drained can fall to 0 at once. Log units taken per zone in the Save Block (`taken`). Nothing else is tracked.

**Reading a Pool.** A Quick look (Scavenge DC 8) or a TALA SCOUT stock estimate (file 05, with its C%) tells you the state: **Plenty** (more than half of this tier's Pool left), **Thin** (some left) or **Bare** (0). A Bare Pool cannot yield; do not roll.

**Scavenge roll.** DC = **9 + zone Density + Tier modifier.** One resource per roll. Time: Task (1 hr).

| Result | Yield (units, taken from the Effective Pool) |
|--------|-----------------------------------------------|
| CLEAN | **3** (Medical **2**), plus a Bonus find: d6 from the tape. 1–3 nothing · 4 +1 unit (if the Pool has it) · 5 a useful item (flavor from file 14 T1) · 6 a lead: +2 to your next Scavenge roll for that resource in that zone |
| COST | **2** (Medical **1**), plus a Cost (file 14 T3) |
| SETBACK | 0; +1 Heat or a complication |
| BREAK | 0; encounter or injury |

Yield can never exceed what is left in the Effective Pool. File 14 T1 says what the units *look like*; it never sets quantities.

**Remisol** is not a Pool resource. Only six vials exist in the Metro (file 04 §5).

## 7b. Renewable food and water

Pools run out, so the long game needs sources that refill. Each has a catch. **Every person eats 2 FOD per Day (about 0.67 Ration), companions included.**

### Water

| Source | Where | Per Short action | Safety |
|--------|-------|------------------|--------|
| **Spring** | Z09 | 6 L | Clean (d100 ≤ 5 → Gut-Sick) |
| **Hand pump / cistern** | Z06, Z10 | 6 L | d100 ≤ 10 → Gut-Sick unless boiled |
| **Taps and tanks** | Z01, Z02, Z04, Z05, Z07 | 4 L (N2) | Boil, or d100 ≤ 30 |
| **Z08 taps** | Z08 | 4 L (N2) | Boil, or d100 ≤ 60 |
| **Rain** | anywhere with a tarp | +1 L per Watch of showers, +2 L per Watch of heavy rain or storm; max 8 L per Day | Clean if the vessel is clean |

Boiling costs 1 hr and 1 Fuel per 4 L (§1).

### Fishing

Shoreline zones: **Z01** (waterfront), **Z03** (east shore), **Z04** (north slips), **Z08** (Heat-limited), **Z11**. Tides allow **two Fishing Tasks per Day (DWN and DSK)**. Roll **HANDS or WITS + Seacraft vs DC 11**, plus Crowding (+1 on D31–60, +2 from D61) and weather (heavy rain +2; storm: no fishing). An improvised line costs 1 Part; a net costs 2 Parts and gives +1.

| Result | Catch (Fish; 2 Fish = 1 Ration) |
|--------|-------|
| CLEAN | 3 |
| COST | 2 |
| SETBACK | 1 |
| BREAK | 0, and a complication (squall, snagged gear, a drone pass) |

Fishing is quiet (N1). Each Task near the cordon (Z03, Z04, Z11) carries **d100 ≤ 15: a drone pass** (Heat +1; at LEASH ≥ 7, Command Attention +1, file 05 §9). **Fresh fish spoil after 1 Day.** Smoking or drying costs a Task and a fire (S2, plus L at night) and turns 6 Fish into 5 Days of keeping.

### Foraging

**Z06, Z09, Z10.** **Wayfinding or Scavenge vs DC 10**, plus Crowding and weather as above (no foraging in a storm). Yield in Rations: CLEAN 2, COST 1, else 0. Each zone's patch has a **Forage Budget of 6 Rations per week (4 from D61)**, shared by everyone and resetting every 7 Days. Fresh greens spoil after 3 Days.

### Gardens

Needs a Hold in **Z06, Z09 or Z10** (Z01 yards possible at the GM's call), 1 Part per plot (seed and tools) and a Task to plant. **Max 3 plots per Hold.** First harvest **21 Days** after planting, then **1 Ration every 2 Days per plot.** Upkeep: **1 L of water per plot per Day** and a Short tend action per Day. **Blight and theft:** each plot, each Day, d100 ≤ 4 → down for 7 Days. A compromised Hold loses its plots.

### Labor for rations

At **Standing ≥ +2** with BAY or CPT, a **Long** labor shift at their kitchens or stalls earns **1 Ration.** Available on about 60% of Days (the GM rolls d100 ≤ 60 once per Day). Every 3 shifts: Standing +1.

### Spoilage

Packaged food keeps. Fresh fish: 1 Day. Cooked leftovers: 1 Day. Fresh greens and ripe fruit: 3 Days. Track perishables in the Save Block (`fresh`); in Lite mode (file 13 §10) they are eaten or lost at the Day boundary.

### Calibration (simulated, not playtested)

90-day food balance, 3,000 runs per row. The PC can reach half of the Metro's Pools and hoards in the Rich tier.

| Party | Sources | Mean hungry days (of 90) | When hunger starts |
|-------|---------|--------------------------|--------------------|
| Solo | Scavenging only | 34 | median Day 57 |
| Solo | Scavenging + labor | 1.7 | rarely |
| Solo | Fishing, or upland (forage + garden) | 0 | never |
| Party of 4 | Scavenging only | 64 | median Day 27 |
| Party of 4 | Fishing | 15.6 | median Day 73 |
| Party of 4 | Fishing + labor | 0.1 | rarely |
| Party of 4 | Upland (forage + garden) | 29.6 | median Day 45 |
| Party of 4 | Upland + labor | 15.0 | median Day 63 |

Reading it: a lone scavenger gets about two months. A group needs a second source by about Day 25. An upland party is safer from the Dead but short on food. Fishing and labor are what actually carry a group, and both cost time, Standing and risk. Not modelled: weather beyond storms, fishing and garden raids beyond the rolls above, and hungry-day consequences (they follow the FOD thresholds in §1).

## 8. Travel & chases

- **On foot:** adjacent-zone costs are in file 08 (in Watches). **Sneaking** doubles the time and reduces N by 2. **Running** halves the time and sets N3.
- **Chase:** track **Distance** 0–5 (0 = grabbed). Each round the PC rolls Athletics vs the fastest pursuer's DC (file 04); win → Distance +1, lose → −1. Breaking line of sight at Distance ≥ 3 ends the chase.
- **Vehicles:** halve travel time, N4 while moving, +1 Heat per zone crossed, 1 Fuel per Watch. Roads may be blocked (file 08); clearing a block is a Task and makes N3.
- **Boats** (Seacraft): quiet at sail/paddle (N1), motor N3; weather per file 14 T4.

## 9. Loob (morale)

Gains: shared meal +1 · helped someone +1 · a victory +1 · rest in a Hold with companions +1/Day · a keepsake/ritual +1/Day · TALA reading Ledger names back to you (if it is honest) +1.
Losses: ally lost −3 · forced cruelty −2 · hunger/thirst Failing −1/Day · long solitude −1/Day · ignored plea for help −1.
**Anchors:** each PC may name 2 Anchors (person, place, object, habit). Honouring one restores +2 once per Day; losing one is a −3 LOB event.

## 10. Holds (bases)

A **Hold** is a claimed location with ratings **Fortification F (0–5)** and **Concealment C (0–5)**; upgrade by spending Parts (+1 F or +1 C per 3 Parts and a Task or Long action, Mechanics DC 12). A Hold shares its zone's Heat.

- **Pack at the door:** if F ≥ 2 the Hold holds; each Pack that engages reduces F by 1 unless the PC defends (file 03 §16).
- **Horde at the door:** requires F ≥ 5 to hold *once*; F drops by 2 afterward. Otherwise evacuate or Dead Quiet.
- **Utilities:** water source, cooking, power each add +1 Loob/Day if secure; each also raises ST during use.
- **Garden:** see §7b (max 3 plots; needs water and tending; lost if the Hold is compromised).
- **Hold Decay:** Heat ≥ 6 for two consecutive Watches means the Hold is **compromised** (−1 F, −1 C). No sanctuary is permanent.

## 11. Power & Parts

- **Parts** (P): generic components used for repairs, Hold upgrades and TALA Protocols.
- **Fuel** (F-unit): 1 per Watch of vehicle driving; 1 per 2 Watches of a generator; 1 per 4 L of boiled water.
- **Power banks:** each full charge restores **+40% battery** to a handset (file 05 §4); recharge via solar (+3% per daylight Watch outdoors, MRN/MID only), vehicle (+10%/Watch), generator (+15%/Watch).

## 12. Weather

Per file 14 T4. Rain: Stealth DC −2, rain collection per §7b, Light visible range halves. Storm: Heat drifts −1 per Watch outdoors but travel DC +2, boats unusable. **Typhoon Dindo (D9–10)** is scheduled (file 11).
