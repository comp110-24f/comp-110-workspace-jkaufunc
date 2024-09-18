__author__ = "James Kaufman"


def guess_a_number() -> None:
    secret: int = 7
    x = int(input("Guess a number!"))
    print(f"Your guess was {x}.")

    if int(x) == secret:
        print("You got it!")
    elif x < secret:
        print(f"Your guess was too low! The secret number is {x}")
    elif x > secret:
        print(f"Your guess was too high! The secret number is {x}")
    return None


if __name__ == "__main__":
    guess_a_number()
