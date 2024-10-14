__author__ = "730761420"


def only_evens(list1: list[int]) -> list:
    """compiles all the even integers from an inputted list into a new list"""

    new_list: list[int] = []

    for num in list1:
        if num % 2 == 0:
            new_list.append(list1[num])
        else:
            new_list = new_list

    print(new_list)

    return new_list


def sub(list1: list[int], start_idx: int, end_index: int) -> list:
    (
        """this function creates a shortened list from the inputted list bounded by
        a given start and end index"""
    )

    new_list: list[int] = []

    for idx in list1:
        if start_idx <= idx < end_index:
            new_list.append(list1[idx])
        else:
            new_list = new_list

    return new_list
