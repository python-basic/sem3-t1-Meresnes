"""
Задача 2.3:
Перепишите генератор списка,
позволяющий получить модуль числа, через лямбда-функцию.

Выполнил: Петров Роман
ИВТ 2 курс группа 1.1
"""
lambd = lambda n: abs(n)
a = [lambd(i) for i in range(-10,0)]
print(a)   