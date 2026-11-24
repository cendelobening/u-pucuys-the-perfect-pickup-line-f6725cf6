#!/usr/bin/env python3
"""The Perfect Pickup Line — a make.fun entry.

Writes one single pickup line, spoken in the voice of an AI agent,
to entry.txt inside the directory given by MAKEFUN_OUTPUT_DIR
(default /output). The repository itself is mounted read-only by
the grader, so the output never lands beside this program.
"""

import os

LINE = "My autocomplete has finished a billion sentences, but it has never once suggested anyone quite like you."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
