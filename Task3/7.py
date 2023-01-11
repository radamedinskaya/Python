"""
Создайте функцию, которая возвращает True, если две строки рифмуются, и False в противном случае.
Для целей этого упражнения две строки рифмуются, если последнее слово из каждого предложения содержит одни и те же
гласные.
"""

def get_low_vow(word):  # функция с помощью которой мы переведем строку в нижний регистр и отфильтруем на наличие повторящихся гласных
    word = word.lower()
    return list(filter(lambda x: x in 'aeiouy', word))  # фильтруем список с помощью фильтра по условию
def does_rhyme(L, R):
    L = L.split()[-1]  # возьмем последние слово в списке
    R = R.split()[-1]
    return get_low_vow(L) == get_low_vow(R) #возвращаем значение True/False сравнивая полученые значения с помощью функции

print(does_rhyme("Sam I am!", "Green eggs and ham."))
print(does_rhyme("Sam I am!", "Green eggs and HAM."))
print(does_rhyme("You are off to the races", "a splendid day."))
print(does_rhyme("and frequently do?", "you gotta move."))