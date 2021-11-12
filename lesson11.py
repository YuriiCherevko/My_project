dict_1 = {'a': 21, 'b': 2, 'k': 13, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}
dict_2 = {'a': 6, 'z': 1, 'x': 9, 'c': 6, 'f': 3, 'e': 48, 'k': 12}

dict_out = dict_1.copy()
dict_out.update(dict_2)
print(dict_out)

for k, v in dict_out.items():
    if v < dict_1.get(k, 0):
        dict_out[k] = dict_1[k]

print(dict_out)
