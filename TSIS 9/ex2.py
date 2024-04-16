import pygame
from random import randint
import random
import time


pygame.init()

WIDTH = 720
HEIGHT = 720

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# colors
colorWHITE = (255, 255, 255)
colorGRAY = (70, 70, 70)
colorBLACK = (0, 0, 0)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)
colorYELLOW = (255, 255, 0)

# Set initial FPS
FPS = 5

# Initialize the clock
clock = pygame.time.Clock()

# Set cell size for grid
CELL = 60

# Initialize score
score = 0  

# Function to display text on the screen
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# Initialize font for score display
text_font = pygame.font.SysFont(None, 30)

# Define Point class to represent positions
class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    # Generate random point within the grid
    
    def generate():
        return Point(randint(0, WIDTH // CELL - 1) * CELL, randint(0, HEIGHT // CELL - 1) * CELL)

# Define Snake class
class Snake:
    def __init__(self):
        # Start with a single point for the snakes head
        self.body = [Point.generate()]
        self.dx = 0
        self.dy = 0

    # Move the snake
    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        head = self.body[0]
        head.x += self.dx * CELL
        head.y += self.dy * CELL
        
        # Check for border wall collision
        if head.x >= WIDTH or head.x < 0 or head.y >= HEIGHT or head.y < 0:
            return True  
        
        return False

    # Check if the snake collides with the food
    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.body.append(Point(head.x, head.y))
            return True

    # Draw the snake on the screen
    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x, head.y, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x, segment.y, CELL, CELL))

# Define Food class
class Food:
    def __init__(self):
        # Generate a random position for the food
        self.pos = Point.generate()
        self.weight = random.randint(30, CELL + 1)
        self.timer = None
    # Draw the food on the screen
    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x, self.pos.y, self.weight, self.weight))

    # Regenerate the food at a new position
    def regenerate(self):
        self.pos = Point.generate()

   
    


# Function to draw the grid on the screen
def draw_grid():
    for i in range(0, HEIGHT, CELL):
        for j in range(0, WIDTH, CELL):
            pygame.draw.rect(screen, colorGRAY, (i, j, CELL, CELL), 1)

# Initialize Snake and Food
snake = Snake()
food = Food()

# Main game loop
done = False
while not done:
    
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -1
            if event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 1
            if event.key == pygame.K_RIGHT:
                snake.dx = 1
                snake.dy = 0
            if event.key == pygame.K_LEFT:
                snake.dx = -1
                snake.dy = 0

    # Fill the screen with black
    screen.fill(colorBLACK)
    
    # Move the snake
    collision = snake.move()
    
    # End the game if the snake collides with the wall
    if collision:
        done = True  

    # Check for collision with food
    if snake.check_collision(food):
        food.regenerate()
        score += 1  # Increase score by 1

    
        

    # Change SPEED of Snake based on score
    if score == 20:
        FPS = 6
    elif score == 40:
        FPS = 7
    elif score == 60:
        FPS = 8
    elif score == 80:
        FPS = 9
    elif score == 100:
        FPS = 10

    
    snake.draw()
    food.draw()
    draw_grid()

   
    draw_text('Score:', text_font, (255, 255, 255), WIDTH - 100, 10)
    draw_text(f'{score}', text_font, (255, 255, 255), WIDTH - 35, 10)
    draw_text('Speed:', text_font, (255, 255, 255), 0, 10)
    draw_text(f'{FPS}', text_font, (255, 255, 255), 70, 10)
    
   
    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()