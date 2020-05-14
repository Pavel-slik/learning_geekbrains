a = [str(i) for i in input('введи слова через пробел').split()]
for i in range(0, len(a)):
    print(i + 1, a[i][0:10])