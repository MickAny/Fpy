# Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.
# Примеры/Тесты:
# 10 -> 1 2 4 8

limit = int(input('Введите число-ограничитель: '))

def calculation(n):
    tmp = 1
    print(str(tmp)+', ', end='')
    while tmp < n:
        tmp *=2
        if(tmp<n):
         print(str(tmp)+', ', end='')

calculation(limit)