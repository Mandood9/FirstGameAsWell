import pygame

pygame.init()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("First Game As Well")

bg = [pygame.image.load('BG1/BGF/BGBack.png'), pygame.image.load('BG1/BGF/BGFront.png'), pygame.image.load('BG1/BGF/CloudsBack.png'), pygame.image.load('BG1/BGF/CloudsFront.png')]

walkRight = [pygame.image.load('MC/adventurer-run-00.png'), pygame.image.load('MC/adventurer-run-01.png'), pygame.image.load('MC/adventurer-run-02.png'), pygame.image.load('MC/adventurer-run-03.png'), pygame.image.load('MC/adventurer-run-04.png'), pygame.image.load('MC/adventurer-run-05.png')]

idle = [pygame.image.load('MC/adventurer-idle-2-00.png'), pygame.image.load('MC/adventurer-idle-2-01.png'), pygame.image.load('MC/adventurer-idle-2-02.png'), pygame.image.load('MC/adventurer-idle-2-03.png')]

jumping = [pygame.image.load('MC/adventurer-smrslt-00.png'), pygame.image.load('MC/adventurer-smrslt-01.png'), pygame.image.load('MC/adventurer-smrslt-02.png'), pygame.image.load('MC/adventurer-smrslt-03.png')]

clock = pygame.time.Clock()

class mainChar():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.standing = True
        self.right = False
        self.left = False
        self.jump = False
        self.standingCount = 0
        self.walkCount = 0
        self.jumpFrame = 0
        self.jumpCount = 8

    def drawMC(self):
        if self.walkCount + 1 >= 36:
            self.walkCount = 0
        if self.standingCount + 1 >= 36:
            self.standingCount = 0

        if self.right:
            window.blit(pygame.transform.scale(walkRight[self.walkCount//6], (self.width * 3, self.height * 3)), (mc.x, mc.y))
            self.walkCount += 6
        elif self.left:
            window.blit(pygame.transform.scale(pygame.transform.flip(walkRight[self.walkCount//6], True, False), (self.width * 3, self.height * 3)), (mc.x, mc.y))
            self.walkCount += 6
        else:
            scaled = pygame.transform.scale(idle[self.standingCount//9], (self.width * 3, self.height * 3))
            window.blit(scaled, (self.x, self.y))
            self.standingCount += 4

    def controls(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] and self.x < 800 - self.width - self.vel:
            self.right = True
            self.left = False
            self.x += self.vel
        elif keys[pygame.K_LEFT] and self.x > self.vel:
            self.right = False
            self.left = True
            self.x -= self.vel
        else:
            self.right = False
            self.left = False
            self.walkCount = 0

        if not(self.jump):
            if keys[pygame.K_SPACE]:
                self.jump = True
        else:
            if self.jumpCount >= -9:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= (self.jumpCount ** 2) * 0.5 * neg
                self.jumpCount -= 1
            else:
                self.jumpCount = 9
                self.jump = False

def redrawGameWindow():
    window.blit(pygame.transform.scale(bg[2], (800, 600)), (0, 0))
    window.blit(pygame.transform.scale(bg[3], (800, 600)), (0, 0))
    window.blit(pygame.transform.scale(bg[0], (800, 600)), (0, 0))
    window.blit(pygame.transform.scale(bg[1], (800, 600)), (0, 0))
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
