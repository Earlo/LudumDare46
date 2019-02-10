from engine.constants import FUNCTIONCALLEVENT


def noGui(GAME):
  return []


def testGui(GAME):
  ui = [
       ["BUTTON", (.2, .1), (.1, .1), "test", [FUNCTIONCALLEVENT, GAME.START]]
  ]
  return ui
