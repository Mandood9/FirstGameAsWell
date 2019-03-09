import pygame
import pytmx

pygame.init()

# Backgrounds
bg1 = [pygame.image.load('BG1/BGF/CloudsBack.png'), pygame.image.load('BG1/BGF/CloudsFront.png'), pygame.image.load('BG1/BGF/BGBack.png'), pygame.image.load('BG1/BGF/BGFront.png')]

magicCliffs = {
    # "level1": pytmx.load_pygame('MagicCliffsMap1.tmx'),
    "sea": pygame.image.load('Magic-Cliffs-Environment/PNG/sea.png'),
    "sky": pygame.image.load('Magic-Cliffs-Environment/PNG/sky.png'),
    "farGrounds": pygame.image.load('Magic-Cliffs-Environment/PNG/far-grounds.png'),
    "clouds":  pygame.image.load('Magic-Cliffs-Environment/PNG/clouds.png'),
    "tile": [pygame.image.load('Magic-Cliffs-Environment/PNG/tile.png'), pygame.image.load('Magic-Cliffs-Environment/PNG/tile (1).png'), pygame.image.load('Magic-Cliffs-Environment/PNG/tile (2).png'), pygame.image.load('Magic-Cliffs-Environment/PNG/tile (3).png'), pygame.image.load('Magic-Cliffs-Environment/PNG/tile (4).png'), pygame.image.load('Magic-Cliffs-Environment/PNG/tile (5).png'), pygame.image.load('Magic-Cliffs-Environment/PNG/tile (6).png'), pygame.image.load('Magic-Cliffs-Environment/PNG/tile (7).png'), pygame.image.load('Magic-Cliffs-Environment/PNG/tile (8).png'), pygame.image.load('Magic-Cliffs-Environment/PNG/tile (9).png'), pygame.image.load('Magic-Cliffs-Environment/PNG/tile (10).png'), pygame.image.load('Magic-Cliffs-Environment/PNG/tile (11).png'), pygame.image.load('Magic-Cliffs-Environment/PNG/tile (12).png'), pygame.image.load('Magic-Cliffs-Environment/PNG/tile (13).png'), pygame.image.load('Magic-Cliffs-Environment/PNG/tile (14).png'), pygame.image.load('Magic-Cliffs-Environment/PNG/tile (15).png'), pygame.image.load('Magic-Cliffs-Environment/PNG/tile (16).png'), pygame.image.load('Magic-Cliffs-Environment/PNG/tile (17).png'), pygame.image.load('Magic-Cliffs-Environment/PNG/tile (18).png'), pygame.image.load('Magic-Cliffs-Environment/PNG/tile (19).png'), pygame.image.load('Magic-Cliffs-Environment/PNG/tile (20).png'), pygame.image.load('Magic-Cliffs-Environment/PNG/tile (21).png'), pygame.image.load('Magic-Cliffs-Environment/PNG/tile (22).png'), pygame.image.load('Magic-Cliffs-Environment/PNG/tile (23).png'), pygame.image.load('Magic-Cliffs-Environment/PNG/tile (24).png'), pygame.image.load('Magic-Cliffs-Environment/PNG/tile (25).png'), pygame.image.load('Magic-Cliffs-Environment/PNG/tile (26).png'), pygame.image.load('Magic-Cliffs-Environment/PNG/tile (27).png'), pygame.image.load('Magic-Cliffs-Environment/PNG/tile (28).png'), pygame.image.load('Magic-Cliffs-Environment/PNG/tile (29).png'), pygame.image.load('Magic-Cliffs-Environment/PNG/tile (30).png'), pygame.image.load('Magic-Cliffs-Environment/PNG/tile (31).png'), pygame.image.load('Magic-Cliffs-Environment/PNG/tile (32).png'), pygame.image.load('Magic-Cliffs-Environment/PNG/tile (33).png'), pygame.image.load('Magic-Cliffs-Environment/PNG/tile (34).png'), pygame.image.load('Magic-Cliffs-Environment/PNG/tile (35).png'), pygame.image.load('Magic-Cliffs-Environment/PNG/tile (36).png'), pygame.image.load('Magic-Cliffs-Environment/PNG/tile (37).png'), pygame.image.load('Magic-Cliffs-Environment/PNG/tile (38).png'), pygame.image.load('Magic-Cliffs-Environment/PNG/tile (39).png'), pygame.image.load('Magic-Cliffs-Environment/PNG/tile (40).png'), pygame.image.load('Magic-Cliffs-Environment/PNG/tile (41).png'), pygame.image.load('Magic-Cliffs-Environment/PNG/tile (42).png')]
}

