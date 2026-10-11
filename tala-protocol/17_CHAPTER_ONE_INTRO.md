# 17 — CHAPTER ONE (THE INTRO)

**TIER:** REF (read at boot) | **DEPENDS:** 01, 05, 06, 07, 08, 12, 16

---

## 1. What it is, and when it runs

Chapter 1 is the opening chapter of every campaign. In the PC's own voice it introduces the world, the PC, TALA and the situation, using public information only, and it ends on the Origin's Day 0 opener (file 16) so that play starts in the middle of a scene.

- **It runs once, automatically,** the moment character creation finishes (file 06 §8): sheet confirmed → Chapter 1 → HUD and options → the player's first action. The player never has to ask for it.
- **It does not re-run.** Once delivered, the Save Block carries `flags: {ch1: done}` (file 13 §2). A Restore Anchor with `ch1: done` resumes play without it. Where there is a file system, an existing `saves/chapter_1.md` also counts as delivered, even before the first Save Block is written.
- **`/intro`** reprints movements I–III on request (§7). It is text only: no state change and no tape rows.
- **Legacy Continuation** (file 06 §6) runs the short LEGACY mode (§7), not the full chapter.
- In Claude Code the `chapter-one` skill (`.claude/skills/chapter-one/SKILL.md`) carries this file out. In a Claude Project, follow this file directly.

This is the one place the GM presents lore the player has not asked for (file 00 §6 normally forbids it). That is why §3 limits what may appear.

## 2. Inputs

Read these and nothing else. Do not open files 10 or 11 for this chapter.

| Need | Source |
|------|--------|
| Name, age, Origin (or the template a custom Origin was mapped to), start zone and time, gear, companions | The confirmed sheet |
| Anchors, Flaws, Voice Seed, TALA call-sign, tone, language mode | The sheet |
| The PC's past | The player's own words at creation. Nothing added |
| The Origin's hook and contact | File 06 §3, the Origin's entry |
| Start, beat, NPC, Pressure clock, options | File 16 §2, the Origin's opener |
| The world before Day 0 | File 07: lines tagged `[PUBLIC]`, and the date, weather and mood line in §4 |
| The place | File 08: zone and district names, and the **first sentence** of the start zone's entry. Skip the Fields table and every other field of the entry ("Controlled by", "Hazards", "Notes") |
| TALA | File 05 §1, §2, §6 and §10 |
| Style | File 12, including §12 in CINEMATIC |

## 3. Disclosure rules

At the start the PC knows what an ordinary resident of Metro Cebu knows on a Friday evening, plus their own life. Nothing has happened yet.

**May appear**
1. The sheet, in plain language. "Steady hands" and "a good eye", never numbers.
2. File 07 `[PUBLIC]` history and the Day 0 date, weather and mood. **At most three historical facts** in the whole chapter, a clause each.
3. Zone and district names, and the first sentence of the start zone's entry (file 08).
4. TALA as an ordinary owner knows it: a civil-resilience AI on a Bantay handset; its name means both *star* and *list*; what it can do on Day 0 (TRIAGE, SCOUT, SIGNAL, COACH and its own LEDGER); that it says how sure it is; its voice (file 05 §10).
5. Institutions as a resident knows them: the barangay and its tanod, the Bayanihan Mesh as a neighbourhood handset network, Firebreak Command as the joint civil–military disaster chain (file 07 §2). Only if the Origin's opener already names them.
6. The Origin's own hook, contact and opener beats (files 06, 16), as written for the opening scene.
7. Sensory colour the GM invents (smells, sounds, street names, a dish) that creates no ability, relationship, secret or plot fact. The player may veto any of it; log a veto in `patches` (file 13 §8).

**Never appear** (narration, TALA lines, options, the how-to block)
- Any `[SEALED:S#]` content or what it implies. Anything in files 09, 10 or 11 beyond item 5. Who built what, who knew what, what any institution intends, why anything is happening.
- Any event, date or rumour later than the Origin's start time, except the opener's own scheduled beats as written in file 16 and its TALA line. No Spine Clock, no ninety-day frame, no endings.
- Infection details: no name for the infected, no medical terms, no Dose or Turn Time. A siren is only a siren.
- TALA's directives, Leash, check-ins, Command Attention, Emission or what the mesh does. TALA appears as the PC experiences it.
- Engine numbers: stats, DCs, Heat, Density, Pools, mesh bars, Standing, Tiwala, tape values. Only the HUD and TALA's C% show numbers.
- The story's theme or central question stated outright. Atmosphere motifs (counting, rice and rain, tide lines, handwritten names) may appear, **at most two**, and are never explained.
- Choices, speech or conclusions written for the PC (file 01 §10).
- Additions to the PC's past: no events, people, injuries, motives or secrets beyond what the player said (file 01 §7). If the backstory is thin, show the Origin's ordinary routine instead.

## 4. Structure

| Part | Heading | Budget | Job |
|------|---------|-------:|-----|
| Card | `CHAPTER 1 · <Title>` and a dateline `<weekday, date> · <place>` | 2 lines | The title is two to four words drawn from the PC (an Anchor, an object, the Hook) or the default *The Last Normal Evening*. Never from a secret |
| I | The City | 120–170 words | The ordinary world: place, weather, crowd, mood. At most three `[PUBLIC]` facts |
| II | You | 170–240 | Who the PC is: name, age, how they live, the Anchors, each Flaw shown in one small moment, the Voice Seed in the inner voice, skills as texture |
| III | The Handset | 120–170 | TALA: what it is, how it speaks, what it calls the PC, how it gives confidence. One greeting line from TALA that makes no claim about hidden state |
| IV | The Origin's evening | ≤ 220 | The Day 0 opener (file 16 §1): start, beat, the Origin's NPC, ending on the Pressure-clock hook. Then TALA's opening claim |
| After | HUD, options, how-to | | HUD (file 12 §2), four numbered options plus `0) Free action` (file 01 §13), then the one-time how-to block (§5) |

