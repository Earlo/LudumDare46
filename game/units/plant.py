from engine.graphics.entity import Entity

from ..unit_logic import tasks

from ..units import unit


class Plant(Entity):
    stage = 0
    daframes = ["crop_0", "crop_1", "crop_2", "crop_3"]
    #sprite = frames[0]

    def __init__(self, GAME, pos, stg):
        super().__init__(pos)
        self.velocity = (0.0, 0.0)
        self.stage = stg
        self.growth = 0
        self.clock = GAME._ENGINE.clock
        self.animationSpeed = 10.0
        self.taskManager = GAME.taskManager
        self.game = GAME
        # self.growth_speed = 1.0 possible feature?

    def grow_plant(self):
        if self.stage < 3:
            if self.growth < 2000:
                self.growth += self.clock.get_time()
            else:
                self.growth = 0
                print("Plant grew a stage!")
                self.stage += 1
                if self.stage == 3:
                    self.taskManager.assign_task(tasks.HarvestOlives(self))
                    

    @property
    def frames(self):
        return [Plant.daframes[self.stage]]

    def harvest(self):
        if self.stage == 3:
            self.stage = 0
            self.growth = 0
            self.game.entities.append(unit.Unit(self.game, self.topleft))
            return True
        else:
            return False

    def tick(self, t):
        self.grow_plant()
        super().tick(t)
