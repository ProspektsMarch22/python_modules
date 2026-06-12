#!/usr/bin/env python3


def main() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook directly")
    print("Test import now - this will raise an ImportError")
    try:
        import alchemy.grimoire.dark_spellbook as ds
        print("Testing record dark spell:",
              ds.dark_spell_record("Flame of Ûdun", "Eyeball, bats"))
    except ImportError as e:
        print("There is a circular import! -", e)


if __name__ == '__main__':
    main()
