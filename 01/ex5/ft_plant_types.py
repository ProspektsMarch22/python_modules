# Parent Class
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


# Child classes
class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.has_bloom = False

    def bloom(self) -> None:
        print(f"[asking the {self.name.lower()} to bloom]")
        self.has_bloom = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.has_bloom is True:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


def main() -> None:
    print("=== Garden Plant Types ===")
    print("=== Flower")
    flower = Flower("rose", 15.0, 30, "red")
    flower.show()
    flower.bloom()
    flower.show()


if __name__ == '__main__':
    main()
