import pygame
from ships import BaseShip

# # Constants
# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600
# BACKGROUND_COLOR = (0, 0, 0)
# GRID_COLOR = (255, 255, 255)
# RECT_WIDTH = 50
# RECT_HEIGHT = 50
# MARGIN = 5  # Space between rectangles

# Access elements


# Access elements again
# for i in range(len(vec)):
#     print(vec[i], end=' ')
# print()


class GameBoard:
    def __init__(self, screen):
        # Constants
        self.SCREEN_HEIGHT = 600
        self.SCREEN_WIDTH = 800

        self.BACKGROUND_COLOR = (0, 0, 0)
        self.GRID_COLOR = (255, 255, 255)
        self.SHIP_COLOR = (48, 69, 77)

        self.RECT_WIDTH = 50
        self.RECT_HEIGHT = 50
        self.MARGIN = 5  # Space between rectangles
        self.cols = self.SCREEN_WIDTH // (self.RECT_WIDTH + self.MARGIN)
        self.rows = self.SCREEN_HEIGHT // (self.RECT_HEIGHT + self.MARGIN)

        self.ships = []

        self.ships.append(BaseShip())

        self.ships[0].size = 4
        self.ships[0].position.x = 1
        self.ships[0].position.y = 1
        self.ships[0].position.horizontal = False

        self.ships.append(BaseShip())

        self.ships[1].size = 2
        self.ships[1].position.x = 3
        self.ships[1].position.y = 6
        self.ships[1].position.horizontal = True

        self.shot_positions = []

        array_2d = []
        for i in range(10):
            inner_array = []
            for j in range(10):
                inner_array.append(False)
            array_2d.append(inner_array)

        # Set up the display
        # self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.screen = screen
        pygame.display.set_caption("Grid of Rectangles")

    def draw_square(self, col, row, color):
        x = col * (self.RECT_WIDTH + self.MARGIN)
        y = row * (self.RECT_HEIGHT + self.MARGIN)
        pygame.draw.rect(self.screen, color, (x, y, self.RECT_WIDTH, self.RECT_HEIGHT))

    def draw_shot(self, row, col):
        # TODO
        pass

    def draw_grid(self, screen):
        for row in range(self.rows):
            for col in range(self.cols):
                self.draw_square(col, row, self.GRID_COLOR)
                # x = col * (self.RECT_WIDTH + self.MARGIN)
                # y = row * (self.RECT_HEIGHT + self.MARGIN)
                # pygame.draw.rect(screen, self.GRID_COLOR, (x, y, self.RECT_WIDTH, self.RECT_HEIGHT))

    def draw_shots(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if (self.shot_positions[row][col] is True):
                    draw_shot(row, col)

    def draw_ships(self):
        print("self.ships len: ", len(self.ships))
        for i in range(len(self.ships)):
            print(i)
            ship_x = self.ships[i].position.x
            ship_y = self.ships[i].position.y

            print("ship size: ", self.ships[i].size)
            print("ship x: ", self.ships[i].position.x)

            ship_horizontal = self.ships[i].position.horizontal
            for j in range(self.ships[i].size):
                self.draw_square(ship_x + (j * ship_horizontal), ship_y + (j * (not ship_horizontal)), self.SHIP_COLOR)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Fill the background
            self.screen.fill(self.BACKGROUND_COLOR)

            # Draw the grid
            self.draw_grid(self.screen)

            self.draw_ships()

            self.draw_shots()

            # Update the display
            pygame.display.flip()
