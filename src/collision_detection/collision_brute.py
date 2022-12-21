import pygame as pg
import random, sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import circle 

screen = None
screen_width = None
screen_height = None

def setup(surface:pg.Surface, width:int, height:int):
    global screen, screen_width, screen_height
    screen = surface
    screen_width = height
    screen_height = height

def create_circles(circle_amount:int, circle_radius:int) -> list[circle.circle]:
    circles = [circle.circle]
    for i in range(circle_amount):
        x = (circle_radius*2) * i
        y = (circle_radius*2) * i
        circlex = circle.circle(screen, x, y, (200, 0, 200), circle_radius)
        circles.append(circlex)
    return circles