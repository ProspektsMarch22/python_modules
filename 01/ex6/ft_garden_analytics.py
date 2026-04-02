class Plant:
    class _Stats:
        def __init__(self) -> None:
            self._grow_calls: int = 0
            self._age_calls: int = 0
            self._show_calls: int = 0

        def display(self) -> None:
            print(f"Stats: {self._grow_calls} grow, "
                  f"{self._age_calls} age, 
                  f"{self._show_calls} show")

    def __init__(self, name: str, height: float, days: int) -> None:
        self._name = name
        self._height = height
        self._days = days
        self._stats = Plant._Stats()

    @staticmethod
    def year_older(age : int) -> bool:
        return days > 365

    @classmethod
    def anon_plant(cls) -> "Plant":
        instance = cls.__new__(cls)
        instance._name = "Unknown plant"
        instance._height = 0
        instance._days = 0
        instance._set_defaults()
        return instance

    def show(self) -> None:
        print(f"{self._name}: "
            f"{self._height:.2f}cm, "
            f"{self._days} days old")
        self._stats._show_calls += 1

    def grow(self) -> None:
        self._height += (0.4 + (len(self.name)/10))
        self._stats._grow_calls += 1

    def age(self) -> None:
        self.grow()
        self._days += 1
        self._stats._age_calls += 1


class Flower(Plant):
    def __init__(self, name: str, height: float, days: int, color: str) -> None:
        super().__init__(name, height, days)
        self._color = color
        self._has_bloom: bool = False

    def show(self) -> None:
        if self._has_bloom:
            super().show()
            print(f" Color: {self._color}"
                  f"{self._name} is blooming beautifully!")
        else:
            super().show()
            print(f" Color: {self._color}"
                  f"{self._name} has not bloomed yet")

    def bloom(self) -> None:
        self.has_bloom = True

