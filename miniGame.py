def main():
    miniGame()

def miniGame():
    while True:
        import random
        number = random.randint(1, 10)
        i = 1
        print('У вас будет три попытки, попробуйте уагадать число от 1 до 10')
        while i <= 3:
            try:
                guessNumber = int(input('Введите число: '))
            except ValueError:
                print('Вводите только числа')
                continue
            if guessNumber > number:
                print('Ваше число больше загаданного')
            elif guessNumber < number:
                print('Ваше число меньше загаданного')
            elif guessNumber == number:
                print('Мои поздравления! Вы победили!')
                csv_logs.save_logs('Позователь победил в игре')
                break
            if i < 3:
                print(f'У вас осталось {3 - i} попыток')
            i += 1
            if i == 4:
                print('Ваши попытки кончились. Вы проиграли!')
                csv_logs.save_logs('Позователь проиграл в игре')
                break
        repeat = input('Повторим еще раз?\nНажмите Y для продолжения: ')
        if repeat.lower() == 'y':
            continue
        else:
            print('Программа "Мини игра" завершена')
            break

if __name__ == '__main__':
    main()
    import csv_logs
else:
    import csv_logs