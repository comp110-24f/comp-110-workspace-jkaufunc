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

    fav: str = ""

    color_count: dict[str, int] = {}

    for key in names_colors:
        if key in color_count:
            color_count[key] += 1
        else:
            color_count[key] = 1

    count_list: list[int] = []
    color_list: list[str] = []

    for key in names_colors:
        count_list.append(color_count[key])

    for key in names_colors:
        color_list.append(key)

    for idx in range(0, len(count_list)):
        count: int = 0
        if idx >= count:
            count = idx

        fav = fav

    return fav

    """
    color_count: dict[int, str] = {}

    for key in names_colors:
        for key_2 in color_count:
            if key_2 == names_colors[key]:
                color_count[key_2] += 1
            else:
                color_count[key_2] = 1

    print(color_count)
    """
    """
    for key in names_colors:
        color_count[1] = names_colors[key]

    print(color_count)

    new_color_count: dict[int, str] = {}

    count: int = 0

    for key in range(0, len(color_count) - 1):
        color: str = color_count[key]
        for key_2 in color_count:
            if color_count[key] == color_count[key_2]:
                count += 1
            new_color_count[count] = color
            count: int = 0

    for key in range(0, len(new_color_count) - 1):
        if key >= key + 1:
            fav = new_color_count[key]

    print(new_color_count)
    print(fav)

    return fav
    """
    # try switching the order of types in the dictionary color_count,
    # e.i. dict[int, str] to allow the use of indexing

    """
    names_list: list[str] = []

    color_list: list[str] = []

    fav: str = ""

    for key in names_colors:
        names_list.append(key)
    for key in names_colors:
        color_list.append(names_colors[key])

    color_count: dict[str, int] = {}

    # print(names_list)
    # print(color_list)
    """

    """
    for idx in names_list:
        color_count[idx] = 0

    indx: int = 0
    idx_2: int = 1
    while indx in range(indx, len(color_list) - 1):
        while idx_2 in range(idx_2, len(color_list)):
            count: int = 1
            if color_list[indx] == color_list[idx_2]:
                count += 1
                color_list.pop(idx_2)
            else:
                idx_2 += 1
        color_count[color_list[indx]] = count
        indx += 1
        idx_2 += 1
    for key in color_count:
        for key_2 in color_count:
            if color_count[key] >= color_count[key_2]:
                fav = key
    """
    return fav


color_dict_1: dict[str, str] = {"James": "blue", "Andy": "purple", "Timmy": "blue"}
color_dict_2: dict[str, str] = {
    "Gerald": "red",
    "Elmo": "red",
    "Bob": "yellow",
    "Big Bird": "yellow",
    "Blaze": "yellow",
    "James": "blue",
}
color_dict_3: dict[str, str] = {
    "Gerald": "red",
    "Jessie": "green",
    "Elmo": "red",
    "James": "blue",
    "Holley": "green",
}


print(favorite_color(color_dict_1))
print(favorite_color(color_dict_2))
print(favorite_color(color_dict_3))
