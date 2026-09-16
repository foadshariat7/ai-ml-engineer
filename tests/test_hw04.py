"""Tests for Homework 04: `average_scores`.

Write at least 14 meaningful test cases covering the behaviors below.
Replace the `...` placeholder in each test with your assertions, and
delete any case you choose not to cover.
"""

import pytest

from notes.hw04 import average_scores


def test_repeated_user_case():
    """One user appearing in several records averages to their mean."""
    ...


def test_multiple_user_case():
    """Several independent users are averaged separately."""
    ...


def test_ignore_none_score_case():
    """A score of exactly None is ignored rather than counted as 0."""
    ...


def test_user_with_only_none_case():
    """A user whose scores are all None is absent from the result."""
    ...


def test_zero_score_included_case():
    """Scores of 0 and 0.0 are valid and counted, not treated as falsy."""
    ...


def test_integer_score_accepted_case():
    """Integer scores are accepted alongside floats."""
    ...


def test_empty_input_case():
    """Empty input returns an empty dict."""
    ...


def test_negative_score_case():
    """A negative score raises ValueError."""
    ...


def test_non_numeric_score_case():
    """A score that is neither int nor float raises TypeError."""
    ...


def test_boolean_score_case():
    """A Boolean score raises TypeError, despite bool subclassing int."""
    ...


def test_nan_score_case():
    """A NaN score raises ValueError."""
    ...


def test_positive_infinity_score_case():
    """A positive-infinity score raises ValueError."""
    ...


def test_negative_infinity_score_case():
    """A negative-infinity score raises ValueError."""
    ...


def test_missing_user_case():
    """A record with no `user_id` key raises ValueError."""
    ...


def test_blank_user_case():
    """An empty or whitespace-only `user_id` raises ValueError."""
    ...


def test_non_string_user_case():
    """A `user_id` that is not a string raises ValueError."""
    ...


def test_missing_score_case():
    """A record with no `score` key raises ValueError."""
    ...


def test_input_not_mutated_case():
    """The caller's records are left unchanged by the call."""
    ...


def test_float_precision_case():
    """A float average compares equal via `pytest.approx`."""
    ...


def test_error_message_index_case():
    """A validation message names the index of the offending record."""
    ...
