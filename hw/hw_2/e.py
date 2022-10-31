"""
Напишите функцию, вычисляющую длину отрезка по координатам его концов. С помощью этой функции напишите программу,
вычисляющую периметр выпуклого многоугольника по координатам вершин.

Формат ввода
На вход программе подается 2 * n целых чисел — координат x1, y1, x2, y2, ... вершин
выпуклого многоугольника. Считайте, что последняя вершина соединяется с первой. Все числа по модулю
не превосходят 30000.

Формат вывода
Выведите значение периметра этого многоугольника с точностью до 6 знаков после десятичной точки.
"""
from sys import stdin


def get_len(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


first_x = int(stdin.readline())
first_y = int(stdin.readline())

prev_x, prev_y = first_x, first_y

result = 0

points = stdin.readlines()

i = 0
for _ in range(len(points) // 2):
    x = int(points[i])
    y = int(points[i + 1])
    result += get_len(prev_x, prev_y, x, y)
    prev_x, prev_y = x, y
    i += 2

result += get_len(prev_x, prev_y, first_x, first_y)

print(f'{result:.6f}')