win = pygame.display.set_mode((1024, 768))

class background():
    def __init__(self):
        self.s1 = 0
        self.s2 = 0
        self.s3 = 0
        self.s4 = 0
        # self.s18 = 0
        # self.s28 = 0
        # self.s38 = 0
        # self.s48 = 0
        self.c1 = 1
        self.c2 = 2
        self.c3 = 4
        self.c4 = 8
        self.y = 0
        # self.width = width
        # self.height = height
        self.screen = 800

    # def drawBackground(self, mc):
    #     keys = pygame.key.get_pressed()
    #
    #     if self.s1 == -800:
    #         self.s1 = 800
    #     if self.s2 == -800:
    #         self.s2 = 800
    #     if self.s3 == -800:
    #         self.s3 = 800
    #     if self.s4 == -800:
    #         self.s4 = 800
    #     if self.s18 + 800 == -800:
    #         self.s18 = 0
    #     if self.s28 + 800 == -800:
    #         self.s28 = 0
    #     if self.s38 + 800 == -800:
    #         self.s38 = 0
    #     if self.s48 + 800 == -800:
    #         self.s48 = 0
    #
    #     if mc.x < 425 - mc.width - mc.vel and keys[pygame.K_RIGHT] and mc.vel == 0 and mc.alive and not(mc.hit) and not(mc.attack1) and not(mc.attack2):
    #         self.s1 -= self.c1
    #         self.s2 -= self.c2
    #         self.s3 -= self.c3
    #         self.s4 -= self.c4
    #         self.s18 -= self.c1
    #         self.s28 -= self.c2
    #         self.s38 -= self.c3
    #         self.s48 -= self.c4
    #
    #     win.blit(pygame.transform.scale(bg1[0], (800, 600)), (self.s18 + 800, self.y))
    #     win.blit(pygame.transform.scale(bg1[0], (800, 600)), (self.s1, self.y))
    #     win.blit(pygame.transform.scale(bg1[1], (800, 600)), (self.s28 + 800, self.y))
    #     win.blit(pygame.transform.scale(bg1[1], (800, 600)), (self.s2, self.y))
    #     win.blit(pygame.transform.scale(bg1[2], (800, 600)), (self.s38 + 800, self.y))
    #     win.blit(pygame.transform.scale(bg1[2], (800, 600)), (self.s3, self.y))
    #     win.blit(pygame.transform.scale(bg1[3], (800, 600)), (self.s48 + 800, self.y))
    #     win.blit(pygame.transform.scale(bg1[3], (800, 600)), (self.s4, self.y))

    def drawBackground(self, mc):
        keys = pygame.key.get_pressed()

        if self.s1 == -1024:
            self.s1 = 1024
        if self.s2 == -512:
            self.s2 = 512

        if mc.x < 544 - mc.width - mc.vel and keys[pygame.K_RIGHT] and mc.vel == 0 and mc.alive and not(mc.hit) and not(mc.attack1) and not(mc.attack2):
            self.s1 -= self.c1
            self.s2 -= self.c2
            self.s3 -= self.c3
            self.s4 -= self.c4

        win.blit(pygame.transform.scale(magicCliffs["sky"], (1024, 768)), (self.s1, self.y))
        win.blit(pygame.transform.scale(magicCliffs["sky"], (1024, 768)), (self.s1 + 1024, self.y))
        win.blit(pygame.transform.scale(magicCliffs["clouds"], (512, 384)), (self.s2, self.y + 216))
        win.blit(pygame.transform.scale(magicCliffs["clouds"], (512, 384)), (self.s2 + 512, self.y + 216))
        win.blit(pygame.transform.scale(magicCliffs["clouds"], (512, 384)), (self.s2 + 1024, self.y + 216))
        win.blit(pygame.transform.scale(magicCliffs["clouds"], (512, 384)), (self.s2 + 1536, self.y + 216))
        win.blit(pygame.transform.scale(magicCliffs["sea"], (512, 384)), (self.s3, self.y + 480))
        win.blit(pygame.transform.scale(magicCliffs["sea"], (512, 384)), (self.s3 + 512, self.y + 480))
        win.blit(pygame.transform.scale(magicCliffs["sea"], (512, 384)), (self.s3 + 1024, self.y + 480))
        win.blit(pygame.transform.scale(magicCliffs["sea"], (512, 384)), (self.s3 + 1536, self.y + 480))
        # win.blit(pygame.transform.scale(magicCliffs["level1"], (1024, 768)), (self.s4, self.y))
