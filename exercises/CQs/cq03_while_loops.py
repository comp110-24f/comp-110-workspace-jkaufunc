__author__ = "James Kaufman"


def num_instances(phrase: str, search_char: str) -> int:
    """This function counts the number of times a character occurs in a sequence of inputted strings."""

    count: int = 0
    """tracks the number of characters in the inputted string: phrase."""

    output: int = 0
    """output is the integer that is updated as the function locates characters that match "search_char", and it will eventually be printed as the final return value."""

    """the expression, "count < len(phrase)" is the boolean expression that will end the function. Once the count is equal to the len(phrase), we know all the characters in the phrase have been considered, and the while loop can be exitted."""
    while count < len(phrase):
        if phrase[count] == search_char:
            output = output + 1
            count = count + 1
        else:
            count = count + 1
    return output


print(num_instances("Success!", "c"))
