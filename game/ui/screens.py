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


def taskManagerGui(GAME, tasks=None):
    def task_to_card(task, index):
        card_height = 0.02
        card_margin = 0.02
        card_top = 1 - (card_height + card_margin) * (index + 1)
        return ["CARD", (0.2, 0.02), (0.7, card_top), task.title]

    task_cards = [
        task_to_card(t[1], t[0])
        for t in enumerate(tasks or GAME.tasks or [])
    ]
    ui = [
        *task_cards
    ]
    return ui
