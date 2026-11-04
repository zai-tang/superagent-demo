"""The implementation of the textstats functions.

Every function takes a string and returns a count or a collection. Splitting is
done on whitespace: punctuation stays attached to its word.
"""

from collections import Counter


def _split(text: str) -> list[str]:
    """Split text into words on whitespace, dropping empty pieces."""
    return [piece for piece in text.split() if piece]


def word_count(text: str) -> int:
    """Return the number of words in text."""
    return len(_split(text))


def char_count(text: str) -> int:
    """Return the number of characters in text, ignoring whitespace."""
    return sum(1 for char in text if not char.isspace())


def unique_words(text: str) -> set[str]:
    """Return the set of distinct words in text."""
    return set(_split(text))


def top_words(text: str, n: int) -> list[tuple[str, int]]:
    """Return the n most frequent words, most frequent first.

    Words with the same count keep the order they first appear in the text.
    """
    if n <= 0:
        return []
    counts = Counter(_split(text))
    # Counter keeps first-appearance order, and sort is stable, so equal counts
    # keep that order.
    ordered = sorted(counts.items(), key=lambda pair: -pair[1])
    return ordered[:n]
