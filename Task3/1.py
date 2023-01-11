"""
Создайте функцию, которая возвращает число десятичных знаков, которое имеет число (заданное в виде строки).
Любые нули после десятичной точки отсчитываются в сторону количества десятичных знаков.
"""
def getDecimalPlaces(str_number):
    # делим строку через точку
    list_numbers = str_number.split('.')
    # проверяем была ли точка, если нет выводим 0, если да выводим длинну строки
    if len(list_numbers) == 1:
        return 0
    return len(list_numbers[1])

print(getDecimalPlaces("43.20"))
print(getDecimalPlaces("400"))
print(getDecimalPlaces("3.1"))