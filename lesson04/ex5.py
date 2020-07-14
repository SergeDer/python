# Произведение четных числе от 100 до 1000
from functools import reduce

ex_list = [el for el in range(1, 1001) if el % 2 == 0]
print(reduce(lambda total, amount: total * amount, ex_list))
