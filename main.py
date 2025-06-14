import pygame
class Platforms:
    def __init__(self, x, y, width=20, height=10, color=(0,255,0)):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self):
        pygame.draw.rect(win, self.color, self.rect )

    def update(self):
        self.draw()


win = pygame.display.set_mode((500, 500))
run = True
player = None
platforms = [Platforms(50, 80, 150),
             Platforms(100, 100)]
platforms_draw = []
drawing = False
erase = False
paint = 700

while run:
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            run = False
        if eve.type == pygame.MOUSEBUTTONDOWN:
            if eve.button == 1:
                drawing = True
            if eve.button == 3:
                erase = True
        if eve.type == pygame.MOUSEBUTTONUP:
            if eve.button == 1:
                drawing = False
            if eve.button == 3:
                erase = False
    mouse = pygame.mouse.get_pos() # (150, 125)
    if drawing and paint > 0:
        platforms_draw.append(Platforms(mouse[0], mouse[1]))
        paint -= 1

    if erase:
        eraser = pygame.Rect(*mouse, 10, 10)
        for platform in platforms_draw:
            if platform.rect.colliderect(eraser):
                platforms_draw.remove(platform)
                paint += 1
    print(paint)
    win.fill((0, 0, 0))
    for platform in platforms:
        platform.update()
    for platform in platforms_draw:
        platform.update()
    pygame.display.update()
pygame.quit()
