import pygame
import itertools

from .baseSurfaceHandler import BaseSurfaceHandler


# NOTE Extend a bgr class form SPRITE if we want to add parallax bgr support
class BgrHandler(BaseSurfaceHandler):

  def __init__(self):
    super().__init__()
    self._bgr_surf = pygame.Surface((self.w, self.h), pygame.HWSURFACE)
    self.rect = self.bgr_surf.get_rect()
    self._background_tile = "checker_dark"

  @property
  def background_tile(self):
    return self._background_tile

  @background_tile.setter
  def background_tile(self, new_tile):
    # self.reset_background()
    self._background_tile = new_tile
    tile = self.graphical_asset_handler['bgr'][new_tile]
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
    self.force_erase(self.rect)

  def update_resolution(self):
    super().update_resolution()
