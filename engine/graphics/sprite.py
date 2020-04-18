import pygame

from ..graphicalAssetHandler import GraphicalAssetHandler


class Sprite(pygame.Rect):
    # example
    frames = ["frog", "frog2"]
    graphic_layer = 0
    animationSpeed = 0
    frameInverted = False
    graphicalAssetHandler = GraphicalAssetHandler()

    def __init__(self, parent, asset_type):
        self.parent = parent
        self.asset_type = asset_type
        self.lastFrameUpdate = 0.0

        self.frame = 0
        self.animationSpeed = 0
        super().__init__((0, 0), self._surf.get_size())

    def draw(self):
        if self.animationSpeed > 0:
            if self.shouldUpdateFrame:
                self.next_frame()
        if self.frameInverted:
            self.parent.display(self.surf, self.topleft, None)
        else:
            self.parent.display(
                pygame.transform.flip(self.surf, True, False), self.topleft, None
            )

    def next_frame(self):
        self.frame = (self._frame + 1) % len(self.frames)
        ## TODO animation can fall out of synk, but works
        self.lastFrameUpdate = pygame.time.get_ticks()

    @property
    def timeperframe(self):
        return self._timePerFrame

    @property
    def animationSpeed(self):
        return self._animationSpeed

    @animationSpeed.setter
    def animationSpeed(self, s):
        self._animationSpeed = s
        if self.animationSpeed > 0:
            self._timePerFrame = 1000.0 / s
        else:
            self._timePerFrame = 1000

    # self.frame is the name of the image
    # self._frame is the index of the frame
    @property
    def frame(self):
        return self.frames[self._frame]

    @frame.setter
    def frame(self, i):
        self._frame = i
        self.surf = self.graphicalAssetHandler[self.asset_type][self.frame]

    @property
    def surf(self):
        return self._surf

    @surf.setter
    def surf(self, new_surf):
        self._surf = new_surf
        self.size = self.surf.get_size()

    @property
    def shouldUpdateFrame(self):
        return self._timePerFrame < (pygame.time.get_ticks() - self.lastFrameUpdate)

    def __repr__(self):
        try:
            return "Sprite {0} {1} at {2}".format(self.asset_type, self.frame, self)
        except AttributeError:
            return "{}".format(self)
