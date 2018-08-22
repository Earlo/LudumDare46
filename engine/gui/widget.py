import pygame


class Widget:
  def __init__(self):
    self.parent = None

  # adjust parents
  def adjust_p(self, p_surf, parent=None):
    if p_surf is not None:
      self.parent_surf = p_surf
    if parent is not None:
      self.parent = parent

  def adjust_r(self):
    self.surf = pygame.Surface((self.relative_cordinate(self.parent_surf, *self.rsurf)))
    self.rect = self.surf.get_rect()
    self.pos = self.relative_cordinate(self.parent_surf, *self.rpos)
    if self.parent is not None:
      self.c_rect = self.rect.copy()
      self.c_rect.topleft = [x + y for x, y in zip(self.pos, self.parent.absolute_position())]
    else:
      self.c_rect = self.rect.copy()
      self.c_rect.topleft = self.pos

  def absolute_position(self):
    return self.c_rect.topleft

  def relative_position(self):
    return self.pos

  def blit(self, update=True, surf=None, area=None):
    if surf is None:
      surf = self.surf
    if area is not None:
      pos = [x + y for x, y in zip(self.relative_position(), area.topleft)]
    else:
      pos = self.relative_position()

    self.parent_surf.blit(surf, pos, area)

    if update:
      if area is None:
        area = self.rect.copy()
        area.topleft = pos
      else:
        area.move_ip(self.relative_position())
      # if self.parent is None: # send event to main screen handle
      # events.blit_request(area, self.parent_surf)   # edit later
        # events.blit_request(self.c_rect, self.parent_surf) # for debugging
      # else: # send message forward to parent
      # self.parent.blit( area = area)

  # returs point relative to scree size
  def relative_cordinate(self, parent, w, h):
    pw, ph = parent.get_size()
    return[int(w * pw), int(h * ph)]

  def RelativeHeight(self, parent, h):
    ph = parent.get_height()
    return int(h * ph)

  def RelativeWidth(self, parent, w, h):
    pw = parent.get_width()
    return int(w * pw)

  def send_fucntion_request(self, func):
    # TODO Rename
    CALLTYPE = func.pop(0)
    f = func.pop(0)
    signal = pygame.event.Event(CALLTYPE, {"func": f, "param": func})
    pygame.event.post(signal)

  def debug(self):
    print("values for this widget", self, "are:\n", self.pos, "\n", self.rect, "\n", self.c_rect)
