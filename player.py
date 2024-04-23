# player.py
import pygame


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.color = (255, 255, 0)  # Yellow

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.width))

    def move(self, direction):
        if direction == 'left':
            self.x -= 2
        elif direction == 'right':
            self.x += 2
        elif direction == 'up':
            self.y -= 2
        elif direction == 'down':
            self.y += 2
