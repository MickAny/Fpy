# Требуется найти в списке целых чисел самый близкий по величине элемент к заданному числу X.
# Пользователь вводит это число с клавиатуры, список можно считать заданным.
# Введенное число не обязательно содержится в списке.
# Если в списке несколько чисел "равноблизких" к заданному числу X, то выводим первое встретившееся.
# Примеры/Тесты:
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
# Output: 2
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9
# Output: 10
# (*) Усложнение. Если в списке несколько чисел "равноблизких" к заданному числу X, выводим
# все числа в отсортированном виде (по возрастанию)

size = int(input('Введите количество элементов списка: '))
tempList = input("Введите через пробел элементы списка: ").split()  # ввод через данных через пробел
mainList = list(map(int, tempList))  # map меняет тип данных списка
figureToCompare = int(input('Введите число, с которым необходимо сравнивать элементы списка: '))

min = abs(figureToCompare - mainList[0])
temp1 = 0
temp2 = 0
temp3 = 0
for i in range(1, size):
    temp1 = abs(figureToCompare - mainList[i])
    if temp1 < min:
        min = temp1
        temp2 = mainList[i]

#(*)
extraList = []

for i in range(size):
    temp3 = abs(figureToCompare - mainList[i])
    if temp3 == min:
        extraList.append(int(mainList[i]))

extraList.sort()
print(extraList)