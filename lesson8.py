import random

class_list = [random.randint(160, 200) for _ in range(15)]
class_list.sort(reverse=True)
print("Список роста детей в классе")
print(class_list)
print("Введите рост Пети:")
peters_height = int(input())

for i, ch in enumerate(class_list):
    if i == len(class_list) - 1:
        print("Порядковый номер Пети:")
        print(i + 2)
    elif peters_height > ch:
        print("Порядковій номер Пети:")
        print(i + 1)
        break
