import pygame
import sys
# from ships import BaseShip
# from GameBoard import GameBoard
from Menu import Menu
from Database import Database, GameBoard
from functools import partial

# Initialize Pygame
pygame.init()

SCREEN_HEIGHT = 1000
SCREEN_WIDTH = 1500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# screen = ScreenWrapper(SCREEN_WIDTH, SCREEN_HEIGHT)

previous_games_list = []
grid_size = 10


def game_start():
    print("Start Game!")
    game_board = GameBoard(screen, grid_size, grid_size)
    game_board.player.set_nickname(menu.text_input)
    game_board.run()


database = Database()


def preview_game(game_file_name: str):
    # print("preview_game()", game_file_name)
    game_board = database.create_gameboard_from_file(screen, game_file_name)
    game_board.run()


def see_previous_games():
    previous_games_list = database.retrieve_stored_games()
    menu_list = []
    for i in range(len(previous_games_list)):
        menu_list.append((previous_games_list[i], partial(preview_game, previous_games_list[i])))
    previous_games_menu = Menu(screen, menu_list)
    previous_games_menu.run()
    print("WIP")


def exit_game():
    # current_function = menu_items_list[2][1]
    #
    # new_tuple = ("Smexit", current_function)
    #
    # menu_items_list[2] = new_tuple   # TODO actually quit the application
    print("Exitting game")


def current_grid_size():
    global grid_size
    current_function = menu_items_list[3][1]

    new_tuple = (f"Current gridsize: {grid_size}", current_function)

    menu_items_list[3] = new_tuple   # TODO actually quit the application


def increase_grid_size():
    global grid_size
    grid_size += 1

    if grid_size >= 16:
        grid_size = 16

    current_grid_size()
    return


def decrease_grid_size():
    global grid_size
    grid_size -= 1

    if grid_size <= 8:
        grid_size = 8
    current_grid_size()
    return


menu_items_list = ([("Start game", game_start), ("See previous games", see_previous_games),
                   ("Exit", exit_game), ("Current gridsize: 10", current_grid_size),
                    ("Increase gridsize", increase_grid_size), ("Decrease gridsize", decrease_grid_size)])
# Create the menu with options and associated functions
menu = Menu(screen, menu_items_list)

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
