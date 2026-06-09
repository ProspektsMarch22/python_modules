#!/usr/bin/env python3

import alchemy.elements as el


def main() -> None:
    print("=== Alembic 2 ===")
    print("Accessing alchemy/elements.py using 'import ...' structure")
    print("Testing create_earth:", el.create_earth())


if __name__ == '__main__':
    main()
