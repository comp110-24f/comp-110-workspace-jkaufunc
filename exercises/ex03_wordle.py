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

    guess: str = input(f"Enter a {guess_len} letter word: ")
    while len(guess) != guess_len:
        guess = input(f"You must choose a {guess_len} letter word: ")

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
        elif contains_char(secret_word, guessed_word[idx]) and num_char(guessed_word):
            display += yellow_box
        elif contains_char(secret_word, guessed_word[idx]):
            display += yellow_box
        else:
            display += white_box

        idx += 1

    return display


def num_char(guessed_word: str) -> bool:
    (
        """this function is designed to prevent emojified from desplaying a yellow box
              for a repeated letter in the guessed_word, when there is only one in the
              secret_word"""
    )
    idx2: int = 0
    guessed_char: str = guessed_word[idx2]
    condition: bool = True

    while idx2 < len(guessed_word):
        idx1: int = 0
        instances: int = 0
        while idx1 < len(guessed_word):
            if guessed_char == guessed_word[idx1]:
                instances += 1
                idx1 += 1
            else:
                idx1 += 1

        if instances > 1:
            condition = False
            idx2 += 1
            if idx2 < len(guessed_word):
                guessed_char = guessed_word[idx2]
        else:
            idx2 += 1
            if idx2 < len(guessed_word):
                guessed_char = guessed_word[idx2]

    return condition


def main(secret_word: str) -> None:
    """the entrypoint of of the program and main game loop"""
    turn: int = 1
    state: bool = True

    while state and turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(secret_word))
        print(emojified(guess, secret_word))

        if guess == secret_word:
            print(f"You won in {turn}/6 turns!")
            state = False

        turn += 1

    if state:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main("haven")