Whole chapter: **about 700 words, hard cap 900.** Phone first: paragraphs of three sentences or fewer. Movement headings are a roman numeral and two or three words, with no other formatting.

## 5. Writing it

- **Voice.** First person, past tense, the PC's voice (file 12 §3). In CINEMATIC (the default) use the Light Novel Style Pack (file 12 §12) with the Voice Seed: **at most two inner-voice lines per movement**, each on its own line, and the inner voice never commits to an action. In GROUNDED, drop the inner voice and the jokes and keep the same facts in a plain register.
- **Register.** R1 for I–III, up to R2 in IV. The anti-pattern caps (file 12 §6) apply to each movement as if it were a scene. Rotate the lead sense and give every movement at least two non-visual senses.
- **Humour and tenderness.** One comic or tender beat per movement.
- **Backstory fidelity.** Use the player's own words for the past. Keep the PC's feelings to what the player chose (Anchors, Flaws, Voice Seed). Do not judge the PC's past choices beyond how the player framed them.
- **Show, don't list.** Anchors and Flaws appear in action (a stranger recognises the PC; someone is holding on), not as a list.
- **Language.** English only unless `/lang` changed it (file 12 §10). Local terms stand as nouns with context.
- **The hook.** The last line of IV is a hook tied to real state: the Pressure clock, or TALA's claim awaiting proof (file 12 §12.4).
- **How-to block (one time).** After the options, one italic block of at most 60 words, outside the fiction: how to choose (a number, or type your own action), the commands that matter early (`/status`, `/inv`, `/tala`, `/map`, `/save`) and the dials (`/tone grounded`, `/lite`, `/intro`).

## 6. State, dice and logging

- **Dice.** Chapter 1 uses **at most one tape row**: the hidden d100 for the opener's TALA claim (file 05 §7, file 15). Compute C from the source tag, show the roll as `[hidden roll T<row>]`, and log `{claim, C, roll, result}` in `tala.claims_open` with the result hidden until verified. No other rolls. A replay never rolls, and a regenerated chapter reuses the locked claim and its row.
- **Clock.** Movements I–III take no game time. IV sets the clock to the Origin's start time (for example `D0 NGT 20:30`).
- **Save Block.** Set `flags.ch1: done`. Set `tala: {mode: STANDARD, battery: 80, leash: 8, attention: 0}` unless the sheet says otherwise. `clock`, `zone` and `tape.ptr` stay as the chapter left them.
- **Journal.** One Tier 1 line: `T1 | D0 <WATCH> hh:mm | <zone> | Chapter 1 delivered; opening TALA claim locked | <ref: T<row>>`.
- **Chronology.** First entry: start time, zone, tape rows used.
- **File system available** (Claude Code): save the delivered text to `saves/chapter_1.md`. `/intro` reprints it.

## 7. Modes

| Mode | When | What changes |
|------|------|--------------|
| **FULL** | New game | Everything above |
| **LEAN** | `/lean` is on | Each of I–III becomes two or three sentences. IV and the handoff are unchanged |
| **LEGACY** | Legacy Continuation (file 06 §6) | Titled `Interlude · <name>`. Replace I with one paragraph on the city *now*, using only Tier 1 Journal facts the new PC could know. II is compact (150 words). III appears only if the new PC has a different handset or a changed relationship with TALA. IV is whatever scene the continuation opens on. At most 500 words. No tape rows |
| **REPLAY** | `/intro` | Print I–III from `saves/chapter_1.md` or the chat, verbatim. No state change, no roll notice, no options |

## 8. Pre-send check (silent)

- [ ] Every proper noun and fact traces to the sheet, the player's words, a `[PUBLIC]` line in file 07, the start zone's first sentence, file 06 or 16, or file 05. Delete anything else.
- [ ] No engine numbers outside the HUD and TALA's C%.
- [ ] Nothing the PC could not know at the start time. No future event. Nothing sealed or implied by a sealed block.
- [ ] No choice, speech or conclusion written for the PC. The inner voice does not commit.
- [ ] At most three historical facts and at most two atmosphere motifs.
- [ ] Word budgets met (§4). IV is 220 words or fewer.
- [ ] One C% claim, one tape row, `ch1` flag set.
- [ ] The hook corresponds to a real clock or claim.
- [ ] Options include a low-Signature choice, a TALA consult and one that pays a visible cost for information (file 01 §13).

## 9. Failure modes

1. **Lore dump.** The chapter turns into a history lesson. Cap the facts and keep them in the PC's voice.
2. **Spoilers by implication.** An ominous line that only makes sense if you know a secret. Cut it. Atmosphere must work for a reader who knows nothing.
3. **Backstory drift.** The GM adds drama to the PC's past. Stay with the player's words.
4. **A second roll.** A replay or regeneration that re-rolls the TALA claim. A claim is locked once rolled.
5. **Running again after a load.** Check `ch1` first.
