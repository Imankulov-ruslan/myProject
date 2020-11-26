from graphics import *
from csv_logs import save_logs
from tkinter import messagebox

def main():
    global mainName, name1, name2, name3, name4, name5, name6, name7, name8, name9
    mainName = '<<<Работа со списками>>>'
    name1 = '<Добавление элементов в список>'
    name2 = '<Удаление элемента из списка>'
    name3 = '<Поменять 2 элемента списка местами>'
    name4 = '<Поменять мах и мин значение списка местами>'
    name5 = '<Удалить повторяющиеся значения>'
    name6 = '<Вывести максимальный элемент списка>'
    name7 = '<Вывести минимальный элемент списка>'
    name8 = '<Очистить список>'
    endProgramm = '<Выход в главное меню>'
    listCreate()  # вызов главной фукнции

    global mainWindow
    mainWindow = CreateWindow(mainName)
    mainWindow.lable('Выберите программу')
    b = {name1: add_to_list, name2: delete_elems, name3: swap_elems,
         name4: swap_min_max_in_list, name5: delete_notUnique_elems, name6: max_in_list, name7: min_in_list,
         name8: clearList, endProgramm: quit}
    for i, j in b.items():
        CreateButtons(mainWindow.window, i, j).pack(pady=5)
    mainWindow.update_and_show_window()


def def_list_type():
    global typeList
    for i in yourList:
        if type(i) == list:
            typeList = 'hard'
        else:
            typeList = 'easy'


def listCreate():
    global yourList
    yourList = []
    inputWindow1 = CreateWindow('Создание словаря')
    inputWindow1.lable('Выберите тип списка который хотите создать:')

    def create_easy_list():
        yourList.clear()
        inputWindow = CreateWindow('Создание простого словаря')
        inputWindow.lable('Введите данные для создания')

        userInput = CreateInput(inputWindow.window, 1, 0, 'Введите данные через пробел')

        def check_input():
            global yourList
            nonlocal inputWindow1
            yourList = [str(i) for i in userInput.value.get().split()]
            messagebox.showinfo('Создание списка', f"Вы создали список {yourList}", master=inputWindow.window)
            inputWindow1.window.destroy()
            inputWindow.window.destroy()

        btn = CreateButtons(inputWindow.window, 'Ввод', check_input)
        btn.grid(2, 0, sticky='nwse')
        inputWindow.update_and_show_window()

    def create_hard_list():
        i = 1
        yourList.clear()

        inputWindow = CreateWindow('Создание простого словаря')
        inputWindow.lable('Введите данные для создания')

        userInput = CreateInput(inputWindow.window, 1, 0, 'Внесите данные')

        def check_input():
            nonlocal i
            i += 1

            btn.name.set(f'Добавить данные в список {i}')
            yourList.append([str(i) for i in userInput.value.get().split()])
            userInput.value.delete(0, END)

        def destroy():
            nonlocal inputWindow1
            messagebox.showinfo('Создание списка', f"Вы создали список {yourList}")
            inputWindow1.window.destroy()
            inputWindow.window.destroy()

        btn = CreateButtons(inputWindow.window, f'Добавить данные в список {i}', check_input)
        btn1 = CreateButtons(inputWindow.window, 'Exit', destroy)

        btn.grid(2, 0, sticky='wnse')
        btn1.grid(2, 1, sticky='wnse')

        inputWindow.update_and_show_window()

    btn = CreateButtons(inputWindow1.window, 'Простой список', create_easy_list)
    btn1 = CreateButtons(inputWindow1.window, 'Вложенный список', create_hard_list)

    btn.grid(0, 0)
    btn1.grid(0, 1)

    inputWindow1.update_and_show_window()
    save_logs(f'Пользователь создал список: "{yourList}"')
    def_list_type()

