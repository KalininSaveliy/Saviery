from random import randrange as rnd, choice
import time


class Ball:
    def __init__(self, canvas, a, b, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.a = a
        self.b = b
        self.canv = canvas
        self.g = 3
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'orange', 'violet', 'gold'])
        self.id = self.canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color)
        self.live = 30
        self.time = 300

    def set_coords(self):
        self.canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r)

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if self.time == 0:
            self.canv.delete(self.id)
        dt = 1
        if self.x - self.r < 0 or self.x + self.r > self.a:
            self.vx *= -1
        if self.y - self.r < 0 :
            self.vy *= -1
        if self.y + self.r >= self.b:
            self.vy *= - 0.8
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.vy += self.g * dt
        self.set_coords()
        self.time -= 1

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (self.x - obj.x)**2 + (self.y - obj.y)**2 < (obj.r + self.r)**2:
            return True
        else:
            return False
