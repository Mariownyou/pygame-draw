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
pygame.display.set_caption("Paint Levushka")


# Square class
current_color = BLACK
class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, color=BLACK):
        super().__init__() 
        w, h = 50, 50
        self.image = pygame.Surface((w, h))
        self.image.fill(color)
        self.rect = self.image.get_rect(center = (x, y))
        self.color = color

    def update(self):
        global current_color
        current_color = self.color
        print('button clicked', current_color)


class Square(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__() 
        w, h = 10, 10
        self.image = pygame.Surface((w, h))
        self.rect = self.image.get_rect(center = (x, y))

    def update(self, color):
        self.image.fill(color)

    def fill(self):
        pass

 
# Creating Lines and Shapes
squares = pygame.sprite.Group()
black_btn = Button(w//2, h+50, BLACK)
red_btn = Button(w//3, h+50, RED)
gui = pygame.sprite.Group(
    black_btn,
    red_btn
)
x, y = 0, 5
gap = 10
for i in range(w // 10):
    for j in range(h // 10):
        x += gap
        new = Square(x, y)
        new.add(squares)
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
        [s.update(current_color) for s in squares if s.rect.collidepoint(pos)]

    DISPLAYSURF.fill(WHITE)
    gui.draw(DISPLAYSURF)
    squares.draw(DISPLAYSURF)
    pygame.display.flip()
    FramePerSec.tick(FPS)
