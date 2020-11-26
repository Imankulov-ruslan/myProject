from graphics import *
import csv_logs
from tkinter import messagebox

mainName = '<<<Работа с числами>>>'
name1 = '<Последовательность Фибоначчи>'
name2 = '<Таблица умножения>'
name3 = '<Факториал числа>'
name4 = '<Треугольное представление числа>'
name5 = '<Арифметическая прогрессия>'
name6 = '<Треугольник высотой N>'
endProgramm = "<Выход в главное меню>"

def main():
    print_sequence_menu()
# запуск функции (выводит меню для пользователя и просит ввод от пользователя)

def print_sequence_menu():
    global mainWindow
    mainWindow = CreateWindow(mainName)
    mainWindow.lable('Выберите программу')
    b = {name1: fibonachhiNumbers, name2: multiplicationTable, name3: numberFactorial,
         name4: triangleNumber, name5: arifmeticProgression, name6: nTriangle, endProgramm: quit}
    for i, j in b.items():
        CreateButtons(mainWindow.window, i, j).pack(pady=5)
    mainWindow.update_and_show_window()

# Функция "Последовательность Фибоначчи"
def fibonachhiNumbers():
    if name1 not in csv_logs.columns:
        csv_logs.columns.append(name1)
    csv_logs.save_logs(f'Пользователь запустил программу {name1}')
    # глобальная переменная, для суммирования шагов (кол-во вызовов пользователем программ)
    # первый элемент в посл-ти фибоначчи
    inputWindow = CreateWindow('Последовательность Фибоначчи')
    inputWindow.lable('Выберите кол-во элементов')
    inputWindow.lable.grid(row=0, column=0, columnspan=2, sticky='wens', ipady=5, ipadx=10, pady=5)
    userInput = Spinbox(master=inputWindow.window, from_=1, to=999)
    userInput.grid(row=1, column=1, pady=10, ipadx=10, ipady=10, sticky='wens')

    def check_input():
        nonlocal userInput
        number = int(userInput.get())
        f1 = 0
        # второй элемент в посл-ти фибоначчи
        f2 = 1
        if number == 1:
            a = ['0']
        elif number == 2:
            # если кол-во элементов 2 список с первыми двумя элементами
            a = ['0', '1']
        else:
            a = ['0', '1']
            for i in range(2, number):
                # третий элемент как сумма первого и второго 1 итерация (f3 = 0 + 1 = 1); 2-я f3 = 1 + 1 = 2
                f3 = f1 + f2
                # первому элементу присваивается значение второго 1 итерация f1 = 1;  2-я f1 = 1
                f1 = f2
                # второму элементу присваивается значение третьего 1 итерация f2 = 1;  2-я f2 = 2
                f2 = f3
                # Добавление в список элемента f3
                a.append(str(f3))
                # вывод списка в одну строку черезе метод join
                # запись строка в словарь, по ключу name1 запись производится в нужный столбец
                b = {name1: ' '.join(a)}
                csv_logs.values.append(b)
                #  в переменную repeat  присвоится True или False (по результатам return в функции continue_or_break)
        messagebox.showinfo('Ваша последовательность фибоначчи', f'{" ".join(a)}',master=inputWindow.window)
        inputWindow.window.destroy()

    button = CreateButtons(inputWindow.window, 'Ввод', check_input)
    button.grid(row=1, column=0, sticky='wens')
    inputWindow.update_and_show_window()


# Функция "Таблица умножения"
def multiplicationTable():
    if name2 not in csv_logs.columns:
        csv_logs.columns.append(name2)
    csv_logs.save_logs(f'Пользователь запустил программу {name2}')
    inputWindow = CreateWindow('Таблица умножения')
    inputWindow.lable('Выберите кол-во элементов')
    inputWindow.lable.grid(row=0, column=0, columnspan=2, sticky='wens', ipady=5, ipadx=10, pady=5)
    number = Spinbox(master=inputWindow.window, from_=2, to=999)
    number.grid(row=1, column=1, pady=10, ipadx=10, ipady=10, sticky='wens')

    def check_input():
        nonlocal number
        numbers = int(number.get())
        a = ''
        for i in range(1, numbers + 1):
            for j in range(1, numbers + 1):
                # добавление элементов в 1ю стороку таблицы умножения
                a += f'{i * j} \t'
            a += '\n\n'
        csv_logs.values.append({name2: a})
        messagebox.showinfo('Таблица умножения', a,master=inputWindow.window)
        inputWindow.window.destroy()

    button = CreateButtons(inputWindow.window, 'Ввод', check_input)
    button.grid(row=1, column=0, sticky='wens')
    inputWindow.update_and_show_window()


