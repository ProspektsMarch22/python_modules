#!/bin/usr/env python3


import random as rd
import typing as tp

PLAYERS: list[str] = ['alice', 'bob', 'charlie', 'dylan']
ACTIONS: list[str] = ['eat', 'sleep', 'grab', 'release', 'use', 'move', 'run']


def gen_event() -> tp.Generator[tuple[str, str], None, None]:
    player: str = rd.choice(PLAYERS)
    action: str = rd.choice(ACTIONS)
    yield (player, action)


def consume_event(events: list[tuple[str, str]]
                  ) -> tp.Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        chosen: tuple[str, str] = rd.choice(events)
        events.remove(chosen)
        yield chosen


def main() -> None:
    print("=== Game Data Stream Processor ===")
    for i in range(1000):
        event: tuple[str, str] = next(gen_event())
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
    events: list[tuple[str, str]] = list()
    for _ in range(10):
        events += [next(gen_event())]
    print("Built list of 10 events:", events)
    for event in consume_event(events):
        print("Got event from the list:", event)
        print("Remains in list:", events)


if __name__ == '__main__':
    main()
