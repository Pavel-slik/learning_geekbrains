my_list = ['Имя\n', 'Фамилия\n', 'Отчество\n']
with open('test_2.txt', 'w+') as file_obj:
    file_obj.writelines(my_list)
with open('test_2.txt') as file_obj:
    lines = 0
    words = 0
    for line in file_obj:
        lines += line.count('\n')
        words = len(line)-1
        print(f'{words} слов в строке')
    print(f'Колличество строк {lines}')