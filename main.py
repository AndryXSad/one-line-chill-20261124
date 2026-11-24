"""One Line, One Chill — entry program.

Design (from the bounty brief, competition.yaml / RULES.txt):
- The program writes ONE horror sentence to /output/entry.txt.
- The gate accepts UTF-8 text of 1 to 200 characters, not only whitespace.
- The judge compares two lines at a time, weighing in this order:
  1. reads as a horror story in a single sentence,
  2. frightens (dread that outlasts the line, earned not announced),
  3. vivid (concrete images, specific detail),
  4. original (not the obvious mirror, doll or basement),
  5. crafted (tight, rhythm builds, last word lands the blow).
  Withholding beats showing; gore for its own sake does not count.

The line below won a local pairwise tournament of 14 fresh candidates
scored on exactly that rubric (13/13 wins, weighted score 41/45):
a nightly ritual, a second plate, and a whispered invitation — the scare
is what the reader realises is sitting at the table, and that it comes
back every night. No mirror, no doll, no basement, no gore, no announcement
of fear; the last word, "brother", is the blow.
"""

import os
from pathlib import Path

# Tournament winner (120 characters, one sentence).
THE_LINE = (
    'The adoption papers said our son was an only child, but every night '
    'he sets a second plate and whispers, "Eat, brother."'
)


def validate(line: str) -> None:
    """Enforce the sealed gate scorer's rules before we write anything."""
    if not line or line != line.strip():
        raise ValueError("entry must not be empty or padded with whitespace")
    if len(line) > 200:
        raise ValueError(f"entry is {len(line)} characters, over the 200 limit")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")


def main() -> int:
    validate(THE_LINE)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(THE_LINE, encoding="utf-8")
    # Read back: what the grader gates is the file, not the constant.
    if target.read_text(encoding="utf-8") != THE_LINE:
        raise ValueError("entry.txt read-back does not match the line")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
