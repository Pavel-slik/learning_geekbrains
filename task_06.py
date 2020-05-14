quan = int(input('Введите количество товаров: '))
n = 1

roster = []

while n <= quan:
    form = []
    form = dict({'название': input('Введите название: '), 'цена': input('Введите цену: '),
                 'количество': input('Введите количество '), 'eд': input('Введите единицу измерения: ')})
    roster.append((n, form))
    n += 1
print(roster)
struct = {}
for roster in roster:
    for form.get('название'), form.get('цена') in roster[1].items():
        if form.get('название') in struct:
            struct[form.get('название')].append(form.get('цена'))
        else:
         struct[form.get('название')] = [form.get('цена')]
print(struct)

# struct = dict({'название': form.get('название'), 'цена': form.get('цена'), 'количество': form.get('количество'),
#          'ед': form.get('ед')})
#
#
# print(struct)