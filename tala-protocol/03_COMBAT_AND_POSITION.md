# 03 — COMBAT & POSITION (v2)

**TIER:** CORE | **DEPENDS:** 01, 02, 04, 05 | **Calibrated:** see §19 (simulated, not yet playtested)

---

## 1. Philosophy

Combat is half of the game's tension, not a punishment for being seen. Stealth and fighting are **two modes of one system**: Noise, Position, Pressure and **Momentum**. A fight is a tactical puzzle with a clock on it: win fast and quietly, hold a good position, or break away. Every swing has Noise; every bite has a locked schedule; running is a legitimate winning move; and a well-played fight should feel **earned**.

Design targets for a typical PC (see §19): a **Skirmish** is a low-risk win; a **Fight** is a real decision with a real chance of a Wound; a **Horde** is a flee-or-hold-a-miracle problem.

## 2. The Battlefield Card

On entering a fight, state a **three-line card** and keep it updated:

```
BATTLEFIELD: Stairwell, 3rd floor. You: CHOKE + HIGH.
FEATURES: door (barricadable) · window (3 m drop) · fire hose
EXITS: stairs down (Gutom) · roof door (locked)
```

## 3. Positions and range bands

**Range bands:** **ENGAGED** (adjacent) · **CLOSE** (≤5 m) · **FAR** (6–25 m) · **OUT** (beyond sight/hearing).

| Tag | Effect |
|-----|--------|
| **OPEN** | up to **4** Gutom may be ENGAGED; −1 Defense |
| **COVER** | +1 vs ranged and thrown |
| **CHOKE** | max **2** ENGAGED; ignore extra Pressure |
| **HIGH** | +1 Melee; unreachable except via stairs/ladder; Noise carries (+1 Heat per Watch if loud) |
| **WATER (deep)** | Gutom cannot follow; −2 Athletics; an item may be lost on a BREAK |
| **INDOORS** | Noise echoes: +1 N |

Declare 2–3 positions on arrival so the player can choose them. **Reposition** is a Minor.

## 4. Threat budget and the Alarm clock

Each Gutom has a **Threat Level (TL)** (file 04 §3): Lakad 1 · Sariwa 2 · Bulok 0.5 · Hiyaw 1. Add them up.

| Total TL | Class | Feel |
|----------|-------|------|
| ≤ 4 | **Skirmish** | Controlled; the PC should win |
| 5–8 | **Fight** | Real risk; position and Momentum matter |
| ≥ 9 | **Set-piece / Horde** | Flee, hold a miracle position, or use the environment |

Convergence groups from file 02 §5: a Pack (Density + 2 Lakad) is a Skirmish or Fight; a Horde (Density × 4 + 10) is always a Set-piece.

**Alarm clock (0–3).** Noise in a fight calls more of them.
- **Round Noise** = weapon N, +1 for Cleave, +1 INDOORS, +1 if the PC shouts. Each round with **Round Noise ≥ 4**: Alarm +1.
- A **gunshot**: Alarm +2 immediately. A **Hiyaw scream**: Alarm +1 and zone Heat +3.
- At **Alarm 3**: a new group (TL = zone Density) arrives next round from the **least-defended band**; Alarm resets to 0.
- Fights at Round Noise ≤ 3 never raise Alarm. Examples: a bolo outdoors (N1), a rebar indoors (N3), a bolo indoors with Cleave (N3). A sledge indoors (N4), or a rebar indoors with Cleave (N4), raises it every round or every Cleave round.

## 5. The round

1. **Update the Battlefield Card.**
2. **PC and allies act.** Each PC turn: **1 Action + 1 Minor**. PCs act first unless **Ambushed** (then the enemy phase runs once first).
3. **Enemy phase:** movement along bands (Lakad close 1 band/round · Sariwa 2 · Bulok 1 per 2 rounds), special actions, then **Pressure** (§8).
4. **Round end:** Alarm check, Fatigue (§17), Momentum carries over.

