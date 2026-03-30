class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.days = days

    def show(self) -> str:
        return (f"{self.name}: {self.height:.2f}cm,"
                + f" {self.days} days old\n")

    def grow(self) -> None:
        self.height += (0.4 + (len(self.name)/10))

    def age(self) -> None:
        self.grow()
        self.days += 1


class Flower(Plant):
    def __init__(self, name: str, height: float, days: int, color: str) -> None:
        super().__init__(name, height, days)
        self.color = color
        self.has_bloom : bool = False

    def show_flower(self) -> str:
        if self.has_bloom:
            return (super().show()
                + f" Color: {self.color}\n"
                + f"{self.name} is blooming beautifully!\n")
        return (super().show()
            + f" Color: {self.color}\n"
            + f"{self.name} has not bloomed yet")

    def bloom(self) -> None:
        print(f"[asking the {self.name.lower()} to bloom]")
        self.has_bloom = True


class Tree(Plant):
    def __init__(self, name: str, height: float, days: int, rad: float) -> None:
        super().__init__(name, height, days)
        self.diameter = rad * 2

    def show_tree(self) -> str:
        return (super().show()
            + f" Trunk diameter: {self.diameter:.2f}cm")

    def shade(self) -> None:
        print(f"[asking the {self.name.lower()} to produce shade]")
        print(f"Tree {self.name} now produces"
              +f" a shade of {self.height}cm long and {self.diameter}cm wide")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, days: int, season: str,
                 nvalue: int) -> None:
        super().__init__(name, height, days)
        self.season = season
        self.nvalue = nvalue

    def show_vegetable(self) -> str:
        return (super().show()
            + f" Harvest season: {self.season}\n"
            + f" Nutritional value: {self.nvalue}")

    def age_vegetable(self, time: int) -> None:
        print(f"[make {self.name.lower()} grow and age for {time} days]")
        for i in range(time):
            super().age()
            self.nvalue += 1


def main() -> None:
    print("=== Garden Plant Types ===")
    flower = Flower("Rose", 15, 10, "red")
    tree = Tree("oak", 200, 365, 2.5)
    vegetable = Vegetable("tomato", 5, 10, "April", 0)
    print("=== Flower")
    print(flower.show_flower())
    flower.bloom()
    print(flower.show_flower(), end="")
    print("\n=== Tree")
    print(tree.show_tree())
    tree.shade()
    print("\n=== Vegetable")
    print(vegetable.show_vegetable())
    vegetable.age_vegetable(20)
    print(vegetable.show_vegetable())

if __name__ == '__main__':
    main()
