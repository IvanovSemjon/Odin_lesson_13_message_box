import tkinter as tk
from tkinter import messagebox

def study_check_box():
    '''Изучение флажков'''
    window = tk.Toplevel()
    window.title('Чекбоксы')
    window.geometry('300x200')

    var_1 = tk.BooleanVar()
    var_2 = tk.BooleanVar()
    var_3 = tk.BooleanVar()

    tk.Label(window, text = 'Выберите языки: ').pack(pady=5)

    tk.Checkbutton(window, text='Python', variable=var_1).pack()
    tk.Checkbutton(window, text='Java', variable=var_2).pack()
    tk.Checkbutton(window, text='C++', variable=var_3).pack()


    def show_choice():
        langs = []

        if var_1.get():
            langs.append('Python')
        if var_2.get():
            langs.append('Java')
        if var_3.get():
            langs.append('C++')

        
        messagebox.showinfo("Результат", f"Выбраны: {', '.join(langs)}")

    tk.Button(window, text='Показать', command=show_choice).pack(pady=10)

