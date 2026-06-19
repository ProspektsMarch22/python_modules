#!/usr/bin/env python3


from ex0 import FlameFactory, AquaFactory


def test_factory(factory: FlameFactory | AquaFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def battle(factory1: FlameFactory | AquaFactory,
           factory2: FlameFactory | AquaFactory):
    print("Testing battle")
    c1 = factory1.create_base()
    c2 = factory2.create_base()
    print(c1.describe())
    print(" vs.")
    print(c2.describe())
    print(" fight!")
    print(c1.attack())
    print(c2.attack())


if __name__ == "__main__":
    magma = FlameFactory()
    aqua = AquaFactory()
    test_factory(magma)
    print()
    test_factory(aqua)
    print()
    battle(magma, aqua)
