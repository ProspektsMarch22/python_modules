class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> str:
        return (f"{self.name}: {"%.2f" % self.height}cm,"
                + f" {self.days} days old\n")


def main() -> None:
    print("=== Garden Plant Registry ===")
    print(Plant("Rose", 25, 30).show())
    print(Plant("Sunflower", 80, 45).show())
    print(Plant("Cactus", 15, 120).show())


if __name__ == '__main__':
    main()
