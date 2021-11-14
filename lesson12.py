def foursquare(arg):
    perimeter = arg * 4
    square = arg * 2
    diagonal = round(arg * (2 ** 0.5), 2)
    return perimeter, square, diagonal


if __name__ == "__main__":
    res = foursquare(10)
    print("Периметр, площадь, диагональ квадрата")
    print(res)
