from csv_logs import save_logs
from graphics import *
from tkinter import messagebox

mainName = '<<<Работа со словарями>>>'
name1 = '<Добавление элементов в словарь>'
name2 = '<Удаление элемента из словаря>'
name3 = '<Поменять 2 элемента словаря местами>'
name4 = '<Сложить словарь с другим словарем>'
name5 = '<Удалить повторяющиеся значения словаря>'
name6 = '<Очистить словарь>'
endProgramm = '<Выход в главное меню>'


def main():
    create_dict()
    global mainWindow
    mainWindow = CreateWindow(mainName)
    b = {name1: add_to_dict, name2: del_from_dict, name3: swap_2_elem_in_dict,
         name4: sum_dict, name5: make_dict_unique, name6: clearDict, endProgramm: quit}
    for i, j in b.items():
        CreateButtons(mainWindow.window, i, j).pack(pady=5)
    mainWindow.update_and_show_window()


def repeat_func(name, master):
    repeat = messagebox.askyesno(title="Повтор операции", message="Повторить данную операцию?", master=master)
    if repeat:
        save_logs(f'Пользователь повторил операцию: {name}')
        return repeat
    save_logs(f'Пользователь завершил операцию: {name}')
    return repeat


def create_dict():
    create_list()
    global newDict
    newDict = dict(newList)
    save_logs(f'Пользователь создал словарь: "{newDict}"')
    messagebox.showinfo('Создание словаря', f"Вы создали словарь {newDict}", master=inputWindow.window)
    inputWindow.window.destroy()


# создание списка формата [[],[],[]] для преобразования в словарь
def create_list(repeat=True):
    global newList
    while repeat:
        global inputWindow
        inputWindow = CreateWindow('Создание словаря')
        intInput = CreateInput(inputWindow.window, 1, 0, 'Введите кол-во значений словаря')

        def check_input():
            try:
                values = int(intInput.value.get())
                if values <= 0:
                    raise Exception
                global newList
                newList = [[] for k in range(values)]
                j = len(newList)
                for i in range(len(newList)):
                    inputWindow = CreateWindow('Создание словаря')
                    stringInput = CreateInput(inputWindow.window, 0, 0, 'Введите ключ')
                    stringInput1 = CreateInput(inputWindow.window, 1, 0, 'Введите значение')
                    button1 = CreateButtons(inputWindow.window, 'Ввод', inputWindow.window.quit)
                    button1.grid(2, 0, sticky='we', columnspan=2)
                    inputWindow.update_and_show_window()
                    newList[i].append(stringInput.value.get())
                    newList[i].append(stringInput1.value.get())
                    inputWindow.window.destroy()
                inputWindow.window.quit()


            except:
                intInput.value.delete(0, END)
                save_logs(f'Ползователь получил ошибку')
                messagebox.showerror("Ошибка", "Поле ввода очищено!\nВводите только числа больше нуля")

        button = CreateButtons(inputWindow.window, 'Ввод', check_input)
        button.grid(2, 0, sticky='wens', columnspan=2)
        inputWindow.update_and_show_window()
        repeat = repeat_func('Создание словаря', inputWindow.window)


# вновь запускает создание списка, потом создает словарь для суммирования
def new_dict_to_sum():
    global newDict1
    create_list(True)
    save_logs(f'Ползователь выбрал операцию: {name4}')
    newDict1 = dict(newList)
    save_logs(f'Пользователь создал словарь: "{newDict1}"')


