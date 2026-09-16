"""Homework 04: Dictionaries, sets, and one-pass aggregation.

Implement the function below according to its docstring. Do not change
the function signature. Replace the `...` placeholder in the function
body with your implementation.

Write this from a blank file rather than adapting existing work: do not
copy the latency implementation and merely rename its variables.
"""


def average_scores(
    records: list[dict[str, object]],
) -> dict[str, float]:
    """Average each user's valid scores in a single pass.

    Each valid record is shaped like:

        {
            "user_id": "u123",
            "score": 0.82,
        }

    Args:
        records: The records to aggregate, grouped by `user_id`. Must
            not be mutated by this function, and must be traversed
            exactly once.

    Returns:
        A mapping from `user_id` to the mean of that user's valid
        scores. A record whose `score` is exactly None is ignored, so a
        user whose scores are all None is absent from the result
        entirely. Scores of `0` and `0.0` are valid and are included.
        Both ints and floats are accepted. Returns an empty dict when
        `records` is empty.

    Raises:
        TypeError: If a `score` is a Boolean, or is neither an int nor
            a float.
        ValueError: If `user_id` is missing, is not a string, or is
            empty or whitespace-only; if the `score` field is missing;
            or if a `score` is negative, NaN, or positive/negative
            infinity.

    Every validation message raised above must include the index of the
    offending record.
    """
    ...
