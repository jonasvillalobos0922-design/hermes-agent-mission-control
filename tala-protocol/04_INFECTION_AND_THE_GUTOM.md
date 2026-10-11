# 04 — INFECTION & THE GUTOM

**TIER:** CORE | **DEPENDS:** 01, 02, 03

---

## 1. The pathogen (public view)

Officially "HV-7 neurotropic infection." Survivors call the infected **Gutom** ("the hungry"). It spreads via bites, deep scratches and infected fluid in open wounds or mucous membranes. It is not airborne in life; Bulok spore blooms (§3) are a late exception. There is **no cure** in Acts I–II. What exists is delay (Remisol) and prevention (washing).

`[SEALED:S1]` The pathogen is a viral vector from Lumina's "Project Buhay" neuro-regenerative trial. It hijacks brainstem motor patterns after death and drives a persistent hunting drive. Lumina's suppressed risk memo was flagged by TALA 11 days before Day 0.

## 2. Exposure Dose

| Dose | Event | Infection chance |
|------|-------|-----------------|
| **D4** | Deep bite to neck, head, torso, back | 100% |
| **D3** | Bite to a limb, shoulder, hand | 85% |
| **D2** | Scratch, or infected fluid into an open wound/eye/mouth | 30% |
| **D1** | Brief splash on intact skin, brief contact | 8% |

**Wash Window:** thorough irrigation within **1 Watch** (Medicine DC 12; TRIAGE assist per file 05 §6) reduces the Dose by **one level** (D4 cannot be reduced).

## 3. The Gutom (field classes)

| Class | Hit DC | TL | Speed | Senses (H/Sg/Sm) | Notes |
|-------|--------|----|-------|-------------------|-------|
| **Sariwa** (fresh, 0–72 h after Turn) | 12 | 2 | fast | 3/3/2 | Dangerous; rare after Day 7 *except* newly Turned people |
| **Lakad** (standard) | 9 | 1 | slow | 3/1/2 | The default; relentless, not clever |
| **Bulok** (rotted; Day 45+) | 7 | 0.5 | very slow | 2/0/3 | Brittle; **Spore Bloom** if broken indoors: S+2 for the scene, and D1 inhalation exposure unless masked |
| **Hiyaw** (shriekers; Day 14+) | 11 | 1 | slow | 3/3/3 | Screams: +3 Heat per scream; priority target; rare |
| **Buhol** (the Knot) | — | zone | stationary | 3/0/1 | A packed knot of 30–200 Gutom in a building; a **location hazard**, not a creature |

Senses are ratings used qualitatively: higher means that Signature channel carries farther. Sariwa degrade into Lakad 72 hours after Turning.

**Street names (Cebuano, approximate; verify with a Cebuano speaker before heavy use):** Lakad = *Naglakaw* ("the walkers"), Sariwa = *Presko*, Bulok = *Madunot*, Hiyaw = *Singgit*, Buhol = *Higot*. Command and the mesh use the official names above. Locals mix both.

`[SEALED:S2]` Gutom with damaged hearing respond to the **mesh sync pulse** of Bantay handsets in STANDARD/FULL mode. That is why handset emission counts in Signature (file 02 §4). The Hum is the network's own heartbeat. The player may discover this in Act II.

`[SEALED:S2]` **Hum Pull rule:** while the handset's Emission E ≥ 1, add **+5 to the Encounter roll per point of E** (file 02 §5). When an encounter triggers only because of that bonus (the d100 landed in the margin above the unmodified chance), log a **Hum Hit** (`hum_hits` in the Save Block). At **3 Hum Hits**, a Signals DC 15 analysis (Long action) flips S2. HIMBING (file 05 §8) lowers E, and so lowers the bonus. Never tell the player a roll landed in the margin; show the encounter, not the arithmetic.

## 4. Locked infection schedule

When an infection check is required:
1. Roll d100 from the tape. If ≤ chance for the Dose → **infected**; otherwise **clear** (log both outcomes).
2. If infected, roll **d6** from the tape **once** to lock the **Turn Time** and record it in the Mutation Journal Tier 1. **Never reroll.**

| Dose | Turn Time (hours after exposure) |
|------|-----------------------------------|
| D4 | 4 + d6 |
| D3 | 12 + 3 × d6 |
| D2 | 24 + 6 × d6 |
| D1 | 48 + 12 × d6 |

The GM may not adjust the schedule for drama. Remisol is the only legal modifier (§5).

## 5. Phases and delay

| Phase | Portion of Turn Time | Effects |
|-------|---------------------|---------|
| **A — Warm** | 0–40% | No symptoms. TALA FULL Scan may flag a thermal anomaly after 25% (see §7) |
| **B — Fever** | 40–80% | −1 all rolls; chills, sweats; Scent +1 |
| **C — Lucid Decline** | 80–100% | −2 all rolls; tremor, hallucination; **Resolve DC 12** each Watch or the PC acts on a Gutom-like impulse (GM offers consequences, the player chooses) |
| **D — Turn** | 100% | The PC cannot act normally; **Final Watch** (§6) |

**Remisol** (antiviral suppressant): one dose adds **+2d6 hours** to the locked Turn Time (roll from tape once); a second dose adds only **half**; a third has no effect. **Only six vials exist in the Metro:** two with Aileen Soriano (if recruited), two in the Annex pharmacy in Z08 (a CLEAN Medical result with a natural d20 of 15 or more while that Pool still has units; one vial per find), and two in Dr. Lumbre's Tower lab (gated, file 10). Log each find in the Journal.

**Concealment:** an infected NPC or PC who hides it rolls **Resolve** vs the observer's Medicine/Wits; discovery at Fever or later is automatic.

## 6. Final Watch

When the PC reaches Phase D (or is Down with no help), play a short **Final Watch** scene instead of ending the game.
- The PC has **up to 3 actions or exchanges** before the end: speak, leave something behind, give an instruction, make one last choice for the people they are with.
- No method detail of self-harm is written; keep it dignified and brief.
- Afterwards, the **Legacy Continuation** rule applies: play continues as another survivor from the Ledger (file 06 §6). The first PC's final actions are logged as Tier 1 history.

## 7. TALA and infection

- **TRIAGE** reports a risk number for any open wound (C% per file 05).
- **FULL Scan** (battery −10%, ST +2): thermographic check of a person. Detects Phase A at 25%+ with C = 70, Phase B at C = 90.
- **Bantay-Sakit Protocol** (upgrade) improves Phase A detection to C = 85 from 10%.
- TALA never reveals the locked Turn Time number. It may provide a window estimate (±1 Watch) at C ≤ 80.

## 8. Companions and NPCs

Infected NPCs follow the same schedule; their Turn Time is locked at exposure and **hidden from the player**. A concealing companion is a dilemma generator: report, isolate, ask, or bargain. Decisions are always the player's.

`[SEALED:S5]` **Dok Willy** (file 10) was bitten (D3) 40+ days before the PC meets him and has never turned. He is a **Silent Carrier**. His blood is the key to the counter-vector in Lumina Tower.

## 9. Corpse handling and Bulok

Disposing of a Lakad corpse: Task, N2, S2. Burning: S4 and L4. Bulok broken indoors: Spore Bloom (above). Masks reduce Bloom exposure to nothing; improvised masks (wet cloth) reduce it to D1 at 5%.
