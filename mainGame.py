import pygame
import image
import window
import sprites
import pytmx

pygame.init()

win = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("First Game As Well")
clock = pygame.time.Clock()

map = pytmx.load_pygame('MagicCliffsMap1.tmx')

mc = sprites.character(0, 534, 50, 37)
background = window.background()
slime = sprites.slime(500, 558, 32, 25)

enemies = {
    "slime": [],
    "skeleton": []
}

enemies["slime"].append(slime)

game = True
while game == True:
    clock.tick(36)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    mc.characterOptions()
    slime.slimeOptions(mc)
    background.drawBackground(mc)
    for layer in map:
        for x, y, gid in layer:
            tile = map.get_tile_image_by_gid(gid)
            if tile:
                win.blit(tile, (x * map.tilewidth, y * map.tileheight))

    mc.drawCharacter()
    mc.drawHearts()
    slime.drawSlime()
    mc.characterAttackAnim(enemies, "slime")
    slime.slimeAttackAnim(mc)

    pygame.draw.rect(window.win, (255, 255, 255), (mc.x, mc.y, mc.width, mc.height), 1)
    pygame.draw.rect(window.win, (255, 255, 255), (mc.x + 45, mc.y, mc.width - 90, mc.height), 1)
    pygame.draw.rect(window.win, (255, 255, 255), (slime.x, slime.y + 20, slime.width, slime.height - 20), 1)
    pygame.display.update()

pygame.quit()
