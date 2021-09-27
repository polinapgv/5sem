def division(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('Error: division by zero!')
    else:
        print('The results is', result)
    finally:
        print('See ya next time')


def summ(x, y):
    return x + y


def power(x, y):
    return x ** y


print(summ(2, power(2, division(2, 0))))