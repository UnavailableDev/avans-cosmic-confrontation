from datatypes import Position as Pos
from Player import Player
from Defines import colors
import random

class AI:
    __rows: int
    __cols: int

    __huntmode: bool = False

    def __init__(self, rows, cols) -> None:
        self.__rows = rows
        self.__cols = cols

        self.targets: Pos = []
        self.grid_shot: bool = []

    def push_target(self, pos: Pos):
        print(pos)
        if pos in self.targets or self.grid_shot[pos.x][pos.y]:
            return 0

        self.targets.append(pos)
        return 1

    def find_surrounding_positions(self, x, y):
        count = 0
        if x > 0:
            # self.grid_shot[x-1][y]
            count += self.push_target(Pos(x-1,y))
        if x < self.__rows-1:
            # self.grid_shot[x+1][y]
            count += self.push_target(Pos(x+1,y))
        if y > 0:
            # self.grid_shot[x][y-1]
            count += self.push_target(Pos(x,y-1))
        if y < self.__cols-1:
            # self.grid_shot[x][y+1]
            count += self.push_target(Pos(x,y+1))

        print(count, " targets count: ", len(self.targets))

    def update(self, player: Player):
        if self.grid_shot == player.shots:
            # No changes
            pass
        else:
            self.grid_shot = player.shots

        tot = 0
        for x in range(self.__rows):
            tot += sum(player.shots[x])
            for y, grid_val in enumerate(player.shots[x]):
                if grid_val:
                    if player.get_grid_ship(Pos(x,y)): # HIT
                        li = self.find_surrounding_positions(x, y)

        print("total shots ", tot)
    
    def shoot(self):
        if len(self.targets) > 0: # Hunt mode
            return self.targets.pop(0)

        rand_x = random.randrange(self.__rows)
        rand_y = random.randrange(self.__rows)

        # rand_x = random.randint(0, self.__rows)
        # rand_y = random.randint(0, self.__cols)

        # Returns shooting position
        return Pos(rand_x, rand_y)
