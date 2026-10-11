# 13 — SAVE, LEDGER & ANCHORS

**TIER:** CORE | **DEPENDS:** 00, 01 | **Schema:** TP-SAVE-1.1

---

## 1. Save types

- **HUD** — shown every turn (file 12 §2). It is a view, not the save.
- **Standard Save Block** — printed on `/save` and offered every **3 Days** or after a major event.
- **Restore Anchor** — a full, self-contained block for resuming in a new chat (§5).

The **Save Block** is the single source of truth for current values. Lore never overrides it (file 00 §5).

## 2. Standard Save Block (compact YAML)

```yaml
TP-SAVE-1.1
build: TP-FC1.3.0-20261011
pc: {name, age, origin, callsign, voice_seed: [w1, w2, w3, tic], tone: cinematic, flaw, anchors: [a, b]}
attrs: {BODY, WITS, NERVE, HANDS, VOICE}
skills: {Athletics, Melee, Marksmanship, Stealth, Scavenge, Medicine, Mechanics, Signals, Wayfinding, Seacraft, Persuade, Resolve}
vit: {cur, max}
conditions: []
needs: {WTR, FOD, RST, LOB}
load: {used, cap}
inv: []               # items, qty, durability
sig: {N, L, S, E, ST}
clock: {day, watch, time}
zone: Z05
heat: {}              # only zones changed from Base Heat
taken: {}             # units the PC has taken per zone, e.g. Z05: {F: 6, M: 2}
fresh: []             # perishables: item, units, spoils_on_day
plots: []             # gardens: zone, plots, planted_day, down_until
forage: {}            # zone: Rations used this week
hum_hits: 0           # Hum Hits logged (file 04 §3); sealed
tracking: standard    # standard | lite (file 13 §10)
infection: {status: none|A|B|C|D, dose, turn_time_h, exposed_at, remisol: n}
tala: {mode, battery, leash, attention, backlog_days, modules: [], protocols: [], honest_mode: false, claims_open: [], advisory_log: [], ledger: []}
standing: {FBC: 0, BAY: 0, CPT: 0, TUL: 0, LRS: 0, KFR: 0, PAG: 0}
tiwala: {}            # Name: value
companions: []
clocks: {}            # Name: segs/max
flags: {}
marks: {}             # skill: marks (3 marks = +1 level, max 4)
combat: {}            # Tier 2 only: mom, alarm, grappled, battlefield card
tape: {ptr, pass, seed: 20261010}
patches: []
```

**Loading an older save.** A TP-SAVE-1.0 save loads under 1.1: missing fields default to `taken {}`, `fresh []`, `plots []`, `forage {}`, `hum_hits 0`, `tracking standard`, `attention 0`, `backlog_days 0`. Replace any old `stocks:` entry by converting to `taken` (units removed from a Pool).

## 3. The Mutation Journal (two tiers)

**Tier 1 — Canon (permanent).** Never edited, never discarded. Logged immediately when it occurs:
- Deaths, Turns, disappearances.
- **Locked infection** results (dose, chance roll, Turn Time).
- Flipped secrets (S1–S6).
- Faction clocks filled; Standing changes ≥ 2.
- Locked facts from Late Binding (file 01 §11).
- Major choices (who was saved, who was refused).
- Ending flags.

**Tier 2 — Ephemeral (current scene state).** Needs, positions, scene-level facts, recent TALA claims awaiting verification. Discarded at each Anchor or scene change.

**Journal entry format:** `T1 | D12 DSK | Z05 | <fact> | <ref: T41>`

## 4. Chronology tracker

Keep the last **10** entries in the Save Block: `D<day> <WATCH> hh:mm | zone | action | tape rows used`. Needed for time conservation checks and restores. A full Chronology rolls into the Anchor summary.

## 5. Restore Anchor (`/anchor`)

```
=== TP ANCHOR ===
build: TP-FC1.3.0-20261011 | schema: TP-SAVE-1.1 | anchored: D<day> <WATCH> hh:mm
RECAP (<=120 words, PC voice)
SAVE BLOCK (full, §2)
TIER-1 JOURNAL (all entries, compressed one-line each)
CHRONOLOGY (last 10)
OPEN THREADS (<=5): who wants what by when
NEXT SPINE EVENTS (next 3 from file 11)
=== END ANCHOR ===
```

**Offer a Save Block** (`/save`) every 3 Days. **Offer an Anchor** at every Act boundary, about every 10 Days (roughly 40 turns), after any major death or reveal, and when the degradation protocol requires (§7).

## 6. Restore protocol (new chat)

1. Load the project (Lean Core). Paste the Anchor.
2. Run **SYSTEM CHECK** (`/verify`): build, schema, tape pointer, sealed tags.
3. Print a **RESTORED** summary: clock, zone, vitals, TALA state, next 3 Spine events.
4. Continue from the same clock and tape pointer. Do **not** re-run past rolls.
5. If the Anchor and the lore conflict, the Anchor's *values* win and its facts are canon.

## 7. Context degradation protocol

| Level | Trigger | Action |
|-------|---------|--------|
| **D0** | < 40 turns since last Anchor | Normal operation |
| **D1** | 40–70 turns | Compress older recaps to 2 lines; stop re-quoting lore |
| **D2** | 70–100 turns | Offer an Anchor; re-read file 01 §2 and file 12 §11 |
| **D3** | > 100 turns **or** drift detected | Require an Anchor; recommend a new chat |

**Drift symptoms:** HUD disagrees with Save Block; a gated feature appears early; tape pointer not advancing; register inflation; options start steering; names/dates mismatched. On any symptom, run `/verify`, correct once, and offer an Anchor.

## 8. Patch notes

Mid-campaign fixes go in `patches: []` as `P<n>: <what> | <why>`. Patches never change locked canon.

## 9. TALA ledger fields

Each Ledger entry: `{name, age, zone, condition, seen_at, notes, standing?}`. The PC sees only entries they have registered. The **Selection score** field is sealed until S4 flips; once flipped, it is visible with the formula as revealed.

## 10. Tracking tiers and Lite mode

**Tiers.** Everything the GM tracks falls in one of three tiers. This keeps the HUD readable and the bookkeeping inside what a long session can hold.

| Tier | What | Rule |
|------|------|------|
| **Shown** | Clock, zone, VIT, WTR, FOD, RST, LOB, ST, Heat, TALA mode and battery, PTR | Every turn (HUD) |
| **On change** | N/L/S/E breakdown, conditions, infection phase (if known), companions' states | Print when it changes |
| **Silent** | Standing, Tiwala, faction clocks, `taken`, `hum_hits`, Attention, flags, Tier 2 combat state | Keep in the Save Block; print on `/status` or `/save` |

Combat state (Momentum, Alarm, Grapple, the Battlefield Card) is Tier 2 and is discarded when the fight ends.

**Lite mode (`/lite`).** For play where the full ledger is a drag, or on a phone. Lite keeps every roll, the locked infection schedule, the Spine Clock and Player Sovereignty, and removes:
- **Weapon Durability tracking:** a weapon breaks only on a natural 1 while attacking with it.
- **Combat Fatigue** (file 03 §17).
- **Per-item Load:** the PC is "Light", "Heavy" or "Overloaded" (Overloaded keeps the old over-capacity penalty).
- **Per-Watch need ticks:** needs tick **twice a Day** (at DWN and DSK) for the total the Watches since the last tick would have cost.
- **Perishable tracking:** fresh food is eaten or lost at the Day boundary.

`/lite` can be toggled at any time. Anchors record `tracking: lite`.
