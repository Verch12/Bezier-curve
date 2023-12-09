import pygame as pg
import sys

FPS = 60

sc = pg.display.set_mode((500, 500))
clock = pg.time.Clock()
 
sc.fill((255, 255, 255))

mass = []
mas = []

t = 0.02
T = 1
Q = 0

pg.display.update()
while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()

        if i.type == pg.MOUSEBUTTONDOWN and i.button == 1:
            sc.fill((255, 255, 255))
            mass.append(i.pos)
            for i in range(1, len(mass)):
                pg.draw.line(sc, (0, 0, 0), mass[i], mass[i-1], 2)
            for i in mass:
                pg.draw.circle(sc, (255, 0, 255), i, 4)
            mas_vr = [mass] + [[]] * (len(mass) - 1)
            T = 0
            pg.time.delay(10)

        elif i.type == pg.MOUSEBUTTONDOWN and i.button == 3:
            mass = []
            mas_vr = []
            sc.fill((255, 255, 255))
            pg.time.delay(10)
            T = 1

    if T < 1:
        for q in range(len(mass)-1):
            for b in range(len(mass) - q-1):
                mas.append([(1-T)*mas_vr[q][b][0]+T*mas_vr[q][b+1][0], (1-T)*mas_vr[q][b][1]+T*mas_vr[q][b+1][1]])
            mas_vr[q+1] = mas
            mas = []
        pg.draw.circle(sc, (0, 0, 255), mas_vr[len(mass)-1][0], 3)
        T = T + t

    clock.tick(FPS)
    pg.display.update()