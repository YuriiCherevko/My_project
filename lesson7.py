import random

input_list = [random.randint(0, 20) for _ in range(10)]
print("Для сверки")
print(input_list)

iter_list = []
for i, ch in enumerate(input_list):
    if i == 0 or i == len(input_list)-1:
        continue
    elif ch > input_list[i - 1] and ch > input_list[i + 1]:
        iter_list.append(ch)
print(len(iter_list))

