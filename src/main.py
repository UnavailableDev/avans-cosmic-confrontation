import pygame
import sys

# from ships import BaseShip
from GameBoard import GameBoard
from Menu import Menu

# Initialize Pygame
pygame.init()
SCREEN_HEIGHT = 1000
SCREEN_WIDTH = 1500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# screen = ScreenWrapper(SCREEN_WIDTH, SCREEN_HEIGHT)
game_board = GameBoard(screen, 10, 10)


def game_start():
    print("Start Game!")
    game_board.player.set_nickname(menu.text_input)
    game_board.run()


def see_previous_games():
    print("WIP")


def exit_game():
    # TODO actually quit the application
    print("Exitting game")


# Create the menu with options and associated functions
menu = Menu(screen, [("Start game", game_start), ("See previous games", see_previous_games), ("Exit", exit_game)])

# Run the menu
menu.run()

# ship1 = BaseShip()
# ship2 = BaseShip()
#
# ship1.position.x = 5
# ship1.position.y = 1
#
# ship2.position.x = 10
# ship2.position.y = 11
#
# print(ship1.position.x)
# print(ship2.position.x)
# Quit Pygame
pygame.quit()
sys.exit()
