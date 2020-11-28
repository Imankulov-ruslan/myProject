def main():
    global mainName, name1, name2, name3, name4
    mainName = '"Работа с кортежами"'
    name1 = '"Вывести первый и последний элемент кортежа"'
    name2 = '"Сумма и произведение элементов кортежа"'
    name3 = '"Проверка кортежа на уникальность"'
    name4 = '"Вывод четных и нечетных значений кортежа"'
    create_new_Tuple(True)
    number_input()

def print_tuple_menu():
    print(f'''
*****\t{mainName}\t*****
Выберите что нужно сделать с вашим кортежом:
1 - {name1}
2 - {name2}
3 - {name3}
4 - {name4}
0 - Выйти из программы "Работа с кортежами" в основное меню
Введите цифру от 0 до 5: ''', end='')

def number_input():
    while True:
        print_tuple_menu()
        number = input()
        if number == '1':
            save_logs(f'Ползователь выбрал операцию: {name1}')
            firs_last_tuple_elem(True)
        elif number == '2':
            save_logs(f'Ползователь выбрал операцию: {name1}')
            sum_multiplicate_tuple(True)
        elif number == '3':
            save_logs(f'Ползователь выбрал операцию: {name1}')
            unique_or_notunique_tuple(True)
        elif number == '4':
            save_logs(f'Ползователь выбрал операцию: {name1}')
            eval_notEval_in_tuple(True)
        elif number == '0':
            print(f'Программа {mainName} завершена')
            save_logs(f'Ползователь ввел 0 и завершил программу: {mainName}')
            break
        else:
            save_logs(f'Ползователь неверно ввел данные')
            print('Введите только числа от 0 до 6')


def create_new_Tuple(repeat):
    global newTuple
    while repeat:
        print('Для начала работы создайте ваш кортеж')
        newTuple = tuple(i for i in input('Введите элементы кортежа через пробел\n').split())
        print('Ваш кортеж - ', newTuple)
        save_logs(f'Пользователь создал кортеж: "{newTuple}"')
        repeat = continue_or_break('"Создание кортежа"')



def firs_last_tuple_elem(repeat):
    while repeat:
        message = f'Первый элемент кортежа -  {newTuple[0]}, Последний элемент кортежа {newTuple[len(newTuple) -1]}'
        print(message)
        save_logs(f'Пользователь получил результат: "{message}"')
        repeat = continue_or_break(name1)

def unique_or_notunique_tuple(repeat):
    while repeat:
        for i in newTuple:
            if newTuple.count(i) > 1:
                unique = True
            else:
                unique = False
        if unique:
            message = 'Ваш кортеж неуникальный'
        else:
            message = 'Ваш кортеж уникальный'
        print(message)
        save_logs(f'Пользователь получил результат: "{message}"')
        repeat = continue_or_break(name2)

def sum_multiplicate_tuple(repeat):
    while repeat:
        try:
            sum = 0
            multiplicate = 1
            for i in newTuple:
                sum += int(i)
                multiplicate *= int(i)
            message = f'Сумма всех элементов кортежа - {sum}, Произведение всех элементов кортежа - {multiplicate}'
            print(message)
        except:
            message = 'Не все значения в кортеже можно преобразовать в числа'
            print(message)
            break
        finally:
            save_logs(f'Ползователь получил результат: "{message}"')
        repeat = continue_or_break(name3)

def eval_notEval_in_tuple(repeat):
    while repeat:
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
            print(message,message1)
        except:
            message2 = 'Не все значения в кортеже можно преобразовать в числа'
            print(message2)
            save_logs(f'Пользователь получил результат: "{message2}"')
            break
        repeat = continue_or_break(name4)

if __name__ == '__main__':
    from numericalSequences import continue_or_break
    from work_with_set import save_logs
    main()
else:
    from numericalSequences import continue_or_break
    from work_with_set import save_logs

