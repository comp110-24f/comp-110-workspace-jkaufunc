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

    # print(color_count)

    count: int = 0

    for key in color_count:
        if color_count[key] > count:
            count = color_count[key]
            fav = key

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
        temp_list = []

    return ret_dict

    # test_list: list[str] = ["cat", "mouse", "chair", "barn", "cape", "mother"]
    # print(alphabetizer(test_list))


def update_attendance(dct: dict[str, list[str]], day: str, student: str) -> None:
    """
    updates a dict[str, list[str]] of the days of the week and the students in
    attendance on those days
    """

    if day not in dct:
        dct[day] = []
        dct[day].append(student)
    else:
        for key in dct:
            if key == day:
                dct[key].append(student)

    """
    attendance_log: dict[str, list[str,]] = {
        "Monday": ["James, Ocean, Amelia"],
        "Tuesday": ["Sid, George, Chris"],
        "Wednesday": ["Bob"],
    }

    print(attendance_log)


    print(attendance_log)
    print(update_attendance(attendance_log, "Thursday", "Gerald"))
    print(attendance_log)
    print(update_attendance(attendance_log, "Wednesday", "Wendy"))
    print(attendance_log)

    update_attendance(attendance_log, "Wednesday", "Wendy")
    print(attendance_log)
    """
