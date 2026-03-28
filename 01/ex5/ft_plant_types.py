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
        print(f"[asking the {self.name} to bloom]")
        self.has_bloom = True


def main() -> None:
    flower = Flower("Rose", 15, 10, "red")
    print(flower.show_flower())
    flower.bloom()
    print(flower.show_flower())

if __name__ == '__main__':
    main()
