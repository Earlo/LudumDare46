import pygame

from .gameCamera import GameCamera
from .guiPort import GuiPort

from ..singleton import Singleton
from ..constants import SWIDTH, SHEIGTH


class ViewportHandler(metaclass=Singleton):
  def __init__(self):
    self.window = pygame.display.set_mode((SWIDTH, SHEIGTH), pygame.DOUBLEBUF)

    self.needs_resize = False
    self.last_resize_request = 0

    # self.relative_cordinate(self.parent_surf, *self.rsurf)
    self.viewPorts = {'GUI': GuiPort(SWIDTH, SHEIGTH)}
    self.camera = GameCamera(self, SWIDTH, SHEIGTH)
    self.to_erase = []
    self.flip = False

  def force_erase(self, rect):
    self.to_erase.append(rect)

  def rezise_request(self, event):
    self.needs_resize = True
    self.last_resize_request = pygame.time.get_ticks()
    super().rezise_request(event)

  def update_display(self):
    if self.needs_resize:
      if pygame.time.get_ticks() - self.last_resize_request > 50:
        self.update_resolution()
        self.needs_resize = False
        self.flip = True

    update_rects = self.blit_updates()
    if not (update_rects == []):
      print(update_rects)
    if self.flip:
      self.flip = False
      pygame.display.flip()
    elif update_rects:
      pygame.display.update(update_rects)

  def blit_updates(self):
    update_rects = self.erase()

    for VP in self.viewPorts.values():
      # TODO vp.updateGenerator
      for change in VP.updates:
        self.window.blit(VP, change, change)
        update_rects.append(change)
        # TODO fix design error
        # Only things that have moved should be erased
        # self.to_erase.append(rect)
      VP.updates = []
    return update_rects

  def erase(self):
    update_rects = []
    cam_x = -self.camera.previous.x
    cam_y = -self.camera.previous.y
    for rect in self.to_erase:
      pos = rect.move(cam_x, cam_y)
      self.window.blit(self.bgr_surf, pos, rect)
      update_rects.append(rect)
    self.to_erase = []
    return update_rects
