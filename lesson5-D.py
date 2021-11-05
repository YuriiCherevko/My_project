print("Enter the height of the pyramid!")
stars_height = int(input())
if stars_height <= 2:
    print("Your pyramid is very small!")
else:
    step = stars_height * 2 - 1
    for i in range(step):
        step -= 1
        indent = step - 1
        if i < (stars_height - 1 / 2):
            print("  " * int(stars_height - i) + "* " * (i * 2 + 1))
        elif step != 0:
            print("  " * (i + 2 - stars_height) + "*" + "  " * indent + " * " + "  " * indent + "*")
        else:
            print("  " * (i + 2 - stars_height) + "*")
