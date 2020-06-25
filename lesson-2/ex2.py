# Парный обмен элементами в списке
list_input = input('Введите список. Элементы спика разделяйте пробелами: ')  # Пример ввода: 12 44 aa
list_result = list_input.split()
list_rev = list_result

for i in range(0, len(list_result) - 1, 2):
    tmp = list_result[i]
    list_rev[i] = list_result[i + 1]
    list_rev[i + 1] = tmp

print(list_rev)
