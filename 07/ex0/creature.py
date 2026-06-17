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
        return f'{self.name} is a {self.type}'
