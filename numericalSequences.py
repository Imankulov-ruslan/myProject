
def main():
    # глобальные переменные, прим-ся во всех функциях в данном методе
    global mainName,name1,name2,name3,name4,name5,name6,step,columns
    mainName = '"Работа с числами"'
    name1 = '"Последовательность Фибоначчи"'
    name2 = '"Таблица умножения"'
    name3 = '"Факториал числа"'
    name4 = '"Треугольное представление числа"'
    name5 = '"Арифметическая прогрессия"'
    name6 = '"Треугольник высотой N"'
    # запуск функции (выводит меню для пользователя и просит ввод от пользователя)
    print_sequence_menu()

def continue_or_break(name_of_programm):
    # универсальная функция для повтора любой программы, в параметр name_of_programm
    # передается в виде аргумента имя программы
    from csv_logs import save_logs
    programmRepeat = input('\nДля повторения данной программы введите Y,\nдля выхода любую клавишу\n')
    if programmRepeat.lower() == 'y':
        # запись в логи информации о повторе операции
        save_logs(f'Пользователь повторил операцию: {name_of_programm}')
        return True
    print(f'Программа {name_of_programm} завершена\n')
    # запись в логи информации о завершении операции
    save_logs(f'Пользователь завершил операцию: {name_of_programm}')
    return False

def print_sequence_menu():
    # вывод меню в консоль и ввод от пользователя
    while True:
        chooseSequence = input(f'''
*****\t{mainName}\t*****
Выберите операцию, которую хотите запустить:
1 - {name1}
2 - {name2}
3 - {name3}
4 - {name4}
5 - {name5}
6 - {name6}
0 - Завершить программу {mainName}
Введите цифру от 0 до 6: ''')
        if chooseSequence == '1':
            # запись логов
            csv_logs.save_logs(f'Пользователь ввел 0 и завершил программу: {name1}')
            # вызов функции, аргумент True - программа циклична до прерывания пользователем
            fibonachhiNumbers(True)
        elif chooseSequence == '2':
            csv_logs.save_logs(f'Пользователь ввел 0 и завершил программу: {name2}')
            multiplicationTable(True)
        elif chooseSequence == '3':
            csv_logs.save_logs(f'Пользователь ввел 0 и завершил программу: {name3}')
            numberFactorial(True)
        elif chooseSequence == '4':
            csv_logs.save_logs(f'Пользователь ввел 0 и завершил программу: {name4}')
            triangleNumber(True)
        elif chooseSequence == '5':
            csv_logs.save_logs(f'Пользователь ввел 0 и завершил программу: {name5}')
            arifmeticProgression(True)
        elif chooseSequence == '6':
            csv_logs.save_logs(f'Пользователь ввел 0 и завершил программу: {name6}')
            nTriangle(True)
        elif chooseSequence == '0':
            csv_logs.csv_logs()
            print(f"Программа {mainName} завершена")
            break
        else:
            print("Введите только числа от 0 до 6")
            continue

 # Функция "Последовательность Фибоначчи"
 # при вызове функции в repeat передается True, в FILENAME путь к файлу логов
def fibonachhiNumbers(repeat):
    if name1 not in csv_logs.columns:
        csv_logs.columns.append(name1)
    # глобальная переменная, для суммирования шагов (кол-во вызовов пользователем программ)
    while repeat:
        # первый элемент в посл-ти фибоначчи
        f1 = 0
        # второй элемент в посл-ти фибоначчи
        f2 = 1
        try:
            number = int(input('Введите кол-во чисeл: '))
            if number <= 0:
                print('Введите число больше нуля')
                continue
            elif number == 1:
                a = ['0']
            elif number == 2:
                # если кол-во элементов 2 список с первыми двумя элементами
                a = ['0','1']
            else:
                a = ['0','1']
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
            print("Ваша последовательность фибоначчи: ", ' '.join(a))
            # запись строка в словарь, по ключу name1 запись производится в нужный столбец
            b = {name1: ' '.join(a)}
            csv_logs.values.append(b)
            #  в переменную repeat  присвоится True или False (по результатам return в функции continue_or_break)
            repeat = continue_or_break(name_of_programm=name1)
        except ValueError:
            print('Введите число, а не строку')

