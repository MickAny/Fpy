# Задача 2: Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
import math

figure = int(input('Введите трехзначное число: '))

print(str(figure)+' ->',figure%10 + math.floor(figure/10%10) + math.floor(figure/100) if figure>99 and figure<1000 else 'Вы ввели не трехзначное число!')

