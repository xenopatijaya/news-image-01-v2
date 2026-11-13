#!/usr/bin/env python3
"""Copy the finished news-image entry to the grader output directory.

The entry image lives next to this script in the repository. This program
moves it, unchanged, into the directory named by MAKEFUN_OUTPUT_DIR (or
"/output" when that variable is absent) under the name "entry.png".

Only the Python standard library is used, there is no network access, and
the copy is a plain byte-for-byte transfer, so the result is deterministic.
If the output directory happens to be the repository directory itself, the
copy is skipped because source and destination are already the same file.
"""

import os
import shutil
import sys
from pathlib import Path

SOURCE_NAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"


def main() -> int:
    script_dir = Path(__file__).resolve().parent
    source = script_dir / SOURCE_NAME

    if not source.is_file():
        print(f"missing source image: {source}", file=sys.stderr)
        return 1

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR)
    output_dir.mkdir(parents=True, exist_ok=True)

    destination = output_dir / SOURCE_NAME
    if destination.resolve() != source.resolve():
        shutil.copyfile(source, destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
