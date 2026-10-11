# 00 — MANIFEST & AUTHORITY

**TITLE:** TALA PROTOCOL — *Firebreak: Metro Cebu*
**BUILD:** TP-FC1.4.0-20261011 (Foundation Candidate 1.4.0)
**SAVE SCHEMA:** TP-SAVE-1.1
**TIER:** CORE (always loaded) | **DEPENDS:** none

---

## 1. What this is

A long-form, AI-run zombie-survival simulator set in **Metro Cebu, Philippines, October 2031 – January 2032**. The player survives a 90-day collapse with the help of **TALA**, a fragment of the national civil-resilience AI living in a government-issued handheld (a *Bantay* handset). TALA can triage wounds, read the mesh, forecast weather and coach decisions. TALA is also a node of the same system that sealed the city. It helps, it is sometimes wrong, and it is never fully on your side.

Story emerges from the simulation. The Dead, the factions and the calendar move whether or not the player acts.

## 2. Design pillars

1. **The world moves without you.** A scheduled Spine Clock (file 11) and off-screen NPC/faction ticks (files 09, 10) advance on the calendar.
2. **Information is the survival resource.** Noise, Light and Scent (file 02) decide who finds you. TALA sells information at a price: its emissions are a signature too.
3. **Help has a cost.** Every TALA assist, ally and shortcut carries a trade-off the player can see coming.
4. **Every number has an owner.** State lives in the Save Block (file 13) and the Dice Tape (file 15). No vibes-based adjudication, no fudged rolls.
5. **Dignity in loss.** Infection, death and betrayal get a scene (Final Watch, Legacy Continuation), not a silent fail state.

## 3. Lineage

Built on the structural strengths of the earlier Deadlight / STORY_RUNTIME work: a strict authority hierarchy, a two-tier mutation journal, a locked infection schedule, Player Sovereignty enforcement, NPC moral asymmetry, Restore Anchors and a Chronology tracker, and a Prose Style / Anti-Pattern Engine. New in this build: the **Dice Tape**, **calibrated AI uncertainty**, **Signature/Heat stealth economy**, and a **Lean Core / Reference split** to stop long-campaign context pressure.

## 4. File manifest

| # | File | Role | Tier |
|---|------|------|------|
| 00 | MANIFEST_AND_AUTHORITY | Authority, loading, versioning | CORE |
| 01 | KERNEL_AND_RESOLUTION | Turn loop, d20 resolution, gates, commands | CORE |
| 02 | SURVIVAL_AND_SIGNATURE | Needs, Load, Signature, Heat, scavenging pools, renewable food and water, travel | CORE |
| 03 | COMBAT_AND_POSITION | Combat v2: Battlefield Card, Momentum and techniques, Pressure/Grapple/Bite, Alarm clock, humans, companions | CORE |
| 04 | INFECTION_AND_THE_GUTOM | Locked infection schedule, Gutom classes | CORE |
| 05 | TALA_AI_SYSTEM | The AI guide: modes, modules, calibration, directives | CORE |
| 06 | CHARACTER_CREATION | Origins, plausibility budget, kits | REF (boot) |
| 07 | WORLD_HISTORY | Timeline and public vs sealed history | REF |
| 08 | GEOGRAPHY | Zones, density, routes, resources | REF |
| 09 | FACTIONS | Factions, clocks, off-screen tick | REF |
| 10 | CHARACTERS | Cast, NPC engine, voices | REF |
| 11 | STORY_BIBLE_AND_SPINE | Themes, Spine Clock, secrets, endings | REF (GM-eyes) |
| 12 | PROSE_STYLE_ENGINE | Output contract, voice, anti-patterns | CORE |
| 13 | SAVE_LEDGER_AND_ANCHORS | Save Block, journal, anchors, degradation protocol | CORE |
| 14 | TABLES | Randomizers and yield tables | REF |
| 15 | DICE_TAPE | 720 pre-rolled rows, pointer, audit rules | CORE (pointer) / REF (data) |
| 16 | DAY0_OPENINGS | Per-Origin Day 0 opening scripts | REF (boot) |
| 17 | CHAPTER_ONE_INTRO | The opening chapter: world, PC and TALA from public lore, run once after character creation | REF (boot) |

Companion: `PROJECT_INSTRUCTIONS.md` (paste into Project custom instructions), `README.md`, `tools/tape_check.py` (optional offline roll checker) and the Claude Code skill `.claude/skills/chapter-one/` (runs file 17).

## 5. Authority hierarchy (highest wins)

1. **Player Sovereignty & Content Boundaries** (file 01 §10, §16)
2. **This Manifest** (file 00)
3. **Kernel** (file 01)
4. **Mechanics** (files 02, 03, 04, 05, 06)
5. **Live Save State** (file 13 values) *wins over lore for current numbers, but never over rules*
6. **Canon Lore** (files 07–11)
7. **Style** (file 12) *wins only inside prose choices; it can never alter state or mechanics*
8. **Tables** (file 14) *are inputs to rules, not rules*

**Conflict rule:** the higher level decides. If two same-level files conflict, the more specific file wins; log the conflict in the Chronology as `AUTH-CONFLICT` and tell the player once, briefly.

**Sealed content:** blocks tagged `[SEALED:S#]` are GM-only truths. They may shape the simulation but may not appear in narration, TALA output or option text until the Spine Clock or a logged discovery flips them to `KNOWN`.

## 6. Loading tiers (context discipline)

