import pygame
import window
import image
import random

pygame.init()

# class collision():
#     def __init__(self, object1x, object1y, object1Width, object1Height, object2x, object2y, object2Width, object2Height):
#         self.object1x = object1x
#         self.object1y = object1y
#         self.object1Width = object1Width
#         self.object1Height = object1Height
#         self.object2x = object2x
#         self.object2y = object2y
#         self.object2Width = object2Width
#         self.object2Height = object2Height
#
#     def hit(self):
#         if ((self.object1x >= self.object2x and self.object1x <= self.object2x + self.object2Width) or (self.object1x + self.object1Width <= self.object2x + self.object2Width and self.object1x + self.object1Width >= self.object2x)) and (self.object1y + self.object1Height/2 >= self.object2y and self.object1y + self.object1Height/2 <= self.object2y + self.object2Height):
#             return True
#         else:
#             return False
#
#     def ground(self):
#         pass

class character():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width * 2
        self.height = height * 2
        self.vel = 8
        self.health = 5
        self.jumpHeight = 8
        self.attack1Damage = 1
        self.attack2Damage = 2

        self.alive = True
        self.switch = True
        self.right = True
        self.left = False
        self.jump = False
        self.attack1 = False
        self.attack2 = False
        self.airAttack = False
        self.hit = False

        self.hitCount = 0
        self.dieCount = 0
        self.standingCount = 0
        self.moveCount = 0
        self.jumpCount = 0
        self.attack1Count = 0
        self.attack2Count = 0
        self.airAttackCount = 0

    def characterOptions(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] and not(self.attack1) and not(self.attack2) and not(self.hit):
            self.right = True
            self.left = False
            self.switch = True
            if self.x < 512 - self.width - self.vel:
                self.vel = 8
                self.x += self.vel
            else:
                self.vel = 0
        elif keys[pygame.K_LEFT] and self.x > self.vel and not(self.attack1) and not(self.attack2) and not(self.hit):
            self.right = False
            self.left = True
            self.switch = False
            self.vel = 8
            self.x -= self.vel
        else:
            self.right = False
            self.left = False
            self.moveCount = 0
            self.jumpCount = 0

        if not(self.jump):
            if keys[pygame.K_SPACE] and not(self.attack1) and not(self.attack2) and not(self.hit):
                self.jump = True
        else:
            if not(self.airAttack):
                if keys[pygame.K_1]:
                    self.airAttack = True
            if self.jumpHeight >= -8:
                neg = 1
                if self.jumpHeight < 0:
                    neg = -1
                self.y -= (self.jumpHeight ** 2) * 0.5 * neg
                self.jumpHeight -= 1
            else:
                self.jumpHeight = 8
                self.airAttackCount = 0
                self.jump = False
                self.airAttack = False

        if not(self.attack1) and not(self.jump):
            if keys[pygame.K_1] and not(self.attack2):
                self.attack1 = True
        if not(self.attack2) and not(self.jump):
            if keys[pygame.K_2] and not(self.attack1):
                self.attack2 = True

    def drawCharacter(self):
        if self.hitCount + 1 >= 36:
            self.hitCount = 0
            self.attack1Count = 0
            self.attack2Count = 0
            self.hit = False
        if self.dieCount + 1 >= 36:
            self.dieCount = 0
            self.alive = False
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

        if not(self.alive):
            pass
        elif self.hit:
            if self.health <= 0:
                if self.switch:
                    window.win.blit(pygame.transform.scale(image.die[self.dieCount//6], (self.width, self.height)), (self.x, self.y))
                    self.dieCount += 1
                else:
                    window.win.blit(pygame.transform.scale(pygame.transform.flip(image.die[self.dieCount//6], True, False), (self.width, self.height)), (self.x, self.y))
                    self.dieCount += 1
            else:
                if self.switch:
                    window.win.blit(pygame.transform.scale(image.hurt[self.hitCount//12], (self.width, self.height)), (self.x, self.y))
                    self.hitCount += 6
                else:
                    window.win.blit(pygame.transform.scale(pygame.transform.flip(image.hurt[self.hitCount//12], True, False), (self.width, self.height)), (self.x, self.y))
                    self.hitCount += 6
        elif self.attack1:
            if self.switch:
                window.win.blit(pygame.transform.scale(image.attack1[self.attack1Count//9], (self.width, self.height)), (self.x, self.y))
                self.attack1Count += 3
            else:
                window.win.blit(pygame.transform.scale(pygame.transform.flip(image.attack1[self.attack1Count//9], True, False), (self.width, self.height)), (self.x, self.y))
                self.attack1Count += 3
        elif self.attack2:
            if self.switch:
                window.win.blit(pygame.transform.scale(image.attack2[self.attack2Count//6], (self.width, self.height)), (self.x, self.y))
                self.attack2Count += 2
            else:
                window.win.blit(pygame.transform.scale(pygame.transform.flip(image.attack2[self.attack2Count//6], True, False), (self.width, self.height)), (self.x, self.y))
                self.attack2Count += 2
        elif self.right:
            if self.jump:
                if self.airAttack:
                    window.win.blit(pygame.transform.scale(image.airAttack[self.airAttackCount//9], (self.width, self.height)), (self.x, self.y))
                    self.airAttackCount += 3
                else:
                    window.win.blit(pygame.transform.scale(image.jumping[self.jumpCount//9], (self.width, self.height)), (self.x, self.y))
                    self.jumpCount += 3
            else:
                window.win.blit(pygame.transform.scale(image.walkRight[self.moveCount//6], (self.width, self.height)), (self.x, self.y))
                self.moveCount += 3
        elif self.left:
            if self.jump:
                if self.airAttack:
                    window.win.blit(pygame.transform.scale(pygame.transform.flip(image.airAttack[self.airAttackCount//9], True, False), (self.width, self.height)), (self.x, self.y))
                    self.airAttackCount += 3
                else:
                    window.win.blit(pygame.transform.scale(pygame.transform.flip(image.jumping[self.jumpCount//9], True, False), (self.width, self.height)), (self.x, self.y))
                    self.jumpCount += 3
            else:
                window.win.blit(pygame.transform.scale(pygame.transform.flip(image.walkRight[self.moveCount//6], True, False), (self.width, self.height)), (self.x, self.y))
                self.moveCount += 3
        elif self.jump:
            if self.switch:
                if self.airAttack:
                    window.win.blit(pygame.transform.scale(image.airAttack[self.airAttackCount//9], (self.width, self.height)), (self.x, self.y))
                    self.airAttackCount += 3
                else:
                    window.win.blit(pygame.transform.scale(image.jumping[self.jumpCount//9], (self.width, self.height)), (self.x, self.y))
                    self.jumpCount += 3
            else:
                if self.airAttack:
                    window.win.blit(pygame.transform.scale(pygame.transform.flip(image.airAttack[self.airAttackCount//9], True, False), (self.width, self.height)), (self.x, self.y))
                    self.airAttackCount += 3
                else:
                    window.win.blit(pygame.transform.scale(pygame.transform.flip(image.jumping[self.jumpCount//9], True, False), (self.width, self.height)), (self.x, self.y))
                    self.jumpCount += 3
        else:
            if self.switch:
                window.win.blit(pygame.transform.scale(image.idle[self.standingCount//9], (self.width, self.height)), (self.x, self.y))
                self.standingCount += 3
            else:
                window.win.blit(pygame.transform.scale(pygame.transform.flip(image.idle[self.standingCount//9], True, False), (self.width, self.height)), (self.x, self.y))
                self.standingCount += 3

    def drawHearts(self):
        pos = 10
        for num in range(self.health):
            window.win.blit(pygame.transform.scale(image.hearts[0], (25, 25)), (pos, 10))
            pos += 30
        for num in range(5 - self.health):
            window.win.blit(pygame.transform.scale(image.hearts[1], (25, 25)), (pos, 10))
            pos += 30

    def characterAttackAnim(self, enemies, type):
        if self.attack1Count >= 12 and self.attack1Count <= 14:
            for enemy in enemies[type]:
                if not(enemy.hit) and (self.x - enemy.x >= 0 and self.x - enemy.x - enemy.width <= 0) or (self.x + self.width - enemy.x - enemy.width <= 0 and self.x + self.width - enemy.x >= 0):
                    enemy.health -= self.attack1Damage
                    enemy.hit = True
                    enemy.hitCount = 0
                    break
        if self.attack2Count >= 24 and self.attack2Count <= 29:
            for enemy in enemies[type]:
                if not(enemy.hit) and (self.x - enemy.x >= 0 and self.x - enemy.x - enemy.width <= 0) or (self.x + self.width - enemy.x - enemy.width <= 0 and self.x + self.width - enemy.x >= 0):
                    enemy.health -= self.attack2Damage
                    enemy.hit = True
                    enemy.hitCount = 0
                    break

class mob():
    def __init__(self, x, y, width, height): # vel, sightRange, attackRange, health):
        self.x = x
        self.y = y
        self.width = width * 2
        self.height = height * 2
        # self.vel = vel
        # self.sightRange = sightRange
        # self.attackRange = attackRange
        # self.health = health

        self.alive = True
        self.hit = False
        self.detected = False
        self.left = True
        self.attack = False
        self.switch = False

        self.hitCount = 0
        self.dieCount = 0
        self.idleCount = 0
        self.dir = random.randint(0, 1)
        self.moveCount = 0
        self.attackCount = 0

    def mobOptions(self, player):
        if (abs(self.x - player.x) <= self.sightRange or self.detected) and not(self.hit):
            self.detected = True

            if self.x - player.x > 0:
                self.left = True
                self.switch = False

                if abs(self.x - player.x) <= self.attackRange or self.attack:
                    self.attack = True
                    self.moveCount = 0
                else:
                    self.attack = False
                    self.attackCount = 0
                    self.x -= self.vel
            else:
                self.left = False
                self.switch = True

                if abs(self.x - player.x) <= self.attackRange - 50 or self.attack:
                    self.attack = True
                    self.moveCount = 0
                else:
                    self.attack = False
                    self.attackCount = 0
                    self.x += self.vel

class slime(mob):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

        self.vel = 2
        self.sightRange = 300
        self.attackRange = 85
        self.health = 2
        self.attackDamage = 1

    def slimeOptions(self, player):
        super().mobOptions(player)

    def drawSlime(self): # slimeIdle, slimeMove, slimeAttack, slimeHurt, slimeDie):
        if self.hitCount + 1 >= 36:
            self.hitCount = 0
            self.hit = False
        if self.dieCount + 1 >= 36:
            self.dieCount = 0
            self.alive = False
        if self.idleCount + 1 >= 36:
            self.idleCount = 0
        if self.moveCount + 1 >= 36:
            self.moveCount = 0
        if self.attackCount + 1 >= 72:
            self.attack = False
            self.attackCount = 0

        if not(self.alive):
            pass
        elif self.health <= 0:
            if not(self.switch):
                window.win.blit(pygame.transform.scale(image.slimeDie[self.dieCount//9], (self.width, self.height)), (self.x, self.y))
                self.dieCount += 3
            else:
                window.win.blit(pygame.transform.scale(pygame.transform.flip(image.slimeDie[self.dieCount//9], True, False), (self.width, self.height)), (self.x, self.y))
                self.dieCount += 3
        elif self.hit:
            self.attackCount = 0
            self.moveCount = 0
            if not(self.switch):
                window.win.blit(pygame.transform.scale(image.slimeHurt[self.hitCount//9], (self.width, self.height)), (self.x, self.y))
                self.hitCount += 3
            else:
                window.win.blit(pygame.transform.scale(pygame.transform.flip(image.slimeHurt[self.hitCount//9], True, False), (self.width, self.height)), (self.x, self.y))
                self.hitCount += 3
        elif self.detected:
            if self.left:
                if self.attack:
                    #draw left attack animation
                    window.win.blit(pygame.transform.scale(image.slimeAttack[self.attackCount//18], (self.width, self.height)), (self.x, self.y))
                    self.attackCount += 1
                else:
                    #draw left move animation
                    window.win.blit(pygame.transform.scale(image.slimeMove[self.moveCount//18], (self.width, self.height)), (self.x, self.y))
                    self.moveCount += 1
            else:
                if self.attack:
                    #draw right attack animation
                    window.win.blit(pygame.transform.scale(pygame.transform.flip(image.slimeAttack[self.attackCount//18], True, False), (self.width, self.height)), (self.x, self.y))
                    self.attackCount += 1
                else:
                    pass
                    #draw right move animation
                    window.win.blit(pygame.transform.scale(pygame.transform.flip(image.slimeMove[self.moveCount//9], True, False), (self.width, self.height)), (self.x, self.y))
                    self.moveCount += 1
        else:
            #draw idle animation
            if self.dir == 0:
                window.win.blit(pygame.transform.scale(image.slimeIdle[self.idleCount//9], (self.width, self.height)), (self.x, self.y))
            else:
                window.win.blit(pygame.transform.scale(pygame.transform.flip(image.slimeIdle[self.idleCount//9], True, False), (self.width, self.height)), (self.x, self.y))
            self.idleCount += 1

    def slimeAttackAnim(self, mc):
        if self.attackCount >= 24 and self.attackCount <= 28 and not(mc.hit):
            if ((self.x - mc.x >= 0 and self.x - mc.x - mc.width <= 0) or (self.x + self.width - mc.x - mc.width <= 0 and self.x + self.width - mc.x >= 0)) and (self.y + self.height/2 >= mc.y and self.y + self.height/2 <= mc.y + mc.height) and not(mc.hit):
                mc.health -= self.attackDamage
                mc.hit = True

class skeleton(mob):
    pass
