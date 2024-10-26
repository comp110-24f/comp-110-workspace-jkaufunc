__author__ = "730761420"

"""writing functions to practice using and manipulating dictionaries"""


def invert(x: dict[str, str]) -> dict[str, str]:
    """function inverts the keys and values of an inputted list"""
    new_dict: dict[str, str] = {}
    """
    count: int = 0
    for first_key in x:
        for key in x:
            if first_key == key:
                count += 1
    if count > 1:
        raise KeyError("two keys in the inputted list cannot have the same value")
    """
    for key in x:
        new_dict[x[key]] = key

    return new_dict


test_dict: dict[str, str] = {"hello": "world", "happy": "birthday"}
test_dict_2: dict[
    str,
    str,
] = {"happy": "day", "sunny": "day"}

print(test_dict)
