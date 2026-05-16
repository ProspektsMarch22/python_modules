#!/bin/usr/env python3

import random as rd


OFFICE_PEOPLE: list[str] = [
    "Michael",
    "jim",
    "Dwight",
    "pam",
    "Angela",
    "oscar",
    "Kevin",
    "phyllis",
    "Stanley"
]


def main() -> None:
    print("=== Game Data Alchemist ===")
    print("Initial list of players:", OFFICE_PEOPLE)
    all_caps: list[str] = [x.capitalize() for x in OFFICE_PEOPLE]
    print("New list with all names capitalized:",
          all_caps)
    only_caps: list[str] = [x for x in OFFICE_PEOPLE if x == x.capitalize()]
    print("New list of capitalized names only:",
          only_caps)
    score_dict: dict[str, int] = {x: rd.randint(0, 1000) for x in all_caps}
    print("Score dict:",
          score_dict)
    avg: float = round(sum(score_dict.values())/len(score_dict), 2)
    print("Score average is", avg)
    higher: dict[str, int] = {x: score_dict[x] for x in score_dict.keys()
                              if score_dict[x] > avg}
    print("High Scores:", higher)


if __name__ == '__main__':
    main()
