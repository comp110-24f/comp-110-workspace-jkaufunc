"""First step towards recreating Wordle."""

__author__ = "730761420"


def input_word() -> str:
    """Collects and stores an inputted 5 letter word."""

    chosen_word = input("Choose a 5 letter word")

    if len(chosen_word) == 5:
        print(chosen_word)
    else:
        print("Error: The word must contain 5 characters.")
        print(chosen_word)

    return chosen_word


def input_letter() -> str:
    """Collects and stores an inputted character."""

    chosen_letter = input("Choose a letter")

    if len(chosen_letter) == 1:
        print(chosen_letter)
    else:
        print("Error: You must choose only a single letter.")
        print(chosen_letter)

    return chosen_letter


def contains_char(word: str, letter: str) -> None:

    current_letter: int = 0
    instances: int = 0
    print(f"Searching for '{letter}' in '{word}'")

    if len(word) > 5 or len(letter) > 1:
        print(f"No instances of '{letter}' found in '{word}'")

    (
        """I kept getting a string index out of range error here because I
        had a condition <= 5 instead of <=4. Since the index starts at zero, a five
      letter word has letters of index 0 to 4, not 1 to 5."""
    )
    while current_letter <= 4:
        if word[current_letter] == letter:
            print(f"letter '{letter}' found at index {current_letter}")
            instances += 1
        current_letter += 1

    print(f"There are {instances} instances of '{letter}' in '{word}'")


contains_char(word=input_word(), letter=input_letter())
