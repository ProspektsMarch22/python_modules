class Plant:
    def __init__(self, name: str, height: float = 0, age: int = 0) -> None:
        self.name = name.capitalize()
        self.set_height(height)
        self.set_age(age)

    # Setters and Getters
    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative",
                  "Height update rejected", sep="\n")
            return
        self._height = new_height

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self.name}: Error, age can't be negative",
                  "Age update rejected", sep="\n")
            return
        self._age = new_age

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    # Class methods
    def show(self) -> None:
        print(f"{self.name}:",
              f"{self.get_height()}cm,",
              f"{self.get_age()} days old")

    def grow(self) -> None:
        self.set_height(self.get_height() + 0.8)

    def age(self) -> None:
        self.set_age(self.get_age() + 1)
        self.grow()


def main() -> None:
    print("=== Garden Security System ===")
    rose = Plant("rose", 15, 30)
    print("Plant created: ", end="")
    rose.show()
    print("\n")
    rose.set_height(25.0)
    rose.set_age(30)
    print(f"Height updated: {rose.get_height()}",
          f"Age updated: {rose.get_age()}", sep="\n", end="\n\n")
    rose.set_height(-3.9)
    rose.set_age(-45)
    print("\nCurrent state: ", end="")
    rose.show()


if __name__ == "__main__":
    main()
