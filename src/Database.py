import json
from GameBoard import GameBoard
from typing import Any, Dict
from datetime import datetime
import os
from ships import BaseShip, ScoutShip, HunterShip, BattleShip, CommandShip, CruiserShip, Pos


class Database:
    def __init__(self):
        self.game_move_count = 0
        pass

    def retrieve_stored_games(self) -> list[str]:
        directory_path = 'database'  # Replace with your directory path

        files_list = os.listdir(directory_path)

        file_names = [file for file in files_list if os.path.isfile(os.path.join(directory_path, file))]

        # print("Files in directory:")
        # for file_name in file_names:
        #     print(file_name)
        return file_names

    def create_gameboard_from_file(self, screen, data_file_name: str) -> GameBoard:
        with open(f"database/{data_file_name}", 'r') as json_file:
            loaded_data = json.load(json_file)

        board_size = loaded_data["board_size"]

        new_gameboard = GameBoard(screen, board_size, board_size)

        turns_played = loaded_data["game_move_count"]
        last_game_state = loaded_data[f"move-{turns_played}"]

        new_gameboard.player.set_nickname(last_game_state["player"]["nickname"])
        new_gameboard.player.shots = last_game_state["player"]["shots"]
        new_gameboard.player.ships = []
        for i in range(last_game_state["player"]["ships"]["AmountOfShips"]):
            ship_data = last_game_state["player"]["ships"][f"ship{i}"]
            ship_size = ship_data["size"]
            ship_type_str = ship_data["type"]

            ship = BaseShip(ship_size)
            if ship_type_str == ScoutShip().__name__():
                ship = ScoutShip()
            if ship_type_str == HunterShip().__name__():
                ship = HunterShip()
            if ship_type_str == BattleShip().__name__():
                ship = BattleShip()
            if ship_type_str == CommandShip().__name__():
                ship = CommandShip()
            if ship_type_str == CruiserShip().__name__():
                ship = CruiserShip()

            ship_pos = Pos(ship_data["x"], ship_data["y"], ship_data["horizontal"])
            ship.set_position(ship_pos)

            ship.set_hits(ship_data["hit"])
            ship.set_cooldown(ship_data["cooldown"])
            ship.set_ability_available(ship_data["ability_available"])

            new_gameboard.player.ships.append(ship)

        new_gameboard.player_ai.set_nickname(last_game_state["player_ai"]["nickname"])
        new_gameboard.player_ai.shots = last_game_state["player_ai"]["shots"]
        new_gameboard.player_ai.ships = []
        for i in range(last_game_state["player_ai"]["ships"]["AmountOfShips"]):
            ship_data = last_game_state["player_ai"]["ships"][f"ship{i}"]
            ship_size = ship_data["size"]
            ship_type_str = ship_data["type"]

            ship = BaseShip(ship_size)
            if ship_type_str == ScoutShip().__name__():
                ship = ScoutShip()
            if ship_type_str == HunterShip().__name__():
                ship = HunterShip()
            if ship_type_str == BattleShip().__name__():
                ship = BattleShip()
            if ship_type_str == CommandShip().__name__():
                ship = CommandShip()
            if ship_type_str == CruiserShip().__name__():
                ship = CruiserShip()

            ship_pos = Pos(ship_data["x"], ship_data["y"], ship_data["horizontal"])
            ship.set_position(ship_pos)

            ship.set_hits(ship_data["hit"])
            ship.set_cooldown(ship_data["cooldown"])
            ship.set_ability_available(ship_data["ability_available"])

            new_gameboard.player_ai.ships.append(ship)

        # for i in range(len(new_gameboard.player_ai.ships)):
        #     print(new_gameboard.player_ai.ships[i].__name__())

        return new_gameboard

