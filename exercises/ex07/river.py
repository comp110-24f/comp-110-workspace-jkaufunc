"""File to define River class."""

__author__ = "730761420"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """A new data type used to simulate a river ecosystem."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Removes fish above a certain age."""
        temp_fish_list: list[Fish] = []
        temp_bear_list: list[Bear] = []

        for fish in self.fish:
            if fish.age <= 3:
                temp_fish_list.append(fish)

        self.fish = temp_fish_list

        for bear in self.bears:
            if bear.age <= 5:
                temp_bear_list.append(bear)

        self.bears = temp_bear_list

    def bears_eating(self):
        """A method that simulates bears eating fish."""
        while len(self.fish) >= 5:
            for bear in self.bears:
                bear.eat(3)
                self.remove_fish(3)

    def check_hunger(self):
        """Moniters bear hunger."""
        temp_bear_list: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                temp_bear_list.append(bear)

        self.bears = temp_bear_list

    def remove_fish(self, amount: int):
        """Removes fish after they reach a certain age."""
        fish_count: int = 0

        while len(self.fish) > 0 and fish_count < amount:
            self.fish.pop(0)
            fish_count += 1

    def repopulate_fish(self):
        """A method that simulates fish reproduction."""
        new_fish: int = (len(self.fish) // 2) * 4
        num: int = 0
        while num in range(0, new_fish):
            self.fish.append(Fish())
            num += 1

    def repopulate_bears(self):
        """A method that simulates bear reproduction."""
        new_bears: int = len(self.bears) // 2
        num: int = 0
        while num in range(0, new_bears):
            self.bears.append(Bear())
            num += 1

    def view_river(self):
        """A method that allows one to view the state of a river ecosystem."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulation of one week in the life of the river."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
