#!/usr/bin/env python3

from abc import ABC, abstractmethod


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: str) -> str:
        pass


class TransformCapability(ABC):
    def __init__(self, **kwargs) -> None:
        self.transformed: bool = False
        super().__init__(**kwargs)

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass
