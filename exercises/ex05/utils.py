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


def add_at_index(list1: list[int], element: int, idx: int) -> None:
    if idx < 0 or idx > len(list1):
        raise IndexError("Index is out of bounds for the index list")
    else:
        temp_list: list = []

        for nums in range(idx, len(list1)):
            temp_list.append(nums)

        for nums in range(idx, len(list1)):
            list1.pop(nums)

        list1.append(element)

        for nums in range(0, len(temp_list)):
            list1.append(temp_list[nums])
