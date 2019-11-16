import ball_m
import math
from random import randrange as rnd
import tkinter as tk
import time


class Gun:
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20, 450, 50, 420, width=7)   # FIXME: don't know how to set it...

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = ball_m.Ball(canv, a, b)
        new_ball.r += 5
        self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy =  self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y-450) / (event.x-20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an),
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class Target(ball_m.Ball):
    def __init__(self, canvas, a, b):
        super().__init__(canvas, a, b)
        self.points = 0
        self.live = 1
        self.vx = rnd(-5, 5)
        self.vy = rnd(-5, 5)
        self.time = -1
        self.g = 0
        # FIXME: don't work!!! How to call this functions when object is created?
        #self.id = canv.create_oval(0, 0, 0, 0)
        self.id_points = canv.create_text(30, 30, text=self.points, font='28')

    def new_target(self):
        """ Инициализация новой цели. """
        self.x = rnd(600, 780)
        self.y = rnd(300, 550)
        self.r = rnd(2, 50)
        self.color = 'red'
        canv.coords(self.id, self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r)
        canv.itemconfig(self.id, fill=self.color)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points
        canv.itemconfig(self.id_points, text=self.points)


def main():
    global canv, target, gun, a, b, text, root, bullet, balls, targets, count_target
    count_target = 2
    a = 800
    b = 600
    root = tk.Tk()
    root.geometry(str(a) + 'x' + str(b))
    canv = tk.Canvas(root, bg='white')
    canv.pack(fill=tk.BOTH, expand=1)
    text = canv.create_text(400, 300, text='', font='28')
    gun = Gun()
    bullet = 0
    balls = []
    new_game()


def new_game():
    global gun, target, text, balls, bullet, root, targets, count_target, a, b
    targets = []
    for t in range(count_target):
        targets.append(Target(canv, a, b))
    for t in targets:
        t.new_target()
    bullet = 0
    balls = []
    canv.bind('<Button-1>', gun.fire2_start)
    canv.bind('<ButtonRelease-1>', gun.fire2_end)
    canv.bind('<Motion>', gun.targetting)

    z = 0.03
    for t in targets:
        t.live = 1
        while t.live or balls:
            t.move()
            for ball in balls:
                ball.move()
                if ball.hittest(t) and t.live:
                    t.live = 0
                    t.hit()
                    canv.bind('<Button-1>', '')
                    canv.bind('<ButtonRelease-1>', '')
                    canv.itemconfig(text, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
                    for i in balls:
                        canv.delete(i.id)
                    balls = []
                    for ta in targets:
                        canv.delete(ta.id)
            canv.update()
            time.sleep(z)
            gun.targetting()
            gun.power_up()
        break
    time.sleep(0.7)
    canv.itemconfig(text, text='')
    canv.delete(gun)
    root.after(1, new_game)


main()
tk.mainloop()
