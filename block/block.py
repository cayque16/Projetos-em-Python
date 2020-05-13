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
colmeia = []
for i in range(1,65):
    colmeia.append(pygame.Rect(x,y,30,15))
    x += 32
    if i % 16 == 0:
        y += 17  
        x = 52
# player        
player = pygame.Rect(0,440,80,15)
# bola
bola = pygame.Rect(width//2,heigth//2,20,20)
velocidade = [0.1,0.1]
clock = pygame.time.Clock()
while True:
    dt = clock.tick(30)
    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        break

    bola.move_ip(velocidade[0]*dt,velocidade[1]*dt)
    if bola.left < 0 or bola.right > width:
        velocidade[0] = -velocidade[0]
    if bola.top < 0 or bola.bottom > heigth:
        velocidade[1] = -velocidade[1]

    screen.fill(BLACK)

    # desenha a bola
    pygame.draw.ellipse(screen,RED,bola)
    # desenha o player
    pygame.draw.rect(screen,WHITE,player)
    #desenha a colmeia
    for bloco in colmeia:
        pygame.draw.rect(screen, BLUE, bloco)

    pygame.display.flip()