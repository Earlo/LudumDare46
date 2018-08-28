from ..graphicalAssetHandler import GraphicalAssetHandler
from ..constants import SWIDTH, SHEIGTH


class BaseSurfaceHandler:
  def __init__(self):
    super().__init__()
    self.w = SWIDTH
    self.h = SHEIGTH

    self.graphical_asset_handler = GraphicalAssetHandler()

  def rezise_request(self, event):
    self.w = event.w
    self.h = event.h
