"""Validated one-pass aggregation examples."""

import math
from collections.abc import Iterable, Mapping

def _require_non_empty_text(
    value: object,
    *,
    field: str,
    index: int,
) -> str:
    """Validate and return a required nonempty string."""
    if not isinstance(value, str) or not value.strip():
        raise ValueError(
            f"record {index}: {field} must be a nonempty string"
        )

    return value

services = [
    {"service": "auth", "latency_ms": 120},
    {"service": "auth", "latency_ms": 80},
    {"service": "auth", "latency_ms": 0},
    {"service": "payments", "latency_ms": 200},
    {"service": "payments", "latency_ms": None},
]

def average_latency_by_service(
    records: Iterable[Mapping[str, object]],
) -> dict[str, float]:
    """Return the average valid latency for each service.

    Latencies whose value is None are ignored. The function reads
    its input records but never mutates them.
    """
    totals: dict[str, float] = {}
    counts: dict[str, int] = {}

    for index, record in enumerate(records):
        if not isinstance(record, Mapping):
            raise TypeError(
                f"record {index}: expected a mapping"
            )

        service = _require_non_empty_text(
            record.get("service"),
            field="service",
            index=index,
        )

        if "latency_ms" not in record:
            raise ValueError(
                f"record {index}: latency_ms is required"
            )

        raw_latency = record["latency_ms"]

        if raw_latency is None:
            continue

        if isinstance(raw_latency, bool) or not isinstance(
            raw_latency,
            (int, float),
        ):
            raise TypeError(
                f"record {index}: "
                "latency_ms must be a number or None"
            )

        latency = float(raw_latency)

        if not math.isfinite(latency):
            raise ValueError(
                f"record {index}: latency_ms must be finite"
            )

        if latency < 0:
            raise ValueError(
                f"record {index}: latency_ms cannot be negative"
            )

        totals[service] = (
            totals.get(service, 0.0) + latency
        )
        counts[service] = (
            counts.get(service, 0) + 1
        )

    return {
        service: totals[service] / counts[service]
        for service in totals
    }

print(average_latency_by_service(services))
    
# Tradeoffs and alternatives:

# Two dictionaries (current implementation) 🟡
# totals: dict[str, float]
# counts: dict[str, int]

# Advantages:
# low memory
# directly represents the mathematics

# Disadvantage:
# related state is split across two structures

# Dictionary of tuples 🟡
# state: dict[str, tuple[float, int]] = {}
# total, count = state.get(user_id, (0.0, 0))
# state[user_id] = (total + score, count + 1)

# Advantages:
# all state for one group remains together
# tuple is simple and immutable

# Disadvantage:
# tuple positions can be less readable
# a new tuple is created for each update

# Dictionary of small objects (we'll discuss more later) 🟡
# @dataclass
# class RunningAverage:
#     total: float = 0.0
#     count: int = 0
    
# Advantages:
# descriptive fields
# easy to extend with minimum, maximum, or variance

# Disadvantages:
# more code
# unnecessary for a small two-value exercise

# Storing every score 🟡
# scores_by_user: dict[str, list[float]]

# Advantages:
# preserves all observations;
# allows median, percentiles, and later analysis.

# Disadvantages:
# space becomes O(n), rather than O(k) [n = number of entries, k = number of unique users]
# unnecessary when only the mean is required
# exposes more mutable nested state



# Complexity questions:
# What does (n) represent?
# What does (k) represent?
# Why is the main loop expected (O(n))?
# Why is the final result construction (O(k))?
# Why does (O(n+k)) simplify to (O(n))?
# Why is auxiliary space (O(k))?
# What dictionary-operation assumption does the analysis use?
# What would the complexity be if you scanned the complete input once for every user?