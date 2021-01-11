import pygame, sys
from pygame.locals import *
 
# Initialize program
pygame.init()
 
# Assign FPS a value
FPS = 60
w, h = 600, 600
FramePerSec = pygame.time.Clock()
 
# Setting up color objects
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
# Setup a 300x300 pixel display with caption
DISPLAYSURF = pygame.display.set_mode((w,h+100))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Example")


# Square class
class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, color=WHITE):
        super().__init__() 
        w, h = 300, 50
        self.image = pygame.Surface((w, h))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect(center = (x, y))
        self.color = color

    def update(self):
        print('button clicked')


class SpriteObject(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__() 
        w, h = 10, 10
        self.original_image = pygame.Surface((w, h))
        self.original_image.fill(RED)
        self.hover_image = pygame.Surface((w, h))
        self.hover_color = GREEN
        self.hover_image.fill(self.hover_color)
        self.image = self.original_image
        self.rect = self.image.get_rect(center = (x, y))

    def update(self, color):
        self.hover_color = color
        self.image = self.hover_image
        print('color changed to', color)

 
# Creating Lines and Shapes
squares = pygame.sprite.Group()
black_btn = Button(w//2, h)
gui = pygame.sprite.Group(
    black_btn
)
x, y = 0, 5
gap = 10
for i in range(w // 10):
    for j in range(h // 10):
        x += gap
        SpriteObject(x, y).add(squares)
    y += gap
    x = 0



# Beginning Game Loop
draw = False
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            [s.update() for s in gui if s.rect.collidepoint(pos)]
            draw = True
        if event.type == pygame.MOUSEBUTTONUP:
            draw = False
    if draw:
        pos = pygame.mouse.get_pos()
        [s.update(black_btn.color) for s in squares if s.rect.collidepoint(pos)]

    DISPLAYSURF.fill(WHITE)
    gui.draw(DISPLAYSURF)
    squares.draw(DISPLAYSURF)
    pygame.display.flip()
    FramePerSec.tick(FPS)
