# Все слова строки с заглавной буквы (способ, где функция делает заглавной только первую букву первого слова строки)
def int_func(word):
    return word.capitalize()


words_string = 'на улице лето и очень красиво'

words_list = words_string.split(' ')
words_list_new = []
for el in words_list:
    words_list_new.append(int_func(el))

print(' '.join(words_list_new))
