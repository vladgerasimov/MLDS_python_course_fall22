"""
Одно из правил жизни Павла Дурова связано с покупками. Он записывает абсолютно всё, что покупает на бумажку
через запятую. Каждую новую покупку он начинает с новой строки. В день рождения Павлу становится интересно,
какие продукты он покупал вместе чаще всего.

Формат ввода
Строчка за строчкой вводятся чеки с записями. Продукты в чеках перечислены через запятую.

Формат вывода
Выведите названия продуктов, которые покупались вместе чаще всего через запятую. Названия отсортируйте
в лексикографическом порядке. Если таких пар несколько, выведите ту, первый элементы которой меньше
в лексикографическом порядке.

Например:

Среди пар ((b,c), 10), ((a,d),10) надо вывести вторую, тк a < b

Среди пар ((a,c), 10), ((a,d),10) надо вывести первую, тк c < d
"""

with open('input.txt') as f:
    bills = f.readlines()

counts = {}

for bill in bills:
    bill = set(bill.strip().split(','))
    for product_first in bill:
        for product_second in bill:
            if product_first != product_second:
                pair = tuple(sorted((product_first, product_second)))
                if pair not in counts:
                    counts[pair] = 0
                counts[pair] += 1

max_count = max(counts.values())
result = sorted(filter(lambda x: x[1] == max_count, counts.items()),
                key=lambda x: (x[0][0], x[0][1]))

print(','.join(result[0][0]))
