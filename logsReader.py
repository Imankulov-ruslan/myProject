# Удаление из файла всех символов, указанных в списке elems
from tkinter import messagebox
def del_noWordsElems(filename):
    with open(filename, 'r', encoding='utf-8') as readFile:
        # считываем файл в одну строку
        text = readFile.read()
        # список элементов для замены
        elems = ('!',',','.','?','\n','-','+','=','\t','"','\'',']','[',':','*')
        for i in elems:
          # замена всех элементов в строке на пробел
            text = text.replace(i, ' ')
    return text

# сортировка списка и нахождение самого длинного элемента списка
def word_to_list(text):
    # создание списка по разделителю space
    words = text.split()
    # сортировка списка
    words.sort()
    # находим самый длинный элемент списка
    lenght = 1
    for i in words:
     if lenght < len(i):
        lenght = len(i)
    # возвращаем кортеж со списком и длиной
    return words, lenght

# создание словаря
def dict_from_list(list):
    # создаем пустой словарь
    wordsDict = dict()
    # перебираем элементы нашего списка
    for word in list:
        # Элемент с ключом Word = 0 + 1, если не найден в словаре
        # или "значения" + 1, то есть пока словарь пустой всегда по ключу записывается значение 1
        # как только ключ повторится  wordsDict.get(word, 0) вернет 1 и прибавит 1
        # если повторится еще раз то уже к 2 прибавит 1, получается словарь-счетчик
        wordsDict[word] = wordsDict.get(word, 0) + 1
    return wordsDict

def main():
    filename = r'C:\Users\rusel\PycharmProjects\My project_v1\programmLogs\logs.txt'
    # множественное присовеное элементов кортежа (return word_to_list)
    # в функции word_to_list аргументом является другая функция del_noWordsElems в нее передается аргумент
    # filename с расположением нашего файла, в результате функции получается строка и она передается
    # как аргумент в функцию word_to_list, а та уже вернет кортеж, где первый элемент - это отсортированный
    # список, а второй - длина самого длинного элемента списка
    words,lenght = word_to_list(del_noWordsElems(filename))
    # создание спика из полученного списка
    wordsDict = dict_from_list(words)
    messagebox.showinfo('Анализ логов','Логи проекта успешно считаны!')
    messagebox.showinfo('Анализ логов',f'Кол-во слов: {len(words)}\nКол-во уникальных слов: {len(wordsDict)}')
    filename1 = r'C:\Users\rusel\PycharmProjects\My project_v1\programmLogs\logs_analyse.txt'
    with open(filename1, 'a',encoding='utf-8') as file:
        file.write('Список и кол-во всех слов в логах:\n')
        for word in wordsDict:
            file.write(f"{word} - {wordsDict[word]}")
            file.write('\n')
