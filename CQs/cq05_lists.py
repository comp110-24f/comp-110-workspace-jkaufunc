"""Mutating functions"""

__author__ = "730761420"


def manual_append(my_list: list[int], x: int) -> None:
    (
        """the function will mutate its input by appending
    the int parameter to the end of the list[int] parameter."""
    )

    my_list.append(x)
    print(my_list)


# manual_append([1, 2, 3], 5)


def double(x: list[int]) -> None:
    """this function will mutate the input by multiplying all the terms by 2"""

    idx: int = 0

    while idx < len(x):
        x[idx] = x[idx] * 2
        idx += 1

    print(x)


# double([5, 10, 15])

list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

# double(list_2)

# print(list_1)
# print(list_2)

# I think they will be the same
# If doulbe(list_2) is printed, I think it will print [2, 4, 6]

# Dang, all three were [2, 4, 6]!!! I guess I should have known,
#   but it is kind of confusing
