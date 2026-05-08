class GardenError(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message) -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message) -> None:
        super().__init__(message)


def main() -> None:
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting Plant Error...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print("\nTesting Water Error...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print("\nTesting catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        raise WaterError("Not enought water in the tank!")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print("\nAll custom error types work correctly!")


if __name__ == '__main__':
    main()
