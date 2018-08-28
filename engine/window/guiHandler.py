import pygame

from .baseSurfaceHandler import BaseSurfaceHandler
from ..constants import FUNCTIONCALLEVENT
from ..gui.button import Button


class GuiHandler(BaseSurfaceHandler):

  def __init__(self):
    super().__init__()

    self.GUI = []
    self.active_text_field = None
    self.active_drag_obj = None

    self.surf_GUI = pygame.Surface((self.w, self.h), pygame.HWSURFACE)
    self.gui_area = pygame.Rect(0, 0, self.w, self.h)

    # from ..Gui import screens
    # self.load_GUI(screens.SMainMenu)
  # TODO remove
  def test_gui(self):
    self.GUI = [Button(self.surf_GUI,
                       (0.2, 0.1), (.1, 0.1),
                       "tesets", [FUNCTIONCALLEVENT, self.STARTGAME])]
    self.refresh_GUI()
    self.blit_GUI()

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

    # TODO GUI(self) is shit
    GUI(self)
    self.GUI_template = GUI

    self.refresh_GUI()
    self.blit_GUI()

  # TODO, less copypasta
  def blit_GUI(self):
    self.draw_frame(0, self.surf_GUI, self.gui_area)
    self.flip = True

  def adjust_GUI(self):
    for wid in self.GUI:
      wid.adjust(self.surf_GUI)
    self.refresh_GUI()