**Action menu** (offer up to 5 relevant options as a numbered list): **Strike** · **Technique** (spend Momentum) · **Guard** · **Break Free** · **Shove/Control** · **Throw/Shoot** · **Barricade** · **Treat** · **Use item** · **TALA call** · **Hold**.
**Minor:** move one band · draw/switch item · shout a warning · open/close a door · toggle handset mode.

## 6. Attacks

**Attack = d20 + (BODY or HANDS) + Melee** (or **Marksmanship**) vs **Hit DC**.

| Target | Hit DC |
|--------|--------|
| Lakad | **9** |
| Sariwa | **12** |
| Bulok | **7** |
| Hiyaw | **11** |
| Human | see §12 |

| Result | Outcome |
|--------|---------|
| **CLEAN** | One kill; **+1 Momentum**; no weapon wear |
| **COST** | One kill; weapon Durability −1 **or** N +1 (player chooses) |
| **SETBACK** | Miss; the target stays |
| **BREAK** | Miss and **Grappled** (if already Grappled: **Bite check**) |

**Mop-up.** When **≤ 2** Gutom remain, none Grappled, and the PC holds COVER, CHOKE or HIGH: one roll resolves it. CLEAN: all down. COST: all down, Durability −1 or N +1. SETBACK: one remains, play a round. BREAK: Grappled.

## 7. Momentum and techniques

**Momentum (MOM 0–5).** Gain **+1** on a CLEAN attack or when Guard beats Pressure by 5 or more. Lose it all at the end of the fight, and when you take a Bite check. **Cap 5** (6 with Melee or Marksmanship 3).

**Core techniques (everyone):**

| Technique | Cost | Effect |
|-----------|------|--------|
| **Cleave** | 1 | On a successful Strike with ≥ 2 ENGAGED, kill **two** (Lakad/Bulok only); N +1 |
| **Break Grip** | 1 | **Reactive:** cancel one Grapple escalation or Bite check this round |
| **Shove Line** | 1 | Push all ENGAGED to CLOSE; no Pressure this round (Athletics DC 12) |
| **Quiet Finish** | 1 | Kill an **unaware or Grappled** target at **N0** |
| **Second Wind** | 2 | Ignore one Wound penalty for this fight |

**Weapon signatures** (cost shown). You know the signature of the weapon type you wield. At Melee or Marksmanship 3 you also choose **one extra signature from any weapon type**, usable with whatever you wield:

| Weapon | Signature | Cost | Effect |
|--------|-----------|------|--------|
| Knife / bolo | **Cut and Slip** | 0 vs Grappled/unaware; else 1 | Quiet Finish becomes cheaper; Reposition as a free Minor after a kill |
| Spear / pole | **Reach Strike** | 1 | Attack from CLOSE with no Pressure exposure this round |
| Rebar / pipe | **Smash** | 1 | Kill one and stagger all ENGAGED (no Pressure this round) |
| Axe / sledge | **Drop the Hammer** | 2 | Kill up to two ENGAGED and knock the rest prone (lose their next move) |
| Bow / crossbow | **Aimed Shot** | 1 | Ignore cover/range penalties; +2 vs Hiyaw at FAR |

*Shove Line, Quiet Finish, Second Wind and the weapon signatures are not yet simulated.*

## 8. Pressure, Grapple, Bite

At the end of each round, if any Gutom are ENGAGED, the PC rolls **Defense**:

**d20 + BODY + Athletics vs DC 8 + n** (n = Gutom ENGAGED). **Grappled** gives −2. **CHOKE/HIGH** cap n at 2.

1. **First failure → Grappled.** No infection yet. −2 to Strikes and Defense until freed. Fiction: a hand on your sleeve, a grip on a jacket.
2. **Break Free** (Action): Athletics (d20 + BODY + Athletics) DC 12. An ally may pull you free as their Action.
3. **Failure while Grappled → Bite check** (unless **Break Grip** is spent).

**Bite check:** roll **d6** for location, then follow the locked infection schedule (file 04 §4).

