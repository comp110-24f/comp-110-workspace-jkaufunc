"""There should be 2 bags of tea per 32oz pot, and a pot serves 5."""

"""A box of Twinings English Breakfeast Tea costs $7 and contains 20 bags."""
"""Each guests should get 3 scones."""
"""A bag of Sticky Fingers Tart Cherry Scone Mix costs $7 and makes about 12 scones."""


def get_teabags(numt: str) -> str:
    print(f"You will need {numt} teabags.")
    if int(numt) > 10:
        print("The tea will cost you $20, but you'll have some left over.")
    elif int(numt) <= 10:
        print("The tea will cost you $10, and there will be plenty for everyone.")
    return numt * 2


def get_scones(nums: str) -> str:
    print(f"You will need {nums} scones.")
    if int(nums) > 5:
        print("The scones will cost you $30, but you'll have some left over.")
    elif int(nums) <= 5:
        print("The scones will cost you $15.")

    return get_teabags(numt=input("How many guests are coming?")) * 2


def num_guests(numg: str) -> str:
    print(f"You will need to make {int(numg)*3} scones.")

    if int(numg) <= 4:
        print("You will need to use 1 box of scone mix, which will cost you $7.")
    elif int(numg) > 8:
        print(
            "Why are you inviting so many people??? It's supposed to be a cozy teaparty! You'll need at least 3 boxes of scones mix, which will cost you $21!"
        )
    elif int(numg) == 8:
        print("You will need to use 2 boxes of scone mix, which will cost you $14.")
    elif int(numg) >= 5:
        print(
            "You will need to use a little more than one box of scone mix, which will cost you $14, but you'll have some mix left over."
        )

    if int(numg) <= 5:
        print(
            "You will need 1 pot of tea made with 2 teabags. The teabags will cost $7, but you will have many left over."
        )
    elif int(numg) >= 10:
        print(
            "You will need at least 3 pots of tea made with 2 teabags each. The teabags will cost $7, but you will have some left over."
        )
    elif int(numg) >= 5:
        print(
            "You will need 2 pots of tea made with 2 teabags each. The teabags will cost $7, but you will have many left over."
        )
    return numg


def main() -> None:
    masternum = input("How many guests are coming?")
    get_teabags(numt=masternum)
    get_scones(nums=masternum)


def new_main() -> None:
    numguests = input("How many guests are coming to the tea party?")
    num_guests(numg=numguests)

    if int(numguests) <= 4:
        print("The total cost of the teaparty is $14")
    elif int(numguests) > 8:
        print("The total cost of the tea party is $28")
    elif int(numguests) > 4:
        print("The total cost of the tea party is $21.")


new_main()
