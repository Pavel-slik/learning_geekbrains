def function(a, b, c):
    sequence = [a, b, c]
    amount = []
    max_1 = max(sequence)
    amount.append(max_1)
    sequence.remove(max_1)
    max_2 = max(sequence)
    amount.append(max_2)
    print(sum(amount))
print('Введите три аргумента: ', function(int(input('1-е число: ')), int(input('2-е число: ')), int(input('3-е число: '))))