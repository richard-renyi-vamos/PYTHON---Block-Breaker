import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Block Breaker")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

# Paddle dimensions
paddle_width = 100
paddle_height = 10
paddle_speed = 10

# Ball dimensions and speed
ball_radius = 10
ball_speed_x = 4
ball_speed_y = -4

# Block dimensions
block_width = 75
block_height = 20

# Paddle
paddle = pygame.Rect(screen_width // 2 - paddle_width // 2, screen_height - 30, paddle_width, paddle_height)

# Ball
ball = pygame.Rect(screen_width // 2, screen_height // 2, ball_radius * 2, ball_radius * 2)

# Blocks
blocks = [pygame.Rect(col * (block_width + 10) + 35, row * (block_height + 10) + 35, block_width, block_height) for row in range(5) for col in range(10)]

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(black)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < screen_width:
        paddle.right += paddle_speed
    
    # Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1
    if ball.top <= 0:
        ball_speed_y *= -1
    if ball.colliderect(paddle):
        ball_speed_y *= -1

    for block in blocks[:]:
        if ball.colliderect(block):
            ball_speed_y *= -1
            blocks.remove(block)
            break

    if ball.bottom >= screen_height:
        ball = pygame.Rect(screen_width // 2, screen_height // 2, ball_radius * 2, ball_radius * 2)
        ball_speed_y = -4
        ball_speed_x = random.choice([-4, 4])

    pygame.draw.rect(screen, blue, paddle)
    pygame.draw.ellipse(screen, red, ball)
    for block in blocks:
        pygame.draw.rect(screen, white, block)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
