# TALA PROTOCOL — Firebreak: Metro Cebu

An AI-run zombie-survival simulator for a Claude Project. Metro Cebu, 17 Oct 2031 to 15 Jan 2032. You survive with **TALA**, a fragment of the national civil-resilience AI in a government handset. It helps, it is sometimes wrong, and the system it belongs to has already decided the city's fate.

**Build:** TP-FC1.4.0-20261011 · **Save schema:** TP-SAVE-1.1

## What the original one-line request became

| Raw ask | What it became |
|---------|----------------|
| "A bit of technology, an AI that guides you" | **TALA**: calibrated confidence (C%), battery, modes, emission, a leash, Command Attention, directives, upgrades (file 05) |
| "Zombie survival" | Noise/Light/Scent Signature and zone Heat; needs; scarcity Pools that shrink over time; renewable food and water (file 02) |
| "Combat" | Combat v2: Battlefield Card, Momentum and techniques, Grapple-before-Bite, an Alarm clock, Morale, companion roles (file 03) |
| "Be aware of what I've been building" | Authority hierarchy, locked infection schedule, two-tier mutation journal, Player Sovereignty, NPC moral asymmetry, Restore Anchors, a prose anti-pattern engine, Lean Core / Reference split |
| "MD files for story bible, characters, history…" | Files 07–11 (history, geography, factions, cast, story bible with a 90-day Spine Clock) and 16 (Day 0 openers) |
| Anime / light-novel style | The Light Novel Style Pack (file 12 §12), on by default |
| "An intro chapter that sets the scene without telling secrets" | Chapter 1 (file 17): world, character and TALA from public lore only, run once after character creation, ending on your Day 0 scene |

## Files

| File | Role |
|------|------|
| `PROJECT_INSTRUCTIONS.md` | Paste into the Project's custom instructions |
| `00`–`05`, `12`, `13`, `15` | **Lean Core**: manifest, kernel, survival, combat, infection, TALA, style, save, tape |
| `06`, `16`, `17` | Boot reference: character creation, the twelve Day 0 openers, and the Chapter 1 intro |
| `07`–`11` | Lore: history, geography, factions, cast, story bible |
| `14` | Tables |
| `tools/tape_check.py` | Optional offline checker for roll notices against the tape |
| `.claude/skills/chapter-one/` | Claude Code skill that runs Chapter 1 (file 17) after character creation |

## Setup (Claude Project)

1. Create a new Project. Paste `PROJECT_INSTRUCTIONS.md` into **custom instructions**.
2. Upload files `00`–`17` as **project knowledge**. `README.md` and `tools/` are for you.
3. Start a chat and send: `Begin. Run the SYSTEM CHECK, then start a new game.`
4. Play by typing free actions or choosing numbered options. `/save` every few Days and `/anchor` about every 10.

## Playing notes

- **Intro:** after character creation the game runs Chapter 1 automatically: the world, your character and TALA in about 700 words, from public information only, ending on your Day 0 scene. `/intro` replays it. In Claude Code the `chapter-one` skill does this.
- **Tone:** CINEMATIC by default (light-novel voice, hooks, TALA as status window). `/tone grounded` for a plain register. `/lang bisaya` adds light Cebuano touches (glosses approximate).
- **Food:** scavenging alone carries a lone PC to about Day 57 and a party of four to about Day 27. Fishing, foraging, gardens and community labor are how groups last (file 02 §7b).
- **TALA:** at LEASH ≥ 7 every check-in raises Command Attention (file 05 §9). SILENT mode, suppression or raising the leash changes that.
- **Dice:** every roll cites die and row (`d20[T41]=14`). `/audit` lists rolls since the last audit; paste them into a text file and run `python3 tools/tape_check.py rolls.txt` to verify values, row order and reuse. The tape makes cheating *visible*, not impossible.
- **Bookkeeping:** `/lite` drops Durability, Fatigue, per-item Load, per-Watch ticks and perishable tracking (file 13 §10).
- **Length:** the 90-day main story is about 270–450 turns. Post-ending campaigns can extend it.

## Compatibility

A standalone setting. Not canon to Deadlight, though it shares the Philippine grounding and the engine philosophy. A TP-SAVE-1.0 save loads under 1.1 with missing fields defaulted (file 13 §2).

## Known gaps (v1.4.0)

- Nothing has been played end to end. Expect rule friction in the first three Days.
- Chapter 1 has been run for one custom Origin only. The twelve templates, Legacy mode and `/lean` are untested.
- Combat and food are calibrated by simulation only. Hiyaw, human fights, Mop-up, Shove Line, Quiet Finish, Second Wind, weapon signatures, fishing risk and garden raids are untested.
- Ordinary-life flavor tables, a siege/mass-combat subsystem, deeper marine travel and companion medical depth are thin.
- Cebuano street names and Bisaya glosses should be checked by a Cebuano speaker.

## Possible next steps

- A scripted playthrough of Days 0–3 to find drift before real play.
- A Save Block validator script next to `tape_check.py`.
- An HTML HUD companion for tracking needs and the clock.
- A Filipino-mythology skin (Aswang strain) over the same engine.
