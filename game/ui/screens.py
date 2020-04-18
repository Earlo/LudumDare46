from engine.constants import FUNCTIONCALLEVENT


def noGui(GAME):
    return []


def testGui(GAME):
    ui = [
        ["BUTTON", (0.2, 0.1), (0.1, 0.1), "test", [FUNCTIONCALLEVENT, GAME.START]],
        ["CARD", (0.2, 0.02), (0.7, 0.8), "Ilmarin kortti"],
    ]
    return ui
