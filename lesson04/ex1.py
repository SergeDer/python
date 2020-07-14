# Расчет заработной платы с передачей параметров
import sys

try:
    file, hours, rate, premium = sys.argv
except ValueError:
    print('Проверьте параметры!')
    exit()


def salary_calc(hours, rate, premium):
    try:
        return hours * rate + premium
    except TypeError:
        return None


print(salary_calc(float(hours), float(rate), float(premium)))
