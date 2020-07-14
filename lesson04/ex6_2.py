# Итератор, повторяющий элементы  списка, определенного заранее
from itertools import cycle


def cycle_iter(source_list, num):
    i = 1
    for el in cycle(source_list):
        if i > num:
            break
        i += 1
        yield el


source_list = [2, 21, 3, 9]

for el in cycle_iter(source_list, 10):
    print(el)
