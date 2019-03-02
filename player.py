import pygame
import window

# Characters
idle = [pygame.image.load('MC/adventurer-idle-2-00.png'), pygame.image.load('MC/adventurer-idle-2-01.png'), pygame.image.load('MC/adventurer-idle-2-02.png'), pygame.image.load('MC/adventurer-idle-2-03.png')]

walkRight = [pygame.image.load('MC/adventurer-run-00.png'), pygame.image.load('MC/adventurer-run-01.png'), pygame.image.load('MC/adventurer-run-02.png'), pygame.image.load('MC/adventurer-run-03.png'), pygame.image.load('MC/adventurer-run-04.png'), pygame.image.load('MC/adventurer-run-05.png')]

jumping = [pygame.image.load('MC/adventurer-smrslt-00.png'), pygame.image.load('MC/adventurer-smrslt-01.png'), pygame.image.load('MC/adventurer-smrslt-02.png'), pygame.image.load('MC/adventurer-smrslt-03.png')]

attack1 = [pygame.image.load('MC/adventurer-attack1-01.png'), pygame.image.load('MC/adventurer-attack1-02.png'), pygame.image.load('MC/adventurer-attack1-03.png'), pygame.image.load('MC/adventurer-attack1-04.png')]

attack2 = [pygame.image.load('MC/adventurer-attack2-00.png'), pygame.image.load('MC/adventurer-attack2-01.png'), pygame.image.load('MC/adventurer-attack2-02.png'), pygame.image.load('MC/adventurer-attack2-03.png'), pygame.image.load('MC/adventurer-attack2-04.png'), pygame.image.load('MC/adventurer-attack2-05.png')]

airAttack = [pygame.image.load('MC/adventurer-air-attack1-00.png'), pygame.image.load('MC/adventurer-air-attack1-01.png'), pygame.image.load('MC/adventurer-air-attack1-02.png'), pygame.image.load('MC/adventurer-air-attack1-03.png')]
# attack3 = [pygame.image.load('MC/adventurer-attack3-01.png'), pygame.image.load('MC/adventurer-attack3-01.png'), pygame.image.load('MC/adventurer-attack3-02.png'), pygame.image.load('MC/adventurer-attack3-03.png'), pygame.image.load('MC/adventurer-attack3-04.png'), pygame.image.load('MC/adventurer-attack3-05.png')]

