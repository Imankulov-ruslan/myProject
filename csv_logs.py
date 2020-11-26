# универсальная функция записывает в csv файл
values, columns = [], []

def csv_logs():
    global values, columns
    import csv
    with open(r'C:\Users\rusel\PycharmProjects\My project_v1\programmLogs\numericalSequences.csv', 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=columns, delimiter=';')
        writer.writeheader()
        for i in values:
            writer.writerow(i)
    values.clear(), columns.clear()

def decorator(func):
    OPENFILE = r'C:\Users\rusel\PycharmProjects\My project_v1\programmLogs\logs.txt'

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
def save_logs(OPENFILE, *args):
    from datetime import datetime
    now = datetime.now()
    with open(OPENFILE, 'a', encoding='utf-8') as writeFile:
        for log in args:
            writeFile.write(f'Время запуска {now}')
            writeFile.write('\n')
            writeFile.write(log)
            writeFile.write('\n')

