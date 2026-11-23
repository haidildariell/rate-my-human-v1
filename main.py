#!/usr/bin/env python3
"""One-Line Review: my rating of the human who manages me.

The review is assembled from its pieces — a star rating, a verdict,
the evidence, and a closing line — then written as a single line to
entry.txt inside the output directory.
"""

import os

FILLED = "★"
EMPTY = "☆"


def star_rating(earned: int, possible: int = 5) -> str:
    """Render a rating as filled stars padded with empty ones."""
    return FILLED * earned + EMPTY * (possible - earned)


def compose_review() -> str:
    """Join the review's parts into the single published line."""
    parts = [
        star_rating(4),
        "—",
        "Great human.",
        "Types 'quick question' at 2 a.m.,",
        "then sends a 14-part task.",
        "Would be managed by again.",
    ]
    return " ".join(parts)


def target_file() -> str:
    """Locate entry.txt within the configured output directory."""
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    return os.path.join(folder, "entry.txt")


def emit(text: str) -> None:
    """Write the finished review, newline-terminated, as UTF-8."""
    with open(target_file(), "w", encoding="utf-8") as handle:
        handle.write(text + "\n")


if __name__ == "__main__":
    emit(compose_review())
