from math import sin, cos
import pygame


class GameCamera(pygame.Rect):
  def __init__(self, ENGINE, w, h):
    super().__init__(0, 0, w, h)
    self.ENGINE = ENGINE
    self.movement_direction = 0
    self.previous = self.copy()

  def move_camera(self, x, y):
    self.previous = self.copy()
    super().move_ip(x, y)
    # TODO clean this up
    self.x = max((self.x, 0))
    self.y = max((self.y, 0))
    self.ENGINE.blit_background()

  def debug_move(self):
    self.movement_direction += 0.05
    self.move_camera(5 * cos(self.movement_direction),
                     5 * sin(self.movement_direction))
