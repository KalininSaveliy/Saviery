from tkinter import *
from random import randrange as rnd, choice

def main():
        # Создем окно, запускаем шарики
    begin()    # окно
    ball()     # запускаем шарики на арену
    canv.bind('<Button-1>', click)
    mainloop()
def begin():
    """Создаем главное окно, вводим основные переменные"""
    global root, canv, colors, text, score, a, b
    score = 0   # Счет
    kol_ball = 3    # Количество шаров
    mas_ball = []   # характеристика каждого мяча (координаты, радиус, цвет, скорость)
        # Создание главного окна
    a = 800    # Для соударения со стенкой надо знать размеры окна (a и b), а root.geometry('...') какая-то мутная херь
    b = 600
    root = Tk()    # да, это и есть главное окно
    root.geometry('800x600')    # размеры главного окна (ширина и высота или наоборот :( )
        # Чертяга
    canv = Canvas(root, bg='white')    # Место для рисования
    canv.pack(fill=BOTH,expand=1)   # Какие-то его свойства, растягивает по ширине окна и че-то еще
        # бла-бла-бла
    colors = ['red','orange','yellow','green','blue']   # Возможные цвета шаров
    text = canv.create_text(100, 100, text='Score: {}'.format(score))   # Создание текстового поля для учета очков
    canv.addtag_withtag("text", text)   # Это вообще крутая тема: создание тега и присваивание его элементу
def ball():
        # Создаем несколько шариков, заставляем их работать
    global ball, livetime, x, y, r, vx, vy  # Сам шарик и его основные хар-ки (время жизни, координаты, радиус, скорость по осям)
    livetime = 1000    # Примерное время жизни шарика. Да-да, он умрет
    new_ball_time = 1000    # Время появления нового шарика
    x = rnd(100, 700)
    y = rnd(100, 500)
    r = rnd(30, 50)
    vx = rnd(-7, 7)    # Скорость шарика по осям
    vy = rnd(-7, 7)
    ball = canv.create_oval(x-r,y-r , x+r,y+r, fill = choice(colors), width=0)    # Создаем шарик
    move_ball()    # Сдвигаем шарик
    print('Пока все ок')  # доп чекалка
    #root.after(new_ball_time, ball)    # Закидаываем новый шарик через new_ball_time милисекунд
def move_ball():
        # Движение и соударение шарика
    global livetime, vx, vy, x, y    # Все те же координаты
    dt = 1    # Время поменьше, и никто ничего не заметит
    livetime -= dt
    dx = vx * dt / 30   # Изменение коородинат за dt
    dy = vy * dt / 30
    x += dx    # Новые координаты шарика. Это нужно для ф-ции click, так как не знаю, как найти координаты обЪекта в любой момент времени
    y += dy
    if x < 0 or x > a:  # Не надо спрашивать, меня почему он частично улетает за стенку. Код написано нормально, наверное. Шарик вообще должен не долетать до нее, тем более там время 1 милисекунда
        vx *= (-1)
    if y < 0 or y > b:
        vy *= (-1)
    canv.move(ball, dx, dy)    # Функция смещения
    if livetime >= 0:
        root.after(dt, move_ball)   # Однократный вызов move_ball через dt
    else:
        canv.delete(ball)
def click(event):
        # Меняет счет, если ткнули в шарик мышкой
    global score, text  # Напоминаю для тех, кто скачет по моему коду, text - поле для вывода очков
    if (x - event.x)**2 + (y - event.y)**2 <= r**2:
        score += r / 10
            # Стираем старые очки и пишем новые (хз, как сделать по-человечески, но это вариант хотя бы работает)
        canv.delete('text')
        text = canv.create_text(100, 100, text='Score: {}'.format(score))
        canv.addtag_withtag("text", text)
        # "Аааа, что за треш, какой нафиг tag" - загляни в функцию begin
        #print(r / 10)  # Тут бывают проблема с очками (много знаков после запятой), не знаю почему так :(


main()