from abc import ABC  # abstractmethod


class MetaGame(ABC):
  def __init__(self, ENGINE):
    self._ENGINE = ENGINE
    self.entities = []

  def tick(self):
    time = self._ENGINE.clock.get_time()
    for e in self.entities:
      e.tick(time)

  def load_gui(self, gui):
    self._ENGINE.viewportHandler.viewPorts['GUI'].load_GUI(gui)

  def load_bgr(self, bgr):
    self._ENGINE.viewportHandler.viewPorts['GAME'].background_tile = bgr
