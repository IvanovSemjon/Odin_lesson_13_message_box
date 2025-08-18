import tkinter as tk
from tkinter import messagebox


def study_entry():
    window = tk.Toplevel()
    window.title('Поля ввода')
    window.geometry('300x200')

    tk.Label(window, text='Имя: ').pack(pady=5)
    entry_1 = tk.Entry(window)
    entry_1.pack(pady=5)    

    tk.Label(window, text='Пароль: ').pack(pady=5)
    entry_2 = tk.Entry(window, show='*')
    entry_2.pack(pady=5)

    def show_values():
        messagebox.showinfo('Результат', 
                            f'Имя: {entry_1.get()}\nПароль: {entry_2.get()}')
        
    
    tk.Button(window, text='Показать значениe', command=show_values).pack(pady=10)