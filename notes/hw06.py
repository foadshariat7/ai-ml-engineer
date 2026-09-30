"""Homework 06: List, set, and dict comprehensions.

Implement each function below according to its docstring. Do not change
any function signatures. Replace the `...` placeholder in each function
body with your implementation.

Each function must be written as a single comprehension (list, set, or
dict, as appropriate) — not a `for` loop with `.append` or manual key
assignment.
"""


def square_positive(
    values: list[int],
) -> list[int]:
    """Square every positive value, dropping the rest.

    Args:
        values: The values to process. Must not be mutated by this
            function.

    Returns:
        A new list containing `value ** 2` for every `value` in
        `values` that is strictly greater than zero, in the original
        order. Zero and negative values are excluded entirely — they
        do not appear as `0` or as their (negative) square.
    """
    ...


def normalize_names(
    names: list[str],
) -> list[str]:
    """Normalize a list of names, dropping any that are blank.

    Args:
        names: The names to process. Must not be mutated by this
            function.

    Returns:
        A new list containing each name in `names` with leading and
        trailing whitespace removed and converted to lowercase, in the
        original order. A name that is empty or whitespace-only after
        stripping is excluded from the result entirely.
    """
    ...


def unique_lengths(
    words: list[str],
) -> set[int]:
    """Collect the distinct string lengths present in a list of words.

    Args:
        words: The words to measure. Must not be mutated by this
            function.

    Returns:
        A set containing `len(word)` for every `word` in `words`, with
        duplicate lengths collapsed since the result is a set.
    """
    ...


def score_labels(
    scores: dict[str, float],
) -> dict[str, str]:
    """Label each score as "high" or "low".

    Args:
        scores: A mapping from name to score. Must not be mutated by
            this function.

    Returns:
        A new dict mapping every key in `scores` to `"high"` if its
        score is greater than or equal to `0.8`, otherwise `"low"`.
    """
    ...


def keep_valid_scores(
    scores: dict[str, float | None],
) -> dict[str, float]:
    """Keep only the scores that are present.

    Args:
        scores: A mapping from name to score, where a score of `None`
            means the value is missing. Must not be mutated by this
            function.

    Returns:
        A new dict containing every entry from `scores` whose score is
        not `None`. A score of `0` or `0.0` is valid and must be kept —
        checking truthiness instead of `is not None` would incorrectly
        drop it.
    """
    ...
