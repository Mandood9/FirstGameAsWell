import pygame

pygame.init()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("First Game As Well")

x = 50
y = 50
width = 40
height = 60
vel = 5

is_jump = False
jump_count = 10
clock = pygame.time.Clock()

game = True
while game == True:
    pygame.time.delay(50)
#    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 800 - width - vel:
        x += vel
    if not(is_jump):
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < 600 - height - vel:
            y += vel
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 10

    window.fill((0, 0, 0))
    pygame.draw.rect(window, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()
