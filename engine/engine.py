import pygame
from game.game import Game

from .graphicalAssetHandler import GraphicalAssetHandler

from .singleton import Singleton
from .window.viewportHandler import ViewportHandler
from .constants import FUNCTIONCALLEVENT, nothing
# TODO localization system

from .constants import FUNCTIONCALLEVENT
from .gui.button import Button


class Engine(metaclass=Singleton):
  FPS = 60
  GAME = None
  graphicalAssetHandler = GraphicalAssetHandler()
  viewportHandler = ViewportHandler()

  def __init__(self):
    super().__init__()
    self.done = False
    self.clock = pygame.time.Clock()
    self.on_tick_action = nothing

    # TODO mouse object
    self.mouse = [pygame.mouse.get_pos(), False, [0, 0], None]

    # TODO remove
    self.test_gui()

  def test_gui(self):
    self.viewportHandler.viewPorts['GUI'].GUI = [Button(self.viewportHandler.viewPorts['GUI'],
                                (0.2, 0.1), (.1, 0.1),
                                "tesets", [FUNCTIONCALLEVENT, self.STARTGAME])]
    self.viewportHandler.viewPorts['GUI'].refresh_GUI()
    self.viewportHandler.blit_GUI()

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

      self.on_tick_action()
      self.viewportHandler.update_display()

      self.clock.tick(self.FPS)
      pygame.display.set_caption("FPS: {}".format(self.clock.get_fps()))

  def mousehandler(self, event):
    # TODO make mousehandler
    if event.button == 1:
      self.mouse[1] = True
      for obj in self.GUI:
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
    self.on_tick_action = self.game_tick

  def game_tick(self):
    self.window.fill((0, 0, 255))
    self.GAME.tick()
    # DEBUG
    self.camera.debug_move()


def start():
  pygame.init()
  pygame.display.init()
  pygame.font.init()
  print("Running SDL {}".format(pygame.get_sdl_version()))

  global PROGRAM
  PROGRAM = Engine()
  load_assets()
  PROGRAM.run()
  pygame.quit()


def load_assets():
  # TODO replace folder names with constants
  PROGRAM.graphicalAssetHandler.load('sprites',
                                     colorkey_pos=(0, 0),
                                     flags=[pygame.RLEACCEL])

  PROGRAM.graphicalAssetHandler.load('portrat',
                                     colorkey_pos=(0, 0))

  PROGRAM.graphicalAssetHandler.load('bgr')
