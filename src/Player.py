from ships import *
from datatypes import Position as Pos


class Player:
    __HIT_COLOR = (255, 0, 0)
    __SHOT_COLOR = (0, 255, 255)
    __SHIP_COLOR = (255, 255, 255)
    __VISIBLE_COLOR = (128, 128, 192)
    __GRID_COLOR = (48, 69, 77)
    __UNK_SHIP_COLOR = (128, 69, 128)

    rows = 0
    cols = 0

    def __init__(self, size: Pos) -> None:
        self.ships: BaseShip = []
        self.shots: bool = []
        self.rows = size.x
        self.cols = size.y
        for i in range(self.rows):
            inner_array = []
            for j in range(self.cols):
                inner_array.append(False)
            self.shots.append(inner_array)

        self.ships.append(ScoutShip())
        self.ships.append(ScoutShip())
        self.ships.append(HunterShip())
        self.ships.append(HunterShip())
        self.ships.append(CruiserShip())
        self.ships.append(CruiserShip())
        self.ships.append(BattleShip())
        self.ships.append(CommandShip())

        # TODO make this dynamic / from the outside
        self.ships[7].set_position(Pos(0 ,0))
        self.ships[6].set_position(Pos(0 ,1))
        self.ships[5].set_position(Pos(0 ,2))
        self.ships[4].set_position(Pos(0 ,3))
        self.ships[3].set_position(Pos(0 ,4))
        self.ships[2].set_position(Pos(0 ,5))
        self.ships[1].set_position(Pos(0 ,6))
        self.ships[0].set_position(Pos(0 ,7))


    def shoot_ships(self, pos:Pos):
        ship: BaseShip = self.get_grid_ship(pos)
        if ship:
            index: int
            if ship.get_position().horizontal:
                index = pos.x - ship.get_position().x
            else:
                index = pos.y - ship.get_position().y

            ship.set_hit(index)
            return True
        return False

    def shoot_grid(self, pos: Pos):
        if self.shots[pos.x][pos.y] == False:
            self.shots[pos.x][pos.y] = True
            self.shoot_ships(pos)
            return True
        
        # Invalid, position was already hit
        return False


    def ships_colliding(self) -> bool:
        temp_array: bool = []
        for i in range(self.rows):
            inner_array = []
            for j in range(self.cols):
                inner_array.append(False)
            temp_array.append(inner_array)

        for i in range(len(self.ships)):
            for j in range(self.ships[i].get_size() + 1):
                ship_pos = self.ships[i].get_position()
                if temp_array[ship_pos.y + (j * (not ship_pos.horizontal))][ship_pos.x +
                                                                            (j * (ship_pos.horizontal))] is True:
                    # print("SHIP COLLISION")
                    return True  # this means that there is a boat collision
                temp_array[ship_pos.y + (j * (not ship_pos.horizontal))][ship_pos.x +
                                                                         (j * (ship_pos.horizontal))] = True

            # print("----------------------------------------------")
            # for i in range(self.rows):
            #     for j in range(self.cols):
            #         print(temp_array[i][j], ", ", end='')
            #     print("")
            # for i in range(len(self.ships)):
            #     for j in range(len(self.ships)):
            #         if i == j:
            #             continue
            #         if self.ships[i].get_position().horizontal is True:
            #             if self.ships[j].get_position().horizontal = True:
            #
            #             elif self.ships[j].get_position().horizontal = False:
            #
            #         elif self.ships[i].get_position().horizontal is False:
            #
        return False

    # TODO add True return if movement got accepted
    def move_ship(self, pos: Pos, vertical: int, horizontal: int) -> bool:
        potential_moved_ship = self.get_grid_ship(pos)
        ship_pos = potential_moved_ship.get_position()
        previous_ship_pos = Pos(ship_pos.x, ship_pos.y, ship_pos.horizontal)

        if (vertical != 0):
            if ship_pos.horizontal is False:
                if (vertical == -1):
                    if ship_pos.y-1 >= 0:
                        ship_pos.y -= 1
                elif (vertical == 1):
                    if ship_pos.y+1+potential_moved_ship.get_size() < self.rows:
                        ship_pos.y += 1
        elif (horizontal != 0):
            if ship_pos.horizontal is True:
                if (horizontal == -1):
                    if ship_pos.x-1 >= 0:
                        ship_pos.x -= 1
                elif (horizontal == 1):
                    if ship_pos.x+1+potential_moved_ship.get_size() < self.cols:
                        ship_pos.x += 1

        potential_moved_ship.set_position(ship_pos)

        if self.ships_colliding() is True:
            potential_moved_ship.set_position(previous_ship_pos)

        return False

    def get_grid_ship(self, pos: Pos) -> BaseShip:
        for i in range(0, len(self.ships)):
            # get size, orientation, and position compare if in range
            size = self.ships[i].get_size()
            ship_pos = self.ships[i].get_position()
            ship_end: Pos

            if ship_pos.horizontal:
                ship_end = Pos(ship_pos.x + size-1, ship_pos.y)
            else:
                ship_end = Pos(ship_pos.x, ship_pos.y + size-1)
            
            # print("Ship ", size, ship_pos, ship_end)

            if (ship_pos.x <= pos.x and pos.x <= ship_end.x):
                if (ship_pos.y <= pos.y and pos.y <= ship_end.y):
                    return self.ships[i]
        return None

    def get_grid_shot(self, pos: Pos):
        return self.shots[pos.x][pos.y]

    def get_grid_color(self, pos: Pos, enemy=False):
        color = self.__GRID_COLOR
        if enemy:
            if self.get_grid_shot(pos):
                color = self.__VISIBLE_COLOR
            
                # see if there is a ship
                if self.get_grid_ship(pos):
                    color = self.__UNK_SHIP_COLOR

                    # see if the ship is hit in that position
                    if None:
                        color = self.__HIT_COLOR                
        else:
            # see if there is a ship
            if self.get_grid_ship(pos):
                color = self.__SHIP_COLOR

        return color
