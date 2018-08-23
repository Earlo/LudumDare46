from abc import ABC, abstractmethod


class MetaGame(ABC):
  def __init__(self, ENGINE):
    self.ENGINE = ENGINE
    print("geimu starttooo")

  @abstractmethod
  def tick(self):
    pass
