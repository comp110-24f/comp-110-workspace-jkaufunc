def get_first(input: list[str]) -> str:
    """eturns the first element in the list"""
    return input[0]


def remove_first(input: list[str]) -> None:
    """pops the first element off of input list"""
    input.pop(0)


def get_and_remove_first(input: list[str]) -> str:
    """returns first elemet and pops it of"""
    first: str = input[0]
    input.pop(0)
    return first
