import pygame, sys, random

pygame.init()
TEXTCOLOR = (0, 0, 0)
def drawText(text, font, surface, x, y):
    textobj = font.render(text, 4, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

windowSurface = pygame.display.set_mode((800, 800), 1, 32)
pygame.display.set_caption('Мишень')

GREEN = (0, 200, 0)

target = pygame.Rect(400, 150, 40, 40)
bow = pygame.Rect(400, 650, 50, 50)
arrow = pygame.Rect(300, 625, 40, 40)

font = pygame.font.SysFont('1', 35)

arrows = 10
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

def gameplaying():
    if arrows > 0:
        return True
    else:
        return False

while True:
    if gameplaying():
        windowSurface.fill(GREEN)
        bow.topleft = (250, 600)
        target.topleft = (300, 50)
        windowSurface.blit(bowImage, bow)
        drawText('стрелы: ' + str(arrows), font, windowSurface, (20), (40))
        drawText('счет: ' + str(score), font, windowSurface, (20), (65))
        windowSurface.blit(targetImage, target)
        firing()
    if arrows > 0:
        drawText('стрелы: ' + str(arrows), font, windowSurface, (20), (40))
        drawText('счет: ' + str(score), font, windowSurface, (20), (65))
        pygame.display.update()
    if arrow.colliderect(target):
        score += 5
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and arrows > 0:
            pygame.mouse.get_rel()
            windowSurface.blit(arrowImage, arrow)
            arrows -= 1
            listarrows.append(arrow)
        if arrow.colliderect(target):
            score += 5

    if arrows > 0:
        drawText('стрелы: ' + str(arrows), font, windowSurface, (20), (40))
        drawText('счет: ' + str(score), font, windowSurface, (20), (65))
    if arrows > 0:
        pygame.display.update(arrow)

    else:
        windowSurface.fill(GREEN)
        drawText('Игра окончена!', font, windowSurface, (300), (250))
        drawText('счет:'+str(score), font, windowSurface, (300), (300))
        drawText('Нажмите клавишу, чтобы играть снова', font, windowSurface, (300), (350))
        pygame.display.update()


