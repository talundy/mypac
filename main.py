import pygame
import sys
from player import Player
from world import World

# Initialize Pygame
pygame.init()

# Set up the display 
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# Initialize the player in middle of screen
player = Player(screen_width/2, screen_height/2)
# Initialize the world and grid
# world = World(screen_width, screen_height)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Check for key presses
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player.x > 0:
        player.move('left')
    if keys[pygame.K_RIGHT] and player.x < (screen_width - player.width):
        player.move('right')
    if keys[pygame.K_UP] and player.y > 0:
        player.move('up')
    if keys[pygame.K_DOWN] and player.y < (screen_height - player.height):
        player.move('down')

    # Draw world
    # world.draw_grid(screen)

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw the player
    player.draw(screen)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

