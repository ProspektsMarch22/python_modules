class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days

    def show(self) -> str:
        return (f"{self.name}: {"%.2f" % self.height}cm,"
                + f" {self.days} days old\n")

    def grow(self) -> None:
        self.height += (0.4 + (len(self.name)/10))

    def age(self) -> None:
        self.grow()
        self.days += 1


def main() -> None:
    growth = Plant("Rose", 25, 30)
    start = growth.height
    print("=== Garden Plant Growth ===")
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        print(growth.show())
        growth.age()
    final = growth.height - start
    print(f"Growth this week: {"%.2f" % final}cm")


if __name__ == '__main__':
    main()
