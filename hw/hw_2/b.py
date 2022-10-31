"""
У каждой статьи указаны авторы (их несколько) и темы (их тоже несколько). Определите самую частую пару автор-тема.
Если несколько пар встретились одинаковое число раз, то выведите обе (каждую на новой строчке).

Формат ввода
На каждой строчке сначала указаны фамилии авторов через пробел, потом запятая, потом темы (в одно слово) через пробел.
Например, "Ivanov Petrov, DeepLearning Biology". Последняя строчка ввода – 0.

Формат вывода
Кортеж из фамилии автора и темы. Например, ("Petrov", "DeepLearning").
"""

input_string = input().split(', ')

counts = {}

while input_string != ['0']:
    authors = input_string[0].split()
    topics = input_string[1].split()

    for author in authors:
        for topic in topics:
            if (author, topic) not in counts:
                counts[(author, topic)] = 0
            counts[(author, topic)] += 1

    input_string = input().split(', ')

max_count = max(counts.values())

for pair, count in counts.items():
    if count == max_count:
        print(pair)
