from ..singleton import Singleton
from .button import Button


class GuiLibrary(metaclass=Singleton):
    def __init__(self):
        self._wDict = {"BUTTON": Button}
        super().__init__()

    def __getitem__(self, key):
        return self._wDict[key]

    # def __setitem__(self, key, value):
    #  self._wDict[key] = value
