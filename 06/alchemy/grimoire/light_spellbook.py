#!/usr/bin/env python3

def light_spell_allowed_ingredients() -> list[str]:
    return [
        "earth",
        "air",
        "fire",
        "water"
    ]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients
    record: str = validate_ingredients(ingredients)
    if "INVALID" in record:
        return f"Spell not recorded: {spell_name} ({record})"
    elif "VALID" in record:
        return f"Spell recorded: {spell_name} ({record})"
