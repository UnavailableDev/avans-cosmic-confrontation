from ships import *
from datatypes import Position as Pos
from Defines import colors
import random


class Player:
    rows = 0
    cols = 0

    def __init__(self, rows, cols) -> None:
        self.ships: BaseShip = []
        self.shots: bool = []
        self.rows = rows
        self.cols = cols
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
        self.ships[7].set_position(Pos(0 + self.cols, 0))
        self.ships[6].set_position(Pos(0 + self.cols, 1))
        self.ships[5].set_position(Pos(0 + self.cols, 2))
        self.ships[4].set_position(Pos(0 + self.cols, 3))
        self.ships[3].set_position(Pos(0 + self.cols, 4))
        self.ships[2].set_position(Pos(0 + self.cols, 5))
        self.ships[1].set_position(Pos(0 + self.cols, 6))
        self.ships[0].set_position(Pos(0 + self.cols, 7))

        self.rand_ship_layout()


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


    def rand_ship_layout(self):
        for i in range(len(self.ships)):
            while not self.new_ship_pos(i):

                self.ships[i].set_position(Pos(self.rows, self.cols))

            print(i, self.ships[i].get_position())
    
    def new_ship_pos(self, idx: int):
        size = self.ships[idx].get_size()
        hor: bool = bool(random.getrandbits(1))

        # rand_x = random.randrange(self.rows)
        # rand_y = random.randrange(self.rows)

        rand_x = random.randrange(self.rows - size * hor)
        rand_y = random.randrange(self.rows - size * (not hor))

        # Edge violations ---->
        # if (rand_x + size > self.rows or rand_y + size > self.cols):
        #     return False
        if hor and (self.rows <= rand_x + size):
            print("NANI X", rand_x)
            return False
        if not hor and (self.cols <= rand_y + size):
            print("NANI Y", rand_y)
            return False

        print(size, Pos(rand_x, rand_y, hor))
        self.ships[idx].set_position(Pos(rand_x, rand_y, hor))
        if self.ships_colliding():
            self.ships[idx].set_position(Pos(self.rows, self.cols))
            return False

        return True # Success

    def ships_colliding(self) -> bool:
        temp_array: bool = []
        for i in range(self.rows):
            inner_array = []
            for j in range(self.cols):
                inner_array.append(False)
            temp_array.append(inner_array)

        for i in range(len(self.ships)):
            ship_pos = self.ships[i].get_position()
            if (ship_pos.x >= self.rows) or (ship_pos.y >= self.cols):
                return False # Ignore ships with starting point outside the grid

            for j in range(self.ships[i].get_size()):
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

        if not self.ships_colliding():
            potential_moved_ship.set_position(previous_ship_pos)

        return True

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
        color = colors.GRID.value
        if enemy:
            pass
            # if self.get_grid_shot(pos):
            #     color = colors.VISIBLE.value
            
            #     # see if there is a ship
            #     if self.get_grid_ship(pos):
            #         color = colors.UNK_SHIP.value

            #         # see if the ship is hit in that position
            #         if None:
            #             color = colors.HIT.value          
        else:
            # see if there is a ship
            if self.get_grid_ship(pos):
                color = colors.SHIP.value

        if self.get_grid_shot(pos):
            if enemy:
                color = colors.VISIBLE.value
            else:
                color = colors.SHOT.value
            
            if self.get_grid_ship(pos):
                if enemy:
                    color = colors.UNK_SHIP.value
                    # see if the ship is hit in that position
                    if None:
                        color = colors.HIT.value 
                else:
                    color = colors.HIT.value

        return color
