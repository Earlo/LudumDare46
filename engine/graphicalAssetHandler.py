import os
import pygame
import __main__

BASEPATH = os.path.dirname(os.path.realpath(__main__.__file__))
fpath = os.path.join(BASEPATH, "Assets")

class GraphicalAssetHandler(dict):
  def __init__(self):
    super().__init__()

    self["SPRITE"] = dict()
    self["PORTRAIT"] = dict()
    self["BGR"] = dict()

    for root, dirs, files in os.walk(os.path.join(fpath, "sprites")):
      for file in files:
        if file.endswith(".png"):
          name = file.split(os.path.sep)[-1].split(".")[0]
          i = pygame.image.load(os.path.join(fpath, "sprites", file)).convert()
          i.set_colorkey(i.get_at((0, 0)), pygame.RLEACCEL)
          self["SPRITE"][name] = i

      for root, dirs, files in os.walk(os.path.join(fpath, "portraits")):
        for file in files:
          if file.endswith(".png"):
            path = os.path.join(fpath, "portraits", file)
            name = file.split(os.path.sep)[-1].split(".")[0]
            i = pygame.image.load(path).convert()
            i.set_colorkey(i.get_at((0, 0)))
            self["PORTRAIT"][name] = i

      for root, dirs, files in os.walk(os.path.join(fpath, "bgr")):
        for file in files:
          if file.endswith(".png"):
            path = os.path.join(fpath, "bgr", file)
            name = file.split(os.path.sep)[-1].split(".")[0]
            i = pygame.image.load(path).convert()
            self["BGR"][name] = i
