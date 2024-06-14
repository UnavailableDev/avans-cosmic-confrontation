from ships import BaseShip, BattleShip, ScoutShip
from datatypes import Position as Pos



class Player:
    __HIT_COLOR = (255, 0, 0)
    __SHOT_COLOR = (0, 255, 255)
    __GRID_COLOR = (255, 255, 255)
    __SHIP_COLOR = (48, 69, 77)
    __UNK_SHIP_COLOR = (255, 69, 255)

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
        self.ships[0].set_position(Pos(1, 1, False))

        self.ships.append(BattleShip())
        self.ships[1].set_position(Pos(6, 6))

    def shoot_grid(self, pos:Pos):
        if self.shots[pos.x][pos.y] == False:
            self.shots[pos.x][pos.y] = True
        else:
            return False
        return True

    # TODO This function needs fixing, positions are not reported correctly
    def get_grid_ship(self, pos:Pos):
        for i in range(len(self.ships)):
            # get size, orientation, and position compare if in range
            size = self.ships[i].get_size()
            ship_pos = self.ships[i].get_position()
            range_: Pos

            if ship_pos.horizontal:
                range_ = Pos(pos.x + size, pos.y)
            else:
                range_ = Pos(pos.x, pos.y + size)
            
            if (pos.x <= range_.x and pos.x >= ship_pos.x):
                if (pos.y <= range_.y and pos.y >= ship_pos.y):
                    print("xxxxx ", i)
                    return self.ships[i]
        return None
    
        for j in range(self.ships_player[i].get_size()):
            self.draw_square(ship_pos.x + (j * ship_pos.horizontal), ship_pos.y +
                                (j * (not ship_pos.horizontal) + self.rows + 1), self.SHIP_COLOR)

    
    # TODO implement this function
    # def get_ship_hit(self, ship: BaseShip, pos:Pos):
    #     pass

    def get_grid_shot(self, pos:Pos):
        return self.shots[pos.x][pos.y]

    def get_grid_color(self, pos:Pos, enemy = False):
        color = self.__GRID_COLOR
        if self.get_grid_shot(pos) and enemy:
            color = self.__SHOT_COLOR
        
            # see if there is a ship
            if self.get_grid_ship(pos):
                color = self.__UNK_SHIP_COLOR

                # see if the ship is hit in that position
                if None:
                    color = self.__HIT_COLOR                
            print("aa")
        else:
            # see if there is a ship
            if self.get_grid_ship(pos):
                print("bbbbbbbbbbbb", pos)
                color = self.__SHIP_COLOR
        
        return color