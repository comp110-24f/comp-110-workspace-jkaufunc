def find_and_remove_max(list1: list[int]) -> int:
    (
        """this function will find the maximum value in a list and remove all
    instances of that value from it"""
    )

    if len(list1) == 0:
        max_num = -1
    else:
        max_num: int = list1[0]
        for idx in range(0, len(list1)):
            if list1[idx] > max_num:
                max_num = list1[idx]
            else:
                max_num = max_num

        for idx in range(0, len(list1)):
            if max_num == list1[idx]:
                list1.pop(idx)
            else:
                list1 = list1

    return max_num
