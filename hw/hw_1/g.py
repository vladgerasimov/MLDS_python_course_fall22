"""
Пятачок хочет запрограммировать разложение в ряд Маклорена экспоненты, но ему нужна ваша помощь.
Напишите программку, которая считает ряд Маклорена для ЭКСПОНЕНТЫ и на каждом шагу выдает значение ошибки
вычисления с помощью ряда Маклорена (модуль разницы значений полученных с помощью ряда Маклорена и с помощью
функции из пакета math)

Формат ввода
На вход программа получает два числа, каждое на своей строчке: x - вещественное число, удовлетворяющее условиям ряда,
N - натуральное число, количество итераций, которое Павел готов ждать.

Формат вывода
На выходе N чисел с точностью 10 знаков после запятой, каждое число выводится на новой строчке.
Для вывода используйте код: print("%.10f"%error)
"""

from math import factorial, exp

x = float(input())
n = int(input())
result = 0
true_exp = exp(x)

for i in range(n):
    result += x ** i / factorial(i)
    error = abs(result - true_exp)
    print(f"{error:.10f}")
