from tkinter import *
from random import randrange as rnd, choice


a = 800
b = 600
colors = ['red', 'orange', 'yellow', 'green', 'blue']
root = Tk()
root.geometry(str(a) + 'x' + str(b))
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)
score = 0
text = canv.create_text(50, 50, text='Score: ' + str(score))
kol_balls = 500     # количество шаров
balls = []


class Ball:
    def __init__(self):
        self.x = rnd(100, a - 100)
        self.y = rnd(100, b - 100)
        self.r = rnd(30, 50)
        self.dx = rnd(-5, 5)
        self.dy = rnd(-5, 5)
        self.color = choice(colors)
        self.id = canv.create_oval(self.x - self.r, self.y - self.r,
                                   self.x + self.r, self.y + self.r,
                                   fill=self.color, width=0)

    def move(self):
        if self.x - self.r < 0 or self.x + self.r > a:
            self.dx *= -1
        if self.y - self.r < 0 or self.y + self.r > a:
            self.dy *= -1
        canv.move(self.id, self.dx, self.dy)
        self.x += self.dx
        self.y += self.dy

    def check_inside(self, event):
        if (self.x - event.x) ** 2 + (self.y - event.y) ** 2 < self.r ** 2:
            return True
        else:
            return False


def move_balls():
    dt = 1
    for i in balls:
        i.move()
    root.after(dt, move_balls)


def click(event):
    global score, text
    for i in balls:
        if i.check_inside(event):
            score += 1
            canv.delete(text)
            text = canv.create_text(50, 50, text='Score: ' + str(score))


def main():
    for i in range(kol_balls):
        balls.append(Ball())
    move_balls()
    canv.bind('<Button>', click)
    mainloop()

main()
