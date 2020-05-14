num = [str(i) for i in input('Введите элементы списка через пробел: ').split()]
for i in range(1, len(num), 2):
    num[i - 1], num[i] = num[i], num[i - 1]
print(' '.join([str(i) for i in num]))