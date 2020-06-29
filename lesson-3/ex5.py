# Сумма чисел-элементов строки
nums_sum = 0
end_flag = 0


def numbers_sum(nums_str):
    """
    Функция, суммирующая числа в строке. Числа в строке отделены пробелами.
    Если один из элементов строки не число, то этот элемент будет проигнорирован
    Если в строке вместо числа '$', то числа, идущие после, не прибавляются к сумме, а функция завершает работу
    :param nums_str: строка чисел, разделенных пробелом
    :return: nums_sum - сумма чисел введенной строки;
             end_flag - флаг остановки, равнен "1", если в строке вместо числа '$'
             ('$' должен быть отделен пробелами)
    """
    nums_list = nums_str.split(' ')
    global nums_sum, end_flag
    for el in nums_list:
        if el != '$':
            try:
                nums_sum += int(el)
            except ValueError:
                continue
        else:
            end_flag = 1
            break
    return nums_sum, end_flag


while end_flag == 0:
    numbers_str = input('Введите строку символов, разделенных пробелом\n'
                        'Если вместо числа вы введете знак доллара ($), программа будет завершена: ')
    numbers_sum(numbers_str)
    print(nums_sum)
