def my_funk(model: str, color: str, year: int) -> dict:
    """
    :return:
    """
    # return {'model': model, 'color': color, 'year': year}
    yield


if __name__ == "__main__":
    res = my_funk("nissaan", "black", 2018)
    print(res)


def bread(func):
    def wrapper(a, b):
        func(a, b)
        print("<\______/>")

    return wrapper


def ingredients(func):
    def wrapper(c, d):
        print("#помидоры#")
        func(c, d)
        print("~салат~")

    return wrapper


@bread
@ingredients
def sandwich(c, d, food="--ветчина--"):
    print(food)
    print(c)
    print(d)


# sandwich = bread(ingredients(sandwich))
sandwich("aaaa", "bbb")
