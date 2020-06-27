# Время года по введенному номеру месяца (реализация через словарь)
season_dict = {'Зима': (12, 1, 2), 'Весна': (3, 4, 5), 'Лето': (6, 7, 8), 'Осень': (9, 10, 11)}
month_dict = {'1': 'Январь', '2': 'Февраль', '3': 'Март', '4': 'Апрель', '5': 'Май', '6': 'Июнь', '7': 'Июль',
              '8': 'Август', '9': 'Сентябрь', '10': 'Октябрь', '11': 'Ноябрь', '12': 'Декабрь'}

while 1:
    try:
        month_num = int(input('Введите номер месяца: '))
        if month_num not in range(1, 13):
            print('Введите число от 1 до 12!')
        else:
            break
    except ValueError:
        print('Введите число от 1 до 12!')

for i in range(len(list(season_dict.keys()))):
    if month_num in list(season_dict.values())[i]:
        print(f'Месяц №{month_num}: {month_dict.get(str(month_num))} - {list(season_dict.keys())[i]}')
        break
