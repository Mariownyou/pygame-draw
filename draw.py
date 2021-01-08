import pygame, sys
from pygame.locals import *
 
# Initialize program
pygame.init()
 
# Assign FPS a value
FPS = 30
FramePerSec = pygame.time.Clock()
 
# Setting up color objects
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
# Setup a 300x300 pixel display with caption
DISPLAYSURF = pygame.display.set_mode((300,300))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Example")


# Square class
class Square():
    def __init__(self, x, y, w=9, h=9, color=BLACK):
        self.x, self.y = x, y
        self.w, self.h = w, h
        self.color = color
        self.is_clicked = False

    def draw(self):
        pygame.draw.rect(DISPLAYSURF, self.color, (self.x, self.y, self.w, self.h))


class SpriteObject(pygame.sprite.Sprite):
    def __init__(self, x, y, color=RED):
        super().__init__() 
        w, h = 10, 10
        self.original_image = pygame.Surface((w, h))
        self.original_image.fill(GREEN)
        self.hover_image = pygame.Surface((w, h))
        self.hover_image.fill(WHITE)
        self.image = self.original_image
        self.rect = self.image.get_rect(center = (x, y))
        self.hover = False

    def update(self):
        self.image = self.hover_image

 
# Creating Lines and Shapes
squares = []
gap = 11
x, y = 0, 0
for i in range(31):
    for j in range(31):
        new_square = SpriteObject(x, y)
        squares.append(new_square)
        x += gap
    x = 0
    y += gap

group = pygame.sprite.Group(squares)

# Beginning Game Loop
draw = False
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            draw = True

        if event.type == pygame.MOUSEBUTTONUP:
            draw = False
    if draw:
        pos = pygame.mouse.get_pos()
        [s.update() for s in squares if s.rect.collidepoint(pos)]


    DISPLAYSURF.fill(0)
    group.draw(DISPLAYSURF)
    pygame.display.flip()
    FramePerSec.tick(FPS)
