"""File to define River class."""

__author__: str = "730826103"

from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear


class River:

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        bear_new: list[Bear] = []
        fish_new: list[Fish] = []
        for abear in self.bears:
            if abear.age <= 5:
                bear_new.append(abear)
        for afish in self.fish:
            if afish.age <= 3:
                fish_new.append(afish)

        self.bears = bear_new
        self.fish = fish_new
        return None

    def bears_eating(self):
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)
        return None

    def check_hunger(self):
        lived_bear: list[Bear] = []
        for abear in self.bears:
            if abear.hunger_score >= 0:
                lived_bear.append(abear)

        self.bears = lived_bear
        return None

    def repopulate_fish(self):
        new_fish: int = (len(self.bears) // 2) * 2
        for _ in range(0, new_fish):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        new_bears: int = len(self.bears) // 2

        for _ in range(0, new_bears):
            self.bears.append(Bear())
        return None

    def view_river(self):
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self):
        """Simulate one day of life in the river"""
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

    def one_river_week(self) -> None:
        for _ in range(7):
            self.one_river_day()

    def remove_fish(self, amount: int) -> None:
        for _ in range(0, amount):
            self.fish.pop(0)