# Функция "Таблица умножения"
def multiplicationTable(repeat):
    if name2 not in csv_logs.columns:
        csv_logs.columns.append(name2)
    while repeat:
        try:
            a = ''
            numbers = int(input('Введите число, до которого необходима таблица: '))
            if numbers <= 0:
                print('Введите число больше нуля')
                continue
            for i in range(1, numbers + 1):
                for j in range(1, numbers + 1):
                    # добавление элементов в 1ю стороку таблицы умножения
                    a += f'{i * j} \t'
                a += '\n\n'
            print(a)
            csv_logs.values.append({name2:a})
            repeat = continue_or_break(name_of_programm=name2)
        except:
            print('Введите число, а не строку')
            continue



# Функция "Факториал числа"
def numberFactorial(repeat):
    if name3 not in csv_logs.columns:
        csv_logs.columns.append(name3)
    while repeat:
        try:
            number = int(input("Введите число: "))
            if number <= 0:
                raise ZeroDivisionError('Введите число больше нуля')
            i = 1
            factorial = 1
            while i <= number:
                factorial *= i
                i += 1
            print(name3, number, "равен", factorial)
            factorialDict = {name3:factorial,'step':step}
            csv_logs.values.append({name3:factorialDict})
            repeat = continue_or_break(name_of_programm=name3)
        except ValueError:
            print('Введите число, а не строку')
        except ZeroDivisionError as e:
            print(e)


# Функция "Треугольное представление числа"
def triangleNumber(repeat):
    if name4 not in csv_logs.columns:
        csv_logs.columns.append(name4)
    while repeat:
        try:
            number = int(input("Введите число: "))
            a = ''
            if number <= 0:
                raise ZeroDivisionError('Введите число больше нуля')
            for i in range(1, number + 1):
                firstNumber = i
                secondNumber = (i + 1)
                thirdNumber = firstNumber * secondNumber
                triangleNumber = thirdNumber / 2
                # в строку добавляются все значения
                a += f'{i} {int(triangleNumber)}\n'
            print(a)
            csv_logs.values.append({name4:a})
            repeat = continue_or_break(name_of_programm=name4)
        except ZeroDivisionError as e:
            print(e)
        except:
            print('Введите число, а не строку')

# Арифметическая прогрессия
def arifmeticProgression(repeat):
    if name5 not in csv_logs.columns:
        csv_logs.columns.append(name5)
    while repeat:
        try:
            firstNumber = int(input('Введите первое число прогрессии: '))
            progressionStep = int(input('Введите шаг прогрессии: '))
            quantity_of_number = int(input('Введите кол-во шагов: '))
            if quantity_of_number <= 0:
                raise Exception
            i = 1
            a = f'{str(firstNumber)} '
            while True:
                print('a', i, '=', firstNumber, sep='', end=' ')
                if i == quantity_of_number:
                    break
                firstNumber += progressionStep
                a += f'{str(firstNumber)} '
                i += 1
            csv_logs.values.append({name5:a})
            repeat = continue_or_break(name_of_programm=name5)
        except ValueError:
            print('Введите только целые числа')
            continue
        except Exception:
            print('Введите число больше нуля')
            continue

# Треугольник высотой N
def nTriangle(repeat):
    if name6 not in csv_logs.columns:
        csv_logs.columns.append(name6)
    while repeat:
        try:
            N = int(input('Введите высоту трегольника: '))
            a = ''
            for i in range(1, N + 1):
                a += f'{(str(i) * i).rjust(N+1)}\n'
            print(a)
            csv_logs.values.append({name6:a})
            repeat = continue_or_break(name_of_programm=name6)
        except ValueError:
            print('Введите только целые числа')
            continue

if __name__ == '__main__':
    import csv_logs
    import csv
    main()
else:
    import csv_logs
    import csv
