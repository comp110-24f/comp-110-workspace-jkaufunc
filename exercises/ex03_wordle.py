"""A recreation of the popular New York Times game, Wordle!"""

__author__ = "730761420"


def input_guess(guess_len: int) -> str:
    (
        """prompts the function caller for a word of the
    inputted length"""
    )

    # at first, I kept trying to make the paramenter it's own local variable.
    # Then I remembered I could assign a local variable to an input
    # I didn't realize the length of the secret word was to be specified when calling
    #   the input_guess function.

    guess: str = input(f"Choose a {guess_len} letter word for your first guess: ")
    while len(guess) != guess_len:
        guess = input(
            f"You must choose a {guess_len} letter word for your first guess: "
        )

    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """this function seraches a string for a specified character"""
    assert len(char_guess) == 1

    idx: int = 0

    condition: bool = False

    while idx < len(secret_word):
        if secret_word[idx] == char_guess:
            condition = True

            idx += 1
        else:
            idx += 1
    return condition


# I forgot to add else:\ idx += 1. This I think makes some kind of infinite loop,
#   which prevents this function and the emojified function from running!

# for now, although I think my contains_char functoin should function, it isn't
#   generating any output when I try to print a function call
#   maybe that won't affect my later code and the final project will work?


def emojified(guessed_word: str, secret_word: str) -> str:
    (
        """this function compares the guessed word to the
    secret word which is the solution to the puzzle"""
    )
    assert len(guessed_word) == len(secret_word)

    white_box: str = "\U00002B1C"
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"

    idx: int = 0

    display: str = ""

    while idx < len(secret_word):
        if secret_word[idx] == guessed_word[idx]:
            display += green_box
        elif contains_char(secret_word, guessed_word[idx]):
            display += yellow_box
        else:
            display += white_box

        idx += 1

    return display


emojified("havoc", "hello")
