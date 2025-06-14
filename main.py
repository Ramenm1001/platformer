import pygame

win = pygame.display.set_mode((500, 500))
run = True
player = None
platforms = []
platforms_draw = []
drawing = False
paint = 100
while run:
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            run = False
        if eve.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
        # if eve.type
    mouse = pygame.mouse.get_pos() # (150, 125)
    if drawing and paint > 0:
        # ??????
        platforms_draw.append(?????)
        # paint ???


    win.fill((0, 0, 0))
    for platform in platforms:
        platform.update()
    for platform in platforms_draw:
        platform.update()
    pygame.display.update()
pygame.quit()