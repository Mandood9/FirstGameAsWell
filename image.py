import pygame

# Characters
hearts = [pygame.image.load('Hearts/PNG/basic/heart.png'), pygame.image.load('Hearts/PNG/basic/background.png')]

idle = [pygame.image.load('MC/adventurer-idle-2-00.png'), pygame.image.load('MC/adventurer-idle-2-01.png'), pygame.image.load('MC/adventurer-idle-2-02.png'), pygame.image.load('MC/adventurer-idle-2-03.png')]

walkRight = [pygame.image.load('MC/adventurer-run-00.png'), pygame.image.load('MC/adventurer-run-01.png'), pygame.image.load('MC/adventurer-run-02.png'), pygame.image.load('MC/adventurer-run-03.png'), pygame.image.load('MC/adventurer-run-04.png'), pygame.image.load('MC/adventurer-run-05.png')]

jumping = [pygame.image.load('MC/adventurer-smrslt-00.png'), pygame.image.load('MC/adventurer-smrslt-01.png'), pygame.image.load('MC/adventurer-smrslt-02.png'), pygame.image.load('MC/adventurer-smrslt-03.png')]

attack1 = [pygame.image.load('MC/adventurer-attack1-01.png'), pygame.image.load('MC/adventurer-attack1-02.png'), pygame.image.load('MC/adventurer-attack1-03.png'), pygame.image.load('MC/adventurer-attack1-04.png')]

attack2 = [pygame.image.load('MC/adventurer-attack2-00.png'), pygame.image.load('MC/adventurer-attack2-01.png'), pygame.image.load('MC/adventurer-attack2-02.png'), pygame.image.load('MC/adventurer-attack2-03.png'), pygame.image.load('MC/adventurer-attack2-04.png'), pygame.image.load('MC/adventurer-attack2-05.png')]

# attack3 = [pygame.image.load('MC/adventurer-attack3-01.png'), pygame.image.load('MC/adventurer-attack3-01.png'), pygame.image.load('MC/adventurer-attack3-02.png'), pygame.image.load('MC/adventurer-attack3-03.png'), pygame.image.load('MC/adventurer-attack3-04.png'), pygame.image.load('MC/adventurer-attack3-05.png')]

airAttack = [pygame.image.load('MC/adventurer-air-attack1-00.png'), pygame.image.load('MC/adventurer-air-attack1-01.png'), pygame.image.load('MC/adventurer-air-attack1-02.png'), pygame.image.load('MC/adventurer-air-attack1-03.png')]

hurt = [pygame.image.load('MC/adventurer-hurt-00.png'), pygame.image.load('MC/adventurer-hurt-01.png'), pygame.image.load('MC/adventurer-hurt-02.png')]

die = [pygame.image.load('MC/adventurer-die-00.png'), pygame.image.load('MC/adventurer-die-01.png'), pygame.image.load('MC/adventurer-die-02.png'), pygame.image.load('MC/adventurer-die-03.png'), pygame.image.load('MC/adventurer-die-04.png'), pygame.image.load('MC/adventurer-die-05.png')]



# Enemies
slimeIdle = [pygame.image.load('Slime/Sprites/slime-idle-0.png'), pygame.image.load('Slime/Sprites/slime-idle-1.png'), pygame.image.load('Slime/Sprites/slime-idle-2.png'), pygame.image.load('Slime/Sprites/slime-idle-3.png')]

slimeMove = [pygame.image.load('Slime/Sprites/slime-move-0.png'), pygame.image.load('Slime/Sprites/slime-move-1.png'), pygame.image.load('Slime/Sprites/slime-move-2.png'), pygame.image.load('Slime/Sprites/slime-move-3.png')]

slimeAttack = [pygame.image.load('Slime/Sprites/slime-attack-1.png'), pygame.image.load('Slime/Sprites/slime-attack-2.png'), pygame.image.load('Slime/Sprites/slime-attack-3.png'), pygame.image.load('Slime/Sprites/slime-attack-4.png')]

slimeHurt = [pygame.image.load('Slime/Sprites/slime-hurt-0.png'), pygame.image.load('Slime/Sprites/slime-hurt-1.png'), pygame.image.load('Slime/Sprites/slime-hurt-2.png'), pygame.image.load('Slime/Sprites/slime-hurt-3.png')]

slimeDie = [pygame.image.load('Slime/Sprites/slime-die-0.png'), pygame.image.load('Slime/Sprites/slime-die-1.png'), pygame.image.load('Slime/Sprites/slime-die-2.png'), pygame.image.load('Slime/Sprites/slime-die-3.png')]

skeletonIdle = []

skeletonMove = []

skeletonAttack = []

skeletonHurt = []

skeletonDie = []

