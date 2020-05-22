from itertools import count
from itertools import cycle

def count_func(start_num, stop_num):
    for el in count(start_num):
        if el > stop_num:
            break
        else:
            print(el)
def cycle_func(my_list, iteration):
    i = 0
    iter = cycle(my_list)
    while i < iteration:
        print(next(iter))
        i += 1
count_func(start_num = int(input('Введите начальное значение: ')), stop_num = int(input('Введите конечное значение: ')))
cycle_func(my_list=[1, 2], iteration=int(input('Введите итерацию: ')))