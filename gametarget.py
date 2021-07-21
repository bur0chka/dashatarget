import pygame, sys, time
from pygame.locals import *

pygame.init()
TEXTCOLOR = (0, 0, 0)
def drawText(text, font, surface, x, y):
    textobj = font.render(text, 4, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

windowSurface = pygame.display.set_mode((800, 800), 0, 32)
pygame.display.set_caption('Мишень')

GREEN = (0, 200, 0)

font = pygame.font.SysFont(None, 35)

arrows = 10
score = 0

#bowImage = pygame.image.load('лук.png')
#arrowImage = pygame.image.load('стрела.png')
#targetImage = pygame.image.load('мишень.png')

while True:

    windowSurface.fill(GREEN)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and arrows > 0:
            arrows -= 1
        if arrows > 0:
            drawText('стрелы: ' + str(arrows), font, windowSurface, (20), (40))
            drawText('счет: ' + str(score), font, windowSurface, (20), (60))
            pygame.display.update()

    if arrows == 0:
        drawText('Игра окончена!', font, windowSurface, (400), (300))
        drawText('счет:'+str(score), font, windowSurface, (400), (250))
        pygame.display.update()