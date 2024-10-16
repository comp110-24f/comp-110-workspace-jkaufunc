def find_and_remove_max(list1: list[int]) -> int:
    (
        """this function will find the maximum value in a list and remove all
    instances of that value from it"""
    )

    # modified_list: list = []

    if len(list1) == 0:
        max_num = -1
    else:
        max_num: int = list1[0]
        for idx in range(0, len(list1)):
            if list1[idx] > max_num:
                max_num = list1[idx]
            else:
                max_num = max_num

        num: int = 0
        while num < len(list1):
            if list1[num] == max_num:
                list1.pop(num)
            else:
                num += 1

        # for idx in range(0, len(list1)):
        # if list1[idx] != max_num:
        # modified_list.append(list1[idx])
        # else:
        # modified_list = modified_list

    # list1 = modified_list

    return max_num
