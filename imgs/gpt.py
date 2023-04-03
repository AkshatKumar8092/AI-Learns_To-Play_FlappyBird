import pygame
import random

pygame.init()

# Set up the game window
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
GAME_WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Flappy Bird')

# Set up the bird
BIRD_WIDTH = 50
BIRD_HEIGHT = 40
BIRD_X = 50
BIRD_Y = WINDOW_HEIGHT / 2 - BIRD_HEIGHT / 2
bird_image = pygame.image.load('bird2.png')
bird_image = pygame.transform.scale(bird_image, (BIRD_WIDTH, BIRD_HEIGHT))

# Set up the pipes
PIPE_WIDTH = 50
PIPE_HEIGHT = 400
PIPE_GAP = 150
pipe_image = pygame.image.load('pipe.png')
pipe_image = pygame.transform.scale(pipe_image, (PIPE_WIDTH, PIPE_HEIGHT))
pipe_list = []

def create_pipe():
    random_height = random.randint(50, 400)
    top_pipe = pipe_image.get_rect(midbottom=(WINDOW_WIDTH + PIPE_WIDTH, random_height - PIPE_GAP))
    bottom_pipe = pipe_image.get_rect(midtop=(WINDOW_WIDTH + PIPE_WIDTH, random_height))
    return top_pipe, bottom_pipe

# Set up the game loop
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                BIRD_Y -= 50

    # Move the bird
    BIRD_Y += 5

    # Create new pipes
    if len(pipe_list) == 0 or pipe_list[-1][0].centerx < WINDOW_WIDTH - 200:
        pipe_list.append(create_pipe())

    # Move the pipes
    for pipe_pair in pipe_list:
        pipe_pair[0].centerx -= 5
        pipe_pair[1].centerx -= 5

    # Remove off-screen pipes
    if len(pipe_list) > 0 and pipe_list[0][0].centerx < -PIPE_WIDTH:
        pipe_list.pop(0)

    # Draw everything
    GAME_WINDOW.fill((0, 0, 0))
    for pipe_pair in pipe_list:
        GAME_WINDOW.blit(pipe_image, pipe_pair[0])
        GAME_WINDOW.blit(pipe_image, pipe_pair[1])
    GAME_WINDOW.blit(bird_image, (BIRD_X, BIRD_Y))
    pygame.display.update()

pygame.quit()
