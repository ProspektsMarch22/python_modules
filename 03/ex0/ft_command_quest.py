import sys


def main() -> None:
    print("=== Command Quest ===")
    print("Program name:", sys.argv[0])
    if (len(sys.argv) == 1):
        print("No arguments provided!")
    else:
        print("Arguments received:", len(sys.argv) - 1)
        for i in range(1, len(sys.argv)):
            print(f"Argument {i}:", sys.argv[i])
    print("Total arguments:", len(sys.argv))


if __name__ == '__main__':
    main()
