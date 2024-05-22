import pygame
from ships import *
from datatypes import Position as Pos

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

        self.ships.append(BattleShip())
        self.ships[0].set_position(Pos(1, 1, False))

        self.ships.append(ScoutShip())
        self.ships[1].set_position(Pos(3, 6))

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

    # def draw_shots(self):
    #     for row in range(self.rows):
    #         for col in range(self.cols):
    #             if (self.shot_positions[row][col] is True):
    #                 draw_shot(row, col)

    def draw_ships(self):
        print("self.ships len: ", len(self.ships))
        for i in range(len(self.ships)):
            print(i)
            ship_pos: Pos = self.ships[i].get_position()

            print("ship size: ", self.ships[i].get_size())
            print("ship x: ", ship_pos.x)

            for j in range(self.ships[i].get_size()):
                self.draw_square(ship_pos.x + (j * ship_pos.horizontal), ship_pos.y + (j * (not ship_pos.horizontal)), self.SHIP_COLOR)

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

            # self.draw_shots()

            # Update the display
            pygame.display.flip()
