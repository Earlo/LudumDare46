from engine.constants import FUNCTIONCALLEVENT


def noGui(GAME):
    return []


def testGui(GAME):
    ui = [
        ["BUTTON", (0.2, 0.1), (0.1, 0.1), "test", [FUNCTIONCALLEVENT, GAME.START]],
        ["BUTTON", (0.2, 0.1), (0.1, 0.3), "Test task manager", [FUNCTIONCALLEVENT, GAME.TEST_TASK_MANAGER]],
        ["CARD", (0.2, 0.02), (0.7, 0.8), "Ilmarin kortti"],
    ]
    return ui


def taskManagerGui(GAME, activeTasks=[], taskBuffer=[]):
    def task_to_card(task, index, colour=[]):
        card_height = 0.02
        card_margin = 0.02
        card_top = 1 - (card_height + card_margin) * (index + 1)
        return ["CARD", (0.2, 0.02), (0.7, card_top), task.title, colour]

    activeColour = [25, 20, 200]
    bufferColour = [200, 25, 20]
  
    allTasks = list(zip(activeTasks, [activeColour] * len(activeTasks)))\
        + list(zip(taskBuffer, [bufferColour] * len(taskBuffer)))

    task_cards = [
        task_to_card(t[1][0], t[0], t[1][1])
        for t in enumerate(allTasks)
    ]

    ui = [
        *task_cards
    ]
    return ui
