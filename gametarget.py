import pygame, sys, random, time
from pygame.locals import *

pygame.init()
def drawText(text, font, surface, x, y):
    textobj = font.render(text, 4, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def gameover():
    windowSurface.fill(GREEN)
    drawText('Игра окончена!', font, windowSurface, (200), (250))
    drawText('счет:' + str(score), font, windowSurface, (200), (300))
    drawText('Нажмите клавишу, чтобы играть снова', font, windowSurface, (200), (350))
    drawText('0.8', font, windowSurface, (825), (850))
    pygame.display.update()

def presskey():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                return

def firing():
    if listarrows != [] and arrows >= 0:
        arrow.y -= 1
        windowSurface.blit(arrowImage, arrow)
        return True
    else:
        return False

windowSurface = pygame.display.set_mode((900, 900), 1, 32)
pygame.display.set_caption('Мишень')

GREEN = (0, 200, 0)

TEXTCOLOR = (0, 0, 0)

font = pygame.font.SysFont('1', 35)

arrows = 10
score = 0
targets = 3

target = pygame.Rect(0, 50, 40, 40)
bow = pygame.Rect(300, 600, 50, 50)
arrow = pygame.Rect(300, 625, 40, 40)

listtargets = []
listarrows = []
listtargets.append(target)



bowImage = pygame.image.load('bow.png')
arrowImage = pygame.image.load('arrow.png')
targetImage = pygame.image.load('target.png')
bowRect = bowImage.get_rect()
targetRect = targetImage.get_rect()
arrowRect = arrowImage.get_rect()

while True:
    target.x +=1
    windowSurface.fill(GREEN)
    windowSurface.blit(bowImage, bow)
    drawText('стрелы: ' + str(arrows), font, windowSurface, (20), (40))
    drawText('счет: ' + str(score), font, windowSurface, (20), (65))
    drawText('0.8', font, windowSurface, (825), (850))
    if arrow.y == -50:
        listarrows.remove(arrow)
        arrow.y = 625
    if target.x >= -100 or target.x < 800:
        windowSurface.blit(targetImage, target)
    if target.x == 900:
        target.x = -100
    if listtargets != []:
        windowSurface.blit(targetImage, target)
    firing()
    if arrows >= 0:
        drawText('стрелы: ' + str(arrows), font, windowSurface, (20), (40))
        drawText('счет: ' + str(score), font, windowSurface, (20), (65))
        pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and arrows >= 0 and listarrows == []:
            pygame.mouse.get_rel()
            windowSurface.blit(arrowImage, arrow)
            arrows -= 1
            listarrows.append(arrow)
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
    for target in listtargets:
        if arrow.colliderect(target):
            score += 50
            arrows += 2
            listtargets.remove(target)
            listarrows.remove(arrow)
            listtargets.append(target)
            target.x = -100
            arrow.y = 625

    if arrows >= 0:
        drawText('стрелы: ' + str(arrows), font, windowSurface, (20), (40))
        drawText('счет: ' + str(score), font, windowSurface, (20), (65))
        pygame.display.update(arrow)

    if arrows == 0 and arrow.y == -49:
        gameover()
        presskey()
        drawText('0.75', font, windowSurface, (725), (750))
        arrows = 10
        score = 0