"""Tests for Homework 06: comprehension functions.

Write at least 25 meaningful test cases covering the behaviors below.
Replace the `...` placeholder in each test with your assertions, and
delete any case you choose not to cover.
"""

import pytest

from notes.hw06 import (
    square_positive,
    normalize_names,
    unique_lengths,
    score_labels,
    keep_valid_scores,
)


# ---------------------------------------------------------------------------
# square_positive
# ---------------------------------------------------------------------------

def test_square_positive_squares_positive_values_case():
    """Positive values are squared."""
    ...


def test_square_positive_excludes_negative_values_case():
    """Negative values are removed entirely, not squared."""
    ...


def test_square_positive_excludes_zero_case():
    """Zero is removed entirely."""
    ...


def test_square_positive_preserves_order_case():
    """Surviving values keep their original relative order."""
    ...


def test_square_positive_empty_input_case():
    """An empty list returns an empty list."""
    ...


def test_square_positive_does_not_mutate_input_case():
    """The caller's list is left unchanged by the call."""
    ...


# ---------------------------------------------------------------------------
# normalize_names
# ---------------------------------------------------------------------------

def test_normalize_names_strips_whitespace_case():
    """Leading and trailing whitespace is removed."""
    ...


def test_normalize_names_lowercases_case():
    """Names are converted to lowercase."""
    ...


def test_normalize_names_removes_blank_names_case():
    """A name that is empty or whitespace-only after stripping is removed."""
    ...


def test_normalize_names_already_normalized_case():
    """A name that is already stripped and lowercase is unchanged."""
    ...


def test_normalize_names_empty_input_case():
    """An empty list returns an empty list."""
    ...


def test_normalize_names_mixed_batch_case():
    """A batch mixing whitespace, casing, and a blank entry is handled at once."""
    ...


def test_normalize_names_does_not_mutate_input_case():
    """The caller's list is left unchanged by the call."""
    ...


# ---------------------------------------------------------------------------
# unique_lengths
# ---------------------------------------------------------------------------

def test_unique_lengths_collapses_duplicates_case():
    """Duplicate word lengths collapse into a single set entry."""
    ...


def test_unique_lengths_empty_input_case():
    """An empty list returns an empty set."""
    ...


# ---------------------------------------------------------------------------
# score_labels
# ---------------------------------------------------------------------------

def test_score_labels_high_case():
    """A score above 0.8 is labeled 'high'."""
    ...


def test_score_labels_low_case():
    """A score below 0.8 is labeled 'low'."""
    ...


def test_score_labels_boundary_case():
    """A score of exactly 0.8 is labeled 'high' (the threshold is inclusive)."""
    ...


def test_score_labels_empty_input_case():
    """An empty dict returns an empty dict."""
    ...


# ---------------------------------------------------------------------------
# keep_valid_scores
# ---------------------------------------------------------------------------

def test_keep_valid_scores_removes_none_case():
    """An entry whose score is exactly None is dropped."""
    ...


def test_keep_valid_scores_keeps_zero_case():
    """A score of 0 or 0.0 is kept, not treated as falsy."""
    ...


def test_keep_valid_scores_keeps_negative_case():
    """A negative score is kept — only None is filtered."""
    ...


def test_keep_valid_scores_empty_input_case():
    """An empty dict returns an empty dict."""
    ...


def test_keep_valid_scores_mixed_batch_case():
    """A batch mixing None, zero, a positive, and a negative score is handled at once."""
    ...


def test_keep_valid_scores_does_not_mutate_input_case():
    """The caller's dict is left unchanged by the call."""
    ...
