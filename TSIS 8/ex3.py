import pygame as pg
import math
pg.init()

screen = pg.display.set_mode((600, 600))
screen.fill((255, 255, 255))  # Set background color to white
baselayer = pg.Surface((600, 600))

clock = pg.time.Clock()
fps = 60

prevx = -1 
prevy = -1

currx = -1
curry = -1

LMBPressed = False

text_font = pg.font.SysFont(None, 30)

activecolor = (255, 255, 255)
activeshape = None


BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
PURPLE = (255, 0, 255)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def calc_rect(x1, x2, y1, y2):
    return pg.Rect((min(x1, x2), min(y1, y2)), (abs(x1 - x2), abs(y1 - y2)))

def calc_circle(x1, x2, y1, y2):
    # Calculate the center and radius of the circle
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2
    radius = math.ceil(math.sqrt((x2 - x1)**2 + (y2 - y1)**2) / 2)
    
    return (center_x, center_y), radius

def draw_header():
    global eraser, blue, red, green, yellow, black, purple
    rect = pg.draw.rect(screen, (229,255,204), [0, 0, 600, 86]) 
    circle = pg.draw.line(screen, 'gray', [0, 85], [600, 85]) 
    
    blue = pg.draw.rect(screen, (0, 0, 255), [600 - 35, 35, 25, 25])
    red = pg.draw.rect(screen, (255, 0, 0), [600 - 35, 60, 25, 25])
    green = pg.draw.rect(screen, (0, 255, 0), [600 - 60, 35, 25, 25])
    yellow = pg.draw.rect(screen, (255, 255, 0), [600 - 60, 60, 25, 25])
    black = pg.draw.rect(screen, (0, 0, 0), [600 - 85, 35, 25, 25])
    purple = pg.draw.rect(screen, (255, 0, 255), [600 - 85, 60, 25, 25])
    eraser = pg.draw.rect(screen, (253, 166, 215), [300, 30, 50, 50])

def draw():
    global activecolor, activeshape, mouse, prevx, prevy, currx, curry, LMBPressed
    if mouse[1] > 100:
        if activeshape == 'rect':
            if LMBPressed:
                if activecolor == (255, 255, 255):  # Check if eraser is active
                    pg.draw.rect(screen, (0, 0, 0), calc_rect(prevx, currx, prevy, curry))
                else:
                    screen.blit(baselayer, (0, 0))
                    pg.draw.rect(screen, activecolor, calc_rect(prevx, currx, prevy, curry), 2)
                    
        if activeshape == 'circle':
            if LMBPressed:
                center, radius = calc_circle(prevx, currx, prevy, curry)
                if activecolor == (255, 255, 255):  # Check if eraser is active
                    pg.draw.circle(screen, (0, 0, 0), center, radius)
                else:
                    screen.blit(baselayer, (0, 0))
                    pg.draw.circle(screen, activecolor, center, radius, 2)



while True:
    
    mouse = pg.mouse.get_pos()
    draw()
    click = pg.mouse.get_pressed()[0] # Get Mouse Button Pressed

    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            LMBPressed = True
            prevx = event.pos[0]
            prevy = event.pos[1]
            currx = event.pos[0]
            curry = event.pos[1]

            if shape_1.collidepoint(mouse):
                activeshape = 'rect'

            if shape_2.collidepoint(mouse):
                activeshape = 'circle'

            if eraser.collidepoint(mouse):  # Check if eraser is clicked
                screen.fill((255, 255, 255))
            
            if blue.collidepoint(mouse):
                activecolor = BLUE
            elif red.collidepoint(mouse):
                activecolor = RED
            elif green.collidepoint(mouse):
                activecolor = GREEN
            elif black.collidepoint(mouse):
                activecolor = BLACK
            elif purple.collidepoint(mouse):
                activecolor = PURPLE
            elif yellow.collidepoint(mouse):
                activecolor = YELLOW

        if event.type == pg.MOUSEMOTION:
            if LMBPressed:
                currx = event.pos[0]
                curry = event.pos[1]

        if event.type == pg.MOUSEBUTTONUP and event.button == 1:
            LMBPressed = False
            baselayer.blit(screen, (0, 0))
            if activecolor == (255, 255, 255):
                activecolor = (0, 0, 0)
    draw_header()
    draw_text("Choose the Shape", text_font, (255, 0, 0), 10, 5)
    draw_text("Eraser", text_font, (255, 0, 0), 295, 5)
    draw_text("Colors", text_font, (255, 0, 0), 520, 5)
    
    shape_1 = pg.draw.rect(screen, (0, 0, 0), [20, 30, 50, 50])
    shape_2 = pg.draw.circle(screen, (0, 0, 0), [135, 55], 30)
    pg.display.flip()
    clock.tick(fps)