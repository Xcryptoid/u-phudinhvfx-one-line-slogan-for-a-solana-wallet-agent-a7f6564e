"""Copy the pre-written slogan into the output directory.

The slogan itself lives in entry.txt next to this file. This program
only copies it to MAKEFUN_OUTPUT_DIR/entry.txt, exactly as written.
"""

import os
import shutil


def main():
    # The slogan is already written in entry.txt; this program only
    # carries it into the output directory, word for word.
    here = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(
        os.path.join(here, "entry.txt"),
        os.path.join(out_dir, "entry.txt"),
    )


if __name__ == "__main__":
    main()
