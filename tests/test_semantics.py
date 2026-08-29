from ai_ml_engineer.semantics import (
    deep_clone_batches,
    record_metric_in_place,
    same_object,
    same_value,
    shallow_clone_batches,
    with_metric,
)


def test_with_metric_uses_fresh_default_each_call() -> None:
    assert with_metric(0.8) == [0.8]
    assert with_metric(0.7) == [0.7]


def test_with_metric_does_not_mutate_input() -> None:
    original = [0.8]
    result = with_metric(0.7, original)

    assert original == [0.8]
    assert result == [0.8, 0.7]
    assert result is not original


def test_record_metric_in_place_mutates_input() -> None:
    original = [0.8]
    result = record_metric_in_place(0.7, original)

    assert result is None
    assert original == [0.8, 0.7]


def test_identity_and_equality_answer_different_questions() -> None:
    left = [1, 2]
    right = [1, 2]

    assert same_value(left, right) is True
    assert same_object(left, right) is False
    assert same_object(left, left) is True


def test_shallow_copy_shares_nested_lists() -> None:
    original = [[1, 2], [3]]
    clone = shallow_clone_batches(original)

    original[0].append(99)

    assert clone is not original
    assert clone[0] is original[0]
    assert clone == [[1, 2, 99], [3]]


def test_deep_copy_has_independent_nested_lists() -> None:
    original = [[1, 2], [3]]
    clone = deep_clone_batches(original)

    original[0].append(99)

    assert clone is not original
    assert clone[0] is not original[0]
    assert clone == [[1, 2], [3]]