#!/bin/usr/env python3

from sys import argv
from typing import IO


def display_file_data() -> None:
    file_names: list[str] = argv[1:]
    if (len(file_names) == 0):
        print("Usage: ft_ancienty_text.py <file1>, <file2>, ...")
        return
    print("=== Cyber Archives Recovery ===")
    for file in file_names:
        try:
            f: IO[str] | None = None
            print(f"Accessing file '{file}'")
            f = open(file)
            content: str = f.read()
        except OSError as e:
            print(f"Error opening file '{file}':", e)
        else:
            print("-" * 3, end="\n\n")
            print(content)
            print("-" * 3)
        finally:
            if f is not None:
                f.close()
                print(f"File '{file}' closed.")


def main() -> None:
    display_file_data()


if __name__ == '__main__':
    main()
