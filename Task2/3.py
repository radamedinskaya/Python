"""
Создайте функцию, которая принимает число в качестве входных данных и возвращает true, если сумма его цифр имеет ту
же четность, что и все число. В противном случае верните false.
"""
def slogenie(s: int):#создаем функцию для нахождения суммы чисел числа
    sum = 0
    while (s != 0):
        sum = sum + s % 10
        s = s // 10
    return(sum)

def parityAnalysis(s: int): #функция сравнивает остаток от деления, он должен быть в обоих случаях либо четный, либо не четный
    if (s % 2 == 0 and slogenie(s) % 2 == 0) or (s % 2 != 0 and slogenie(s) % 2 != 0):
        return (True)
    else:
        return (False)

print(parityAnalysis(243))
print(parityAnalysis(12))
print(parityAnalysis(3))