from ships import *
from datatypes import Position as Pos
from Defines import colors
import random


class Player:
    rows = 0
    cols = 0

    def __init__(self, size: Pos) -> None:
        self.nickname = "undefined nickname"

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
        self.ships[7].set_position(Pos(0, 0))
        self.ships[6].set_position(Pos(0, 1))
        self.ships[5].set_position(Pos(0, 2))
        self.ships[4].set_position(Pos(0, 3))
        self.ships[3].set_position(Pos(0, 4))
        self.ships[2].set_position(Pos(0, 5))
        self.ships[1].set_position(Pos(0, 6))
        self.ships[0].set_position(Pos(0, 7))

        # self.rand_ship_layout()

    def shoot_ships(self, pos: Pos) -> bool:
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

    # TODO: make the invalid detection?
    def shoot_grid(self, pos: Pos) -> True:
        # if self.shots[pos.x][pos.y] == False:
        self.shots[pos.x][pos.y] = True
        self.shoot_ships(pos)
        return True

        # Invalid, position was already hit
        return False
    
    def new_rand_ship_layout(self) -> None:
        for i in range(len(self.ships)):
            self.ships[i].set_position(Pos(0 + self.cols, i, True))

        self.rand_ship_layout()

    def rand_ship_layout(self) -> None:
        for i in range(len(self.ships)):
            while not self.new_ship_pos(i):

                self.ships[i].set_position(Pos(self.rows, self.cols))

            # print(i, self.ships[i].get_position())

    def new_ship_pos(self, idx: int) -> bool:
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

        self.ships[idx].set_position(Pos(rand_x, rand_y, hor))
        if self.ships_colliding():
            self.ships[idx].set_position(Pos(self.rows, self.cols))
            return False

        return True  # Success

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
                return False  # Ignore ships with starting point outside the grid

            for j in range(self.ships[i].get_size()):
                if (ship_pos.y + (j * (not ship_pos.horizontal))) >= self.rows or (ship_pos.x + (j * (ship_pos.horizontal))) >= self.cols:
                    return True

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

    def move_ship_one(self, ship_index: int, vertical: int, horizontal: int) -> bool:
        potential_moved_ship = self.ships[ship_index]
        previous_ship_pos = Pos(potential_moved_ship.get_position().x,
                                potential_moved_ship.get_position().y, potential_moved_ship.get_position().horizontal)

        ship_pos = potential_moved_ship.get_position()

        if (vertical != 0):
            if (vertical == -1):
                if ship_pos.y-1 >= 0:
                    ship_pos.y -= 1
            elif (vertical == 1):
                if ship_pos.y+1 < self.rows:
                    ship_pos.y += 1
        if (horizontal != 0):
            if (horizontal == -1):
                if ship_pos.x-1 >= 0:
                    ship_pos.x -= 1
            elif (horizontal == 1):
                if ship_pos.x+1 < self.cols:
                    ship_pos.x += 1

        potential_moved_ship.set_position(ship_pos)

        if self.ships_colliding():
            potential_moved_ship.set_position(previous_ship_pos)

        return True

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

        if self.ships_colliding():
            print("move resulted in ships colliding")
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

    def get_ship_shot(self, ship: BaseShip, pos: Pos) -> bool:
        ship_pos = ship.get_position()
        hits = ship.get_hits()
        
        if ship_pos.horizontal:
            return hits[pos.x - ship_pos.x]
        else:
            return hits[pos.y - ship_pos.y]

    def get_grid_shot(self, pos: Pos) -> bool:
        return self.shots[pos.x][pos.y]

    def get_grid_color(self, pos: Pos, enemy=False) -> colors:
        color = colors.GRID
        if not enemy:
            if self.get_grid_ship(pos):
                color = colors.SHIP

        if self.get_grid_shot(pos):
            if enemy:
                color = colors.VISIBLE
            else:
                color = colors.SHOT
            
            ship = self.get_grid_ship(pos)
            if ship != None:
                # if enemy:
                color = colors.UNK_SHIP
                # see if the ship is hit in that position
                if self.get_ship_shot(ship, pos):
                    color = colors.HIT 
                # else:
                #     color = colors.UNK_SHIP

                    # if self.get_ship_shot(ship, pos):
                    #     color = colors.HIT

        return color

    def set_nickname(self, new_nickname: str) -> None:
        self.nickname = new_nickname

    def get_nickname(self) -> str:
        return self.nickname

    def attempt_rotation(self, ship_index: int) -> bool:
        ship_to_rotate = self.ships[ship_index]

        ship_to_rotate.get_position().horizontal = (not ship_to_rotate.get_position().horizontal)

        if self.ships_colliding():
            ship_to_rotate.get_position().horizontal = (not ship_to_rotate.get_position().horizontal)

        return True
