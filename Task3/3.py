"""
Если задано целое число, создайте функцию, которая возвращает следующее простое число.
Если число простое, верните само число.
"""

def isPrimeNumber(number: int):
    """"
    метод для определения простого числа
    если True, то переданное число простое
    если False, то нет
    перебираем числа от 2 до number // 2.
    И если остаток от деления равен 0, то значит имеется больше двух делителей, значит число не является простым
    """

    end = number // 2
    for item in range(2, end):
        if number % item == 0:
            return False
    return True


def getNextPrime(number: int):
    if isPrimeNumber(number):
        return(f'This number {number} is prime')
    while not isPrimeNumber(number):
        number += 1
    else:
        return(f'Next prime number is {number}')

print(getNextPrime(12))
print(getNextPrime(24))
print(getNextPrime(11))