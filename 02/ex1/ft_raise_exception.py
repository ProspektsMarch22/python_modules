def input_temperature(temp_str: str) -> int:
    temp_int = int(temp_str)
    if (temp_int > 40 or temp_int < 0):
        raise Exception()
    else:
        return temp_int


def test_temperature(input_data: str) -> None:
    print("\nInput data is", input_data)
    try:
        temp_int: int = input_temperature(input_data)
    except ValueError:
        print("Caught input_temperature error:",
              "invalid literal for int() with base 10",
              f"'{input_data}'")
    except Exception:
        if int(input_data) > 40:
            print("Caught input_temperature error:",
                  f"{input_data}°C is too hot for plants",
                  "(max 40°C)")
        elif int(input_data) < 0:
            print("Caught input_temperature error:",
                  f"{input_data}°C is too cold for plants",
                  "(min 0°C)")
    else:
        print("Temperature is now",
              f"{temp_int}°C")


def main() -> None:
    print("=== Garden Temperature Checker ===")
    test_temperature("25")
    test_temperature("abc")
    test_temperature("100")
    test_temperature("-50")
    print("\nAll tests completed - Program didn't crash!")


if __name__ == '__main__':
    main()
