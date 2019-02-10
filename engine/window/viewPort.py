from pygame import Surface


class ViewPort():
  def __init__(self, x, y):
    self.updates = []
    self.surf = Surface((x, y))

  def get_updates(self):
    return self.updates

  def clear_updates(self):
    self.updates = []

  def resize(self, event):
    self.surf = Surface((event.w, event.h))

  def clear(self):
    self.fill((255, 255, 255, 0))
    self.updates.append(self.get_rect())

  def draw(self, surf, pos, area):
    return self.surf.blit(surf, pos, area)

  @property
  def w(self):
    return self.surf.get_width()

  @property
  def h(self):
    return self.surf.get_height()

  def fill(self, c):
    self.surf.fill(c)

  def get_rect(self):
    return self.surf.get_rect()
