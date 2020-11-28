

def main():
    global mainName, name1, name2, name3, name4, name5, name6, name7, name8, name9
    mainName = '"Работа со списками"'
    name1 = '"Добавление элементов в список"'
    name2 = '"Удаление элемента из списка"'
    name3 = '"Поменять 2 элемента списка местами"'
    name4 = '"Поменять мах и мин значение списка местами"'
    name5 = '"Сложить список с новым списком"'
    name6 = '"Удалить повторяющиеся значения"'
    name7 = '"Вывести максимальный элемент списка"'
    name8 = '"Вывести минимальный элемент списка"'
    name9 = '"Очистить список"'
    listCreate(True)# вызов главной фукнции
    number_input()



def print_list_menu():
    print(f'''
*****\t{mainName}\t*****
Выберите что нужно сделать с вашим списком:
1 - {name1}
2 - {name2}
3 - {name3}
4 - {name4}
5 - {name5}
6 - {name6}
7 - {name7}
8 - {name8}
9 - {name9}
0 - Выйти из программы {mainName} в основное меню
Введите цифру от 0 до 9: ''', end='')

def number_input():
    while True:
        print_list_menu()
        number = input()
        if number == '1':
            save_logs(f'Ползователь выбрал операцию: {name1}')
            add_to_list(True)
        elif number == '2':
            save_logs(f'Ползователь выбрал операцию: {name2}')
            delete_elems(True)
        elif number == '3':
            save_logs(f'Ползователь выбрал операцию: {name3}')
            swap_elem_list(True)
        elif number == '4':
            save_logs(f'Ползователь выбрал операцию: {name4}')
            swap_min_max_in_list(True)
        elif number == '5':
            save_logs(f'Ползователь выбрал операцию: {name5}')
            listSum(True)
        elif number == '6':
            save_logs(f'Ползователь выбрал операцию: {name6}')
            delete_notUnique_elems(True)
        elif number == '7':
            save_logs(f'Ползователь выбрал операцию: {name7}')
            max_in_list(True)
        elif number == '8':
            save_logs(f'Ползователь выбрал операцию: {name8}')
            min_in_list(True)
        elif number == '9':
            save_logs(f'Ползователь выбрал операцию: {name9} и очистил список')
            yourList.clear()
            print('Ваш список полностью очищен')
            global listType
            listType = 'easy'
        elif number == '0':
            save_logs(f'Ползователь ввел 0 и завершил программу: {mainName}')
            print(f'Программа {mainName} завершена')
            break
        else:
            save_logs(f'Ползователь неверно ввел данные')
            print('\tВведите только числа от 0 до 9\n')
            continue

def def_list_type():
    global listType
    for i in yourList:
        if type(i) == list:
            listType = 'hard'
        else:
            listType = 'easy'


def listCreate(repeat):
    while repeat:
        global yourList
        print('Для начала работы вам необходимо создать список')
        type_of_list = input("Какой список вы хотите создать? 1 - простой список, 2 - вложенный список\n")
        if type_of_list == "1":
            while True:
                listType = input("Выберите тип списка: 1 - список с одинаковыми значениями, 2 - список с уникальными"
                                 " значениями\n")
                if listType == "1":
                    while True:
                        try:
                            yourList = [str(input("Введите элемент\n"))] * int(input("Введите количество элементов\n"))
                        except ValueError:
                            print("Введите верные данные")
                            continue
                        break
                elif listType == "2":
                    yourList = [str(i) for i in input("Введите элементы через пробел и нажмите Enter\n").split()]
                else:
                    print('Введите только 1 или 2')
                    continue
                break
        elif type_of_list == "2":
            while True:
                try:
                    quantity_of_lists_in_main_list = int(input("Введите кол-во вложенных списков\n"))
                    yourList = [[str(i) for i in input("Введите элементы через пробел\n").split()] for k in
                                range(quantity_of_lists_in_main_list)]
                except ValueError:
                    print('При вводе количества вложенных списков вводите только целые числа!')
                    continue
                break
        else:
            print('Введите только 1 или 2')
            continue
        def_list_type()
        print("Ваш список: ", yourList)
        save_logs(f'Пользователь создал список: "{yourList}"')
        repeat = continue_or_break("Создание списка")



def add_hard_list():
    while True:
        global yourList
        addPosition = input('Каким методом добавить элементы? 1 - добавить эл-ты во вложенный список,'
                            '2 - добавить новый вложенный список\n')
        if addPosition == '1':
            while True:
                try:
                    indexAdd = int(input('Введите индекс вложенного списка в который необходимо добавить элементы\n'))
                    for i in range(int(input('Сколько добавить элементов?\n'))):
                        yourList[indexAdd - 1].append(input('Введите элемент\n'))
                except:
                    print('При вводе индекса списка произошла ошибка, вводите только числа от 1 до', len(yourList))
                    continue
                break
            break
        elif addPosition == '2':
            yourList.append(input('Введите элементы через пробел и нажмите Enter\n').split())
            break
        else:
            print('Введите только числа 1, 2')
            continue


