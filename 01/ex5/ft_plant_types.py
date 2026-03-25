class FatherPlant:
    def __init__(self, name: str, height: int, days: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.days = days


class Flower(FatherPlant):
    def __init__(self, name: str, height: int, days: int, color: str) -> None:
        super().__init__(name, height, days)
        self.color = color

    def __str__(self) -> str:
        return (
            f"{self.name} (Flower): {self.height}cm, {self.days} days"
            + f", {self.color} color\n"
            + f"{self.name} is blooming beautifully!\n"
        )


class Tree(FatherPlant):
    def __init__(self, name: str, height: int, days: int, diam: int) -> None:
        super().__init__(name, height, days)
        self.diameter = diam

    def __str__(self) -> str:
        return (
            f"{self.name} (Tree): {self.height}cm, {self.days} days"
            + f", {self.diameter}cm diameter\n"
            + f"{self.name} provides {((self.days/self.diameter) * 2) + 5}"
            + " square meters of shade\n"
        )


class Vegetable(FatherPlant):
    def __init__(self, name: str, height: int, days: int, hrvst: str) -> None:
        super().__init__(name, height, days)
        self.harvest = hrvst