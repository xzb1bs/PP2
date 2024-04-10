import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

player_width = 60
player_height = 100
player_x = (WIDTH - player_width) // 2
player_y = HEIGHT - player_height - 30
player_speed = 5

coin_radius = 15
coins = []
coin_count = 0
font = pygame.font.Font(None, 36)

def draw_player(x, y):
    pygame.draw.rect(screen, RED, (x, y, player_width, player_height))

def draw_coins():
    global coin_count
    for coin in coins:
        pygame.draw.circle(screen, GREEN, (coin[0], coin[1]), coin_radius)
    text = font.render("Coins: " + str(coin_count), True, (0, 0, 0))
    screen.blit(text, (WIDTH - 150, 20))

running = True
clock = pygame.time.Clock()
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if random.randint(0, 100) < 5:
        coin_x = random.randint(0, WIDTH - coin_radius * 2)
        coin_y = random.randint(-HEIGHT, 0)
        coins.append([coin_x, coin_y])

    for coin in coins[:]:
        coin[1] += 5  
        if player_x < coin[0] < player_x + player_width and player_y < coin[1] < player_y + player_height:
            coins.remove(coin)
            coin_count += 1
        elif coin[1] > HEIGHT:
            coins.remove(coin)

    draw_player(player_x, player_y)
    draw_coins()

    pygame.display.update()
    clock.tick(30) 

pygame.quit()