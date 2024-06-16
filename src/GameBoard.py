import pygame
from ships import BaseShip
from datatypes import Position as Pos
from Player import Player
from AI import AI
import Database
from Defines import colors
from enum import Enum

from Visitor import Visitor

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

        self.PLAYER_GRID_OFFSET = 50

        self.RECT_WIDTH = 30
        self.RECT_HEIGHT = 30
        self.MARGIN = 5  # Space between rectangles
        self.cols = cols
        self.rows = rows

        self.buttons = []
        self.state: states = states.INIT

        self.player = Player(Pos(rows, cols))
        self.player_ai = Player(Pos(rows, cols))

        self.AI = AI(rows, cols)

        # Set up the display
        # self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.screen = screen
        self.font = pygame.font.SysFont(None, 24)
        pygame.display.set_caption("Grid of Rectangles")
        self.setup_buttons()

    def setup_buttons(self):
        for y in range(len(self.player.ships)):
            rect = pygame.Rect((self.cols + 1) * (self.RECT_WIDTH + self.MARGIN), (y + self.cols + 1) * (self.RECT_HEIGHT + self.MARGIN),
                               300, self.RECT_HEIGHT)
            self.buttons.append(rect)

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

    def draw_ui(self):
        for i, button in enumerate(self.buttons):
            color = colors.GRID.value  # Default

            text_surface = self.font.render(self.player.ships[i].__name__(), True, colors.BACKGROUND.value)
            text_rect = text_surface.get_rect(center=button.center)

            if self.state == states.INIT:
                color = colors.SHIP.value
                if button.collidepoint(pygame.mouse.get_pos()):
                    color = colors.SHOT.value
            else:
                if self.player.ships[i].is_alive():
                    color = colors.SHIP.value
                    if self.player.ships[i].ability_available() and self.player.ships[i].get_cooldown() == 0:
                        if button.collidepoint(pygame.mouse.get_pos()):
                            color = colors.SHOT.value
                    else:
                        color = colors.GRID.value
                else:
                    color = colors.HIT.value

            pygame.draw.rect(self.screen, color, button)
            self.screen.blit(text_surface, text_rect)

    def win_condition(self):
        player_alive: bool = False
        player_ai_alive: bool = False
        for ship in self.player.ships:
            ship: BaseShip = ship
            if ship.is_alive():
                player_alive = True

        for ship in self.player_ai.ships:
            ship: BaseShip = ship
            if ship.is_alive():
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
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    return event

    def check_for_ability_button_press(self, event) -> int:
        for i, rect in enumerate(self.buttons):
            if rect.collidepoint(event.pos):
                # Call the associated function
                return i
                # Check if the text box was clicked
        return None

    def run(self):
        self.database = Database.Database()
        self.database.start_new_game()
        self.database.write_gameboard(self)

        vis: Visitor = Visitor()

        running = True
        self.state = states.INIT
        playing_ai = False

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    ai_grid_click = self.click_local_grid(Pos(event.pos[0], event.pos[1]))
                    player_grid_click = self.click_local_grid(Pos(event.pos[0], event.pos[1]), Pos(0, self.cols + 1))

                    print(self.state)
                    self.database.write_gameboard(self)

                    if not playing_ai:
                        match self.state:
                            case states.INIT:
                                resulting = self.check_for_ability_button_press(event)  # TEST
                                if resulting is not None:  # TEST
                                    print(resulting)  # TEST
                                if player_grid_click:
                                    self.input_movement(player_grid_click)

                                if ai_grid_click:  # Start game
                                    self.state = states.ATTACK
                            case states.ATTACK:
                                if ai_grid_click is not None:
                                    if self.player_ai.shoot_grid(ai_grid_click):
                                        # TODO this is disabled for testing purousses
                                        # pass
                                        # playing_ai = True

                                        self.state = states.MOVE
                            case states.MOVE:
                                if player_grid_click:
                                    # _____________ for moving ships # TODO: intergrate with eventual statemachine
                                    ship: BaseShip = self.player.get_grid_ship(player_grid_click)
                                    if ship:
                                        if ship.get_cooldown() == 0:
                                            pressed_key = self.wait_for_keypress()
                                            if pressed_key == pygame.K_DOWN:
                                                self.player.move_ship(player_grid_click, 1, 0)
                                            if pressed_key == pygame.K_UP:
                                                self.player.move_ship(player_grid_click, -1, 0)
                                            if pressed_key == pygame.K_LEFT:
                                                self.player.move_ship(player_grid_click, 0, -1)
                                            if pressed_key == pygame.K_RIGHT:
                                                self.player.move_ship(player_grid_click, 0, 1)
                                    # _____________________________________________________________
                                            self.state = states.ABILITY
                            case states.ABILITY:

                                idx = self.check_for_ability_button_press(event)
                                print(idx)
                                if idx is not None:
                                    ev = self.wait_for_keypress()
                                    vis.do(self.player.ships[idx], self.player, self.player_ai, Pos(ev.pos[0], ev.pos[1]))

                                    self.state = states.ATTACK
                                    playing_ai = True
                            case _:  # error / default case
                                pass

            # call AI logic
            if playing_ai:
                self.AI.update(self.player)
                while not self.player.shoot_grid(self.AI.shoot()):
                    pass

                # End of Both player's turn
                playing_ai = False
                for i in range(len(self.player.ships)):
                    self.player.ships[i].reduce_cooldown()
                    self.player_ai.ships[i].reduce_cooldown()

            # Fill the background
            self.screen.fill(colors.BACKGROUND.value)

            # Draw the grid
            self.draw_AI_grid()
            self.draw_player_grid()

            self.draw_ui()

            # print(self.player_ai.ships)
            # print(self.player.ships)

            result = self.win_condition()
            if result is not None:
                txt = None
                if result:
                    txt = self.font.render("YOU WON!!!", True, (255, 255, 255))
                    print("Player won!")
                else:
                    txt = self.font.render("YOU LOST :<", True, (255, 255, 255))
                    print("AI won!")
                # TODO Exit game
                self.screen.blit(txt, (((self.cols/2) * (self.RECT_WIDTH + self.MARGIN)),
                                 (self.rows * (self.RECT_HEIGHT + self.MARGIN)) + self.RECT_HEIGHT/4))
            # print("------------ CYCLE ------------")

            # Update the display
            pygame.display.flip()
