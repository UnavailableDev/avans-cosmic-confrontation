from datatypes import Position as Pos
from enum import Enum

# class ShipTypes(Enum):
#     scout = 1
#     hunter = 2
#     cruiser = 3
#     battleship = 4
#     commandship = 5


class BaseShip:

    def __init__(self) -> None:
        self.size = 3
        self.position = Pos()
        self.position.x = -1
        self.position.y = -1
        self.position.horizontal = False
        self.hits = 0
        self.ability = True
        self.cooldown = 0
        pass

    def action(self):
        pass
