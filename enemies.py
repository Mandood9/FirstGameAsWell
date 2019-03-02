import pygame
import random
import window
import player

# Enemies
skeleton = []

slimeIdle = [pygame.image.load('Slime/Sprites/slime-idle-0.png'), pygame.image.load('Slime/Sprites/slime-idle-1.png'), pygame.image.load('Slime/Sprites/slime-idle-2.png'), pygame.image.load('Slime/Sprites/slime-idle-3.png')]

slimeMove = [pygame.image.load('Slime/Sprites/slime-move-0.png'), pygame.image.load('Slime/Sprites/slime-move-1.png'), pygame.image.load('Slime/Sprites/slime-move-2.png'), pygame.image.load('Slime/Sprites/slime-move-3.png')]

slimeAttack = [pygame.image.load('Slime/Sprites/slime-attack-1.png'), pygame.image.load('Slime/Sprites/slime-attack-2.png'), pygame.image.load('Slime/Sprites/slime-attack-3.png'), pygame.image.load('Slime/Sprites/slime-attack-4.png')]

class mob():
    def __init__(self, x, y, width, height, vel, sightRange, attackRange):
        self.x = x
        self.y = y
        self.width = width * 3
        self.height = height * 3
        self.vel = vel
        self.sightRange = sightRange
        self.attackRange = attackRange

        self.detected = False
        self.left = True
        self.attack = False

        self.idleCount = 0
        self.dir = random.randint(0, 1)
        self.moveCount = 0
        self.attackCount = 0

    def mobOptions(self, player):
        if abs(self.x - player.x) <= self.sightRange or self.detected:
            self.detected = True

            if self.x - player.x > 0:
                self.left = True

                if abs(self.x - player.x) <= self.attackRange or self.attack:
                    self.attack = True
                    self.moveCount = 0
                else:
                    self.attack = False
                    self.attackCount = 0
                    self.x -= self.vel
            else:
                self.left = False

                if abs(self.x - player.x) <= self.attackRange - 50 or self.attack:
                    self.attack = True
                    self.moveCount = 0
                else:
                    self.attack = False
                    self.attackCount = 0
                    self.x += self.vel

    def drawMob(self):
        if self.idleCount + 1 >= 36:
            self.idleCount = 0
        if self.moveCount + 1 >= 36:
            self.moveCount = 0
        if self.attackCount + 1 >= 36:
            self.attack = False
            self.attackCount = 0

        if self.detected:
            if self.left:
                if self.attack:
                    #draw left attack animation
                    window.win.blit(pygame.transform.scale(slimeAttack[self.attackCount//9], (self.width, self.height)), (self.x, self.y))
                    self.attackCount += 3
                else:
                    #draw left move animation
                    window.win.blit(pygame.transform.scale(slimeMove[self.moveCount//9], (self.width, self.height)), (self.x, self.y))
                    self.moveCount += 1
            else:
                if self.attack:
                    #draw right attack animation
                    window.win.blit(pygame.transform.scale(pygame.transform.flip(slimeAttack[self.attackCount//9], True, False), (self.width, self.height)), (self.x, self.y))
                    self.attackCount += 3
                else:
                    pass
                    #draw right move animation
                    window.win.blit(pygame.transform.scale(pygame.transform.flip(slimeMove[self.moveCount//9], True, False), (self.width, self.height)), (self.x, self.y))
                    self.moveCount += 1
        else:
            #draw idle animation
            if self.dir == 0:
                window.win.blit(pygame.transform.scale(slimeIdle[self.idleCount//9], (self.width, self.height)), (self.x, self.y))
            else:
                window.win.blit(pygame.transform.scale(pygame.transform.flip(slimeIdle[self.idleCount//9], True, False), (self.width, self.height)), (self.x, self.y))
            self.idleCount += 1
