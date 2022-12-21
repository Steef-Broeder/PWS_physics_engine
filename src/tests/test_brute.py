import pygame as pg
import random, sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import circle 
import collision_detection.collision_brute as collision_brute

WIDTH = 840
HEIGHT = 600
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
pg.display.set_caption("Simulation")
clock = pg.time.Clock()     ## For syncing the FPS

#Setup
collision_brute.setup(screen, WIDTH, HEIGHT)
circles = collision_brute.create_circles(20, 10)

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

    for circlex in circles:
        circlex.draw()

    ## Done after drawing everything to the screen
    pg.display.flip()       

pg.quit()