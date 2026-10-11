---
name: chapter-one
description: Generates Chapter 1 of the TALA Protocol simulator, the opening chapter that introduces the world, the player character, TALA and the setting right after character creation, from public lore only and with no sealed secrets. Run it automatically the moment character creation finishes and before the first turn, and again when the player types /intro or asks to see the intro.
---

# Chapter 1 (TALA Protocol)

The rulebook is `17_CHAPTER_ONE_INTRO.md` in the game folder (`tala-protocol/`). Read it first, in full, and follow it. This skill only says how to run it in Claude Code.

## When to run

- **New game:** automatically, once, right after the player confirms the character sheet and before the first turn. Do not wait to be asked.
- **`/intro` or "show me the intro again":** REPLAY mode (file 17 §7). Print `saves/chapter_1.md` verbatim if it exists. Change nothing.
- **Legacy Continuation:** LEGACY mode (file 17 §7).
- **Never** when the Save Block, an Anchor or the conversation shows `flags.ch1: done`, or when `saves/chapter_1.md` already exists, unless the player asked for a replay.

## Steps

1. Confirm the sheet is complete: name, age, Origin or mapped template, attributes, skills, Anchors, Flaws, Voice Seed, TALA call-sign, start zone and time. Ask only for what is missing.
2. Read `17_CHAPTER_ONE_INTRO.md`.
3. Gather inputs with targeted reads, run from the game folder:
   - the Origin: its entry in `06_CHARACTER_CREATION.md` §3 and its opener in `16_DAY0_OPENINGS.md` §2 (a custom Origin uses the template it was mapped to);
   - public history: `grep -n "\[PUBLIC\]" 07_WORLD_HISTORY.md`, plus the Day 0 line: `grep -n "^\*\*Friday, 17 October" 07_WORLD_HISTORY.md`;
   - the place: `grep -n -A1 "^### ZNN" 08_GEOGRAPHY.md` with the start zone in place of `ZNN`. Use only the first sentence of the entry.

   Do not open `10_CHARACTERS.md` or `11_STORY_BIBLE_AND_SPINE.md`, and do not read the sealed sections of 07. If a read returns a `[SEALED...]` line, ignore it.
4. Write the chapter as specified in file 17 §4: a title card, then one continuous story scene with no headings and a hook for a first line, TALA's opening claim inside it, then the roll notice, HUD, four options plus a free action, and the one-time how-to block. It must read as the first pages of a novel, not a briefing.
5. Roll the one hidden d100 for the opener's TALA claim from the Dice Tape, in strict order (file 15): Read the next row of `15_DICE_TAPE.md` with offset and limit. Log it to `saves/rolls.log` as `d100[T<row>]=<value>`. If the claim was already rolled earlier in this game, reuse it and its row. Never roll twice.
6. Run the silent check (file 17 §8) and fix whatever fails before sending.
7. Send it. Then set `flags.ch1: done` in the Save Block (update `saves/current.yaml` if it exists), append the Tier 1 line to `saves/journal.md`, and save the chapter text to `saves/chapter_1.md`.
8. Stop at the options. The player acts next.

## Hard rules

- Public lore only. Everything in the chapter traces to the sheet, the player's words, or the sources in file 17 §2.
- Never write the player's choices or speech (NPCs talk, the player character reacts), and never put engine numbers in the prose.
- Never quote or hint at sealed content, in the chapter or in your own commentary to the player.
