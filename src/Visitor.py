# from __future__ import annotations
from Player import Player
from ships import *

from math import sqrt

def direct_to_distance(a: Pos, b: Pos):
    delta_x = abs(a.x - b.x)
    delta_y = abs(a.y - b.y)
    d = sqrt(delta_x^2 + delta_y^2)

    return d

##! use hor to define if the area should be 3x1/1x3, if None, area is 3x3
##! function returns true if space is available
def three_check(player: Player, pos: Pos, hor=None):
    if hor == None:
        return (0 < pos.x and pos.x < player.rows) and (0 < pos.y and pos.y < player.cols)
    
    if hor == True:
        return (0 < pos.x and pos.x < player.rows) and (0 <= pos.y and pos.y <= player.cols)
    else:
        return (0 <= pos.x and pos.x <= player.rows) and (0 < pos.y and pos.y < player.cols)

def three_mark(action: bool, subject: Player, pos: Pos, hor=None):
    if hor == None:
        subject.shots[pos.x-1][pos.y-1] = action
        subject.shots[pos.x-0][pos.y-1] = action
        subject.shots[pos.x+1][pos.y-1] = action
    if hor == None or hor == True:
        subject.shots[pos.x-1][pos.y] = action
        subject.shots[pos.x-0][pos.y] = action
        subject.shots[pos.x+1][pos.y] = action
    if hor == None:
        subject.shots[pos.x-1][pos.y+1] = action
        subject.shots[pos.x-0][pos.y+1] = action
        subject.shots[pos.x+1][pos.y+1] = action

    if hor == False:
        subject.shots[pos.x][pos.y-1] = action
        subject.shots[pos.x][pos.y-0] = action
        subject.shots[pos.x][pos.y+1] = action

class Visitor:
    # __player: Player = None

    def __init__(self) -> None:
        pass

    def do(self, ship, actor: Player, subject: Player, pos: Pos):
        if isinstance(ship, ScoutShip):
            return self.do_ability_scout(ship, actor, subject, pos)

        if isinstance(ship, HunterShip):
            return self.do_ability_hunter(ship, actor, subject, pos)

        if isinstance(ship, BattleShip):
            return self.do_ability_battle(ship, actor, subject, pos)

        if isinstance(ship, CruiserShip):
            return self.do_ability_cuiser(ship, actor, subject, pos)

        if isinstance(ship, CommandShip):
            return self.do_ability_command(ship, actor, subject, pos)

    # def do_ability(self, ship: BaseShip, actor: Player, subject: Player, pos: Pos):
    #     print("Base")
    #     ship.set_ability_available(False)

    def do_ability_scout(self, ship: ScoutShip, actor: Player, subject: Player, pos: Pos):
        if three_check(actor, pos):
            three_mark(True, subject, pos)
        else:
            return False
        # subject.shots
        print("scan")
        ship.set_ability_available(False)
        return True

    def do_ability_hunter(self, ship: HunterShip, actor: Player, subject: Player, pos: Pos):
        shortest_dist = 9999
        closest = []
        for sh in subject.ships:
            dist = direct_to_distance(pos, sh.get_position())
            if dist < shortest_dist:
                closest.append(sh)

        # Find intact piece of closest ship
        while True:
            sh: BaseShip = closest.pop()
            if sh.is_alive():
                target: Pos = None

                # Figure out where ship is not yet hit
                hits = sh.get_hits()
                for n, hit in enumerate(hits):
                    if not hit:
                        target = sh.get_position()

                        if target:
                            target.x += n
                        else:
                            target.y += n
                        break
                subject.shoot_grid(target)
                break
            if sh is None:
                return False
        

        # Update shots to show actually shot pos
        
        print("Homing Missile")
        ship.set_ability_available(False)
        return True

    def do_ability_cuiser(self, ship: CruiserShip, actor: Player, subject: Player, pos: Pos):

        print("Cruise")
        ship.set_ability_available(False)
        return True
    
    def do_ability_battle(self, ship: BattleShip, actor: Player, subject: Player, pos: Pos):
        print("Battle")
        ship.set_ability_available(False)
        return True

    def do_ability_command(self, ship: CommandShip, actor: Player, subject: Player, pos: Pos):
        print("Command")
        ship.set_ability_available(False)
        return True


