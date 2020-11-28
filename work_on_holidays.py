# Функция "Запись сотрудников на выходные"
def work_on_holidays():
    from csv_logs import save_logs
    programmRepeat = 'repeat'
    while programmRepeat == "repeat":
            work_on_weekend = input("Будете работать в выходные? Введите Да\Нет: ")
            if work_on_weekend == 'Да':
                while True:
                    try:
                        day_to_work = int(input('Вы будете работать в субботу или в воскресенье? 1 - суббота, 2 - воскресенье '))
                        if day_to_work == 1:
                            day_to_work = 'в субботу'
                        elif day_to_work == 2:
                            day_to_work = 'в воскресенье'
                        else:
                            raise ZeroDivisionError('Введите только 1 или 2')
                        save_logs(f'Пользователь выбрал работу {day_to_work}')
                        while True:
                            name_of_worker = input("Введите ваше имя: ")
                            save_logs(f'Ползователь ввел имя: "{name_of_worker}"')
                            surname_of_worker = input("Введите вашу фамилию: ")
                            save_logs(f'Ползователь ввел фамилию: "{surname_of_worker}"')
                            time_to_work = input('Введите время работы в формате \"чч:мм-чч:мм\" ')
                            save_logs(f'Ползователь ввел время работы: "{time_to_work}"')
                            project_to_do = input("Введите название проекта: ")
                            save_logs(f'Ползователь ввел название проекта: "{project_to_do}"')
                            print(name_of_worker, surname_of_worker, "- выход", day_to_work, time_to_work, "\nРабота для выполнения:", project_to_do)
                            save_logs(f'Пользователь получил результат:\n'
                                      f'Имя работника: "{name_of_worker}", Фамилия работника: "{surname_of_worker}"\n'
                                      f'Выход: "{day_to_work}" , Время работы: "{time_to_work}"\n'
                                      f'Работа для выполнения: "{project_to_do}"')
                            break
                    except ZeroDivisionError as e:
                        print(e)
                        continue
                    except ValueError:
                        print("Введите только 1 или 2")
                        continue
                    break
            elif work_on_weekend == 'Нет':
                save_logs('Пользователь не будет работать в выходные')
                print('Хорошего отдыха!')
            else:
                print("Введите только Да или Нет")
                continue
            programmRepeat = input("Для повторения программы \"Запись сотрудников на выходные\" введите repeat ")
    print("Программа \"Запись сотрудников на выходные\" завершена")

if __name__ == '__main__':
    work_on_holidays()

