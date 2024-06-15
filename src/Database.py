import json
import GameBoard
from typing import Any, Dict
from datetime import datetime
import os


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
        loaded_data[f"move-{self.game_move_count}"] = {}
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

            data["player"]["ships"][f"ship{i}"]["hit"] = game_board.player.ships[i].get_hits()
            data["player"]["ships"][f"ship{i}"]["cooldown"] = game_board.player.ships[i].get_cooldown()
            data["player"]["ships"][f"ship{i}"]["ablitity_available"] = game_board.player.ships[i].ability_available()
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

            data["player_ai"]["ships"][f"ship{i}"]["hit"] = game_board.player_ai.ships[i].get_hits()
            data["player_ai"]["ships"][f"ship{i}"]["cooldown"] = game_board.player_ai.ships[i].get_cooldown()
            data["player_ai"]["ships"][f"ship{i}"]["ablitity_available"] = game_board.player_ai.ships[i].ability_available(
            )
            data["player_ai"]["ships"][f"ship{i}"]["type"] = game_board.player.ships[i].__name__()

        with open(self.file_path, 'w') as json_file:
            json.dump(loaded_data, json_file, indent=4)

        with open(self.file_path, 'r') as json_file:
            loaded_data = json.load(json_file)

        print(loaded_data)

        self.game_move_count += 1
        return
