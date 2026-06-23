#!/usr/bin/env python3

from functools import wraps
from collections.abc import Callable
from typing import Any
import time


def spell_timer(func: Callable) -> Callable:
    # functools wrap is used to preserve function metadata
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        duration = end - start
        print(f"Spell completed in {duration:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    # my first decorator
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            if isinstance(args[0], int):
                power = args[0]
            else:
                power = args[-1]
            if power >= min_power:
                return func(*args, **kwargs)  # This enables functions calling
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print("Spell failed, retrying..."
                          f"(attempt {attempt}/{max_attempts})")
            if attempt == max_attempts:
                return (f"Spell casting failed after {max_attempts} attempts")
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(
            char.isalpha() or char.isspace() for char in name
        )

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == '__main__':
    spells = [
        ("fireball", 30),
        ("flash", 19),
        ("earthquake", 3),
        ("freeze", 22)
    ]

    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball Cast!"

    # Spell_timer
    print("Testing spell timer...")
    spell_t = spell_timer(fireball)
    print(f"Result: {spell_t()}\n")

    # Power_validator
    @power_validator(20)
    def cast_spell(power: int, target: str) -> str:
        return f"Spell hits {target} with {power} power"

    print("Testing power validator...\n")
    for spell, power in spells:
        print(f"{cast_spell(power, spell)}")

    # Retry_spell
    print("\nTesting retrying spell...")

    @retry_spell(max_attempts=3)
    def unstable_spell() -> str:
        unstable_spell.attempts += 1
        if unstable_spell.attempts < 4:
            raise ValueError("Spell failed!")
        return "WAAAAAAAAAAAAAAAAAAA :("

    @retry_spell(max_attempts=10)
    def stable_spell() -> str:
        stable_spell.attempts += 1
        if stable_spell.attempts < 0:
            raise ValueError("Spell failed!")
        return "WAAAAAAAAAAAAAAAAAAA :("

    unstable_spell.attempts = 0
    stable_spell.attempts = 0
    print(f"{unstable_spell()}\n"
          f"{stable_spell()}\n")
