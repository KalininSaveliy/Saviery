from tkinter import *
from random import randrange as rnd, choice

a = 800
b = 600
colors = ['red', 'orange', 'yellow', 'green', 'blue']
root = Tk()
root.geometry(str(a) + 'x' + str(b))
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)


class Ball:
    x = rnd(100, a - 100)
    y = rnd(100, b - 100)
    r = rnd(30, 50)
    dx = rnd(-7, 7)
    dy = rnd(-7, 7)
    color = choice(colors)
    canv.create_oval(x - r, y - r, x + r, y + r, fill=color, width=0)

    def move(self):
        print(self.r)
        #canv.move(self.ball, self.dx, self.dy)

    def chek_inside(self):
        pass

def main():
    ball = Ball
    print(ball.r)
    for i in range(100):
        ball.move()     # i do not know, please help with this f line
    mainloop()


main()
