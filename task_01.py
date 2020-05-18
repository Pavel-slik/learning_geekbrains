def function(a, b):
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        return 'Введенное число не может быть равно 0'
    except ValueError:
        return 'Введенный элемент не число'
print('c = a / b = ', function(int(input('Введите число a: ')), int(input('Введите число b: '))))
