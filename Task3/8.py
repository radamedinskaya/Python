"""
Пришло время отправлять и получать секретные сообщения.
Создайте две функции, которые принимают строку и массив и возвращают закодированное или декодированное сообщение.
Первая буква строки или первый элемент массива представляет собой символьный код этой буквы. Следующие элементы-это
различия между символами: например, A +3 --> C или z -1 --> y.

"""
def encrypt(s):
    res = [ord(s[0])]
    for i in range(1, len(s)):
        res.append(ord(s[i]) - ord(s[i - 1]))
    print(res)

def decrypt(a):
    a = [int(i) for i in a]
    res = chr(a[0])
    for i in range(1, len(a)):
        a[i] += a[i - 1]
    res += chr(a[i])
    print(res)


encrypt("Hello")  # ➞ [72, 29, 7, 0, 3]
decrypt([72, 33, -73, 84, -12, -3, 13, -13, -68])  # ➞ "Hi there!"
encrypt("Sunshine")  # ➞ [83, 34, -7, 5, -11, 1, 5, -9]