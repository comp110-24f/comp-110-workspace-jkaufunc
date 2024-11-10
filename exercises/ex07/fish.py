"""File to define Fish class."""


class Fish:
    age: int

    def __init__(self):
        """initializing the age of a fish at 0"""
        self.age = 0

    def one_day(self):
        """method adds 1 age to every each fish per day"""
        self.age += 1
