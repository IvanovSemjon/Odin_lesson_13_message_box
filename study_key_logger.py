import keyboard
import tkinter as tk
from tkinter import scrolledtext

def f():
    
    root = tk.Tk()
    root.title("Кейлогер")
    root.geometry("400x300")

    text_box = scrolledtext.ScrolledText(root, width=50, height=15)
    text_box.pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    print("Кейлогер запущен, нажмите Esc для остановки")
    f()

    
