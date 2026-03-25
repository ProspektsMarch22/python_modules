def recursive(current, day):
    if (day + 1) == current:
        return
    print(f"Day {current}")
    recursive(current + 1, day)


def ft_count_harvest_recursive():
    recursive(1, int(input("Days until harvest: ")))
    print("Harvest time!")
