print("Enter the height of the pyramid!")
stars_height = int(input())
if stars_height <= 1:
    print("Your pyramid is very small!")
else:
    for i in range(stars_height):
        half_width = int(stars_height - i)
        print("  " * half_width + "* " * (i * 2 + 1))
