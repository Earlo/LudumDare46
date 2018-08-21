import pygame

from . import guiHandler
#from . import localization

#from ..Game.game import game
from .constants import FUNCTIONCALLEVENT

class Engine(guiHandler.GuiHandler):
  FPS = 60 #silky smooth 60 frames per second
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
      #pygame.event.pump()
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.done = True
        elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
          self.mousehandler(event)
        # TODO make custome event handler
        elif event.type == FUNCTIONCALLEVENT:
          self.call_one_time_function(event)

      #self.update_display()
      self.clock.tick(self.FPS)
      pygame.display.set_caption("FPS: %i" % self.clock.get_fps())

  def mousehandler(self, event):
    if event.button == 1: #TODO make mousehandler later, seriosly
      self.mouse[1] = True
      for obj in self.GUI:
        #self.mouse[0]
        obj.on_click(event)
    if event.type == pygame.MOUSEBUTTONUP:
      self.active_drag_obj = None
    elif event.type == pygame.MOUSEBUTTONDOWN:
      if not self.active_text_field is None:
        self.active_text_field.inactivate()
        self.active_text_field = None

  def call_one_time_function(self, e):
    e.func(*e.param)


  def STARTGAME(self):
    self.GAME = game(self)
    self.reset_GUI()

    self.function = self.geamloap

  def geamloap(self):
    self.GAME.game_step()
    self.drawGame()



def start():
  pygame.init()
  pygame.display.init()
  pygame.font.init()

  PROGRAM = Engine()
  PROGRAM.run()
  pygame.quit()
