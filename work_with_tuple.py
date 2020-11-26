from graphics import *
from tkinter import messagebox
from csv_logs import save_logs

def main():
    global mainName, name1, name2, name3, name4, endProgramm
    mainName = '<<<Работа с кортежами>>>'
    name1 = '<Вывести первый и последний элемент кортежа>'
    name2 = '<Сумма и произведение элементов кортежа>'
    name3 = '<Проверка кортежа на уникальность>'
    name4 = '<Вывод четных и нечетных значений кортежа>'
    endProgramm = '<Выход в главное меню>'
    create_new_Tuple()
    print_tuple_menu()

def print_tuple_menu():
    global mainWindow
    mainWindow = CreateWindow(mainName)
    mainWindow.lable('Выберите программу')
    b = {name1:firs_last_tuple_elem, name2: sum_multiplicate_tuple, name3: unique_or_notunique_tuple,
         name4: eval_notEval_in_tuple, endProgramm: quit}
    for i, j in b.items():
        CreateButtons(mainWindow.window, i, j).pack(pady=5)
    mainWindow.update_and_show_window()


def create_new_Tuple():
    inputWindow = CreateWindow('Создание простого кортеж')
    inputWindow.lable('Введите данные для создания')

    userInput = CreateInput(inputWindow.window, 1, 0, 'Введите данные через пробел')

    def check_input():
        nonlocal inputWindow
        global newTuple
        newTuple = tuple(str(i) for i in userInput.value.get().split())
        messagebox.showinfo('Создание списка', f"Вы создали кортеж {newTuple}", master=inputWindow.window)
        save_logs(f'Пользователь создал кортеж: "{newTuple}"')
        inputWindow.window.destroy()

    btn = CreateButtons(inputWindow.window, 'Ввод', check_input)
    btn.grid(2, 0, sticky='nwse')
    inputWindow.update_and_show_window()

def firs_last_tuple_elem():
    save_logs(f'Ползователь выбрал операцию: {name1}')
    message = f'Первый элемент кортежа -  {newTuple[0]}, Последний элемент кортежа {newTuple[len(newTuple) -1]}'
    messagebox.showinfo(None, message)
    save_logs(f'Пользователь получил результат: "{message}"')

def unique_or_notunique_tuple():
    save_logs(f'Ползователь выбрал операцию: {name2}')
    for i in newTuple:
        if newTuple.count(i) > 1:
            unique = True
        else:
            unique = False
    if unique:
        message = 'Ваш кортеж неуникальный'
    else:
        message = 'Ваш кортеж уникальный'
    messagebox.showinfo(None, message)
    save_logs(f'Пользователь получил результат: "{message}"')

def sum_multiplicate_tuple():
    save_logs(f'Ползователь выбрал операцию: {name3}')
    try:
        sum = 0
        multiplicate = 1
        for i in newTuple:
            sum += int(i)
            multiplicate *= int(i)
        message = f'Сумма всех элементов кортежа - {sum}, Произведение всех элементов кортежа - {multiplicate}'
        messagebox.showinfo(None, message)
    except:
        message = 'Не все значения в кортеже можно преобразовать в числа'
        messagebox.showinfo(None, message)
    finally:
        save_logs(f'Ползователь получил результат: "{message}"')

def eval_notEval_in_tuple():
    save_logs(f'Ползователь выбрал операцию: {name4}')
    try:
        eval = []
        notEval = []
        for i in newTuple:
            if int(i) % 2 == 0:
                eval.append(i)
            else:
                notEval.append(i)
        if len(eval) == 0:
            message = 'В кортеже нет четных значений'
        else:
            message = f'Четные значения в кортеже -  {eval}'
        if len(notEval) == 0:
            message1 = 'В кортеже нет нечетных значений'
        else:
            message1 = f'Нечетные значения в кортеже - {notEval}'
        save_logs(f'Пользователь получил результат: "{message}", "{message1}"')
        messagebox.showinfo(None, f'{message}{message1}')
    except:
        message2 = 'Не все значения в кортеже можно преобразовать в числа'
        messagebox.showinfo(None, f'{message2}')
        save_logs(f'Пользователь получил результат: "{message2}"')

def quit():
    mainWindow.window.destroy()
    save_logs('Пользователь вышел в основное меню')
    import myProject
    myProject.main()

if __name__ == '__main__':
    main()


