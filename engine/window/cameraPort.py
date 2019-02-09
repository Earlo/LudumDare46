from pygame import Rect, Surface
import itertools

from math import sin, cos

from .viewPort import ViewPort

from ..graphicalAssetHandler import GraphicalAssetHandler


class CameraPort(ViewPort):
  graphicalAssetHandler = GraphicalAssetHandler()

  def __init__(self, x, y):
    super().__init__(x, y)
    self.erase = []
    self.previous = Rect(0, 0, x, y)
    self.camera = Rect(0, 0, x, y)
    self.movement_direction = 0
    self.background = "DEBUG"
    self.DDD = False

  def get_updates(self):
    return self.erase + self.updates

  def clear_updates(self):
    """if self.DDD:
      self._tile = self.graphicalAssetHandler['bgr']['DEBUG']
    else:
      self._tile = self.graphicalAssetHandler['bgr']['checker_dark']
    self.DDD = not self.DDD
    """
    # self.debug_move()

    self.erase = []
    for r in self.updates:
      self.clear_at(r.move(0, 0))
    self.updates = []

  def move_camera(self, x, y):
    self.previous = self.camera.copy()
    self.camera.move_ip(x, y)
    self.camera.x = max((self.camera.x, 0))
    self.camera.y = max((self.camera.y, 0))
    self.updates.append(self.get_rect())

  @property
  def background(self):
    return self._bgr

  @background.setter
  def background(self, new_bgr):
    print("setting bgr to {}".format(new_bgr))
    self._bgr = new_bgr
    self._tile = self.graphicalAssetHandler['bgr'][new_bgr]
    tw = self._tile.get_width()
    th = self._tile.get_height()
    self._fillTile = Surface((tw * 2, th * 2))

    for x, y in itertools.product(range(0, self.w, tw),
                                  range(0, self.h, self._tile.get_height())):
      self.surf.blit(self._tile, (x, y), self._tile.get_rect())
    for x, y in itertools.product(range(0, tw * 2, tw),
                                  range(0, th * 2, th)):
      self._fillTile.blit(self._tile, (x, y), self._tile.get_rect())

    self.updates.append(self.get_rect())

  def clear_at(self, r):
    area = r.copy()
    area.topleft = (r.x % self._tile.get_width(),
                    r.y % self._tile.get_height())
    print("Covering {}, with {} of {}".format(r, area, self._fillTile))
    self.surf.blit(self._fillTile, r, area)
    self.erase.append(r)

  def debug_move(self):
    self.movement_direction += 0.05
    self.move_camera(5 * cos(self.movement_direction),
                     5 * sin(self.movement_direction))
