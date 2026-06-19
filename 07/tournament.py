#!/usr/bin/env python3

from ex0 import CreatureFactory
from ex0 import AquaFactory as af
from ex0 import FlameFactory as ff
from ex1 import HealingCreatureFactory as hcf
from ex1 import TransformCreatureFactory as tcf
from ex2 import BattleStrategy
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy


def battle(opps: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opps)} opponents involved\n")
    if len(opps) == 1:
        print("There's no sufficient participants!")
        return
    i: int = 0
    while i < (len(opps) - 1):
        j: int = i + 1
        while j < len(opps):
            c1 = opps[i][0].create_base()
            c1_s: BattleStrategy = opps[i][1]
            c2 = opps[j][0].create_base()
            c2_s: BattleStrategy = opps[j][1]
            print("* Battle *")
            print(c1.describe())
            print(" vs.")
            print(c2.describe())
            print(" now fight!")
            try:
                c1_s.act()
                c2_s.act()
                print()
            except TypeError as e:
                print("Battle error, aborting tournament:", e)
                return
            j += 1
        i += 1


if __name__ == '__main__':
    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    test_0 = [
        (ff(), NormalStrategy(ff().create_base())),
        (hcf(), DefensiveStrategy(hcf().create_base()))
    ]
    battle(test_0)
    print("\nTournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    test_1 = [
        (ff(), AggressiveStrategy(ff().create_base())),
        (hcf(), DefensiveStrategy(hcf().create_base()))
    ]
    battle(test_1)
    print("\nTournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    test_2 = [
        (af(), NormalStrategy(af().create_base())),
        (hcf(), DefensiveStrategy(hcf().create_base())),
        (tcf(), AggressiveStrategy(tcf().create_base()))
    ]
    battle(test_2)
