import pygame, sys, random, time
from pygame.locals import *


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
    drawText('рекорд: ' + str(topScore), font, windowSurface, (20), (90))
    drawText('1.0', font, windowSurface, (825), (850))
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
        arrow.y -= 3
        windowSurface.blit(arrowImage, arrow)
        return True
    else:
        return False





if __name__ == '__main__':
    pygame.init()
    windowSurface = pygame.display.set_mode((900, 900), 1, 32)
    pygame.display.set_caption('Мишень')

    GREEN = (0, 200, 0)
    BROWN = (150, 75, 0)

    TEXTCOLOR = (0, 0, 0)

    font = pygame.font.SysFont('1', 35)

    arrows = 10
    score = 0

    wall = pygame.Rect(0, 0, 900, 300)

    target = pygame.Rect(0, 100, 50, 100)
    bow = pygame.Rect(300, 600, 50, 50)
    arrow = pygame.Rect(300, 625, 50, 50)
    badtarget = pygame.Rect(0, 100, 50, 75)
    goodtarget = pygame.Rect(0, 100, 50, 50)
    distance = 900 - target.x

    listtargets = []
    listbadtargets = []
    listgoodtargets = []
    listarrows = []
    listtargets.append(target)
    listbadtargets.append(badtarget)
    listgoodtargets.append(goodtarget)

    bowImage = pygame.image.load('bow.png')
    arrowImage = pygame.image.load('arrow.png')
    targetImage = pygame.image.load('target.png')
    badTargetImage = pygame.image.load('badtarget.png')
    goodTargetImage = pygame.image.load('goodtarget.png')
    bowRect = bowImage.get_rect()
    targetRect = targetImage.get_rect()
    badtargetRect = badTargetImage.get_rect()
    goodtargetRect = goodTargetImage.get_rect()
    arrowRect = arrowImage.get_rect()
    with open("recordscore.txt", "r") as gr:
        topScore = int(gr.read())
    while True:
        target.x += 5
        badtarget.x += 4
        goodtarget.x += 6
        r = 900 - target.x
        windowSurface.fill(GREEN)
        pygame.draw.rect(windowSurface, BROWN, wall)
        windowSurface.blit(bowImage, bow)
        drawText('стрелы: ' + str(arrows), font, windowSurface, (20), (40))
        drawText('счет: ' + str(score), font, windowSurface, (20), (65))
        drawText('рекорд: ' + str(topScore), font, windowSurface, (20), (90))
        drawText('1.1', font, windowSurface, (825), (850))
        if arrow.y < -50:
            listarrows.remove(arrow)
            arrow.y = 625
        if target.x > -100 or target.x < 900:
            windowSurface.blit(targetImage, target)
        if target.x > 900:
            target.x = -100
        if badtarget.x > -100 or badtarget.x < 900:
            windowSurface.blit(badTargetImage, badtarget)
        if badtarget.x > 900:
            badtarget.x = -100
        if goodtarget.x > -100 or goodtarget.x < 900:
            windowSurface.blit(goodTargetImage, goodtarget)
        if goodtarget.x > 900:
            goodtarget.x = -100
        if listtargets != []:
            windowSurface.blit(targetImage, target)
        firing()
        if listbadtargets != []:
            windowSurface.blit(badTargetImage, badtarget)
        firing()
        if arrows >= 0:
            drawText('стрелы: ' + str(arrows), font, windowSurface, (20), (40))
            drawText('счет: ' + str(score), font, windowSurface, (20), (65))
            drawText('рекорд: ' + str(topScore), font, windowSurface, (20), (90))
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
                target.x = -distance
                arrow.y = 625
        for badtarget in listbadtargets:
            if arrow.colliderect(badtarget):
                score -= 50
                arrows -= 5
                listbadtargets.remove(badtarget)
                listarrows.remove(arrow)
                listbadtargets.append(badtarget)
                badtarget.x = -distance
                arrow.y = 625
        for goodtarget in listgoodtargets:
            if arrow.colliderect(goodtarget):
                score += 100
                arrows += 5
                listgoodtargets.remove(goodtarget)
                listarrows.remove(arrow)
                listgoodtargets.append(goodtarget)
                goodtarget.x = -distance
                arrow.y = 625

        if arrows >= 0 or arrows <= 0:
            drawText('стрелы: ' + str(arrows), font, windowSurface, (20), (40))
            drawText('счет: ' + str(score), font, windowSurface, (20), (65))
            drawText('рекорд: ' + str(topScore), font, windowSurface, (20), (90))
            pygame.display.update(arrow)

        if arrows <= 0 and arrow.y < -49 or arrow.colliderect(badtarget):
            if score > topScore:
                topScore = score
            gameover()
            presskey()
            arrows = 10
            score = 0
            with open("recordscore.txt", "r") as f:
                try:
                    if int(f.read()) < topScore:
                        with open("recordscore.txt", "w") as fw:
                            fw.write(str(topScore))
                except ValueError:
                    with open("recordscore.txt", "w") as fverr:
                        fverr.write("0")