__author__ = "730761420"


def only_evens(list1: list[int]) -> list:
    """compiles all the even integers from an inputted list into a new list"""

    new_list: list[int] = []

    for num in range(0, len(list1)):
        if list1[num] % 2 == 0:
            new_list.append(list1[num])
        else:
            new_list = new_list

    return new_list


def sub(list1: list[int], start_idx: int, end_idx: int) -> list:
    (
        """this function creates a shortened list from the inputted list bounded by
        a given start and end index. The start index is included, while the end index
        is excluded"""
    )

    new_list: list[int] = []

    if len(list1) == 0:
        new_list = new_list
    else:
        if start_idx < 0 and end_idx > len(list1):
            new_list = list1
        elif start_idx < 0 or end_idx > len(list1):
            if start_idx < 0:
                for num in range(0, len(list1)):
                    if num >= 0 and num < end_idx:
                        new_list.append(list1[num])
                    else:
                        new_list = new_list
            elif end_idx > len(list1):
                for num in range(0, len(list1)):
                    if num >= start_idx and num < len(list1):
                        new_list.append(list1[num])
                    else:
                        new_list = new_list
        else:
            for num in range(0, len(list1)):
                if num >= start_idx and num < end_idx:
                    new_list.append(list1[num])

    return new_list


def add_at_index(list1: list[int], element: int, idx: int) -> None:
    if idx < 0 or idx > len(list1):
        raise IndexError("Index is out of bounds for the index list")
    else:
        temp_list: list = []

        for nums in range(idx, len(list1)):
            temp_list.append(list1[nums])

        for nums in range(idx, len(list1)):
            list1.pop(nums)

        list1.append(element)

        for nums in range(0, len(temp_list)):
            list1.append(temp_list[nums])
