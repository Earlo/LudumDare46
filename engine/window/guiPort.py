from .viewPort import ViewPort
from ..gui.guiLibrary import GuiLibrary


class GuiPort(ViewPort):
  guiLib = GuiLibrary()

  def __init__(self, x, y):
    super().__init__(x, y)
    self.GUI = []
    self.active_text_field = None
    self.active_drag_obj = None

    self.gui_area = self.get_rect()

  def resize(self):
    super().resize()
    self.adjust_GUI()

  def refresh_GUI(self):
    # TODO remove
    from random import randrange
    self.fill((randrange(255), randrange(255), randrange(255)))

    for wid in self.GUI:
      wid.draw()
      self.updates.append(wid.blit())

  def reset_GUI(self):
    self.clear()
    self.GUI = []
    self.active_text_field = None

  def load_GUI(self, GUI):
    self.reset_GUI()
    for g in GUI:
      self.load_widget(g)
    self.GUI_template = GUI

    self.refresh_GUI()

  def load_widget(self, w):
    t = w[0]
    args = w[1:]
    # TODO figure, self or self surf
    self.GUI.append(self.guiLib[t](self.surf, *args))

  def adjust_GUI(self):
    for wid in self.GUI:
      wid.adjust(self)
    self.refresh_GUI()
