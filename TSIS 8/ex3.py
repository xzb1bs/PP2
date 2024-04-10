import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

brush_size = 10
brush_color = BLACK
eraser_size = 20

def draw_shape(shape, start, end):
    if shape == "rectangle":
        pygame.draw.rect(screen, brush_color, (start, end))
    elif shape == "circle":
        radius = ((start[0] - end[0])**2 + (start[1] - end[1])**2)**0.5
        pygame.draw.circle(screen, brush_color, start, int(radius))
    elif shape == "eraser":
        pygame.draw.circle(screen, WHITE, start, eraser_size)

running = True
drawing = False
start_pos = None
shape_to_draw = "brush"

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                start_pos = event.pos
            elif event.button == 3:
                shape_to_draw = "eraser"
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                start_pos = None
            elif event.button == 3:
                shape_to_draw = "brush"
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                shape_to_draw = "rectangle"
            elif event.key == pygame.K_c:
                shape_to_draw = "circle"
            elif event.key == pygame.K_b:
                brush_color = BLACK
            elif event.key == pygame.K_w:
                brush_color = WHITE
            elif event.key == pygame.K_r:
                brush_color = RED
            elif event.key == pygame.K_g:
                brush_color = GREEN
            elif event.key == pygame.K_b:
                brush_color = BLUE

    if drawing:
        end_pos = pygame.mouse.get_pos()
        draw_shape(shape_to_draw, start_pos, end_pos)

    pygame.display.flip()

pygame.quit()
sys.exit()
