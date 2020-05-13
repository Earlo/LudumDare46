class ExampleLevel:
    background = "plains"

    def __init__(self, GAME):
        self.GAME = GAME
        self.GAME.load_bgr(self.background)
