#!/usr/bin/env python3

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    sorted_artifacts: list[dict] = sorted(artifacts,
                                          key=lambda x: x['power'],
                                          reverse=True)
    return sorted_artifacts


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    power = list(filter(lambda x: (x['power'] >= min_power), mages))
    return power


def spell_transformer(spells: list[str]) -> list[str]:
    spell_names = list(map(lambda s: "* " + s + " *", spells))
    return spell_names


def mage_stats(mages: list[dict]) -> dict:
    min_power = min(mages, key=lambda x: x['power'])['power']
    max_power = max(mages, key=lambda x: x['power'])['power']
    avg_power = round(sum(map(lambda x: x['power'], mages)) / len(mages), 2)
    return {
        'max_power': max_power,
        'min_power': min_power,
        'avg_power': avg_power
    }


if __name__ == '__main__':
    print("Test suite for the functions")
    art = [
        {
            'name': "Master Sword",
            'power': 190,
            'type': "Sword"
        },
        {
            'name': "Dark Grimoire",
            'power': 400,
            'type': "Spellbook"
        },
        {
            'name': "Palantir",
            'power': 0,
            'type': "Middle-Earth Mcguffin"
        }
    ]
    print("Artifact sorter")
    print(artifact_sorter(art), end="\n\n")
    mages = [
        {
            'name': "Sage",
            'power': 93,
            'element': "earth"
        },
        {
            'name': "Alex",
            'power': 96,
            'element': "shadow"
        },
        {
            'name': "River",
            'power': 53,
            'element': "light"
        },
        {
            'name': "Jordan",
            'power': 97,
            'element': "fire"
        },
        {
            'name': "Zara",
            'power': 62,
            'element': "water"
        },
        {
            'name': "Nova",
            'power': 59,
            'element': "wind"
        },
        {
            'name': "Kai",
            'power': 71,
            'element': "ice"
        }
    ]
    spells = ["tsunami", "blizzard", "lightning", "flash"]
    print("Power Filter")
    print(power_filter(mages, 70), end="\n\n")
    print("Spell Transformer")
    print(spell_transformer(spells), end="\n\n")
    print("Mage Stats")
    print(mage_stats(mages))
