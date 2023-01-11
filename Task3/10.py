"""
Напишите функцию, которая выбирает все слова, имеющие все те же гласные (в любом порядке и / или количестве), что и
первое слово, включая первое слово.
"""
def sameVowelGroup(lst:list):
 vow = [i for i in lst[0] if i in 'aeiouy'] #в первом цикле ищет все гласные буквы в первом слове
 return [i for i in lst if all(j in i for j in vow)] #возвращает все слова которые совпадают с первым словом

print(sameVowelGroup(["toe", "ocelot", "maniac"]))
print(sameVowelGroup(["many", "carriage", "emit", "apricot", "animal"]))
print(sameVowelGroup(["hoops", "chuff", "bot", "bottom"]))
