# Для проверки
# set_1 = {1, 2, 3, 4, 5}
set_1 = {1, 2, 3, 4}
set_2 = {2, 3, 4, 5}
superset = {*set_1, *set_2}

is_superset = True if set_1 == superset else False
print(is_superset)
