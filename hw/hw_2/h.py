"""
Вам даны две строки, состоящие из слов, точек и запятых. Проверьте, состоят ли эти предложения из одинакового
набора слов (в том числе, по количеству) без учета порядка и регистра.

Формат ввода
Две строки - два предложения

Формат вывода
YES/NO
"""

words_1 = input().strip().split()
words_2 = input().strip().split()


def get_counts(words):
    counts = {}
    for word in words:
        word = word.lower().strip(',.')
        if word not in counts:
            counts[word] = 0
        counts[word] += 1

    return counts


counts_1 = get_counts(words_1)
counts_2 = get_counts(words_2)

if counts_1 == counts_2:
    print('YES')
else:
    print('NO')
