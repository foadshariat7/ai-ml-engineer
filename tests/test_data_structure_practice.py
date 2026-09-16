from copy import deepcopy
from math import inf, nan

import pytest

from ai_ml_engineer._04_data_structure_practice import (
    average_latency_by_service,
)


def test_returns_average_by_service() -> None:
    records = [
        {"service": "api", "latency_ms": 100.0},
        {"service": "worker", "latency_ms": 50.0},
        {"service": "api", "latency_ms": 140.0},
    ]

    assert average_latency_by_service(records) == {
        "api": 120.0,
        "worker": 50.0,
    }


def test_ignores_none_values() -> None:
    records = [
        {"service": "api", "latency_ms": None},
        {"service": "api", "latency_ms": 80.0},
        {"service": "unused", "latency_ms": None},
    ]

    assert average_latency_by_service(records) == {
        "api": 80.0,
    }


def test_zero_is_a_valid_latency() -> None:
    records = [
        {"service": "cache", "latency_ms": 0.0},
        {"service": "cache", "latency_ms": 10.0},
    ]

    result = average_latency_by_service(records)

    assert result["cache"] == 5.0


def test_rejects_negative_latency() -> None:
    with pytest.raises(
        ValueError,
        match="cannot be negative",
    ):
        average_latency_by_service(
            [{"service": "api", "latency_ms": -1.0}]
        )


@pytest.mark.parametrize(
    "service",
    [None, "", "   ", 123],
)
def test_rejects_invalid_service(
    service: object,
) -> None:
    with pytest.raises(
        ValueError,
        match="nonempty string",
    ):
        average_latency_by_service(
            [
                {
                    "service": service,
                    "latency_ms": 10.0,
                }
            ]
        )


def test_requires_latency_field() -> None:
    with pytest.raises(
        ValueError,
        match="latency_ms is required",
    ):
        average_latency_by_service(
            [{"service": "api"}]
        )


@pytest.mark.parametrize(
    "latency",
    ["10", [], {}, True],
)
def test_rejects_non_numeric_latency(
    latency: object,
) -> None:
    with pytest.raises(
        TypeError,
        match="number or None",
    ):
        average_latency_by_service(
            [
                {
                    "service": "api",
                    "latency_ms": latency,
                }
            ]
        )


@pytest.mark.parametrize(
    "latency",
    [nan, inf, -inf],
)
def test_rejects_non_finite_latency(
    latency: float,
) -> None:
    with pytest.raises(
        ValueError,
        match="must be finite",
    ):
        average_latency_by_service(
            [
                {
                    "service": "api",
                    "latency_ms": latency,
                }
            ]
        )


def test_does_not_mutate_input() -> None:
    records = [
        {"service": "api", "latency_ms": 100.0},
        {"service": "api", "latency_ms": None},
    ]
    snapshot = deepcopy(records)

    average_latency_by_service(records)

    assert records == snapshot


def test_accepts_one_pass_generator() -> None:
    records = (
        {"service": "api", "latency_ms": value}
        for value in [10.0, 20.0]
    )

    assert average_latency_by_service(records) == {
        "api": 15.0,
    }


def test_uses_approximate_float_comparison() -> None:
    records = [
        {"service": "api", "latency_ms": 0.1},
        {"service": "api", "latency_ms": 0.2},
    ]

    result = average_latency_by_service(records)

    assert result["api"] == pytest.approx(0.15)