| d6 | Location | Dose |
|----|----------|------|
| 1–2 | Leg/lower body | D3 |
| 3 | Hand/forearm | D3 |
| 4 | Back/torso | D4 |
| 5 | Neck/head | D4 |
| 6 | Shoulder/upper arm | D3 |

A bite also causes a **Wound** (−2 Vit) unless the location is covered by **Layer 2 or more**.

## 9. Guard and Layers

**Guard** (Action): **+3 to Defense** this round; if Defense wins by 5 or more, **+1 Momentum**. You cannot Strike. Doubles as bracing behind COVER.

**Layers (armor).** Wear before the fight. Each Layer lowers a bite's Dose by one level for the covered location, **max two levels**. D4 → D3 → D2 means Dose chance falls from 100% to 85% to 30%.

| Layer | Examples | Cost |
|-------|----------|------|
| **1** | Thick jacket, jeans, leather gloves | None |
| **2** | Padding (magazines, foam, bike guards), shin/forearm guards | −1 Athletics; WTR −1 extra per 2 Watches in heat |
| **3** | Helmet, vest, neck guard | −1 Athletics, +1 slot, and Stealth −1 |

A neck needs its own guard (scarf or collar guard) to count as covered.

## 10. How the Gutom fight (tactics)

- **Lakad:** advance by the shortest path to the loudest, then warmest, then smelliest target; grab the nearest.
- **Sariwa:** sprint; ignore low obstacles; **CHOKE caps at 3 ENGAGED instead of 2**; will flank.
- **Bulok:** slow; **Spore Bloom** when broken indoors (file 04 §3).
- **Hiyaw:** screams at the end of its first free round (Alarm +1, Heat +3) unless killed or blocked; **priority target**.
- **Buhol (a knot of 30–200):** if N ≥ 4 occurs within CLOSE of the building, it releases a **Horde** in 2 rounds.

## 11. Weapons

| Weapon | Reach | N | Durability | Slots |
|--------|-------|---|-----------|-------|
| Kitchen knife | Engaged | 0 | 3 | 1 |
| Bolo/machete | Engaged | 1 | 5 | 1 |
| Rebar/pipe | Engaged | 2 | 8 | 1 |
| Fire axe | Engaged | 2 | 6 | 2 |
| Crowbar | Engaged | 2 | 7 | 1 |
| Spear/long pole | Close | 1 | 4 | 2 |
| Sledge | Engaged | 3 | 6 | 2 |
| Bow/crossbow | Far | 1 | 6 | 2 |

At Durability 0 a weapon breaks. **Mechanics DC 12** (Task) jury-rigs **+2 Durability** once. **Sharpen/true** (Task, 1 Part): restore **1 Durability up to max − 1**.
**Heavy weapons (fire axe, sledge) get +1 to Strike** against Lakad and Bulok (not Sariwa or Hiyaw). Their Noise makes them risky indoors, since INDOORS adds +1 to Round Noise. The calibration in §19 assumes no such bonus.

Firearms: **N5**, Alarm +2 per shot, Heat +3, **12-round** typical loads, no resupply except Pool finds. Marksmanship DC: FAR 12, CLOSE 10, ENGAGED 12. A gun is a **tool, not a solution**: one kill per shot, and everything within earshot comes.

## 12. Humans in combat

Humans use a **Contest**: your approach roll vs **Threat × 3 + 6**. Each group has **Threat (1–5), Morale (1–5), Arms**.
- **Morale** drops 1 for each ally down, each Guard that beats them, and any unanswered threat. At **0**: they **flee, parley, or surrender**.
- **Break their nerve:** Intimidate or Parley (VOICE + Persuade vs Morale × 3 + 6); **Disarm** (HANDS + Melee); **Hold** a hostage.
- Faction styles: **Tulisan**: ambush, hit-and-run, steal and flee (Morale 3). **FBC**: disciplined, drones, compliance first then lethal (Morale 4). **LRS**: defensive, batons, tasers (Morale 3). **Pagsibol**: fanatic, mostly melee (Morale 5, unarmed or crude weapons).
- Killing humans: **LOB −2** unless clearly defensive; Standing shifts with the group.