# Функция "Факториал числа"
def numberFactorial():
    if name3 not in csv_logs.columns:
        csv_logs.columns.append(name3)
    csv_logs.save_logs(f'Пользователь запустил программу {name3}')
    inputWindow = CreateWindow('Факториал числа')
    inputWindow.lable('Выберите кол-во элементов')
    inputWindow.lable.grid(row=0, column=0, columnspan=2, sticky='wens', ipady=5, ipadx=10, pady=5)
    number = Spinbox(master=inputWindow.window, from_=1, to=999)
    number.grid(row=1, column=1, pady=10, ipadx=10, ipady=10, sticky='wens')

    def check_input():
        i = 1
        global factorial
        factorial = 1
        while i <= int(number.get()):
            factorial *= i
            i += 1
        factorialDict = {name3: factorial}
        csv_logs.values.append({name3: factorialDict})
        messagebox.showinfo('Факториал числа', f"{name3} {number.get()} равен {factorial}",master=inputWindow.window)
        inputWindow.window.destroy()

    button = CreateButtons(inputWindow.window, 'Ввод', check_input)
    button.grid(row=1, column=0, sticky='wens')
    inputWindow.update_and_show_window()


# Функция "Треугольное представление числа"
def triangleNumber():
    if name4 not in csv_logs.columns:
        csv_logs.columns.append(name4)
    csv_logs.save_logs(f'Пользователь запустил программу {name4}')
    inputWindow = CreateWindow('Треугольное представление числа')
    inputWindow.lable('Выберите кол-во элементов')
    inputWindow.lable.grid(row=0, column=0, columnspan=2, sticky='wens', ipady=5, ipadx=10, pady=5)
    number = Spinbox(master=inputWindow.window, from_=1, to=9)
    number.grid(row=1, column=1, pady=10, ipadx=10, ipady=10, sticky='wens')

    def check_input():
        a = ''
        for i in range(1, int(number.get()) + 1):
            firstNumber = i
            secondNumber = (i + 1)
            thirdNumber = firstNumber * secondNumber
            triangleNumber = thirdNumber / 2
            # в строку добавляются все значения
            a += f'{i} {int(triangleNumber)}\n'
            csv_logs.values.append({name4: a})
        messagebox.showinfo('Треугольное представление числа', f"{a}",master=inputWindow.window)
        inputWindow.window.destroy()

    button = CreateButtons(inputWindow.window, 'Ввод', check_input)
    button.grid(row=1, column=0, sticky='wens')
    inputWindow.update_and_show_window()


# Арифметическая прогрессия
def arifmeticProgression():
    if name5 not in csv_logs.columns:
        csv_logs.columns.append(name5)
    inputWindow = CreateWindow('Арифметическая прогрессия')
    inputWindow.lable('Выберите первое число прогрессии:\nВыберите шаг прогрессии:\nВыберите кол-во элементов:')
    inputWindow.lable.grid(row=0, column=0, rowspan=3, sticky='wens', ipadx=10, pady=5, padx=5)

    number = Spinbox(master=inputWindow.window, from_=1, to=999)
    number.grid(row=0, column=1, sticky='wens', pady=5)

    number1 = Spinbox(master=inputWindow.window, from_=1, to=999)
    number1.grid(row=1, column=1, sticky='wens', pady=5)

    number2 = Spinbox(master=inputWindow.window, from_=1, to=999)
    number2.grid(row=2, column=1, sticky='wens', pady=5)

    def check_input():
        firstNumber = int(number.get())
        progressionStep = int(number1.get())
        quantity_of_number = int(number2.get())
        i = 1
        a = f'a1={str(firstNumber)} '
        while True:
            print('a', i, '=', firstNumber, sep='', end=' ')
            if i == quantity_of_number:
                break
            firstNumber += progressionStep
            a += f'a{i + 1}={str(firstNumber)} '
            i += 1
        messagebox.showinfo('Арифметическая прогрессия', f"{a}",master=inputWindow.window)
        csv_logs.values.append({name5: a})
        inputWindow.window.destroy()

    button = CreateButtons(inputWindow.window, 'Ввод', check_input)
    button.grid(row=3, column=0, sticky='wens', columnspan=2)

    inputWindow.update_and_show_window()

# Треугольник высотой N
def nTriangle():
    if name6 not in csv_logs.columns:
        csv_logs.columns.append(name6)
    csv_logs.save_logs(f'Пользователь запустил программу {name6}')
    inputWindow = CreateWindow('Арифметическая прогрессия')
    inputWindow.lable('Выберите число элементов')
    inputWindow.lable.grid(row=0, column=0, columnspan=2, sticky='wens', ipady=5, ipadx=10, pady=5)

    number = Spinbox(master=inputWindow.window, from_=1, to=20)
    number.grid(row=1, column=1, pady=10, ipadx=10, ipady=10, sticky='wens')

    def check_input():
        N = int(number.get())
        a = ''
        x = len(str(N)*N)
        for i in range(1, N + 1):
            a += f'{(str(i) * i).rjust(x)}\n'
        print(a)
        csv_logs.values.append({name6: a})
        messagebox.showinfo('Треугольник высотой N', a,master=inputWindow.window)
        inputWindow.window.destroy()

    button = CreateButtons(inputWindow.window, 'Ввод', check_input)
    button.grid(row=1, column=0, sticky='wens')
    inputWindow.update_and_show_window()

def quit():
    mainWindow.window.destroy()
    csv_logs.save_logs('Пользователь вышел в основное меню')
    import myProject
    myProject.main()

if __name__ == '__main__':
    main()
