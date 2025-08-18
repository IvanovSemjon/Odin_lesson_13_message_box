import tkinter as tk

root = tk.Tk()
root.title("Арканоид")
root.attributes("-topmost", True)
canvas = tk.Canvas(root, width=400, height=400, bg="black")
canvas.pack()

paddle = canvas.create_rectangle(150, 350, 250, 370, fill="white")
ball = canvas.create_oval(190, 330, 210, 350, fill="red")

c=0
r=0
blocks = []
for i in range(4):
    for j in range(10):
        blocks.append(canvas.create_rectangle(c*50, r*30, c*50+45, r*30+25, fill="blue"))
        c+=1
    r+=1
    c=0

def move_paddle(event):
    pos = canvas.coords(paddle)
    if event.keysym == "Left" and pos[0] > 0:
        canvas.move(paddle, -20, 0)
    if event.keysym == "Right" and pos[2] < 400:
        canvas.move(paddle, 20, 0)



root.bind("<Key>", move_paddle)
root.mainloop()