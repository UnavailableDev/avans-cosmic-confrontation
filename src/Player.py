from ships import BaseShip, BattleShip, ScoutShip
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
    

    def __init__(self, size:Pos) -> None:
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
        self.ships.append(BattleShip())

        # TODO make this dynamic / from the outside
        self.ships[0].set_position(Pos(2, 2, False))
        self.ships[1].set_position(Pos(4, 6))

    def shoot_ships(self, pos:Pos):
        ship: BaseShip = self.get_grid_ship(pos)
        if ship:
            print(ship.get_size())
            index: int
            if ship.get_position().horizontal:
                index = pos.x - ship.get_position().x
            else:
                index = pos.y - ship.get_position().y

            ship.set_hit(index)
            return True
        return False

    def shoot_grid(self, pos:Pos):
        if self.shots[pos.x][pos.y] == False:
            self.shots[pos.x][pos.y] = True
            self.shoot_ships(pos)
            return True
        
        # Invalid, position was already hit
        return False

    # TODO This function needs fixing, positions are not reported correctly
    def get_grid_ship(self, pos:Pos):
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


    # TODO implement this function
    # def get_ship_hit(self, ship: BaseShip, pos:Pos):
    #     pass

    def get_grid_shot(self, pos:Pos):
        return self.shots[pos.x][pos.y]

    def get_grid_color(self, pos:Pos, enemy = False):
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