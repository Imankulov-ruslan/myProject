def main():
    from csv_logs import save_logs  # импорт функции, записывающей логи в файл txt
    import logsReader  # импорт модуля, для чтения всех логов и вывода в консоль
    while True:
        chooseProgramm = input(f'''
*****\tMy project\t*****
Выберите программу, которую хотите запустить:
1 - Работа с числами
2 - Запись сотрудников на выходные
3 - Работа со списками
4 - Работа со словарями
5 - Работа с кортежами
6 - Работа с множествами
7 - Мини игра
8 - Активировать класс МиниБухгалтерия
0 - Завершить программу
Введите число от 0 до 8: ''')
        if chooseProgramm == "1":
            import numericalSequences  # импорт модуля
            save_logs('******\tПользователь запустил программу "Работа с числами"\t******') # строка запишется в логи txt
            numericalSequences.main()  # вызов главной функции из модуля по работе с числами
        elif chooseProgramm == "2":
            import work_on_holidays
            save_logs('******\tПользователь запустил программу "Запись сотрудников на выходные"\t******')
            work_on_holidays.work_on_holidays()
        elif chooseProgramm == "3":
            import work_with_list
            save_logs('******\tПользователь запустил программу "Работа со списками"\t******')
            work_with_list.main()
        elif chooseProgramm == "4":
            import work_with_dict
            save_logs('******\tПользователь запустил программу "Работа со словарями"\t******')
            work_with_dict.main()
        elif chooseProgramm == "5":
            import work_with_tuple
            save_logs('******\tПользователь запустил программу "Работа с кортежами"\t******')
            work_with_tuple.main()
        elif chooseProgramm == "6":
            import work_with_set
            save_logs('******\tПользователь запустил программу "Работа с множествами"\t******')
            yourSet = work_with_set.Work_with_set()
        elif chooseProgramm =='7':
            import miniGame
            save_logs('******\tПользователь запустил программу "Угадай-Ка"\t******')
            miniGame.miniGame()
        elif chooseProgramm == '8':
            import MiniBuhgaltery
            MiniBuhgaltery.main()
        elif chooseProgramm == "0":
            break
        else:
            print("Введите только число от 0 до 6\n")
            continue
    save_logs(f'******\tПолзователь завершил работу с программой MyProject!\t******')
    logsReader.main() # вызов функции по чтению и выводу логов в консоль
    print('Программа MyProject завершена\n','Удачного дня!')

if __name__ == '__main__':
    main()


# отдельный txt файл с описанием программы
