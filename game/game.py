
from .level import ExampleLevel


# should it inherit engine? Maybe?
class Game():
  def __init__(self, ENGINE):
    self.ENGINE = ENGINE
    self.pos = [0, 0]

    self.entities = []

    self.level = ExampleLevel(self)

    print("geimu starttooo")

  def tick(self):
    self.level.tick()
    for e in self.entities:
      e.tick()
