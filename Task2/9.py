"""
Создайте функцию, которая будет рекурсивно подсчитывать количество цифр числа. Преобразование числа в строку не
допускается, поэтому подход является рекурсивным.
"""
def digitsCount(n :int):
    return 1 + digitsCount(n // 10) if n > 10 else 1 #считает итерации пока есть целая часть от деления

print(digitsCount(4666))
print(digitsCount(544))
print(digitsCount(121317))
print(digitsCount(0))
print(digitsCount(12345))

