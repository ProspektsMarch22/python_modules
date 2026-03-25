def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_str = seed_type.capitalize()
    if (unit == "packets"):
        print(f"{seed_str} seeds: {quantity} {unit} available")
    elif (unit == "grams"):
        print(f"{seed_str} seeds: {quantity} {unit} total")
    elif (unit == "area"):
        print(f"{seed_str} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
