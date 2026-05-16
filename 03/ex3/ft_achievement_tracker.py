#!/usr/bin/env python3


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
    #
    # Iniializes player achievements sets
    alice, bob = (get_player_achievements(10) for _ in range(2))
    charlie, dylan = (get_player_achievements(10) for _ in range(2))
    #
    # Prints player sets
    print("Player Alice:", alice, end="\n\n")
    print("Player Bob:", bob, end="\n\n")
    print("Player Charlie:", charlie, end="\n\n")
    print("Player Dylan:", dylan, end="\n\n")
    #
    # Prints all elements within union of sets, uniques
    print("All distinctive achievements:",
          set.union(alice, bob, charlie, dylan))
    #
    # Intersection between player sets
    print("\nCommon achievements:",
          set.intersection(alice, bob, charlie, dylan))
    #
    # Difference between player set and union of rest of players' sets
    print("\nOnly Alice has:",
          set.difference(alice, set.union(bob, charlie, dylan)))
    print("Only Bob has:",
          set.difference(bob, set.union(alice, charlie, dylan)))
    print("Only Charlie has:",
          set.difference(charlie, set.union(alice, bob, dylan)))
    print("Only Dylan has:",
          set.difference(dylan, set.union(alice, bob, charlie)))
    #
    # Difference between union of rest of players' sets and player set
    print("\nAlice is missing:",
          set.difference(set.union(bob, charlie, dylan), alice))
    print("Bob is missing:",
          set.difference(set.union(alice, charlie, dylan), bob))
    print("Charlie is missing:",
          set.difference(set.union(alice, bob, dylan), charlie))
    print("Dyaln is missing:",
          set.difference(set.union(alice, bob, charlie), dylan))


if __name__ == '__main__':
    main()
