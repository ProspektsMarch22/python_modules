class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


def display_plants(plant_list: list) -> None:
    for plant in plant_list:
        elem = Plant(plant[0], plant[1], plant[2])
        print(f"{elem.name}: {elem.height}cm, {elem.age} days old")


def main() -> None:
    plant_list = [
        ["Rose", 25, 30],
        ["Sunflower", 80, 45],
        ["Cactus", 15, 120]
    ]
    print("=== Welcome to My Garden ===")
    display_plants(plant_list)
    print("\n=== End of Program ===")


if __name__ == "__main__":
    main()
