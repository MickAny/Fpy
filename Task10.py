#  На столе лежат монетки. Некоторые из них лежат вверх решкой, а некоторые – гербом.
#  Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх
#  одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть. Количество монет и их
#  положение (0 или 1) пользователь вводит с клавиатуры.
# Примеры/Тесты:
# Введите кол-во монет>? 5
# Положение монеты 0: 0 или 1>? 1
# 1 0 1 1 0
# Кол-во монет, чтобы перевернуть: 2

coinsNumber = int(input('Введите количество монеток: '))

list_1 = []
x = 0
y = 0

for i in range(coinsNumber):
  x=int(input('Введите положение монетки(0/1): '))
  list_1.append(x)
print(list_1)

for i in range(len(list_1)):
  if(list_1[i]==0):
    list_1[i]=1
    y+=1
print('Кол-во монет, чтобы перевернуть: ' + str(y))