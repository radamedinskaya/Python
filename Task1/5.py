"""
Создайте функцию, которая возвращает количество полных стен, которые я могу покрасить,
прежде чем мне нужно будет отправиться в магазины, чтобы купить еще.
Пример:
howManyWalls(54, 1, 43) ➞ 1
howManyWalls(46, 5, 4) ➞ 2
"""

def howManyWalls(n,w,h): #функция poln
    pol = int(n//(w*h))
    print(pol)

n = int(input("input n")) #вводим количество квадратных метров
w = int(input("input w")) #вводим ширину стены
h = int(input("input h")) #вводим высоту стены

howManyWalls(n,w,h) #передаем значения