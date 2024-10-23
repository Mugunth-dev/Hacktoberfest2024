import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 600, 200
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dino Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Dino settings
dino_width, dino_height = 40, 40
dino_x, dino_y = 50, height - dino_height - 10
dino_jump = 10
is_jumping = False
jump_count = 10

# Obstacle settings
obstacle_width, obstacle_height = 20, 40
obstacle_x = width
obstacle_speed = 5

# Game loop
running = True
while running:
    pygame.time.delay(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Movement
    keys = pygame.key.get_pressed()
    
    if not is_jumping:
        if keys[pygame.K_SPACE]:
            is_jumping = True
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            dino_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            is_jumping = False
            jump_count = 10

    # Move obstacle
    obstacle_x -= obstacle_speed
    if obstacle_x < 0:
        obstacle_x = width
        obstacle_height = random.randint(20, 60)

    # Collision detection
    if (dino_x + dino_width > obstacle_x and dino_x < obstacle_x + obstacle_width) and (dino_y + dino_height > height - obstacle_height - 10):
        print("Game Over!")
        running = False

    # Drawing
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, (dino_x, dino_y, dino_width, dino_height))
    pygame.draw.rect(screen, BLACK, (obstacle_x, height - obstacle_height - 10, obstacle_width, obstacle_height))
    
    pygame.display.update()

pygame.quit()
