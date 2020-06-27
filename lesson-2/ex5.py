# Довавление элемента в невозрастающий список
while 1:
    try:
        new_el = int(input('Введите новый элемент рейтинга: '))
        if new_el <= 0:
            print('Введите натуральное число!')
        else:
            break
    except ValueError:
        print('Введите натуральное число!')

rating = [7, 5, 3, 3, 2, new_el]
rating.sort(reverse=True)
print(rating)
