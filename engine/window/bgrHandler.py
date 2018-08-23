import pygame

from .baseSurfaceHandler import BaseSurfaceHandler


class BgrHandler(BaseSurfaceHandler):

  def __init__(self):
    super().__init__()
    self.surf_BGR = pygame.Surface((self.w, self.h), pygame.HWSURFACE)
    self.bgr_area = pygame.Rect(0, 0, self.w, self.h)

  def update_resolution(self):
    super().update_resolution()

  def reset_BGR(self):
    self.surf_BGR = pygame.Surface((self.w, self.h), pygame.HWSURFACE)

  def load_BGR(self, BGR):
    self.reset_BGR()

    self.blit_BGR()

  def blit_BGR(self):
    self.window.blit(self.surf_BGR, self.bgr_area, self.bgr_area)
    pygame.display.flip()
