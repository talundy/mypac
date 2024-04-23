import pygame

# Define world objects
WALL = 0
PATH = 1
PELLET = 2
POWER_PELLET = 3

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# Define base cell_size
cell_size = 20


class World:
    def __init__(self, width, height):
        self.grid = generateGrid(width, height)
        self.width = width
        self.height = height

    def draw_grid(self, screen):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
                # Color walls blue
                if self.grid[y][x] == 0:
                    pygame.draw.rect(screen, BLUE, rect)
                elif self.grid[y][x] == 1 or self.grid[y][x] == 2:
                    pygame.draw.rect(screen, BLACK, rect)
                if self.grid[y][x] == 2:
                    # Draw pellets
                    center_x = x * cell_size + cell_size // 2
                    center_y = y * cell_size + cell_size // 2
                    pygame.draw.circle(screen, YELLOW, (center_x, center_y), 5)


def generateGrid(width, height):
    """
     Generates a basic world (2D array) from scratch based on the window size.
     First row and column should always be filled with zeroes, as are the last row and column.
     """
    grid = [[0 for _ in range(width)] for _ in range(height)]

    for y in range(1, height - 1):
        for x in range(1, width - 1):
            grid[y][x] = 1
    return grid