# from ships import BaseShip, ScoutShip, HunterShip, BattleShip, CommandShip, CruiserShip, Pos

    def start_new_game(self) -> None:
        # Get the current date and time
        current_datetime = datetime.now()
        default_format = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        # print("Default format:", default_format)
        self.file_path = f"database/game-{default_format}.json"

        # with open(self.file_path, 'w') as json_file:
        #     # loaded_data = json.load(json_file)
        #     pass
        return

    def write_gameboard(self, game_board: GameBoard) -> None:
        # Initialize an empty dictionary
        if self.game_move_count == 0:
            with open(self.file_path, 'w') as json_file:
                empty_data = {}
                json.dump(empty_data, json_file, indent=4)
                loaded_data = {}
        else:
            with open(self.file_path, 'r') as json_file:
                loaded_data = json.load(json_file)

        self.game_move_count += 1

        loaded_data[f"move-{self.game_move_count}"] = {}

        loaded_data["game_move_count"] = self.game_move_count
        loaded_data["board_size"] = game_board.rows

        data = loaded_data[f"move-{self.game_move_count}"]

        data["player"] = {}
        data["player"]["nickname"] = game_board.player.get_nickname()
        data["player"]["shots"] = {}
        data["player"]["shots"] = game_board.player.shots

        data["player"]["ships"] = {}
        data["player"]["ships"]["AmountOfShips"] = len(game_board.player.ships)
        for i in range(len(game_board.player.ships)):
            data["player"]["ships"][f"ship{i}"] = {}
            data["player"]["ships"][f"ship{i}"]["x"] = game_board.player.ships[i].get_position().x
            data["player"]["ships"][f"ship{i}"]["y"] = game_board.player.ships[i].get_position().y
            data["player"]["ships"][f"ship{i}"]["horizontal"] = game_board.player.ships[i].get_position().horizontal
            data["player"]["ships"][f"ship{i}"]["size"] = game_board.player.ships[i].get_size()

            data["player"]["ships"][f"ship{i}"]["hit"] = game_board.player.ships[i].get_hits()
            data["player"]["ships"][f"ship{i}"]["cooldown"] = game_board.player.ships[i].get_cooldown()
            data["player"]["ships"][f"ship{i}"]["ability_available"] = game_board.player.ships[i].ability_available()
            data["player"]["ships"][f"ship{i}"]["type"] = game_board.player.ships[i].__name__()

        data["player_ai"] = {}
        data["player_ai"]["nickname"] = game_board.player.get_nickname()
        data["player_ai"]["shots"] = {}
        data["player_ai"]["shots"] = game_board.player_ai.shots

        data["player_ai"]["ships"] = {}
        data["player_ai"]["ships"]["AmountOfShips"] = len(game_board.player_ai.ships)
        for i in range(len(game_board.player_ai.ships)):
            data["player_ai"]["ships"][f"ship{i}"] = {}
            data["player_ai"]["ships"][f"ship{i}"]["x"] = game_board.player_ai.ships[i].get_position().x
            data["player_ai"]["ships"][f"ship{i}"]["y"] = game_board.player_ai.ships[i].get_position().y
            data["player_ai"]["ships"][f"ship{i}"]["horizontal"] = game_board.player_ai.ships[i].get_position(
            ).horizontal
            data["player_ai"]["ships"][f"ship{i}"]["size"] = game_board.player_ai.ships[i].get_size()

            data["player_ai"]["ships"][f"ship{i}"]["hit"] = game_board.player_ai.ships[i].get_hits()
            data["player_ai"]["ships"][f"ship{i}"]["cooldown"] = game_board.player_ai.ships[i].get_cooldown()
            data["player_ai"]["ships"][f"ship{i}"]["ability_available"] = game_board.player_ai.ships[i].ability_available(
            )
            data["player_ai"]["ships"][f"ship{i}"]["type"] = game_board.player.ships[i].__name__()

        with open(self.file_path, 'w') as json_file:
            json.dump(loaded_data, json_file, indent=4)

        with open(self.file_path, 'r') as json_file:
            loaded_data = json.load(json_file)

        # print(loaded_data)

        self.game_move_count += 1
        return
