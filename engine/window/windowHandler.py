import pygame
from collections import defaultdict

from .guiHandler import GuiHandler
from .bgrHandler import BgrHandler
from .gameCamera import GameCamera


class WindowHandler(GuiHandler, BgrHandler):
  def __init__(self):

    super().__init__()
    self.window = pygame.display.set_mode((self.w, self.h),
                                          pygame.HWSURFACE |
                                          pygame.DOUBLEBUF)

    self.needs_resize = False
    self.last_resie_request = 0

    self.camera = GameCamera(self.w, self.h)

    self.updates = defaultdict(list)
    self.flip = False

  def rezise_request(self, event):
    self.needs_resize = True
    self.last_resie_request = pygame.time.get_ticks()
    super().rezise_request(event)

  def update_display(self):
    if self.needs_resize:
      if pygame.time.get_ticks() - self.last_resie_request > 50:
        self.update_resolution()
        self.needs_resize = False
        self.flip = True

    update_rects = self.blit_updates()

    if self.flip:
      pygame.display.flip()
    elif update_rects:
      pygame.display.update(update_rects)

  def blit_updates(self):
    update_rects = self.erase()
    sorted(self.updates)

    cam_x = self.camera.x
    cam_y = self.camera.y
    for depth in self.updates:
      for change in self.updates[depth]:
        sprite, rect = change
        self.window.blit(sprite, rect.move(cam_x, cam_y))
        update_rects.append(rect)
        self.updates[-1].append(rect)
      self.updates[depth] = []
    return update_rects

  def erase(self):
    update_rects = []
    cam_x = self.camera.previous.x
    cam_y = self.camera.previous.y
    for rect in self.updates[-1]:
      pos = rect.move(cam_x, cam_y)
      self.window.blit(self.surf_BGR, pos, pos)
      update_rects.append(rect)
    self.updates[-1] = []
    return update_rects

  def blit_everything(self):

    # TODO refactor
    # for e in self.GAME.entities:
    #   self.surf_GAME.blit(e.CURRENTSURFACE, e)

    # TODO no
    self.window.blit(self.surf_GUI, self.camera, self.gui_area)
    self.window.blit(self.surf_BGR, self.camera, self.bgr_area)
