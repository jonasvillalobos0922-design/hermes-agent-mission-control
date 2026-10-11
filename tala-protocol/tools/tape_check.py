#!/usr/bin/env python3
"""Check TALA PROTOCOL roll notices against the Dice Tape (file 15).

Usage:  python3 tools/tape_check.py rolls.txt [path/to/15_DICE_TAPE.md]

rolls.txt: paste roll notices or /audit lines. Recognised patterns (Pass 1 only):
    d20[T41]=14        d100[T12]=45        d6[T200]=3
    T41 d20 = 14       (the /audit format)
Checks: value matches the tape row, no row repeats, rows strictly increase.
"""
import re, sys, os

def load_tape(path):
    tape = {}
    for line in open(path, encoding="utf-8"):
        m = re.match(r"^\| (\d+) \| (\d+) \| (\d+) \| (\d+) \|$", line.strip())
        if m:
            i, a, b, c = map(int, m.groups())
            tape[i] = {"d100": a, "d20": b, "d6": c}
    return tape

PATTERNS = [
    re.compile(r"(d100|d20|d6)\[T(\d+)\]\s*=\s*(\d+)"),
    re.compile(r"T(\d+)\s+(d100|d20|d6)\s*=\s*(\d+)"),
]

def parse(text):
    out = []
    for line in text.splitlines():
        for k, pat in enumerate(PATTERNS):
            for m in pat.finditer(line):
                if k == 0:
                    die, row, val = m.group(1), int(m.group(2)), int(m.group(3))
                else:
                    row, die, val = int(m.group(1)), m.group(2), int(m.group(3))
                out.append((row, die, val))
    return out

def main():
    if len(sys.argv) < 2:
        print(__doc__); return 2
    rolls_path = sys.argv[1]
    tape_path = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(__file__), "..", "15_DICE_TAPE.md")
    tape = load_tape(tape_path)
    if len(tape) != 720:
        print(f"WARNING: tape has {len(tape)} rows (expected 720)")
    rolls = parse(open(rolls_path, encoding="utf-8").read())
    problems = 0
    seen = set(); last = 0
    for row, die, val in rolls:
        if row not in tape:
            print(f"BAD ROW  T{row}: not in tape"); problems += 1; continue
        if tape[row][die] != val:
            print(f"MISMATCH T{row} {die}: notice says {val}, tape says {tape[row][die]}"); problems += 1
        if row in seen:
            print(f"REUSED   T{row}: row used more than once"); problems += 1
        elif row < last:
            print(f"ORDER    T{row}: comes after T{last}"); problems += 1
        seen.add(row); last = max(last, row)
    print(f"checked {len(rolls)} rolls, {problems} problem(s)")
    return 1 if problems else 0

if __name__ == "__main__":
    sys.exit(main())
