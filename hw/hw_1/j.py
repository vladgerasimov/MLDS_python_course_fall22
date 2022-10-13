"""
Маша отправилась в горное путешествие. В каждый момент ее пути высота меняется. Высота задается натуральным числом.
Маше интересно: какое минимальное расстояние между горными вершинами на ее пути. Маша заканчивает свое
путешествие у моря, поэтому высота там всегда равна 0. Вершиной называется место, которое больше своих
соседей по высоте.

Если на пути меньше чем 2 вершины, то выведите 0. Начало и конец пути вершинами не считаются.

Формат ввода
Вводится последовательность целых чисел, оканчивающаяся числом 0 (само число 0 в последовательность не входит,
а служит как признак ее окончания).

Формат вывода
Выведите ответ на задачу.
"""


heights = []
height = None
while height != 0:
    height = int(input())
    heights.append(height)

min_distance = float('inf')
prev_peak_idx = None

for idx, height in enumerate(heights[1:-2], 1):
    if heights[idx - 1] < height > heights[idx + 1]:
        is_peak = 1
        peak_idx = idx
        if prev_peak_idx:
            distance = idx - prev_peak_idx
            if distance < min_distance:
                min_distance = distance
        prev_peak_idx = idx
    else:
        is_peak = 0
if isinstance(min_distance, int):
    print(min_distance)
else:
    print(0)
