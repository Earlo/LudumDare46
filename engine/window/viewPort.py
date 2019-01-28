import pygame


class ViewPort(pygame.Surface):
  def __init__(self, x, y):
    super().__init__((x, y))

  def rezise_request(self, event):
    self.w = event.w
    self.h = event.h
