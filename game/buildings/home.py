from .building import Building

class Home(Building):
    sprite = ["frog"]
    graphic_layer = 1

    def __init__(self, GAME, pos):
        super().__init__(GAME, pos)

    def deliver_olive(self,amount):
        self.game.resources['olives'] += amount
        return True



    