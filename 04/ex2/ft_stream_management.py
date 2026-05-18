#!/bin/usr/env python3

from sys import argv, stdin, stderr
from typing import IO


def display_file_data() -> None:
    file_names: list[str] = argv[1:]
    if (len(file_names) == 0):
        print("Usage: ft_ancienty_text.py <file1>, <file2>, ...")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    for file in file_names:
        content: str | None = None
        f: IO[str] | None = None
        try:
            print(f"Accessing file '{file}'")
            f = open(file)
            content = f.read()
        except OSError as e:
            print(f"[STDERR] Error opening file '{file}':", e, file=stderr)
        else:
            print("-" * 3, end="\n\n")
            print(content)
            print("-" * 3)
        finally:
            if f is not None:
                f.close()
                print(f"File '{file}' closed.")
        if content is not None and len(content) > 0:
            print("\nTransform data:")
            print("-" * 3, end="\n\n")
            lines: list[str] = content.split("\n")
            lines.pop(-1)
            for i in range(len(lines)):
                lines[i] = lines[i] + "#\n"
                print(lines[i], end="")
            print("\n" + "-" * 3)
            print("Enter new file namr (or empty): ", end="", flush=True)
            new_file: str = stdin.readline().rstrip("\n")
            if (len(new_file) > 0):
                print(f"Saving data to '{new_file}'")
                n_f: IO[str] | None = None
                try:
                    n_f = open(new_file, "w")
                    for line in lines:
                        n_f.write(line)
                    print(f"Data saved in file '{new_file}'")
                except OSError as e:
                    print(f"[STDERR] Error writing to file '{new_file}':",
                          e, file=stderr)
                    print("Data not saved.")
                finally:
                    if n_f is not None:
                        n_f.close()
            else:
                print("Not saving data.")


def main() -> None:
    display_file_data()


if __name__ == '__main__':
    main()
