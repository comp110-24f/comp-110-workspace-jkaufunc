__author__ = "730761420"

"""writing functions to practice using and manipulating dictionaries"""


def invert(x: dict[str, str]) -> dict[str, str]:
    """function inverts the keys and values of an inputted list"""
    new_dict: dict[str, str] = {}

    count: int = 0
    for first_key in x:
        for key in x:
            if first_key == key:
                count += 1
    if count > 1:
        raise KeyError("two keys in the inputted list cannot have the same value")

    for key in x:
        new_dict[x[key]] = key

    return new_dict


test_dict: dict[str, str] = {"hello": "world", "happy": "birthday"}
test_dict_2: dict[
    str,
    str,
] = {"happy": "day", "sunny": "day"}
test_dict_3: dict[str, str] = {"happy": "day", "hello": "world", "sunny": "day"}

# print(invert(test_dict_2))
# print(invert(test_dict_3))
# the result for both tests is a KeyError as expected


def favorite_color(names_colors: dict[str, str]) -> str:
    """returns the most frequent color"""

    color_count: dict[str, int] = {}

    fav: str = ""

    """
    for key in names_colors:
        for key_2 in color_count:
            if key_2 == names_colors[key]:
                color_count[key_2] += 1
            else:
                color_count[key_2] = 1

    print(color_count)
    """

    for key in names_colors:
        color_count[key] = 1

    print(color_count)

    for key in color_count:
        count: int = 1
        for key_2 in color_count:
            if key == key_2:
                count += 1
        color_count[key] = count

    print(color_count)

    for key in color_count:
        for key_2 in color_count:
            if color_count[key] >= color_count[key_2]:
                fav = key

    return fav


# try switching the order of types in the dictionary color_count, e.i. dict[int, str]
#   to allow you to use indexing


color_dict: dict[str, str] = {"James": "blue", "Andy": "purple", "Timmy": "blue"}

print(favorite_color(color_dict))
