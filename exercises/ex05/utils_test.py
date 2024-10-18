from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_only_evens_usecase_1() -> None:
    assert only_evens([1, 2, 3, 4, 5, 6]) == [2, 4, 6]


def test_only_evens_edgecase() -> None:
    assert only_evens([]) == []


def test_only_evens_usecase_2() -> None:
    assert only_evens([1, 3, 5]) == []


def test_sub_caseuse_1() -> None:
    assert sub([1, 2, 3, 4, 5], 1, 4) == [2, 3, 4]


def test_sub_caseuse_2() -> None:
    assert sub([1, 2, 3, 4, 5], -1, 5) == [1, 2, 3, 4, 5]


def test_sub_edgecase() -> None:
    assert sub([], 1, 4) == []


def test_add_at_index_caseuse_1() -> None:
    test_list: list = [1, 2, 4]
    add_at_index(test_list, 3, 2)
    assert test_list == [1, 2, 3, 4]


def test_add_at_index_raises_indexerror():
    """Test that add_at_index raises an IndexError for an invalid index."""
    # your object to pass to add_at_index function
    with pytest.raises(IndexError):
        add_at_index([1, 2, 4], 3, -1)

    with pytest.raises(IndexError):
        add_at_index([], 4, 7)


def test_add_at_index_caseuse_2() -> None:
    test_list: list = [2, 4, 6]
    add_at_index(test_list, 8, 3)
    assert test_list == [2, 4, 6, 8]
