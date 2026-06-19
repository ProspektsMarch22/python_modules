#!/usr/bin/env python3

from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_heal(factory: HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")
    base = factory.create_base()
    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.heal("itself"))
    evolved = factory.create_evolved()
    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal("itself and others"))


def test_transform(factory: TransformCreatureFactory) -> None:
    print("Testing Creature with transform capability")
    base = factory.create_base()
    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())
    evolved = factory.create_evolved()
    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


if __name__ == '__main__':
    heal = HealingCreatureFactory()
    test_heal(heal)
    print()
    transform = TransformCreatureFactory()
    test_transform(transform)
