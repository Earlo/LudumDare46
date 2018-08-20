
import sys
import os
import time

import pygame
from pygame.locals import *

from . import window
#from . import localization

#from ..Game.game import game
from .constants import FUNCTIONCALLEVENT

class Engine(window.WindowHandler):
  def __init__(self):
    super().__init__() #initialize window handler

    self.FPS = 60 #silky smooth 60 frames per second

    self.mouse = [pygame.mouse.get_pos() , False ,  [0,0] , None ]
    self.clock = pygame.time.Clock()
    self.additional_tasks = []
    self.done = False
    self.active_text_field = None
    self.active_drag_obj = None

    self.GAME = None


  def m_loop(self):
    while not self.done:
      self.mouse[0] = pygame.mouse.get_pos()
      self.mouse[1] = False
      #pygame.event.pump()
      for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT:
          self.done = True
        elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
          self.mousehandler(event)
        # TODO make custome event handler
        elif event.type == FUNCTIONCALLEVENT:
          event.func( *event.param )

      #self.update_display()
      self.clock.tick(self.FPS)
      pygame.display.set_caption("FPS: %i" % self.clock.get_fps())

  def STARTGAME(self):
    self.GAME = game(self)
    self.reset_GUI()

    self.function = self.geamloap

  def mousehandler(self, event):
    if event.button == 1: #TODO make mousehandler later, seriosly
      self.mouse[1] = True
      for obj in self.GUI: #check if any in game buttons are on_click
        obj.on_click(self,event) #self.mouse[0]
    if event.type == pygame.MOUSEBUTTONUP:
      self.active_drag_obj = None
    elif event.type == pygame.MOUSEBUTTONDOWN:
      if not self.active_text_field == None:
        self.active_text_field.inactivate()
        self.active_text_field = None


  def geamloap(self):
    self.GAME.game_step()
    self.drawGame()

  def OTfunction_wrapper(self,e):
    e.func( *e.param )


def start():
  pygame.init()
  pygame.display.init()
  pygame.font.init()

  global PROGRAM
  PROGRAM = Engine()
  PROGRAM.m_loop()
  pygame.quit()
