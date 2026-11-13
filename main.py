#!/usr/bin/env python3
"""news-image-01 entry program.

The entry image lives in this repository as entry.png, next to this file.
The program's whole job is to copy those bytes, unchanged, to
<output dir>/entry.png, where the output dir is $MAKEFUN_OUTPUT_DIR when
set and /output otherwise (in the grader's container only /output is
writable, and no environment variable is set). The default is the
absolute path /output, never a relative directory.

Standard library only; no network; deterministic: running it any number
of times writes the same bytes.
"""

import os

# Copy in 256 KiB blocks: small enough to stream comfortably inside the
# grader's 512 MB container, large enough to finish near-instantly.
CHUNK_SIZE = 256 * 1024


def copy_entry(src: str, dst: str) -> None:
    """Copy src to dst byte for byte, in chunks."""
    with open(src, "rb") as fin, open(dst, "wb") as fout:
        while True:
            chunk = fin.read(CHUNK_SIZE)
            if not chunk:
                break
            fout.write(chunk)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    copy_entry(src, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
