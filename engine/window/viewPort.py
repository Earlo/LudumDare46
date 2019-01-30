import pygame


class ViewPort(pygame.Surface):
  def __init__(self, x, y):
    super().__init__((x, y))
    self.updates = []

  def get_updates(self):
    return self.updates

  def rezise_request(self, event):
    self.w = event.w
    self.h = event.h
