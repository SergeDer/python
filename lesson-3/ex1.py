# Деление чисел
def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return
    except TypeError:
        return


print(division(1, 0))
