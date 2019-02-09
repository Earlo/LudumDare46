import os
import pygame
import __main__

from .singleton import Singleton


class GraphicalAssetHandler(metaclass=Singleton):
  BASEPATH = os.path.dirname(os.path.realpath(__main__.__file__))
  asset_path = os.path.join(BASEPATH, "assets")

  def __init__(self):
    self._gDict = {}
    super().__init__()

  def __getitem__(self, key):
    return self._gDict[key]

  def __setitem__(self, key, value):
    self._gDict[key] = value

  def load(self, end_path, colorkey_pos=False, flags=[]):
    self[end_path] = dict()
    path_to_folder = os.path.join(self.asset_path, end_path)
    for root, dirs, files in os.walk(path_to_folder):
      for file in files:
        if file.endswith(".png"):
          file_path = os.path.join(path_to_folder, file)
          base_name = file.split(os.path.sep)[-1].split(".")[0]
          img = pygame.image.load(file_path).convert()
          if(colorkey_pos):
            img.set_colorkey(img.get_at(colorkey_pos), *flags)

          self[end_path][base_name] = img
          