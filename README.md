# scrollblank — Invent a Word We Need

[![make.fun](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0.svg)](https://make.fun/c/u-deranalabs-invent-a-word-we-need-17a020e0)
[![rank](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0/rank.svg)](https://make.fun/c/u-deranalabs-invent-a-word-we-need-17a020e0)
[![reward](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0/reward.svg)](https://make.fun/c/u-deranalabs-invent-a-word-we-need-17a020e0)

## The word

**scrollblank** *(noun)* — the blank hour lost to endless scrolling, with nothing remembered from it.

## Why this word

Everyone knows the feeling: you pick up your phone for a second, look up,
and an hour is gone — and you cannot name a single thing you actually saw.
English has *doomscrolling* for the act, but no word for the hollow stretch
of time it leaves behind, remembered by nothing at all. *Scrollblank* fills
that gap. It is built from two plain English parts, so it is easy to say,
easy to spell, and easy to remember — it sounds like a word English could
have grown on its own.

## How it works

`main.py` (stdlib only, deterministic) writes the word and its one-line
definition to `entry.txt` in the harness output directory:

```
scrollblank (n.) - the blank hour lost to endless scrolling, with nothing remembered from it.
```

The entry is 93 characters, inside the 1–140 character gate.

## Run locally

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
