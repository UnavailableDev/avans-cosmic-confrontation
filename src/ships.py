from datatypes import Position as Pos
from enum import Enum

# class ShipTypes(Enum):
#     scout = 1
#     hunter = 2
#     cruiser = 3
#     battleship = 4
#     commandship = 5

class BaseShip:
    __size: int
    __position: Pos
    __hits: bool
    __ability: bool
    __cooldown: int
    
    def __init__(self) -> None:
        pass
    
    def action(self):
        pass

