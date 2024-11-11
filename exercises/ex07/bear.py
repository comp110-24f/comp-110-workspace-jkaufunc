"""File to define Bear class."""


class Bear:
    """A new bear class."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializing bear age and hunger at 0."""
        self.age = 0
        self.hunger_score = 0

    def one_day(self):
        """Method adds 1 age and subtracts 1 hunger from each bear per day."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int):
        """Simulates that act of a bear eating a fish."""
        self.hunger_score += num_fish
