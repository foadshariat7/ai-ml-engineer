"""Homework 02: Mutability and copying.

Implement each function below according to its docstring. Do not change
any function signatures. Replace the `...` placeholder in each function
body with your implementation.
"""

from collections.abc import Sequence


def add_loss(
    loss: float,
    history: Sequence[float] | None = None,
) -> list[float]:
    """Append a loss value to a training history without mutating the input.

    Args:
        loss: The loss value to append.
        history: The existing history, or None to start a fresh history.

    Returns:
        A new list containing every value in `history`, in order,
        followed by `loss`. The caller-provided `history` is left
        unchanged. If `history` is None, the result contains only
        `loss`.
    """
    ...


def add_loss_in_place(
    loss: float,
    history: list[float],
) -> None:
    """Append a loss value to a training history in place.

    Args:
        loss: The loss value to append.
        history: The list to mutate. Modified directly by this call.

    Returns:
        None. `history` is mutated in place rather than replaced.
    """
    ...


def clone_folds(
    folds: list[list[int]],
    *,
    deep: bool = False,
) -> list[list[int]]:
    """Copy a list of cross-validation folds.

    Args:
        folds: The folds to copy. Must not be mutated by this function.
        deep: Keyword-only (the `*` before it forbids passing it
            positionally, e.g. `clone_folds(folds, deep=True)` rather
            than `clone_folds(folds, True)`). When False, perform a
            shallow copy: the returned outer list is new, but its
            inner lists are the same objects as in `folds`. When True,
            perform a deep copy: the inner lists are also new,
            independent objects.

    Returns:
        The copied folds, per the `deep` flag described above.
    """
    ...


def same_object(left: object, right: object) -> bool:
    """Check whether two references point to the same object in memory.

    Args:
        left: The first value to compare.
        right: The second value to compare.

    Returns:
        True if `left` and `right` are identical (`left is right`),
        False otherwise. Note that this is stricter than value
        equality: two equal but distinct objects should return False.
    """
    ...


def same_value(left: object, right: object) -> bool:
    """Check whether two values are equal.

    Args:
        left: The first value to compare.
        right: The second value to compare.

    Returns:
        True if `left == right`, False otherwise. Note that this
        compares by value, not by identity: two distinct objects with
        equal contents should return True.
    """
    ...


def shallow_clone_batches(
    batches: list[list[int]],
) -> list[list[int]]:
    """Shallow-copy a list of batches.

    Args:
        batches: The batches to copy. Must not be mutated by this
            function.

    Returns:
        A new outer list containing the same inner list objects as
        `batches`. Mutating an inner list in the result will therefore
        also affect the corresponding inner list in `batches`.
    """
    ...


def deep_clone_batches(
    batches: list[list[int]],
) -> list[list[int]]:
    """Deep-copy a list of batches.

    Args:
        batches: The batches to copy. Must not be mutated by this
            function.

    Returns:
        A new outer list containing new, independent inner lists with
        the same values as `batches`. Mutating the result, at any
        depth, must never affect `batches`.
    """
    ...
