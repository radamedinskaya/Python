"""
Напишите функцию, которая находит слово "бомба" в данной строке. Ответьте "ПРИГНИСЬ!", если найдешь, в противном случае
: "Расслабься, бомбы нет".

"""

def toBOOM(bomb):
    if 'bomb' in bomb.lower(): #проверяем по условию есть ли бомб в строке, используем метод lower
        return("DUCK")
    else:
        return("Relax, there's no bomb")

print(toBOOM("There is a bomb."))
print(toBOOM("Hey, did you think there is a BOMB?"))
print(toBOOM("This goes boom!!!"))