# добавление данных в словарь
def add_to_dict(repeat=True):
    save_logs(f'Ползователь выбрал операцию: {name1}')
    while repeat:
        inputWindow = CreateWindow('Создание словаря')
        inputWindow.lable('Выберите сколько элементов добавить')
        inputWindow.lable.grid(row=0, column=0, columnspan=2, sticky='wens', ipady=5, ipadx=10, pady=5)
        value = Spinbox(master=inputWindow.window, from_=1, to=999)
        value.grid(row=1, column=1, pady=10, ipadx=10, ipady=10, sticky='wens')

        def check_input():
            global newDict
            nonlocal value
            i = int(value.get())
            for i in range(int(value.get())):
                inputWindow = CreateWindow('Создание словаря')
                dict_key = CreateInput(inputWindow.window, 0, 0, 'Введите ключ')
                dict_value = CreateInput(inputWindow.window, 1, 0, 'Введите значение')
                button1 = CreateButtons(inputWindow.window, 'Ввод', inputWindow.window.quit)
                button1.grid(2, 0, sticky='we', columnspan=2)
                inputWindow.update_and_show_window()
                newDict[dict_key.value.get()] = dict_value.value.get()
                save_logs(f'Пользователь ввел пару ключ-значение: "{dict_key.value.get()}"-"{dict_value.value.get()}"')
                inputWindow.window.destroy()
            inputWindow.window.quit()

        button = CreateButtons(inputWindow.window, 'Ввод', check_input)
        button.grid(row=1, column=0, sticky='wens')
        inputWindow.update_and_show_window()
        repeat = repeat_func(name1, inputWindow.window)
        messagebox.showinfo('Добавление элементов в словарь',
                            f"Вы добавили новые элементы и полуичли новый словарь:\n {newDict}",
                            master=inputWindow.window)
        inputWindow.window.destroy()


# удаление значений из словаря
def del_from_dict(repeat=True):
    save_logs(f'Ползователь выбрал операцию: {name2}')
    while repeat:
        inputWindow = CreateWindow('Создание словаря')
        inputWindow.lable('Выберите элементы для удаления')
        inputWindow.lable.pack(fill=X, ipadx=10)
        fLeft = LabelFrame(master=inputWindow.window, text='Ваши значения в словаре')
        fRight = LabelFrame(master=inputWindow.window, text='Список для удаления')
        fCenter = Frame(master=inputWindow.window)
        fLeft.pack(side=LEFT, expand=1, fill=BOTH, ipadx=5, ipady=5)
        fCenter.pack(side=LEFT, expand=1, fill=BOTH, ipadx=5, ipady=5)
        fRight.pack(side=RIGHT, expand=1, fill=BOTH, ipadx=5, ipady=5)
        lbox = Listbox(fLeft, height=15, selectmode=EXTENDED)
        scroll = Scrollbar(fLeft, command=lbox.yview)
        scroll.pack(side=RIGHT, fill=Y)
        lbox.config(yscrollcommand=scroll.set)
        lbox.pack(expand=1, side=TOP, fill=BOTH, padx=5, pady=5)
        lbox1 = Listbox(fRight, height=15, selectmode=EXTENDED)
        scroll1 = Scrollbar(fRight, command=lbox1.yview)
        scroll1.pack(side=RIGHT, fill=Y)
        lbox1.config(yscrollcommand=scroll1.set)
        lbox1.pack(expand=1, side=TOP, fill=BOTH, padx=5, pady=5)

        def add_to_left_list():
            select = list(lbox.curselection())
            select.reverse()
            values = []
            for i in select:
                values.insert(0, lbox.get(i))
                lbox.delete(i)
            for i in values:
                lbox1.insert(END, i)

        def add_to_right_list():
            select = list(lbox1.curselection())
            select.reverse()
            values = []
            for i in select:
                values.insert(0, lbox1.get(i))
                lbox1.delete(i)
            for i in values:
                lbox.insert(END, i)

        def del_from_dict():
            keys = []
            for i in lbox1.get(0, END):
                for key, value in newDict.items():
                    if i == value:
                        keys.append(key)
            for i in keys:
                newDict.pop(i)
            messagebox.showinfo('Удаление элементов', f'Вы удалили из словаря значения:\n {lbox1.get(0, END)}',
                                master=inputWindow.window)
            save_logs(f'Пользователь удалил из словаря значения:\n {lbox1.get(0, END)}')
            inputWindow.window.quit()

        btn = Button(fCenter, text='>>>', command=add_to_left_list)
        btn.pack(expand=1, anchor=S, pady=5)
        btn2 = Button(fCenter, text='<<<', command=add_to_right_list)
        btn2.pack(expand=1, anchor=N)
        btn3 = Button(fCenter, text='OK', command=del_from_dict)
        btn3.pack(expand=1, anchor=N)
        for values in newDict.values():
            lbox.insert(END, values)
        inputWindow.update_and_show_window()
        repeat = repeat_func(name2, inputWindow.window)
        inputWindow.window.destroy()


