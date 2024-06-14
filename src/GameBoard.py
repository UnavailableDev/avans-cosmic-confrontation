import pygame
from ships import BaseShip, BattleShip, ScoutShip
from datatypes import Position as Pos
from Player import Player

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
    def __init__(self, screen, rows, cols):
        # Constants
        self.SCREEN_HEIGHT = screen.get_height()
        self.SCREEN_WIDTH = screen.get_width()

        self.BACKGROUND_COLOR = (0, 0, 0)
        self.GRID_COLOR = (255, 255, 255)
        self.SHOT_SQUARE = (0, 255, 255)
        self.UNSHOT_SQUARE = (255, 255, 255)
        self.SHIP_COLOR = (48, 69, 77)

        self.PLAYER_GRID_OFFSET = 50

        self.RECT_WIDTH = 30
        self.RECT_HEIGHT = 30
        self.MARGIN = 5  # Space between rectangles
        self.cols = cols
        self.rows = rows

        self.player = Player(Pos(rows, cols))
        self.player_ai = Player(Pos(rows, cols))

        # Set up the display
        # self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.screen = screen
        pygame.display.set_caption("Grid of Rectangles")

    def draw_square(self, col, row, color):
        x = col * (self.RECT_WIDTH + self.MARGIN)
        y = row * (self.RECT_HEIGHT + self.MARGIN)
        pygame.draw.rect(self.screen, color, (x, y, self.RECT_WIDTH, self.RECT_HEIGHT))

    def draw_player_grid(self):
        for row in range(self.rows):
            for col in range(self.cols):
                square_color = self.player.get_grid_color(Pos(row, col))
                self.draw_square(row, col + self.cols + 1, square_color)

    def draw_AI_grid(self):
        for row in range(self.rows):
            for col in range(self.cols):
                square_color = self.player_ai.get_grid_color(Pos(row, col), True)
                self.draw_square(row, col, square_color)

    def click_local_grid(self, pos:Pos, offset:Pos = Pos(0, 0)):
        cell_width = (self.RECT_WIDTH + self.MARGIN)
        cell_height = (self.RECT_HEIGHT + self.MARGIN)
        
        offset = Pos(offset.x * cell_width, offset.y * cell_height)
        pos = Pos(pos.x - offset.x, pos.y - offset.y)

        if pos.x > 0 and pos.x < (self.cols * cell_width):
            if pos.y > 0 and pos.y < (self.rows * cell_height):
                return Pos((pos.x//cell_width),(pos.y//cell_height))

        return None

    def run(self):
        running = True
        i = 0

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    ai_grid_click = self.click_local_grid(Pos(event.pos[0], event.pos[1]))
                    if ai_grid_click is not None:
                        # pass
                        # TODO update board state
                        print("foo: ", ai_grid_click.x, ai_grid_click.y)
                        # self.draw_square(foo.x, foo.y, self.BACKGROUND_COLOR)
                    player_grid_click = self.click_local_grid(Pos(event.pos[0], event.pos[1]), Pos(0, self.cols + 1))
                    if player_grid_click is not None:
                        print("bar: ", player_grid_click.x, player_grid_click.y)

            # Fill the background
            self.screen.fill(self.BACKGROUND_COLOR)

            # Draw the grid
            self.draw_AI_grid()
            self.draw_player_grid()

            # print(self.player_ai.ships)
            # print(self.player.ships)

            print("------------ CYCLE ------------")

            # Update the display
            pygame.display.flip()
