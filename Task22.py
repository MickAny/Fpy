# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Если таких чисел нет - выдать внятное диагностическое сообщение
# Наборы (списки) чисел можно считать заданными и не вводить с клавиатуры
#
# Примеры/Тесты:
# Input1: 2 4 6 8 10 12 10 8 6 4 2
# Input2: 3 6 9 12 15 18
# Output: 6 12     Обратите внимание: Без скобочек, в одну строку
#
# Input1: 2 4 6 8 10 10 8 6 4 2
# Input2: 3 9 12 15 18
# Output: Повторяющихся чисел нет


list_1 = [2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2]
list_2 = [3, 6, 9, 12, 15, 18]
list_3 = []

# list_1 = [2, 4, 6, 8, 10, 10, 8, 6, 4, 2]
# list_2 = [3, 9, 12, 15, 18]
# list_3 = []

print(list_1)
print(list_2)
for i in list_1:
    for x in list_2:
        if( i == x and i not in list_3):
            list_3.append(i)

if list_3:
 print(*list_3, sep=' ')
else:
    print("Повторяющихся чисел нет!")