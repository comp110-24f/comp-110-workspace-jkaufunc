"""implementing algorithms to practice computational thinking"""

__author__ = "730761420"


def all(list: list[int], num: int) -> bool:
    (
        """if every item in 'list' equals 'int', the function will return 'True', else
      it returns 'False'"""
    )
    condition: bool = False
    for item in list:
        if item != num:
            condition = False
        else:
            condition = True
    return condition


# print(all([1, 1, 1], 1))


def max(list: list[int]) -> int:
    """the max function will return the largest number in a list of integers"""

    if len(list) == 0:
        raise (ValueError("max() arg is an empty List"))

    max_num: int = list[0]

    for item in list:
        if item > max_num:
            max_num = item
        else:
            max_num = max_num
    return max_num


def is_equal(list1: list[int], list2: list[int]) -> bool:
    (
        """returns 'True' if every the items at all respective indexes
    of each list match, else it returns 'False'"""
    )

    condition: bool = True

    if len(list1) != len(list2):
        condition = False
    else:
        for idx in range(0, len(list1)):
            if list1[idx] != list2[idx]:
                condition = False
            else:
                condition = True

    return condition


def extend(list1: list[int], list2: list[int]) -> None:
    """This function appends the itmes from the second list to the end of the first"""
    for idx in range(0, len(list2)):
        list1.append(list2[idx])
