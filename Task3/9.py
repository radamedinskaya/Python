"""
Создайте функцию, которая принимает имя шахматной фигуры, ее положение и целевую позицию. Функция должна возвращать
True, если фигура может двигаться к цели, и False, если она не может этого сделать.
Возможные входные данные - "пешка", "конь", "слон", "Ладья", "Ферзь" и " король".
"""
def canmove(figure, start, end ):
    xS = ord(start[0]) - 96
    yS = int(start[1])
    xE = ord(end[0]) - 96
    yE = int(end[1])
    if figure == "pawn": #пешка
        if yS == yE-1 and xS == yS:
            return True
    if figure == "rook": #ладья
        if yS == yE or xS == yS:
            return True
    if figure == "bishop": #слон
        if yS - yE == xS - xE or yS - yE == (xS - xE) * -1:
            return True
    if figure == "queen": #королева
        if yS - yE == xS - yS or yS - yE == (xS - xE) * -1 or yS == yE or xS == yS:
            return True
    if figure == "king": #король
        if (yS - yE == xS - yS or yS - yE == (xS - xE) * -1 or yS == yE or xS == yS):
            return True
    if figure == "knight": #ферзь
        if (xS + 2 == xE and yS + 1 == yE) or (xS + 2 == xE and yS - 1 == yE) or (xS - 2 == xE and yS + 1 == yE) or (xS - 2 == xE and yS - 1 == yE) or(xS + 1 == xE and yS + 2 == yE) or (xS + 1 == xE and yS - 2 == yE) or (xS - 1 == xE and yS + 2 == yE) or (xS - 1 == xE and yS - 2 == yE):
            return True
    return False

print(canmove("Rook", "A8", "H8"))
print(canmove("Bishop", "A7", "G1"))
print(canmove("Queen", "C4", "D6"))

