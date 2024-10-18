from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest

__author__ = "730761420"


def test_only_evens_usecase_1() -> None:
    (
        """basic test to see if the function only_evens
    removes all the odd numbers in the list"""
    )
    assert only_evens([1, 2, 3, 4, 5, 6]) == [2, 4, 6]


def test_only_evens_edgecase() -> None:
    (
        """test to confirm that an empty list inputted to
    only_evens will return and empty list"""
    )
    assert only_evens([]) == []


def test_only_evens_usecase_2() -> None:
    (
        """test to confirm that only_evens will return an empty
     list when given a list of only odd numbers"""
    )
    assert only_evens([1, 3, 5]) == []


def test_sub_caseuse_1() -> None:
    """test of the basic purpose and use of the function"""
    assert sub([1, 2, 3, 4, 5], 1, 4) == [2, 3, 4]


def test_sub_caseuse_2() -> None:
    (
        """test to show that inputting a start and end index out of the bounds of the
    indices of the list will return the whole inputted list"""
    )
    assert sub([1, 2, 3, 4, 5], -1, 5) == [1, 2, 3, 4, 5]


def test_sub_caseuse_3() -> None:
    assert sub([1, 2, 3, 4, 5], -1, 4) == [1, 2, 3, 4]


def test_sub_caseuse_4() -> None:
    assert sub([1, 2, 3, 4, 5], 2, 6) == [3, 4, 5]


def test_sub_edgecase() -> None:
    """empty list will return an empty list"""
    assert sub([], 1, 4) == []


def test_add_at_index_caseuse_1() -> None:
    """testing the insertion of a number into the middle of the list"""
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
    """testing the insertion of a number to the end of the list"""
    test_list: list = [2, 4, 6]
    add_at_index(test_list, 8, 3)
    assert test_list == [2, 4, 6, 8]
