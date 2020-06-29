# Сумма двух наибольших аргументов
def my_func(a, b, c):
    try:
        abc_list = sorted([a, b, c])
        abc_sum = abc_list[1] + abc_list[2]
        return abc_sum
    except TypeError:
        return


print(my_func(77, 2, 5))
