import keyboard
import tkinter as tk
from tkinter import scrolledtext

def keylogger():
    
    root = tk.Tk()
    root.title("Кейлогер")
    root.geometry("400x300")
    root.attributes('-topmost', True)

    text_box = scrolledtext.ScrolledText(root, width=50, height=15)
    text_box.pack(pady=20)

    def on_key_event(event):
        key = event.name
        if key == "esc":
            root.destroy()
        else:
            text_box.insert(tk.END, key + " ")
            text_box.see(tk.END)

    keyboard.on_press(on_key_event)
    text_box.insert(tk.END, "Кейлогер запущен, нажмите Esc для остановки\n")

    root.mainloop()


    