## 13. Companions in combat

Each companion has a **Role** and **one assist per round**:
- **Anchor:** reduces your ENGAGED count for Pressure by 1 while adjacent.
- **Striker:** one free attack roll per round at their own bonus, no Momentum.
- **Medic:** Treat becomes a Minor.
- **Eyes:** calls flanks and Hiyaw; **+1 Defense** to the PC for the round.

When a companion is ENGAGED and not covered, roll **one Companion Check** per round: d20 + 5 vs DC 8 + n. First failure: Wound. Second: Bite check (GM rolls from the tape). **Pogi:** can **Draw** one Gutom away for a round by barking (N4, risk of harm).

## 14. Environment features

| Feature | Effect |
|---------|--------|
| **Door** | Barricade (Mechanics DC 12): creates CHOKE; holds 3 rounds |
| **Stairs** | CHOKE + HIGH |
| **Vehicle** | COVER; starting it is N4 |
| **Deep water** | Gutom cannot follow; see §3 |
| **Fire** | Clears a closed room; L4 S4; risk to Hold (compromise −1 F) |
| **Rope/ladder** | Cut it to stop pursuit |
| **Glass** | Crossing it: N +1 |
| **Live wire + puddle (storm)** | Mechanics DC 15 to trigger; kills a group; N3 |

## 15. TALA in combat

**TALA call** (Minor, 2% battery, STANDARD or FULL): reveals one unseen threat or flank at C% (file 05 §7); if correct, **+1 Defense** this round. **TRIAGE** can treat in-fight at Medicine −2. Toggling to **SILENT** is a Minor and drops Emission to 0 (file 05 §5).

## 16. Defending a Hold

Treat the breach point as **CHOKE** if the Hold has **F ≥ 2**. Each wave is a Fight at the breach. Each Pack that engages costs **F −1** unless defended. A Horde needs **F ≥ 5** to hold *once* (file 02 §10). A Task of barricade repair gives **+1 F** temporarily until the next Convergence.

## 17. Fatigue

After **round 5**, apply **−1 cumulative** to all combat rolls for every 2 rounds (rounds 6–7: −1; 8–9: −2). Long fights are won by position, not by endurance.

## 18. Aftermath and growth

