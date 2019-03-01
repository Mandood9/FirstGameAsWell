import pygame

pygame.init()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("First Game As Well")

bg1 = [pygame.image.load('BG1/BGF/BGBack.png'), pygame.image.load('BG1/BGF/BGFront.png'), pygame.image.load('BG1/BGF/CloudsBack.png'), pygame.image.load('BG1/BGF/CloudsFront.png')]

walkRight = [pygame.image.load('MC/adventurer-run-00.png'), pygame.image.load('MC/adventurer-run-01.png'), pygame.image.load('MC/adventurer-run-02.png'), pygame.image.load('MC/adventurer-run-03.png'), pygame.image.load('MC/adventurer-run-04.png'), pygame.image.load('MC/adventurer-run-05.png')]

idle = [pygame.image.load('MC/adventurer-idle-2-00.png'), pygame.image.load('MC/adventurer-idle-2-01.png'), pygame.image.load('MC/adventurer-idle-2-02.png'), pygame.image.load('MC/adventurer-idle-2-03.png')]

jumping = [pygame.image.load('MC/adventurer-smrslt-00.png'), pygame.image.load('MC/adventurer-smrslt-01.png'), pygame.image.load('MC/adventurer-smrslt-02.png'), pygame.image.load('MC/adventurer-smrslt-03.png')]

attack1 = [pygame.image.load('MC/adventurer-attack1-01.png'), pygame.image.load('MC/adventurer-attack1-02.png'), pygame.image.load('MC/adventurer-attack1-03.png'), pygame.image.load('MC/adventurer-attack1-04.png')]

attack2 = [pygame.image.load('MC/adventurer-attack2-00.png'), pygame.image.load('MC/adventurer-attack2-01.png'), pygame.image.load('MC/adventurer-attack2-02.png'), pygame.image.load('MC/adventurer-attack2-03.png'), pygame.image.load('MC/adventurer-attack2-04.png'), pygame.image.load('MC/adventurer-attack2-05.png')]

attack3 = [pygame.image.load('MC/adventurer-attack3-01.png'), pygame.image.load('MC/adventurer-attack3-01.png'), pygame.image.load('MC/adventurer-attack3-02.png'), pygame.image.load('MC/adventurer-attack3-03.png'), pygame.image.load('MC/adventurer-attack3-04.png'), pygame.image.load('MC/adventurer-attack3-05.png')]

clock = pygame.time.Clock()

class mainChar():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width * 3
        self.height = height * 3
        self.vel = 10

        self.standingCount = 0

        self.facingRight = True
        self.right = False
        self.left = False
        self.walkCount = 0

        self.jump = False
        self.jumpFrame = 0
        self.jumpCount = 7

        self.attack1 = False
        self.attack1Count = 0

#    def counter(self):
        # if self.walkCount + 1 >= 36:
        #     self.walkCount = 0
        # if self.standingCount + 1 >= 36:
        #     self.standingCount = 0
        # if self.jumpFrame + 1 >= 36:
        #     self.jumpFrame = 0
        # if self.attack1Count + 1 >= 36:
        #     self.attack1Count = 0

    def drawMC(self):
#        counter()
        if self.walkCount + 1 >= 36:
            self.walkCount = 0
        if self.standingCount + 1 >= 36:
            self.standingCount = 0
        if self.jumpFrame + 1 >= 36:
            self.jumpFrame = 0
        if self.attack1Count + 1 >= 36:
            self.attack1Count = 0

        if self.right:
            if self.jump:
                scaled = pygame.transform.scale(jumping[self.jumpFrame//9], (self.width, self.height))
                window.blit(scaled, (self.x, self.y))
                self.jumpFrame += 4
            else:
                window.blit(pygame.transform.scale(walkRight[self.walkCount//6], (self.width, self.height)), (mc.x, mc.y))
            self.walkCount += 3

        elif self.left:
            if self.jump:
                window.blit(pygame.transform.scale(pygame.transform.flip(jumping[self.jumpFrame//9], True, False), (self.width, self.height)), (mc.x, mc.y))
                self.jumpFrame += 4
            else:
                window.blit(pygame.transform.scale(pygame.transform.flip(walkRight[self.walkCount//6], True, False), (self.width, self.height)), (mc.x, mc.y))
            self.walkCount += 3

        elif self.jump:
            if self.facingRight:
                scaled = pygame.transform.scale(jumping[self.jumpFrame//9], (self.width, self.height))
                window.blit(scaled, (self.x, self.y))
            else:
                window.blit(pygame.transform.scale(pygame.transform.flip(jumping[self.jumpFrame//9], True, False), (self.width, self.height)), (mc.x, mc.y))
            self.jumpFrame += 4

        elif self.attack1:
            if self.facingRight:
                scaled = pygame.transform.scale(attack1[self.attack1Count//9], (self.width, self.height))
                window.blit(scaled, (self.x, self.y))
            else:
                window.blit(pygame.transform.scale(pygame.transform.flip(attack1[self.attack1Count//9], True, False), (self.width, self.height)), (mc.x, mc.y))
            self.attack1Count += 4

        else:
            if self.facingRight:
                scaled = pygame.transform.scale(idle[self.standingCount//9], (self.width, self.height))
                window.blit(scaled, (self.x, self.y))
            else:
                window.blit(pygame.transform.scale(pygame.transform.flip(idle[self.standingCount//9], True, False), (self.width, self.height)), (mc.x, mc.y))
            self.standingCount += 4

    def controls(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] and self.x < 800 - self.width - self.vel:
            self.right = True
            self.facingRight = True
            self.left = False
            self.x += self.vel
        elif keys[pygame.K_LEFT] and self.x > self.vel:
            self.right = False
            self.facingRight = False
            self.left = True
            self.x -= self.vel
        # elif keys[pygame.K_1]:
        #     self.attack1 = True
        else:
            self.right = False
            self.left = False
            self.attack1 = False
            self.walkCount = 0

        if not(self.attack1):
            if keys[pygame.K_1]:
                self.attack1 = True
        else:
            # dealDamage()
            pass

        if not(self.jump):
            if keys[pygame.K_SPACE]:
                self.jump = True
        else:
            if self.jumpCount >= -7:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= (self.jumpCount ** 2) * 0.5 * neg
                self.jumpCount -= 1
            else:
                self.jumpCount = 7
                self.jump = False

def redrawGameWindow():
    window.blit(pygame.transform.scale(bg1[2], (800, 600)), (0, 0))
    window.blit(pygame.transform.scale(bg1[3], (800, 600)), (0, 0))
    window.blit(pygame.transform.scale(bg1[0], (800, 600)), (0, 0))
    window.blit(pygame.transform.scale(bg1[1], (800, 600)), (0, 0))
    mc.drawMC()
    pygame.display.update()

mc = mainChar(0, 425, 50, 37)
game = True
while game == True:
    clock.tick(36)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    mc.controls()
    redrawGameWindow()

pygame.quit()
