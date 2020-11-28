class Work_with_set:
    import csv_logs
    __mainName = '"Работа с множествами"'
    __name1 = '"Добавление элементов в множество №1"'
    __name2 = '"Удаление элементов из множества"'
    __name3 = '"Логическое сложение, вычитание, умножение, симметричная разность"'
    __name4 = '"Проверка на входимость множеств (родитель-потомок)"'

    def __init__(self):
        print('Для начала вам необходимо создать ваши множества')
        self.newSet = set([i for i in input('Введите элементы множества №1 через пробел\n').split()])
        self.newSet1 = set([i for i in input('Введите элементы множества №2 через пробел\n').split()])
        print(f'Ваше множество номер 1 - {self.newSet}\nВаше множество номер 2 - {self.newSet1}')
        Work_with_set.choose_method(self)

    def print_method(self):
        print(f'''*****\t{Work_with_set.__mainName}\t*****
Выберите метод для работы с элементом класса:
1 - {Work_with_set.__name1}
2 - {Work_with_set.__name2}
3 - {Work_with_set.__name3}
4 - {Work_with_set.__name4}
0 - Выйти из программы {Work_with_set.__mainName} в основное меню
Введите цифру от 0 до 4: ''', end='')

    def choose_method(self):
        while True:
            self.print_method()
            number = (input(''))
            print('')
            if number == '1':
                Work_with_set.csv_logs.save_logs(f'Ползователь выбрал операцию: {Work_with_set.__name1}')
                self.add_to_newSet(True)
            elif number == '2':
                Work_with_set.csv_logs.save_logs(f'Ползователь выбрал операцию: {Work_with_set.__name2}')
                self.del_from_set(True)
            elif number == '3':
                Work_with_set.csv_logs.save_logs(f'Ползователь выбрал программу: {Work_with_set.__name3}')
                self.choose_logic()
            elif number == '4':
                Work_with_set.csv_logs.save_logs(f'Ползователь выбрал операцию: {Work_with_set.__name4}')
                self.parent_child(True)
            elif number == '0':
                Work_with_set.csv_logs.save_logs(f'Ползователь ввел 0 и завершил программу: {Work_with_set.__mainName}')
                print(f'Программа {Work_with_set.__mainName} завершена')
                break
            else:
                Work_with_set.csv_logs.save_logs(f'Ползователь неверно ввел данные')
                print('Введите только числа от 0 до 4')
                continue


    def add_to_newSet(self,repeat):

        while repeat:
            quantity = input('Сколько элементов хотите добавить: 1 - один, 2 - множество элементов\n')
            if quantity == '1':
                elem = input('Введите элемент\n')
                self.newSet.add(elem)
            elif quantity == '2':
                elem = [i for i in input('Введите элементы через пробел\n').split()]
                self.newSet.update(elem)
            print('Ваше множество - ', self.newSet)
            Work_with_set.csv_logs.save_logs(f'Пользователь добавил элемент(-ы) "{elem}" в множество',
                                             f'Ползователь получил в результате новое множество: "{self.newSet}"')
            repeat = Work_with_set.csv_logs.continue_or_break(Work_with_set.__name1)

    def del_from_set(self,repeat):
        while repeat:
            print('Ваше множество - ', self.newSet)
            elem = input('Введите элемент для удаления\n')
            if elem in self.newSet:
                self.newSet.remove(elem)
                print('Элемент', elem, 'удален')
                Work_with_set.csv_logs.save_logs(f'Пользователь удалил элемент "{elem}" из множества')
            else:
                print('Такого элемента нет в вашем множестве')
                Work_with_set.csv_logs.save_logs(f'Пользователь ввел элемент "{elem}" которого нет в множестве {self.newSet}')
                continue
            print('Ваше множество - ', self.newSet)
            Work_with_set.csv_logs.values.append({'del_set_elem': self.newSet})
            Work_with_set.csv_logs.columns.append('del_set_elem')
            repeat = Work_with_set.csv_logs.continue_or_break(Work_with_set.__name2)

    def print_logic_menu(self):
        number = input('''Выберите какую логическую операцию произвести с множеством:
1 - Логическое умножение (пересечение)
2 - Логическое вычитание
3 - Логическое сложение
4 - Симметричная разность
0 - Выйти из программы  в основное меню
Введите число от 0 до 4: ''')
        return number


    def choose_logic(self):
        while True:
            number = self.print_logic_menu()
            if number == '1':
                self.logicMultiplication = self.newSet.intersection(self.newSet1)
                print('Логическое умножение вашего множество с множеством №1', self.logicMultiplication)
                Work_with_set.csv_logs.save_logs('Ползователь выбрал операцию: Логическое умножение',
                          f'Ползователь получил результат: "{self.logicMultiplication}"')
            elif number == '2':
                self.logicMinus = self.newSet.difference(self.newSet1)
                print('Логическое вычитание вашего множество с множеством №1', self.logicMinus)
                Work_with_set.csv_logs.save_logs('Ползователь выбрал операцию: Логическое вычитание',
                          f'Ползователь получил результат: "{self.logicMinus}"')
            elif number == '3':
                self.logicPlus = self.newSet.union(self.newSet1)
                print('Логическое сложение вашего множество с множеством №1', self.logicPlus)
                Work_with_set.csv_logs.save_logs('Ползователь выбрал операцию: Логическое сложение',
                          f'Ползователь получил результат: "{self.logicPlus}"')
            elif number == '4':
                self.simmetricMinus = self.newSet ^ self.newSet1
                print('Симметричная разность вашего множество с множеством №1', self.simmetricMinus)
                Work_with_set.csv_logs.save_logs('Ползователь выбрал операцию: Симметричная разность',
                          f'Ползователь получил результат: "{self.simmetricMinus}"')
            elif number == '0':
                print('Программа \"Логические операции с множествами\" завершена')
                Work_with_set.csv_logs.save_logs('Ползователь ввел 0 и вышел в главное меню')
                break
            else:
                print('Введите только числа от 0 до 4\n')
                Work_with_set.csv_logs.save_logs('Ползователь ввел неверные данные, необходимо вводить данные числа от 0 до 4')
                continue
            if input('Введите Y для повторения\n').lower() == 'y':
                continue
            print('')

    def parent_child(self,repeat):
        while repeat:
            if self.newSet.issubset(self.newSet1):
                result = 'Ваше множество входит в множество №1'
            elif self.newSet.issuperset(self.newSet1):
                result = 'Множество №1 входит в ваше множество'
            else:
                result = 'Входимость не найдена'
            print(result)
            Work_with_set.csv_logs.save_logs(f'Пользователь получил результат: "{result}"')
            repeat = Work_with_set.csv_logs.continue_or_break(Work_with_set.__name4)

    def print_result(self):
        print(self.newSet1, self.newSet1, self.logicPlus, self.logicMultiplication)