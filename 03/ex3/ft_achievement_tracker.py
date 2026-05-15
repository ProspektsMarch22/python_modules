#!/usr/bin/python3

import random as rd

def get_player_achievements(ach_nbr: int) -> set:
    ach_list: list = [
    "Crafting Genius",
    "World Savior",
    "Master Explorer",
    "Collector Supreme",
    "Untouchable",
    "Boss Slayer",
    "Strategist",
    "Unstoppable",
    "Speed Runner",
    "Survivor",
    "Treasure Hunter",
    "First Steps",
    "Sharp Mind",
    ]
    ach_set: set = set()
    for i in range(ach_nbr):
        ach_set.add(rd.choice(ach_list))
    return ach_set


def main() -> None:
    print("=== Achievement Tracker System ===\n")
    alice, bob, charlie, dylan = (get_player_achievements(10) for _ in range(4))
    print("Player Alice:", alice, end="\n\n")
    print("Player Bob:", bob, end="\n\n")
    print("Player Charlie:", charlie, end="\n\n")
    print("Player Dylan:", dylan, end="\n\n")
    print("All distinctive achievements:", set.union(alice, bob, charlie, dylan))
    print("\nCommon achievements:", set.intersection(alice, bob, charlie, dylan))
    print("\nOnly Alice has:", set.difference(alice, set.union(bob, charlie, dylan)))
    print("Only Bob has:", set.difference(bob, set.union(alice, charlie, dylan)))
    print("Only Charlie has:", set.difference(charlie, set.union(alice, bob, dylan)))
    print("Only Dylan has:", set.difference(dylan, set.union(alice, bob, charlie)))


if __name__ == '__main__':
    main()

