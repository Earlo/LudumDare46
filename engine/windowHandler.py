import pygame
from . import graphicalAssetHandler

from .constants import SWIDTH, SHEIGTH


class WindowHandler:
  def __init__(self):
    self.w = SWIDTH
    self.h = SHEIGTH
    self.create_surfaces()
    self.gamepos = (10, 10)

    self.GHandle = graphicalAssetHandler.GraphicalAssetHandler()
    self.needs_resize = False
    self.last_resie_request = 0

    self.updates = {}

  def create_surfaces(self): #TODO reconsider this
    self.MainWindow = pygame.display.set_mode((self.w, self.h), pygame.HWSURFACE | pygame.DOUBLEBUF)
    self.surf_GUI = pygame.Surface((self.w, self.h), pygame.HWSURFACE)
    self.surf_GUI.set_colorkey((0, 0, 0))

  def update_resolution(self):
    self.create_surfaces()

  def rezise_request(self, event):
    self.needs_resize = True
    self.last_resie_request = pygame.time.get_ticks()

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
            self.MainWindow.blit(s, r, r)
            #self.MainWindow.blit(s, r)
            upd.append(r)
        self.updates[depth] = []
    if not upd == [] and not flip:
        pygame.display.update(upd)
    elif flip:
        pygame.display.flip()"""

    pygame.display.flip()

  def drawGame(self):

    self.surf_GAME.blit(self.GAME.AREA.surf(), (0, self.GAME.AREA.scroll))
    if not self.GAME.AREA.oldsprite == "":
      self.surf_GAME.blit(self.GAME.AREA.oldsurf(), (0, self.GAME.AREA.oldscroll))
    for e in self.GAME.effects:
      self.surf_GAME.blit(e.CURRENTSURFACE, e)
    for u in self.GAME.units:
      self.surf_GAME.blit(u.CURRENTSURFACE, u)
    for a in self.GAME.ammo:
      self.surf_GAME.blit(a.CURRENTSURFACE, a)

    self.MainWindow.blit(self.surf_GAME, self.gamepos, self.GAME.AREA)
    self.MainWindow.blit(self.surf_EFFECT, self.gamepos, self.GAME.AREA)
