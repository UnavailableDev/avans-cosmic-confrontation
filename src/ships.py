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
    __hits: bool = []
    __ability: bool
    __cooldown: int

    def __init__(self, size: int) -> None:
        self.__size = size
        self.__hits = []  # For some reason this needs to be reset, otherwise it shares the same array between all child classes
        for i in range(size):
            self.__hits.append(False)

        self.__ability = True
        self.__cooldown = 0

    def get_size(self):
        return self.__size

    def get_position(self):
        return self.__position

    def set_position(self, pos: Pos):
        # TODO add position checking
        self.__position = pos

    def get_hits(self):
        return self.__hits

    def set_hit(self, index: int):
        self.__hits[index] = True

    def set_hits(self, hit_list: [int]):
        self.__hits = hit_list

    def is_alive(self):
        return not (sum(self.__hits) == self.__size)

    def get_cooldown(self):
        return self.__cooldown

    def set_cooldown(self, cooldown: int):
        self.__cooldown = cooldown

    def ability_available(self):
        return self.__ability

    def set_ability_available(self, value: bool):
        self.__ability = value

    def action(self):
        pass

    def __name__(self) -> str:
        return "BaseShip"


class ScoutShip(BaseShip):
    def __init__(self) -> None:
        super().__init__(size=2)

    def action(self):
        pass

    def __name__(self) -> str:
        return "ScoutShip"


class HunterShip(BaseShip):
    def __init__(self) -> None:
        super().__init__(size=3)

    def action(self):
        pass

    def __name__(self) -> str:
        return "HunterShip"


class CruiserShip(BaseShip):
    def __init__(self) -> None:
        super().__init__(size=3)

    def action(self):
        pass

    def __name__(self) -> str:
        return "CruiserShip"


class BattleShip(BaseShip):
    def __init__(self) -> None:
        super().__init__(size=4)

    def action(self):
        pass

    def __name__(self) -> str:
        return "BattleShip"


class CommandShip(BaseShip):
    def __init__(self) -> None:
        super().__init__(size=5)

    def action(self):
        pass

    def __name__(self) -> str:
        return "CommandShip"
