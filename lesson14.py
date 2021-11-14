def checkio(arg):
    reduce = 1
    arg = str(arg)
    for i in arg:
        if int(i) == 0:
            continue
        reduce *= int(i)
    return reduce


if __name__ == "__main__":
    res = checkio(123405)
    print(res)
    res2 = checkio(20506)
    print(res2)
