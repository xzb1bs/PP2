import pygame 
from sys import exit 

pygame.init()

screen = pygame.display.set_mode((1200, 800))

clock = pygame.time.Clock()
x = 400
y = 300
radius = 25
while True:
    screen.fill((255,255,255))
    circle = pygame.draw.circle(screen, (255, 0, 0),(x, y), radius)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_RIGHT] and x + 20 + radius< 1200: 
        x += 20
    if keys[pygame.K_LEFT] and x - 20 - radius> 0: 
        x -= 20
    if keys[pygame.K_UP]and y - 20 - radius> 0: 
        y -= 20
    if keys[pygame.K_DOWN]and y + 20 + radius< 800: 
        y += 20
    
    pygame.display.flip()
    clock.tick(60)