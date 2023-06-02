# Напишите рекурсивную функцию для возведения числа a в степень b. Разрешается использовать только операцию умножения.
# Циклы использовать нельзя
# Примеры/Тесты:
# <function_name>(2,0) -> 1
# <function_name>(2,1) -> 2
# <function_name>(2,3) -> 8
# <function_name>(2,4) -> 16
# <function_name>(2,5) -> 32

def mult(a, b):

    if(b == 0):
        a = 1
        return a
    elif(b == 1):
        return a

    if(b>0):
        return a * mult(a, b-1)


print(mult(2, 0))
print(mult(2, 1))
print(mult(2, 3))
print(mult(2, 4))
print(mult(2, 5))
print(mult(2, 6))
print(mult(2, 7))