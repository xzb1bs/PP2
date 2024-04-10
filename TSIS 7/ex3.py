import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Ball")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

ball_radius = 25
ball_x = (screen_width - ball_radius) // 2
ball_y = (screen_height - ball_radius) // 2
ball_speed = 20

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        ball_y -= ball_speed
    if keys[pygame.K_DOWN]:
        ball_y += ball_speed
    if keys[pygame.K_LEFT]:
        ball_x -= ball_speed
    if keys[pygame.K_RIGHT]:
        ball_x += ball_speed

    if ball_x < 0:
        ball_x = 0
    if ball_x > screen_width - ball_radius:
        ball_x = screen_width - ball_radius
    if ball_y < 0:
        ball_y = 0
    if ball_y > screen_height - ball_radius:
        ball_y = screen_height - ball_radius

    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    pygame.display.update()

    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()