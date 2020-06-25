# Список из элементов различного типа данных
ex_list = [1,
           3.14,
           'Hello',
           True,
           [1, 2],
           (3, 4),
           {'id': 1, 'name': 'Alex'},
           b'Hi',
           bytearray(b'Sir'),
           None
           ]

for i in range(len(ex_list)):
    print(type(ex_list[i]))
