from datatypes import Position as Pos
# from enum import Enum

# class ShipTypes(Enum):
#     scout = 1
#     hunter = 2
#     cruiser = 3
#     battleship = 4
#     commandship = 5

#  TODO track hit positions on ship
class BaseShip:
    __size: int
    __position: Pos
    __hits: bool
    __ability: bool
    __cooldown: int
    
    def __init__(self, size: int) -> None:
        self.__size = size
        # self.__hits = 
        self.__ability = True
        self.__cooldown = 0
    
    def get_size(self):
        return self.__size

    def get_position(self):
        return self.__position
    
    def set_position(self, pos: Pos):
        # TODO add position checking
        self.__position = pos
    
    def get_cooldown(self):
        return self.__cooldown
    
    def set_cooldown(self, cooldown: int):
        self.__cooldown = cooldown

    def ability_available(self):
        return self.__ability

    def action(self):
        pass


class ScoutShip(BaseShip):
    def __init__(self) -> None:
        super().__init__(size=2)

    def action(self):
        pass

class HunterShip(BaseShip):
    def __init__(self) -> None:
        super().__init__(size=3)

    def action(self):
        pass

class CruiserShip(BaseShip):
    def __init__(self) -> None:
        super().__init__(size=3)

    def action(self):
        pass

class BattleShip(BaseShip):
    def __init__(self) -> None:
        super().__init__(size=4)

    def action(self):
        pass

class CommandShip(BaseShip):
    def __init__(self) -> None:
        super().__init__(size=5)

    def action(self):
        pass
