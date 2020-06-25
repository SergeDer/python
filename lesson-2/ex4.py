# Разбиение введенной строки на слова
str1 = input('Введите строку, разделяя слова пробелами: ').split()
for i, el in enumerate(str1):
    print(i + 1, str(str1[i])[:20])
