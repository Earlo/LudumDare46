import pygame

from .viewPort import ViewPort
from ..constants import FUNCTIONCALLEVENT
from ..gui.button import Button


class GuiPort(ViewPort):

  def __init__(self, x, y):
    super().__init__(x, y)
    self.fill((50, 100, 50))
    self.GUI = []
    self.active_text_field = None
    self.active_drag_obj = None

    self.gui_area = self.get_rect()

    # from ..Gui import screens
    # self.load_GUI(screens.SMainMenu)

  def update_resolution(self):
    super().update_resolution()
    self.adjust_GUI()

  def refresh_GUI(self):
    for wid in self.GUI:
      wid.draw()
      wid.blit()

  def reset_GUI(self):
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

  def adjust_GUI(self):
    for wid in self.GUI:
      wid.adjust(self)
    self.refresh_GUI()
