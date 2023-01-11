"""
Создайте функцию, которая возвращает true, если две строки имеют один и тот же буквенный шаблон, и false в противном
случае.
"""

def sameLetterPattern(a, b):
    if len(a) != len(b): #сразу проверяем по длине строк, возвращает False если строки не совпадают
        return False
    x, y = ord(a[0]), ord(b[0]) #функция ord возвращает значение первого элемента из таблицы символов UNICODE(запоминаем первые символы)
    pos = 1
    while pos < len(a): #запускаем цикл, в котором будем проходить по символьно
        dx, dy = x - ord(a[pos]), y - ord(b[pos]) #запоминаем разницу между первым и вторым элементов
        if dx != dy: #если разница отличается возвращает False
            return False
        x, y = ord(a[pos]), ord(b[pos]) #Если разница равна, переходим к следующему элементу
        pos += 1
    return True #возвращает True если соответстует шаблону


print(sameLetterPattern("ABAB", "CDCD"))
print(sameLetterPattern("ABCBA", "BCDCB"))
print(sameLetterPattern("FFGG", "CDCD"))
print(sameLetterPattern("FFFF", "ABCD"))