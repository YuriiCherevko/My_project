import random

first_list = [random.randint(0, 20) for _ in range(15)]
second_list = [random.randint(10, 30) for _ in range(15)]
# для проверки
print(first_list)
print(second_list)

print(len([i for i in [*first_list, *second_list] if [*first_list, *second_list].count(i) == 1]))
