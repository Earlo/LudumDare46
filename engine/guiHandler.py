import pygame
from . import windowHandler

from .constants import FUNCTIONCALLEVENT
from .gui.button import Button


from .constants import SWIDTH, SHEIGTH

class GuiHandler(windowHandler.WindowHandler):

  def __init__(self):
    super().__init__()

    self.GUI = []
    self.active_text_field = None
    self.active_drag_obj = None

    self.surf_GUI = pygame.Surface((self.w, self.h), pygame.HWSURFACE)

    ## TODO move
    self.GUI = [Button(self.surf_GUI, (0.2, 0.1), (.1, 0.1), "tesets", [FUNCTIONCALLEVENT, self.STARTGAME])]
    self.refresh_GUI()
    self.MainWindow.blit(self.surf_GUI, self.gamepos)
    pygame.display.flip()

    #from ..Gui import screens
    #self.load_GUI(screens.SMainMenu)

  def update_resolution(self):
    super().update_resolution()
    self.adjust_GUI()

  def refresh_GUI(self):
    for wid in self.GUI:
      wid.draw()
      wid.blit()

  def reset_GUI(self):
    self.surf_GUI = pygame.Surface((self.w, self.h), pygame.HWSURFACE)

    self.GUI = []
    self.active_text_field = None

    self.blit_GUI()

  def load_GUI(self, GUI):
    self.reset_GUI()

    #TODO GUI(self) is shit
    GUI(self)
    self.GUI_template = GUI

    self.refresh_GUI()
    self.blit_GUI()

  def blit_GUI(self):
    self.MainWindow.blit(self.surf_GUI, self.gamepos)
    pygame.display.flip()

  def adjust_GUI(self):
    for wid in self.GUI:
      wid.adjust(self.surf_GUI)
    self.refresh_GUI()
