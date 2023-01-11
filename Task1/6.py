"""
Создайте функцию, которая принимает три аргумента prob, prize, pay и возвращает true,
если prob * prize > pay; в противном случае возвращает false.
profitableGamble(0.2, 50, 9) ➞ true
profitableGamble(0.9, 1, 2) ➞ false
profitableGamble(0.9, 3, 2) ➞ true

"""
def profitableGamble(p,pr,pa): #функция которая должна возвращать значения true false согласно условию задачи
    if pr*p>pa:
        return True
    else:
        return False
#вводим значения
prod = float(input("input prod"))
prize = float(input("input prize"))
pay = float(input("input pay"))
print(profitableGamble(prod,prize,pay)) #вызов и вывод функции
