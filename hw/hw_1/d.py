"""
Вера в совершенстве отточила навык придумывания новых паролей и теперь объясняет своей подруге Ане какие пароли
можно использовать, а какие нет. Помогите ей написать программку для оценки силы пароля Ани.

Правила простые: сильным может считаться только тот пароль, в котором есть буквы в разных регистрах и цифры.
Пароли длины менее 8, пароли состоящие менее чем из 4 уникальных символов, и пароли,
в которых встречается слово anna (в любом регистре букв) считаются слабыми.

Ваша задача — реализовать код, который на вход принимает пароль, а на выход возвращает строчку weak или strong.

Формат ввода
Вводится одна строка

Формат вывода
Выведите ответ на задачу - либо weak либо strong в формате строки
"""

password = input()

len_is_ok = len(password) >= 8
uniq_symbols = set(password)
uniq_symbols_is_ok = len(uniq_symbols) >= 4
different_registers_is_ok = password != password.lower() and password != password.upper()
anna_is_ok = 'anna' not in password.lower()

digits_is_ok = False
for symbol in uniq_symbols:
    if symbol.isdigit():
        digits_is_ok = True
        break

if len_is_ok and uniq_symbols_is_ok and different_registers_is_ok and anna_is_ok and digits_is_ok:
    print('strong')
else:
    print('weak')
