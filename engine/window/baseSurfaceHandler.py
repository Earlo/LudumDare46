import pygame

from ..graphicalAssetHandler import GraphicalAssetHandler

from ..constants import SWIDTH, SHEIGTH


class BaseSurfaceHandler:
  def __init__(self):
    super().__init__()

    self.w = SWIDTH
    self.h = SHEIGTH

    self.graphical_asset_handler = GraphicalAssetHandler()

    self.updates = {}

  def rezise_request(self, event):
    self.w = event.w
    self.h = event.h

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
