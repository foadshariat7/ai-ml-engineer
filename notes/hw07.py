"""Homework 07: Functions, arguments, closures, and recursion.

Implement each function below according to its docstring. Do not change
any function signatures. Replace the `...` placeholder in each function
body with your implementation.
"""

from collections.abc import Callable


def clamp_score(
    score: float,
    minimum: float = 0.0,
    maximum: float = 1.0,
) -> float:
    """Clamp a score into the inclusive range `[minimum, maximum]`.

    Args:
        score: The score to clamp.
        minimum: The lowest allowed value. Defaults to `0.0`.
        maximum: The highest allowed value. Defaults to `1.0`.

    Returns:
        `minimum` if `score` is below it, `maximum` if `score` exceeds
        it, otherwise `score` unchanged. For example,
        `clamp_score(-0.3)` returns `0.0`, `clamp_score(0.6)` returns
        `0.6`, and `clamp_score(1.8)` returns `1.0`.

    Raises:
        ValueError: If `minimum` is greater than `maximum`.
    """
    ...


def metric_report(
    name: str,
    *scores: float,
    precision: int = 3,
) -> dict[str, object]:
    """Build a summary report for a named metric.

    Args:
        name: The metric's name, such as `"validation"`.
        *scores: Any number of scores, collected into a tuple.
        precision: The number of decimal places to round the average
            to. Defaults to `3`. Because it follows `*scores`, it is
            keyword-only — it can only be supplied as `precision=...`.

    Returns:
        A new dict of the form
        `{"name": name, "scores": scores, "average": average}`, where
        `scores` stays a tuple and `average` is the mean of the scores
        rounded to `precision` places, or `None` if no scores were
        supplied. For example,
        `metric_report("validation", 0.8, 0.9, precision=2)` returns
        `{"name": "validation", "scores": (0.8, 0.9), "average": 0.85}`.
    """
    ...


def build_config(
    model: str,
    **options: object,
) -> dict[str, object]:
    """Build a configuration dict from a model name and keyword options.

    Args:
        model: The model's name.
        **options: Any number of extra keyword options, collected into
            a dict. A caller's dict unpacked here with `**` must not be
            mutated by this function.

    Returns:
        A new dict of the form `{"model": model, **options}`, where
        every supplied option becomes an ordinary dictionary entry.
        Supplying `model` twice through argument binding (for example
        `build_config("a", **{"model": "b"})`) is rejected by Python
        itself with a `TypeError` before the body ever runs.
    """
    ...


def apply_transform(
    values: list[float],
    transform: Callable[[float], float],
) -> list[float]:
    """Apply a transform function to every value.

    Args:
        values: The values to transform. Must not be mutated by this
            function.
        transform: A function taking one float and returning a float.
            It must be called exactly once per input value.

    Returns:
        A new list containing `transform(value)` for every `value` in
        `values`, in the original order. For example, with
        `double = lambda value: value * 2`,
        `apply_transform([1.0, 2.0, 3.0], double)` returns
        `[2.0, 4.0, 6.0]`.
    """
    ...


def make_threshold_checker(
    threshold: float,
) -> Callable[[float], bool]:
    """Create a function that checks whether a value meets a threshold.

    Args:
        threshold: The minimum value considered "high". The returned
            function must remember its own threshold, so two
            independently created checkers never interfere.

    Returns:
        A function taking one float that returns `True` if the value
        is greater than or equal to `threshold`, otherwise `False`. For
        example, with `is_high = make_threshold_checker(0.8)`,
        `is_high(0.7)` is `False`, `is_high(0.8)` is `True`, and
        `is_high(0.9)` is `True`.
    """
    ...


def make_running_total(
    start: float = 0.0,
) -> Callable[[float], float]:
    """Create a function that keeps a running total across calls.

    Must use a closure and `nonlocal` — not a global variable — so
    separate instances maintain separate state.

    Args:
        start: The initial total. Defaults to `0.0`.

    Returns:
        A function taking one float that adds it to the running total
        and returns the new total. For example, with
        `total = make_running_total()`, `total(2.0)` returns `2.0`,
        then `total(3.0)` returns `5.0`, then `total(-1.0)` returns
        `4.0`.
    """
    ...


def factorial(
    value: int,
) -> int:
    """Compute `value!` recursively.

    Must be implemented recursively, without `math.factorial`.

    Args:
        value: A non-negative integer. `0! == 1`.

    Returns:
        The factorial of `value`.

    Raises:
        TypeError: If `value` is not an `int`, including `bool` values
            (which must not silently become `0` or `1`) and floats.
        ValueError: If `value` is negative.
    """
    ...
