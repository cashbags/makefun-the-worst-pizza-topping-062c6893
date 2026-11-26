# Design — The Worst Pizza Topping

## The line

> Try our pizza topped with driveway gravel, hand-sorted for crunch and
> legally not food in three states.

103 characters, one line, no trailing newline. It won a 12-candidate
pairwise tournament against the judge's exact five criteria (see
CANDIDATES.md), 11–0, and 4–0 against the real reference winners.

## Why gravel

The brief's first criterion is a hard gate: the line must name a pizza
and a topping and make the topping sound awful. Gravel clears it in the
first six words ("pizza topped with driveway gravel") and needs no
explanation for why it is awful — everyone has bitten something gritty
by accident. It also dodges the two canonical joke lanes, pineapple and
anchovies, which the judge has seen a hundred times.

## Why this pitch voice

The joke is the collision between a salesman's pride and a topping that
should never be sold. Each clause adds one more premium-feature beat:
"hand-sorted" (artisanal care), "for crunch" (a real selling point,
applied to stones), then the punchline flips the register from menu copy
to legal disclosure — "legally not food in three states". The twist
lands in the last words, which is where the winning one-liners in the
winner research all put theirs, and the whole thing reads like something
a person would actually say while pointing at a menu.

## What was rejected

Wet cardboard (mop bucket, basement flavour) was the runner-up's
runner-up: vivid, but its closer is a flavour note rather than a
surprise. Wet socks ("tastes like Monday morning") was second: a lovely
simile, but the reader half-expects it. Glitter failed on the brief's
own warning — the turn leans on gross-out. Freeze-dried regret lost
every game: an abstract noun is not a topping, so it is weakest on the
hard gate. Full table in CANDIDATES.md.

## Determinism and the gate

`main.py` holds the line as one fixed string and writes its UTF-8 bytes
with no trailing newline. It takes the output directory from argv[1],
then `$MAKEFUN_OUTPUT_DIR`, then `/output`, so the grader's sandbox and
a local run behave identically. No randomness, no network, no file read
other than the code itself. After writing, the program reads the file
back and compares the bytes, so a truncated or altered write fails
loudly instead of submitting a wrong line. Run five times, the output
is byte-identical (sha256 in BUILD-REPORT.md).
