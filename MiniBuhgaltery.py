def main():
    chooseMethod()

class MiniBuhgaltery:
    FILENAME = r'C:\Users\rusel\PycharmProjects\My project\programmLogs\hours.csv'

    def __init__(self):
        self.__name = input('Введите имя\n')
        self.__lastName = input('Введите фамилию\n')
        self.__position = input('Введите должность\n')
        while True:
            try:
                self.__rate_per_hour = int(input('Введите ставку\n'))
            except ValueError:
                print('При введении ставки вводите только числа')
                continue
            break

    @property
    def name(self):
        return self.__name, self.__lastName

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

    @property
    def rate_per_hour(self):
        return self.__rate_per_hour

    @rate_per_hour.setter
    def rate_per_hour(self, value):
            self.__rate_per_hour = value

    def writeHours(self):
        try:
            self.__hours = float(input('Введите кол-во часов\n'))
            import csv
            with open(MiniBuhgaltery.FILENAME, 'w', newline='') as file:
                write = csv.DictWriter(file, delimiter=';', fieldnames=[self.__name])
                write.writeheader()
                write.writerow({self.__name: self.__hours})
        except ValueError as e:
            return e
        return f" Вы внесли {self.__hours} рабочих часов в табель"


    def calculateSalary(self):
        import csv
        with open(MiniBuhgaltery.FILENAME, 'r', newline='') as file:
            read = csv.DictReader(file, delimiter=';')
            for row in read:
                try:
                    hours = row[self.__name]
                    salary = float(hours) * self.__rate_per_hour
                    return f'Зарплата в этом месяце: {salary} рублей'
                except KeyError:
                    return 'Сначала введите рабочие часы в табель'




    def __str__(self):
        return f'Имя {self.__name} Фамилия {self.__lastName}'

def chooseMethod():
    print('Вы создали экземпляр класса')
    name = MiniBuhgaltery()
    while True:
        print('''Выберите что сделать с экземпляром вашего класса:
1 - Вывести Имя и Фамилию
2 - Вывести должность
3 - Вывести часовую ставку
4 - Сменить часовую ставку
5 - Занести рабочие часы в табель
6 - Вывести расчет месячной зарплаты
0 - Выйти в основное меню''')
        number = input()
        if number == '1':
            print(*name.name)
        elif number == '2':
            print(name.position)
        elif number == '3':
            print(f' Вы изменили ставку на {name.rate_per_hour}')
        elif number == '4':
            try:
                name.rate_per_hour = int(input('Введите новую ставку\n'))
                print(name.rate_per_hour)
            except ValueError:
                print('Введены неверные данные')
        elif number == '5':
            print(name.writeHours())
        elif number == '6':
            print(name.calculateSalary())
        elif number == '0':
            break
        else:
            print('Вводите только числа от 0 до 6')
            continue


if __name__ == '__main__':
    main()




