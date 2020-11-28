
def main():
    global mainName, name1, name2, name3, name4, name5, name6
    mainName = '"Работа со словарями"'
    name1 = '"Добавление элементов в словарь"'
    name2 = '"Удаление элемента из словаря"'
    name3 = '"Поменять 2 элемента словаря местами"'
    name4 = '"Сложить словарь с другим словарем"'
    name5 = '"Удалить повторяющиеся значения словаря"'
    name6 = '"Очистить словарь"'
    print('Для начала работы создайте ваш словарь')
    new_list_for_dict(True)
    newDict()
    number_input()

# печать меню с доступными операциями
def print_dict_menu():
    print(f'''
*****\t{mainName}\t*****
Выберите что нужно сделать с вашим словарем:
1 - {name1}
2 - {name2}
3 - {name3}
4 - {name4}
5 - {name5}
6 - {name6}
0 - Выйти из программы {mainName} в основное меню
Введите цифру от 0 до 6: ''', end='')

# функция по запуску выбранной операции
def number_input():
    while True:
        print_dict_menu()
        number = input()
        if number == '1':
            save_logs(f'Ползователь выбрал операцию: {name1}')
            add_to_dict(True)
        elif number == '2':
            save_logs(f'Ползователь выбрал операцию: {name2}')
            del_from_dict(True)
        elif number == '3':
            save_logs(f'Ползователь выбрал операцию: {name3}')
            swap_2_elem_in_dict(True)
        elif number == '4':
            save_logs(f'Ползователь выбрал операцию: {name4}')
            sum_dict(True)
        elif number == '5':
            save_logs(f'Ползователь выбрал операцию: {name5}')
            make_dict_unique(True)
        elif number == '6':
            save_logs(f'Ползователь выбрал операцию: {name6}')
            clearDict()
        elif number == '0':
            save_logs(f'Ползователь ввел 0 и завершил программу: {mainName}')
            print(f'Программа {mainName} завершена')
            break
        else:
            save_logs(f'Ползователь неверно ввел данные')
            print('Введите только числа от 0 до 6')
            continue

# создание списка формата [[],[],[]] для преобразования в словарь
def new_list_for_dict(repeat):
    while repeat:
        global newList
        while True:
            try:
                quantity = int(input('Введите кол-во значений словаря\n'))
                if quantity <= 0: # исключение для того, чтобы словарь не был пустым
                    raise Exception
                # создание пустых вложенных словарей в кол-во равном quantity
                newList = [[] for k in range(quantity)]
                for i in range(len(newList)):
                    newList[i].append(input("Введите ключ\n"))
                    newList[i].append(input("Введите значение\n"))
                break
            except:
                save_logs('Пользователь ввел неверные данные')
                print("Введены неверные данные, повторите операцию")
                continue
        # функция повтора опепрации, выдает True, если введено Y
        repeat = continue_or_break('Создание словаря')

# Создание словаря из списка
def newDict():
    global newDict
    newDict = dict(newList)
    print('Ваш  словарь - ', newDict)
    save_logs(f'Пользователь создал словарь: "{newDict}"')

# вновь запускает создание списка, потом создает словарь для суммирования
def new_dict_to_sum():
    new_list_for_dict(True)
    global newDict1
    newDict1 = dict(newList)
    save_logs(f'Пользователь создал словарь: "{newDict1}"')

# добавление данных в словарь
def add_to_dict(repeat):
    global newDict
    while repeat:
        while True:
            try:
                number = int(input('Сколько элементов вы хотите добавить?\n'))
                if number <= 0:
                    raise ZeroDivisionError
                for i in range(number):
                    key = input('Введите ключ\n')
                    value = input('Введите значение\n')
                    newDict[key] = value
                    save_logs(f'Пользователь ввел пару ключ-значение: "{key}"-"{value}"')
                break
            except:
                print('Введены неверные данные, повторите попытку')
                save_logs('Пользователь ввел неверные данные')
                continue
        print('Ваш словарь - ', newDict)
        # функция повтора опепрации, выдает True, если введено Y
        repeat = continue_or_break(f'{name1}')

