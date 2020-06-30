# Деление чисел
def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return


a = float(input('Введите число "a": '))
b = float(input('Введите число "b": '))
div = round(division(a, b), 2)
print(f'Результат деления a на b: {div}') if div is not None else print('Делить на ноль нельзя!')
