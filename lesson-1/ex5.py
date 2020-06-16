# Соотношение выручки и издержек
while 1:
    income = int(input('Введите выручку: '))
    if income <= 0:
        print('Выручка должна быть положительной!')
    else:
        break

while 1:
    outgo = int(input('Введите издержки: '))
    if outgo <= 0:
        print('Издержки должны быть положительны!')
    else:
        break

if income > outgo:
    print('Поздравляем! Выручка больше издержек! Прибыль: {:.2f} Рентабельность: {:.2f}'.format(income - outgo, (
            income - outgo) / outgo))
    number_of_emp = int(input('Введите число сотрудников: '))
    print('Прибыль на одного сотрудника: {:.2f}'.format((income - outgo) / number_of_emp))
elif income == outgo:
    print('Выручка равна издержкам. Вы работаете а ноль!')
else:
    print('Выручка меньше издержек. У вас убытки!')
