#!/usr/bin/env python3

from ex0.creature import Creature
from .capability import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def heal(self, target: str) -> str:
        return f"{self.name} heals {target} for a small amount"

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def heal(self, target: str) -> str:
        return f"{self.name} heals {target} for a large amount"

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} returns to normal."

    def attack(self) -> str:
        if self.transformed is False:
            return f"{self.name} attacks normally"
        elif self.transformed is True:
            return f"{self.name} unleashes a devastating morph strike!"


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Morphagon", "Normal/Dragon")

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} returns to normal."

    def attack(self) -> str:
        if self.transformed is False:
            return f"{self.name} attacks normally"
        elif self.transformed is True:
            return f"{self.name} unleashes a devastating morph strike!"
