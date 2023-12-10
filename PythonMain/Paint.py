import pygame as pg
pg.init()
import sys, random

mainClock = pg.time.Clock()
pg.display.set_caption("Cube")
from pygame.locals import *

height = 800
width = 1600
screen = pg.display.set_mode((height, width),0,32)

squareSize = 50
cellSize = squareSize
extraSpace = 1.5


white = (255, 255, 255)
black = (0, 0, 0)
grey = (240, 240, 240)
green = (0, 255, 0)
blue = (0, 0, 128)
red = (128, 0, 0)

squareAttributes = []
squareColor = []
squareLocation = []
squareWidth = []

color = red

for i in range(0, width, cellSize):
        for j in range(0, height, cellSize):
            squareColor.append((white))
            squareLocation.append((j, i, squareSize, squareSize))
            squareWidth.append(1)
            squareAttributes.append([squareColor[-1], squareLocation[-1], squareWidth[-1]])

while True:

    mx, my = pg.mouse.get_pos()
    screen.fill("black")

    for square in squareAttributes:
        pg.draw.rect(screen, square[0], square[1], square[2])


    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        if event.type == KEYDOWN:
                if event.key ==  K_ESCAPE:
                    pg.quit()
                    sys.exit()
                if event.key == K_1:
                     color = red
                if event.key == K_2:
                     color = green
                if event.key == K_3:
                     color = blue
                if event.key == K_4:
                     color = white
                if event.key == K_5:
                     color = black
                

        if event.type == MOUSEBUTTONDOWN:
            mx, my = event.pos
            for square in squareAttributes:
                x, y, square_width, square_height = square[1]
                if x <= mx <= x + square_width and y <= my <= y + square_height:
                    if square[2] != 0:
                        square[2] = 0
                        square[0] = color
                    
                    else:
                         square[2] = 1
                         square[0] = white


    pg.display.update()
    mainClock.tick(60)

