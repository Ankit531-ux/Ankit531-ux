import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong Game')

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define paddle and ball properties
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 15

# Paddle positions
left_paddle = pygame.Rect(30, (HEIGHT // 2) - (PADDLE_HEIGHT // 2), PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 40, (HEIGHT // 2) - (PADDLE_HEIGHT // 2), PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball properties
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_SIZE, BALL_SIZE)
ball_speed_x = 5
ball_speed_y = 5

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= 5
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += 5
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= 5
    if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
        right_paddle.y += 5

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with top and bottom
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Ball collision with paddles
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_speed_x *= -1

    # Reset ball if it goes out of bounds
    if ball.left <= 0 or ball.right >= WIDTH:
        ball.x = WIDTH // 2
        ball.y = HEIGHT // 2
        ball_speed_x *= -1  # Change direction

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Update the display
    pygame.display.flip()
    pygame.time.Clock().tick(60)  # Limit to 60 FPS