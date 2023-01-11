"""
Бесси работает над сочинением для своего класса писателей. Поскольку ее почерк довольно плох, она решает напечатать
эссе с помощью текстового процессора. Эссе содержит N слов (1≤N≤100), разделенных пробелами. Каждое слово имеет длину
от 1 до 15 символов включительно и состоит только из прописных или строчных букв. Согласно инструкции к заданию, эссе
должно быть отформатировано очень специфическим образом: каждая строка должна содержать не более K (1≤K≤80) символов,
не считая пробелов. К счастью, текстовый процессор Бесси может справиться с этим требованием, используя следующую
стратегию:
– Если Бесси набирает Слово, и это слово может поместиться в текущей строке, поместите его в эту строку. В противном
случае поместите слово на следующую строку и продолжайте добавлять к этой строке. Конечно, последовательные слова в
одной строке все равно должны быть разделены одним пробелом. В конце любой строки не должно быть места.
–	К сожалению, текстовый процессор Бесси только что сломался. Пожалуйста, помогите ей правильно оформить свое эссе!

"""
def len_list_with_str(listik: list): #функция которая считает количество символов в заданном списке
    summa = 0
    for i in listik:
        summa += len(i)
    return summa


def essay_constructor(n: int, k: int, essay: str):
    list_with_word = essay.split(' ') #разбивает строку на пробелы
    empty_list = [] #создаем переменную в которой будем хранить результат кратковременный
    for word_number in range(n):
        empty_list.append(list_with_word[word_number]) #в конец строки ставим пробел
        if len_list_with_str(empty_list) < k: #если длина строки больше заданного числа, условие далее не проверяется
            continue
        elif len_list_with_str(empty_list) == k: #сравнивает количество, перечает совпаление
            print(*empty_list)
            empty_list.clear() #после того как напечатал, очищаешь и прокручиваем занного
            continue
        print(*empty_list[:-1]) #делаем срез строки и выводим результат без последнего
        del empty_list[:-1] #удаляет элемент по срезу

    print(*empty_list)

print(essay_constructor(10, 7, "hello my name is Bessie and this is my essay"))