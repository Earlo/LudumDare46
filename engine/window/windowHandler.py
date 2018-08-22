import pygame

from .guiHandler import GuiHandler
from .bgrHandler import BgrHandler


class WindowHandler(GuiHandler, BgrHandler):
  def __init__(self):

    super().__init__()
    self.window = pygame.display.set_mode((self.w, self.h),
                                          pygame.HWSURFACE |
                                          pygame.DOUBLEBUF)

    self.needs_resize = False
    self.last_resie_request = 0

    self.updates = {}

  def rezise_request(self, event):
    self.needs_resize = True
    self.last_resie_request = pygame.time.get_ticks()
    super().rezise_request(event)

  def update_display(self):
    """flip = False
    if self.needs_resize:
        if pygame.time.get_ticks() - self.last_resie_request > 50:
            self.update_resolution()
            self.needs_resize = False
            flip = True
    sorted(self.updates)
    upd = []
    for depth in self.updates:
        for change in self.updates[depth]:
            s, r = change
            self.window.blit(s, r, r)
            # self.window.blit(s, r)
            upd.append(r)
        self.updates[depth] = []
    if not upd == [] and not flip:
        pygame.display.update(upd)
    elif flip:
        pygame.display.flip()"""

    pygame.display.flip()

  def draw_game(self):

    # TODO refactor
    # for e in self.GAME.entities:
    #   self.surf_GAME.blit(e.CURRENTSURFACE, e)

    # TODO no
    self.window.blit(self.surf_GUI, self.gui_pos, self.gui_area)
    self.window.blit(self.surf_BGR, self.bgr_pos, self.bgr_area)
