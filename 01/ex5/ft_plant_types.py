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

def main() -> None:
    flower = Flower("Rose", 15, 10, "red")
    tree = Tree("oak", 200, 365, 2.5) 
    print("=== Flower")
    print(flower.show_flower())
    flower.bloom()
    print(flower.show_flower())
    print("\n=== Tree")
    print(tree.show_tree())
    tree.shade()

if __name__ == '__main__':
    main()
