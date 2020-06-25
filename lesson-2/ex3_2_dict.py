# Время года по введенному номеру месяца (реализация через словарь)
while 1:
    try:
        month_num = int(input('Введите номер месяца: '))
        if month_num not in range(1, 13):
            print('Введите число от 1 до 12!')
        else:
            break
    except ValueError:
        print('Введите число от 1 до 12!')

month_dict = {'1': ('Январь', 'Зима'), '2': ('Февраль', 'Зима'), '3': ('Март', 'Весна'), '4': ('Апрель', 'Весна'),
              '5': ('Май', 'Весна'), '6': ('Июнь', 'Лето'), '7': ('Июль', 'Лето'),
              '8': ('Август', 'Лето'), '9': ('Сентябрь', 'Осень'), '10': ('Октябрь', 'Осень'), '11': ('Ноябрь', 'Осень'),
              '12': ('Декабрь', 'Зима')}

print(f'Месяц №{month_num}: {month_dict.get(str(month_num))[0]}, {month_dict.get(str(month_num))[1]}')