- **Record:** Durability, Wounds, Momentum cleared, **Aftermath Heat** (+1 if any round's Round Noise was 3 or more; gunshots as per file 02 §5), Scent (corpses S2 for a Watch), exposure events.
- **Combat Hangover:** after any fight that reached R4, **LOB −1** unless a **Debrief** (Short action) with a companion or TALA reading Ledger names.
- **Marks:** a skill earns a **Mark** for a notable, risky or clever use (GM awards, max 1 per skill per Day). **3 Marks → +1 skill level** (max 4). There is no XP for kills.
- **Skill 3+:** +1 Momentum cap and a second weapon signature. **Skill 4:** one technique per fight costs 1 less (min 1).

## 19. Calibration data (simulated, not playtested)

6,000 simulated fights per cell. "Smart" play: Cleave when two Lakad are engaged, Break Grip to absorb a bite, Break Free when Grappled. Lakad (Hit DC 9) and Sariwa (Hit DC 12) mixes, with Pressure, Fatigue, the Alarm clock and reinforcements (3 Lakad per Alarm 3). Typical PC: BODY 3, Melee 2, Athletics 1. Strong PC: BODY 4, Melee 3, Athletics 2. **P(at least one Bite check):**

| PC · position · Round Noise | 3 Lakad | 3L + 1 Sariwa | 5 Lakad | 5L + 2S | 7L + 2S |
|-----------------------------|---------|---------------|---------|---------|---------|
| Typical · open · N1 (bolo outdoors) | 9% | 21% | 20% | 50% | 68% |
| Typical · open · N3 (rebar indoors) | 9% | 21% | 21% | 49% | 73% |
| Typical · open · N4 (sledge indoors) | 45% | 78% | 84% | 94% | 95% |
| Typical · choke · N1 | 8% | 18% | 15% | 43% | 59% |
| Strong · open · N1 | 3% | 6% | 6% | 14% | 24% |
| Strong · open · N4 | 17% | 40% | 48% | 67% | 72% |
| Strong · choke · N1 | 3% | 4% | 4% | 10% | 17% |

Threat classes (§4): 3 Lakad is TL 3 (Skirmish). 3L + 1S and 5 Lakad are TL 5 (Fight). 5L + 2S is TL 9 and 7L + 2S is TL 11 (Set-pieces). Mean rounds, typical PC in the open at N1: 3.8 · 6.4 · 7.2 · 14.0 · 16.7.

**Reading it**
- Quiet play (N1) and indoor play with a moderate weapon (N3) look almost the same: reinforcements rarely arrive. A typical PC has about one chance in ten against three Lakad, about one in five in a Fight, and a coin flip at TL 9.
- Loud play (Round Noise 4 every round: a sledge indoors, a vehicle, constant shouting) is a different fight. Reinforcements arrive in about 6 of 10 three-Lakad fights and in every larger one, which takes a typical PC from 9% to 45% against three Lakad. Heavy weapons belong on open ground.
- A strong build stays safe in Skirmishes and Fights if it stays quiet (3–6%). Its pressure comes from Sariwa mixes, Set-pieces, noise, Fatigue, Hiyaw and Heat, not from Lakad.
- Weak build (BODY 2, Melee 1, Athletics 0), quiet, Lakad only (earlier run): 23% against three and 47% against five in the open.
- Naive play (Strike every round, no techniques), typical PC, Lakad only (earlier run): 24% against three and 61% against five. Momentum and position are the difference.
- Under the v1 rules a typical PC faced 64% against three and 93% against five.

**Not modelled:** Wounds, Durability, Hiyaw, human fights, Mop-up, Shove Line, Quiet Finish, Second Wind, weapon signatures, and the heavy-weapon +1. Treat these as untested.

**Tape cost:** about 3 rows per round. The 720-row tape covers roughly 240 rounds if nothing else rolls; follow the wrap rule (file 15).

## 20. Combat round format (phone-friendly)

Each combat round: **~100–180 words of prose** (cinematic, one beat per round; **one slow-motion beat per fight, R4 only**), roll notices, a **combat HUD**, and **3–5 numbered tactical options**.

```
ROUND 2 | MOM 2 | ENGAGED 2 · CLOSE 3 · FAR 0 | ALARM 1/3 | GRAPPLED no
VIT 6/7 | N3 · HEAT 5 | TALA STD 61% | PTR 74
```

*Options:*
1) Strike the nearest [Melee]
2) Cleave [1 MOM]: take two
3) Guard: brace and read them
4) Fall back to the stairwell (CHOKE) [Minor + Action]
5) Shove Line [1 MOM, Athletics DC 12]
0) Free action

**Example round (original):**
The bolo caught the first one under the jaw, and it folded onto the landing.
Two more. One had my sleeve already.
`d20[T88]=17 +BODY3 +Melee2 =22 vs DC9 → CLEAN`
Momentum clicked up a notch. I did not have time to be proud about it.
`TALA // SCOUT // C79 // SNS: Third group on the stairs. Eight seconds.`
Eight seconds. Lovely.

## 21. Set-piece templates

- **Stairwell Hold** (TL 6): CHOKE + HIGH; goal: hold 5 rounds while an ally cuts a line. Alarm climbs from round 2.
- **Bridge Gate Crush** (humans + Lakad): crowd Morale, Threat 3; N is constant; goal: clear a lane without a bite.
- **Hiyaw Hunt** (TL 3 + Hiyaw): kill within 2 rounds or Alarm 3; open ground, no cover.
- **Buhol Break** (Horde on a 2-round timer): do not fight it; use environment, water or a door.
- **Tulisan Ambush** (Threat 3, Morale 3): they steal and flee; break Morale by round 3.
