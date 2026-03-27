class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.days = days

    def show(self) -> str:
        return (f"{self.name}: {"%.2f" % self.height}cm,"
                + f" {self.days} days old\n")

    def __str__(self) -> str:
        return "Created: " + self.show()

    def grow(self) -> None:
        self.height += (0.4 + (len(self.name)/10))

    def age(self) -> None:
        self.grow()
        self.days += 1


def main() -> list:
    plants_info: list[tuple[str, float, int]] = [
        ("rose", 25, 30),
        ("oak", 200, 365),
        ("cactus", 5, 90),
        ("sunflower", 80, 45),
        ("fern", 15, 120)
    ]
    print("=== Plant Factory Output ===")
    plants = list[]
    for plant in plants_info:
        new_plant = Plant(plant[0], plant[1], plant[2])
        print(new_plant, end="")
        plants.append(new_plant)
    return plants


if __name__ == "__main__":
    main()
