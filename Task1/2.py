"""
Коля, Федя и Толя спорят кто из них должен стоять первый на построении на уроке физкультуры.
Напишите программу, упорядочивающую учеников по росту. На вход подаются три строки с ростом,
на выход – три упорядоченные строки.
Пример
Ввод: Вывод:
132   144
144   132
126   126
"""

rost = input("Input rost:").split() # Вводим значение и с помощью split разбиваем на элементы
rost.sort(reverse=True) #сортируем по убыванию с помощью sort
print(rost) #вывод