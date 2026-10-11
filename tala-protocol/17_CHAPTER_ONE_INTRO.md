# 17 — CHAPTER ONE (THE INTRO)

**TIER:** REF (read at boot) | **DEPENDS:** 01, 05, 06, 07, 08, 12, 16

---

## 1. What it is, and when it runs

Chapter 1 is the opening chapter of every campaign. It reads like the first pages of a light novel: one scene, in the PC's own voice, that shows the world, the PC and TALA through what is happening, using public information only. It ends on the Origin's Day 0 opener (file 16) so that play starts in the middle of the scene.

- **It runs once, automatically,** the moment character creation finishes (file 06 §8): sheet confirmed → Chapter 1 → HUD and options → the player's first action. The player never has to ask for it.
- **It does not re-run.** Once delivered, the Save Block carries `flags: {ch1: done}` (file 13 §2). A Restore Anchor with `ch1: done` resumes play without it. Where there is a file system, an existing `saves/chapter_1.md` also counts as delivered, even before the first Save Block is written.
- **`/intro`** reprints the saved chapter on request (§7). It is text only: no state change and no tape rows.
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
- Choices, speech or conclusions written for the PC (file 01 §10). NPCs talk; the PC reacts in reflex and thought.
- Additions to the PC's past: no events, people, injuries, motives or secrets beyond what the player said (file 01 §7). If the backstory is thin, show the Origin's ordinary routine instead.

## 4. Shape: a story, not a briefing

Chapter 1 is **one continuous scene** with a title card (`CHAPTER 1 · <Title>` and a dateline) and nothing else: no section headings, no labelled parts, no "the world / you / the handset" blocks. A briefing, however well written, is a draft. Write the first pages of a book.

How stories open, and how this one must:
1. **Hook first.** The first line is a specific, odd or funny thing in the PC's voice, tied to something real in the scene. Never a weather report, a date as prose, or "My name is".
2. **Already in motion.** Begin inside the Origin's evening at its start time (file 16), mid-action or mid-argument. Anything earlier arrives as a glimpse, a line of dialogue or a thought, in the middle of the scene, never as a block.
3. **World through things and people.** Place, weather, crowd and the recent past surface through what is on the table, what is on the radio, what someone says. The three `[PUBLIC]` facts are each a clause inside the scene.
4. **The PC through friction.** Anchors, Flaws and skills show in how the PC reacts to the people present. The Voice Seed colours every line. The backstory is a glimpse, never a biography paragraph.
5. **TALA as a character,** with a manner, a habit and a joke, not a feature list. It appears because the evening gives it a reason.
6. **One small want, then a turn.** The PC wants something immediate and ordinary (to get through dinner). The evening then bends toward the Origin's Pressure clock. The scene ends on the bend: a sound, a line, a countdown.

**Length.** About 750 words, hard cap 900. Paragraphs of three sentences or fewer. Dialogue-forward: speech should be a real share of the lines. The stretch that plays the Origin's opener beats (file 16 §1) closes the scene, and it still follows that file: first contact stays unrevealed, the last line is a hook tied to the Pressure clock or TALA's claim.

**Around the story.** TALA lines sit in their own blocks inside the scene (never in a paragraph), at most three, and exactly one of them is a calibrated claim (§6). After the prose come the roll notice, the HUD (file 12 §2), four numbered options plus `0) Free action` (file 01 §13), and the one-time how-to block.

## 5. Writing it

- **Voice.** First person, past tense, the PC's voice (file 12 §3). In CINEMATIC (the default) use the Light Novel Style Pack (file 12 §12) with the Voice Seed: no more than four standalone inner-voice lines in the whole chapter, and the inner voice never commits to an action. In GROUNDED, drop the inner voice and the jokes and keep the same facts in a plain register.
- **Never write the PC's speech.** NPCs speak. The PC reacts (a face, a hand, a thought). This is the easiest rule to break in a scene full of other people.
- **Register.** R1 through the evening, up to R2 at the turn. The anti-pattern caps (file 12 §6) apply to the chapter as one scene: one "not X but Y", one triplet list, two similes. Rotate the lead sense, and use at least two non-visual senses.
- **Humour and tenderness.** At least one comic and one tender beat.
- **Backstory fidelity.** Use the player's own words for the past. Keep the PC's feelings to what the player chose (Anchors, Flaws, Voice Seed). Do not judge the PC's past choices beyond how the player framed them.
- **Show, don't list.** Anchors and Flaws appear in action (a stranger recognises the PC; someone is holding on), not as a list.
- **Language.** English only unless `/lang` changed it (file 12 §10). Local terms stand as nouns with context.
- **How-to block (one time).** After the options, one italic block of at most 60 words, outside the fiction: how to choose (a number, or type your own action), the commands that matter early (`/status`, `/inv`, `/tala`, `/map`, `/save`) and the dials (`/tone grounded`, `/lite`, `/intro`).

