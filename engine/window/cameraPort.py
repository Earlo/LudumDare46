import pygame
import itertools

from math import sin, cos

from .viewPort import ViewPort

from ..graphicalAssetHandler import GraphicalAssetHandler


class CameraPort(ViewPort):
  graphicalAssetHandler = GraphicalAssetHandler()

  def __init__(self, x, y):
    super().__init__(x, y)
    self.previous = pygame.Rect(0, 0, x, y)
    self.camera = pygame.Rect(0, 0, x, y)
    self.movement_direction = 0
    self._background_tile = ""

  def move_camera(self, x, y):
    self.previous = self.camera.copy()
    self.camera.move_ip(x, y)
    self.camera.x = max((self.x, 0))
    self.camera.y = max((self.y, 0))
    self.updates.append(self.get_rect())

  @property
  def background_tile(self):
    return self._background_tile

  @background_tile.setter
  def background_tile(self, new_tile):
    print("Setting bagr")
    self._background_tile = new_tile
    tile = self.graphicalAssetHandler['bgr'][new_tile]
    for x, y in itertools.product(range(0, self.w, tile.get_width()),
                                  range(0, self.h, tile.get_height())):
      self.surf.blit(tile, (x, y), tile.get_rect())

    self.updates.append(self.get_rect())

  def debug_move(self):
    self.movement_direction += 0.05
    self.move_camera(5 * cos(self.movement_direction),
                     5 * sin(self.movement_direction))
