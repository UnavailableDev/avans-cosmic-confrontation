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


      self.MARGIN = 5  # Space between rectangles
      self.cols = cols
      self.rows = rows

      self.update_screen_size()
      

   def update_screen_size(self) -> None:
      self.SCREEN_HEIGHT = self.screen.get_height()
      self.SCREEN_WIDTH = self.screen.get_width()

      # Get smallest value of SCREEN_WIDTH/HEIGHT

      # (val * 0.75)/self.rows => RECT_LENGTH

      self.RECT_LENGTH = 30
      

   def draw_square(self, col, row, color) -> None:
      x = col * (self.RECT_LENGTH + self.MARGIN)
      y = row * (self.RECT_LENGTH + self.MARGIN)
      pygame.draw.rect(self.screen, color, (x, y, self.RECT_LENGTH, self.RECT_LENGTH))

   def draw_ship(self, col, row, color, ship: BaseShip) -> None:
      # ship_pos: Pos = ship.get_position()
      # vertecies = []

      # ship_size = ship.get_size()

      # if ship_pos.horizontal is True:
      #    if ship_pos.x == row or ship_pos.x+ship_size == row:
      #       # Render end points
      # else:
      #    pass

      self.draw_square(col, row, (128, 128, 255))



   def draw_grid(self, p: Player, offset: Pos) -> None:
      for col in range(self.cols):
         for row in range(self.rows):


            color: colors = p.get_grid_color(Pos(col, row), False)
            self.draw_square(col + offset.x, row + offset.y, color.value)
            # if color is colors.GRID or colors.SHOT or colors.UNK_SHIP:
            #    self.draw_square(col + offset.x, row + offset.y, color.value)
            # else:
            #    ship = p.get_grid_ship(Pos(col, row))
            #    self.draw_ship(col + offset.x, row + offset.y, color, ship)