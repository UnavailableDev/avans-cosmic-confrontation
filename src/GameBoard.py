import pygame
from ships import BaseShip, BattleShip, ScoutShip
from datatypes import Position as Pos
from Player import Player
from AI import AI

from enum import Enum

class states(Enum):
    INIT = 0
    ATTACK = 1
    MOVE = 2
    ABILITY = 3

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

        self.player = Player(rows, cols)
        self.player_ai = Player(rows, cols)

        self.AI = AI(rows, cols)

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

    def win_condition(self):
        player_alive: bool = False
        player_ai_alive: bool = False
        for ship in self.player.ships:
            ship: BaseShip = ship
            if sum(ship.get_hits()) == ship.get_size():
                pass
            else:
                player_alive = True
        
        for ship in self.player_ai.ships:
            ship: BaseShip = ship
            if sum(ship.get_hits()) == ship.get_size():
                pass
            else:
                player_ai_alive = True

        if not player_alive:
            return False
        elif not player_ai_alive:
            return True
        else:
            return None

    def click_local_grid(self, pos: Pos, offset: Pos = Pos(0, 0)):
        cell_width = (self.RECT_WIDTH + self.MARGIN)
        cell_height = (self.RECT_HEIGHT + self.MARGIN)

        offset = Pos(offset.x * cell_width, offset.y * cell_height)
        pos = Pos(pos.x - offset.x, pos.y - offset.y)

        if pos.x > 0 and pos.x < (self.cols * cell_width):
            if pos.y > 0 and pos.y < (self.rows * cell_height):
                return Pos((pos.x//cell_width), (pos.y//cell_height))

        return None
    
    def input_movement(self, player_grid_click: Pos):
        if self.player.get_grid_ship(player_grid_click):
            pressed_key = self.wait_for_keypress()
            if pressed_key == pygame.K_DOWN:
                return self.player.move_ship(player_grid_click, 1, 0)
            if pressed_key == pygame.K_UP:
                return self.player.move_ship(player_grid_click, -1, 0)
            if pressed_key == pygame.K_LEFT:
                return self.player.move_ship(player_grid_click, 0, -1)
            if pressed_key == pygame.K_RIGHT:
                return self.player.move_ship(player_grid_click, 0, 1)
        return False

    def wait_for_keypress(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    # print(f"Key {pygame.key.name(event.key)} was pressed")
                    return event.key  # Return the key that was pressed

    def run(self):
        running = True
        # TODO INIT State
        state: states = states.INIT
        playing_ai = False

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    ai_grid_click = self.click_local_grid(Pos(event.pos[0], event.pos[1]))
                    player_grid_click = self.click_local_grid(Pos(event.pos[0], event.pos[1]), Pos(0, self.cols + 1))
                    
                    print(state)

                    if not playing_ai:
                        match state:
                            case states.INIT:
                                if player_grid_click: 
                                    self.input_movement(player_grid_click)
                                
                                if ai_grid_click: # Start game
                                    state = states.ATTACK
                            case states.ATTACK:
                                if ai_grid_click is not None:
                                    if self.player_ai.shoot_grid(ai_grid_click):
                                        # TODO this is disabled for testing purousses
                                        # pass
                                        playing_ai = True

                                        state = states.ATTACK
                            case states.MOVE:
                                if player_grid_click : 
                                # # _____________ for moving ships # TODO: intergrate with eventual statemachine
                                #     if self.player.get_grid_ship(player_grid_click):
                                #         pressed_key = self.wait_for_keypress()
                                #         move_ok = False
                                #         if pressed_key == pygame.K_DOWN:
                                #             move_ok = self.player.move_ship(player_grid_click, 1, 0)
                                #         if pressed_key == pygame.K_UP:
                                #             move_ok = self.player.move_ship(player_grid_click, -1, 0)
                                #         if pressed_key == pygame.K_LEFT:
                                #             move_ok = self.player.move_ship(player_grid_click, 0, -1)
                                #         if pressed_key == pygame.K_RIGHT:
                                #             move_ok = self.player.move_ship(player_grid_click, 0, 1)
                                # # _____________________________________________________________
                                    print(self.input_movement(player_grid_click))
                                    # if self.input_movement(player_grid_click):
                                    state = states.ABILITY
                            case states.ABILITY:

                                state = states.ATTACK
                                playing_ai = True
                            case _: # error / default case
                                pass

            # call AI logic
            if playing_ai:
                
                self.AI.update(self.player)
                self.player.shoot_grid(self.AI.shoot())
                playing_ai = False

            # Fill the background
            self.screen.fill(self.BACKGROUND_COLOR)

            # Draw the grid
            self.draw_AI_grid()
            self.draw_player_grid()

            # print(self.player_ai.ships)
            # print(self.player.ships)

            result = self.win_condition()
            if result is not None:
                if result:
                    print("Player won!")
                else:
                    print("AI won!")
                # TODO Exit game

            # print("------------ CYCLE ------------")

            # Update the display
            pygame.display.flip()
