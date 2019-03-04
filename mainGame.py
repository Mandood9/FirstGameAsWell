import pygame
import image
import window
import sprites


pygame.init()

pygame.display.set_caption("First Game As Well")
clock = pygame.time.Clock()

mc = sprites.character(0, 425, 50, 37)
slime = sprites.slime(500, 461, 32, 25)

def mcAttacks(mc):
    if mc.attack1Count >= 9 and mc.attack1Count <= 18:
        return True
    elif mc.attack2Count >= 24 and mc.attack2Count <= 30:
        return True
    else:
        return False, 0

def slimeAttacks(slime):
    if slime.attackCount >= 9 and slime.attackCount <= 18:
        return True
    else:
        return False

def hit(attacker, victim):
    if ((attacker.x >= victim.x and attacker.x <= victim.x + victim.width) or (attacker.x + attacker.width <= victim.x + victim.width and attacker.x + attacker.width >= victim.x)) and (attacker.y + attacker.height/2 >= victim.y and attacker.y + attacker.height/2 <= victim.y + victim.height):
        if attacker.attack1:
            return True #, 1
        if attacker.attack2:
            return True #, 2
        if attacker.airAttack:
            return True #, 1
        # if attacker.attack:
        #     return True #, 1
    else:
        return False, 0

game = True
while game == True:
    clock.tick(36)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    mc.characterOptions()
    slime.slimeOptions(mc)
    window.redrawGameWindow()
    # if slimeAttacks(slime) or skeletonAttacks(skeleton):
    mc.drawCharacter(False, 0)
    # else:
    #     mc.drawCharacter(False, 0)
    if mcAttacks(mc):
        slime.drawSlime(hit(mc, slime), 1)
    else:
        slime.drawSlime(False, 0)
    pygame.display.update()

pygame.quit()