def add_to_list(repeat):
    global yourList
    while repeat:
        print("Ваш список: ", yourList)
        if listType == 'hard':
            add_hard_list()
        else:
            yourList += (input('Введите элементы через пробел и нажмите Enter\n').split())
        save_logs(f'Пользователь добавил элементы и получил список: "{yourList}"')
        print("Ваш список: ", yourList)
        repeat = continue_or_break(f'{name1}')


def swap_elem_hard_list():
    while True:
        global yourList
        try:
            elems = [[int(i) for i in input("Введите первый индекс\n").split()],
                     [int(i) for i in input("Введите второй индекс\n").split()]]
            if len(elems[0]) != 2 or len(elems[1]) != 2:
                print("Некорректный ввод индексов! Для каждого индекса введите 2 числа")
                continue
            a, b = elems[0]
            c, d = elems[1]
            yourList[a][b], yourList[c][d] = yourList[c][d], yourList[a][b]
            break
        except IndexError:
            print("Некорректный ввод индексов! Индекс вне диапазона")
            continue
        except ValueError:
            print('Введите только целые числа!')
            continue


def swap_elem_easy_list():
    while True:
        global yourList
        try:
            index = 0
            for i in yourList:
                print('Элемент - ', i, "Индекс элемента - ", index)
                index += 1
            elem1 = int(input('Введите индекс первого элемента\n'))
            elem2 = int(input('Введите индекс второго элемента\n'))
            yourList[elem1], yourList[elem2] = yourList[elem2], yourList[elem1]
            break
        except ValueError:
            print("Введите только числовые значения")
            continue
        except IndexError:
            print("Введен неверный индекс, повторите операцию заново")
            continue


def swap_elem_list(repeat):
    while repeat:
        from copy import deepcopy
        a = deepcopy(yourList)
        if listType == 'hard':
            for i in yourList:
                index = 0
                for j in i:
                    print('Элемент - ', j, "Индекс элемента - ", yourList.index(i), index)
                    index += 1
            swap_elem_hard_list()
        else:
            swap_elem_easy_list()
        print("Ваш  исходный список: ",a)
        print("Ваш  измененный список: ", yourList)
        save_logs(f'Пользователь поменял элементы местами и получил список: "{yourList}"')
        repeat = continue_or_break(f'{name3}')


def swap_min_max_in_hard_list():
    global yourList, max_in_list, max_in_list
    a = yourList[0][0]
    b = a
    for i in range(len(yourList)):
        for j in range(len(yourList[i])):
            if yourList[i][j] >= a:
                a = yourList[i][j]
                indA = [i, j]
            if yourList[i][j] <= b:
                b = yourList[i][j]
                indB = [i, j]
    yourList[indA[0]][indA[1]], yourList[indB[0]][indB[1]] = b, a
    # max_in_list, min_in_list = a, b

def max_in_hard_list():
    a = yourList[0][0]
    for i in yourList:
        for j in i:
            if j >= a:
                a = j
    print('Максимальное значение в вашем списке - ', a)
    save_logs(f'Пользователь получил максимальное значение: "{a}"')

def min_in_hard_list():
    a = yourList[0][0]
    for i in range(len(yourList)):
        for j in range(len(yourList[i])):
            if yourList[i][j] <= a:
                a = yourList[i][j]
    print('Минимальное значение в вашем списке - ', a)
    save_logs(f'Пользователь получил минимальное значение: "{a}"')


def max_in_list(repeat):
    while repeat:
        print("Ваш список: ", yourList)
        if listType == 'hard':
            max_in_hard_list()
        else:
            print('Максимальное значение в вашем списке -', max(yourList))
            save_logs(f'Пользователь получил максимальное значение списка: "{max(yourList)}"')
        repeat = continue_or_break(f"{name7}")

def min_in_list(repeat):
    while repeat:
        print("Ваш список: ", yourList)
        if listType == 'hard':
            min_in_hard_list()
        else:
            print('Минимальное значение в вашем списке - ', min(yourList))
            save_logs(f'Пользователь получил минимальное значение списка: "{min(yourList)}"')
        repeat = continue_or_break(f"{name8}")


def swap_min_max_in_easy_list():
    global yourList, max_in_list, max_in_list
    a = max(yourList)
    b = min(yourList)
    indA = yourList.index(a)
    indB = yourList.index(b)
    yourList[indA], yourList[indB] = b, a
    max_in_list, min_in_list = a, b


def swap_min_max_in_list(repeat):
    while repeat:
        print("Ваш исходный список: ", yourList)
        if listType == 'hard':
            swap_min_max_in_hard_list()
        else:
            swap_min_max_in_easy_list()
        print("Ваш измененный список список: ", yourList)
        save_logs(f'Пользователь поменял максимальный и минимальный элементы местами и получил список: "{yourList}"')
        repeat = continue_or_break(f'{name4}')


