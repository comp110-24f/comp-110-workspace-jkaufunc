"""File to define Fish class."""


class Fish:
    """A new fish class."""

    age: int

    def __init__(self):
        """Initializing the age of a fish at 0."""
        self.age = 0

    def one_day(self):
        """Method adds 1 age to every each fish per day."""
        self.age += 1
