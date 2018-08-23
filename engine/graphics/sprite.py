import pygame


class Sprite(pygame.Rect):
  # example
  sprites = ["frog"]

  def __init__(self, GAME, sprite_type):
    self.sprite_type = sprite_type
    self.change_sprite_to(0)
    super().__init__((0, 0), self._surf.get_size())
    self.GAME = GAME

  def change_sprite_to(self, i):
    self.sprite = self.sprites[i]
    self.change_sprite(self.sprite_type, self.sprite)

  def change_sprite(self, sprite_type, sprite):
    self.surf = self.GAME.ENGINE.graphical_asset_handler[sprite_type][sprite]

  @property
  def sprite(self):
    return self._sprite

  @sprite.setter
  def sprite(self, new_sprite):
    self._sprite = new_sprite

  @property
  def surf(self):
    return self._surf

  @surf.setter
  def surf(self, new_surf):
    self._surf = new_surf
    self.size = self.surf.get_size()

  def drawable_rect(self):
    return self.GAME.ENGINE.camera.clip(self)

  # TODO add dunders
