import tkinter as tk

# Создаем главное окно игры
root = tk.Tk()
root.title("Арканоид")
root.attributes("-topmost", True)

# Создаем игровое поле
canvas = tk.Canvas(root, width=400, height=400, bg="black")
canvas.pack()

# Создаем платформу
paddle = canvas.create_rectangle(150, 350, 250, 370, fill="white")

# Создаем шарик
ball = canvas.create_oval(190, 330, 210, 350, fill="red")

# Создаем блоки
blocks = []
for i in range(4):  # 4 ряда блоков
    for j in range(10):  # 10 блоков в ряду
        block = canvas.create_rectangle(j*40, i*20, j*40+38, i*20+18, fill="blue")
        blocks.append(block)

# Параметры игры
dx, dy = -3, -3  # Скорость шарика
ball_active = False  # Флаг активности шарика
game_started = False  # Флаг начала игры
game_over_text = None  # Текст проигрыша
win_text = None  # Текст победы

def move_ball():
    global dx, dy, ball_active, game_started, game_over_text, win_text
    
    if ball_active:
        canvas.move(ball, dx, dy)
    
        # Получаем координаты шарика
        x1, y1, x2, y2 = canvas.coords(ball)
        
        # Отскок от стен
        if x1 <= 0 or x2 >= 400:
            dx = -dx
        if y1 <= 0:
            dy = -dy
        
        # Отскок от платформы
        paddle_pos = canvas.coords(paddle)
        if (y2 >= paddle_pos[1] and y2 <= paddle_pos[3]) and \
           (x1 < paddle_pos[2] and x2 > paddle_pos[0]):
            dy = -dy
        
        # Проверка столкновения с блоками
        for block in blocks[:]:
            block_pos = canvas.coords(block)
            # Проверяем пересечение с блоком
            if (x2 > block_pos[0] and x1 < block_pos[2]) and \
               (y2 > block_pos[1] and y1 < block_pos[3]):
                canvas.delete(block)
                blocks.remove(block)
                dy = -dy
                break  # Прерываем цикл после первого столкновения
        
        # Проверка победы (не осталось блоков)
        if len(blocks) == 0:
            ball_active = False
            if win_text is None:
                win_text = canvas.create_text(200, 200, text="ВЫ ВЫИГРАЛИ!", font=("Arial", 30), fill="green")
            return
        
        # Проверка падения шарика
        if y2 >= 400:
            ball_active = False
            if game_over_text is None:
                game_over_text = canvas.create_text(200, 200, text="ВЫ ПРОИГРАЛИ", font=("Arial", 30), fill="red")
    
    root.after(30, move_ball)

def move_paddle(event):
    global ball_active, game_started, game_over_text, win_text
    
    # Удаляем сообщения при начале движения
    if game_over_text:
        canvas.delete(game_over_text)
        game_over_text = None
    if win_text:
        canvas.delete(win_text)
        win_text = None
    
    pos = canvas.coords(paddle)
    moved = False
    
    if event.keysym == "Left" and pos[0] > 0:
        canvas.move(paddle, -20, 0)
        moved = True
    elif event.keysym == "Right" and pos[2] < 400:
        canvas.move(paddle, 20, 0)
        moved = True
    
    # Активируем шарик при первом движении
    if moved and not game_started:
        ball_active = True
        game_started = True
    
    # Перезапуск игры после победы/проигрыша
    if moved and not ball_active:
        reset_game()

def reset_ball():
    global ball_active, game_started
    
    paddle_pos = canvas.coords(paddle)
    ball_x = (paddle_pos[0] + paddle_pos[2]) / 2 - 10
    canvas.coords(ball, ball_x, 330, ball_x + 20, 350)
    ball_active = False
    game_started = False

def reset_game():
    global blocks, ball_active, game_started, dx, dy
    
    # Очищаем старые блоки
    for block in blocks:
        canvas.delete(block)
    blocks = []
    
    # Создаем новые блоки
    for i in range(4):  # 4 ряда блоков
        for j in range(10):  # 10 блоков в ряду
            block = canvas.create_rectangle(j*40, i*20, j*40+38, i*20+18, fill="blue")
            blocks.append(block)
    
    # Сбрасываем шарик
    reset_ball()
    
    # Сбрасываем скорость
    dx, dy = -3, -3

# Начальная установка
reset_ball()
root.bind("<Key>", move_paddle)
move_ball()
root.mainloop()