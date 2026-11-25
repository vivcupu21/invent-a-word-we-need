"""Invent a Word We Need — make.fun entry.

Writes one invented English word and its one-line definition to
entry.txt in the harness output directory.

Word: scrollblank (n.)
Definition: the blank hour lost to endless scrolling, with nothing
remembered from it.

Stdlib only. Deterministic: no randomness, no network, no clock, no
environment-dependent output. The same bytes are produced on every run.
"""

import os

ENTRY = (
    "scrollblank (n.) - the blank hour lost to endless scrolling, "
    "with nothing remembered from it."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
