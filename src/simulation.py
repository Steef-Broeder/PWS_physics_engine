from objects import *
import collision
import random

import pygame as pg

WIDTH = 600
HEIGHT = 480
FPS = 30

# Define Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

## initialize pg and create window
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Physics Simulation")
clock = pg.time.Clock()     ## For syncing the FPS

circles = []

def gen_circles(n):
    circles.clear()
    for i in range(n):
        circle1 = circle(surface=screen, x=random.randint(0,WIDTH), y=random.randint(0,HEIGHT), color=(random.randint(0,255),random.randint(0,255),random.randint(0,255)), radius=random.randint(0,50))
        circles.append(circle1)

## Game loop
running = True
while running:

    #1 Process input/events
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYUP:
            if event.key == pg.K_RETURN:
                gen_circles(40)

    #2 Update

    #3 Draw/render
    screen.fill(BLACK)

    for circle1 in circles:
        circle1.draw()

    ## Done after drawing everything to the screen
    pg.display.flip()       

pg.quit()