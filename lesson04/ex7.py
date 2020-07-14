# Итератор из факториалов
def fact(n):
    i = 1
    factorial = 1
    while i <= n:
        factorial *= i
        i += 1
        yield factorial


for el in fact(5):
    print(el)
