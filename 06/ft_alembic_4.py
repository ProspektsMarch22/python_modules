#!/usr/bin/env python3

import alchemy


def main() -> None:
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print("Testing create_air:", alchemy.create_air())
    print("Now show that not all functions can be reached")
    print("THIS EXCEPTION IS SUPPOSED TO HAPPEN")
    print("Testing the hidden create_earth:", alchemy.create_earth())


if __name__ == '__main__':
    main()
