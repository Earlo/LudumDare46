class ExampleLevel:
    background = "checker_dark"

    def __init__(self, GAME):
        self.GAME = GAME
        self.GAME.load_bgr(self.background)
