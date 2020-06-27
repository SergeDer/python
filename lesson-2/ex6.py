# Аналитика словаря
goods = [
    (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
    (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
    (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
]

keys_list = list(goods[0][1])  # Список ключей
full_list = []  # Двумерный список - будущие списки значений для финального словаря
final_dict = {}  # Требуемая структура (словарь)

for j in range(len(keys_list)):
    items_list = []  # Список значений с одинаковым ключем
    for i in range(len(goods)):
        items_list.append(goods[i][1].get(keys_list[j]))
    items_list = list(set(items_list))  # Уберем одинаковые элементы
    full_list.append(items_list)

for i in range(len(keys_list)):
    final_dict.update({keys_list[i]: full_list[i]})

print(final_dict)
