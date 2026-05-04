class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.days = age
        print("Created: ", end="")
        self.show()

    def show(self) -> None:
        print(f"{self.name}:",
              f"{round(self.height, 1)}cm,",
              f"{self.days} days old")

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.days += 1
        self.grow()


def main() -> None:
    print("=== Plant Factory Output ===")
    plants = [
        ["rose", 15.0, 30],
        ["oak", 200.0, 365],
        ["cactus", 5.0, 90],
        ["sunflower", 80.0, 45],
        ["fern", 15.0, 120]
    ]
    for plant in plants:
        name, height, age = plant[0], plant[1], plant[2]
        Plant(name, height, age)


if __name__ == '__main__':
    main()
