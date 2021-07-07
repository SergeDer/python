# Параметры пользователя
def users_profile(**user_params):
    users_profile_list = []
    for param in user_params.values():  # Преобразуем каждый введенный параметр в строку
        users_profile_list.append(str(param))
    return ' '.join(users_profile_list)


print(users_profile(
    name='John',
    surname='Black',
    birthday_year=1990,
    city='San Diego',
    email='john-black@gmail.com',
    phone='+58933453354'))
