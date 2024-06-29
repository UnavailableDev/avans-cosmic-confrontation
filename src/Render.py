import pygame

from ships import BaseShip
from datatypes import Position as Pos
from Player import Player

from Defines import colors


class Render:
   def __init__(self, screen, rows, cols) -> None:
      self.screen = screen
      self.font = pygame.font.SysFont(None, 24)

      self.PLAYER_GRID_OFFSET = 50


      # self.MARGIN = 5  # Space between rectangles
      self.cols = cols
      self.rows = rows

      self.update_screen_size()
      

   def update_screen_size(self) -> None:
      self.SCREEN_HEIGHT = self.screen.get_height()
      self.SCREEN_WIDTH = self.screen.get_width()

      # Get smallest value of SCREEN_WIDTH/HEIGHT

      # (val * 0.75)/self.rows => RECT_LENGTH

      self.RECT_LENGTH = 30

      self.MARGIN = self.RECT_LENGTH * 0.2
   
   def grid_to_scren(self, col, row):
      x = col * (self.RECT_LENGTH + self.MARGIN)
      y = row * (self.RECT_LENGTH + self.MARGIN)

      return (int(x), int(y))

   def draw_square(self, col, row, color) -> None:
      x, y = self.grid_to_scren(col, row)
      pygame.draw.rect(self.screen, color, (x, y, self.RECT_LENGTH, self.RECT_LENGTH))

   def draw_ship(self, col, row, offset: Pos, color, ship: BaseShip) -> None:
      ship_pos: Pos = ship.get_position()
      vertecies = []

      ship_size = ship.get_size()

      if ship_pos.horizontal is True:
         # Render end points horizontal
         if ship_pos.x == col:
            vertecies.append((col+0.8, row))
            vertecies.append((col, row+0.4))
            vertecies.append((col+0.8, row+0.8))
         elif ship_pos.x+ship_size == col + 1:
            vertecies.append((col, row))
            vertecies.append((col+0.8, row+0.4))
            vertecies.append((col, row+0.8))

      elif ship_pos.horizontal is False:
         # Render end points vertical
         if ship_pos.y == row:
            vertecies.append((col, row+0.8))
            vertecies.append((col+0.4, row))
            vertecies.append((col+0.8, row+0.8))
         elif ship_pos.y+ship_size == row + 1:
            vertecies.append((col, row))
            vertecies.append((col+0.4, row+0.8))
            vertecies.append((col+0.8, row))

      if len(vertecies) > 2:
         for idx in range(len(vertecies)):
            x, y = vertecies[idx]
            vertecies[idx] = self.grid_to_scren(x + offset.x, y + offset.y)
         
         pygame.draw.polygon(self.screen, color, vertecies)
      else:
         self.draw_square(col + offset.x, row + offset.y, color)

   def draw_grid(self, p: Player, enemy: bool, offset: Pos) -> None:
      for col in range(self.cols):
         for row in range(self.rows):


            color: colors = p.get_grid_color(Pos(col, row), enemy)
            if color is colors.GRID or color is colors.UNK_SHIP:
               self.draw_square(col + offset.x, row + offset.y, color.value)
            else:
               ship = p.get_grid_ship(Pos(col, row))
               if ship is not None:
                  self.draw_square(col + offset.x, row + offset.y, colors.GRID.value)
                  self.draw_ship(col, row, offset, color.value, ship)
               else:
                  self.draw_square(col + offset.x, row + offset.y, color.value)
