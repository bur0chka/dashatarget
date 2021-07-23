import pygame, sys, time

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
YELLOW = (255, 255, 0)
BLUE =(0, 0, 250)
RED = (255, 0, 0)

target = pygame.Rect(400, 150, 40, 40)
bow = pygame.Rect(400, 650, 50, 50)
arrow = pygame.Rect(400, 625, 40, 40)


font = pygame.font.SysFont(None, 35)

arrows = 10
score = 0
targets = []
listarrows = []
arrowx = 300
arrowy = 500


bowImage = pygame.image.load('bow.png')
arrowImage = pygame.image.load('arrow.png')
targetImage = pygame.image.load('target.png')
bowRect = bowImage.get_rect()
targetRect = targetImage.get_rect()
arrowRect = arrowImage.get_rect()

def gameover():
    if arrows == 0:
        return True
    else:
        return False

def firing():
    if listarrows != [] and arrows > 0:
        arrow.top -= 1
        time.sleep(0.02)
        windowSurface.blit(arrowImage, arrow)
        return True
    else:
        return False

while True:
    windowSurface.fill(GREEN)
    bow.topleft = (250, 600)
    target.topleft = (300, 50)
    windowSurface.blit(bowImage, bow)
    windowSurface.blit(targetImage, target)
    firing()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and arrows > 0:
            pygame.mouse.get_rel()
            listarrows.append(arrow)
            windowSurface.blit(arrowImage, arrow)
            arrows -= 1

        if arrows >= 0:
            drawText('стрелы: ' + str(arrows), font, windowSurface, (20), (40))
            drawText('счет: ' + str(score), font, windowSurface, (20), (60))
            pygame.display.update()

    if arrows == 0:
        drawText('Игра окончена!', font, windowSurface, (300), (250))
        drawText('счет:'+str(score), font, windowSurface, (300), (300))
        drawText('Нажмите клавишу, чтобы играть снова', font, windowSurface, (300), (350))
        gameover()
        pygame.display.update()


