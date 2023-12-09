import pygame as pg
import sys
import  random

FPS = 60

sc = pg.display.set_mode((700, 300))
clock = pg.time.Clock()

sc.fill((255, 255, 255))
mass = []
mas_B = []
mas_old_B = []

for i in range(26):
    mass.append(random.randint(0, 13))
    pg.draw.line(sc, (70, 70, 70), [30*i+10, 20*mass[i]+10], [30*i+10, 290], 2)

pg.draw.line(sc, (70, 70, 70), [10, 0], [10, 300], 2)
pg.draw.line(sc, (70, 70, 70), [0, 290], [700, 290], 2)
for i in range(15): pg.draw.circle(sc, (70, 70, 70), [11, 20 * i + 10], 3)
for i in range(26): pg.draw.circle(sc, (70, 70, 70), [30 * i + 11, 291], 3)
for i in range(1, 26): pg.draw.line(sc, (150, 70, 70), [30*i+10, 20*mass[i]+10], [30*(i-1)+10, 20*mass[i-1]+10], 2)
for i in range(0, len(mass) - 2, 2): mas_old_B.append([30*i+10, 20*mass[i]+10])

t = 0.05
T = 0

pg.display.update()
while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()

    if T <= 1:
        for i in range(0, len(mass)-2, 2):
            Q0 = [(1 - T) * 30*(i)+10 + T * 30*(i+1)+10, (1 - T) * 20*mass[i]+10 + T * 20*mass[i+1]+10]
            Q1 = [(1 - T) * 30*(i+1)+10 + T * 30*(i+2)+10, (1 - T) * 20*mass[i+1]+10 + T * 20*mass[i+2]+10]

            B = [round((1 - T) * Q0[0] + T * Q1[0]-10), round((1 - T) * Q0[1] + T * Q1[1]-10)]
            if i == 0 and T != 0:
                for i in range(len(mas_B)):
                    pg.draw.line(sc, (70, 150, 70), mas_old_B[i], mas_B[i], 4)
                mas_old_B = mas_B
                mas_B = []
            mas_B.append(B)
    if round(T, 2) == 1-t:
        for i in range(0, len(mass) - 2, 2): pg.draw.line(sc, (70, 150, 70), [30*(i+2)+10, 20*mass[i+2]+10], mas_B[int(i/2)], 4)
        for i in range(len(mas_B)): pg.draw.line(sc, (70, 150, 70), mas_old_B[i], mas_B[i], 4)
    T = T + t

    clock.tick(FPS)
    pg.display.update()