def listSum(repeat):
    while repeat:
        print("Ваш список: ", yourList)
        what_to_do = input("Создайте второй список для сложения? 1 -  создать простой список, 2 - создать вложенный список\n")
        if what_to_do == "1":
            while True:
                listType = input(
                    "Выберите тип списка: 1 - список с одинаковыми значениями, 2 - список с уникальными"
                    " значениями\n")
                if listType == "1":
                    while True:
                        try:
                            secondList = [input("Введите элемент\n")] * int(input("Введите количество элементов\n"))
                        except ValueError:
                            print("Введите верные данные")
                            continue
                        break
                elif listType == "2":
                    secondList = [i for i in input("Введите элементы через пробел и нажмите Enter\n").split()]
                else:
                    print('Введите только 1 или 2')
                    continue
                break
        elif what_to_do == "2":
            while True:
                try:
                    quantity_of_lists_in_main_list = int(input("Введите кол-во вложенных списков\n"))
                    secondList = [[i for i in input("Введите элементы через пробел\n").split()] for k in
                                  range(quantity_of_lists_in_main_list)]
                except ValueError:
                    print('При вводе количества вложенных списков вводите только целые числа!')
                    continue
                break
        sumList = yourList + secondList
        print('Результаты суммы списков - ',sumList)
        save_logs(f'Пользователь сложил список {yourList} со списком {secondList} и получил новый списко: "{sumList}"')
        repeat = continue_or_break(f'{name5}')


def delete_notUnique_elems(repeat):
    while repeat:
        print("Ваш список: ", yourList)
        delElem = input('Выберите элемент для удаления\n')
        if listType == 'hard':
            count = 0
            for i in yourList:
                if delElem in i:
                    if i.count(delElem) > 1:
                        while i.count(delElem) > 1:
                            i.remove(delElem)
                            save_logs(f'Пользователь удалил повторящиеся значения элемента: "{delElem}"')
                    else:
                        print('Кол-во вхождений элемента', delElem,'в список', i, 'равно единице')
                        save_logs(f'Кол-во вхождений элемента: "{delElem}" равно единице')
                else:
                    print('Элемента',delElem, 'нет в списке', i)
                    save_logs(f'Элемента: "{delElem}" нет в списке')
        else:
            if delElem in yourList:
                if yourList.count(delElem) > 1:
                    while yourList.count(delElem) > 1:
                        yourList.remove(delElem)
                        save_logs(f'Пользователь удалил повторящиеся значения элемента: "{delElem}"')
                else:
                    print("Кол-во его вхождений элемента равно единице, выберите другой элемент")
                    save_logs(f'Кол-во вхождений элемента: "{delElem}" равно единице')
            else:
                print("Такого элемента нет в списке")
                save_logs(f'Элемента: "{delElem}" нет в списке')
        print("Ваш список: ", yourList)
        repeat = continue_or_break(f'{name6}')

def delete_elems(repeat):
    while repeat:
        print("Ваш список: ", yourList)
        if listType == 'hard':
            for i in yourList:
                index = 0
                for j in i:
                    print('Элемент - ', j, "Индекс элемента - ", yourList.index(i), index)
                    index += 1
            delete_elems_hard_list()
        else:
            delete_elems_easy_list()
        print("Ваш список: ", yourList)
        repeat = continue_or_break(f'{name2}')

def delete_elems_hard_list():
    while True:
        global yourList
        try:
            elems = [int(i) for i in input("Введите индекс\n").split()]
            if len(elems) != 2:
                print("Некорректный ввод индексов! Для каждого индекса введите 2 числа")
                continue
            a, b = elems[0], elems[1]
            save_logs(f'Пользователь удалил элемент: "{yourList[a][b]}')
            del yourList[a][b]
            break
        except IndexError:
            print("Некорректный ввод индексов! Индекс вне диапазона")
            save_logs(f'Пользователь ввел неверные данные')
            continue
        except ValueError:
            print('Введите только целые числа!')
            save_logs(f'Пользователь ввел неверные данные')
            continue

def delete_elems_easy_list():
    while True:
        global yourList
        try:
            index = 0
            for i in yourList:
                print('Элемент - ', i, "Индекс элемента - ", index)
                index += 1
            elem = int(input('Введите индекс элемента\n'))
            save_logs(f'Пользователь удалил элемент: {yourList[elem]}')
            del yourList[elem]
            break
        except ValueError:
            print("Введите только числовые значения")
            save_logs(f'Пользователь ввел неверные данные')
            continue
        except IndexError:
            print("Введен неверный индекс, повторите операцию заново")
            save_logs(f'Пользователь ввел неверные данные')
            continue

if __name__ == '__main__':
    from csv_logs import continue_or_break, save_logs
    main()
else:
    from csv_logs import continue_or_break, save_logs
