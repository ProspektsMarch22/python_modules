#!/usr/bin/env python3

from typing import Any
from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.capability import HealCapability, TransformCapability


class BattleStrategy(ABC):
    def __init__(self, creature: Any) -> None:
        self.creature = creature

    @abstractmethod
    def is_valid(self) -> bool:
        pass

    @abstractmethod
    def act(self) -> None:
        pass


class NormalStrategy(BattleStrategy):
    def __init__(self, creature: Any) -> None:
        super().__init__(creature)

    def is_valid(self) -> bool:
        return isinstance(self.creature, Creature)

    def act(self) -> None:
        if self.is_valid() is True:
            print(self.creature.attack())
        else:
            raise TypeError(f"Invalid Creature '{self.creature.name}' for this strategy")


class AggressiveStrategy(BattleStrategy):
    def __init__(self, creature: Any) -> None:
        super().__init__(creature)

    def is_valid(self) -> bool:
        return isinstance(self.creature, TransformCapability)

    def act(self) -> None:
        if self.is_valid() is True:
            print(self.creature.transform())
            print(self.creature.attack())
            print(self.creature.revert())
        else:
            raise TypeError(f"Invalid creature '{self.creature.name}'"+
                " for this aggresive strategy")


class DefensiveStrategy(BattleStrategy):
    def __init__(self, creature: Any) -> None:
        super().__init__(creature)

    def is_valid(self) -> bool:
        return isinstance(self.creature, HealCapability)

    def act(self) -> None:
        if self.is_valid() is True:
            print(self.creature.attack())
            print(self.creature.heal("itself"))
        else:
            raise TypeError(f"Invalid creature '{self.creature.name}'"+
                " for this defensive strategy")
