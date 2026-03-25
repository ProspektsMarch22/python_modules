class Plant:
    def __init__(self, name: str, height: int, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days

    def __str__(self) -> str:
        return f"Created: {self.name}: ({self.height}, {self.days} days)"


def main() -> None:
    plants = [
        ["Rose", 25, 30],
        ["Oak", 200, 365],
        ["Cactus", 5, 90],
        ["Sunflower", 80, 45],
        ["Fern", 15, 120]
    ]
    print("=== Plant Factory Output ===")
    for plant in plants:
        print(Plant(plant[0], plant[1], plant[2]))
    print(f"\nTotal plants created: {len(plants)}")


if __name__ == "__main__":
    main()