## 6. State, dice and logging

- **Dice.** Chapter 1 uses **at most one tape row**: the hidden d100 for the opener's TALA claim (file 05 §7, file 15). Compute C from the source tag, show the roll as `[hidden roll T<row>]`, and log `{claim, C, roll, result}` in `tala.claims_open` with the result hidden until verified. No other rolls. A replay never rolls, and a regenerated chapter reuses the locked claim and its row.
- **Clock.** The scene starts at the Origin's start time (for example `D0 NGT 20:30`) and stays there except where the scene's own beats move it.
- **Save Block.** Set `flags.ch1: done`. Set `tala: {mode: STANDARD, battery: 80, leash: 8, attention: 0}` unless the sheet says otherwise. `clock`, `zone` and `tape.ptr` stay as the chapter left them.
- **Journal.** One Tier 1 line: `T1 | D0 <WATCH> hh:mm | <zone> | Chapter 1 delivered; opening TALA claim locked | <ref: T<row>>`.
- **Chronology.** First entry: start time, zone, tape rows used.
- **File system available** (Claude Code): save the delivered story text (title card to final hook, TALA lines included; not the HUD or options) to `saves/chapter_1.md`. `/intro` reprints it.

## 7. Modes

| Mode | When | What changes |
|------|------|--------------|
| **FULL** | New game | Everything above |
| **LEAN** | `/lean` is on | The scene is cut to about 300 words, keeping the hook, the Origin's NPC, TALA's claim and the turn |
| **LEGACY** | Legacy Continuation (file 06 §6) | Titled `Interlude · <name>`. One short scene, at most 500 words: the new PC in their first moment, the city as the Journal says it is now (only Tier 1 facts the new PC could know), TALA meeting a new owner only if the handset changed hands. No tape rows |
| **REPLAY** | `/intro` | Print the saved chapter verbatim from `saves/chapter_1.md` or the chat. No state change, no roll notice, no options |

## 8. Pre-send check (silent)

- [ ] Reads as a story: a hook first line, one scene, no section headings, no briefing paragraphs.
- [ ] Every proper noun and fact traces to the sheet, the player's words, a `[PUBLIC]` line in file 07, the start zone's first sentence, file 06 or 16, or file 05. Delete anything else.
- [ ] No engine numbers outside the HUD and TALA's C%.
- [ ] Nothing the PC could not know at the start time. No future event. Nothing sealed or implied by a sealed block.
- [ ] No speech, choice or conclusion written for the PC. The inner voice does not commit.
- [ ] At most three historical facts and at most two atmosphere motifs.
- [ ] Length within §4. Style caps within §5.
- [ ] One C% claim, one tape row, `ch1` flag set.
- [ ] The last line is a hook that corresponds to a real clock or claim.
- [ ] Options include a low-Signature choice, a TALA consult and one that pays a visible cost for information (file 01 §13).

## 9. Failure modes

1. **It reads like a briefing.** Headings, a world paragraph, a character paragraph, a TALA paragraph. Rewrite it as one scene.
2. **Lore dump.** The recent past arrives as a block. Cap the facts and put them inside the scene.
3. **Spoilers by implication.** An ominous line that only makes sense if you know a secret. Cut it. Atmosphere must work for a reader who knows nothing.
4. **Backstory drift.** The GM adds drama to the PC's past. Stay with the player's words.
5. **The PC speaks.** A line of dialogue written for the PC. Turn it into a reaction.
6. **A second roll.** A replay or regeneration that re-rolls the TALA claim. A claim is locked once rolled.
7. **Running again after a load.** Check `ch1` and `saves/chapter_1.md` first.
