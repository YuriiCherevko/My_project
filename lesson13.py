def arithmetic(first, second, action):
    math_data = {
        "+": first + second,
        "-": first - second,
        "*": first * second,
        "/": first / second,
    }
    return math_data.get(action, "Неизвестная операция")


if __name__ == "__main__":
    res = arithmetic(3, 2, "*")
    print(res)
    res2 = arithmetic(3, 2, "zg")
    print(res2)
