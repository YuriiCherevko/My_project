import math

input_int = 867
first_int = (input_int % 10) * 100
second_int = (math.floor((input_int % 100) / 10)) * 10
third_int = math.floor((input_int % 1000) / 100)
result = first_int + second_int + third_int
print(result)
