"""File to define Fish class."""

__author__: str = "730826103"


class Fish:

    age: int

    def __init__(self):
        self.age = 0

    def one_day(self):
        self.age += 1
        return None
