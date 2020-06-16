# Вывод секунд в формате чч:мм:сс
seconds_source = int(input('Введите время в секундах: '))

hours = seconds_source // 3600
minutes = (seconds_source % 3600) // 60
seconds = (seconds_source % 3600) % 60

print(f'{hours}:{minutes}:{seconds}')