def add_hard_list():
    inputWindow = CreateWindow('Добавление данных в список')
    # inputWindow.lable('Выберите элементы для удаления')
    # inputWindow.lable.pack(fill=X, ipadx=10)
    fLeft = LabelFrame(master=inputWindow.window, text='Ваши вложенные списки')
    fRight = LabelFrame(master=inputWindow.window, text='Выделите список в левом столбце, введите элементы в поле и'
                                                        'нажмите ОК')
    fLeft.pack(side=LEFT, expand=1, fill=BOTH, ipadx=5, ipady=5)
    fRight.pack(side=RIGHT, expand=1, fill=BOTH, ipadx=5, ipady=5)
    lbox = Listbox(fLeft, height=15, selectmode=EXTENDED)
    scroll = Scrollbar(fLeft, command=lbox.yview)
    scroll.pack(side=RIGHT, fill=Y)
    lbox.config(yscrollcommand=scroll.set)
    lbox.pack(expand=1, side=TOP, fill=BOTH, padx=5, pady=5)

    userInput = CreateInput(fRight, 0, 0, 'Введите данные')

    def add_value():
        select = lbox.curselection()
        print(select)
        value = userInput.value.get()
        lbox.delete(0, END)
        for i in select:
            for j in value.split():
                print(j, i)
                yourList[i].append(j)
        for values in yourList:
            lbox.insert(END, values)
        userInput.value.delete(0, END)

    btn = CreateButtons(fRight, 'Ввод', add_value)
    btn.grid(1, 0, sticky='wsne')

    btn = CreateButtons(fRight, 'Выход', inputWindow.window.destroy)
    btn.grid(1, 1, sticky='wsne')
    # btn = Button(fRight, text='>>>', command=add_value)
    # btn.grid()

    for values in yourList:
        lbox.insert(END, values)
        print(values)
    inputWindow.update_and_show_window()
    save_logs(f'Пользователь добавил элементы и получил новый список: "{yourList}"')


def add_easy_list():
    inputWindow = CreateWindow('Создание простого словаря')
    inputWindow.lable('Введите данные для создания')

    userInput = CreateInput(inputWindow.window, 1, 0, 'Внесите данные')

    def check_input():
        # nonlocal inputWindow1
        # inputWindow1.window.destroy()
        for i in userInput.value.get().split():
            yourList.append(str(i))
        messagebox.showinfo('Добавление элементов', f'Вы добавили элементы:\n{userInput.value.get()}')
        inputWindow.window.destroy()

    btn = CreateButtons(inputWindow.window, 'Ввод', check_input)
    btn.grid(2, 0, sticky='wnse')
    inputWindow.update_and_show_window()
    save_logs(f'Пользователь добавил элементы и получил новый список: "{yourList}"')


def add_to_list():
    global yourList
    save_logs(f'Пользователь запустил программу {name1}')
    if typeList == 'hard':
        add_hard_list()
    else:
        add_easy_list()

