# Напишите программу, генерирующую элементы арифметической прогрессии
# Программа принимает от пользователя три числа :
# Первый элемент прогрессии, Разность (шаг) и Количество элементов
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Напишите функцию
# - Аргументы: три указанных параметра
# - Возвращает: список элементов арифмитической прогрессии.
# Примеры/Тесты:
# Ввод: 7 2 5
# Вывод: [7 9 11 13 15]
# Ввод: 2 3 12
# Вывод: [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
# (*) Усложнение. Для формирования списка внутри функции используйте Comprehension
# (**) Усложнение. Присвоение значений переменным a1,d,n запишите, используя только один input,
# в одну строку, вам понадобится распаковка и Comprehension или map

print("Введите параметры арифметической прогрессии в порядке:\n 1.Начало прогрессии\n 2.Шаг\n 3.Количество повторений")
options = input().split()
mainList = list(map(int, options))

def arProgression(list):
    arg1 = list[0]
    arg2 = list[1]
    arg3 = list[2] - 1
    print(arg1, end=' ')
    for i in range(arg3):
        print(str(arg1 + arg2), end=' ')
        arg1 += arg2

arProgression(mainList)

minNum = int

