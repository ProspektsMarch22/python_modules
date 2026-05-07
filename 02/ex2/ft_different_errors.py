def garden_operations(operation_number: int) -> None:
    match operation_number:
        case 0:
            int("abc")
        case 1:
            42/0
        case 2:
            open("/non/existent/file")
        case 3:
            1 + "abc"


def test_error_type(operation_number: int) -> None:
    try:
        garden_operations(operation_number)
    except ValueError:
        print("Caught ValueError:",
              "invalid literal for int() with base 10",
              "'abc'")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError:",
              "division by zero")
    except FileNotFoundError:
        print("Caught FileNotFoundError:",
              "[Errno 2] No such file or directory:",
              "/non/existent/file")
    except TypeError:
        print("Caught TypeError:",
              "can only concatenate str (not \"int\") to str")
    else:
        print("Operation completed succesfully")


def main() -> None:
    print("=== Garden Error Types Demo ===")
    print("Testing operation 0...")
    test_error_type(0)
    print("Testing operation 1...")
    test_error_type(1)
    print("Testing operation 2...")
    test_error_type(2)
    print("Testing operation 3...")
    test_error_type(3)
    print("Testing operation 4...")
    test_error_type(4)
    print("\nAll error types tested succesfully!")


if __name__ == '__main__':
    main()
