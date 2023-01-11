"""
Напишите функцию, которая преобразует строку в звездную стенографию. Если символ повторяется n раз, преобразуйте его
в символ*n.
"""

def toStarShorthand(task: str):
    element = task[0] #запоминаем 1 элемент
    count = 0 #число в которое запоминаем количество дублей
    res = '' #вывод результата
    for item in task:
        if element == item: #если первоначальный элементы равен 1 позиции, запоминаем количество
            count += 1
        else:
            res += element if count == 1 else element + '*' + str(count) #если каунт равен 1 выводил значение, обнуляем значения
            #иначе выводим звездочки
            element = item
            count = 1
    return (res)

print(toStarShorthand("abbccc"))
print(toStarShorthand("77777geff"))
print(toStarShorthand("abc"))