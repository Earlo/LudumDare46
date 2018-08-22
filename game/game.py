class Game():
  def __init__(self, ENGINE):
    self.ENGINE = ENGINE
    self.pos = [0, 0]

    self.entities = []

    print("geimu starttooo")

  def tick(self):
    for e in self.entities:
      e.tick()
