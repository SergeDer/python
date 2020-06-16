# Cумма чисел n + nn + nnn
while 1:
    n = int(input('Введите положительное число "n": '))
    if n <= 0:
        print('Число должно быть положительным!')
    else:
        break

print(f'{n}+{n}{n}+{n}{n}{n}={n + (10 * n + n) + (100 * n + 10 * n + n)}')
