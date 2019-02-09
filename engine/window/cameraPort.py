import pygame
import itertools

from .viewPort import ViewPort


class CameraPort(ViewPort):
  def __init__(self, x, y):
    super().__init__(x, y)
    self._bgr_surf = pygame.Surface((self.w, self.h), pygame.HWSURFACE)
    self._background_tile = "checker_dark"

  @property
  def background_tile(self):
    return self._background_tile

  @background_tile.setter
  def background_tile(self, new_tile):
    # self.reset_background()
    self._background_tile = new_tile
    tile = self.graphicalAssetHandler['bgr'][new_tile]
    for x, y in itertools.product(range(0, self.w, tile.get_width()),
                                  range(0, self.h, tile.get_height())):
      self.bgr_surf.blit(tile, (x, y), tile.get_rect())

    self.blit_background()

  @property
  def bgr_surf(self):
    return self._bgr_surf

  def reset_background(self):
    self.bgr_surf = pygame.Surface((self.w, self.h), pygame.HWSURFACE)

  def blit_background(self):
    self.force_erase(self)
