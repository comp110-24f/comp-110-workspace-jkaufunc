from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max_use_case_1() -> None:
    assert find_and_remove_max([1, 2, 3, 5, 5, 4]) == 5


def test_find_and_remove_max_use_case_2() -> None:
    test_list: list = [2, 4, 6, 8]
    find_and_remove_max(test_list)

    assert test_list == [2, 4, 6]


def test_find_and_remove_max_edge_case() -> None:
    assert find_and_remove_max([]) == -1
