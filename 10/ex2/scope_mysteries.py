#!/usr/bin/env python3


from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    count: int = 0

    def mystery() -> int:
        nonlocal count  # only works within nested scope
        count += 1
        return count
    return mystery


def spell_accumulator(initial_power: int) -> Callable:
    amount = initial_power

    def increment(nbr: int) -> int:
        nonlocal amount
        amount += nbr
        return amount
    return increment


def enchantment_factory(enchantment_type: str) -> Callable:

    def produce_enchantment(item_to_enchant: str) -> str:
        return f"{enchantment_type} {item_to_enchant}"
    return produce_enchantment


def memory_vault() -> dict[str, Callable]:
    vault_info: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        vault_info[key] = value

    def recall(key: str) -> Any:
        return vault_info.get(key, "Memory not found")
    return {
        'store': store,
        'recall': recall
    }


if __name__ == '__main__':
    c_a = mage_counter()
    print("Testing mage counter...\n\n"
          f"call 1: {c_a()}\n"
          f"call 2: {c_a()}\n"
          "calling 20 times...\n")
    for _ in range(20):
        c_a()
    print(f"last call: {c_a()}\n")
    print("=" * 40, end="\n\n")

    acc = spell_accumulator(10)
    print("Testing spell accumulator, initial value of 10...\n\n"
          f"Incrementing by 10: {acc(10)}\n"
          f"Incrementing by 20: {acc(20)}\n"
          f"Incrementing by 1: {acc(1)}\n")
    print("=" * 40, end="\n\n")

    charm_1 = enchantment_factory("Blazing")
    charm_2 = enchantment_factory("Chilling")
    print("Testing enchantment factory...\n\n"
          f"{charm_1('Sword')}\n"
          f"{charm_2('Staff')}\n")
    print("=" * 40, end="\n\n")

    vault = memory_vault()
    key = "secret"
    value = 42
    vault['store'](key, value)
    print("Testing memory vault...\n\n"
          f"Store '{key}' = {value}")
    print(f"Recall '{key}': {vault['recall'](key)}\n"
          f"Recall 'unknown': {vault['recall']('unknown')}")
