"""
Учитывая строку, создайте функцию для обратного обращения. Все буквы в нижнем регистре должны быть прописными,
и наоборот.
"""
def reverseCase(s :str):
    res = ''
    for item in list(s):
        if item.islower():
            res += item.upper()
        else:
            res += item.lower()
    return(res)

print(reverseCase("Happy Birthday"))
print(reverseCase("MANY THANKS"))
print(reverseCase("sPoNtAnEoUs"))
