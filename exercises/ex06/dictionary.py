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

    # test_dict: dict[str, str] = {"hello": "world", "happy": "birthday"}
    # test_dict_2: dict[str,str,] = {"happy": "day", "sunny": "day"}
    # test_dict_3: dict[str, str] = {"happy": "day", "hello": "world", "sunny": "day"}

    # print(invert(test_dict_2))
    # print(invert(test_dict_3))
    # the result for both tests is a KeyError as expected


def favorite_color(names_colors: dict[str, str]) -> str:
    """returns the most frequent color"""

    fav: str = ""

    color_count: dict[str, int] = {}

    for key in names_colors:
        color: str = names_colors[key]
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1

    print(color_count)

    count: int = 0

    for key in color_count:
        if color_count[key] > count:
            count = color_count[key]
            fav = key

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

    # color_dict_1: dict[str, str] = {"James": "blue", "Andy": "purple",
    #   "Timmy": "blue"}
    # color_dict_2: dict[str, str] = {"Gerald": "red","Elmo": "red","Bob": "yellow",
    #   "Big Bird": "yellow","Blaze": "yellow","James": "blue",}
    # color_dict_3: dict[str, str] = {"Gerald": "red","Jessie": "green","Elmo": "red",
    #   "James": "blue","Holley": "green",}

    # print(favorite_color(color_dict_1))
    # print(favorite_color(color_dict_2))
    # print(favorite_color(color_dict_3))


def count(list_str: list[str]) -> dict[str, int]:
    """
    function returns a dictionary of strings (keys) and the number of times each
    occurs in the inputted list (values)
    """

    return_dict: dict[str, int] = {}

    for idx in list_str:
        if idx in return_dict:
            return_dict[idx] += 1
        else:
            return_dict[idx] = 1

    return return_dict

    # test_list: list[str] = ["hi", "hello", "sup", "hi", "sup", "hi", "hiiiiiii"]
    # print(count(test_list))


def alphabetizer(inp_list: list[str]) -> dict[str, list[str]]:
    """
    this function groups the words in the inputted string based on the letters
    they start with
    """

    ret_dict: dict[str, list[str]] = {}

    """
    letter_list: list[str] = []

    for idx in inp_list:
        letter_list.append(idx[0])
    """

    temp_list: list[str] = []
    for string in inp_list:
        if not string[0] in ret_dict:
            ret_dict[string[0]] = temp_list
            for elem in inp_list:
                if elem[0] == string[0]:
                    temp_list.append(elem.lower())
            ret_dict[string[0]] = temp_list
        temp_list: list[str] = []

    return ret_dict

    # test_list: list[str] = ["cat", "mouse", "chair", "barn", "cape", "mother"]
    # print(alphabetizer(test_list))


def update_attendance(dct: dict[str, list[str]], day: str, student: str):
    """
    updates a dict[str, list[str]] of the days of the week and the students in
    attendance on those days
    """

    new_dict: dict[str, list[str]] = dct

    for key in dct:
        if key == day:
            new_dict[day].append(student)
        else:
            new_dict[day] = [student]

    dct = new_dict


attendance_log: dict[str, list[str,]] = {
    "Monday": ["James, Ocean, Amelia"],
    "Tuesday": ["Sid, George, Chris"],
    "Wednesday": ["Bob"],
}
print(attendance_log)
print(update_attendance(attendance_log, "Thursday", "Gerald"))
print(update_attendance(attendance_log, "Wednesday", "Wendy"))
