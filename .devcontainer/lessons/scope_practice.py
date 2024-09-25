__author__ = "James Kaufman"

"""exercise for while loops and scope"""


def remove_chars(msg: str, char: str) -> str:
    """Returns a copy of msg with all instances char removed."""
    copy: str = ""
    index: int = 0
    while index < len(msg):
        if msg[index] != char:
            copy = copy + msg[index]
        index += 1

    return copy


word: str = "soup"
(
    """word is a global variable!!! It has a global scope because it exists on its own,
    outside of a function."""
)
print(remove_chars(word, "o"))
