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

def calc_square(x1, x2, y1, y2):
    # Calculate the top-left corner and size of the square
    left = min(x1, x2)
    top = min(y1, y2)
    size = min(abs(x1 - x2), abs(y1 - y2))
    
    return pg.Rect((left, top), (size, size))

def calc_right_triangle(x1, x2, y1, y2):
    # Calculate the vertices of the right triangle
    vertices = [(x1, y1), (x2, y2), (x1, y2)]
    
    return vertices

def calc_equilateral_triangle(x1, x2, y1, y2):
    # Calculate the center of the base
    base_center_x = (x1 + x2) // 2
    base_center_y = y2
    
    # Calculate the height of the triangle
    height = math.sqrt(3) / 2 * (x2 - x1)
    
    # Calculate the vertices of the equilateral triangle
    vertices = [(x1, y2), (x2, y2), (base_center_x, base_center_y - height)]
    
    return vertices

def calc_rhombus(x1, x2, y1, y2):
    # Calculate the center of the rhombus
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2
    
    # Calculate the vertices of the rhombus
    vertices = [(center_x, y1), (x2, center_y), (center_x, y2), (x1, center_y)]
    
    return vertices


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
        if activeshape == 'rectangle':
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
        
        if activeshape == 'square':
            if LMBPressed:
                if activecolor == (255, 255, 255):  # Check if eraser is active
                    pg.draw.rect(screen, (0, 0, 0), calc_square(prevx, currx, prevy, curry))
                else:
                    screen.blit(baselayer, (0, 0))
                    pg.draw.rect(screen, activecolor, calc_square(prevx, currx, prevy, curry), 2)
        
        if activeshape == 'right_triangle':
            if LMBPressed:
                if activecolor == (255, 255, 255):  # Check if eraser is active
                    pg.draw.polygon(screen, (0, 0, 0), calc_right_triangle(prevx, currx, prevy, curry))
                else:
                    screen.blit(baselayer, (0, 0))
                    pg.draw.polygon(screen, activecolor, calc_right_triangle(prevx, currx, prevy, curry), 2)

        if activeshape == 'equilateral_triangle':
            if LMBPressed:
                if activecolor == (255, 255, 255):  # Check if eraser is active
                    pg.draw.polygon(screen, (0, 0, 0), calc_equilateral_triangle(prevx, currx, prevy, curry))
                else:
                    screen.blit(baselayer, (0, 0))
                    pg.draw.polygon(screen, activecolor, calc_equilateral_triangle(prevx, currx, prevy, curry), 2)

        if activeshape == 'rhombus':
            if LMBPressed:
                if activecolor == (255, 255, 255):  # Check if eraser is active
                    pg.draw.polygon(screen, (0, 0, 0), calc_rhombus(prevx, currx, prevy, curry))
                else:
                    screen.blit(baselayer, (0, 0))
                    pg.draw.polygon(screen, activecolor, calc_rhombus(prevx, currx, prevy, curry), 2)

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

            if rectangle.collidepoint(mouse):
                activeshape = 'rectangle'

            if circle.collidepoint(mouse):
                activeshape = 'circle'

            if square.collidepoint(mouse):
                activeshape = 'square'
            
            if right_triangle.collidepoint(mouse):
                activeshape = 'right_triangle'
            
            if equilateral_triangle.collidepoint(mouse):
                activeshape = 'equilateral_triangle'
            
            if rhombus.collidepoint(mouse):
                activeshape = 'rhombus'


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
    
    rectangle = pg.draw.rect(screen, BLACK, [5, 40, 30, 20])
    circle = pg.draw.circle(screen, BLACK, [55, 45], 15)
    square = pg.draw.rect(screen, BLACK, [75, 30, 30, 30])
    right_triangle = pg.draw.polygon(screen, BLACK,[[130,30], [110, 60], [130, 60]])
    equilateral_triangle = pg.draw.polygon(screen, BLACK, [[160, 30], [140, 60], [180,60]])
    rhombus = pg.draw.polygon(screen, BLACK, [[210, 25], [230, 45], [210, 65], [190, 45]])
    pg.display.flip()
    clock.tick(fps)