#  Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает
#  в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца, т.е. функцию двух аргументов.
#  Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
#  Нумерация строк и столбцов идет с единицы.
#
# Примеры/Тесты:
# print_operation_table(lambda x,y: x**y,4,4)
# 1   1   1   1
# 2   4   8  16
# 3   9  27  81
# 4  16  64 256
#
# print_operation_table(lambda x,y: x*y)
# 1   2   3   4   5   6
# 2   4   6   8  10  12
# 3   6   9  12  15  18
# 4   8  12  16  20  24
# 5  10  15  20  25  30
# 6  12  18  24  30  36

def printOperationTable(sign, cols, rows):


 for x in range(1, cols+1):
  print(str(x)+' |  ', end=' ')
  for y in range(1, rows+1):
   if(sign == '**'):
    print("{:>3}".format(str(x**y)), end='  ')
   if (sign == '*'):
    print("{:>2}".format(str(x * y)), end='  ')
  print()


operation = input('Введите "*" или "**" операцию: ')
printOperationTable(operation,4,4)