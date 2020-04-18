from engine.graphics.entity import Entity


class Plant(Entity):
    stage = 0
    sprite = ["frog"]  # placeholder

    def __init__(self, GAME, pos, stg):
        super().__init__(pos)
        self.velocity = (0.0, 0.0)
        self.stage = stg
        self.growth = 0
        self.clock = GAME._ENGINE.clock
        # self.growth_speed = 1.0 possible feature?

    def grow_plant(self):
        if self.stage < 3:
            if self.growth < 2000:
                self.growth += self.clock.get_time()
            else:
                self.growth = 0
                self.stage += 1

    def harvest(self):
        if self.stage == 3:
            self.stage = 0
            self.growth = 0
            return True
        else:
            return False

    def tick(self, t):
        self.grow_plant()
        super().tick(t)