# import pygame
#
# pygame.init()
# # Characters
# idle = [pygame.image.load('MC/adventurer-idle-2-00.png').convert(), pygame.image.load('MC/adventurer-idle-2-01.png').convert(), pygame.image.load('MC/adventurer-idle-2-02.png').convert(), pygame.image.load('MC/adventurer-idle-2-03.png').convert()]
#
# walkRight = [pygame.image.load('MC/adventurer-run-00.png').convert(), pygame.image.load('MC/adventurer-run-01.png').convert(), pygame.image.load('MC/adventurer-run-02.png').convert(), pygame.image.load('MC/adventurer-run-03.png').convert(), pygame.image.load('MC/adventurer-run-04.png').convert(), pygame.image.load('MC/adventurer-run-05.png').convert()]
#
# jumping = [pygame.image.load('MC/adventurer-smrslt-00.png').convert(), pygame.image.load('MC/adventurer-smrslt-01.png').convert(), pygame.image.load('MC/adventurer-smrslt-02.png').convert(), pygame.image.load('MC/adventurer-smrslt-03.png').convert()]
#
# attack1 = [pygame.image.load('MC/adventurer-attack1-01.png').convert(), pygame.image.load('MC/adventurer-attack1-02.png').convert(), pygame.image.load('MC/adventurer-attack1-03.png').convert(), pygame.image.load('MC/adventurer-attack1-04.png').convert()]
#
# attack2 = [pygame.image.load('MC/adventurer-attack2-00.png').convert(), pygame.image.load('MC/adventurer-attack2-01.png').convert(), pygame.image.load('MC/adventurer-attack2-02.png').convert(), pygame.image.load('MC/adventurer-attack2-03.png').convert(), pygame.image.load('MC/adventurer-attack2-04.png').convert(), pygame.image.load('MC/adventurer-attack2-05.png').convert()]
#
# # attack3 = [pygame.image.load('MC/adventurer-attack3-01.png').convert(), pygame.image.load('MC/adventurer-attack3-01.png').convert(), pygame.image.load('MC/adventurer-attack3-02.png').convert(), pygame.image.load('MC/adventurer-attack3-03.png').convert(), pygame.image.load('MC/adventurer-attack3-04.png').convert(), pygame.image.load('MC/adventurer-attack3-05.png').convert()]
#
# airAttack = [pygame.image.load('MC/adventurer-air-attack1-00.png').convert(), pygame.image.load('MC/adventurer-air-attack1-01.png').convert(), pygame.image.load('MC/adventurer-air-attack1-02.png').convert(), pygame.image.load('MC/adventurer-air-attack1-03.png').convert()]
#
# hurt = [pygame.image.load('MC/adventurer-hurt-00.png').convert(), pygame.image.load('MC/adventurer-hurt-01.png').convert(), pygame.image.load('MC/adventurer-hurt-02.png').convert()]
#
# die = [pygame.image.load('MC/adventurer-die-00.png').convert(), pygame.image.load('MC/adventurer-die-01.png').convert(), pygame.image.load('MC/adventurer-die-02.png').convert(), pygame.image.load('MC/adventurer-die-03.png').convert(), pygame.image.load('MC/adventurer-die-04.png').convert(), pygame.image.load('MC/adventurer-die-05.png').convert()]
#
#
#
# # Enemies
# slimeIdle = [pygame.image.load('Slime/Sprites/slime-idle-0.png').convert(), pygame.image.load('Slime/Sprites/slime-idle-1.png').convert(), pygame.image.load('Slime/Sprites/slime-idle-2.png').convert(), pygame.image.load('Slime/Sprites/slime-idle-3.png').convert()]
#
# slimeMove = [pygame.image.load('Slime/Sprites/slime-move-0.png').convert(), pygame.image.load('Slime/Sprites/slime-move-1.png').convert(), pygame.image.load('Slime/Sprites/slime-move-2.png').convert(), pygame.image.load('Slime/Sprites/slime-move-3.png').convert()]
#
# slimeAttack = [pygame.image.load('Slime/Sprites/slime-attack-1.png').convert(), pygame.image.load('Slime/Sprites/slime-attack-2.png').convert(), pygame.image.load('Slime/Sprites/slime-attack-3.png').convert(), pygame.image.load('Slime/Sprites/slime-attack-4.png').convert()]
#
# slimeHurt = [pygame.image.load('Slime/Sprites/slime-hurt-0.png').convert(), pygame.image.load('Slime/Sprites/slime-hurt-1.png').convert(), pygame.image.load('Slime/Sprites/slime-hurt-2.png').convert(), pygame.image.load('Slime/Sprites/slime-hurt-3.png').convert()]
#
# slimeDie = [pygame.image.load('Slime/Sprites/slime-die-0.png').convert(), pygame.image.load('Slime/Sprites/slime-die-1.png').convert(), pygame.image.load('Slime/Sprites/slime-die-2.png').convert(), pygame.image.load('Slime/Sprites/slime-die-3.png').convert()]
#
# skeletonIdle = []
#
# skeletonMove = []
#
# skeletonAttack = []
#
# skeletonHurt = []
#
# skeletonDie = []
