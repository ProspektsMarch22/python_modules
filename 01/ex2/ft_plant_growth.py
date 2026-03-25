class Plant:
    def __init__(self, name: str, height: int, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days

    def grow(self) -> None:
        self.height += 1

    def age(self) -> None:
        self.days += 1

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.days} days old"


def main() -> None:
    plant = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    initial_growth = plant.height
    print(f"{plant.get_info()}")
    print("=== Day 7 ===")
    for _ in range(1, 7):
        plant.grow()
        plant.age()
    final_growth = plant.height
    print(f"{plant.get_info()}")
    print(f"Growth this week: +{final_growth - initial_growth}cm")


if __name__ == "__main__":
    main()
