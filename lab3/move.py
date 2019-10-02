from graph import *
from math import *

time = 0
dt = 100

def main0():
    global time
    xship = time/10 
    xwave = 10*cos(time/2)
    main(500, 400, 'cyan', 'blue', 'yellow', xwave, 20, 2 * pi / 4, 440, 60, 40, 50, 50, 15, 10, 'white', xship,230, 'brown', 'grey',
         60, 300, 'red')
    time += dt
def main(a,b,sky,water,send,xwave,rwave,alpha,xsun,ysun,rsun,xcloud,ycloud,oa,ob,cloudcolor,xship,yship,shipcolor,sail,xumb,yumb,umbcolor):
    background(a,b,sky,water,send)
    sun(xsun, ysun, rsun)
    wave(a,xwave,b*3/4,rwave,alpha,water,send)
    cloud(xcloud,ycloud,oa,ob,cloudcolor)
    cloud(xcloud+150,ycloud+20,oa+5,ob+3,cloudcolor)
    ship(xship,yship,shipcolor,sail,1)
    ship(xship-150, yship-20, shipcolor, sail, 0.5)
    umbrella(xumb,yumb,umbcolor,1)
    umbrella(xumb+100, yumb+20, umbcolor, 0.6)
def background(a,b,sky,water,send):
    """Основной фон (небо, вода, песок)."""
    windowSize(a, b)
    brushColor(sky)
    rectangle(0, 0, a, b / 2)
    brushColor(water)
    rectangle(0, b / 2, a, 3 * b / 4)
    brushColor(send)
    rectangle(0, 3 * b / 4, a, b)
def sun(x,y,r):
    """Рисует солнышко с лучиками. Параметры лучиков и цвет внутри функции"""
    suncolor = 'yellow'
    penColor(suncolor)
    brushColor(suncolor)
    circle(x,y,r)
def wave(a,x,y,r,alpha,water,send):
    penSize(0.000005)
    """Рисует волнистое разделение между водой и песком"""
    l = 2*r*sin(alpha/2)    # l - длина по X одной дуги
    k = int(a // l + 1)     # k - количество дуг на экране; про b читай ниже
    for i in range(k):
        arc(x, y+r*cos(alpha/2), r,alpha,send)
        rearc(x, y+r*cos(alpha/2), r,alpha,water)
        x += 2*l
def arc(x,y,r,alpha,send):
    penColor(send)
    """Нужно для функции wave (песок)"""
    a = [(x, y)]
    n = 50
    for i in range(1, n + 1):
        a.append((x - r * sin(alpha / 2 - i * alpha / n), y - r * cos(alpha / 2 - i * alpha / n)))
    a.append((x, y))
    brushColor(send)
    polygon(a)
def rearc(x,y,r,alpha,water):
    penColor(water)
    """Нужно для функции wave (вода)"""
    rex = x + 2*r*sin(alpha/2)
    rey = y - 2*r*cos(alpha/2)
    a = [(rex, rey)]
    n = 50
    for i in range(1, n + 1):
        a.append((rex - r * sin(alpha / 2 - i * alpha / n), rey + r * cos(alpha / 2 - i * alpha / n)))
    a.append((rex, rey))
    brushColor(water)
    polygon(a)
def cloud(x,y,oa,ob,cloudcolor):
    for i in range(3):
        oval(x,y,oa,ob,cloudcolor)
        x += 25
    for i in range(4):
        oval(x-15,y+10,oa,ob,cloudcolor)
        x -= 25
def oval(x0,y0,oa,ob,cloudcolor):
    penColor('black')
    brushColor(cloudcolor)
    mas = []
    n = 100
    for i in range(n):
        x = x0 + oa*cos(2*i*pi/n)
        y = y0 - ob*sin(2*i*pi/n)
        mas.append((x,y))
    polygon(mas)
def ship(x,y,shipcolor,sail,shipsize):
    brushColor(shipcolor)
    l = 150*shipsize # длина прямоуголтника
    h = 30*shipsize  # высота прямоугльника
    d = 20*shipsize  # сдвиг паруса
    k = 2/3 # отношения прямоугольной части корабля к его длине без дуги
    rectangle(x,y , x+l*k,y+h)
    polygon([ (x+l*k,y) , (x+l*k,y+h) , (x+l,y) , (x+l*k,y) ])

    A = [(x,y)]
    n = 10
    for i in range(n+1):
        A.append((x - h * cos(i * pi / (2*n)), y + h * sin(i * pi / (2*n))))
    A.append((x,y))
    polygon(A)

    R = (-sqrt((l*(1-k))**2 + (h)**2) + l*(1-k) + h) / 2
    brushColor('black')
    circle(x+l*k+R , y+R , R*0.75)
    brushColor('white')
    circle(x+l*k+R , y+R , R*0.5)

    penSize(8*shipsize)
    line(x+l*k/2,y , x+l*k/2,y-l*k*k)

    brushColor(sail)
    penSize(1)
    polygon([(x+l*k/2,y) , (x+l*k/2+d,y-l*k*k/2) , (x+l*k/2+d+d,y-l*k*k/2) , (x+l*k/2,y)])
    polygon([(x + l * k / 2, y-l*k*k), (x + l * k / 2 + d, y - l * k * k / 2), (x + l * k / 2 + d + d, y - l * k * k / 2),
             (x + l * k / 2, y-l*k*k)])
def umbrella(x,y,umbcolor,umbsize):
    l = 100*umbsize
    h = 80*umbsize
    k = 1/4 # оттношение длины ручки зонтика к его полной длине
    penSize(5*umbsize)
    penColor('brown')
    line(x,y , x,y+l*(1-k))
    penSize(1)
    penColor('black')
    brushColor(umbcolor)
    n = 8
    for i in range(n):
        polygon([(x,y-l*k), (x-h/2 + i*h/n, y), (x-h/2 +10 + i*h/n, y), (x,y-l*k)])

onTimer(main0, dt)

# Тесты:
#oval(440,60,10,10,'white')

run()