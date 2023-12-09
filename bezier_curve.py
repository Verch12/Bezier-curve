import pygame as pg
import sys
 
FPS = 60

sc = pg.display.set_mode((1000, 1000))
clock = pg.time.Clock()
 
sc.fill((255, 255, 255))

P0 = [450, 350]
P1 = [100, 500]
P2 = [400, 720]
P3 = [100, 720]

mass = [P0, P1, P2, P3]

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
    pg.draw.line(sc, (0,0,0), P2, P3, 2)
    pg.draw.circle(sc, (255, 0, 255), P3, 3)

    if T <= 1:
        Q0 = [(1-T)*P0[0]+T*P1[0], (1-T)*P0[1]+T*P1[1]]
        Q1 = [(1-T)*P1[0]+T*P2[0], (1-T)*P1[1]+T*P2[1]]
        #Q2 = [(1-T)*P2[0]+T*P3[0], (1-T)*P2[1]+T*P3[1]]

        R0 = [(1-T)*Q0[0]+T*Q1[0], (1-T)*Q0[1]+T*Q1[1]]
        #R1 = [(1-T)*Q1[0]+T*Q2[0], (1-T)*Q1[1]+T*Q2[1]]

        #B = [(1-T)*R0[0]+T*R1[0], (1-T)*R0[1]+T*R1[1]]

        print('-----------------------------------------------------------------------------------------------111111111111')
        #print(Q0,Q1,Q2)
        print('-----------------------------------------------------------------------------------------------')
        #print(R0,R1)
        print('-----------------------------------------------------------------------------------------------')
        #print(B)

        pg.draw.circle(sc, (0, 0, 255), R0, 3)

        #print(T)
    #T = round(T+t, 2)
    T = T+t

    clock.tick(FPS)
    pg.display.update()
