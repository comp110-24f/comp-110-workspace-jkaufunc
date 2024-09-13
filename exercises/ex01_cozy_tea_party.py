"""Created by JamesK"""


def main() -> None:
    people = input("How many people are coming to the party?")
    print(f"You will need {tea_bags(people=int(people))} teabags.")
    print(f"You will also need {treats(people=int(people))} treats to go with the tea.")
    print(
        f"The total cost of teabags and treats will be ${cost(tea_count=int(people), treat_count=int(people))}."
    )


def tea_bags(people: int) -> int:
    """Calculates how many bags of tea are needed based on the number of guests."""

    return people * 2 + 2


def treats(people: int) -> int:
    """Calculates the number of treats needed for the party."""

    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Returns the total cost of teabags and treats, which cost 0.5 and 0.75 each respectively."""

    return tea_bags(people=tea_count) * 0.5 + treats(people=treat_count) * 0.75


main()
