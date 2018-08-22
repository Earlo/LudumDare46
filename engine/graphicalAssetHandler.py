import os
import pygame
import __main__


class GraphicalAssetHandler(dict):
  BASEPATH = os.path.dirname(os.path.realpath(__main__.__file__))
  asset_path = os.path.join(BASEPATH, "Assets")

  def __init__(self):
    super().__init__()

    self.load("SPRITES", colorkey_pos=(0, 0), flags=[pygame.RLEACCEL])
    self.load("PORTRAIT", colorkey_pos=(0, 0))
    self.load("BGR")

  def load(self, end_path, colorkey_pos=(-1, -1), flags=[]):
    self[end_path] = dict()
    path_to_folder = os.path.join(self.asset_path, end_path)
    for root, dirs, files in os.walk(path_to_folder):
      for file in files:
        if file.endswith(".png"):
          file_path = os.path.join(path_to_folder, file)
          base_name = file.split(os.path.sep)[-1].split(".")[0]

          img = pygame.image.load(file_path).convert()
          img.set_colorkey(img.get_at(colorkey_pos), *flags)

          self[end_path][base_name] = img
