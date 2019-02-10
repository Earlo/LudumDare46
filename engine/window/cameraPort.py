from pygame import Rect
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
    # self.background = "DEBUG"
    self.DDD = False

  def get_updates(self):
    return self.erase + self.updates

  def clear_updates(self):
    """
    if self.DDD:
      self.background = 'DEBUG'
    else:
      self.background = 'checker_dark'
    self.DDD = not self.DDD
    """
    # self.debug_move()

    self.erase = []
    for r in self.updates:
      # TODO figure the move
      self.clear_at(r.move(0, 0))
    self.updates = []

  @property
  def x(self):
    return self.camera.x

  @property
  def y(self):
    return self.camera.y

  def move_camera(self, x, y):
    print("MBO")
    self.previous = self.camera.copy()
    self.camera.move_ip(x, y)
    # self.camera.x = max((self.camera.x, 0))
    # self.camera.y = max((self.camera.y, 0))
    self.updates.append(self.get_rect())

  @property
  def background(self):
    return self._bgr

  @background.setter
  def background(self, new_bgr):
    print("setting bgr to {}".format(new_bgr))
    self._bgr = new_bgr
    self._tile = self.graphicalAssetHandler['bgr'][new_bgr]

    self.updates.append(self.get_rect())

  def clear_at(self, r):
    tw = self._tile.get_width()
    th = self._tile.get_height()
    tile_rect = self._tile.get_rect()
    clip_r = r.copy()
    rangX = [r.x] + [(1 + n) * tw for n in range(r.x // tw, (r.x + r.w) // tw)]
    rangY = [r.y] + [(1 + n) * th for n in range(r.y // th, (r.y + r.h) // th)]
    for x, y in itertools.product(rangX, rangY):
      clip_r.topleft = (x % tw, y % th)
      area = clip_r.clip(tile_rect)
      self.draw(self._tile, (x, y), area)
    self.erase.append(r)

  def draw(self, surf, pos, area):
    p = (pos[0] - self.x, pos[1] - self.y)
    super().draw(surf, p, area)

  def debug_move(self):
    self.movement_direction += 0.05
    self.move_camera(5 * cos(self.movement_direction),
                     5 * sin(self.movement_direction))
