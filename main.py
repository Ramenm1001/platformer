import pygame
pygame.init()
class Platforms:
    def __init__(self, x, y, width=20, height=10, color=(0,255,0)):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self):
        pygame.draw.rect(win, self.color, self.rect )

    def update(self):
        self.draw()
class Player:
    def __init__(self, x, y, width=15, height=40, color=(185, 122, 87)):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self):
        pygame.draw.rect(win, self.color, self.rect )
    def move(self):
        pass
    def update(self):
        self.draw()
        self.move()


win = pygame.display.set_mode((500, 500))
run = True
player = Player(50, 0)
platforms = [Platforms(50, 80, 150),
             Platforms(100, 100)]
platforms_draw = []
drawing = False
erase = False
paint = 700
font = pygame.font.Font(None, 32)
text = font.render(f"краска str(paint)",
                   False,
                   (255, 255, 255))
paint = 820

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
        plat = Platforms(mouse[0], mouse[1])
        screen = pygame.Rect(0, 0, 500, 500)
        if screen.colliderect(plat.rect):
            platforms_draw.append(plat)
            paint -= 1

    if erase:
        eraser = pygame.Rect(*mouse, 10, 10)
        for platform in platforms_draw:
            if platform.rect.colliderect(eraser):
                platforms_draw.remove(platform)
                paint += 1
    text = font.render(f"краска {str(paint)}",
                       True,
                       (255, 255, 255))

    win.fill((0, 0, 0))
    for platform in platforms:
        platform.update()
    for platform in platforms_draw:
        platform.update()
    player.update()
    win.blit(text, (10, 10))
    pygame.display.update()
pygame.quit()
