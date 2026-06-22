#!/usr/bin/env python3

from collections.abc import Callable


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def lightning(target: str, power: int) -> str:
    return f"Lightning strikes {target} for {power} damage"


def spell_combiner(spell_1: Callable, spell_2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple[str, str]:
        return spell_1(target, power), spell_2(target, power)
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def new_spell_amp(target: str, power: int) -> str:
        base_spell(target, (multiplier * power))
        return f'Original: {power}, Amplified {power * multiplier}'
    return new_spell_amp


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def new_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return new_spell


def is_strong(target: str, power: int) -> bool:
    # helper function to test the conditional_caster function
    return power >= 15 and target != "elf"


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list[str]:
        results: list[str] = []
        for spell in spells:
            results.append(spell(target, power))
        return results
    return sequence


if __name__ == '__main__':
    power = [10, 15, 9]
    targets = ['Wyvern Rider', 'Brigand', 'Pirate', 'Shaman']
    combined = spell_combiner(fireball, heal)
    res_combined = combined("Wyvern Rider", 10)
    print("\nTesting spell combiner...\n"
          "Combine spell result: "
          f"{res_combined[0]}, {res_combined[1]}\n")
    power_amp = power_amplifier(lightning, 3)
    res_amp = power_amp('Goblin', 10)
    print("\nTesting power amplifier...\n"
          "Power amplifier result: "
          f"{res_amp}\n")
    spell_cond = conditional_caster(is_strong, fireball)
    res_cond_1 = spell_cond('Wizard', 10)
    res_cond_2 = spell_cond('Goblin', 20)
    print("\nTesting conditional caster...\n"
          "  -> Example 1 (false condition):\n"
          f"      {res_cond_1}\n"
          "  -> Example 2 (true condition):\n"
          f"       {res_cond_2}\n")
    spell_seq = spell_sequence([fireball, heal, lightning])
    res_seq = spell_seq('Knight', 12)
    print("\nTesting spell sequence...\n"
          "Spell sequence result (list): \n"
          f"{res_seq}\n")
