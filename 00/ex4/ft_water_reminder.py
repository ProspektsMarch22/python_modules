def ft_water_reminder():
    woter = int(input("Days since last watering: "))
    if (woter > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
