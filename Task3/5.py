"""
Напишите функцию, которая группирует строку в кластер скобок. Каждый кластер должен быть сбалансирован.
"""
def split(str):
    countO = 0
    countC = 0
    flag = 0
    arr = []
    for i in range(len(str)):
        if str[i] == '(':#проверяет последовательно каждый элемент на скобку, считает повтор
            countO += 1
        else:
            countC += 1 #иначе начинает записывать сколько других скобок
        if countO == countC: #проверяем условие если количество совпадает найденных скобок
            arr.append(str[flag:i+1]) #в конец списка делим на кластеры
            flag = i+1
            countO = 0 #обнуляем значение
            countC = 0
    return arr #возвращаем значение
print(split("()()()"))
print(split("((()))"))
print(split("((()))(())()()(()())"))
print(split("((())())(()(()()))"))
