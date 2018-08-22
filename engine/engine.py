import pygame
from game.main import Game

from . import guiHandler
# from . import localization
from .constants import FUNCTIONCALLEVENT


class Engine(guiHandler.GuiHandler):
  FPS = 60
  GAME = None

  def __init__(self):
    super().__init__()

    # TODO mouse object
    self.mouse = [pygame.mouse.get_pos(), False, [0, 0], None]
    self.clock = pygame.time.Clock()
    self.additional_tasks = []
    self.done = False

  def run(self):
    while not self.done:
      self.mouse[0] = pygame.mouse.get_pos()
      self.mouse[1] = False
      # pygame.event.pump()
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.done = True
        elif event.type in [pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP]:
          self.mousehandler(event)
        # TODO make custome event handler
        elif event.type == FUNCTIONCALLEVENT:
          self.call_one_time_function(event)

      # self.update_display()
      self.clock.tick(self.FPS)
      pygame.display.set_caption("FPS: %i" % self.clock.get_fps())

  def mousehandler(self, event):
    if event.button == 1: # TODO make mousehandler later, seriosly
      self.mouse[1] = True
      for obj in self.GUI:
        # self.mouse[0]
        obj.on_click(event)
    if event.type == pygame.MOUSEBUTTONUP:
      self.active_drag_obj = None
    elif event.type == pygame.MOUSEBUTTONDOWN:
      if self.active_text_field is not None:
        self.active_text_field.inactivate()
        self.active_text_field = None

  def call_one_time_function(self, e):
    e.func(*e.param)

  # TODO move these
  def STARTGAME(self):
    self.GAME = Game(self)
    self.reset_GUI()
    self.function = self.game_loop

  def game_loop(self):
    self.GAME.tick()
    self.draw_game()


def start():
  pygame.init()
  pygame.display.init()
  pygame.font.init()

  PROGRAM = Engine()
  PROGRAM.run()
  pygame.quit()
