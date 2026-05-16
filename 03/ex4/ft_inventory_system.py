#!/usr/bin/env python3


import sys


class PlayerInventory:
    def __init__(self) -> None:
        self.item_list: list[str] = list()
        self.inventory: dict[str, int] = {}

    def get_player_inventory(self, arg_list: list[str]) -> dict[str, int]:
        if len(arg_list) < 1:
            return {}
        for arg in arg_list:
            dict_pair: list[str] = arg.split(":")
            if len(dict_pair) != 2:
                print(f"Error - Invalid parameter '{arg}'")
            else:
                item_name = dict_pair[0].strip()
                try:
                    quantity = int(dict_pair[1])
                    if item_name in self.inventory:
                        print(f"Redundant item '{item_name}' - discarding")
                    else:
                        self.inventory[item_name] = quantity
                except ValueError as e:
                    print(f"Quantity error for '{item_name}':", e)
        return self.inventory

    def get_player_item_list(self) -> list[str]:
        return list(self.inventory.keys())

    @property
    def count_items(self) -> int:
        return len(self.inventory)

    @property
    def item_quantity(self) -> int:
        return sum(self.inventory.values())

    def display_item_percentages(self) -> None:
        for k in self.inventory.keys():
            item_percentage: float = self.inventory[k]/self.item_quantity
            item_percentage *= 100
            print(f"Item {k} represents",
                  f"{round(item_percentage, 1)}%")

    def get_most_qty(self) -> str:
        most_qty: str = list(self.inventory.keys())[0]
        for k in self.inventory.keys():
            if self.inventory[k] > self.inventory[most_qty]:
                most_qty = k
        return most_qty

    def get_least_qty(self) -> str:
        least_qty: str = list(self.inventory.keys())[0]
        for k in self.inventory.keys():
            if self.inventory[k] < self.inventory[least_qty]:
                least_qty = k
        return least_qty

    def update_inventory(self, item: str) -> dict[str, int]:
        item_pair = item.split(":")
        try:
            self.inventory.update({item_pair[0].strip(): int(item_pair[1])})
        except ValueError as e:
            print(f"Quantity error for '{item_pair[0]}':", e)
        finally:
            return self.inventory


def main() -> None:
    print("=== Inventory System Analysis ===")
    player_inventory = PlayerInventory()
    print("Got inventory:",
          player_inventory.get_player_inventory(sys.argv[1:]))
    print("Item list:",
          player_inventory.get_player_item_list())
    print(f"Total quantity of the {player_inventory.count_items} items:",
          player_inventory.item_quantity)
    player_inventory.display_item_percentages()
    print("Item most abundant:",
          player_inventory.get_most_qty(),
          "with quantity",
          player_inventory.inventory[player_inventory.get_most_qty()])
    print("Item least abundant:",
          player_inventory.get_least_qty(),
          "with quantity",
          player_inventory.inventory[player_inventory.get_least_qty()])
    print("Updated inventory:",
          player_inventory.update_inventory('magic_potion : 1'))


if __name__ == '__main__':
    main()
