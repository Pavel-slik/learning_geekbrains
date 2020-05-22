def function(a, b):
    if b < 0:
        return 1 / a ** abs(b)
    else: return a ** abs(b)

        # через цикл без использования **
        # res = 1
        # for i in range(abs(b)):
        #     res *= a
        # if b >= 0:
        #     return res
        # else: return 1 / res

print('c = a^b = ', function(int(input('Введите число a: ')), int(input('Введите число b: '))))