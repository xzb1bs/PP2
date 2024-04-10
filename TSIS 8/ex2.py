import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

block_size = 20
snake_speed = 10
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = "RIGHT"

food_position = [random.randrange(1, (WIDTH // block_size)) * block_size,
                 random.randrange(1, (HEIGHT // block_size)) * block_size]

score = 0
level = 1

def display_info():
    font = pygame.font.SysFont("comicsansms", 25)
    score_text = font.render("Score: " + str(score), True, RED)
    level_text = font.render("Level: " + str(level), True, RED)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

def draw_snake(snake_body):
    for block in snake_body:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], block_size, block_size])

def generate_food():
    food_x = random.randrange(1, (WIDTH // block_size)) * block_size
    food_y = random.randrange(1, (HEIGHT // block_size)) * block_size
    return food_x, food_y

running = True
clock = pygame.time.Clock()
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                snake_direction = "LEFT"
            elif event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                snake_direction = "RIGHT"
            elif event.key == pygame.K_UP and snake_direction != "DOWN":
                snake_direction = "UP"
            elif event.key == pygame.K_DOWN and snake_direction != "UP":
                snake_direction = "DOWN"

    if (snake_body[0][0] >= WIDTH or snake_body[0][0] < 0 or
            snake_body[0][1] >= HEIGHT or snake_body[0][1] < 0):
        running = False

    for block in snake_body[1:]:
        if snake_body[0] == block:
            running = False

    if snake_direction == "RIGHT":
        snake_body[0][0] += block_size
    elif snake_direction == "LEFT":
        snake_body[0][0] -= block_size
    elif snake_direction == "UP":
        snake_body[0][1] -= block_size
    elif snake_direction == "DOWN":
        snake_body[0][1] += block_size

    if snake_body[0] == [food_position[0], food_position[1]]:
        food_position = generate_food()
        snake_body.append([0, 0])
        score += 1

    draw_snake(snake_body)
    pygame.draw.rect(screen, RED, [food_position[0], food_position[1], block_size, block_size])

    display_info()
    pygame.display.update()
    clock.tick(snake_speed)

pygame.quit()