class GardenError(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message) -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> str:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    return "[OK]"


def test_watering_system(plants: list) -> None:
    print("Opening watering system")
    try:
        for plant in plants:
            print(f"Watering {plant}:", water_plant(plant))
    except PlantError as e:
        print(f"Caught PlantError: {e}",
              ".. ending tests and returning to main", sep="\n")
    finally:
        print("Closing watering system")


def main() -> None:
    print("=== Garden Watering System ===")
    print("\nTesting valid plants...")
    plants = ['Tomato', 'Lettuce', 'Carrots']
    test_watering_system(plants)
    print("\nTesting invalid plants...")
    plants = ['Tomato', 'lettuce', 'Carrots']
    test_watering_system(plants)
    print("\nCleanup always happens, even with errors!")


if __name__ == '__main__':
    main()
