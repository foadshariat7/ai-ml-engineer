from collections.abc import Sequence
from copy import deepcopy


def with_metric(
    metric: float,
    history: Sequence[float] | None = None,
) -> list[float]:
    if history is None:
        result: list[float] = []
    else:
        result = list(history)

    result.append(metric)
    return result


def record_metric_in_place(
    metric: float,
    history: list[float],
) -> None:
    history.append(metric)


def same_object(left: object, right: object) -> bool:
    return left is right


def same_value(left: object, right: object) -> bool:
    return left == right


def shallow_clone_batches(
    batches: list[list[int]],
) -> list[list[int]]:
    return batches.copy()


def deep_clone_batches(
    batches: list[list[int]],
) -> list[list[int]]:
    return deepcopy(batches)