input_string = "В единственной строке записан текст. Для каждого слова из данного оно текста," \
               " подсчитайте сколько раз оно встречалось в этом тексте. Для оно данного раз."
out_list = input_string.split(" ")
count_dictionary = {}

for i in out_list:
      if count_dictionary.get(i):
            count_dictionary[i] += 1
      else:
            count_dictionary[i] = 1
print(count_dictionary)
