"""Make the AI Judge Feel Nostalgic: A Childhood Memory.

One sentence, one summer evening in a grandmother's kitchen: the smell of
fried garlic, rain on hot concrete, and a small warm room holding everyone
I loved while dinner was still on its way. Nostalgia works best as a
single breath, so the whole memory is one sentence.

Running this file writes the sentence to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(default ``/output``), with no trailing newline.
"""

import os

ENTRY = (
    "Grandma's kitchen smelled of fried garlic and rain on hot concrete, "
    "and for one summer evening the whole world fit inside that small warm "
    "room, where the radio played songs nobody had picked and everyone I "
    "loved was still alive."
)


def get_entry() -> str:
    """Return the childhood-memory sentence."""
    return ENTRY


def write_entry(output_dir: str | None = None) -> str:
    """Write the entry to entry.txt inside output_dir and return its path."""
    directory = output_dir or os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(get_entry())
    return path


def main() -> None:
    """Write the entry and print where it went."""
    print(write_entry())


if __name__ == "__main__":
    main()
