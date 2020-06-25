# Время года по введенному номеру месяца (реализация через список)
while 1:
    try:
        month_num = int(input('Введите номер месяца: '))
        if month_num not in range(1, 13):
            print('Введите число от 1 до 12!')
        else:
            break
    except ValueError:
        print('Введите число от 1 до 12!')

month_list = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь',
              'Декабрь']
print(f'Месяц №{month_num}: {month_list[month_num - 1]}')
