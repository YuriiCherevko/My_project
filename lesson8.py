import random

class_list = [random.randint(160, 200) for _ in range(15)]
class_list.sort(reverse=True)
print("Список роста детей в классе")
print(class_list)
print("Введите рост Пети:")
peters_height = int(input())

for i, ch in enumerate(class_list):
    if i == len(class_list) - 1:
        class_list.append(peters_height)
        print("Порядковый номер Пети:")
        print(i + 2)
        print("Список класса с Петей:")
        print(class_list)
        break
    elif peters_height > ch:
        class_list.insert(i, peters_height)
        print("Порядковій номер Пети:")
        print(i + 1)
        print("Список класса с Петей:")
        print(class_list)
        break
