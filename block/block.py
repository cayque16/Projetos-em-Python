# -*- coding: utf-8 -*-
import pygame,time
from pygame.locals import *

# cores
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
# movimentos do player
DIREITA = 1
ESQUERDA = 2
# dimensoes do player
PL_POS_X = 0 # posicicao inicial do player no eixo X
PL_POS_Y = 440 # posicao inicial do player no eixo y
PL_WIDTH = 80 # largura do player
PL_HEIGTH = 15 # altura do player
PL_MOVIMENTO = 100 # tamanho do movimento do player
# dimensoes da bola
BL_VELOCIDADE = 0.3
BL_VETOR_X_Y = [BL_VELOCIDADE,BL_VELOCIDADE]

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
player = pygame.Rect(PL_POS_X,PL_POS_Y,PL_WIDTH,PL_HEIGTH)
# bola
bola = pygame.Rect(width//2,heigth//2,20,20)
clock = pygame.time.Clock()
direcao = 0
while True:
    dt = clock.tick(30)
    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        break
    if event.type == KEYDOWN:
        if event.key == K_RIGHT:
            direcao = DIREITA
        if event.key == K_LEFT:
            direcao = ESQUERDA

    # calcula a velocidade da bola
    bola.move_ip(BL_VETOR_X_Y[0]*dt,BL_VETOR_X_Y[1]*dt)
    # corrige a direcao da bola em caso de colisao com as paredes
    if bola.left < 0 or bola.right > width-BL_VELOCIDADE:
        BL_VETOR_X_Y[0] = -BL_VETOR_X_Y[0]
    if bola.top < 0 or bola.bottom > heigth-BL_VELOCIDADE:
        BL_VETOR_X_Y[1] = -BL_VETOR_X_Y[1]
    # testa o movimento do player
    if direcao == DIREITA:
        if (player.right + PL_MOVIMENTO) <= width:
            player.right += PL_MOVIMENTO
        else:
            player.right = width
        direcao = 0
    elif direcao == ESQUERDA:
        if (player.right - PL_MOVIMENTO) >= PL_WIDTH:
            player.right -= PL_MOVIMENTO
        else:
            player.right = PL_WIDTH
        direcao = 0
    # testa a colisao da bola com o player
    # if collision(bola, player):
        # print("colisao")
    screen.fill(BLACK)

    # desenha a bola
    pygame.draw.ellipse(screen,RED,bola)
    # desenha o player
    pygame.draw.rect(screen,WHITE,player)
    #desenha a colmeia
    for bloco in colmeia:
        pygame.draw.rect(screen, BLUE, bloco)

    pygame.display.flip()