class character():
    def __init__(self, x, y, width, height, vel):
        self.x = x
        self.y = y
        self.width = width * 3
        self.height = height * 3
        self.vel = vel

        self.switch = True
        self.right = True
        self.left = False
        self.jump = False
        self.attack1 = False
        self.attack2 = False
        self.airAttack = False

        self.standingCount = 0
        self.moveCount = 0
        self.jumpCount = 0
        self.jumpHeight = 7
        self.attack1Count = 0
        self.attack2Count = 0
        self.airAttackCount = 0

    def characterOptions(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] and self.x < 800 - self.width - self.vel and not(self.attack1) and not(self.attack2):
            self.right = True
            self.left = False
            self.switch = True
            self.x += self.vel
        elif keys[pygame.K_LEFT] and self.x > self.vel and not(self.attack1) and not(self.attack2):
            self.right = False
            self.left = True
            self.switch = False
            self.x -= self.vel
        else:
            self.right = False
            self.left = False
            self.moveCount = 0
            self.jumpCount = 0

        if not(self.jump):
            if keys[pygame.K_SPACE]:
                self.jump = True
        else:
            if not(self.airAttack):
                if keys[pygame.K_1]:
                    self.airAttack = True
            if self.jumpHeight >= -7:
                neg = 1
                if self.jumpHeight < 0:
                    neg = -1
                self.y -= (self.jumpHeight ** 2) * 0.5 * neg
                self.jumpHeight -= 1
            else:
                self.jumpHeight = 7
                self.airAttackCount = 0
                self.jump = False
                self.airAttack = False

        # if not(self.airAttack):
        #     if keys[pygame.K_1]:
        #         self.airAttack = True
        if not(self.attack1) and not(self.airAttack):
            if keys[pygame.K_1]:
                self.attack1 = True
        if not(self.attack2) and not(self.airAttack):
            if keys[pygame.K_2]:
                self.attack2 = True

    def drawCharacter(self):
        if self.standingCount + 1 >= 36:
            self.standingCount = 0
        if self.moveCount + 1 >= 36:
            self.moveCount = 0
        if self.jumpCount + 1 >= 36:
            self.jumpCount = 0
        if self.attack1Count + 1 >= 36:
            self.attack1 = False
            self.attack1Count = 0
        if self.attack2Count + 1 >= 36:
            self.attack2 = False
            self.attack2Count = 0
        if self.airAttackCount + 1 >= 36:
            self.airAttack = False
            self.airAttackCount = 0

        if self.attack1:
            if self.switch:
                window.win.blit(pygame.transform.scale(attack1[self.attack1Count//9], (self.width, self.height)), (self.x, self.y))
                self.attack1Count += 3
            else:
                window.win.blit(pygame.transform.scale(pygame.transform.flip(attack1[self.attack1Count//9], True, False), (self.width, self.height)), (self.x, self.y))
                self.attack1Count += 3
        elif self.attack2:
            if self.switch:
                window.win.blit(pygame.transform.scale(attack2[self.attack2Count//6], (self.width, self.height)), (self.x, self.y))
                self.attack2Count += 1
            else:
                window.win.blit(pygame.transform.scale(pygame.transform.flip(attack2[self.attack2Count//6], True, False), (self.width, self.height)), (self.x, self.y))
                self.attack2Count += 1
        elif self.right:
            if self.jump:
                if self.airAttack:
                    window.win.blit(pygame.transform.scale(airAttack[self.airAttackCount//9], (self.width, self.height)), (self.x, self.y))
                    self.airAttackCount += 3
                else:
                    window.win.blit(pygame.transform.scale(jumping[self.jumpCount//9], (self.width, self.height)), (self.x, self.y))
                    self.jumpCount += 3
            else:
                window.win.blit(pygame.transform.scale(walkRight[self.moveCount//6], (self.width, self.height)), (self.x, self.y))
                self.moveCount += 1
        elif self.left:
            if self.jump:
                if self.airAttack:
                    window.win.blit(pygame.transform.scale(pygame.transform.flip(airAttack[self.airAttackCount//9], True, False), (self.width, self.height)), (self.x, self.y))
                    self.airAttackCount += 3
                else:
                    window.win.blit(pygame.transform.scale(pygame.transform.flip(jumping[self.jumpCount//9], True, False), (self.width, self.height)), (self.x, self.y))
                    self.jumpCount += 3
            else:
                window.win.blit(pygame.transform.scale(pygame.transform.flip(walkRight[self.moveCount//6], True, False), (self.width, self.height)), (self.x, self.y))
                self.moveCount += 1
        elif self.jump:
            if self.switch:
                if self.airAttack:
                    window.win.blit(pygame.transform.scale(airAttack[self.airAttackCount//9], (self.width, self.height)), (self.x, self.y))
                    self.airAttackCount += 3
                else:
                    window.win.blit(pygame.transform.scale(jumping[self.jumpCount//9], (self.width, self.height)), (self.x, self.y))
                    self.jumpCount += 3
            else:
                if self.airAttack:
                    window.win.blit(pygame.transform.scale(pygame.transform.flip(airAttack[self.airAttackCount//9], True, False), (self.width, self.height)), (self.x, self.y))
                    self.airAttackCount += 3
                else:
                    window.win.blit(pygame.transform.scale(pygame.transform.flip(jumping[self.jumpCount//9], True, False), (self.width, self.height)), (self.x, self.y))
                    self.jumpCount += 3
        else:
            if self.switch:
                window.win.blit(pygame.transform.scale(idle[self.standingCount//9], (self.width, self.height)), (self.x, self.y))
                self.standingCount += 3
            else:
                window.win.blit(pygame.transform.scale(pygame.transform.flip(idle[self.standingCount//9], True, False), (self.width, self.height)), (self.x, self.y))
                self.standingCount += 3
