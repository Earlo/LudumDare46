from engine.constants import FUNCTIONCALLEVENT


def testGui(GAME):
  ui = [
       ["BUTTON", (.2, .1), (.1, .1), "test", [FUNCTIONCALLEVENT, GAME.START]]
  ]
  return ui
