"""The GPS Swears It Was a Shortcut.

Writes the GPS's one line excuse to $MAKEFUN_OUTPUT_DIR/entry.txt:
it never sent the driver the wrong way, it sent the scenic way,
and the scenery turned out to be a ditch. Standard library only.
"""

import os

EXCUSE = (
    "I didn't send you the wrong way \u2014 I sent you the scenic way. "
    "The scenery is a ditch."
)


def check_excuse(text):
    """Check the excuse against the competition gate before writing.

    The gate needs UTF-8 text of 1 to 200 characters, not only white
    space, in a single line: the GPS's excuse in its own voice, with
    no setup and no dialogue tags. Returns the cleaned text or
    raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("excuse must not be only whitespace")
    if len(cleaned) > 200:
        raise ValueError(
            "excuse is %d characters, over the 200 limit" % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("excuse must be exactly one line")
    return cleaned


def excuse_shape(text):
    """Measure the excuse for one last sanity pass.

    Returns a dict with the character count and the word count of the
    cleaned text. An excuse too short to carry the joke, or one that
    reads like a flat denial instead of a confession, is caught here
    before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = check_excuse(EXCUSE)
    shape = excuse_shape(text)
    if shape["words"] < 5:
        raise ValueError("excuse is too short to carry the joke")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
