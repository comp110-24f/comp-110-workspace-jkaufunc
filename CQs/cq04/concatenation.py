__author__ = "730761420"


def concat(str1: str, str2: str) -> str:
    """returns the concatenation of two inputted strings."""
    return str1 + str2


word1: str = "happy"
word2: str = "tuesday"

if __name__ == "__main__":
    print(concat(word1, word2))
