import pygame, sys, random
from pygame.locals import *

pygame.init()
TEXTCOLOR = (0, 0, 0)
def drawText(text, font, surface, x, y):
    textobj = font.render(text, 4, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def gameover():
    windowSurface.fill(GREEN)
    drawText('Игра окончена!', font, windowSurface, (300), (250))
    drawText('счет:' + str(score), font, windowSurface, (300), (300))
    drawText('Нажмите клавишу, чтобы играть снова', font, windowSurface, (300), (350))
    pygame.display.update()

def presskey():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # Нажатие ESC осуществляет выход.
                    pygame.quit()
                    sys.exit()
                return

windowSurface = pygame.display.set_mode((800, 800), 1, 32)
pygame.display.set_caption('Мишень')

GREEN = (0, 200, 0)

target = pygame.Rect(300, 150, 40, 40)
bow = pygame.Rect(400, 650, 50, 50)
arrow = pygame.Rect(300, 625, 40, 40)

font = pygame.font.SysFont('1', 35)

arrows = 10
hitPoints = 0
score = 0
targets = 3
listtargets = []
listarrows = []

bowImage = pygame.image.load('bow.png')
arrowImage = pygame.image.load('arrow.png')
targetImage = pygame.image.load('target.png')
bowRect = bowImage.get_rect()
targetRect = targetImage.get_rect()
arrowRect = arrowImage.get_rect()

def firing():
    if listarrows != [] and arrows > 0:
        arrow.top -= 1
        windowSurface.blit(arrowImage, arrow)
        return True
    else:
        return False



newtarget = {'draw': pygame.Rect(random.randint(0, 500 - 100), 0 - 40, 40, 40),
             'surface': pygame.transform.scale(targetImage, (50, 50))}

listtargets.append(target)

while True:
    windowSurface.fill(GREEN)
    bow.topleft = (250, 600)
    target.topleft = (300, 50)
    windowSurface.blit(bowImage, bow)
    drawText('стрелы: ' + str(arrows), font, windowSurface, (20), (40))
    drawText('счет: ' + str(score), font, windowSurface, (20), (65))
    if arrow.y == -50:
        listarrows.remove(arrow)
        arrow.y = 625
    if listtargets != []:
        windowSurface.blit(targetImage, target)
    firing()
    if arrows > 0:
        drawText('стрелы: ' + str(arrows), font, windowSurface, (20), (40))
        drawText('счет: ' + str(score), font, windowSurface, (20), (65))
        pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and arrows > 0 and listarrows == []:
            pygame.mouse.get_rel()
            windowSurface.blit(arrowImage, arrow)
            arrows -= 1
            listarrows.append(arrow)
    for targets in listtargets:
        if arrow.colliderect(target):
            score += 50
            listtargets.remove(target)
            listarrows.remove(arrow)
            arrow.y = 625

    if arrows > 0:
        drawText('стрелы: ' + str(arrows), font, windowSurface, (20), (40))
        drawText('счет: ' + str(score), font, windowSurface, (20), (65))
    if arrows > 0:
        pygame.display.update(arrow)

    if arrows == 0:
        gameover()
        presskey()