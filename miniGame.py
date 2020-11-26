from tkinter import messagebox
from graphics import *
import csv_logs
import myProject

def main():
    miniGame()
 

def miniGame():
    import random
    number = random.randint(1, 10)
    inputWindow = CreateWindow('УгадайКа')
    inputWindow.lable('Попробуйте угадать число от 1 до 10')
    inputWindow.lable.grid(columnspan=2)
    guessNumber = CreateInput(inputWindow.window, 1, 0, 'Введите число в поле')
    i = 0

    def check_input():
        nonlocal i
        try:
            Number = int(guessNumber.value.get())
            guessNumber.value.delete(0, END)
            i += 1
            if Number > number:
                messagebox.showinfo(None, 'Ваше число больше загаданного')
            if Number < number:
                messagebox.showinfo(None, 'Ваше число меньше загаданного')
            if Number == number:
                messagebox.showinfo(None, 'Мои поздравления!!! Вы победили!!!')
                csv_logs.save_logs('Пользователь победил в игре')
                inputWindow.window.destroy()
            elif i == 3:
                messagebox.showinfo(None, 'ВЫ ПРОИГРАЛИ!!!')
                csv_logs.save_logs('Позователь проиграл в игре')
                inputWindow.window.destroy()
            elif i < 3:
                messagebox.showinfo(None, f'Осталось попыток: {3 - i}')

        except ValueError:
            messagebox.showerror(None, 'Вводите только числа')

    btn = CreateButtons(inputWindow.window, 'Guess!', check_input)
    btn.grid(2, 0, sticky='wsne')

    btn = CreateButtons(inputWindow.window, 'Exit', inputWindow.window.destroy)
    btn.grid(2, 1, sticky='wsne')

    inputWindow.update_and_show_window()

    myProject.main()

if __name__ == '__main__':
    main()

