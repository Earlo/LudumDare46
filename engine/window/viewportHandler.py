import pygame

from ..singleton import Singleton
from ..constants import SWIDTH, SHEIGTH


class ViewportHandler(metaclass=Singleton):
  def __init__(self):
    self.window = pygame.display.set_mode((SWIDTH, SHEIGTH), pygame.DOUBLEBUF)

    self.needs_resize = False
    self.last_resize_request = 0

    # self.relative_cordinate(self.parent_surf, *self.rsurf)
    self.to_erase = []
    self.flip = False

  def resize(self, event):
    self.needs_resize = True
    self.last_resize_request = pygame.time.get_ticks()
    for wp in self.viewPorts.values:
      wp.resize(event)

  def update_display(self):
    if self.needs_resize:
      if pygame.time.get_ticks() - self.last_resize_request > 50:
        self.update_resolution()
        self.needs_resize = False
        self.flip = True

    update_rects = self.blit_updates()
    if not (update_rects == []):
      print("Updating {}".format(update_rects))
    if self.flip:
      self.flip = False
      pygame.display.flip()
    elif update_rects:
      pygame.display.update(update_rects)

  def blit_updates(self):
    update_rects = []
    for VP in self.viewPorts.values():
      # TODO vp.updateGenerator
      for change in VP.updates:
        self.window.blit(VP.surf, change, change)
        update_rects.append(change)
      VP.updates = []
    return update_rects
