# Возведение в степень без оператора **
def my_func(x, y):
    power = 1
    if (isinstance(x, int) or isinstance(x, float)) and isinstance(y, int) and x > 0 and y < 0:
        for i in range(abs(y)):
            power = power * x
        return 1/power
    else:
        return


print(my_func(122.23, -4))
