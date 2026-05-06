from __future__ import annotations
from typing import Self


# Parent Class
class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self.set_height(height)
        self.set_age(age)
        self._tracker = self._StatsTracker()

    # Setters and Getters
    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative",
                  "Height update rejected", sep="\n")
            return
        self._height = new_height

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self.name}: Error, age can't be negative",
                  "Age update rejected", sep="\n")
            return
        self._age = new_age

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    # General methods
    def show(self) -> None:
        print(f"{self.name}:",
              f"{round(self.get_height(), 1)}cm,",
              f"{self.get_age()} days old")
        self._tracker.increment_show()

    def grow(self) -> None:
        self.set_height(self.get_height() + 0.6)
        self._tracker.increment_grow()

    def age(self) -> None:
        self.set_age(self.get_age() + 1)
        self.grow()
        self._tracker.increment_age()

    def display_stats(self) -> None:
        print("Stats:", self._tracker.count_grow, "grow,",
              self._tracker.count_age, "age,",
              self._tracker.count_show, "show")

    # Static methods
    @staticmethod
    def older_than_year(age: int) -> bool:
        return age > 365

    # Class method for unknown plant creation
    @classmethod
    def unknown_plant(cls, name) -> Self:
        return cls(name, 0, 0)

    # Inner Stats Class encapsulated
    class _StatsTracker:
        def __init__(self) -> None:
            self.__tracker_grow: int = 0
            self.__tracker_age: int = 0
            self.__tracker_show: int = 0

        def increment_grow(self) -> None:
            self.__tracker_grow += 1

        def increment_age(self) -> None:
            self.__tracker_age += 1

        def increment_show(self) -> None:
            self.__tracker_show += 1

        @property
        def count_grow(self) -> int:
            return self.__tracker_grow

        @property
        def count_age(self) -> int:
            return self.__tracker_age

        @property
        def count_show(self) -> int:
            return self.__tracker_show


# Child classes
class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.has_bloom = False

    def bloom(self) -> None:
        self.has_bloom = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.has_bloom is True:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet.")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int,
                 color: str) -> None:
        super().__init__(name, height, age, color)
        self.seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds += 42

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seeds}")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self._tracker: Tree._StatsTracker = self._StatsTracker()

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces ",
              f"a shade of {self.get_height()}cm long",
              f" and {self.trunk_diameter}cm wide", sep="")
        self._tracker.increment_shade()

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def display_stats(self) -> None:
        super().display_stats()
        print(" ", self._tracker.count_shade, "shade")

    class _StatsTracker(Plant._StatsTracker):
        def __init__(self) -> None:
            super().__init__()
            self.__tracker_shade = 0

        def increment_shade(self) -> None:
            self.__tracker_shade += 1

        @property
        def count_shade(self):
            return self.__tracker_shade


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value: int = 0

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}",
              f" Nutritional value: {self.nutritional_value}", sep="\n")


def show_plant_stats(plant: Plant) -> None:
    plant.display_stats()


def main() -> None:
    flower = Flower("rose", 15.0, 30, "red")
    print(flower.older_than_year(flower.get_age()))
    moranguete = Plant.unknown_plant("moranguete")
    moranguete.show()
    sunflower = Seed("sunflower", 80.0, 45, "yellow")
    sunflower.show()
    for i in range(20):
        sunflower.age()
    sunflower.bloom()
    sunflower.show()
    sunflower.display_stats()
    oak = Tree("oak", 200.0, 365, 20.0)
    oak.produce_shade()
    oak.display_stats()
    show_plant_stats(moranguete)


if __name__ == '__main__':
    main()