# удаление значений из словаря
def del_from_dict(repeat):
    global newDict
    print(newDict)
    while repeat:
        while True:
            try:
                # вывод на печать всех пар ключ-значение
                for key,value in newDict.items():
                    print('Ключ - ', key,"Значение - ",value)
                for i in range(int(input('Сколько элементов вы хотите удалить?\n'))):
                    x = input('Введите ключ\n')
                    save_logs(f'Ползователь удалил значение {newDict[x]}')
                    newDict.pop(x)
                break
            except ValueError:
                print('Вводите только целое число')
                save_logs('Пользователь ввел неверное число элементов для удаления')
                continue
            except KeyError:
                print('Введен неверный ключ, повторите заново')
                save_logs('Пользователь ввел неверный ключ')
                continue
        print('Ваш словарь - ', newDict)
        # функция повтора опепрации, выдает True, если введено Y
        repeat = continue_or_break(f'{name2}')

def swap_2_elem_in_dict(repeat):
    while repeat:
        global newDict
        while True:
            for key, value in newDict.items():
                print('Ключ - ', key, "Значение - ", value)
            key1 = input('Введите первый ключ\n')
            key2 = input('Введите второе ключ\n')
            # проверка, естьли введенные ключи в словаре
            if key1 in newDict and key2 in newDict:
                # замена значений местами, переменные введены для сокращения кол-ва символов
                a,b = newDict[key1], newDict[key2]
                a, b = b,a
                save_logs(f'Пользователь поменял 2 значения местами: 1 значение - {a}, 2 значение - {b}\n'
                              f'и получил словарь {newDict}')
                break
            else:
                save_logs(f'Пользователь ввел неверные ключи: {key1}, {key2}')
                print('Введены неверные ключи, повторите ввод')
                continue
        print('Ваш словарь - ', newDict)
        # функция повтора опепрации, выдает True, если введено Y
        repeat = continue_or_break(f'{name3}')

def sum_dict(repeat):
    while repeat:
        global newDict
        # вызов фукнции по созданию второго слагаемого словаря newDict1
        new_dict_to_sum()
        print('Ваш исходный словарь - ', newDict)
        print('Ваш словарь с которым вы складываете - ', newDict1)
        # сложение ихсодного словаря с созданным
        newDict.update(newDict1)
        print('Ваш сложенный словарь - ', newDict)
        save_logs(f'Ползователь сложил два словаря и получил результат: {newDict}')
        # функция повтора опепрации, выдает True, если введено Y
        repeat = continue_or_break(f"{name4}")

def make_dict_unique(repeat):
    while repeat:
        global newDict
        # преобразование словаря в список формата [[],[],[]]
        newList = list(i for i in newDict.items())
        i = 0
        # ПОскольу i=0 берет первый список
        while i < len(newList):
            j = i + 1
            #сравнивает значение превого вложенного списка со всеми списками, по циклу проверяет все
            # списки
            while j < len(newList):
                # удаляет список по индеку j елси есть совпадние значенией
                if newList[i][1] == newList[j][1]:
                    del newList[j]
                # если нет совпадения переходит на след список
                else:
                    j += 1
            # после проверки первого элемента списка, переходит ко второму и сравнивает его с каждым элементом
            # и так далее, пока i не достигнет длины списка, то есть последнего элемента
            i += 1
            newDict = dict(newList)
        print('Ваш словарь - ', newDict)
        save_logs('Ползователь удалил из словаря повторящиеся значения')
        repeat = continue_or_break(f'{name5}')

def clearDict():
    global newDict
    newDict.clear()
    save_logs('Пользователь очистил словарь')
    print('Ваш словарь полностью очищен')

if __name__ == '__main__':
    from csv_logs import continue_or_break, save_logs
    main()
else:
    from csv_logs import continue_or_break, save_logs