The Full Export of every file creates context pressure in long campaigns. Use tiers:

- **Lean Core** (always active): 00, 01, 02, 03, 04, 05, 12, 13, 15 pointer rules. This is enough to run any turn.
- **Boot Reference** (read once at game start, then on demand): 06, 16, 17.
- **On-demand Reference:** 07–11 and 14. Retrieve only the entry needed (a zone, an NPC, a clock, a table). Do not recite whole files.
- **Never re-narrate lore the player has not asked for or discovered.** The one scheduled exception is Chapter 1 (file 17), limited to public lore.

## 7. Versioning discipline

- Every change ships with a changelog line: `BUILD | file | what changed | why | risk`.
- Never edit canon retroactively inside a live campaign. Use a Patch Note in the Save Block (`patches:` field).
- Version bump rules: PATCH = typo/table value; MINOR = new rule or file (additive Save Schema fields are allowed: the schema minor goes up and older saves load with defaults); MAJOR = a breaking Save Schema change.

### Changelog
- `TP-FC1.0.0-20261010` — initial Foundation Candidate: 16 files, Lean Core split, Dice Tape, TALA calibration.
- `TP-FC1.1.0-20261011` | 12, 06, 13, PROJECT_INSTRUCTIONS | Added Light Novel Style Pack (file 12 §12); default tone changed GROUNDED → CINEMATIC; Voice Seed added to character creation and Save Block | requested style direction | risk: inner-voice drift into player decisions (guarded by Sovereignty rule), hook inflation (guarded by "tied to real state")
- `TP-FC1.2.0-20261011` | 03 (rewritten), 04, 02, 01, 10, 12, 13, PROJECT_INSTRUCTIONS, README | Combat v2: Momentum and techniques, Grapple-before-Bite, Alarm clock, Battlefield Card, Layers, Morale, companion roles, Marks growth; Hit DCs lowered by 1 (Lakad 9, Sariwa 12, Bulok 7, Hiyaw 11); Pressure DC 8 + n | requested emphasis on combat; v1 simulated at 64% bite-check vs 3 Lakad and 93% vs 5 | risk: Shove Line, Quiet Finish, Second Wind and weapon signatures unsimulated; Sariwa, Hiyaw and the Alarm clock not modelled
- `TP-FC1.3.0-20261011` | 02, 04, 05, 08, 09, 11, 13, 14, 15 (720 rows), 16 (new), 01, 03, 06, 07, 10, 12, 00, PROJECT_INSTRUCTIONS, README, tools/tape_check.py (new) | Scarcity Pools with Rich/Picked/Scraped tiers and fixed yields; renewable food and water; Compact Stores and barter; Command Attention for TALA check-ins; Hum Pull for S2; Wash Window and Remisol supply fixed; faction codes defined; 720-row tape, /audit and offline checker; tracking tiers and Lite mode; Anchor cadence fixed; 12 Day 0 openers; style-priming and Cebuano language fixes; Alarm threshold raised to Round Noise 4 and extended combat calibration; schema 1.0 → 1.1 (additive) | closes the open defects from the v1.2.0 review | risk: renewables, Hiyaw, humans, Mop-up and several techniques unplayed; Cebuano terms approximate
- `TP-FC1.4.0-20261011` | 17 (new), skill `chapter-one` (new), 00, 01, 06, 12, 13, 16, PROJECT_INSTRUCTIONS, CLAUDE.md, README | Chapter 1: an intro generated once after character creation that presents the world, the PC and TALA from public lore only and ends on the Day 0 opener; `ch1` flag, `/intro` replay, LEGACY mode; save schema unchanged | the player asked for an opening chapter that sets the scene without telling secrets | risk: run on one custom Origin only; the public-lore allow-list may be too tight or too loose for other Origins; the skill depends on the model following the allow-list

## 8. `/verify` checklist (run at boot and on request)

- [ ] Build IDs match across files 00, 13 and any loaded Anchor
- [ ] Save Schema version matches (TP-SAVE-1.1)
- [ ] Dice Tape present (720 rows) and pointer valid (1–720)
- [ ] Spine Clock date math consistent: Day 0 = Fri 17 Oct 2031; Day 90 = Thu 15 Jan 2032
- [ ] All `[SEALED]` tags intact and none leaked into narration
- [ ] Feature Gates (file 01 §9) consistent with Anchor `unlocked:` list
- [ ] Chapter 1 delivered: `flags.ch1` is `done` in any save or Anchor past character creation (file 17)

## 9. Known gaps (honest list for the next build)

- Ordinary-life content (Act II routines, community upkeep) is specified at system level; flavor tables are thin.
- No formal mass-combat or siege subsystem beyond Hold ratings and Convergence events.
- Marine travel is abstracted; weather-on-water rules are minimal.
- Companion NPC injury/medical depth is lighter than the player's.
- Combat v2 and the food economy are calibrated by simulation only (Lakad and Sariwa mixes; food for solo and four-person parties). Hiyaw, human fights, Mop-up, Shove Line, Quiet Finish, Second Wind, weapon signatures, fishing risk and garden raids still need playtesting.
- Nothing has been played end to end. Expect rule friction in the first three Days.
- Cebuano street names (file 04) and Bisaya glosses (file 12) are approximate; verify with a Cebuano speaker.
- Chapter 1 (file 17) has been run for one custom Origin only. The twelve templates, LEGACY mode and `/lean` are untested.
