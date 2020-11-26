from tkinter import *

class CreateWindow:
    def __init__(self, mainName):
        import tkinter
        self.window = tkinter.Tk()
        self.window.title(f'{mainName}')
        self.window['bg'] = 'gray75'

    def update_size(self):
        self.window.update_idletasks()
        s = self.window.geometry()
        s = s.split('+')
        s = s[0].split('x')
        width_root = int(s[0])
        height_root = int(s[1])
        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()
        w = w // 2
        h = h // 2
        w = w - width_root // 2
        h = h - height_root // 2
        self.window.geometry(f'+{w}+{h}')

    def update_and_show_window(self):
        self.update_size()
        self.window.mainloop()

    def lable(self, lable):
        self.lable=Label(master=self.window, text=lable, font=('Arial', 20, 'bold'), bd='0', relief='solid', bg='#FAE7B5',
              fg='#CB4154')

    def printMessage(self, title, message):
        from tkinter import messagebox
        messagebox.showinfo(title, message)

    def showWindow(self):
        self.window.mainloop()


class CreateInput:
    def __init__(self, master, row, column, lable, **kwargs):
        Label(master=master, text=lable, font=('Arial', 20, 'bold'), bd='0', relief='solid', bg='#FAE7B5',
              fg='#CB4154').grid(row=row, column=column, ipadx=10, ipady=6, padx=10, pady=10, sticky='we',
                                 **kwargs)
        self.value = Entry(master=master)
        self.value.grid(row=row, column=column + 1, sticky='wens', ipadx=10, ipady=6, padx=10,
                        pady=10)

class CreateButtons:
    def __init__(self, master, text, command):
        import tkinter
        self.name = tkinter.StringVar(master=master)
        self.name.set(text)
        self.button = tkinter.Button(master=master, textvariable=f'{self.name}', font=('Arial', 15),
                                     activebackground='#00FF00',
                                     bd='1', relief='raise',
                                     bg='#78DBE2', command=command)

    def pack(self, **kwargs):
        self.button.pack(expand=True, fill='x', **kwargs)

    def grid(self, row, column, **kwargs):
        self.button.grid(row=row, column=column, ipadx=10, ipady=5, padx=10, pady=10, **kwargs)
