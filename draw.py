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
class Cursor:
    def __init__(self):
        self.type = 'brush'
        self.color = BLACK
cursor = Cursor()


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, type='brush'):
        super().__init__() 
        w, h = 50, 50
        self.image = pygame.Surface((w, h))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect(center = (x, y))
        self.type = type

    def update(self):
        cursor.type = self.type
        print('button clicked')


class Brush(Button):
    def __init__(self, x, y, color):
        super().__init__(x, y)
        self.color = color

    def update(self):
        cursor.type = self.type
        cursor.color = self.color
        print('brush selceted')

class Fill(Button):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.activated = False
        self.type = 'fill'
    
    def update(self):
        self.activated = False if self.activated else True
        print('fill activated')

class Square(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__() 
        w, h = 10, 10
        self.image = pygame.Surface((w, h))
        self.rect = self.image.get_rect(center = (x, y))
        self.empty = True

    def update(self, color):
        self.empty = False
        self.image.fill(color)

    def fill(self, pos):
        if self.empty:
            self.image.fill(cursor.color)
            self.empty = False
            pos = list(pos)
            pos_1 = (pos[0] + 10, pos[1])
            pos_2 = (pos[0] - 10, pos[1])
            pos_3 = (pos[0], pos[1] - 10)
            pos_4 = (pos[0], pos[1] + 10)
            [s.fill(pos_1) for s in squares if s.rect.collidepoint(pos_1)]
            [s.fill(pos_2) for s in squares if s.rect.collidepoint(pos_2)]
            [s.fill(pos_3) for s in squares if s.rect.collidepoint(pos_3)]
            [s.fill(pos_4) for s in squares if s.rect.collidepoint(pos_4)]
            print('fill', pos)

 
# Creating Lines and Shapes
squares = pygame.sprite.Group()
black_btn = Brush(w//2, h+50, BLACK)
red_btn = Brush(w//3, h+50, RED)
fill_btn = Fill(w//4, h+50)
gui = pygame.sprite.Group(
    black_btn,
    red_btn,
    fill_btn
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
            if fill_btn.activated:
                [s.fill(pos) for s in squares if s.rect.collidepoint(pos)]
            
                
        if event.type == pygame.MOUSEBUTTONUP:
            draw = False
    if draw:
        pos = pygame.mouse.get_pos()
        [s.update(cursor.color) for s in squares if s.rect.collidepoint(pos)]

    DISPLAYSURF.fill(WHITE)
    gui.draw(DISPLAYSURF)
    squares.draw(DISPLAYSURF)
    pygame.display.flip()
    FramePerSec.tick(FPS)