def swap_elem_hard_list():
    # создание главного окна
    inputWindow = CreateWindow('Замена данных в списке')

    # создание фреймов (разделение главного окна)
    fBottom = Label(master=inputWindow.window)
    fBottom.pack(side=BOTTOM, expand=1, fill=BOTH, ipadx=5, ipady=5)

    fLeft = LabelFrame(master=inputWindow.window, text='Выберите 2 элемента для замены')
    fLeft.pack(side=LEFT, expand=1, fill=BOTH, ipadx=5, ipady=5)

    fRight1 = Label(master=inputWindow.window)
    fRight1.pack(side=LEFT, expand=1, fill=BOTH, ipadx=5, ipady=5)

    lbox = Listbox(fLeft, height=15, selectmode=EXTENDED)

    scroll = Scrollbar(fLeft, command=lbox.yview)
    scroll.pack(side=RIGHT, fill=Y)

    lbox.config(yscrollcommand=scroll.set)
    lbox.pack(expand=1, side=RIGHT, fill=BOTH, padx=5, pady=5)

    def swap_elem():
        nonlocal lbox
        if len(lbox.curselection()) != 2:
            return messagebox.showerror('Ошибка', 'Выберите только 2 значения', master=inputWindow.window)
        select = lbox.curselection()
        try:
            index1 = [int(i) for i in (myDict[select[0]].split('|'))]
            index2 = [int(i) for i in (myDict[select[1]].split('|'))]
            print(index1, index2)
            a, b = yourList[index1[0]][index1[1]], yourList[index2[0]][index2[1]]
            yourList[index1[0]][index1[1]], yourList[index2[0]][index2[1]] = b, a
            save_logs(f'Пользователь поменял местами значения {a} и {b}')
            lbox.delete(0, END)
            myDict.clear()
            a = 0
            c = 0
            for i in yourList:
                b = 0
                myDict[c] = lbox.insert(END, f'<Spisok {a + 1}>')
                for j in i:
                    lbox.insert(END, j)
                    c += 1
                    myDict[c] = str(a) + '|' + str(b)
                    b += 1
                c += 1
                a += 1
        except:
            messagebox.showerror('Ошибка', "Выберите только значения из списков", master=inputWindow.window)
        print(yourList)

    myDict = {}
    a = 0
    c = 0
    for i in yourList:
        b = 0
        myDict[c] = lbox.insert(END, f'<Spisok {a + 1}>')
        for j in i:
            lbox.insert(END, j)
            c += 1
            myDict[c] = str(a) + '|' + str(b)
            b += 1
        c += 1
        a += 1
    print(myDict)

    btn = CreateButtons(fBottom, 'Выход', inputWindow.window.destroy)
    btn.pack(side=BOTTOM)

    btn1 = CreateButtons(fBottom, 'Выполнить', swap_elem)
    btn1.pack(anchor=S)

    inputWindow.update_and_show_window()

def swap_elem_easy_list():
    inputWindow = CreateWindow('Замена данных в списке')

    fBottom = Label(master=inputWindow.window)
    fBottom.pack(side=BOTTOM, expand=1, fill=BOTH, ipadx=5, ipady=5)

    fLeft = LabelFrame(master=inputWindow.window, text='Выберите 2 элемента для замены')
    fLeft.pack(side=LEFT, expand=1, fill=BOTH, ipadx=5, ipady=5)

    lbox = Listbox(fLeft, height=15, selectmode=EXTENDED)

    scroll = Scrollbar(fLeft, command=lbox.yview)
    scroll.pack(side=RIGHT, fill=Y)

    lbox.config(yscrollcommand=scroll.set)
    lbox.pack(expand=1, side=TOP, fill=BOTH, padx=5, pady=5)

    for i in yourList:
        lbox.insert(END, i)

    def swap_elem():
        select = lbox.curselection()
        if len(lbox.curselection()) != 2:
            return messagebox.showerror('Ошибка', 'Выберите только 2 значения', master=inputWindow.window)
        yourList[select[0]], yourList[select[1]] = yourList[select[1]], yourList[select[0]]
        save_logs(f'Пользователь поменял местами значения {yourList[select[0]]} и {yourList[select[1]]}')
        lbox.delete(0, END)
        for i in yourList:
            lbox.insert(END, i)

    btn = CreateButtons(fBottom, 'Выход', inputWindow.window.destroy)
    btn.pack(side=BOTTOM)

    btn1 = CreateButtons(fBottom, 'Выполнить', swap_elem)
    btn1.pack(anchor=S, side=BOTTOM)

    inputWindow.update_and_show_window()

def swap_elems():
    save_logs(f'Пользователь запустил программу {name3}')
    if typeList == 'hard':
        swap_elem_hard_list()
    else:
        swap_elem_easy_list()

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
    messagebox.showinfo('Замена максимального и минимальнго значения',
                        f'Вы поменяли мах и мин значения списка местами\n Ваш новый список {yourList}',
                        master=mainWindow.window)
    # max_in_list, min_in_list = a, b

