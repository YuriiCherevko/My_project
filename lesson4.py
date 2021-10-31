input_string = "я ввел мою уникальную"
first_string = f"Это строка в которую {input_string} новую строку"
second_string = first_string.replace("я ввел мою уникальную", "замена в строке")
find_word = second_string.find("строка")

if find_word != -1:
    has_second_string_word = "ДА"
else:
    has_second_string_word = "НЕТ"

print(first_string)
print(second_string)
print(len(second_string))
print(has_second_string_word)
