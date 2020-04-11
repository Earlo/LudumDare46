from abc import ABC  # abstractmethod

from engine.window.viewportHandler import ViewportHandler
from engine.window.cameraPort import CameraPort
from engine.window.guiPort import GuiPort


class MetaGame(ABC):
    def __init__(self, ENGINE):
        self._ENGINE = ENGINE
        self._ViewportHandler = ViewportHandler()

        self.entities = []

    def tick(self):
        time = self._ENGINE.clock.get_time()
        for e in self.entities:
            e.tick(time)

    def load_gui(self, gui):
        self._ViewportHandler.viewPorts["GUI"].load_GUI(gui)

    def load_bgr(self, bgr):
        self._ViewportHandler.viewPorts["GAME"].background = bgr

    def add_guiport(self, name, x, y):
        self._ViewportHandler.viewPorts[name] = GuiPort(x, y)

    def add_cameraport(self, name, x, y):
        self._ViewportHandler.viewPorts[name] = CameraPort(x, y)
