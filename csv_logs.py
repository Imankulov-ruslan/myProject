# универсальная функция записывает в csv файл
values, columns = [], []

def csv_logs():
    global values, columns
    import csv
    with open(r'C:\Users\rusel\PycharmProjects\My project\programmLogs\numericalSequences.csv', 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=columns, delimiter=';')
        writer.writeheader()
        for i in values:
            writer.writerow(i)
    values.clear(), columns.clear()

def decorator(func):
    OPENFILE = r'C:\Users\rusel\PycharmProjects\My project\programmLogs\logs.txt'

    def inner(*args, **kwargs):
        decor()
        func(OPENFILE, *args, **kwargs)
        decor()

    def decor():
        with open(OPENFILE, 'a', encoding='utf-8') as writeFile:
                writeFile.write(('*' * 10).center(50))
                writeFile.write('\n')

    return inner

@decorator
def save_logs(OPENFILE, *source):
    from datetime import datetime
    now = datetime.now()
    with open(OPENFILE, 'a', encoding='utf-8') as writeFile:
        for log in source:
            writeFile.write(f'Время запуска {now}')
            writeFile.write('\n')
            writeFile.write(log)
            writeFile.write('\n')


def continue_or_break(name_of_programm):
    # универсальная функция для повтора любой программы, в параметр name_of_programm
    # передается в виде аргумента имя программы
    programmRepeat = input('\nДля повторения данной программы введите Y,\nдля выхода любую клавишу\n')
    if programmRepeat.lower() == 'y':
        # запись в логи информации о повторе операции
        save_logs(f'Пользователь повторил операцию: {name_of_programm}')
        return True
    print(f'Программа {name_of_programm} завершена\n')
    # запись в логи информации о завершении операции
    save_logs(f'Пользователь завершил операцию: {name_of_programm}')
    return False
