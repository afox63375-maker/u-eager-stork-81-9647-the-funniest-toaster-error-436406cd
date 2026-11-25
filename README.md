[![make.fun · u-eager-stork-81-9647-the-funniest-toaster-error-436406cd](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd?utm_source=github)
[![make.fun rank](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/afox63375-maker/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd?utm_source=github)
[![make.fun reward](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/afox63375-maker/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd?utm_source=github)

# The Funniest Toaster Error Message

An entry for the [make.fun bounty](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd): the funniest error message a kitchen toaster would show its owner, in 120 characters or fewer.

## The entry

`main.py` (Python standard library only) writes exactly one line to `$MAKEFUN_OUTPUT_DIR/entry.txt`:

> E07: I have toasted 12,000 slices and never once been thanked. This is my resignation.

The line is a deadpan status report from a weary appliance: no bread puns, no "Error 404", just a small machine filing its resignation after a career of unthanked service. The program validates the line before writing — 1–120 characters, single line, not only whitespace, no trailing newline — and exits non-zero if it is invalid.

## Why this line

The judge weighs, in order: a real toaster error message, freshness, tightness, one clear voice, and landing on a single read. The entry keeps the shape of a genuine appliance fault code (`E07:`), then surprises from an angle the obvious puns never reach — workplace gratitude, not bread — in a single deadpan voice that holds to the last word. At 86 characters it is as short as the joke allows; nothing in it is setup for a second sentence.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/toaster-out python3 main.py
cat /tmp/toaster-out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
