from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max() -> None:
    assert find_and_remove_max([1, 2, 3, 4, 5]) == 5

    test_list: list = [2, 4, 6, 8]
    find_and_remove_max(test_list)

    assert test_list == [2, 4, 6]

    assert find_and_remove_max([]) == -1
