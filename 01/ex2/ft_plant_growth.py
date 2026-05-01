class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.days = age

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
    rose = Plant("rose", 25, 30)
    initial_height = rose.height
    print("=== Garden Plant Growth ===")
    rose.show()
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.age()
        rose.show()
    print(f"Growth this week: {round(rose.height - initial_height, 1)}cm")


if __name__ == '__main__':
    main()
