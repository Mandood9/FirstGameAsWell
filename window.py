import pygame

pygame.init()

# Backgrounds
bg1 = [pygame.image.load('BG1/BGF/CloudsBack.png'), pygame.image.load('BG1/BGF/CloudsFront.png'), pygame.image.load('BG1/BGF/BGBack.png'), pygame.image.load('BG1/BGF/BGFront.png'), ]

win = pygame.display.set_mode((800, 600))

class background():
    def __init__(self):
        self.s1 = 0
        self.s2 = 0
        self.s3 = 0
        self.s4 = 0
        self.s18 = 0
        self.s28 = 0
        self.s38 = 0
        self.s48 = 0
        self.c1 = 1
        self.c2 = 2
        self.c3 = 4
        self.c4 = 8
        self.y = 0
        # self.width = width
        # self.height = height
        self.screen = 800

    def drawBackground(self, mc):
        keys = pygame.key.get_pressed()

        if self.s1 == -800:
            self.s1 = 800
        if self.s2 == -800:
            self.s2 = 800
        if self.s3 == -800:
            self.s3 = 800
        if self.s4 == -800:
            self.s4 = 800
        if self.s18 + 800 == -800:
            self.s18 = 0
        if self.s28 + 800 == -800:
            self.s28 = 0
        if self.s38 + 800 == -800:
            self.s38 = 0
        if self.s48 + 800 == -800:
            self.s48 = 0

        if mc.x < 425 - mc.width - mc.vel and keys[pygame.K_RIGHT] and mc.vel == 0 and mc.alive and not(mc.hit):
            self.s1 -= self.c1
            self.s2 -= self.c2
            self.s3 -= self.c3
            self.s4 -= self.c4
            self.s18 -= self.c1
            self.s28 -= self.c2
            self.s38 -= self.c3
            self.s48 -= self.c4

        win.blit(pygame.transform.scale(bg1[0], (800, 600)), (self.s18 + 800, self.y))
        win.blit(pygame.transform.scale(bg1[0], (800, 600)), (self.s1, self.y))
        win.blit(pygame.transform.scale(bg1[1], (800, 600)), (self.s28 + 800, self.y))
        win.blit(pygame.transform.scale(bg1[1], (800, 600)), (self.s2, self.y))
        win.blit(pygame.transform.scale(bg1[2], (800, 600)), (self.s38 + 800, self.y))
        win.blit(pygame.transform.scale(bg1[2], (800, 600)), (self.s3, self.y))
        win.blit(pygame.transform.scale(bg1[3], (800, 600)), (self.s48 + 800, self.y))
        win.blit(pygame.transform.scale(bg1[3], (800, 600)), (self.s4, self.y))
