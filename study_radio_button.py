import tkinter as tk
from tkinter import messagebox

def study_radio_button():
    '''Изучение радиокнопок'''
    window = tk.Toplevel()
    window.title('Радиокнопки')
    window.geometry('300x200')

    var = tk.StringVar(value='Python')

    tk.Label(window, text = 'Выберите язык: ').pack(pady=5)
    tk.Radiobutton(window, text='Python', variable=var, value='Python').pack()
    tk.Radiobutton(window, text='Java', variable=var, value='Java').pack()
    tk.Radiobutton(window, text='C++', variable=var, value='C++').pack()


    def show_choice():
        messagebox.showinfo("Результат", f"Выбран: {var.get()}")

    tk.Button(window, text='Показать', command=show_choice).pack(pady=10)

