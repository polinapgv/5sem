def division(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('Error: division by zero!')
    else:
        print('The results is', result)
    finally:
        print('See ya next time')
print(division(2, 2), division(2, 0))