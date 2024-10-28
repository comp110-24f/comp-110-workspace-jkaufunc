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

    color_count: dict[int, str] = {}

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
        color_count[1] = names_colors[key]

    new_color_count: dict[int, str] = {}

    for key in color_count:
        color: str = color_count[key]
        count: int = 0
        if key == key + 1:
            count += 1
        new_color_count[count] = color

    for key in new_color_count:
        if key >= key + 1:
            fav = new_color_count[key]

    return fav


# try switching the order of types in the dictionary color_count, e.i. dict[int, str]
#   to allow the use of indexing


color_dict: dict[str, str] = {"James": "blue", "Andy": "purple", "Timmy": "blue"}

print(favorite_color(color_dict))
