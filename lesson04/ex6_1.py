# Итератор, генерирующий целые числа, начиная с указанного
from itertools import count


def count_iter(start, end):
    for el in count(start, 1):
        if el > end:
            break
        yield el


start = 5
end = 100

for el in count_iter(start, end):
    print(el)
