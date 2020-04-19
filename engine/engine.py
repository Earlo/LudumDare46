import pygame
from game.game import Game

from .graphicalAssetHandler import GraphicalAssetHandler
from .singleton import Singleton
from .window.viewportHandler import ViewportHandler
from .constants import FUNCTIONCALLEVENT

# TODO localization system


class Engine(metaclass=Singleton):
    FPS = 60
    graphicalAssetHandler = GraphicalAssetHandler()
    viewportHandler = ViewportHandler()

    graphicalAssetHandler.load("sprites", colorkey_pos=(0, 0), flags=[pygame.RLEACCEL])
    graphicalAssetHandler.load("portrat", colorkey_pos=(0, 0))
    graphicalAssetHandler.load("bgr")

    def __init__(self):
        super().__init__()
        self.done = False
        self.clock = pygame.time.Clock()

        # TODO mouse object
        self.mouse = [pygame.mouse.get_pos(), False, [0, 0], None]

        self.GAME = Game(self)

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

            self.game_tick()
            self.viewportHandler.update_display()

            self.clock.tick(self.FPS)
            pygame.display.set_caption("FPS: {}".format(self.clock.get_fps()))

    def mousehandler(self, event):
        if event.button == 1:
            self.mouse[1] = True
            for obj in self.viewportHandler.viewPorts["GUI"].GUI:
                obj.on_click(event)
        # if event.type == pygame.MOUSEBUTTONUP:
        #  self.active_drag_obj = None
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #  if self.active_text_field is not None:
        #    self.active_text_field.inactivate()
        #    self.active_text_field = None

    def call_one_time_function(self, e):
        e.func(*e.param)

    def game_tick(self):
        self.GAME.tick()


def start():
    pygame.init()
    pygame.display.init()
    pygame.font.init()
    print("Running SDL {}".format(pygame.get_sdl_version()))

    global PROGRAM
    PROGRAM = Engine()
    PROGRAM.run()
    pygame.quit()
