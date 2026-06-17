#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Creature(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def type(self):
        pass

    @abstractmethod
    def attack(self):
        pass

    def describe(self) -> str:
        return f'{self.name()} is a {self.type()} type Creature'


class Flameling(Creature):
    def name(self) -> str:
        return "Flameling"

    def type(self) -> str:
        return "Fire"

    def attack(self) -> str:
        return f'{self.name()} uses Ember!'


class Pyrodon(Creature):
    def name(self) -> str:
        return "Pyrodon"

    def type(self) -> str:
        return "Fire/Flying"

    def attack(self) -> str:
        return f'{self.name()} uses Flamethrower!'


class Aquabub(Creature):
    def name(self) -> str:
        return "Aquabub"

    def type(self) -> str:
        return "Water"

    def attack(self) -> str:
        return f'{self.name()} uses Water Gun!'


class Torragon(Creature):
    def name(self) -> str:
        return "Torragon"

    def type(self) -> str:
        return "Water"

    def attack(self) -> str:
        return f'{self.name()} uses Hydro Pump!'


if __name__ == '__main__':
    """ Testing suite for the creatures """
    pocket_monsters: list[Creature] = [
        Flameling(),
        Pyrodon(),
        Aquabub(),
        Torragon()
    ]
    for mon in pocket_monsters:
        print(mon.describe())
        print(mon.attack())
