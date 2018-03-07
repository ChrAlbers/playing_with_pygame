# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 21:25:42 2018

@author: Heinz

Description
This code is derived from and inspired by this blog post
http://trevorappleton.blogspot.de/2014/04/writing-pong-using-python-and-pygame.html
"""


# import pygame, import pygame locals which are variables storing values for
# keyboard events, for example

import pygame, sys
from pygame.locals import *

# Parameters for game behavior
FPS = 100
SPEEDFAC = 2            # Factor controling the speed (a factor on DT)
G = 100                 # Gravitational constant
DT = 1/FPS*SPEEDFAC     # Time increment
BESCH_BALL = 50         # Acceleration of ball on button press

# Parameters for appearance
WINDOWWIDTH = 800
WINDOWHEIGHT = 600
LINETHICKNESS = 15
BALLWIDTH = 20

# Defining some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# BIS = BALL IN SPACE, a dictionary containing all information of ball,
# location x, y and speed vx, vy
BIS = {"x": (WINDOWWIDTH - LINETHICKNESS)/2,
       "y": (WINDOWHEIGHT- LINETHICKNESS)/2,
       "vx": 1,
       "vy": 0}

def displayText(text, topleft):
    resultSurf = BASICFONT.render(text, True, WHITE)
    resultRect = resultSurf.get_rect()
    resultRect.topleft = topleft
    DISPLAYSURF.blit(resultSurf, resultRect)

def main():
    pygame.init()
    global DISPLAYSURF
    global BASICFONT, BASICFONTSIZE
    
    score = "A"
    
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption("GravPing")
    
    BASICFONTSIZE = 20
    BASICFONT = pygame.font.Font("freesansbold.ttf", BASICFONTSIZE)
    
    ball = pygame.Rect(round(BIS["x"]), round(BIS["y"]), BALLWIDTH, BALLWIDTH)
    ball_acc = "none"
    
    lower_edge = (WINDOWHEIGHT - LINETHICKNESS) # y-Koordinate der unteren Linie
    left_edge = LINETHICKNESS
    right_edge = WINDOWWIDTH - LINETHICKNESS
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    ball_acc = "left"
                if event.key == pygame.K_RIGHT:
                    ball_acc = "right"
                if event.key == pygame.K_SPACE:
                    BIS["vx"] = 0
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    ball_acc = "none"
                if event.key == pygame.K_RIGHT:
                    ball_acc = "none"
        
        DISPLAYSURF.fill((0, 0, 0))
        pygame.draw.rect(DISPLAYSURF, WHITE, ((0, 0),
                (WINDOWWIDTH, WINDOWHEIGHT)), LINETHICKNESS*2)

        pygame.draw.rect(DISPLAYSURF, WHITE, ball)
        
        BIS["vy"] += G*DT # Gravitationsbeschleunigung anwenden.
        
        # Collision with lower boundary
        pot_y = BIS["y"] + BALLWIDTH + BIS["vy"]*DT
        if pot_y > lower_edge:
            diff = lower_edge - (BIS["y"] + BALLWIDTH)
            BIS["y"] = lower_edge - (BIS["vy"]*DT + BALLWIDTH - diff) 
            BIS["vy"] *= -1 # Bounce in y-Richtung
            
        else:
            BIS["y"] += BIS["vy"]*DT
        
        
        if ball_acc == "left":
            BIS["vx"] -= BESCH_BALL*DT
        elif ball_acc == "right":
            BIS["vx"] += BESCH_BALL*DT
        
        # Collusion with left and right boundary
        pot_x_left = BIS["x"] + BIS["vx"]*DT
        if pot_x_left <= left_edge:
            diff = BIS["x"] - left_edge
            BIS["x"] = left_edge - diff - BIS["vx"]*DT 
            BIS["vx"] *= -1
        else:
            BIS["x"] += BIS["vx"]*DT
        
        pot_x_right = BIS["x"] + BIS["vx"]*DT + BALLWIDTH
        if pot_x_right >= right_edge:
            diff = right_edge - (BIS["x"] + BALLWIDTH)
            BIS["x"] = right_edge - (BIS["vx"]*DT - diff) - BALLWIDTH
            BIS["vx"] *= -1
        else:
            BIS["x"] += BIS["vx"]*DT
        
        

        BIS["x"] += BIS["vx"]*DT

        ball.x = round(BIS["x"])
        ball.y = round(BIS["y"])
        
        displayText(str(ball_acc), (WINDOWWIDTH - 150, 15))
        displayText(str(round(BIS["vx"], 3)), (WINDOWWIDTH - 150, 35))
        displayText(str(round(BIS["vy"], 3)), (WINDOWWIDTH - 75, 35))
        displayText("x: " + str(round(BIS["x"])) + ", y: " + str(round(BIS["y"])), (WINDOWWIDTH - 250, 55))
        displayText(str(round(pot_x_left)), (WINDOWWIDTH - 250, 75))
        displayText(str(LINETHICKNESS), (WINDOWWIDTH - 150, 75))
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        
if __name__ == "__main__":
    main()


