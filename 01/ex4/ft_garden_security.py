class SecurePlant:
    def __init__(self, name: str, height: int, days: int) -> None:
        self.__name = name
        print(f"Plant created: {self.__name.capitalize()}")
        print(self.set_height(height))
        print(self.set_age(days))

    def get_name(self) -> str:
        return self.__name

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def set_height(self, new_height: int) -> str:
        if new_height < 0:
            return (
                f"\nInvalid operation attempted: height {new_height}cm"
                + " [REJECTED]\nSecurity: Negative height rejected\n"
            )
        else:
            self.__height = new_height
            return (f"Height updated: {self.__height}cm [OK]")

    def set_age(self, new_age: int) -> str:
        if new_age < 0:
            return (
                f"\nInvalid operation attempted: age {new_age} days old"
                + " [REJECTED]\nSecurity: Negative age rejected\n"
            )
        else:
            self.__age = new_age
            return (f"Age updated: {self.__age} days [OK]")

    def get_plant_status(self) -> str:
        return (
            f"Current plant: {self.get_name()} ({self.get_height()}cm,"
            + f" {self.get_age()} days)"
        )


def main() -> None:
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", 25, 30)
    print(plant.set_height(-5))
    print(plant.get_plant_status())


if __name__ == "__main__":
    main()
