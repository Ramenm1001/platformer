import pygame

win = pygame.display.set_mode((500, 500))
run = True
player = None
platforms = []
while run:
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            run = False

    win.fill((0,0,0))
    for platform in platforms:
        platform.update()
    pygame.display.update()
pygame.quit()