# from __future__ import annotations
from Player import Player
from ships import *

from math import sqrt

def direct_to_distance(a: Pos, b: Pos):
    delta_x = abs(a.x - b.x)
    delta_y = abs(a.y - b.y)
    d = sqrt(delta_x^2 + delta_y^2)

    return d

class Visitor:
    # __player: Player = None

    def __init__(self) -> None:
        pass

    def do(self, ship, actor: Player, foo: Player, pos: Pos):
        if isinstance(ship, ScoutShip):
            self.do_ability_scout(ship, actor, foo, pos)

        if isinstance(ship, HunterShip):
            self.do_ability_hunter(ship, actor, foo, pos)

        if isinstance(ship, BattleShip):
            self.do_ability_battle(ship, actor, foo, pos)

        if isinstance(ship, CruiserShip):
            self.do_ability_cuiser(ship, actor, foo, pos)

        if isinstance(ship, CommandShip):
            self.do_ability_command(ship, actor, foo, pos)

    # def do_ability(self, ship: BaseShip, actor: Player, foo: Player, pos: Pos):
    #     print("Base")
    #     ship.set_ability_available(False)

    def do_ability_scout(self, ship: ScoutShip, actor: Player, foo: Player, pos: Pos):
        # foo.shots
        print("scout")
        ship.set_ability_available(False)

    def do_ability_hunter(self, ship: HunterShip, actor: Player, foo: Player, pos: Pos):
        shortest_dist = 9999
        closest = []
        for sh in foo.ships:
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
                        print(target)

                        if target:
                            target.x += n
                        else:
                            target.y += n
                        break
                print(target)
                foo.shoot_grid(target)
                break
            if sh is None:
                return False
        

        # Update shots to show actually shot pos
        
        print("Homing Missile")
        ship.set_ability_available(False)

    def do_ability_battle(self, ship: BattleShip, actor: Player, foo: Player, pos: Pos):
        print("Battle")
        ship.set_ability_available(False)

    def do_ability_cuiser(self, ship: CruiserShip, actor: Player, foo: Player, pos: Pos):
        print("Cruise")
        ship.set_ability_available(False)
    
    def do_ability_command(self, ship: CommandShip, actor: Player, foo: Player, pos: Pos):
        print("Command")
        ship.set_ability_available(False)


