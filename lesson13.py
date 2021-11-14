def arithmetic(first, second, action):
    data = {
        "+": first + second,
        "-": first - second,
        "*": first * second,
        "/": first / second,
    }
    return data.get(action, "Неизвестная операция")


if __name__ == "__main__":
    res = arithmetic(3, 2, "*")
    print(res)
    res2 = arithmetic(3, 2, "zg")
    print(res2)
