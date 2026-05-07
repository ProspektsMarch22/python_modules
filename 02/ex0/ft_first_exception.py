def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature(input_data: str) -> None:
    print("\nInput data is", input_data)
    try:
        temp_int: int = input_temperature(input_data)
    except ValueError:
        print("Caught input_temperature error:",
              "invalid literal for int() with base 10",
              f"'{input_data}'")
    else:
        print("Temperature is now",
              f"{temp_int}°C")


def main() -> None:
    print("=== Garden Temperature ===")
    test_temperature("25")
    test_temperature("abc")
    print("\nAll tests completed - Program didn't crash!")


if __name__ == '__main__':
    main()
