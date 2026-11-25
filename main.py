"""One-line crypto trading joke for make.fun — Laugh Track contest.

Writes exactly one line (1-200 chars) to /output/entry.txt.

Judge criteria, in order:
1. One-line joke about crypto and trading life, clear setup + turn.
2. Real laugh: surprise turn, payoff rewards the setup.
3. True to trading life: recognisable detail (gas fees) — earned, not generic.
4. Tight phrasing, punchline at the end.
5. Repeatable to a friend on a second read.

Pattern: ONE concrete scene (made a profit, then checked the gas fees) +
ONE reversal (the blockchain kept the profit) + ONE landing final line
("I kept the screenshot").

Hardening (revise): validate() proves UTF-8 encodability before any
write, so a lone/unpaired surrogate exits 1 cleanly instead of raising
a mid-write UnicodeEncodeError traceback; a UTF-8 byte-length bound
(4 bytes per char max) guards the output size as well.
"""

import os

ENTRY = "I finally made a profit trading, then checked the gas fees. The blockchain kept the profit; I kept the screenshot."
MAX_CHARS = 200


def validate(text):
    if not text or not text.strip():
        raise SystemExit("entry is empty")
    if len(text) > MAX_CHARS:
        raise SystemExit("entry exceeds 200 characters")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if any(ord(c) < 0x20 for c in text):
        raise SystemExit("entry contains a control character")
    try:
        encoded = text.encode("utf-8")
    except UnicodeEncodeError:
        raise SystemExit("entry is not valid UTF-8")
    if len(encoded) > MAX_CHARS * 4:
        raise SystemExit("entry exceeds UTF-8 byte limit")
    return text


def main():
    entry = validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
