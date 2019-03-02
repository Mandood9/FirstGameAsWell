import pygame
import window
import player
import enemies

pygame.init()

pygame.display.set_caption("First Game As Well")
clock = pygame.time.Clock()

mc = player.character(0, 425, 50, 37, 8)
slime = enemies.mob(500, 461, 32, 25, 2, 300, 90)

game = True
while game == True:
    clock.tick(36)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    mc.characterOptions()
    slime.mobOptions(mc)
    window.redrawGameWindow()
    mc.drawCharacter()
    slime.drawMob()
    pygame.display.update()

pygame.quit()
