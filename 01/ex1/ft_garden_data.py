class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self.height}cm,", end="")
        print(f" {self.age} days old")


def main() -> None:
    print("=== Garden Plant Registry ===")
    Plant("Rose", 25, 30).show()
    Plant("Sunflower", 80, 45).show()
    Plant("Cactus", 15, 120).show()


if __name__ == '__main__':
    main()
