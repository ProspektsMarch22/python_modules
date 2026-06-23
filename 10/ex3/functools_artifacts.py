#!/usr/bin/env python3

from collections.abc import Callable
from typing import Any
from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    if operation == "add":
        return reduce(add, spells)
    elif operation == "multiply":
        return reduce(mul, spells)
    elif operation == "max":
        return reduce(lambda x, y: x if x > y else y, spells)
    elif operation == "min":
        return reduce(lambda x, y: x if x < y else y, spells)
    else:
        raise ValueError("Unknown operation")


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire": partial(base_enchantment, power=50, element="fire"),
        "ice": partial(base_enchantment, power=50, element="ice"),
        "lightning": partial(base_enchantment, power=50, element="lightning")
    }


@lru_cache(maxsize=None)  # This is used to avoid repeated calculations
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative.")
    if (n == 0) or (n == 1):
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatch(spell: Any) -> str:
        return "Unknown spell type"

    @dispatch.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatch.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatch.register(list)
    def _(spell: list[Any]) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatch


if __name__ == '__main__':
    # Test data
    spell_powers = [27, 19, 22, 35, 31, 41]
    operations = ['add', 'multiply', 'max', 'min']
    fibonacci_tests = [11, 14, 12]
    print("\nTesting spell reducer...\n"
          f"Sum: {spell_reducer(spell_powers, operations[0])}\n"
          f"Product: {spell_reducer(spell_powers, operations[1])}\n"
          f"Max: {spell_reducer(spell_powers, operations[2])}\n"
          f"Min: {spell_reducer(spell_powers, operations[-1])}\n")

    # Partial Enchanter
    def base_enchantment(power: int, element: str, target: str) -> str:
        # Just to test the partial enchanter
        return f"{element} enchantment hits {target} with {power} power"
    enchantment = partial_enchanter(base_enchantment)
    print("Testing partial enchanter...\n"
          f"{enchantment['fire'](target="Sword")}\n")

    # Memoized fibonacci
    print("Testing memoized fibonacci...\n"
          f"Fib(0): {memoized_fibonacci(0)}\n"
          f"Fib(1): {memoized_fibonacci(1)}\n"
          f"Fib(10): {memoized_fibonacci(10)}\n"
          f"Fib(15): {memoized_fibonacci(15)}\n")

    # Spell Dispatcher
    dispatcher = spell_dispatcher()
    print("Testing spell dispatcher..."
          f"\n"
          f"{dispatcher(42)}\n"
          f"{dispatcher('fireball')}\n"
          f"{dispatcher(spell_powers)}\n"
          f"{dispatcher(1.3)}\n")
