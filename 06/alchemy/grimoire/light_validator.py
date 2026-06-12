#!/usr/bin/env python3

def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    allowed: list[str] = light_spell_allowed_ingredients()
    for item in allowed:
        if item in ingredients.lower():
            return ingredients + " - VALID"
    return ingredients + " - INVALID"
