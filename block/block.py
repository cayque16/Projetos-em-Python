# -*- coding: utf-8 -*-
import pygame,time
from pygame.locals import *

BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

pygame.init()
width, heigth = 640, 480
screen = pygame.display.set_mode((width,heigth))
screen.fill(BLACK)

# colmeia
x = 52
y = 25
for i in range(1,65):
    pygame.draw.rect(screen,BLUE,[x,y,30,15])
    x += 32
    if i % 16 == 0:
        y += 17  
        x = 52
# player        
pygame.draw.rect(screen,WHITE,[0,440,80,15])
# bola
pygame.draw.ellipse(screen, RED, [width/2, heigth/2, 20, 20])
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    pygame.display.flip()



# o limite do objeto na tela deve ser calculado com base
# no seu tamanho