def max_in_hard_list():
    a = yourList[0][0]
    for i in yourList:
        for j in i:
            if j >= a:
                a = j
    messagebox.showinfo('Максимальное значение', f'Максимальное значение в вашем списке - {a}',
                        master=mainWindow.window)
    save_logs(f'Пользователь получил максимальное значение: "{a}"')


def min_in_hard_list():
    a = yourList[0][0]
    for i in range(len(yourList)):
        for j in range(len(yourList[i])):
            if yourList[i][j] <= a:
                a = yourList[i][j]
    messagebox.showinfo('Минимальное значение', f'Минимальное значение в вашем списке - {a}', master=mainWindow.window)
    save_logs(f'Пользователь получил минимальное значение: "{a}"')

def max_in_list():
    save_logs(f'Пользователь запустил программу {name6}')
    if typeList == 'hard':
        max_in_hard_list()
    else:
        messagebox.showinfo('Максимальное значение', f'Максимальное значение в вашем списке - {max(yourList)}',
                            master=mainWindow.window)
        save_logs(f'Пользователь получил максимальное значение списка: "{max(yourList)}"')

def min_in_list():
    save_logs(f'Пользователь запустил программу {name7}')
    if typeList == 'hard':
        min_in_hard_list()
    else:
        messagebox.showinfo('Минимальное значение', f'Минимальное значение в вашем списке - {min(yourList)}',
                            master=mainWindow.window)
        save_logs(f'Пользователь получил минимальное значение списка: "{min(yourList)}"')

def swap_min_max_in_easy_list():
    global yourList, max_in_list, max_in_list
    a = max(yourList)
    b = min(yourList)
    indA = yourList.index(a)
    indB = yourList.index(b)
    yourList[indA], yourList[indB] = b, a
    max_in_list, min_in_list = a, b
    messagebox.showinfo('Замена максимального и минимальнго значения',
                        f'Вы поменяли мах и мин значения списка местами\n Ваш новый список {yourList}',
                        master=mainWindow.window)

def swap_min_max_in_list():
    save_logs(f'Пользователь запустил программу {name4}')
    if typeList == 'hard':
        swap_min_max_in_hard_list()
    else:
        swap_min_max_in_easy_list()
    save_logs(f'Пользователь поменял максимальный и минимальный элементы местами и получил список: "{yourList}"')

def delete_notUnique_elems():
    save_logs(f'Пользователь запустил программу {name5}')
    if typeList == 'hard':
        count = 0
        for i in yourList:
            for j in i:
                if i.count(j) > 1:
                    while i.count(j) > 1:
                        i.remove(j)
                        save_logs(f'Пользователь удалил повторящиеся значения элемента: "{j}"')
                else:
                    save_logs(f'Кол-во вхождений элемента: "{j}" равно единице')
    else:
        for i in yourList:
            if yourList.count(i) > 1:
                while yourList.count(i) > 1:
                    yourList.remove(i)
                    save_logs(f'Пользователь удалил повторящиеся значения элемента: "{i}"')
            else:
                save_logs(f'Кол-во вхождений элемента: "{i}" равно единице')
    messagebox.showinfo('Уникальный список',
                        f"Вы удалили все повторяющиеся значения в списке\nВаш список: {yourList}",
                        master=mainWindow.window)

def delete_elems():
    save_logs(f'Пользователь запустил программу {name2}')
    if typeList == 'hard':
        delete_elems_hard_list()
    else:
        delete_elems_easy_list()

