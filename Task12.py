# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
# Примеры/Тесты:
# 4 4 -> 2 2
# 5 6 -> 2 3

sum = int(input('Введите сумму чисел: '))
mult = int(input('Введите произведение чисел: '))

def calculate(x, y):
    for i in range(1, x+y):
        for a in range(1, x+y):
            if(i+a==x and i*a==y):
                return(i, a)


print(calculate(sum, mult))