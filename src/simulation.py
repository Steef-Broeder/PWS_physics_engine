from objects import *
import collision

import pygame as pg

WIDTH = 360
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


rectangle = rect(surface=screen, x=20, y=10, color=WHITE, mass=10, speed=10, friction=10, gravity=True, width=20, height=10)


## Game loop
running = True
while running:

    #1 Process input/events
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    #2 Update


    #3 Draw/render
    screen.fill(BLACK)



    ## Done after drawing everything to the screen
    pg.display.flip()       

pg.quit()