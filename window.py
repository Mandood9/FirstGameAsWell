import pygame

# Backgrounds
bg1 = [pygame.image.load('BG1/BGF/BGBack.png'), pygame.image.load('BG1/BGF/BGFront.png'), pygame.image.load('BG1/BGF/CloudsBack.png'), pygame.image.load('BG1/BGF/CloudsFront.png')]

win = pygame.display.set_mode((800, 600))

def redrawGameWindow():
    win.blit(pygame.transform.scale(bg1[2], (800, 600)), (0, 0))
    win.blit(pygame.transform.scale(bg1[3], (800, 600)), (0, 0))
    win.blit(pygame.transform.scale(bg1[0], (800, 600)), (0, 0))
    win.blit(pygame.transform.scale(bg1[1], (800, 600)), (0, 0))
    # mc.drawMC()
    # slime.drawMob()
    # pygame.display.update()

class background():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def moveBackground(self, right, xValue):
        pass
