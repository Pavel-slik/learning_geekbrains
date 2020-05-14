a = [7, 5, 3, 3, 2]
num = int(input('введите число: '))
quan = a.count(num)
for i in a:
    if quan > 0:
        a.insert(a.index(num) + quan, num)
        break
    else:
        if num > i:
            a.insert(a.index(i), num)
            break
        elif num < a[len(a) - 1]:
            a.append(num)
print(a)