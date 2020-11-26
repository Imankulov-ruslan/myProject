from graphics import *
from csv_logs import save_logs
from csv_logs import csv_logs
import logsReader

mainName, name1, name2, name3, name4, name5, name6, name7, name8, endProgramm = \
    '<<<My project>>>', '<Работа с числами>', '<Запись сотрудников на выходные>', '<Работа со списками>', '<Работа со словарями>', \
    '<Работа с кортежами>', '<Работа с множествами>', '<Мини игра>', '<Активировать класс МиниБухгалтерия>', '<Завершить программу>'

def main():
    global mainWindow
    mainWindow = CreateWindow(mainName)
    mainWindow.lable('Выберите программу')
    b = {name1: start_numericalSequences, name3: start_work_with_list,
         name4: start_work_with_dict, name5: start_work_with_tuple, name6: start_work_with_set,
         name7: start_miniGame, endProgramm: quit}
    for i, j in b.items():
        CreateButtons(mainWindow.window, i, j).pack(pady=5)
    mainWindow.update_and_show_window()

def start_numericalSequences():
    import numericalSequences  # импорт модуля
    save_logs(f'******\tПользователь запустил программу "{name1}"\t******')  # строка запишется в логи txt
    mainWindow.window.destroy()
    numericalSequences.main()  # вызов главной функции из модуля по работе с числами

def start_work_with_list():
    import work_with_list
    save_logs(f'******\tПользователь запустил программу "{name3}"\t******')
    mainWindow.window.destroy()
    work_with_list.main()


def start_work_with_dict():
    import work_with_dict
    save_logs(f'******\tПользователь запустил программу "{name4}"\t******')
    mainWindow.window.destroy()
    work_with_dict.main()


def start_work_with_tuple():
    import work_with_tuple
    save_logs(f'******\tПользователь запустил программу "{name5}"\t******')
    mainWindow.window.destroy()
    work_with_tuple.main()


def start_work_with_set():
    import work_with_set
    save_logs(f'******\tПользователь запустил программу "{name6}"\t******')
    mainWindow.window.destroy()
    work_with_set.main()


def start_miniGame():
    import miniGame
    save_logs(f'******\tПользователь запустил программу "{name7}"\t******')
    mainWindow.window.destroy()
    miniGame.miniGame()

def quit():
    csv_logs()
    save_logs(f'******\tПолзователь завершил работу с программой {mainName}!\t******')
    logsReader.main()
    mainWindow.window.destroy()

if __name__ == '__main__':
    main()

