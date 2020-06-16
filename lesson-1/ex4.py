# Наибольшая цифра в числе
while 1:
    source_number = int(input('Введите положительное число: '))
    if source_number <= 0:
        print('Число должно быть положительным!')
    else:
        break

max_numeral = 0
number = source_number

while number != 0:
    numeral = number % 10  # Вычисляем цифру младшего разряда
    if max_numeral < numeral:  # Узнаем, больше ли данная цифра предыдущих
        max_numeral = numeral
    number = number // 10  # Уменьшаем число на разряд

print(f'В числе {source_number} наибольшая цифра {max_numeral}')
