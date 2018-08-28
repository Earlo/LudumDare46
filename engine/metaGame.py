from abc import ABC  # abstractmethod


class MetaGame(ABC):
  def __init__(self, ENGINE):
    self.ENGINE = ENGINE
    self.entities = []
    print("geimu starttooo")

  def tick(self):
    time = self.ENGINE.clock.get_time()
    for e in self.entities:
      e.tick(time)
