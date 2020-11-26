from graphics import *
from tkinter import messagebox
import csv_logs

mainName = '<<<Работа с множествами>>>'
name1 = '<Добавление элементов в множество №1>'
name2 = '<Удаление элементов из множества>'
name3 = '<Логическое сложение, вычитание, умножение, симметричная разность>'
name4 = '<Проверка на входимость множеств (родитель-потомок)>'
endProgramm = '<Выход в главное меню>'

def main():
    inputWindow = CreateWindow('Создание множеств')
    inputWindow.lable('Для начала вам необходимо создать ваши множества')

    userInput = CreateInput(inputWindow.window, 1, 0, 'Введите через пробел элементы множества №1')
    userInput1 = CreateInput(inputWindow.window, 2, 0, 'Введите через пробел элементы множества №2')

    def check_input():
        global newSet, newSet1
        newSet = set([i for i in userInput.value.get().split()])
        newSet1 = set([i for i in userInput1.value.get().split()])
        csv_logs.save_logs(f'Ползователь создал 2 множества: №1 - {newSet}, №2 - {newSet1}')
        messagebox.showinfo("Создание множества",
                            f'Ваше множество номер 1 - {newSet}\nВаше множество номер 2 - {newSet1}')
        inputWindow.window.destroy()

    button = CreateButtons(inputWindow.window, 'Ввод', check_input)
    button.grid(3, 0, sticky='wens', columnspan=2)
    inputWindow.update_and_show_window()
    choose_method()

def choose_method():
    global mainWindow
    mainWindow = CreateWindow(mainName)
    mainWindow.lable('Выберите программу')
    b = {name1: add_to_newSet, name2: del_from_set, name3:main1,
         name4: parent_child, endProgramm: quit}
    for i, j in b.items():
        CreateButtons(mainWindow.window, i, j).pack(pady=5)
    mainWindow.update_and_show_window()

def add_to_newSet():
    csv_logs.save_logs(f'Ползователь выбрал операцию: {name1}')
    inputWindow = CreateWindow('Добавление элементов в множество')

    userInput = CreateInput(inputWindow.window, 1, 0, 'Введите через пробел элементы для множества №1')

    def check_input():
        elem = set([i for i in userInput.value.get().split()])
        newSet.update(elem)
        csv_logs.save_logs(f'Пользователь добавил элемент(-ы) "{elem}" в множество',
                           f'Ползователь получил в результате новое множество: "{newSet}"')
        messagebox.showinfo(None,f"Вы добавили {elem} в множество")
        inputWindow.window.destroy()

    button = CreateButtons(inputWindow.window, 'Ввод', check_input)
    button.grid(3, 0, sticky='wens', columnspan=2)
    inputWindow.update_and_show_window()
    csv_logs.save_logs(f'Операция {name1} завершена')

def del_from_set():
    csv_logs.save_logs(f'Ползователь выбрал операцию: {name2}')
    inputWindow = CreateWindow('Создание словаря')
    inputWindow.lable('Выберите элементы для удаления')
    inputWindow.lable.pack(fill=X, ipadx=10)
    fLeft = LabelFrame(master=inputWindow.window, text='Ваши значения в множестве')
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

    def del_from_set():
        values = []
        for i in lbox1.get(0, END):
            values.append(i)
            newSet.remove(i)
        messagebox.showinfo('Удаление элементов', f'Вы удалили из множества значения:\n {lbox1.get(0, END)}')
        csv_logs.save_logs(f'Пользователь удалил из множества значения:\n {lbox1.get(0, END)}')
        inputWindow.window.quit()

    btn = Button(fCenter, text='>>>', command=add_to_left_list)
    btn.pack(expand=1, anchor=S, pady=5)
    btn2 = Button(fCenter, text='<<<', command=add_to_right_list)
    btn2.pack(expand=1, anchor=N)
    btn3 = Button(fCenter, text='OK', command=del_from_set)
    btn3.pack(expand=1, anchor=N)
    for values in newSet:
        lbox.insert(END, values)
    inputWindow.update_and_show_window()
    inputWindow.window.destroy()
    csv_logs.save_logs(f'Операция {name2} завершена')


def main1():
    csv_logs.save_logs(f'Ползователь выбрал операцию: {name3}')
    global mainWindow1
    mainWindow1 = CreateWindow(mainName)
    mainWindow1.lable('Выберите логическую операцию')

    def logicMultiplication():
        csv_logs.save_logs(f'Пользователь запустил операцию <Логическое умножение>')
        csv_logs.save_logs(f'Пользователь получил результат: {newSet.intersection(newSet1)}')
        messagebox.showinfo('Логическое умножение',f"Результат: {newSet.intersection(newSet1)}")
        csv_logs.save_logs(f'Операция Логическое умножение завершена')

    def logicMinus():
        csv_logs.save_logs(f'Пользователь запустил операцию <Логическое вычитание>')
        csv_logs.save_logs(f'Пользователь получил результат: {newSet.difference(newSet1)}')
        messagebox.showinfo("Логическое вычитание",f"Результат: {newSet.difference(newSet1)}")
        csv_logs.save_logs(f'Операция Логическое вычитание завершена')

    def logicPlus():
        csv_logs.save_logs(f'Пользователь запустил операцию <Логическое сложение>')
        csv_logs.save_logs(f'Пользователь получил результат: {newSet.union(newSet1)}')
        messagebox.showinfo("Логическое сложение",f"Результат: {newSet.union(newSet1)}")
        csv_logs.save_logs(f'Операция Логическое сложение завершена')

    def simmetricMinus():
        csv_logs.save_logs(f'Пользователь запустил операцию <Симметричная разность>')
        csv_logs.save_logs(f'Пользователь получил результат: {newSet ^ newSet1}')
        messagebox.showinfo("Симметричная разность",f"Результат: {newSet ^ newSet1}")
        csv_logs.save_logs(f'Операция Симметричная разность завершена')

    b = {'<Логическое умножение>': logicMultiplication, "<Логическое вычитание>": logicMinus,
         "<Логическое сложение>": logicPlus, "<Симметричная разность>": simmetricMinus, "Назад": mainWindow1.window.destroy}
    for i, j in b.items():
        CreateButtons(mainWindow1.window, i, j).pack(pady=5)
    # mainWindow1.update_and_show_window()

def parent_child():
    csv_logs.save_logs(f'Пользователь запустил операцию {name4}')

    if newSet.issubset(newSet1):
        result = 'Ваше множество входит в множество №1'
    elif newSet.issuperset(newSet1):
        result = 'Множество №1 входит в ваше множество'
    else:
        result = 'Входимость не найдена'

    messagebox.showinfo('Вхождение множеств', result)

    csv_logs.save_logs(f'Пользователь получил результат: "{result}"')

def quit():
    mainWindow.window.destroy()
    csv_logs.save_logs('Пользователь вышел в основное меню')
    import myProject
    myProject.main()

if __name__ == '__main__':
    main()