import pygame


class ViewPort(pygame.Surface):
  def __init__(self, x, y):
    super().__init__((x, y))
    self.updates = []

  def get_updates(self):
    return self.updates

  def resize(self, event):
    # TODO FIX
    # self.w = event.w get_width()
    # self.h = event.h get_height()
    pass