def delete_elems_hard_list():
    inputWindow = CreateWindow('Удаление элементов из списка')

    # создание фреймов (разделение главного окна)
    fBottom = Label(master=inputWindow.window)
    fBottom.pack(side=BOTTOM, expand=1, fill=BOTH, ipadx=5, ipady=5)

    fLeft = LabelFrame(master=inputWindow.window, text='Выберите элемент для удаления')
    fLeft.pack(side=LEFT, expand=1, fill=BOTH, ipadx=5, ipady=5)

    fRight1 = Label(master=inputWindow.window)
    fRight1.pack(side=LEFT, expand=1, fill=BOTH, ipadx=5, ipady=5)

    lbox = Listbox(fLeft, height=15)

    scroll = Scrollbar(fLeft, command=lbox.yview)
    scroll.pack(side=RIGHT, fill=Y)

    lbox.config(yscrollcommand=scroll.set)
    lbox.pack(expand=1, side=RIGHT, fill=BOTH, padx=5, pady=5)

    def swap_elem():
        nonlocal lbox
        select = lbox.curselection()
        try:
            index = [int(i) for i in (myDict[select[0]].split('|'))]
            del yourList[index[0]][index[1]]
            save_logs(f'Пользователь удалил значение {yourList[index[0]][index[1]]} из списка')
            lbox.delete(0, END)
            myDict.clear()
            a = 0
            c = 0
            for i in yourList:
                b = 0
                myDict[c] = lbox.insert(END, f'<Spisok {a + 1}>')
                for j in i:
                    lbox.insert(END, j)
                    c += 1
                    myDict[c] = str(a) + '|' + str(b)
                    b += 1
                c += 1
                a += 1
        except:
            messagebox.showerror('Ошибка', "Выберите только значения из списков")
        print(yourList)

    myDict = {}
    a = 0
    c = 0
    for i in yourList:
        b = 0
        myDict[c] = lbox.insert(END, f'<Spisok {a + 1}>')
        for j in i:
            lbox.insert(END, j)
            c += 1
            myDict[c] = str(a) + '|' + str(b)
            b += 1
        c += 1
        a += 1
    print(myDict)

    btn = CreateButtons(fBottom, 'Выход', inputWindow.window.destroy)
    btn.pack(side=BOTTOM)

    btn1 = CreateButtons(fBottom, 'Выполнить', swap_elem)
    btn1.pack(anchor=S)

    inputWindow.update_and_show_window()

def delete_elems_easy_list():
    inputWindow = CreateWindow('Удаление элементов из спика')

    fBottom = Label(master=inputWindow.window)
    fBottom.pack(side=BOTTOM, expand=1, fill=BOTH, ipadx=5, ipady=5)

    fLeft = LabelFrame(master=inputWindow.window, text='Выберите элемент в списке для удаления')
    fLeft.pack(side=LEFT, expand=1, fill=BOTH, ipadx=5, ipady=5)

    lbox = Listbox(fLeft, height=15)

    scroll = Scrollbar(fLeft, command=lbox.yview)
    scroll.pack(side=RIGHT, fill=Y)

    lbox.config(yscrollcommand=scroll.set)
    lbox.pack(expand=1, side=TOP, fill=BOTH, padx=5, pady=5)

    for i in yourList:
        lbox.insert(END, i)

    def swap_elem():
        select = lbox.curselection()
        save_logs(f'Пользователь удалил значение {yourList[select[0]]} из списка')
        del yourList[select[0]]
        lbox.delete(0, END)
        for i in yourList:
            lbox.insert(END, i)

    btn = CreateButtons(fBottom, 'Выход', inputWindow.window.destroy)
    btn.pack(side=BOTTOM)

    btn1 = CreateButtons(fBottom, 'Удалить', swap_elem)
    btn1.pack(anchor=S, side=BOTTOM)

    inputWindow.update_and_show_window()

def clearList():
    save_logs(f'Пользователь запустил программу {name8}')
    if messagebox.askyesno("Очистка списка", 'Вы уверены, что хотите очистить словарь?'):
        global yourList, typeList
        yourList.clear()
        typeList = 'easy'
        messagebox.showinfo('Очистка списка', 'Ваш список очищен')
        save_logs(f'Пользователь очистил список')

def quit():
    mainWindow.window.destroy()
    save_logs('Пользователь вышел в основное меню')
    import myProject
    myProject.main()

if __name__ == '__main__':
    main()

