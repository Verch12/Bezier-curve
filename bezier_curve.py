import pygame as pg
import sys
 
FPS = 60

sc = pg.display.set_mode((500, 500))
clock = pg.time.Clock()
 
sc.fill((255, 255, 255))

P0 = [50, 350]
P1 = [150, 450]
P2 = [300, 100]
P3 = [100, 120]

t = 0.1
T = 0

pg.display.update()
 
while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
    
    pg.draw.circle(sc, (255, 0, 255), P0, 3)
    pg.draw.line(sc, (0,0,0), P0, P1, 2)
    pg.draw.circle(sc, (255, 0, 255), P1, 3)
    pg.draw.line(sc, (0,0,0), P1, P2, 2)
    pg.draw.circle(sc, (255, 0, 255), P2, 3)

    if T <= 1:
        Q0 = [(1-T)*P0[0]+T*P1[0], (1-T)*P0[1]+T*P1[1]]
        Q1 = [(1-T)*P1[0]+T*P2[0], (1-T)*P1[1]+T*P2[1]]

        R0 = [(1-T)*Q0[0]+T*Q1[0], (1-T)*Q0[1]+T*Q1[1]]


        pg.draw.circle(sc, (0, 0, 255), R0, 3)

    T = T+t

    clock.tick(FPS)
    pg.display.update()
