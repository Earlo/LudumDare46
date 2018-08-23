from math import sin, cos
import pygame


class GameCamera(pygame.Rect):
  def __init__(self, w, h):
    super().__init__(0, 0, w, h)
    self.movement_direction = 0

  def move(self, x, y):
    super().move_ip(x, y)

  def debug_move(self):
    self.movement_direction += 0.05
    self.move(5 * cos(self.movement_direction), 5 * sin(self.movement_direction))