def swap_2_elem_in_dict(repeat=True):
    while repeat:
        save_logs(f'Ползователь выбрал операцию: {name3}')
        inputWindow = CreateWindow('Создание словаря')
        inputWindow.lable('Выберите 2 значения для \nзамены значений у ключа')
        inputWindow.lable.pack(fill=X, ipadx=10)
        fLeft = LabelFrame(master=inputWindow.window, text='Пара ключ значение')
        fLeft.pack(side=LEFT, expand=1, fill=BOTH, ipadx=5, ipady=5)
        lbox = Listbox(fLeft, height=15, selectmode=EXTENDED)
        scroll = Scrollbar(fLeft, command=lbox.yview)
        scroll.pack(side=RIGHT, fill=Y)
        lbox.config(yscrollcommand=scroll.set)
        lbox.pack(expand=1, side=TOP, fill=BOTH, padx=5, pady=5)

        for keys, values in newDict.items():
            lbox.insert(END, f'{keys}-{values}')

        def swap_elems_in_dict():
            if len(lbox.curselection()) != 2:
                save_logs(f'Пользователь получил ошибку неправильного выбора')
                return messagebox.showerror('Ошибка', 'Выберите только 2 значения', master=inputWindow.window)
            key1 = lbox.get(lbox.curselection()[0]).split('-')
            key2 = lbox.get(lbox.curselection()[1]).split('-')
            newDict[key1[0]], newDict[key2[0]] = newDict[key2[0]], newDict[key1[0]]
            save_logs(f'Пользователь поменял {newDict[key1[0]]} и {newDict[key2[0]]} местами')
            inputWindow.window.quit()

        btn = Button(fLeft, text='Ok', command=swap_elems_in_dict)
        btn.pack(expand=1, anchor=S, pady=5)
        inputWindow.update_and_show_window()
        repeat = repeat_func(name3, inputWindow.window)
        messagebox.showinfo('Новый словарь', f'Ваш новый словарь:\n{newDict}', master=inputWindow.window)
        inputWindow.window.destroy()


def sum_dict(repeat=True):
    while repeat:
        save_logs(f'Ползователь выбрал операцию: {name4}')
        # вызов фукнции по созданию второго слагаемого словаря newDict1
        new_dict_to_sum()
        # сложение ихсодного словаря с созданным
        newDict.update(newDict1)
        save_logs(f'Ползователь сложил два словаря и получил результат: {newDict}')
        # функция повтора опепрации, выдает True, если введено Y
        messagebox.showinfo('Создание словаря', f"Вы сложили 2 словаря и получили словарь {newDict}",
                            master=inputWindow.window)
        inputWindow.window.destroy()
        repeat = repeat_func(name4, mainWindow.window)


def make_dict_unique():
    global newDict
    save_logs(f'Ползователь выбрал операцию: {name5}')
    # преобразование словаря в список формата [[],[],[]]
    newList = list(i for i in newDict.items())
    i = 0
    # ПОскольу i=0 берет первый список
    while i < len(newList):
        j = i + 1
        # сравнивает значение превого вложенного списка со всеми списками, по циклу проверяет все
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
    messagebox.showinfo('Уникальный словарь', 'Вы сделали словарь с уникальными значениями')
    save_logs('Ползователь удалил из словаря повторящиеся значения')


def clearDict():
    save_logs(f'Ползователь выбрал операцию: {name6}')
    if messagebox.askyesno("Очистка списка", 'Вы уверены, что хотите очистить словарь?'):
        newDict.clear()
        typeList = 'easy'
        save_logs('Пользователь очистил словарь')
        messagebox.showinfo('Очистка словаря', 'Вы очистили ваш словарь')


def quit():
    mainWindow.window.destroy()
    save_logs('Пользователь вышел в основное меню')
    import myProject
    myProject.main()


if __name__ == '__main__':
    main()
