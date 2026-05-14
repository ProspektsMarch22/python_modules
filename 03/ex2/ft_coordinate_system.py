#!/usr/bin/python3


import math


# Given the constraints on the subject, I'm very limited to what
# I can do for the get_player_pos() definition.
# I commented my preferred solution, which in my opinion is equal
# In terms of abstraction.


def get_player_pos() -> tuple:
    while True:
        pos_input: str = input("Enter new coordinates"
                               + "as floats in format 'x,y,z': ")
        subs: list = pos_input.split(',')
        vector: list[float] = list()
        try:
            # can't use map, but if i could, then:
            #
            # vector: tuple = tuple(map(float, subs))
            #
            # This naturally scratchs the declaration and initialization
            # of the latter "vector" variable
            for coords in subs:
                vector.append(float(coords))
        except ValueError:
            print("Invalid syntax")
        else:
            # I'd have to only return the vector
            #
            # return vector
            return tuple(vector)


def v_distance(v_one: tuple, v_two: tuple) -> float:
    return (math.sqrt(((v_two[0] - v_one[0])**2)
            + ((v_two[1] - v_one[1])**2)
            + ((v_two[2] - v_one[2])**2)))


def main() -> None:
    print("=== Game Coordinate System ===")
    print("\nGet a first set of coordinates")
    v_one: tuple = get_player_pos()
    print("Got a first tuple: ", v_one)
    print(f"It includes: X={v_one[0]}, Y={v_one[1]}, Z={v_one[2]}")
    print("Distance to center:", round(v_distance((0, 0, 0), v_one), 4))
    print("\nGet a second set of coordinates")
    v_two: tuple = get_player_pos()
    print("Distance between the 2 sets of coordinates:",
          round(v_distance(v_one, v_two), 4))


if __name__ == '__main__':
    main()
