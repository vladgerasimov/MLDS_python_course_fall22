"""
На экзамен по машинному обучению пришло N человек. Определите, из какой группы пришло больше всего студентов,
которые сдали экзамен на отлично (>=8).

Формат ввода
Информация о результатах экзамена записана в файле, в котором каждая из строк имеет вид: фамилия имя группа балл

Фамилия и имя являются строками, группа - целое число от 1 до 1000, балл - целое число от 0 до 10.

Сначала вводится число n - количество студентов, далее n строк с информацией о них.

Формат вывода
Если наиболее часто встречающаяся группа одна - выведите ее номер. Если таких групп оказалось
несколько - выведите их номера через пробел в порядке возрастания.
"""

n = int(input())

counts = {}

for _ in range(n):
    surname, name, group, score = input().strip().split()
    score = int(score)

    if score >= 8:
        if group not in counts:
            counts[group] = 0
        counts[group] += 1

max_count = max(counts.values())
result = sorted(filter(lambda x: x[1] == max_count, counts.items()),
                key=lambda x: x[0])

print(' '.join([i[0] for i in result]))
