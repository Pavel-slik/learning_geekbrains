def total():
    result = 0
    e = False
    while e == False:
        number = input('Введите число или Q для выхода - ').split()
        result_1 = 0
        for i in range(len(number)):
            if number[i] == 'q' or number[i] == 'Q':
                e = True
                break
            else:
                result_1 = result_1 + int(number[i])
        result = result + result_1
        print(f'Текущая сумма равна {result}')
    print(f'Результирующая сумма равна {result}')
total()