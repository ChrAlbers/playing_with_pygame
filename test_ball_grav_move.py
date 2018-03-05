# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 21:25:42 2018

@author: Heinz

Beschreibung
Leitet sich von diesem Pong-Tutorial ab: 
http://trevorappleton.blogspot.de/2014/04/writing-pong-using-python-and-pygame.html
"""

# pygame importen, locals importen. Die locals sind Codes für einige Events,
# wie z.B. bestimmte Tasten, Mausbewegung und so weiter.
import pygame, sys
from pygame.locals import *

# Faktor, um die Geschwindigkeit zu erhöhen
SPEEDFAC = 2

FPS = 100

WINDOWWIDTH = 800
WINDOWHEIGHT = 600
LINETHICKNESS = 10

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

G = 100 # Gravitationskonstante
DT = 1/FPS*SPEEDFAC

# BIS = BALL IN SPACE, x, y, und vx, vy, also alle Ball-Informationen in einem
# Dictionary
BIS = {"x": (WINDOWWIDTH - LINETHICKNESS)/2,
       "y": (WINDOWHEIGHT- LINETHICKNESS)/2,
       "vx": 1,
       "vy": 0}

def main():
    pygame.init()
    global DISPLAYSURF
    global G
    
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption("GravPing")
    
    ball = pygame.Rect(round(BIS["x"]), round(BIS["y"]), LINETHICKNESS, LINETHICKNESS)
    
    lower_edge = (WINDOWHEIGHT - LINETHICKNESS) # y-Koordinate der unteren Linie
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        DISPLAYSURF.fill((0, 0, 0))
        pygame.draw.rect(DISPLAYSURF, WHITE, ((0, 0),
                (WINDOWWIDTH, WINDOWHEIGHT)), LINETHICKNESS*2)

        pygame.draw.rect(DISPLAYSURF, WHITE, ball)
        
        BIS["vy"] += G*DT # Gravitationsbeschleunigung anwenden.
        
        # Für die Kollisionsabfrage mit der unteren Kante die Position des
        # unteren Ballrandes einen Zeitschritt weiter projezieren
        pot_y = BIS["y"] + LINETHICKNESS + BIS["vy"]*DT
        
        # Falls die untere Kante des Balls tiefer liegt als die obere Kante der
        # unteren Begrenzung, dann muss der Ball bouncen unter der Annahme
        # konstanten Geschwindigkeitsbetrages, d.h. er ist nach dem Bounce so
        # hoch wie die Differenz von y - v_y*dt über der unteren Begrenzung.
        if pot_y > lower_edge:
            diff = lower_edge - (BIS["y"] + LINETHICKNESS)
            BIS["y"] = lower_edge - (BIS["vy"]*DT + LINETHICKNESS - diff) 
            # BIS["y"] = BIS["vy"]*DT - (BIS["y"] - lower_edge)
            # BIS["y"] = lower_edge - LINETHICKNESS
            BIS["vy"] *= -1 # Bounce in y-Richtung
            
        else:
            BIS["y"] += BIS["vy"]*DT
        
        
        BIS["x"] += BIS["vx"]*DT

        ball.x = round(BIS["x"])
        ball.y = round(BIS["y"])
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        
if __name__ == "__main__":
    main()


