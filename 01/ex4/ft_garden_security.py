class Plant:
    def __init__(self, name: str, height:float=0, days:int=0) -> None:
        self._name = name.capitalize()
        self.set_height(height)
        self.set_age(days)

    def get_height(self) -> float:
        return self._height

    def set_height(self, height) -> None:
        if (height < 0):
            print(f"\n{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            try:
                if (self.get_height()):
                    self._height = height
                    print(f"Height updated: {self.get_height()}cm")
            except AttributeError:
                self._height = height

    def get_age(self) -> int:
        return self._age

    def set_age(self, age) -> None:
        if (age < 0):
            print(f"\n{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            try:
                if (self.get_age()):
                    self._age = age
                    print(f"Age updated: {self.get_age()} days")
            except AttributeError:
                self._age = age

    def show(self) -> str:
        return (f"{self._name}: {self.get_height():.2f}cm,"
                + f" {self.get_age()} days old\n")

    def __str__(self) -> str:
        return "Plant created: " + self.show()


def main() -> None:
    print("=== Garden Security System ===")
    plant = Plant("rose", 15, 10)
    print(plant)
    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-1)
    plant.set_age(-1)
    print(f"\nCurrent state: " + plant.show())


if __name__ == "__main__":
    main()
